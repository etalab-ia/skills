# react-dsfr

Skill pour assistants de code IA — créer des interfaces React conformes au [Design System de l'État](https://www.systeme-de-design.gouv.fr/) avec [`@codegouvfr/react-dsfr`](https://github.com/codegouvfr/react-dsfr).

## Ce que fait cette skill

Quand elle est activée, l'assistant IA sait :

- **Générer des composants** conformes au DSFR : Header, Footer, Button, Card, Alert, Input, Select, Modal, etc.
- **Configurer le setup** selon le framework : Vite, Next.js (App Router & Pages Router), Create React App
- **Appliquer les bons patterns** : import par composant, routing, grille 12 colonnes, icônes DSFR/Remix, couleurs du thème, dark mode sans flash
- **Éviter les erreurs courantes** : imports Next.js App Router (v1.30+), icônes dynamiques, config ESLint

## Contenu

| Fichier | Description |
|---------|-------------|
| [`SKILL.md`](SKILL.md) | Instructions principales — patterns, composants, exemples de mise en page |
| [`references/setup.md`](references/setup.md) | Installation et configuration par framework (Vite, Next.js, CRA) |
| [`references/components.md`](references/components.md) | Référence complète des composants : props, types, exemples |

## Installation

```bash
# Avec Vercel Skills CLI (recommandé)
npx skills add etalab-ia/skills --skill react-dsfr

# Claude Code
npx skills add etalab-ia/skills --skill react-dsfr -a claude-code

# OpenCode
npx skills add etalab-ia/skills --skill react-dsfr -a opencode
```

## Exemples d'utilisation

Une fois la skill installée, l'assistant IA peut répondre à des demandes comme :

- *"Crée une page avec un Header, un Breadcrumb et un formulaire de contact"*
- *"Configure react-dsfr sur mon projet Next.js App Router"*
- *"Ajoute une grille de Cards avec pagination"*
- *"Corrige le flash de dark mode sur mon app Next.js"*

## Liens utiles

- [react-dsfr sur GitHub](https://github.com/codegouvfr/react-dsfr)
- [Storybook react-dsfr](https://components.react-dsfr.codegouv.studio/)
- [Design System de l'État](https://www.systeme-de-design.gouv.fr/)

## Licence

MIT
