# dsfr

Skill pour assistants de code IA — documentation du [Système de design de l'État](https://www.systeme-de-design.gouv.fr/) (DSFR) en HTML et CSS : composants, fondamentaux, modèles de pages et de formulaires, accessibilité, avec le HTML officiel de chaque variante.

> [!CAUTION]
> **Usage réservé à l'État.** Les [modalités d'utilisation du DSFR](https://github.com/GouvernementFR/dsfr/blob/main/doc/legal/cgu.md) le réservent aux sites en .gouv.fr et aux applications mobiles des services de l'État (et des opérateurs agréés par leur ministère de tutelle). Hors de ce cadre, il peut créer une confusion avec un service public officiel, réprimée par l'article 433-13 du code pénal. La skill demande à l'assistant de vérifier que le projet relève de l'État et de refuser sinon.

> **Note** : cette skill est synchronisée automatiquement depuis le repo upstream [`numerique-gouv/dsfr-skill`](https://github.com/numerique-gouv/dsfr-skill), où elle est générée depuis le paquet npm `@gouvfr/dsfr` (version dans [`VERSION.md`](VERSION.md)). Le générateur, les évals et le plugin Claude Code y restent : pour contribuer, ouvrir une PR sur le repo upstream. Un workflow GitHub Actions vérifie chaque semaine (lundi 9h UTC) si le contenu a changé et ouvre une PR de synchronisation le cas échéant. Seul ce README est propre à ce repo.

## Ce que fait cette skill

Quand elle est activée, l'assistant IA sait :

- **Écrire le HTML officiel** des 51 composants, en partant des exemples du paquet et de la liste des classes `fr-*` et icônes existantes, sans en inventer
- **Appliquer les fondamentaux** : grille, couleurs et thème sombre, typographie, espacements, icônes et pictogrammes
- **Assembler des pages et formulaires** à partir des modèles officiels (connexion, création de compte, pages d'erreur, blocs nom, adresse, date…)
- **Vérifier une page** avec `scripts/verifier.mjs` (Node, sans dépendance) : `id` en double, références ARIA cassées, champs sans libellé, CDN non versionné, classes inconnues
- **Partir de l'intégration existante** du projet et signaler une version du DSFR différente de celle documentée

## Quand utiliser `dsfr`, `react-dsfr` ou `rgaa`

| Besoin | Skill |
|--------|-------|
| HTML et CSS avec les classes `fr-*`, sans framework ou avec un moteur de gabarits (Twig, Jinja, ERB…) | **dsfr** |
| Projet React avec `@codegouvfr/react-dsfr` | [**react-dsfr**](../react-dsfr/) |
| Audit de conformité RGAA complet (106 critères) | [**rgaa**](../rgaa/) |

## Contenu

| Fichier | Description |
|---------|-------------|
| [`SKILL.md`](SKILL.md) | Usage réservé à l'État, règles et index des fichiers |
| [`demarrage.md`](demarrage.md) | Imports, squelette de page, thème, JS, intégration dans un framework |
| [`audit.md`](audit.md) | Démarche d'audit d'une page DSFR |
| `composants/<nom>/` | Par composant : index, design, code, accessibilité, exemples HTML |
| `fondamentaux/<nom>/` | Grille, couleurs, typographie, espacements, icônes… |
| `modeles/` | Modèles de pages et blocs de formulaire |
| `reference/` | Classes CSS, icônes et pictogrammes de la version |
| [`scripts/verifier.mjs`](scripts/verifier.mjs) | Vérificateur HTML sans dépendance |

La skill compte 345 fichiers : avec la config `skills.urls` d'OpenCode, son installation déclenche autant de requêtes vers GitHub raw.

## Installation

```bash
# Avec Vercel Skills CLI (recommandé)
npx skills add etalab-ia/skills --skill dsfr

# Claude Code
npx skills add etalab-ia/skills --skill dsfr -a claude-code

# OpenCode
npx skills add etalab-ia/skills --skill dsfr -a opencode
```

La même skill reste installable comme plugin Claude Code depuis le repo upstream (`/plugin marketplace add numerique-gouv/dsfr-skill`), sous le nom `dsfr-skill` : n'installer que l'une des deux copies.

## Exemples d'utilisation

Une fois la skill installée, l'assistant IA peut répondre à des demandes comme :

- *"Fais-moi une page de connexion DSFR"*
- *"Ajoute un formulaire avec gestion des erreurs conforme au DSFR"*
- *"Quelles sont les règles d'accessibilité pour un accordéon ?"*
- *"Audite cette page : respecte-t-elle le DSFR ?"*

## Liens utiles

- [Système de design de l'État](https://www.systeme-de-design.gouv.fr/)
- [`@gouvfr/dsfr` sur GitHub](https://github.com/GouvernementFR/dsfr)
- [numerique-gouv/dsfr-skill](https://github.com/numerique-gouv/dsfr-skill) — générateur, évals, plugin Claude Code
