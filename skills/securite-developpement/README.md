# securite-developpement

Skill pour assistants de code IA — règles essentielles de sécurité pour le développement d'applications de l'État, générées par la DINUM en s'appuyant sur **13 guides publiés par l'ANSSI**.

**14 domaines** dans le socle, plus **3 modules conditionnels** (langage C, Rust, CMS) chargés uniquement si le projet est concerné.

## Ce que fait cette skill

La skill a **deux modes** :

- **Mode conseil** — pendant le développement. Quand l'assistant écrit du code, configure un serveur, un reverse proxy, une base de données ou un pipeline CI/CD, il applique les règles du domaine concerné et reprend les valeurs exactes de l'ANSSI (suites TLS, tailles de clés, paramètres de dérivation de mots de passe) sans les réinventer.
- **Mode audit** — évaluation de conformité. Production d'un rapport structuré avec grille de priorités (🔴 Critique, 🟠 Élevé, 🟡 Modéré), qualification de l'exploitabilité de chaque non-conformité et étape de validation des faux positifs. Export dans `audits/securite-developpement-AAAA-MM-JJ.md`, avec une sortie JSON machine-lisible optionnelle.

## Traçabilité

Chaque règle porte l'origine de son exigence entre crochets :

- `[TLS R3]`, `[MFA R29]`, `[CRYPTO R16]` — recommandation numérotée d'un guide, citée par son identifiant exact. Les suffixes `-` et `--` désignent des **alternatives dégradées**, à n'utiliser que si la recommandation nominale est hors d'atteinte.
- `[ESS-DEVSECOPS]`, `[ESS-BDD]`, `[ESS-LIBRE]`, `[ESS-CMS]` — les « Essentiels » de l'ANSSI **ne numérotent pas** leurs recommandations ; le libellé exact fait foi.
- `[DINUM]` — bonne pratique retenue par la DINUM, **sans équivalent dans les guides ANSSI**. Jamais présentée comme une exigence de l'ANSSI.

Ce dernier point est délibéré : plusieurs mesures usuelles (protection des branches, SBOM en CI, scan d'images, `X-Content-Type-Options`, critère de licence) **ne figurent dans aucun des 13 guides**. Elles restent recommandées, mais correctement attribuées.

## Les 13 guides couverts

Guide d'hygiène informatique (42 mesures) · Sécurisation des sites web · Authentification multifacteur et mots de passe · Sélection d'algorithmes cryptographiques (+ dimensionnement des mécanismes) · TLS · Architecture d'un système de journalisation · Cloisonnement système · Essentiel DevSecOps · Essentiel Bases de données relationnelles · Essentiel Sélection d'un logiciel libre · Essentiel Mise en œuvre sécurisée d'un CMS · Règles de programmation en langage C · Règles de programmation en Rust.

Versions, URLs, dates de consultation et divergences entre guides : [`references/sources.md`](references/sources.md).

## Contenu

| Fichier | Description |
|---------|-------------|
| [`SKILL.md`](SKILL.md) | Les deux modes, workflow d'audit, sélection des modules, conventions de citation |
| [`references/checklist.md`](references/checklist.md) | Les 14 domaines du socle, chaque règle tracée à sa source |
| [`references/valeurs-anssi.md`](references/valeurs-anssi.md) | Valeurs chiffrées à citer sans les réinventer (crypto, TLS, mots de passe, journaux) |
| [`references/sources.md`](references/sources.md) | Les 13 guides : version, URL, structure, ce qu'ils ne couvrent pas |
| [`references/modules/`](references/modules/) | Modules conditionnels : [langage C](references/modules/langage-c.md), [Rust](references/modules/langage-rust.md), [CMS](references/modules/cms.md) |
| [`references/rapport.md`](references/rapport.md) | Format du rapport, grille de priorités, export, sortie JSON optionnelle |
| [`references/findings-schema.json`](references/findings-schema.json) | JSON Schema de la sortie structurée optionnelle |

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

**Mode conseil**

- *"Configure nginx en TLS pour ce service"*
- *"Comment stocker les mots de passe de cette application ?"*
- *"Ajoute une CSP à cette page"*

**Mode audit**

- *"Audite la sécurité de mon API Express"*
- *"Vérifie que je ne stocke pas de secrets en dur dans le code"*
- *"Génère un rapport de sécurité pour ce projet"*

## Changement de référentiel

Le passage de 12 à 14 domaines **modifie la numérotation** : les audits produits avec la version précédente ne sont pas directement comparables aux nouveaux. Le domaine « Headers de sécurité HTTP » a notamment été absorbé par le domaine 8 (Sécurité navigateur et API), au sens du guide ANSSI *Recommandations pour la mise en œuvre d'un site web*.

## Liens utiles

- [Guide d'hygiène informatique ANSSI](https://messervices.cyber.gouv.fr/guides/guide-dhygiene-informatique)
- [Mes services cyber — guides de l'ANSSI](https://messervices.cyber.gouv.fr/)
- [ANSSI — Agence nationale de la sécurité des systèmes d'information](https://cyber.gouv.fr/)

## Licence

MIT
