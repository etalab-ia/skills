# Contrat de conteneur et spécificités par stack

## Sommaire

- [Contrat minimal pour Scaleway Serverless Containers](#contrat-minimal-pour-scaleway-serverless-containers)
- [Protocole de test local avant premier push](#protocole-de-test-local-avant-premier-push)
- [Notes par stack FDE](#notes-par-stack-fde)
  - [Next.js (App Router standalone)](#nextjs-app-router-standalone)
  - [Python / FastAPI (uvicorn)](#python--fastapi-uvicorn)
  - [Python / Streamlit](#python--streamlit)
- [Hygiène d'image et robots.txt](#hygiène-dimage-et-robotstxt)

---

## Contrat minimal pour Scaleway Serverless Containers

Toute image destinée à Scaleway Serverless Containers doit respecter ces sept règles :

1. **Architecture `linux/amd64`** : la plateforme exécute des images `amd64`. Sur poste Apple Silicon (M1–M4), passer explicitement `--platform linux/amd64` à `docker build` lors du premier push local (les runners GitHub Actions `ubuntu-24.04` sont nativement `amd64`).
2. **Écoute sur `0.0.0.0`** : le processus applicatif doit s'attacher à toutes les interfaces (`0.0.0.0`), jamais à `127.0.0.1` ni au nom d'hôte du conteneur.
3. **`HOSTNAME=0.0.0.0` dans l'environnement du conteneur** : le moteur d'exécution renseigne `HOSTNAME` avec l'identifiant interne du conteneur, que le DNS de Scaleway ne résout pas. Tout runtime qui lit `HOSTNAME` comme adresse d'écoute (notamment Next.js standalone) semble démarrer (`Ready`) mais reste injoignable.
4. **Ne jamais définir `PORT` côté Scaleway** : le nom `PORT` est réservé par la plateforme. Fixer le port via l'attribut `port` de la ressource conteneur (`8080` par défaut) et configurer l'application pour écouter sur ce port (`ENV PORT=8080` dans le `Dockerfile` ou drapeau `--port 8080` dans `CMD`).
5. **Utilisateur non-root** : créer un utilisateur système dédié dans l'étape finale (`USER appuser`, UID/GID `1001`) et limiter les permissions aux fichiers strictement nécessaires.
6. **Build hermétique sans secrets** : aucun vrai secret (`API_KEY`, mot de passe, jeton) ne doit être requis pendant `docker build` ni copié dans une couche. Si le framework exige qu'une variable soit non vide au build, passer une valeur factice dans l'étape `build` du `Dockerfile` (`ENV MY_API_KEY=build-placeholder`) et injecter la vraie valeur au runtime via `secret-environment-variables`.
7. **`.dockerignore` strict** : exclure `.git`, `.github`, `.env*`, `node_modules`, `.venv`, `__pycache__`, `.next`, `coverage` et journaux locaux afin d'éviter toute fuite de secret ou contexte de build obèse.

---

## Protocole de test local avant premier push

Un test `docker run` ou `podman run` classique masque le piège `HOSTNAME`, car le moteur local résout l'identifiant du conteneur dans `/etc/hosts`. Pour démasquer le bug avant de pousser sur Scaleway, forcer un `HOSTNAME` non résoluble :

```bash
docker build --platform linux/amd64 --pull -t poc-local:test .
docker run --rm -p 8080:8080 \
  -e HOSTNAME=0.0.0.0 \
  --env-file .env.local \
  poc-local:test
```

Vérifier ensuite dans un second terminal que l'application répond bien sur `http://127.0.0.1:8080/` (et sur la route de santé configurée dans la CI) ainsi que `http://127.0.0.1:8080/robots.txt`.

Si le serveur refuse de démarrer ou échoue quand on lance le conteneur **sans** `-e HOSTNAME=0.0.0.0` et **avec** `--hostname unresolvable-scaleway-id`, c'est la preuve que `HOSTNAME=0.0.0.0` est indispensable dans l'environnement Scaleway (ou directement en dur dans le `CMD`).

---

## Notes par stack FDE

### Next.js (App Router standalone)

Modèle directement éprouvé sur `etalab-ia/albert-chat` :

- Activer `output: "standalone"` dans `next.config.ts` pour produire `.next/standalone/server.js` avec le sous-ensemble minimal de dépendances tracées.
- **Node 26 et `pnpm`** : Node 26 ne fournit plus Corepack. Installer la version épinglée de `pnpm` explicitement (`RUN npm install --global pnpm@<version>`).
- **Dossier `public/`** : ne copier `/app/public` dans l'étape finale que si le dépôt versionne réellement des fichiers dans `public/` (un dossier vide ne survit pas au `git checkout` en CI et fait échouer `COPY`).
- **Variables au build vs au runtime** : toute variable `NEXT_PUBLIC_*` ou lue au chargement de `next.config.ts` (comme des en-têtes CSP statiques) est figée au **build** et impose un rebuild + redéploiement. Les clés serveur lues dans les Route Handlers sont lues au **runtime**.
- **Anti-indexation** : ajouter `app/robots.ts` renvoyant `{ rules: { userAgent: "*", disallow: "/" } }`.

```dockerfile
FROM node:26-slim AS deps
WORKDIR /app
RUN npm install --global pnpm@11.18.0
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
RUN pnpm install --frozen-lockfile

FROM node:26-slim AS build
WORKDIR /app
RUN npm install --global pnpm@11.18.0
ENV NEXT_TELEMETRY_DISABLED=1
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN pnpm build

FROM node:26-slim AS run
WORKDIR /app
ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1
ENV HOSTNAME=0.0.0.0
ENV PORT=8080

RUN groupadd --system --gid 1001 nodejs \
  && useradd --uid 1001 --gid nodejs --shell /usr/sbin/nologin nextjs

COPY --from=build --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=build --chown=nextjs:nodejs /app/.next/static ./.next/static
COPY --from=build --chown=nextjs:nodejs /app/public ./public

USER nextjs
EXPOSE 8080
CMD ["node", "server.js"]
```

Définir tout de même `environment-variables.HOSTNAME=0.0.0.0` côté Scaleway en défense en profondeur : la plateforme peut injecter `HOSTNAME` au démarrage du conteneur et écraser `ENV HOSTNAME` du `Dockerfile`.

### Python / FastAPI (uvicorn)

- Écouter explicitement sur `0.0.0.0` et le port `8080` : `uvicorn app.main:app --host 0.0.0.0 --port 8080 --proxy-headers`.
- L'option `--proxy-headers` est indispensable pour que FastAPI lise `X-Forwarded-Proto` et `X-Real-IP` transmis par la passerelle TLS de Scaleway (génération d'URLs `https://`, journalisation IP).
- Conserver **`--workers 1`** en POC (`max_scale: 1`, mémoire bornée à 512 Mio) afin d'éviter la duplication de mémoire et des compteurs en mémoire.
- Exposer une route légère `GET /health` renvoyant `200 {"status": "ok"}` sans appel amont coûteux (LLM, API externe), et servir `GET /robots.txt` avec `User-agent: *\nDisallow: /\n`.
- Utiliser une image multi-étapes (`uv` ou `pip` dans un `.venv` copié dans `python:3.12-slim`) exécutée par un utilisateur non-root.

```dockerfile
FROM python:3.12-slim AS build
WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:0.7.12 /uv /usr/local/bin/uv
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project
COPY . .
RUN uv sync --frozen --no-dev

FROM python:3.12-slim AS run
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"

RUN groupadd --system --gid 1001 app \
  && useradd --uid 1001 --gid app --shell /usr/sbin/nologin appuser

COPY --from=build --chown=appuser:app /app/.venv ./.venv
COPY --from=build --chown=appuser:app /app/app ./app

USER appuser
EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers"]
```

### Python / Streamlit

- Lancer Streamlit en mode headless, lié à `0.0.0.0:8080` et sans télémétrie :

```dockerfile
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8080", "--server.headless=true", "--browser.gatherUsageStats=false"]
```

- **Route de santé native** : Streamlit expose `/_stcore/health` (renvoie `ok` en HTTP 200), pratique pour le contrôle de santé CI.
- **Limites WebSockets et scale-to-zero** : Streamlit maintient une session WebSocket en mémoire de l'instance. Rester impérativement à **`max-scale=1`** (sinon les requêtes d'une même session basculent entre instances et réinitialisent l'interface). Avec `min-scale=0`, une inactivité prolongée coupe la session et déclenche une reconnexion au réveil ; pendant une démonstration critique, on peut passer temporairement à `min-scale=1` puis revenir à `min-scale=0` après la séance.
- **Anti-indexation** : Streamlit ne sert pas de `robots.txt` personnalisé par défaut ; si le POC est public, ajouter `<meta name="robots" content="noindex, nofollow">` ou placer un léger proxy statique/en-tête `X-Robots-Tag: noindex, nofollow`.

---

## Hygiène d'image et robots.txt

- **Images de base épinglées et mises à jour** : activer Dependabot sur l'écosystème `docker` (avec délai de maturité de 7 jours, cf. `.github/dependabot.yml`) pour suivre les correctifs de sécurité de l'image de base.
- **Taille d'image** : plus l'image est lourde, plus le démarrage à froid (`min_scale: 0`) est long. Rester sur des images `-slim` ou distroless et éviter d'embarquer des modèles ML ou des jeux de données volumineux dans l'image.
- **Exclusion des moteurs de recherche** : pour tout POC exposé sur Internet, renvoyer `User-agent: *\nDisallow: /\n` sur `/robots.txt` et, si possible, l'en-tête HTTP `X-Robots-Tag: noindex, nofollow`.
