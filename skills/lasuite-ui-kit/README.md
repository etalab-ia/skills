# lasuite-ui-kit

Skill pour assistants de code IA — créer des interfaces React pour les applications [LaSuite](https://lasuite.numerique.gouv.fr/) avec [`@gouvfr-lasuite/ui-kit`](https://github.com/suitenumerique/ui-kit) et [`@gouvfr-lasuite/cunningham-react`](https://github.com/openfun/cunningham).

## Ce que fait cette skill

Quand elle est activée, l'assistant IA sait :

- **Générer des interfaces** avec le layout applicatif LaSuite : MainLayout, Header, Footer, Hero
- **Utiliser les composants de navigation** : DropdownMenu, ContextMenu, TreeView, Tabs
- **Intégrer les patterns LaSuite** : QuickSearch, ShareModal, badges, icônes Material
- **Utiliser les composants Cunningham** : Button, Input, Select, Modal, DataGrid
- **Configurer le setup** selon le framework : Vite, Next.js (App Router & Pages Router)

## Contenu

| Fichier | Description |
|---------|-------------|
| [`SKILL.md`](SKILL.md) | Instructions principales — patterns, composants, setup |
| [`references/components.md`](references/components.md) | Référence composants `@gouvfr-lasuite/ui-kit` |
| [`references/cunningham.md`](references/cunningham.md) | Référence composants Cunningham (Button, Input, Select, Modal, DataGrid) |
| [`references/setup.md`](references/setup.md) | Installation et configuration par framework |

## Installation

```bash
# Avec Vercel Skills CLI (recommandé)
npx skills add etalab-ia/skills --skill lasuite-ui-kit

# Claude Code
npx skills add etalab-ia/skills --skill lasuite-ui-kit -a claude-code

# OpenCode
npx skills add etalab-ia/skills --skill lasuite-ui-kit -a opencode
```

## Exemples d'utilisation

Une fois la skill installée, l'assistant IA peut répondre à des demandes comme :

- *"Crée une page avec le layout LaSuite, un Header et un TreeView en sidebar"*
- *"Ajoute un DataGrid Cunningham avec tri et pagination"*
- *"Configure ui-kit sur mon projet Next.js App Router"*
- *"Intègre un QuickSearch avec les résultats filtrés"*

## Liens utiles

- [LaSuite](https://lasuite.numerique.gouv.fr/)
- [UI Kit sur GitHub](https://github.com/suitenumerique/ui-kit)
- [Cunningham sur GitHub](https://github.com/openfun/cunningham)
- [Storybook Cunningham](https://openfun.github.io/cunningham/)

## Licence

MIT
