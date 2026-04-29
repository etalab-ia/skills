# Skills expérimentales

Ce dossier regroupe des skills **expérimentales**, à distinguer des skills officielles de [`skills/`](../).

## ⚠️ Avertissement

- Ces skills **ne sont pas portées par le département IAE de la DINUM**.
- Elles consomment des **outils tiers non audités** (cf. tableau ci-dessous), sans pin de version stricte. **Auditer avant adoption** dans un projet de l'État.
- **Aucune garantie** de maintenance, de sécurité ni de continuité. Elles peuvent être retirées à tout moment.
- Le statut "officiel" suppose une autorité de référence (DSFR, RGAA, ANSSI, data.gouv.fr, La Suite, etc.). Les skills présentes ici n'en ont pas.

## Skills disponibles

| Skill | Description | Outil tiers |
|-------|-------------|-------------|
| [**rag-parse**](rag-parse/) | Convertir PDF/DOCX/PPTX/XLSX/images en markdown ou JSON | [LiteParse](https://github.com/run-llama/liteparse) (run-llama) |
| [**rag-index**](rag-index/) | Indexer un corpus de documents pour la recherche sémantique | [qmd](https://github.com/tobi/qmd) (tobi) |
| [**rag-search**](rag-search/) | Rechercher dans une base de connaissances indexée | [qmd](https://github.com/tobi/qmd) (tobi) |

## Convention de dossier

Le sous-dossier `skills/.experimental/` est une convention reconnue par la [Vercel Skills CLI](https://github.com/vercel-labs/skills) : ces skills restent installables via `npx skills add etalab-ia/skills`, mais leur statut expérimental est explicite.
