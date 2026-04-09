---
name: rag-index
description: Indexer un corpus de documents markdown pour la recherche sémantique. Utiliser quand l'utilisateur veut créer une base de connaissances, indexer des documents, ou configurer une recherche sémantique.
provider: qmd
available-providers:
  - qmd
  - pinecone
  - weaviate
---

# rag-index Skill

Index a document corpus for semantic search. This skill uses **qmd** under the hood.

## Prerequisites

Install qmd:

```bash
bun install -g @tobilu/qmd
```

Verify installation:

```bash
qmd --version
```

Documents must be in markdown format. Use `/rag-parse` first to convert PDFs/DOCX.

## Response Requirements

When using this skill, always include:

1. **Collection name** that will be created/used (e.g. `my-project`)
2. **Source documents path** being indexed (e.g. `./docs`)
3. **Where the index/collection is stored** (qmd collection location), and a verification command (`qmd status`)

Never omit storage location details in your final answer.

## Workflow

### 1. Verify qmd

```bash
qmd --version
```

If not installed, see Prerequisites above.

### 2. Create Collection

```bash
qmd collection add <path> --name <name>
```

Arguments:

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `path` | string | required | Path to document directory |
| `name` | string | derived | Collection name (defaults to directory name) |

Examples:

```bash
qmd collection add ./docs --name my-project
qmd collection add ~/Documents/api-docs --name api-docs
```

### 3. Add Context (Optional)

Add semantic context to help with retrieval:

```bash
qmd context add qmd://<name> "<description>"
```

Examples:

```bash
qmd context add qmd://api-docs "API documentation for the project"
qmd context add qmd://contracts "Legal contracts and agreements"
```

### 4. Generate Embeddings

```bash
qmd embed
```

This creates vector embeddings for all documents in the collection.

### 5. Verify Setup

```bash
qmd status
```

Should show your collection with document count.

## Full Example

```bash
# Create collection
qmd collection add ./docs --name my-project

# Add context
qmd context add qmd://my-project "Project documentation and guides"

# Generate embeddings
qmd embed

# Verify
qmd status
```

## Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `path` | string | required | Path to document directory |
| `name` | string | derived | Collection name |
| `context` | string | asked | Context description for retrieval |

## Troubleshooting

### "sqlite-vec is not available"

qmd requires SQLite with extension loading support. Solutions:

- **macOS**: `brew install sqlite`
- **Linux**: Build sqlite-vec from source
- **Docker**: Use official qmd Docker image

### Other Issues

If embeddings fail:
1. Check qmd status: `qmd status`
2. Verify documents exist: `ls -la <path>`
3. Check for empty files: `find <path> -empty`

## Next Steps

After setting up the knowledge base, use `/rag-search` to search your documents.

## Provider-Specific Notes

### qmd (current)

- Storage: Local SQLite with sqlite-vec extension
- Embeddings: Local model (no API key required)
- Best for: Small to medium corpora, offline usage

### pinecone (planned)

- Storage: Pinecone cloud
- Embeddings: OpenAI or custom embeddings
- Best for: Large-scale production deployments
- Setup: Requires `PINECONE_API_KEY` environment variable

### weaviate (planned)

- Storage: Weaviate instance (self-hosted or cloud)
- Embeddings: Configurable
- Best for: Enterprise deployments with hybrid search
- Setup: Requires `WEAVIATE_URL` and optionally `WEAVIATE_API_KEY`
