# albert-chat

Skill pour assistants de code IA — guide FDE (Forward Deployed Engineer) pour adapter, configurer, déployer et intégrer [`etalab-ia/albert-chat`](https://github.com/etalab-ia/albert-chat) sur un corpus métier dans l'API Albert.

## Ce que fait cette skill

Quand elle est activée, l'assistant IA sait :

- **Cadrer la frontière entre dépôts** — distinguer le runtime lecture seule (`albert-chat`) du dépôt d'ingestion métier (à adosser à [`albert-api`](../albert-api/SKILL.md)), et vérifier l'éligibilité fonctionnelle (pas d'authentification ni de droits par utilisateur).
- **Respecter le contrat de corpus** — produire des extraits compatibles avec `buildContextBlocks` (`<= 1200` caractères, `title`, `source_url`, `page_number`), éviter la perte des numéros de page lors de l'ingestion, et interpréter correctement `pnpm check:config`.
- **Adapter un fork sans régression** — personnaliser les libellés et suggestions tout en préservant la balise `<albert-chat>`, l'isolation CSS `(site)` / `(embed)` et la cohérence prompt/citations.
- **Déployer sur Scaleway** — éviter le piège des variables de repli dans `ci-cd.yml` et les écueils API/runtime (`HOSTNAME=0.0.0.0`, `PORT` réservé, démarrage à froid).
- **Intégrer et diagnostiquer** — choisir entre iframe (`/embed.js`) et Web Component (`<albert-chat>`), configurer `EMBED_ALLOWED_PARENTS`, `WIDGET_ALLOWED_ORIGINS` et la CSP de la page hôte.

## Contenu

| Fichier | Description |
|---------|-------------|
| [`SKILL.md`](SKILL.md) | Positionnement, workflow FDE en 5 étapes et tableau de diagnostic rapide |
| [`references/contrat-corpus.md`](references/contrat-corpus.md) | Contrat des extraits, ingestion préservant les pages et validation `check:config` |
| [`references/integration-et-deploiement.md`](references/integration-et-deploiement.md) | Modes d'intégration, variables d'env, déploiement Scaleway et personnalisation sûre |

## Installation

```bash
# Avec Vercel Skills CLI (recommandé)
npx skills add etalab-ia/skills --skill albert-chat

# Claude Code
npx skills add etalab-ia/skills --skill albert-chat -a claude-code

# OpenCode
npx skills add etalab-ia/skills --skill albert-chat -a opencode
```

## Exemples d'utilisation

- *« Je déploie albert-chat sur notre base documentaire RH, par où commencer ? »*
- *« Pourquoi check:config est vert alors que le widget répond à côté ? »*
- *« Comment indexer nos PDF dans Albert pour garder les liens vers la bonne page ? »*
- *« Mon fork albert-chat échoue en CI sur Verify the Scaleway project and container »*
- *« Faut-il intégrer albert-chat en iframe ou en Web Component sur notre intranet ? »*

## Prérequis

- Un projet utilisant [`etalab-ia/albert-chat`](https://github.com/etalab-ia/albert-chat) (Node 26, pnpm 11).
- Une clé API Albert dédiée au projet (`ALBERT_API_KEY`) et, pour le déploiement CI/CD, un espace Scaleway Serverless Containers.

## Liens utiles

- [Dépôt `etalab-ia/albert-chat`](https://github.com/etalab-ia/albert-chat)
- [Documentation Albert API](https://doc.incubateur.net/alliance/albert-api)
- Skill complémentaire : [`albert-api`](../albert-api/)

## Licence

MIT
