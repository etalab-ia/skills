---
name: scaleway-poc-deploy
description: "Accompagner un FDE (Forward Deployed Engineer) dans le déploiement complet d'un POC HTTP sans état sur Scaleway Serverless Containers : cadrage d'exposition et garde-fous (fr-par, robots.txt, échelle 0–1, choix public vs protégé), contrat de conteneur multi-stack (Next.js standalone, Python/FastAPI, Streamlit), provisionnement Jour 0 par CLI scw et gh (projet dédié, IAM applicatif moindre privilège, registre privé, conteneur), pipeline CI/CD GitHub Actions reproductible, dépannage des pièges Scaleway et démontage propre en fin de POC. À utiliser dès que l'utilisateur veut déployer, conteneuriser, automatiser, sécuriser, diagnostiquer ou supprimer un POC sur Scaleway Serverless Containers. Complémentaire d'albert-chat (spécifique au corpus et au fork albert-chat) et de securite-developpement (durcissement avant passage en production)."
---

# Scaleway POC Deploy — Guide FDE Serverless Containers

Déployer rapidement un POC HTTP **sans état** sur **Scaleway Serverless Containers** (`fr-par`, mise en veille automatique `min_scale: 0`, plafond `max_scale: 1`) sans tomber dans les écueils opérationnels de la plateforme ni laisser de ressources orphelines après la démonstration.

## Périmètre et critères d'éligibilité

- **Adapté** : application web, API HTTP, interface de démonstration ou serveur MCP **stateless**, image Linux `amd64`, trafic intermittent ou démonstrations métier, tolérance à un démarrage à froid.
- **Hors périmètre** (sortir de cette skill) :
  - **Base de données ou stockage persistant** : un conteneur Serverless n'offre aucun disque durable entre instances ; prévoir un service managé externe hors de cette skill.
  - **Connexions longues ou GPU** : préférer une Instance CPU/GPU ou Kapsule si le POC requiert des WebSockets persistants critiques, des tâches longues au-delà du `timeout` HTTP ou un GPU.
  - **Passage en production** : un POC n'est pas un service en production ; basculer sur [`securite-developpement`](../securite-developpement/SKILL.md) (durcissement complet, journalisation, CSP stricte, authentification pérenne, haute disponibilité) avant toute ouverture durable.

---

## Workflow FDE en 5 étapes

**L'ordre compte** : verrouiller la décision d'exposition avant de déployer, pousser une première image `linux/amd64` avant de créer le conteneur, puis câbler la CI/CD avec une identité IAM restreinte au seul projet du POC.

### 1. Cadrer l'exposition et les garde-fous avant tout déploiement

Avant de créer la moindre ressource, trancher explicitement le niveau d'exposition du POC et appliquer les garde-fous par défaut :

- **Souveraineté et indexation** : déployer en région **`fr-par`** et servir un `robots.txt` bloquant l'indexation (`User-agent: *` / `Disallow: /`).
- **Maîtrise des coûts et de l'état** : démarrer avec **`min-scale=0`**, **`max-scale=1`**, `memory-limit-bytes=536870912` (512 Mio), `mvcpu-limit=500`, `timeout=300s` et **`https-connections-only=true`**. Limiter `max-scale=1` borne la facture et préserve la cohérence des éventuels compteurs anti-abus en mémoire.
- **Hygiène des secrets** : aucune clé d'API côté navigateur ni dans les couches Docker ; stocker tous les secrets applicatifs en `secret-environment-variables` côté Scaleway.
- **Choix obligatoire d'accès (porte de décision)** :
  1. **Public (`privacy=public`)** — acceptable **uniquement** pour une démonstration sans donnée sensible, accompagnée de plafonds anti-abus et d'un plafond journalier côté serveur (en particulier si le POC appelle une API LLM payante).
  2. **Protégé par IAM Scaleway (`privacy=private`)** — adapté aux **API, backends et serveurs MCP** appelés par un client technique ou un proxy : la passerelle Scaleway rejette toute requête sans en-tête `X-Auth-Token` valide (clé d'une application IAM dotée de `ContainersPrivateAccess`). Ne pas utiliser les anciens jetons JWT (`scw container token create`), désormais dépréciés.
  3. **Protégé côté application ou mandataire authentifiant** — obligatoire pour une **interface web consultée depuis un navigateur** avec données sensibles ou accès restreint (un navigateur ne peut pas injecter nativement `X-Auth-Token`) : activer une authentification applicative (Basic Auth dédiée au POC, OIDC/ProConnect ou reverse proxy authentifiant).

### 2. Préparer un conteneur conforme au contrat Scaleway

Respecter le contrat minimal suivant quel que soit le langage ou le framework :

- Image **multi-étapes**, utilisateur **non-root**, architecture **`linux/amd64`**.
- Écoute explicite sur **`0.0.0.0`** et sur le port déclaré sur la ressource conteneur (`8080` par défaut).
- Définir **`HOSTNAME=0.0.0.0`** dans les variables d'environnement du conteneur (obligatoire pour Next.js standalone et tout serveur qui lit `process.env.HOSTNAME`).
- Ne **jamais** déclarer la variable d'environnement **`PORT`** dans Scaleway : ce nom est réservé ; régler le port via le paramètre `port` du conteneur.
- Build **hermétique** : ne jamais injecter de vrai secret à l'étape `docker build` (utiliser une valeur factice si le build exige la présence d'une variable).
- Valider localement avec un test simulant un `HOSTNAME` non résoluble avant de pousser l'image.

