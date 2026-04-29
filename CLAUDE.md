# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A collection of AI coding assistant skills ("skills") for French government software development standards. Each skill is a self-contained directory with a `SKILL.md` (frontmatter + instructions) and optional `references/` folder with detailed documentation. Skills are installed by copying them into `~/.claude/skills/` (Claude Code) or `~/.config/opencode/skills/` (OpenCode).

This is a **documentation-only repo** — no build system, no tests, no dependencies. All files are Markdown.

## Architecture

Each skill follows the same structure:
```
skill-name/
├── SKILL.md          # Frontmatter (name, description, trigger conditions) + main instructions
└── references/       # Optional detailed reference docs split by topic
```

The `SKILL.md` frontmatter fields (`name`, `description`) are used by AI tools to decide when to activate the skill. The `description` field is critical — it defines the trigger conditions. Some skills (rag-*) use additional fields `provider` and `available-providers` to support plug-and-play of different backend providers.

## Current Skills

Skills are split into two tiers:

**Official skills (`skills/`)** — backed by State standards, maintained by the DINUM IAE department:
- **react-dsfr** — React components for the Design System de l'État (DSFR) using `@codegouvfr/react-dsfr`
- **lasuite-ui-kit** — React components for LaSuite apps using `@gouvfr-lasuite/ui-kit` and `@gouvfr-lasuite/cunningham-react`
- **rgaa** — RGAA 4.1.2 accessibility audit tool (106 criteria, produces structured conformity reports)
- **securite-anssi** — ANSSI security checklist (12 rules for government app development)
- **datagouv-apis** — data.gouv.fr APIs reference (catalog, metrics, tabular) — synced from [datagouv/datagouv-skill](https://github.com/datagouv/datagouv-skill)

**Experimental skills (`skills/.experimental/`)** ⚠️ — not maintained by the DINUM, depend on unaudited third-party tools, no continuity guarantee. The `.experimental/` subdirectory is a convention recognized by the [Vercel Skills CLI](https://github.com/vercel-labs/skills) so they remain installable. See [skills/.experimental/README.md](skills/.experimental/README.md):
- **rag-parse** — Convert PDF/DOCX/PPTX/XLSX/images to markdown or JSON with LiteParse (local, no cloud dependencies)
- **rag-index** — Index markdown documents for semantic search with qmd (local SQLite + sqlite-vec)
- **rag-search** — Search indexed documents with qmd (semantic and keyword search)

## Templates

The `templates/instructions/` directory contains ready-to-use `INSTRUCTIONS.md` files for government projects. Each template covers language conventions, design system, accessibility, security, testing, Git conventions, and links to relevant skills from this repo. Two variants exist: `beta.gouv.md` (beta.gouv ecosystem, DSFR, pnpm) and `LaSuite.md` (La Suite numérique, UI Kit + Cunningham, yarn). Templates are written in English (instruction language) while preserving French convention values.

## Upstream Sync

The `datagouv-apis` skill is synced from an external repo (`datagouv/datagouv-skill`). A GitHub Actions workflow (`.github/workflows/sync-datagouv.yml`) runs weekly (Monday 9h UTC) and on manual trigger. It compares the upstream HEAD SHA against `.sync-state/datagouv.sha` and opens a PR if changes are detected. This mechanism is extensible to other third-party skills.

## Conventions

- All content is in **French**
- Skills target React/TypeScript projects
- SKILL.md files use YAML frontmatter (`---` delimiters) with `name` and `description` fields; RAG skills additionally use `provider` and `available-providers` fields
- Reference files are split by theme/topic to keep individual files manageable
- The rgaa skill is an audit tool (input: code to audit → output: structured report), not a code generation skill
- Commit messages follow conventional commits format (e.g., `feat(skill-name):`, `docs(readme):`, `refactor(skill-name):`)

## Tests
  - Any new feature must be accompanied by tests
  - Before considering a task complete, run the tests and verify that they pass
  - If you modify existing code, add tests if there aren't any already
