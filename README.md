# Skills État

Skills pour les assistants de code IA (Claude Code, OpenCode, Mistral Vibe) intégrant les standards du développement dans l'État français.

## Skills disponibles

### react-dsfr

Créer des interfaces React conformes au [Design System de l'État](https://www.systeme-de-design.gouv.fr/) avec `@codegouvfr/react-dsfr`.

- Setup Vite + React + react-dsfr
- Import patterns pour chaque composant
- Grille, icônes, classes utilitaires `fr.cx()`
- Composants : Header, Footer, Button, Card, Alert, Input, Select, etc.

### rgaa

Outil d'audit de conformité [RGAA 4.1.2](https://accessibilite.numerique.gouv.fr/) — 106 critères d'accessibilité numérique.

Fournir du code HTML/React à auditer → rapport de conformité structuré avec statut C/NC/NA par critère, liste des non-conformités et corrections priorisées (🔴 Bloquant, 🟠 Majeur, 🟡 Mineur).

- Workflow d'audit en 4 étapes et format de rapport standardisé
- 106 critères avec test de code, non-conformité type et priorité
- Couvre les 13 thèmes : images, cadres, couleurs, multimédia, tableaux, liens, scripts, structure, présentation, formulaires, navigation, consultation
- Basé sur WCAG 2.1 niveau AA

### securite-anssi

12 règles essentielles de sécurité issues du [guide d'hygiène ANSSI](https://cyber.gouv.fr/publications/guide-dhygiene-informatique).

- TLS/HTTPS, gestion des secrets, authentification
- Headers de sécurité, validation des entrées
- Dépendances, logs, conteneurs, incidents

## Installation

### Claude Code

```bash
# Cloner dans le dossier skills de Claude Code
git clone https://github.com/benoitvx/skills-etat.git
cp -r skills-etat/react-dsfr ~/.claude/skills/
cp -r skills-etat/rgaa ~/.claude/skills/
cp -r skills-etat/securite-anssi ~/.claude/skills/
```

### OpenCode

```bash
git clone https://github.com/benoitvx/skills-etat.git
cp -r skills-etat/react-dsfr ~/.config/opencode/skills/
cp -r skills-etat/rgaa ~/.config/opencode/skills/
cp -r skills-etat/securite-anssi ~/.config/opencode/skills/
```

### Mistral Vibe

Copier les fichiers `SKILL.md` et `references/` dans le dossier de votre projet comme fichiers de référence dans `INSTRUCTIONS.md`.

## Structure

```
skills-etat/
├── react-dsfr/
│   ├── SKILL.md
│   └── references/
│       ├── setup.md
│       └── components.md
├── rgaa/
│   ├── SKILL.md
│   └── references/
│       ├── criteres-formulaires.md
│       ├── criteres-images-cadres-couleurs.md
│       ├── criteres-multimedia-tableaux-liens-scripts.md
│       ├── criteres-navigation-consultation.md
│       └── criteres-structure-presentation.md
└── securite-anssi/
    └── SKILL.md
```

## Licence

MIT
