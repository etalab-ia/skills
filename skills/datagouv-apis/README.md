# datagouv-apis

Skill pour assistants de code IA — référence consolidée des 3 APIs de [data.gouv.fr](https://www.data.gouv.fr/) pour interagir avec la plateforme de données ouvertes.

> **Note** : cette skill est synchronisée automatiquement depuis le repo upstream [`datagouv/datagouv-skill`](https://github.com/datagouv/datagouv-skill). Pour contribuer au contenu de la skill, ouvrir une PR sur le repo upstream. Un workflow GitHub Actions vérifie chaque semaine (lundi 9h UTC) si des changements sont disponibles et ouvre une PR de synchronisation le cas échéant.

## Ce que fait cette skill

Quand elle est activée, l'assistant IA sait :

- **API principale** — Interroger le catalogue : datasets, organisations, utilisateurs, ressources, réutilisations, discussions
- **API Metrics** — Récupérer les statistiques d'usage et de téléchargement par modèle
- **API Tabulaire** — Requêter les données CSV par resource ID avec filtrage, tri, pagination et agrégation

## Contenu

| Fichier | Description |
|---------|-------------|
| [`SKILL.md`](SKILL.md) | Référence consolidée des 3 APIs (endpoints, paramètres, exemples) |

## Installation

```bash
# Avec Vercel Skills CLI (recommandé)
npx skills add etalab-ia/skills --skill datagouv-apis

# Claude Code
npx skills add etalab-ia/skills --skill datagouv-apis -a claude-code

# OpenCode
npx skills add etalab-ia/skills --skill datagouv-apis -a opencode
```

Pour d'autres clients (Cursor, Mistral Vibe, Codex CLI, ChatGPT), voir les [instructions d'installation du repo upstream](https://github.com/datagouv/datagouv-skill#installation).

## Exemples d'utilisation

Une fois la skill installée, l'assistant IA peut répondre à des demandes comme :

- *"Liste les datasets de data.gouv.fr sur le thème transport"*
- *"Récupère les statistiques de téléchargement de ce dataset"*
- *"Requête les lignes du CSV de cette ressource avec un filtre sur la colonne région"*
- *"Crée un script qui publie un dataset sur data.gouv.fr"*

## Liens utiles

- [data.gouv.fr](https://www.data.gouv.fr/)
- [Repo upstream de la skill](https://github.com/datagouv/datagouv-skill)
- [Serveur MCP data.gouv.fr](https://github.com/datagouv/datagouv-mcp) — pour les appels API structurés via MCP
- [Documentation API data.gouv.fr](https://doc.data.gouv.fr/api/reference/)

## Licence

MIT
