# Pièges Scaleway Serverless Containers et dépannage

Catalogue des pièges vérifiés sur `etalab-ia/albert-chat` et sur la référence officielle de Scaleway CLI **`v2.65.2`** (API Serverless Containers **`v1`**).

## Sommaire

- [Réseau, port et runtime](#réseau-port-et-runtime)
- [API v1 et CLI `scw v2.65.2`](#api-v1-et-cli-scw-v2652)
- [IAM, registre et noms immuables](#iam-registre-et-noms-immuables)
- [CI/CD et dépôts forkés](#cicd-et-dépôts-forkés)
- [Exploitation et limites d'un POC](#exploitation-et-limites-dun-poc)

---

## Réseau, port et runtime

### `HOSTNAME=0.0.0.0` obligatoire

Next.js standalone (et tout serveur qui lit `process.env.HOSTNAME` comme interface d'écoute) échoue silencieusement sur Scaleway sans cette variable : le moteur renseigne `HOSTNAME` avec l'identifiant du conteneur, que le DNS interne de Scaleway ne résout pas. Les journaux affichent `Ready`, puis Scaleway échoue avec :

```text
Container is unable to start OR is not listening on port 8080
```

Le piège est trompeur car `docker run` et `podman run` résolvent cet identifiant en local. Définir `environment-variables.HOSTNAME=0.0.0.0` sur la ressource conteneur (et ne pas se reposer uniquement sur `ENV HOSTNAME=0.0.0.0` dans le `Dockerfile`, que la plateforme peut surcharger).

### `PORT` est un nom réservé

Scaleway refuse de définir une variable d'environnement nommée `PORT` sur le conteneur. Configurer le port via le champ `port` de la ressource (`port=8080` par défaut) ; l'application doit écouter sur ce même port.

### Architecture `linux/amd64` obligatoire (piège Apple Silicon)

Les conteneurs Serverless s'exécutent en `linux/amd64`. Un premier push réalisé depuis un Mac Apple Silicon sans `--platform linux/amd64` produit une image `arm64` qui échoue au démarrage (`exec format error`). Le job CI sur runner `ubuntu-24.04` construit nativement en `amd64`.

---

## API v1 et CLI `scw v2.65.2`

La transition de l'API Serverless Containers de `v1beta1` vers `v1` (prise en charge par `scw v2.65.2`) a changé plusieurs noms de champs par rapport aux anciens tutoriels en ligne :

| Paramètre | Nom correct (`v1` / `scw v2.65.2`) | Ancien nom obsolète (`v1beta1`) |
|---|---|---|
| Image du conteneur | `image` | `registry-image` / `registry_image` |
| Mémoire (en octets) | `memory-limit-bytes` (`memory_limit_bytes`) | `memory-limit` (en Mo) |
| CPU (en millivCPU) | `mvcpu-limit` (`mvcpu_limit`) | `cpu-limit` |
| Durée maximale d'exécution | `timeout` au format durée protobuf (`"300s"`) | — |
| Variables secrètes (CLI) | `secret-environment-variables.<CLE>=<VAL>` | `secret-environment-variables.0.key=...` |
| URL publique retournée | `public_endpoint` (inclut déjà `https://`) | `domain_name` (sans schéma) |

### Divergence de drapeau `https-connections-only` vs `https-connection-only`

Particularité vérifiée dans `scw v2.65.2` :
- `scw container container create` utilise **`https-connections-only=true`** (pluriel).
- `scw container container update` utilise **`https-connection-only=true`** (singulier).

### `--wait` obligatoire pour bloquer sur le déploiement

Par défaut, `scw container container create`, `update` et `redeploy` rendent la main immédiatement dès l'acceptation de la requête, avant la fin du déploiement. Passer systématiquement **`--wait`** en CI/CD et dans les scripts de provisionnement, puis revérifier `image` et `status == "ready"` avec `scw container container get`.

### `public_endpoint` contient déjà `https://`

Le champ JSON `.public_endpoint` retourné par `scw container container get -o json` commence déjà par `https://` (ex. `https://monpoc1234-monpoc.functions.fnc.fr-par.scw.cloud`). Ne pas le préfixer une seconde fois avec `https://` dans les contrôles `curl`.

### Secrets renvoyés hachés en `argon2id`

Lorsque l'on inspecte un conteneur via `scw container container get -o json` ou l'API, les valeurs de `secret_environment_variables` apparaissent sous forme d'empreintes `$argon2id$...`. C'est le comportement normal de masquage de Scaleway, pas une corruption de la valeur injectée au conteneur.

### Jetons JWT `scw container token create` dépréciés

L'authentification par jeton JWT de conteneur (`scw container token create`) est dépréciée au profit de l'authentification IAM (`ContainersPrivateAccess` + clé d'API passée dans l'en-tête `X-Auth-Token`).

---

## IAM, registre et noms immuables

### Une clé applicative IAM ne peut pas lire les API d'organisation/projet

Une application IAM de moindre privilège (`ContainersFullAccess` + `ContainerRegistryFullAccess` sur un seul projet) n'a pas accès aux endpoints compte (`scw account project get`, etc.). Pour vérifier en CI que la clé pointe bien vers la bonne organisation, le bon projet et le bon conteneur, interroger les ressources où le droit existe réellement :

1. `scw container namespace get "$SCW_NAMESPACE_ID"` → vérifier `.organization_id == $SCW_ORGANIZATION_ID` et `.project_id == $SCW_PROJECT_ID`.
2. `scw container container get "$SCW_CONTAINER_ID"` → vérifier `.namespace_id == $SCW_NAMESPACE_ID`.

### Délai de propagation IAM (jusqu'à 1 minute)

Après un `scw iam policy create` ou une modification de politique, les droits peuvent mettre jusqu'à **60 secondes** à se propager dans les caches Scaleway. Un échec `403` immédiat après le provisionnement Jour 0 se résout généralement en attendant une minute avant de relancer la vérification.

### Noms immuables et unicité globale du registre

- **Noms immuables** : les noms de namespace de registre, namespace de conteneurs et conteneur ne peuvent pas être modifiés après création. Renommer exige de **recréer** les ressources, ce qui génère de nouveaux UUIDs (`SCW_NAMESPACE_ID`, `SCW_CONTAINER_ID`) et une nouvelle URL `public_endpoint`.
- **Unicité globale régionale du registre** : le nom d'un namespace Container Registry (`rg.fr-par.scw.cloud/<namespace>`) doit être unique dans toute la région `fr-par`, toutes organisations Scaleway confondues. Préfixer le nom avec un identifiant d'équipe ou de ministère (ex. `alliance-<poc>`).
- **Nomenclature d'image complète** : toujours utiliser la référence complète `rg.<region>.scw.cloud/<namespace>/<image>:<tag>` à la fois pour `docker push` et pour l'argument `image=` du conteneur.

---

## CI/CD et dépôts forkés

### Ne jamais laisser d'IDs Scaleway en repli dans le workflow

Dans un dépôt modèle ou susceptible d'être forké, mettre des UUIDs Scaleway en valeur par défaut (`${{ vars.SCW_CONTAINER_ID || '<uuid>' }}`) est un anti-pattern :
- Un fork qui oublie de renseigner ses variables échoue contre les ressources du dépôt d'origine avec une erreur qui ressemble à un problème d'identifiants IAM au lieu d'une variable manquante.
- Si les ressources d'origine sont recréées (renommage), le repli pointe silencieusement vers des UUIDs supprimés (`404` / `401`).

**Règle** : imposer `test -n "$SCW_CONTAINER_ID"` (ainsi que `SCW_NAMESPACE_ID` et `SCW_IMAGE_BASE`) en échec rapide dès la première étape du job `deploy`, et afficher les valeurs résolues dans les logs.

### Ne pas annuler un déploiement en cours

Sur le job `deploy`, définir :

```yaml
concurrency:
  group: scaleway-production
  cancel-in-progress: false
```

Annuler une mise à jour Scaleway en plein vol laisse un état transitoire qui bloque le déploiement suivant.

### Tags immuables `sha-<SHA>`

Ne jamais déployer sur `:latest` en CI : un tag mutable masque la version réellement déployée, complique les retours arrière et oblige à appeler `scw container container redeploy`. Taguer chaque image avec `sha-${{ github.sha }}` et passer cette référence exacte à `scw container container update`.

---

## Exploitation et limites d'un POC

### Démarrage à froid sous `min_scale: 0`

Après une période d'inactivité, Scaleway arrête toutes les instances. La première requête subit un démarrage à froid (plusieurs secondes selon la taille d'image et le runtime) :
- **En CI** : les contrôles HTTP post-déploiement doivent utiliser un timeout généreux (`--max-time 45`) et une boucle de réessais (ex. 12 tentatives espacées de 10 s).
- **Avant une démo** : envoyer une requête réelle quelques secondes avant de présenter le POC.

### Compteurs en mémoire, `min_scale: 0` et plafonds budgétaires

Les compteurs conservés en mémoire du processus (anti-rafale par IP ou compteur applicatif) ne sont qu'un **frein au mieux (*best-effort*) sur l'instance courante** :
- Avec **`min-scale=0`**, Scaleway arrête le conteneur après inactivité ; chaque démarrage à froid, redéploiement ou redémarrage sur crash **remet ces compteurs à zéro**. Ils ne garantissent donc pas un plafond budgétaire journalier réel, même avec `max-scale=1`.
- Passer **`max-scale` au-delà de `1`** multiplie en outre la limite par le nombre d'instances actives et fragmente l'état.

Pour borner réellement le coût d'un POC public appelant une API payante (LLM, OCR), s'appuyer sur un **plafond imposé côté fournisseur amont** (clé d'API dédiée avec quota/budget plafonné) ou sur un **stockage persistant externe** (Redis / base partagée), plutôt que sur un compteur en mémoire seul. Pour un passage en production, suivre [`securite-developpement`](../../securite-developpement/SKILL.md).

### Consulter les journaux de démarrage

En cas d'échec de déploiement ou d'erreur 5xx, lire directement les journaux du conteneur :

```bash
scw container container logs "$SCW_CONTAINER_ID" region="$SCW_REGION" time-span=2h
```

Vérifier aussi l'état détaillé et le dernier message d'erreur de la ressource :

```bash
scw container container get "$SCW_CONTAINER_ID" region="$SCW_REGION" -o json | jq '{status, error_message, image, port, public_endpoint}'
```
