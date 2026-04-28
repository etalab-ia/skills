# Skills État

Skills pour les assistants de code IA (Claude Code, OpenCode, Mistral Vibe) intégrant les standards du développement dans l'État français.

> **Deux niveaux de skills** :
> - [`skills/`](skills/) — skills **officiels**, portés par le département IAE de la DINUM, adossés à des standards de l'État (DSFR, RGAA, ANSSI, data.gouv.fr, La Suite).
> - [`skills/.experimental/`](skills/.experimental/) ⚠️ — skills **expérimentaux**, non portés par la DINUM, consommant des outils tiers non audités. À utiliser avec précaution. Voir l'[avertissement](skills/.experimental/README.md).

## Skills officiels

| Skill | Description |
|-------|-------------|
| [**react-dsfr**](skills/react-dsfr/) | Interfaces React conformes au [Design System de l'État](https://www.systeme-de-design.gouv.fr/) avec `@codegouvfr/react-dsfr` |
| [**rgaa**](skills/rgaa/) | Audit de conformité [RGAA 4.1.2](https://accessibilite.numerique.gouv.fr/) — 106 critères d'accessibilité numérique |
| [**lasuite-ui-kit**](skills/lasuite-ui-kit/) | Interfaces React pour [LaSuite](https://lasuite.numerique.gouv.fr/) avec `@gouvfr-lasuite/ui-kit` et `@gouvfr-lasuite/cunningham-react` |
| [**securite-anssi**](skills/securite-anssi/) | 12 règles de sécurité issues du [guide d'hygiène ANSSI](https://cyber.gouv.fr/publications/guide-dhygiene-informatique) |
| [**datagouv-apis**](skills/datagouv-apis/) | 3 APIs de [data.gouv.fr](https://www.data.gouv.fr/) — synchronisée depuis [datagouv/datagouv-skill](https://github.com/datagouv/datagouv-skill) |

## Skills expérimentaux ⚠️

Non portés par la DINUM, dépendances tierces non auditées, pas de garantie de maintenance. [Lire l'avertissement complet](skills/.experimental/README.md) avant adoption.

| Skill | Description |
|-------|-------------|
| [**rag-parse**](skills/.experimental/rag-parse/) ⚠️ | Convertir PDF/DOCX/PPTX/XLSX/images en markdown ou JSON avec [LiteParse](https://github.com/run-llama/liteparse) |
| [**rag-index**](skills/.experimental/rag-index/) ⚠️ | Indexer un corpus de documents pour la recherche sémantique avec [qmd](https://github.com/tobi/qmd) |
| [**rag-search**](skills/.experimental/rag-search/) ⚠️ | Rechercher dans une base de connaissances indexée avec [qmd](https://github.com/tobi/qmd) |

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
# Installer tous les skills (officiels + expérimentaux)
npx skills add etalab-ia/skills

# Installer une skill spécifique
npx skills add etalab-ia/skills --skill react-dsfr
npx skills add etalab-ia/skills --skill rgaa
```

> Le sous-dossier `skills/.experimental/` est une convention reconnue par la CLI : les skills expérimentaux sont installables au même titre que les skills officiels. Vérifier leur statut avant adoption (cf. [avertissement](skills/.experimental/README.md)).

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
│   ├── README.md
│   ├── SKILL.md
│   └── references/
│       ├── setup.md
│       └── components.md
├── lasuite-ui-kit/
│   ├── README.md
│   ├── SKILL.md
│   └── references/
│       ├── components.md
│       ├── cunningham.md
│       └── setup.md
├── rgaa/
│   ├── README.md
│   ├── SKILL.md
│   └── references/
│       ├── criteres-formulaires.md
│       ├── criteres-images-cadres-couleurs.md
│       ├── criteres-multimedia-tableaux-liens-scripts.md
│       ├── criteres-navigation-consultation.md
│       └── criteres-structure-presentation.md
├── securite-anssi/
│   ├── README.md
│   └── SKILL.md
├── datagouv-apis/
│   ├── README.md
│   └── SKILL.md
└── .experimental/          # ⚠️ skills non portés par la DINUM, dépendances tierces non auditées
    ├── README.md
    ├── rag-parse/
    │   ├── README.md
    │   └── SKILL.md
    ├── rag-index/
    │   ├── README.md
    │   └── SKILL.md
    └── rag-search/
        ├── README.md
        └── SKILL.md

templates/
└── instructions/
    ├── beta.gouv.md
    └── LaSuite.md
```

## Licence

MIT
