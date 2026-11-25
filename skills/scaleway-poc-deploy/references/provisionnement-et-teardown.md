# Provisionnement Jour 0, exploitation et démontage (`scw` + `gh`)

Toutes les commandes ci-dessous sont vérifiées pour Scaleway CLI **`v2.65.2`** (API Serverless Containers **`v1`**) et GitHub CLI **`gh`**.

## Sommaire

- [Prérequis et variables de session](#prérequis-et-variables-de-session)
- [1. Créer ou cibler le projet Scaleway](#1-créer-ou-cibler-le-projet-scaleway)
- [2. Créer le registre privé et pousser la première image](#2-créer-le-registre-privé-et-pousser-la-première-image)
- [3. Créer le namespace et le conteneur Serverless](#3-créer-le-namespace-et-le-conteneur-serverless)
- [4. Restreindre l'accès si le POC n'est pas public](#4-restreindre-laccès-si-le-poc-nest-pas-public)
- [5. Créer l'application IAM dédiée à la CI/CD](#5-créer-lapplication-iam-dédiée-à-la-cicd)
- [6. Câbler les secrets et variables GitHub Actions](#6-câbler-les-secrets-et-variables-github-actions)
- [Opérations courantes (Jour N)](#opérations-courantes-jour-n)
- [Démontage complet en fin de POC (Teardown)](#démontage-complet-en-fin-de-poc-teardown)

---

## Prérequis et variables de session

Outils requis en local : `scw` (`v2.65.2`), `gh`, `docker` et `jq`.

Le profil local `scw` utilisé au Jour 0 doit disposer des droits de création de projet (`ProjectManager`) et de gestion IAM (`IAMManager` ou `IAMApplicationManager` + `IAMPolicyManager`) pour isoler le POC dans son propre projet. Sans droit `ProjectManager`, voir la variante projet pré-créé à l'étape 1.

Définir les variables de session dans le terminal (remplacer `<poc-slug>`, `<org-prefix>` et `<owner>/<repo>`) :

```bash
export POC_NAME="<poc-slug>"
export REGISTRY_NS="<org-prefix>-${POC_NAME}"
export SCW_REGION="fr-par"
export SCW_REGISTRY_HOST="rg.${SCW_REGION}.scw.cloud"
export SCW_ORGANIZATION_ID="$(scw config get default-organization-id)"
export GH_REPO="<owner>/<repo>"
export GIT_SHA="$(git rev-parse HEAD)"
```

Vérifier que `REGISTRY_NS` est unique : un nom de namespace Container Registry doit être **globalement unique dans toute la région `fr-par`**, toutes organisations confondues, et **ne peut pas être renommé** après création.

---

## 1. Créer ou cibler le projet Scaleway

**Par défaut (recommandé) — un projet dédié par POC**, pour isoler facturation, droits IAM et suppression finale :

```bash
export SCW_PROJECT_ID="$(scw account project create \
  name="poc-${POC_NAME}" \
  description="POC FDE ${POC_NAME}" \
  organization-id="$SCW_ORGANIZATION_ID" \
  -o json | jq -r '.id')"
echo "SCW_PROJECT_ID=${SCW_PROJECT_ID}"
```

**Variante — projet pré-créé** (si le FDE ne dispose pas du droit `ProjectManager`) : renseigner directement l'UUID du projet existant dans `SCW_PROJECT_ID`, et ne jamais exécuter `scw account project delete` au démontage.

---

## 2. Créer le registre privé et pousser la première image

`scw container container create` exige une image existante (`image` est obligatoire). Créer donc le registre privé (`is-public=false`) et pousser une première image **`linux/amd64`** taguée `sha-<SHA>` avant de créer le conteneur.

Créer le namespace Container Registry :

```bash
REGISTRY_JSON="$(scw registry namespace create \
  name="$REGISTRY_NS" \
  project-id="$SCW_PROJECT_ID" \
  is-public=false \
  region="$SCW_REGION" \
  -o json)"
export SCW_REGISTRY_NAMESPACE_ID="$(jq -r '.id' <<<"$REGISTRY_JSON")"
export SCW_REGISTRY_ENDPOINT="$(jq -r '.endpoint' <<<"$REGISTRY_JSON")"
export SCW_IMAGE_BASE="${SCW_REGISTRY_ENDPOINT}/${POC_NAME}"
export INITIAL_IMAGE="${SCW_IMAGE_BASE}:sha-${GIT_SHA}"
echo "SCW_REGISTRY_NAMESPACE_ID=${SCW_REGISTRY_NAMESPACE_ID}"
echo "INITIAL_IMAGE=${INITIAL_IMAGE}"
```

Se connecter au registre avec le profil local (`scw registry login` gère Docker et Podman), construire pour `linux/amd64` et pousser la première image :

```bash
scw registry login region="$SCW_REGION"
docker build --platform linux/amd64 --pull --tag "$INITIAL_IMAGE" .
docker push "$INITIAL_IMAGE"
```

---

## 3. Créer le namespace et le conteneur Serverless

Créer le namespace Serverless Containers (Scaleway génère automatiquement une identité interne `serverless-namespace-<region>-<id>` autorisée à tirer les images du registre) :

```bash
export SCW_NAMESPACE_ID="$(scw container namespace create \
  name="$POC_NAME" \
  project-id="$SCW_PROJECT_ID" \
  region="$SCW_REGION" \
  -o json | jq -r '.id')"
echo "SCW_NAMESPACE_ID=${SCW_NAMESPACE_ID}"
```

Créer le conteneur avec les garde-fous POC (`min-scale=0`, `max-scale=1`, 512 Mio, 500 mvCPU, `timeout=300s`, `https-connections-only=true`, `HOSTNAME=0.0.0.0`). Choisir explicitement `privacy=public` (démonstration sans donnée sensible, avec plafonds anti-abus) ou `privacy=private` (accès protégé par `X-Auth-Token` IAM) :

```bash
CONTAINER_JSON="$(scw container container create \
  namespace-id="$SCW_NAMESPACE_ID" \
  name="$POC_NAME" \
  image="$INITIAL_IMAGE" \
  port=8080 \
  min-scale=0 \
  max-scale=1 \
  memory-limit-bytes=536870912 \
  mvcpu-limit=500 \
  timeout=300s \
  privacy=public \
  https-connections-only=true \
  environment-variables.HOSTNAME=0.0.0.0 \
  region="$SCW_REGION" \
  --wait \
  -o json)"
export SCW_CONTAINER_ID="$(jq -r '.id' <<<"$CONTAINER_JSON")"
export SCW_ENDPOINT="$(jq -r '.public_endpoint' <<<"$CONTAINER_JSON")"
echo "SCW_CONTAINER_ID=${SCW_CONTAINER_ID}"
echo "SCW_ENDPOINT=${SCW_ENDPOINT}"
```

Pour injecter des variables d'environnement ou des secrets applicatifs dès la création (sans les exposer dans le `Dockerfile`), ajouter autant d'arguments que nécessaire :
- variables non secrètes : `environment-variables.NOM=valeur`
- secrets : `secret-environment-variables.NOM=valeur`

Ne **jamais** passer `environment-variables.PORT=...` (`PORT` est réservé par Scaleway).

Vérifier immédiatement la disponibilité (noter que `SCW_ENDPOINT` contient déjà `https://`) :

```bash
curl --fail --silent --show-error --max-time 45 "${SCW_ENDPOINT}/" -o /dev/null && echo "OK"
```

---

## 4. Restreindre l'accès si le POC n'est pas public

### Cas A : API, backend ou serveur MCP (`privacy=private` + IAM)

Lorsque le conteneur est créé ou mis à jour avec `privacy=private`, la passerelle Scaleway rejette en `403` toute requête sans en-tête `X-Auth-Token` valide.

Créer une application IAM dédiée aux appelants, lui attribuer uniquement **`ContainersPrivateAccess`** sur le projet du POC, puis générer sa clé d'API (ne pas utiliser `scw container token create`, déprécié) :

```bash
export SCW_CALLER_APP_ID="$(scw iam application create \
  name="invoke-${POC_NAME}" \
  description="Appelant autorisé pour le POC privé ${POC_NAME}" \
  organization-id="$SCW_ORGANIZATION_ID" \
  -o json | jq -r '.id')"

export SCW_CALLER_POLICY_ID="$(scw iam policy create \
  name="invoke-${POC_NAME}" \
  application-id="$SCW_CALLER_APP_ID" \
  organization-id="$SCW_ORGANIZATION_ID" \
  rules.0.project-ids.0="$SCW_PROJECT_ID" \
  rules.0.permission-set-names.0=ContainersPrivateAccess \
  -o json | jq -r '.id')"

CALLER_KEY_JSON="$(scw iam api-key create \
  application-id="$SCW_CALLER_APP_ID" \
  default-project-id="$SCW_PROJECT_ID" \
  description="Jeton X-Auth-Token pour ${POC_NAME}" \
  -o json)"
```

Attendre jusqu'à 60 secondes la propagation IAM, puis appeler le conteneur privé avec la valeur `.secret_key` dans l'en-tête `X-Auth-Token` :

```bash
curl --fail --silent --show-error --max-time 45 \
  -H "X-Auth-Token: $(jq -r '.secret_key' <<<"$CALLER_KEY_JSON")" \
  "${SCW_ENDPOINT}/"
```

### Cas B : interface web consultée dans un navigateur

Un navigateur ne peut pas injecter d'en-tête `X-Auth-Token` sur la navigation standard. Garder `privacy=public` au niveau de la passerelle Scaleway et placer la protection au niveau applicatif (authentification Basic Auth dédiée au POC, OIDC/ProConnect ou mandataire authentifiant en amont).

---

## 5. Créer l'application IAM dédiée à la CI/CD

Ne jamais injecter une clé d'API personnelle ou de niveau organisation dans GitHub Actions. Créer une application IAM dédiée, limitée au seul projet du POC avec exactement deux ensembles de permissions : **`ContainersFullAccess`** et **`ContainerRegistryFullAccess`**.

```bash
export SCW_CI_APP_ID="$(scw iam application create \
  name="ci-${POC_NAME}" \
  description="Déploiement GitHub Actions pour ${POC_NAME}" \
  organization-id="$SCW_ORGANIZATION_ID" \
  -o json | jq -r '.id')"

export SCW_CI_POLICY_ID="$(scw iam policy create \
  name="ci-${POC_NAME}" \
  application-id="$SCW_CI_APP_ID" \
  organization-id="$SCW_ORGANIZATION_ID" \
  rules.0.project-ids.0="$SCW_PROJECT_ID" \
  rules.0.permission-set-names.0=ContainersFullAccess \
  rules.0.permission-set-names.1=ContainerRegistryFullAccess \
  -o json | jq -r '.id')"

CI_KEY_JSON="$(scw iam api-key create \
  application-id="$SCW_CI_APP_ID" \
  default-project-id="$SCW_PROJECT_ID" \
  description="GitHub Actions CI/CD pour ${GH_REPO}" \
  -o json)"
```

Option recommandée pour un POC borné dans le temps : ajouter `expires-at="<YYYY-MM-DDT00:00:00Z>"` à `scw iam api-key create` pour imposer une expiration automatique de la clé CI.

La valeur `.secret_key` n'est retournée qu'une seule fois : la transférer directement vers GitHub Actions à l'étape suivante sans l'afficher dans le terminal.

---

## 6. Câbler les secrets et variables GitHub Actions

Séparer strictement les **4 Secrets** (identifiants et périmètre) des **5 Variables** (cibles de déploiement lisibles et surchargées sans toucher au code) :

```bash
jq -r '.access_key' <<<"$CI_KEY_JSON" | gh secret set SCW_ACCESS_KEY --repo "$GH_REPO"
jq -r '.secret_key' <<<"$CI_KEY_JSON" | gh secret set SCW_SECRET_KEY --repo "$GH_REPO"
printf '%s' "$SCW_ORGANIZATION_ID" | gh secret set SCW_ORGANIZATION_ID --repo "$GH_REPO"
printf '%s' "$SCW_PROJECT_ID" | gh secret set SCW_PROJECT_ID --repo "$GH_REPO"

gh variable set SCW_CONTAINER_ID --repo "$GH_REPO" --body "$SCW_CONTAINER_ID"
gh variable set SCW_NAMESPACE_ID --repo "$GH_REPO" --body "$SCW_NAMESPACE_ID"
gh variable set SCW_IMAGE_BASE --repo "$GH_REPO" --body "$SCW_IMAGE_BASE"
gh variable set SCW_REGISTRY_HOST --repo "$GH_REPO" --body "$SCW_REGISTRY_HOST"
gh variable set SCW_REGION --repo "$GH_REPO" --body "$SCW_REGION"
```

Si le conteneur est en `privacy=private` et que la CI exécute un contrôle HTTP post-déploiement, ajouter également la clé secrète de l'application appelante (`CALLER_KEY_JSON`) dans un secret `SCW_INVOKE_TOKEN` :

```bash
jq -r '.secret_key' <<<"$CALLER_KEY_JSON" | gh secret set SCW_INVOKE_TOKEN --repo "$GH_REPO"
```

Nettoyer ensuite les variables sensibles de la session locale (`unset CI_KEY_JSON CALLER_KEY_JSON`) et copier [`assets/ci-cd-scaleway.yml`](../assets/ci-cd-scaleway.yml) dans `.github/workflows/ci-cd.yml`.

Noter les identifiants créés (`SCW_PROJECT_ID`, `SCW_NAMESPACE_ID`, `SCW_REGISTRY_NAMESPACE_ID`, `SCW_CI_APP_ID`, `SCW_CI_POLICY_ID`, et éventuellement `SCW_CALLER_APP_ID` / `SCW_CALLER_POLICY_ID`) pour faciliter le démontage en fin de POC (ils restent retrouvables via `scw ... list`).

---

## Opérations courantes (Jour N)

**Mettre à jour un secret ou une variable d'environnement** (les autres champs restent inchangés ; noter `https-connection-only` au singulier sur `update`) :

```bash
scw container container update "$SCW_CONTAINER_ID" \
  secret-environment-variables.ALBERT_API_KEY="$NEW_VALUE" \
  region="$SCW_REGION" \
  --wait \
  -o json
```

**Préchauffer avant une démonstration** (quand `min-scale=0`) :

```bash
curl --fail --silent --show-error --max-time 45 "${SCW_ENDPOINT}/" -o /dev/null
```

**Consulter les journaux des 2 dernières heures** :

```bash
scw container container logs "$SCW_CONTAINER_ID" region="$SCW_REGION" time-span=2h
```

**Associer un domaine personnalisé** (après création de l'enregistrement DNS CNAME vers l'hôte de `public_endpoint`) :

```bash
scw container domain create \
  container-id="$SCW_CONTAINER_ID" \
  hostname="<poc.example.gouv.fr>" \
  region="$SCW_REGION" \
  -o json
```

---

## Démontage complet en fin de POC (Teardown)

Un POC terminé ne doit laisser ni endpoint oublié ni clé IAM active. Respecter l'ordre suivant :

1. **Supprimer le namespace Serverless Containers** (supprime en cascade les conteneurs, domaines personnalisés et déclencheurs) :

```bash
scw container namespace delete "$SCW_NAMESPACE_ID" region="$SCW_REGION"
```

2. **Supprimer le namespace Container Registry** (supprime les images stockées) :

```bash
scw registry namespace delete "$SCW_REGISTRY_NAMESPACE_ID" region="$SCW_REGION"
```

3. **Supprimer la politique et l'application IAM de CI/CD** (la suppression de l'application révoque et supprime automatiquement ses clés d'API). Répéter pour `SCW_CALLER_POLICY_ID` / `SCW_CALLER_APP_ID` si le mode privé avait été activé :

```bash
scw iam policy delete "$SCW_CI_POLICY_ID"
scw iam application delete "$SCW_CI_APP_ID"
```

4. **Supprimer le projet Scaleway dédié** (uniquement si un projet dédié a été créé à l'étape 1 ; le projet doit être vide) :

```bash
scw account project list-resources "$SCW_PROJECT_ID"
scw account project delete project-id="$SCW_PROJECT_ID"
```

5. **Nettoyer les secrets et variables GitHub Actions** :

```bash
for s in SCW_ACCESS_KEY SCW_SECRET_KEY SCW_ORGANIZATION_ID SCW_PROJECT_ID; do
  gh secret delete "$s" --repo "$GH_REPO"
done
for v in SCW_CONTAINER_ID SCW_NAMESPACE_ID SCW_IMAGE_BASE SCW_REGISTRY_HOST SCW_REGION; do
  gh variable delete "$v" --repo "$GH_REPO"
done
```
