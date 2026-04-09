# rag-tracking

Skill pour assistants de code IA — mémoire externe pour l'ingestion de documents, conçue pour les agents sans persistance (Claude Code, Codex, OpenCode).

## Ce que fait cette skill

Quand elle est activée, l'assistant IA sait :

- **Maintenir un historique des collections** indexées (`.context/COLLECTIONS.md`)
- **Tracker les problèmes de parsing** et leurs solutions (`.context/ISSUES.md`)
- **Promouvoir les patterns découverts** vers la mémoire persistante (`ctx add learning`)
- **Générer des rappels automatiques** via des hooks configurés

## Contenu

| Fichier | Description |
|---------|-------------|
| [`SKILL.md`](SKILL.md) | Instructions principales — workflow, commandes, intégration ctx |
| [`COLLECTIONS.md`](COLLECTIONS.md) | Template pour tracker les collections et l'historique d'ingestion |
| [`ISSUES.md`](ISSUES.md) | Template pour tracker les problèmes de parsing |
| [`ctxrc.template`](ctxrc.template) | Configuration ctx avec hooks automatiques |

## ⚠️ Important

Cette skill **n'est pas nécessaire pour Letta Code** qui a une mémoire native persistante. Elle est utile pour :

- Claude Code
- Codex
- OpenCode
- Tout agent sans mémoire persistante

## Installation

```bash
# Avec Vercel Skills CLI (recommandé)
npx skills add etalab-ia/skills --skill rag-tracking

# Claude Code
npx skills add etalab-ia/skills --skill rag-tracking -a claude-code

# OpenCode
npx skills add etalab-ia/skills --skill rag-tracking -a opencode
```

## Exemples d'utilisation

- *"Quelles collections avons-nous indexées ?"* → Lire `.context/COLLECTIONS.md`
- *"Quels problèmes de parsing avons-nous rencontrés ?"* → Lire `.context/ISSUES.md`
- *"Enregistre cette ingestion"* → Ajouter une entrée dans `COLLECTIONS.md`
- *"Note ce problème de parsing"* → Ajouter une entrée dans `ISSUES.md`

## Workflow typique

```bash
# 1. Initial setup
ctx init
cp skills/rag-tracking/COLLECTIONS.md .context/
cp skills/rag-tracking/ISSUES.md .context/

# 2. Après ingestion d'un corpus
# → Mettre à jour .context/COLLECTIONS.md

# 3. Si erreur rencontrée
# → Ajouter dans .context/ISSUES.md

# 4. Promouvoir un pattern découvert
ctx add learning "French government PDFs require --ocr-language fra"
```

## Liens utiles

- [ctx (outil de mémoire externe)](https://ctx.ist)

## Licence

MIT
