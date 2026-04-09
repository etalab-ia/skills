# Skills État

Skills pour les assistants de code IA (Claude Code, OpenCode, Mistral Vibe) intégrant les standards du développement dans l'État français.

## Skills disponibles

| Skill | Description |
|-------|-------------|
| [**react-dsfr**](skills/react-dsfr/) | Interfaces React conformes au [Design System de l'État](https://www.systeme-de-design.gouv.fr/) avec `@codegouvfr/react-dsfr` |
| [**rgaa**](skills/rgaa/) | Audit de conformité [RGAA 4.1.2](https://accessibilite.numerique.gouv.fr/) — 106 critères d'accessibilité numérique |
| [**lasuite-ui-kit**](skills/lasuite-ui-kit/) | Interfaces React pour [LaSuite](https://lasuite.numerique.gouv.fr/) avec `@gouvfr-lasuite/ui-kit` et `@gouvfr-lasuite/cunningham-react` |
| [**securite-anssi**](skills/securite-anssi/) | 12 règles de sécurité issues du [guide d'hygiène ANSSI](https://cyber.gouv.fr/publications/guide-dhygiene-informatique) |
| [**datagouv-apis**](skills/datagouv-apis/) | 3 APIs de [data.gouv.fr](https://www.data.gouv.fr/) — synchronisée depuis [datagouv/datagouv-skill](https://github.com/datagouv/datagouv-skill) |

Chaque skill a son propre README avec des exemples d'utilisation et des liens utiles.

## Templates d'instructions

Fichiers `INSTRUCTIONS.md` prêts à l'emploi pour configurer un assistant de code IA sur un projet de l'État. Copier le fichier correspondant à la racine de votre projet sous le nom `INSTRUCTIONS.md` ou `CLAUDE.md`.

| Template | Écosystème | Design System | Package manager |
|----------|-----------|---------------|-----------------|
| [`beta.gouv.md`](templates/instructions/beta.gouv.md) | [beta.gouv.fr](https://beta.gouv.fr/) | DSFR (`@codegouvfr/react-dsfr`) | pnpm |
| [`LaSuite.md`](templates/instructions/LaSuite.md) | [La Suite numérique](https://lasuite.numerique.gouv.fr/) | UI Kit + Cunningham | yarn |

Chaque template inclut : conventions de langue, design system, accessibilité RGAA, sécurité ANSSI, RGPD, stack recommandée, tests, conventions Git, pre-commit gitleaks (détection de secrets) et références vers les skills pertinentes de ce repo.

Le template `beta.gouv.md` inclut également : Definition of Done (boucle tests → vérification navigateur → correction), CI GitHub Actions, pre-commit Husky (`gitleaks` + `pnpm validate`), contrainte sur les dépendances, section Expected Behavior (Plan Mode, gestion des tâches, self-improvement loop), section Architecture et guides de personnalisation.

## Installation

### Vercel Skills CLI (recommandé)

```bash
# Installer toutes les skills
npx skills add etalab-ia/skills

# Installer une skill spécifique
npx skills add etalab-ia/skills --skill react-dsfr
npx skills add etalab-ia/skills --skill rgaa
```

### Claude Code

```bash
npx skills add etalab-ia/skills -a claude-code
```

### OpenCode

```bash
npx skills add etalab-ia/skills -a opencode
```

### Mistral Vibe

Copier les fichiers `SKILL.md` et `references/` dans le dossier de votre projet comme fichiers de référence dans `INSTRUCTIONS.md`.

## Structure

```
skills/
├── react-dsfr/
│   ├── SKILL.md
│   └── references/
│       ├── setup.md
│       └── components.md
├── lasuite-ui-kit/
│   ├── SKILL.md
│   └── references/
│       ├── components.md
│       ├── cunningham.md
│       └── setup.md
├── rgaa/
│   ├── SKILL.md
│   └── references/
│       ├── criteres-formulaires.md
│       ├── criteres-images-cadres-couleurs.md
│       ├── criteres-multimedia-tableaux-liens-scripts.md
│       ├── criteres-navigation-consultation.md
│       └── criteres-structure-presentation.md
├── securite-anssi/
│   └── SKILL.md
├── datagouv-apis/
│   └── SKILL.md
└── templates/
    └── instructions/
        ├── beta.gouv.md
        └── LaSuite.md
```

## Licence

MIT
