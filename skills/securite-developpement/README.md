# securite-developpement

Skill pour assistants de code IA — 12 règles essentielles de sécurité, générées par la DINUM en s'appuyant sur le [guide d'hygiène ANSSI](https://cyber.gouv.fr/publications/guide-dhygiene-informatique) pour le développement d'applications de l'État.

## Ce que fait cette skill

Quand elle est activée, l'assistant IA peut :

- **Auditer la sécurité** d'une application web, API ou service exposé selon les 12 règles de sécurité
- **Produire un rapport structuré** avec grille de priorités (🔴 Critique, 🟠 Élevé, 🟡 Modéré), qualification de l'exploitabilité de chaque non-conformité et étape de validation des faux positifs
- **Appliquer les bonnes pratiques** : TLS/HTTPS, gestion des secrets, authentification, headers de sécurité, validation des entrées, dépendances, logs, conteneurs
- **Exporter le rapport** dans `audits/securite-developpement-AAAA-MM-JJ.md`, avec une sortie structurée `securite-developpement-AAAA-MM-JJ.json` optionnelle (machine-lisible)

## Contenu

| Fichier | Description |
|---------|-------------|
| [`SKILL.md`](SKILL.md) | Workflow d'audit (analyse, qualification, validation, export) et renvois |
| [`references/checklist.md`](references/checklist.md) | Les 12 domaines de sécurité détaillés (règles à vérifier) |
| [`references/rapport.md`](references/rapport.md) | Format du rapport, grille de priorités, export, sortie JSON optionnelle |
| [`references/findings-schema.json`](references/findings-schema.json) | JSON Schema de la sortie structurée optionnelle (`securite-developpement-AAAA-MM-JJ.json`) |

## Installation

```bash
# Avec Vercel Skills CLI (recommandé)
npx skills add etalab-ia/skills --skill securite-developpement

# Claude Code
npx skills add etalab-ia/skills --skill securite-developpement -a claude-code

# OpenCode
npx skills add etalab-ia/skills --skill securite-developpement -a opencode
```

## Exemples d'utilisation

Une fois la skill installée, l'assistant IA peut répondre à des demandes comme :

- *"Audite la sécurité de mon API Express"*
- *"Est-ce que mes headers de sécurité sont correctement configurés ?"*
- *"Vérifie que je ne stocke pas de secrets en dur dans le code"*
- *"Génère un rapport de sécurité pour ce projet"*

## Liens utiles

- [Guide d'hygiène informatique ANSSI](https://cyber.gouv.fr/publications/guide-dhygiene-informatique)
- [ANSSI — Agence nationale de la sécurité des systèmes d'information](https://cyber.gouv.fr/)

## Licence

MIT
