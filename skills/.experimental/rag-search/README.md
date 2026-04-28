# rag-search

Skill pour assistants de code IA — rechercher dans une base de connaissances indexée avec [qmd](https://github.com/tobi/qmd).

## Ce que fait cette skill

Quand elle est activée, l'assistant IA sait :

- **Effectuer des recherches sémantiques** dans les documents indexés
- **Présenter les résultats** avec scores de pertinence et extraits
- **Filtrer par collection** pour des recherches ciblées
- **Utiliser les différents modes de recherche** : query, vsearch, search (hybride)

## Contenu

| Fichier | Description |
|---------|-------------|
| [`SKILL.md`](SKILL.md) | Instructions principales — commandes de recherche, modes, format de sortie |

## Prérequis

- qmd installé : `bun install -g @tobilu/qmd`
- Collection configurée : utiliser `/rag-index` d'abord

```bash
qmd status  # Vérifier la configuration
```

## Installation

```bash
# Avec Vercel Skills CLI (recommandé)
npx skills add etalab-ia/skills --skill rag-search

# Claude Code
npx skills add etalab-ia/skills --skill rag-search -a claude-code

# OpenCode
npx skills add etalab-ia/skills --skill rag-search -a opencode
```

## Exemples d'utilisation

Une fois la skill installée, l'assistant IA peut répondre à des demandes comme :

- *"Cherche dans mes documents comment configurer l'authentification"* → `qmd query "authentication configuration" --json`
- *"Trouve des infos sur les APIs"* → `qmd query "API design patterns" --json`
- *"Recherche dans la collection api-docs"* → `qmd query "deployment" --collection api-docs --json`
- *"Limite les résultats à 10"* → `qmd query "API design" --limit 10 --json`

## Modes de recherche

| Mode | Description |
|------|-------------|
| `query` | Recherche sémantique (défaut) |
| `vsearch` | Recherche vectorielle avec scores |
| `search` | Recherche hybride |

## Liens utiles

- [qmd sur GitHub](https://github.com/tobi/qmd)

## Licence

MIT
