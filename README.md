# Skills État

Skills pour les assistants de code IA (Claude Code, OpenCode, Mistral Vibe) intégrant les standards du développement dans l'État français.

## Skills disponibles

### react-dsfr

Créer des interfaces React conformes au [Design System de l'État](https://www.systeme-de-design.gouv.fr/) avec `@codegouvfr/react-dsfr`.

- Setup Vite / Next.js (App Router & Pages Router) + react-dsfr
- Dark mode sans flash (`createGetHtmlAttributes` + `getScriptToRunAsap`)
- Re-initialisation DSFR après hydratation React (pattern `DsfrStartup` / `window.dsfr.start()`)
- Composant Display et intégration Header/Footer avec `headerFooterDisplayItem`
- Import patterns pour chaque composant
- Grille, icônes, classes utilitaires `fr.cx()`
- Config ESLint recommandée (CI sans prompt interactif, règles DSFR)
- Fix imports Next.js App Router (chemins `next-app-router` depuis v1.30+)
- Fix icônes dynamiques (import `icons.main.min.css` pour le Header)
- Composants : Header, Footer, Button, Card, Alert, Input, Select, etc.

### rgaa

Outil d'audit de conformité [RGAA 4.1.2](https://accessibilite.numerique.gouv.fr/) — 106 critères d'accessibilité numérique.

Fournir du code HTML/React à auditer → rapport de conformité structuré avec statut C/NC/NA par critère, liste des non-conformités et corrections priorisées (🔴 Bloquant, 🟠 Majeur, 🟡 Mineur).

- Workflow d'audit en 4 étapes et format de rapport standardisé
- 106 critères avec test de code, non-conformité type et priorité
- Couvre les 13 thèmes : images, cadres, couleurs, multimédia, tableaux, liens, scripts, structure, présentation, formulaires, navigation, consultation
- Export du rapport d'audit dans `audits/rgaa-YYYY-MM-DD.md`
- Basé sur WCAG 2.1 niveau AA

### lasuite-ui-kit

Créer des interfaces React pour les applications [LaSuite](https://lasuite.numerique.gouv.fr/) avec `@gouvfr-lasuite/ui-kit` et `@gouvfr-lasuite/cunningham-react`.

- Layout applicatif (MainLayout, Header, Footer, Hero)
- Composants de navigation (DropdownMenu, ContextMenu, TreeView, Tabs)
- Recherche rapide (QuickSearch), partage (ShareModal), badges, icônes Material
- Composants de base Cunningham (Button, Input, Select, Modal, DataGrid)
- Setup Vite / Next.js (App Router & Pages Router)

### securite-anssi

12 règles essentielles de sécurité issues du [guide d'hygiène ANSSI](https://cyber.gouv.fr/publications/guide-dhygiene-informatique).

- Workflow d'audit structuré et grille de priorités (🔴 Critique, 🟠 Élevé, 🟡 Modéré)
- TLS/HTTPS, gestion des secrets, authentification
- Headers de sécurité, validation des entrées
- Dépendances, logs, conteneurs, incidents
- Export du rapport d'audit dans `audits/securite-anssi-YYYY-MM-DD.md`

### datagouv-apis

Référence consolidée des 3 APIs de [data.gouv.fr](https://www.data.gouv.fr/) pour interagir avec la plateforme de données ouvertes.

- API principale (catalogue : datasets, organisations, réutilisations, ressources)
- API Metrics (statistiques d'usage par modèle)
- API Tabulaire (requêter les données CSV par resource ID)
- Skill synchronisée automatiquement depuis [datagouv/datagouv-skill](https://github.com/datagouv/datagouv-skill)

## Templates d'instructions

Fichiers `INSTRUCTIONS.md` prêts à l'emploi pour configurer un assistant de code IA sur un projet de l'État. Copier le fichier correspondant à la racine de votre projet sous le nom `INSTRUCTIONS.md` ou `CLAUDE.md`.

| Template | Écosystème | Design System | Package manager |
|----------|-----------|---------------|-----------------|
| [`beta.gouv.md`](templates/instructions/beta.gouv.md) | [beta.gouv.fr](https://beta.gouv.fr/) | DSFR (`@codegouvfr/react-dsfr`) | pnpm |
| [`LaSuite.md`](templates/instructions/LaSuite.md) | [La Suite numérique](https://lasuite.numerique.gouv.fr/) | UI Kit + Cunningham | yarn |

Chaque template inclut : conventions de langue, design system, accessibilité RGAA, sécurité ANSSI, RGPD, stack recommandée, tests, conventions Git et références vers les skills pertinentes de ce repo.

Le template `beta.gouv.md` inclut également : Definition of Done (boucle tests → vérification navigateur → correction), CI GitHub Actions, pre-commit Husky (`pnpm validate`), contrainte sur les dépendances, section Expected Behavior (Plan Mode, gestion des tâches, self-improvement loop), section Architecture et guides de personnalisation.

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
