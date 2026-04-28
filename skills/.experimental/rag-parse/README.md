# rag-parse

Skill pour assistants de code IA — convertir des documents non-structurés (PDF, DOCX, PPTX, XLSX, images) en markdown ou JSON localement avec [LiteParse](https://github.com/run-llama/liteparse).

## Ce que fait cette skill

Quand elle est activée, l'assistant IA sait :

- **Parser des documents** localement sans cloud : PDF, DOCX, PPTX, XLSX, ODT, ODP, ODS, images (JPG, PNG, TIFF, WebP, SVG)
- **Générer les bonnes commandes** `lit parse` avec les options adaptées (OCR, DPI, plages de pages)
- **Produire des screenshots** de pages pour les agents LLM qui ont besoin de voir le layout visuel
- **Configurer LiteParse** pour des usages répétés avec un fichier de config

## Contenu

| Fichier | Description |
|---------|-------------|
| [`SKILL.md`](SKILL.md) | Instructions principales — commandes CLI, options OCR, formats supportés |

## Prérequis

```bash
# Installer LiteParse globalement
npm i -g @llamaindex/liteparse

# Pour Office (DOCX, PPTX, XLSX)
brew install --cask libreoffice   # macOS
apt-get install libreoffice       # Ubuntu/Debian

# Pour les images
brew install imagemagick          # macOS
apt-get install imagemagick       # Ubuntu/Debian
```

## Installation

```bash
# Avec Vercel Skills CLI (recommandé)
npx skills add etalab-ia/skills --skill rag-parse

# Claude Code
npx skills add etalab-ia/skills --skill rag-parse -a claude-code

# OpenCode
npx skills add etalab-ia/skills --skill rag-parse -a opencode
```

## Exemples d'utilisation

Une fois la skill installée, l'assistant IA peut répondre à des demandes comme :

- *"Parse ce PDF et extrais le texte"* → `lit parse document.pdf`
- *"Convertis ce DOCX en JSON avec les bounding boxes"* → `lit parse document.docx --format json -o output.json`
- *"Prends des screenshots des pages 1-10 de ce PDF"* → `lit screenshot document.pdf --pages "1-10" -o ./screenshots`
- *"Parse tous les PDFs de ce dossier récursivement"* → `lit batch-parse ./input ./output --extension .pdf --recursive`

## Liens utiles

- [LiteParse sur GitHub](https://github.com/run-llama/liteparse)
- [Documentation LiteParse](https://docs.llamaindex.ai/projects/liteparse/)

## Licence

MIT
