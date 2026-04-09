# rag-index

Skill pour assistants de code IA — indexer un corpus de documents markdown pour la recherche sémantique avec [qmd](https://github.com/tobi/qmd).

## Ce que fait cette skill

Quand elle est activée, l'assistant IA sait :

- **Créer des collections** à partir de documents markdown
- **Générer des embeddings** pour la recherche sémantique
- **Ajouter du contexte** sémantique pour améliorer la recherche
- **Configurer l'indexation** avec les bons paramètres

## Contenu

| Fichier | Description |
|---------|-------------|
| [`SKILL.md`](SKILL.md) | Instructions principales — workflow, commandes qmd, troubleshooting |

## Prérequis

```bash
# Installer qmd
bun install -g @tobilu/qmd

# Vérifier l'installation
qmd --version
```

Les documents doivent être au format markdown. Utiliser `/rag-parse` pour convertir PDFs/DOCX.

## Installation

```bash
# Avec Vercel Skills CLI (recommandé)
npx skills add etalab-ia/skills --skill rag-index

# Claude Code
npx skills add etalab-ia/skills --skill rag-index -a claude-code

# OpenCode
npx skills add etalab-ia/skills --skill rag-index -a opencode
```

## Exemples d'utilisation

Une fois la skill installée, l'assistant IA peut répondre à des demandes comme :

- *"Indexe tous les documents de ./docs"* → `qmd collection add ./docs --name my-project`
- *"Crée une base de connaissances pour mes API docs"* → `qmd collection add ~/Documents/api-docs --name api-docs`
- *"Ajoute du contexte pour améliorer la recherche"* → `qmd context add qmd://api-docs "API documentation for the project"`
- *"Génère les embeddings"* → `qmd embed`

## Workflow typique

```bash
# 1. Créer la collection
qmd collection add ./docs --name my-project

# 2. Ajouter du contexte
qmd context add qmd://my-project "Project documentation and guides"

# 3. Générer les embeddings
qmd embed

# 4. Vérifier
qmd status
```

## Liens utiles

- [qmd sur GitHub](https://github.com/tobi/qmd)
- [sqld (moteur de qmd)](https://github.com/tursodatabase/sqld)

## Licence

MIT
