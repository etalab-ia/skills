# presentation-docs

Skill pour assistants de code IA — transformer une source (note Markdown, texte brut, ou fichier de présentation PPTX/PDF/DOCX) en un fichier Markdown propre respectant la convention du **mode présentation de [Docs (La Suite)](https://docs.numerique.gouv.fr/)** : une diapo par diviseur `---`.

## Ce que fait cette skill

Quand elle est activée, l'assistant IA sait :

- **Produire un `.md` aux conventions Docs** : diviseur `---` entouré de lignes vides = nouvelle diapo, pas de `# H1` initial (Docs ajoute le titre du document en H1 à l'import), 1 diapo = 1 idée
- **Respecter la source** : pour un PDF/PPTX, reproduire le deck à l'identique (même découpage, même ordre) ; pour une note ou un texte, découper en diapos logiques
- **Garder texte ET images** : le texte reste du markdown éditable, et seuls les médias non reproductibles (photos, captures, schémas) sont extraits et embarqués
- **Rester honnête sur les limites** : alignement, couleurs et colonnes sont des réglages de l'éditeur Docs, à faire à la main après import

La skill **produit uniquement le fichier `.md`** (et ses assets) — elle ne publie rien et n'appelle aucun service.

## Contenu

| Fichier | Description |
|---------|-------------|
| [`SKILL.md`](SKILL.md) | Instructions principales — convention diapos, extraction texte/médias, workflow |
| [`master-prompt.md`](master-prompt.md) | Version « master prompt » pour les assistants qui n'ingèrent pas les skills (ex. Assistant IA de l'État) — sans exécution de code |

## Prérequis

Aucun pour une note Markdown ou un texte brut.

Pour un **fichier de présentation externe** (PPTX/PDF/DOCX) :

```bash
# Extraction texte et médias d'un PDF
brew install poppler        # macOS  (pdftotext, pdfimages, pdftoppm)
apt-get install poppler-utils   # Ubuntu/Debian

# Optionnel — recadrage d'images
brew install imagemagick    # macOS
apt-get install imagemagick     # Ubuntu/Debian

# Optionnel — parsing PPTX (séparation texte/images par diapo)
pip install python-pptx
```

Une présentation disponible uniquement en ligne doit d'abord être exportée en PPTX ou PDF.

## Installation

```bash
# Avec Vercel Skills CLI (recommandé)
npx skills add etalab-ia/skills --skill presentation-docs

# Claude Code
npx skills add etalab-ia/skills --skill presentation-docs -a claude-code

# OpenCode
npx skills add etalab-ia/skills --skill presentation-docs -a opencode
```

## Exemples d'utilisation

Une fois la skill installée, l'assistant IA peut répondre à des demandes comme :

- *"Transforme cette note en présentation Docs"* → un `.md` découpé en diapos par `---`
- *"Mets ce PPTX en diapos Docs"* → deck reproduit à l'identique, texte + images extraites
- *"Formate ce texte en présentation Docs"* → réécriture aux conventions du mode présentation

## Licence

MIT