Contrat complet, notes Next.js standalone / Python FastAPI / Streamlit et protocole de test local : [`references/conteneur-et-stacks.md`](references/conteneur-et-stacks.md).

### 3. Provisionner les ressources et câbler GitHub (Jour 0)

Utiliser les CLI officiels **`scw` (`v2.65.2`)** et **`gh`** (sans gestion d'état Terraform à héberger pour un POC) :

1. **Isoler le POC dans un projet Scaleway dédié** (`scw account project create`) pour cloisonner le rayon d'impact, la facturation et le démontage. Si le FDE ne dispose pas du droit `ProjectManager`, cibler un projet pré-créé existant et isoler par namespaces et application IAM dédiés.
2. **Créer un namespace de registre privé** (`scw registry namespace create ... is-public=false`) — attention : le nom est **globalement unique dans la région** et **immuable**. Construire (`--platform linux/amd64`) et pousser la première image `sha-<SHA>` **avant** de créer le conteneur (`image` est obligatoire à la création).
3. **Créer le namespace et le conteneur Serverless** (`scw container namespace create` puis `scw container container create ... --wait`).
4. **Créer une identité IAM dédiée à la CI/CD** (`scw iam application create` + `scw iam policy create` scopée au seul `SCW_PROJECT_ID` avec `ContainersFullAccess` et `ContainerRegistryFullAccess` + `scw iam api-key create`). Attendre jusqu'à **1 minute** la propagation de la politique IAM.
5. **Configurer GitHub Actions** en séparant strictement les **4 Secrets** (`SCW_ACCESS_KEY`, `SCW_SECRET_KEY`, `SCW_ORGANIZATION_ID`, `SCW_PROJECT_ID`) des **5 Variables** (`SCW_CONTAINER_ID`, `SCW_NAMESPACE_ID`, `SCW_IMAGE_BASE`, `SCW_REGISTRY_HOST`, `SCW_REGION`).

Runbook complet Jour 0, mise à jour de secrets, domaine personnalisé et démontage : [`references/provisionnement-et-teardown.md`](references/provisionnement-et-teardown.md).

### 4. Automatiser les déploiements avec GitHub Actions (Jour 2)

Partir du modèle prêt à adapter [`assets/ci-cd-scaleway.yml`](assets/ci-cd-scaleway.yml), qui reprend les garanties validées en production sur `etalab-ia/albert-chat` :

- **Conditionnement qualité** : le job `deploy` ne tourne que sur `push` vers `main` après succès de `verify` (lint, types, tests, build), avec `concurrency.cancel-in-progress: false` pour ne jamais interrompre un déploiement en cours.
- **Épinglage strict** : toutes les actions GitHub épinglées par **SHA de commit complet** (`actions/checkout`, `scaleway/action-scw`) et version du CLI `scw` explicitement épinglée (`v2.65.2`), avec Dependabot actif sur `docker` et `github-actions` (délai de maturité 7 jours).
- **Échec rapide sans IDs en repli** : afficher les variables résolues et échouer dès le début si `SCW_CONTAINER_ID`, `SCW_NAMESPACE_ID` ou `SCW_IMAGE_BASE` sont vides. Ne jamais laisser d'identifiants Scaleway en dur en valeur de repli dans un dépôt destiné à être cloné ou forké.
- **Vérification de portée IAM** : une clé applicative ne peut pas lire les API compte/organisation ; vérifier `organization_id` et `project_id` via `scw container namespace get` puis `namespace_id` via `scw container container get`.
- **Déploiement immuable et contrôle post-rollout** : tag `sha-${{ github.sha }}` (jamais `:latest`), `scw container container update ... --wait`, assertion de `image` et `status == "ready"`, puis contrôles HTTP `curl --fail --max-time 45` avec réessais sur `public_endpoint` (qui inclut déjà `https://`).

### 5. Exploiter, diagnostiquer et démonter en fin de POC (Jour N)

- **Avant une démonstration en direct** : avec `min_scale: 0`, envoyer une requête de chauffe quelques secondes avant de partager l'écran pour absorber le démarrage à froid.
- **Diagnostic** : inspecter l'état (`scw container container get`) et les journaux (`scw container container logs <id> region=fr-par`).
- **Renommage** : les noms de namespace, registre et conteneur Scaleway sont **immuables** ; renommer implique de recréer les ressources (nouveaux UUIDs, nouvelle URL `public_endpoint`, mise à jour des variables GitHub).
- **Fin de POC** : exécuter la procédure de démontage complet (`references/provisionnement-et-teardown.md`) dès la fin de l'expérimentation afin d'éviter toute surface exposée oubliée ou facturation résiduelle.

Catalogue détaillé des pièges et résolutions : [`references/pieges-et-depannage.md`](references/pieges-et-depannage.md).

---

## Diagnostic rapide des pièges connus

| Symptôme | Cause vérifiée | Correction |
|---|---|---|
| Le conteneur affiche `Ready` puis Scaleway signale *« unable to start OR is not listening on port 8080 »* | Le serveur écoute sur `HOSTNAME` (ID de conteneur non résolu par le DNS Scaleway ; masqué en local par Docker/Podman) | Définir `HOSTNAME=0.0.0.0` dans l'environnement du conteneur et écouter sur `0.0.0.0` |
| Scaleway refuse la variable d'environnement `PORT` | `PORT` est un nom réservé par Serverless Containers | Supprimer `PORT` de l'environnement Scaleway et configurer `port=8080` sur la ressource |
| Crash `exec format error` au démarrage après un push local depuis macOS | Image construite en `linux/arm64` sur Apple Silicon alors que Scaleway exécute `linux/amd64` | Reconstruire avec `docker build --platform linux/amd64` |
| Le pipeline passe au vert mais l'ancienne image tourne encore | Oubli de `--wait` sur `scw container container update` ou utilisation d'un tag mutable `:latest` | Passer `--wait`, utiliser des tags `sha-<SHA>` et vérifier `image` + `status == "ready"` |
| Échec `curl` sur `https://https://...` dans la CI | `public_endpoint` renvoyé par `scw container container get` contient déjà `https://` | Utiliser `"${endpoint}/health"` directement sans préfixer `https://` |
| Erreur `403` / `404` à la vérification de portée juste après la création IAM | Délai de propagation IAM (jusqu'à 1 min), ou `SCW_CONTAINER_ID`/`SCW_NAMESPACE_ID` obsolètes après recréation | Attendre 60 s après `scw iam policy create` ; vérifier les 5 variables GitHub et les UUIDs courants |
| Les secrets relus via l'API apparaissent comme des empreintes `argon2id` | Comportement normal de l'API Scaleway pour `secret_environment_variables` | Ne rien corriger : le secret n'est pas corrompu, il est injecté en clair dans le conteneur |
| Erreur de drapeau `unknown flag` entre création et mise à jour HTTPS | `create` attend `https-connections-only` (pluriel) ; `update` attend `https-connection-only` (singulier) en CLI `v2.65.2` | Adapter le nom du paramètre selon la sous-commande |

---

## Références, modèle et skills complémentaires

- [`references/conteneur-et-stacks.md`](references/conteneur-et-stacks.md) — contrat de conteneur, notes Next.js standalone / FastAPI / Streamlit et test local anti-piège `HOSTNAME`.
- [`references/provisionnement-et-teardown.md`](references/provisionnement-et-teardown.md) — runbook complet Jour 0 (`scw` + `gh`), IAM moindre privilège, mode privé, domaine personnalisé et démontage complet.
- [`references/pieges-et-depannage.md`](references/pieges-et-depannage.md) — inventaire détaillé des pièges Scaleway Serverless Containers v1 et CLI `v2.65.2`.
- [`assets/ci-cd-scaleway.yml`](assets/ci-cd-scaleway.yml) — modèle de workflow GitHub Actions prêt à adapter (actions et CLI épinglés, zéro ID en repli).
- [`albert-chat`](../albert-chat/SKILL.md) — si le POC est un fork d'`etalab-ia/albert-chat` (contrat de corpus Albert, `check:config`, intégration iframe / Web Component).
- [`securite-developpement`](../securite-developpement/SKILL.md) — référentiel DINUM/ANSSI obligatoire lorsque le POC passe en production.
