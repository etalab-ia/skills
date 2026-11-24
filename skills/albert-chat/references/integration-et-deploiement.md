# Intégration, configuration et déploiement

## Sommaire

- [Choisir le mode d'intégration](#choisir-le-mode-dintégration)
- [Variables d'environnement et portée](#variables-denvironnement-et-portée)
- [Déployer un fork sur Scaleway](#déployer-un-fork-sur-scaleway)
- [Personnalisation sûre et validation](#personnalisation-sûre-et-validation)

---

## Choisir le mode d'intégration

| Critère | Iframe via `/embed.js` (recommandé) | Web Component `<albert-chat>` |
|---------|-------------------------------------|-------------------------------|
| Isolation DOM & CSS | Complète (document `/embed` séparé) | CSS isolé par Shadow DOM uniquement |
| Isolation JavaScript & stockage | Complète sur origine distincte + `sandbox` + `Permissions-Policy` | **Aucune** : exécution dans les privilèges de la page hôte |
| Variable serveur associée | `EMBED_ALLOWED_PARENTS` (`CSP: frame-ancestors`) | `WIDGET_ALLOWED_ORIGINS` (CORS sur `/api/chat`) |
| Rechargement après modif d'env | **Rebuild + redéploiement** requis | Redémarrage du conteneur suffit |
| Directives CSP côté page hôte | `script-src`, `frame-src` | `script-src`, `style-src`, `connect-src` |

### Intégration Iframe

```html
<script
  src="https://<hote>/embed.js"
  referrerpolicy="strict-origin-when-cross-origin"
  defer
></script>
```

- `/embed.js` crée une seule iframe `sandbox="allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"` et refuse caméra, micro et géolocalisation (`allow` + en-tête `Permissions-Policy`).
- Le redimensionnement repose sur `postMessage` ciblant l'origine lue dans `document.referrer` grâce à `referrerpolicy="strict-origin-when-cross-origin"`. Si la page hôte impose `referrerpolicy="no-referrer"`, l'origine cible retombe sur `"*"` (seul l'état ouvert/fermé est transmis).
- Sur `/embed`, l'en-tête `Content-Security-Policy: frame-ancestors 'self' <EMBED_ALLOWED_PARENTS>` contrôle qui peut encadrer le widget.

### Intégration Web Component

```html
<script type="module" src="https://<hote>/widget.js"></script>
<albert-chat api-url="https://<hote>/api/chat"></albert-chat>
```

- `pnpm build` (via `pnpm build:widget`) génère `public/widget.js`, `public/widget.css` et `public/widget.js.LEGAL.txt`. En cas d'auto-hébergement sur la page hôte, copier ces **trois fichiers ensemble** et renseigner `api-url` (URL HTTP(S) sans identifiants ni fragment).
- Événements DOM émis (`bubbles: true, composed: true`) : `open-change` (`detail.open`) et `widget-error` (`detail.message`).
- Éviter plusieurs instances sur une même page (positionnement fixe en bas à droite). Modifier `api-url` ou retirer l'élément annule la requête en cours et réinitialise la conversation.
- Préférer une version figée ou auto-hébergée si la page hôte héberge des données sensibles : le composant s'exécute dans son origine JavaScript.

---

## Variables d'environnement et portée

| Variable | Obligatoire | Défaut | Prise d'effet | Contraintes et pièges |
|----------|-------------|--------|---------------|-----------------------|
| `ALBERT_API_KEY` | oui | — | démarrage / requête | Côté serveur uniquement. Clé dédiée au projet. |
| `ALBERT_COLLECTION_IDS` | oui | — | requête | Entiers positifs séparés par virgule. Chaîne vide ou `0` refusée (échec fermé, jamais « toutes les collections »). |
| `ALBERT_BASE_URL` | non | `https://albert.api.etalab.gouv.fr` | requête | URL valide requise ; une valeur vide `""` fait échouer `/api/chat`. |
| `ALBERT_CHAT_MODEL` | non | `gpt-oss-120b` | requête | Doit être un `id` canonique retourné par `GET /v1/models` d'Albert. |
| `EMBED_ALLOWED_PARENTS` | si iframe | vide (`'self'` seul) | **build / chargement config** | Origines nues `http(s)` séparées par virgule. Chemins, query et jokers (`*.gouv.fr`) sont écartés au parsing. |
| `WIDGET_ALLOWED_ORIGINS` | si Web Component | vide (même origine) | **par requête** | Origines nues séparées par virgule. Aucun joker `*`, aucune origine `null`. CORS vérifie `Host` + `X-Forwarded-Proto`. |
| `ABUSE_MAX_PER_CLIENT` | non | `10` | démarrage du processus | Plafond par IP (`X-Real-IP` puis 1re IP de `X-Forwarded-For`) et par fenêtre. |
| `ABUSE_CLIENT_WINDOW_MS` | non | `60000` | démarrage du processus | Durée de la fenêtre par client en ms. |
| `ABUSE_MAX_PER_DAY` | non | `500` | démarrage du processus | Plafond global par instance. Multiplié si `max_scale > 1` (compteurs en mémoire). |

---

## Déployer un fork sur Scaleway

### 1. Paramètres GitHub Actions du fork

Dans `Settings → Secrets and variables → Actions` du fork :

- **Secrets obligatoires pour `ci-cd.yml`** : `SCW_ACCESS_KEY`, `SCW_SECRET_KEY`, `SCW_ORGANIZATION_ID`, `SCW_PROJECT_ID`.
- **Variables de dépôt obligatoires (les 5)** :
  - `SCW_CONTAINER_ID`
  - `SCW_NAMESPACE_ID`
  - `SCW_IMAGE_BASE` (ex. `rg.fr-par.scw.cloud/<namespace>/<image>`, sans `:tag`)
  - `SCW_REGISTRY_HOST` (ex. `rg.fr-par.scw.cloud`)
  - `SCW_REGION` (ex. `fr-par`)

Ne pas omettre ces 5 variables : les replis dans `.github/workflows/ci-cd.yml` ciblent le démonstrateur ANSSI et provoquent un échec trompeur à l'étape *« Verify the Scaleway project and container »*.

Workflows annexes :
- `anssi-sync.yml` est neutralisé hors propriétaire `etalab-ia` (`github.repository_owner == 'etalab-ia'`).
- `release-please.yml` peut être supprimé ou laissé inactif sur un fork dédié à un déploiement unique.

### 2. Provisionnement du conteneur Scaleway

- Définir **`HOSTNAME=0.0.0.0`** dans les variables d'environnement du conteneur (sans quoi le serveur Next standalone écoute sur l'identifiant du conteneur non résolu par le DNS Scaleway et échoue le contrôle sur le port `8080`, même si un test Podman local passe).
- Ne **jamais** ajouter `PORT` dans les variables d'environnement du conteneur : `PORT` est réservé par Scaleway et se configure via le champ `port` (`8080`) de la ressource conteneur.
- Pour les appels directs à l'API Scaleway Containers (`/containers/v1beta1/...`) : le champ de l'image est `image` (pas `registry_image`), les ressources sont `memory_limit_bytes` et `mvcpu_limit`, et `timeout` est une chaîne protobuf (`"300s"`).
- `ALBERT_API_KEY` est stockée en variable secrète côté Scaleway ; l'API la restitue hachée en argon2id (comportement normal).
- Avec `min_scale: 0`, le conteneur se met en veille entre deux sessions : préchauffer avec une question avant toute démo.

---

## Personnalisation sûre et validation

### Ce qui se modifie dans le fork

- `components/widget/assistant-modal.tsx` : libellé d'en-tête (`"Assistant ANSSI"`), `aria-label` du bouton d'ouverture/fermeture.
- `components/widget/thread.tsx` : paragraphe d'accueil dans `EmptyState` et tableau `SUGGESTIONS`.
- `app/(site)/page.tsx` : contenu de la page d'accueil / démonstration DSFR (ou remplacement par une redirection/page minimale).
- `lib/rag/prompt.ts` : contexte de rôle dans `SYSTEM_PROMPT`, **en conservant** les règles de citation `[n]` et l'interdiction du Markdown (`*`, `#`, `|`).

### Ce qu'il faut préserver

- `WIDGET_TAG = "albert-chat"` (`widget/element.tsx`) et les identifiants du chargeur `public/embed.js` (`__anssiWidget`, `data-anssi-widget`, `data-anssi-auto-mount`, `EMBED_MESSAGE_SOURCE = "anssi-widget"`).
- La séparation des layouts : `app/(site)/layout.tsx` (DSFR) et `app/(embed)/layout.tsx` (Tailwind pur sans DSFR). Un import DSFR dans `(embed)` casse la mise en forme des boutons et paragraphes du widget.

### Vérification locale complète avant mise en ligne

```bash
pnpm install
pre-commit install --install-hooks
pnpm check:config -- --env-file .env.local
pnpm lint
pnpm typecheck
pnpm test
pnpm build
pnpm exec playwright install chromium   # au premier passage
pnpm test:browser
```
