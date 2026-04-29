---
name: rag-search
description: Rechercher dans une base de connaissances indexée. Utiliser quand l'utilisateur veut trouver des documents, effectuer une recherche sémantique, ou interroger un index de documents.
provider: qmd
available-providers:
  - qmd
  - pinecone
  - weaviate
---

# rag-search Skill

Search the qmd index for relevant documents. This skill uses **qmd** under the hood.

## Prerequisites

- qmd installed: `bun install -g @tobilu/qmd`
- Collection set up: Use `/rag-index` first

Verify setup:

```bash
qmd status
```

## Workflow

### 1. Verify Knowledge Base

```bash
qmd status
```

Should show your collection(s) with document counts.

### 2. Run Search

```bash
qmd query "<query>" --json
```

Examples:

```bash
qmd query "authentication flow" --json
qmd query "API design patterns" --json
qmd query "deployment process" --json
```

### 3. Present Results

Parse the JSON output and present:

- Document path
- Relevance score
- Relevant excerpt

## Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `query` | string | required | Search query |
| `mode` | string | query | Search mode: `query`, `vsearch`, `search` |
| `limit` | int | 5 | Number of results |
| `collection` | string | all | Restrict to specific collection |

## Search Modes

| Mode | Description |
|------|-------------|
| `query` | Semantic search (default) |
| `vsearch` | Vector search with scores |
| `search` | Hybrid search |

## Examples

```bash
# Basic search
qmd query "authentication" --json

# Limit results
qmd query "API design" --limit 10 --json

# Search specific collection
qmd query "deployment" --collection api-docs --json

# Vector search with scores
qmd vsearch "configuration" --json
```

## Output Format

JSON output structure:

```json
{
  "results": [
    {
      "path": "docs/guide.md",
      "score": 0.89,
      "content": "..."
    }
  ]
}
```

## Integration with Agents

When using this skill:

1. Run the search query
2. Parse JSON results
3. Present top results with scores
4. Optionally read full documents for deeper context

## Troubleshooting

If no results:
1. Check collection exists: `qmd status`
2. Verify embeddings generated: `qmd embed`
3. Try broader query terms

## Provider-Specific Notes

### qmd (current)

- Storage: Local SQLite with sqlite-vec extension
- Embeddings: Local model (no API key required)
- Best for: Small to medium corpora, offline usage

### pinecone (planned)

- Storage: Pinecone cloud
- Embeddings: OpenAI or custom embeddings
- Best for: Large-scale production deployments

### weaviate (planned)

- Storage: Weaviate instance (self-hosted or cloud)
- Embeddings: Configurable
- Best for: Enterprise deployments with hybrid search
