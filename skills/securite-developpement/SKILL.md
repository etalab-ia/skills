---
name: securite-developpement
description: "Règles essentielles de sécurité pour le développement d'applications de l'État, générées par la DINUM en s'appuyant sur 13 guides produits par l'ANSSI. 14 domaines couvrant TLS, cryptographie, secrets, authentification multifacteur, entrées et bases de données, dépendances, journalisation, sécurité navigateur et API, cloisonnement système, conteneurs, chaîne CI/CD, poste de développement, sauvegarde et incidents — plus des modules pour le langage C, Rust et les CMS. Utiliser cette skill quand l'utilisateur développe une application web, une API ou tout service exposé, quand il mentionne la sécurité, l'ANSSI, le durcissement, la cryptographie, le chiffrement, le DevSecOps ou le cloisonnement, et quand on configure un serveur, un reverse proxy, une base de données ou un pipeline CI/CD."
---

# Sécurité — Règles essentielles pour le développement

Règles de sécurité pour le développement d'applications de l'État, générées par la DINUM en s'appuyant sur 13 guides publiés par l'ANSSI. La liste des guides, leur version et la correspondance avec chaque domaine figurent dans [`references/sources.md`](references/sources.md).

Source : https://cyber.gouv.fr/reglementation/cybersecurite-systemes-dinformation/

---

## Deux modes d'usage

### Mode conseil — pendant le développement

Quand on écrit du code, qu'on configure un serveur, un reverse proxy, une base de données ou un pipeline CI/CD, appliquer directement les règles du ou des domaines concernés, **sans produire de rapport**.

- Consulter le ou les domaines pertinents de [`references/checklist.md`](references/checklist.md).
- Dès qu'une valeur concrète est en jeu — version de TLS, suite cryptographique, taille de clé, courbe elliptique, fonction de dérivation de mot de passe, durée de rétention des journaux — la reprendre depuis [`references/valeurs-anssi.md`](references/valeurs-anssi.md). **Ne jamais inventer ni approximer ces valeurs de mémoire.**
- Signaler à l'utilisateur la règle appliquée et sa source ANSSI quand elle contraint un choix technique.

### Mode audit — évaluation de conformité

Quand l'utilisateur demande un audit, un rapport de conformité, ou de vérifier la sécurité d'un projet existant, dérouler le workflow ci-dessous.

### Hors périmètre

Pour une question de sécurité hors des 14 domaines — architecture réseau, pare-feu, DNS, Active Directory, remédiation, systèmes industriels, IA générative… — utiliser la skill [`anssi-guides`](../anssi-guides/SKILL.md), qui cherche dans l'ensemble du catalogue ANSSI (128 guides).

---

## Workflow d'audit

1. **Analyser le projet** (code source, configuration, infrastructure, CI/CD)
2. **Sélectionner les modules applicables** (voir ci-dessous) — aucun module n'est chargé par défaut
3. **Parcourir les 14 domaines** de la checklist détaillée dans [`references/checklist.md`](references/checklist.md), puis les modules retenus
4. **Pour chaque règle**, attribuer un statut :
   - **OK** — Règle respectée
   - **KO** — Règle non respectée (identifier le problème et le risque)
   - **NA** — Non applicable (justifier)
   - **Partiel** — Partiellement respectée (préciser ce qui manque)
5. **Qualifier l'exploitabilité de chaque KO** : distinguer une faille **exploitable** (activable en l'état → chemin d'attaque réel) d'une **bonne pratique manquante** (défense en profondeur, sans exploitation directe). Cette qualification alimente la priorité.
6. **Valider les non-conformités** : avant de finaliser, re-vérifier chaque KO contre le code et la configuration réels. Écarter les faux positifs, ou requalifier le statut/l'exploitabilité si le constat ne tient pas. Ne conserver que les constats étayés par une preuve concrète (fichier, ligne, réglage).
7. **Produire le rapport structuré** selon le format défini dans [`references/rapport.md`](references/rapport.md)
8. **Exporter le rapport** : écrire le rapport dans un fichier Markdown ET l'afficher dans la conversation (règles d'export dans [`references/rapport.md`](references/rapport.md)). Une sortie structurée JSON optionnelle est disponible au format `securite-developpement-AAAA-MM-JJ.json` (schéma : [`references/findings-schema.json`](references/findings-schema.json)).

---

## Les 14 domaines du socle

| # | Domaine | # | Domaine |
|---|---------|---|---------|
| 1 | TLS / HTTPS | 8 | Sécurité navigateur et API |
| 2 | Cryptographie | 9 | Cloisonnement système |
| 3 | Gestion des secrets | 10 | Conteneurs et déploiement |
| 4 | Authentification, MFA et mots de passe | 11 | Chaîne de développement (CI/CD) |
| 5 | Validation des entrées et bases de données | 12 | Poste de développement |
| 6 | Dépendances et composants tiers | 13 | Sauvegarde et continuité |
| 7 | Journalisation | 14 | Gestion des incidents |

## Sélection des modules conditionnels

Les modules ne sont **ni chargés ni audités par défaut**. Détecter la stack du projet et ne retenir que les modules dont le déclencheur est effectivement présent :

| Module | Charger si |
|--------|-----------|
| [`references/modules/langage-c.md`](references/modules/langage-c.md) | présence de fichiers `*.c` / `*.h`, `Makefile`, `CMakeLists.txt` |
| [`references/modules/langage-rust.md`](references/modules/langage-rust.md) | présence de `Cargo.toml` / `Cargo.lock` |
| [`references/modules/cms.md`](references/modules/cms.md) | CMS détecté : `wp-config.php` (WordPress), Drupal, Joomla, ou hébergement CMS géré |

Un module non chargé n'apparaît pas dans le rapport et ne compte pas dans le résultat global.

---

## Traçabilité des règles

Chaque règle de la checklist porte entre crochets l'origine de son exigence :

- `[TLS R3]`, `[MFA R29]`, `[CRYPTO R5]`… — recommandation numérotée d'un guide ANSSI, citée par son identifiant exact. Les suffixes `-` et `--` (ex. `[MFA R29-]`) désignent des alternatives dégradées, à n'utiliser que si la recommandation nominale est hors d'atteinte.
- `[ESS-DEVSECOPS]`, `[ESS-BDD]`, `[ESS-LIBRE]`, `[ESS-CMS]` — les « Essentiels » de l'ANSSI **ne numérotent pas** leurs recommandations : elles sont citées par guide, le libellé exact figurant dans [`references/sources.md`](references/sources.md).
- `[DINUM]` — bonne pratique de place retenue par la DINUM, **sans équivalent dans les guides ANSSI**. Ne jamais la présenter comme une exigence de l'ANSSI.

---

## Références

| Fichier | Contenu |
|---------|---------|
| [`references/checklist.md`](references/checklist.md) | Les 14 domaines du socle (règles à vérifier, avec leur source) |
| [`references/valeurs-anssi.md`](references/valeurs-anssi.md) | Valeurs chiffrées à citer sans les réinventer (crypto, TLS, mots de passe, journaux) |
| [`references/sources.md`](references/sources.md) | Les 13 guides ANSSI : version, URL, date de consultation, domaines alimentés |
| [`references/modules/`](references/modules/) | Modules conditionnels : langage C, Rust, CMS |
| [`references/rapport.md`](references/rapport.md) | Format du rapport, grille de priorités, export, sortie JSON optionnelle |
| [`references/findings-schema.json`](references/findings-schema.json) | JSON Schema de la sortie structurée optionnelle (`securite-developpement-AAAA-MM-JJ.json`) |
