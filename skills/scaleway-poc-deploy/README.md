# scaleway-poc-deploy

Skill pour assistants de code IA — guide FDE (Forward Deployed Engineer) pour conteneuriser, provisionner, déployer en CI/CD, diagnostiquer et démonter un POC HTTP sans état sur **Scaleway Serverless Containers**.

Issue des retours terrain d'[`etalab-ia/albert-chat`](https://github.com/etalab-ia/albert-chat) et vérifiée sur la documentation officielle de Scaleway CLI **`v2.65.2`** (API Serverless Containers `v1`).

## Ce que fait cette skill

Quand elle est activée, l'assistant IA sait :

- **Poser les garde-fous avant exposition** — région `fr-par`, `robots.txt` bloquant l'indexation, `min_scale: 0` / `max_scale: 1`, séparation secrets/build, et choix explicite entre POC public borné et accès protégé (`privacy=private` + IAM `ContainersPrivateAccess` ou authentification applicative).
- **Produire une image compatible Scaleway** — multi-étapes non-root `linux/amd64`, `HOSTNAME=0.0.0.0`, sans variable `PORT`, avec notes spécifiques pour Next.js standalone, Python/FastAPI et Streamlit.
- **Provisionner de bout en bout en CLI (`scw` + `gh`)** — projet Scaleway dédié par POC (avec variante projet pré-créé), registre privé, conteneur Serverless, application IAM scopée au seul projet (`ContainersFullAccess` + `ContainerRegistryFullAccess`) et câblage des Secrets/Variables GitHub Actions.
- **Générer un pipeline GitHub Actions fiable** — basé sur [`assets/ci-cd-scaleway.yml`](assets/ci-cd-scaleway.yml) (actions épinglées par SHA, `scw` épinglé, aucun ID en repli, vérification de portée, tags `sha-<SHA>`, `--wait`, contrôles HTTP tolérants au démarrage à froid).
- **Diagnostiquer et démonter proprement** — résoudre les pièges récurrents (DNS `HOSTNAME`, noms immuables, `public_endpoint`, `arm64`, propagation IAM) et nettoyer toutes les ressources en fin de POC.

## Contenu

| Fichier | Description |
|---------|-------------|
| [`SKILL.md`](SKILL.md) | Périmètre, workflow FDE en 5 étapes et tableau de diagnostic rapide |
| [`references/conteneur-et-stacks.md`](references/conteneur-et-stacks.md) | Contrat d'image Scaleway, notes Next.js / FastAPI / Streamlit et test local |
| [`references/provisionnement-et-teardown.md`](references/provisionnement-et-teardown.md) | Runbook CLI Jour 0 (`scw` + `gh`), IAM moindre privilège, accès privé et démontage complet |
| [`references/pieges-et-depannage.md`](references/pieges-et-depannage.md) | Catalogue détaillé des pièges Scaleway Serverless Containers (`v1` / `scw v2.65.2`) |
| [`assets/ci-cd-scaleway.yml`](assets/ci-cd-scaleway.yml) | Modèle annoté de workflow GitHub Actions prêt à adapter |

## Installation

```bash
npx skills add etalab-ia/skills --skill scaleway-poc-deploy
```

Pour un assistant précis :

```bash
npx skills add etalab-ia/skills --skill scaleway-poc-deploy -a claude-code
npx skills add etalab-ia/skills --skill scaleway-poc-deploy -a opencode
```

## Exemples d'utilisation

- *« Je veux déployer mon POC FastAPI sur Scaleway Serverless Containers avec une CI GitHub Actions. »*
- *« Mon conteneur Next.js affiche Ready puis Scaleway dit qu'il n'écoute pas sur le port 8080. »*
- *« Provisionne le projet Scaleway, le registre privé et l'application IAM moindre privilège pour ce POC. »*
- *« Comment restreindre l'accès à mon POC Scaleway avant de le montrer au métier ? »*
- *« Le POC est terminé, donne-moi la procédure complète pour tout démonter proprement sur Scaleway et GitHub. »*

## Prérequis

- CLI [`scw`](https://github.com/scaleway/scaleway-cli) (`v2.65.2` recommandée), [`gh`](https://cli.github.com/), `docker` et `jq`.
- Un compte Scaleway configuré en local (droits `ProjectManager` et IAM pour créer un projet dédié, ou accès à un projet pré-créé).

## Liens utiles

- [Documentation Scaleway Serverless Containers](https://www.scaleway.com/en/docs/serverless-containers/)
- [Référence CLI `scw container`](https://www.scaleway.com/en/developers/cli/container)
- [Référence des ensembles de permissions IAM Scaleway](https://www.scaleway.com/en/docs/iam/policies-permissions/permission-sets/)
- Retour d'expérience source : [`etalab-ia/albert-chat`](https://github.com/etalab-ia/albert-chat)
- Skills complémentaires : [`albert-chat`](../albert-chat/), [`securite-developpement`](../securite-developpement/)

## Licence

MIT
