# Sources — les 13 guides ANSSI

Table de traçabilité des règles de [`checklist.md`](checklist.md) et des [`modules/`](modules/). Chaque règle porte entre crochets un identifiant qui se résout ici.

**Date de consultation des guides : 2026-07-20.** Les versions ci-dessous sont celles en vigueur à cette date ; en cas de révision ANSSI, rejouer l'extraction (méthode en fin de fichier).

---

## Conventions de citation

| Forme | Signification |
|-------|---------------|
| `[TLS R7]` | Recommandation numérotée d'un guide ANSSI, citée par son identifiant exact |
| `[TLS R7-]` | **Alternative dégradée** — niveau de sécurité moindre, à n'utiliser que si la recommandation nominale est hors d'atteinte pour des raisons de compatibilité |
| `[LOG R23+]` | **Alternative renforcée** — au-delà de l'exigence nominale |
| `[ESS-BDD]` | « Essentiel » de l'ANSSI : ces fiches **ne numérotent pas** leurs recommandations. Le libellé exact fait foi et figure ci-dessous |
| `[ESS-CMS 3]` | Idem, avec un repère de position **ajouté par la DINUM** pour la traçabilité — le chiffre n'est pas de l'ANSSI |
| `[C RÈGLE 168]` | Guide C : numérotation globale 1–181, avec le type imprimé (`RÈGLE`, `RECOMMANDATION`, `BONNE PRATIQUE`) |
| `[DINUM]` | **Bonne pratique DINUM sans équivalent dans les guides ANSSI.** Ne jamais la présenter comme une exigence de l'ANSSI |

> **Règle d'or.** Un identifiant ne s'invente pas. Si une règle utile n'a pas de source ANSSI vérifiée, elle est marquée `[DINUM]` — c'est plus honnête, et c'est vérifiable.

---

## Les guides

### 1. Guide d'hygiène informatique — `HYGIENE M<n>`

- **Titre** : *Guide d'hygiène informatique — Renforcer la sécurité de son système d'information en 42 mesures*
- **Version** : 2.0 — septembre 2017 (1re version : janvier 2013)
- **URL** : https://messervices.cyber.gouv.fr/guides/guide-dhygiene-informatique
- **Structure** : 42 mesures numérotées, réparties en 10 thèmes. Deux niveaux : *standard* (par défaut) et *renforcé*. Les mesures **38, 41 et 42** sont exclusivement *renforcé*.
- **Domaines alimentés** : 3, 4, 6, 12, 13, 14 (et partiellement 1, 7, 9, 10)
- **Périmètre retenu** : **30 mesures sur 42** sont applicables par une équipe produit. Les 12 autres (7, 15, 16, 19, 20, 22, 24, 25, 26, 27, 28, 33) supposent la maîtrise du réseau physique, du parc bureautique ou des locaux — leviers d'une DSI ministérielle, pas d'une équipe produit. Elles ne sont pas reprises dans la checklist.

> ⚠️ L'ancienne URL `cyber.gouv.fr/publications/guide-dhygiene-informatique` renvoie un **301**.

### 2. Sécurisation des sites web — `WEB R<n>`

- **Titre** : *Recommandations pour la mise en œuvre d'un site web : maîtriser les standards de sécurité côté navigateur*
- **Référence** : ANSSI-PA-009 — **version 2.0** — 28/04/2021
- **URL** : https://messervices.cyber.gouv.fr/guides/securiser-un-site-web
- **Structure** : **63 recommandations R1–R63**, avec des variantes `-` (dégradées : R14-, R23-, R24-, R36-, R42-) et `+` (renforcées : R36+, R48+, R52+)
- **Domaines alimentés** : 8 (principal), 1, 5, 6
- **Portée** : mécanismes de sécurité **côté navigateur** — TLS/HSTS, XSS, CSP, Referrer-Policy, Web Storage et cookies, XHR/CORS, HTML5/JavaScript, iframes et Web Workers, maintien en condition

> ⚠️ L'ancienne URL `cyber.gouv.fr/publications/securiser-un-site-web` renvoie un **301**.
> ⚠️ **`X-Content-Type-Options` n'apparaît pas dans ce guide.** La maîtrise du typage y passe par R6 (`Content-Type` explicite). Une règle exigeant `nosniff` est donc `[DINUM]`.

### 3. Authentification multifacteur et mots de passe — `MFA R<n>`

- **Titre** : *Recommandations relatives à l'authentification multifacteur et aux mots de passe*
- **Référence** : ANSSI-PG-078 — **version 2.0** — 08/10/2021 (réécriture complète ; contribution de la CNIL)
- **URL** : https://messervices.cyber.gouv.fr/documents-guides/anssi-guide-authentification_multifacteur_et_mots_de_passe.pdf
- **Structure** : **42 recommandations R1–R42**, plus 3 variantes dégradées : **R29-, R39-, R39--**
- **Domaines alimentés** : 4 (principal), 3, 7

### 4. Sélection d'algorithmes cryptographiques — `CRYPTO R<n>` et `CRYPTO-DIM`

Deux documents, à ne pas confondre.

**4a. Guide développeur — `CRYPTO R<n>`**
- **Titre** : *Guide de sélection d'algorithmes cryptographiques*
- **Référence** : ANSSI-PA-079 — **version 1.0** — 08/03/2021
- **Structure** : **27 recommandations R1–R27**, sans variantes dégradées. Le caractère dégradé est porté par la colonne `R/O` des tableaux : `R` = recommandé, `O` = obsolescent (toléré à court terme), `R*` = utilisable seulement comme brique d'une construction recommandée.

**4b. Guide de dimensionnement — `CRYPTO-DIM <NomDeRègle>`**
- **Titre** : *Règles et recommandations concernant le choix et le dimensionnement des mécanismes cryptographiques*
- **Référence** : ANSSI-PG-083 — **version 3.00** — 20/03/2026 — révision « menace quantique prise en compte »
- **Structure** : identifiants **nominatifs** (`RègleTailleCléSym`, `RecoPQHachage`, `RecoFactorisation.1`…), 23 règles et 23 recommandations.

- **URL commune** : https://messervices.cyber.gouv.fr/guides/mecanismes-cryptographiques
- **Domaines alimentés** : 2 (principal), 1, 4

> ⚠️ **En cas de divergence, PG-083 v3.00 (2026) prévaut sur PA-079 v1.0 (2021)** : il est plus récent de cinq ans et intègre la menace quantique. Le guide développeur n'a jamais été révisé depuis 2021.
> ⚠️ La page vitrine affiche une date de publication unique qui correspond à PG-083, pas au guide développeur.

### 5. TLS — `TLS R<n>`

- **Titre** : *Recommandations de sécurité relatives à TLS*
- **Référence** : SDE-NT-35/ANSSI/SDE/NP — **version 1.2** — 26/03/2020
- **URL** : https://messervices.cyber.gouv.fr/guides/recommandations-de-securite-relatives-tls
- **Structure** : **39 recommandations R1–R39**, plus 6 dégradées : **R7-, R8-, R9-, R10-, R18-, R21-**
- **Domaines alimentés** : 1 (principal), 2

> ⚠️ **R31 n'a pas de titre imprimé** dans le guide (l'encadré ne porte que l'identifiant) — ce n'est pas une omission de notre part.
> ⚠️ Guide de 2020 : il précède PG-083 v3.00 sur les tailles de clés. Pour tout dimensionnement, se référer à [`valeurs-anssi.md`](valeurs-anssi.md).

### 6. Architecture d'un système de journalisation — `LOG R<n>`

- **Titre** : *Recommandations de sécurité pour l'architecture d'un système de journalisation*
- **Référence** : ANSSI-PA-012 — **version 2.0** — 28/01/2022
- **URL** : https://messervices.cyber.gouv.fr/documents-guides/anssi-guide-recommandations_securite_architecture_systeme_journalisation.pdf
- **Structure** : **31 recommandations R1–R31**, plus les variantes **R9-, R14-, R20-** (dégradées) et **R23+, R26+** (renforcées)
- **Domaines alimentés** : 7 (principal), 9, 12
- **À noter** : l'**annexe A** définit le *socle minimal de journalisation* (les catégories d'événements à collecter) et l'**annexe C** introduit la détection d'incidents. Ce sont les parties les plus directement exploitables pour une application.

### 7. Cloisonnement système — `CLOIS R<n>`

- **Titre** : *Recommandations pour la mise en place de cloisonnement système*
- **Référence** : ANSSI-PG-040 — **version 1.0** — 14/12/2017
- **URL** : https://messervices.cyber.gouv.fr/guides/recommandations-pour-la-mise-en-place-de-cloisonnement-systeme
- **Structure** : **25 recommandations R1–R25**, sans variantes. Pas d'annexe récapitulative : les recommandations sont en encadrés dans le corps du texte.
- **Domaines alimentés** : 9 (principal), 10, 5
- **Nature** : guide **méthodologique**, pas prescriptif au niveau technique. Il ne fournit ni configuration Docker/Kubernetes, ni profil seccomp, ni liste de capabilities. Les prescriptions concrètes se trouvent dans l'étude de cas du chapitre 5.

> ⚠️ **Guide de 2017, jamais révisé.** Certaines références sont datées (CoreOS Rkt abandonné en 2020, grsecurity non public depuis 2017) et il ne couvre ni seccomp-bpf, ni gVisor, ni les conteneurs rootless, ni les Pod Security Standards Kubernetes. **La méthode d'analyse reste valide** ; les mesures techniques modernes correspondantes sont `[DINUM]`.

### 8. Essentiel « DevSecOps » — `ESS-DEVSECOPS`

- **Titre** : *Les Essentiels — DevSecOps* — **V1.0 (02/24)**, publication 13/03/2024
- **URL** : https://messervices.cyber.gouv.fr/guides/devsecops
- **Structure** : fiche **d'une seule page**, **13 puces non numérotées**. Aucun identifiant.
- **Domaines alimentés** : 11 (principal), 3, 6, 10

Libellés exacts des 13 recommandations, dans l'ordre du document :

1. Réaliser et maintenir à jour une cartographie des applications utilisées
2. Faire une analyse de risque globale (postes des développeurs, sous-traitance, chaîne CI/CD, technologies)
3. Considérer que les actions réalisées par la CI/CD de production sont des actions d'administration — poste d'administration dédié, moindre privilège, jetons générés à la demande, journalisation et supervision
4. Gérer les secrets de manière sécurisée — gestionnaire de secrets distinct par environnement ; absence de secrets en dur dans le code, les journaux de *jobs* et les dépôts
5. Gérer les dépendances avec rigueur : les minimiser, les évaluer et appliquer les correctifs de sécurité avant déploiement
6. Prévoir des tests de sécurité automatisés dans la CI/CD — non-régression, étanchéité entre profils d'utilisateurs, analyses statique et dynamique, conformité de l'IaC
7. Sécuriser le déploiement en production — intégrité du code de bout en bout, signature et vérification des signatures des tags de version des artefacts
8. Implémenter une authentification multifacteur pour l'accès aux dépôts et pour la signature des *commits*
9. Séparer les infrastructures CI/CD de développement et de production, et ne pas les exposer directement sur Internet
10. Réinstancier régulièrement l'infrastructure CI/CD et ne pas y stocker de données persistantes
11. Être vigilants sur les besoins en confidentialité vis-à-vis de l'infrastructure de CI/CD
12. Imposer des règles de développements sécurisés dans les équipes
13. Appliquer des règles de durcissement sur les OS hébergeant les applications

> ⚠️ **Absents de cette fiche** : protection des branches, revue de code obligatoire, SBOM, scan d'images de conteneurs, acronymes SAST/DAST/SCA, positionnement des contrôles dans le pipeline, processus de gestion des vulnérabilités. Ces exigences sont `[DINUM]`.

### 9. Essentiel « Bases de données relationnelles » — `ESS-BDD`

- **Titre** : *Les Essentiels — Bases de données relationnelles* — **V1.0 (12/24)**, publication 31/01/2025
- **URL** : https://messervices.cyber.gouv.fr/guides/bases-de-donnees-relationnelles
- **Structure** : fiche 2 pages, **10 recommandations non numérotées**
- **Domaines alimentés** : 5 (principal), 4, 7, 13

Les 10 recommandations : maintenir à jour le SGBD · sécuriser l'administration des serveurs et minimiser les extensions · journaliser les événements et accès administrateurs · sécuriser les accès (comptes distincts humains/applications, authentification systématique, compte administrateur natif en dernier recours, MFA administrateurs) · appliquer le moindre privilège (droits au strict nécessaire, rôles) · durcir la configuration (isolation données/configuration, désactivation des fonctions de lecture-écriture-exécution de fichiers système, typage imposé) · paramétrer la sauvegarde · protéger les données sensibles (pas de données de production hors production, vigilance SaaS mutualisé, chiffrement *on-transit* et *at-rest*, un serveur par niveau de sensibilité, vues) · **bonnes pratiques de développement pour l'accès aux BDD, ex. requêtes préparées contre les injections** · superviser la BDD.

> ⚠️ **Non traités** : exposition réseau du SGBD, séparation lecture/écriture, migrations de schéma. Ne pas les attribuer à ce guide.
> ⚠️ Les identifiants `R58`–`R61`, `R3`, `R9`, `R26`, `R27` cités dans cette fiche **renvoient à d'autres guides** ANSSI, ce ne sont pas ses propres recommandations.

### 10. Essentiel « Sélection d'un logiciel libre » — `ESS-LIBRE`

- **Titre** : *Les Essentiels — Sélection d'un logiciel libre* — **V1.0 (05/25)**
- **URL** : https://messervices.cyber.gouv.fr/documents-guides/anssi_essentiels_selection_logiciel_libre_1.0.pdf
- **Structure** : dépliant 2 pages, **10 critères non numérotés**. L'ANSSI le présente comme « une liste de critères », en précisant : « **Il n'est pas nécessaire pour un projet d'obtenir un score parfait.** »
- **Domaines alimentés** : 6 (principal)

Les critères : historique et notoriété du projet · maintien en conditions opérationnelles (MCO) · maintien en conditions de sécurité (MCS : point de contact sécurité, procédure publique de gestion des vulnérabilités, délai de correction des vulnérabilités critiques) · **inventaire et surveillance des dépendances (SBOM au format SPDX ou CycloneDX, dépendances à jour et sans vulnérabilité connue, outils enrichis en données de vulnérabilité)** · analyses de sécurité tierces (visa de sécurité ANSSI) · qualité du socle technique (documentation, configuration par défaut sécurisée, standards ouverts) · pratiques de développement déclarées (conformité aux guides C et Rust de l'ANSSI, OWASP Developer Guide, revue par les pairs, tests et CI, reproductibilité des binaires, sûreté mémoire du langage) · **audit régulier de l'évolution des contributions** (justifié par le cas XZ-utils) · contrat de support · veille sur les appels au soutien des mainteneurs.

> **Périmètre confirmé** : le guide couvre explicitement les **bibliothèques et dépendances applicatives** — sa phrase d'ouverture vise « un produit (outil, bibliothèque, cadriciel) » et son exemple central, XZ-utils, est une bibliothèque. Il raisonne cependant au niveau du *projet amont* (dépôt, mainteneurs, commits), pas du *paquet publié sur un registre* : typosquatting, compromission de compte de publication, scripts `postinstall`, épinglage de versions et dépendances transitives n'y sont pas traités — ces règles sont `[DINUM]`.
> ⚠️ **Absents** : la **licence** (jamais mentionnée, ce qui est notable pour un guide sur le logiciel libre) et la **réversibilité / plan de sortie**. L'ANSSI oriente vers le *soutien* du projet, pas vers sa substitution.

### 11. Essentiel « Mise en œuvre sécurisée d'un CMS » — `ESS-CMS`

- **Titre** : *Les Essentiels — Mise en œuvre sécurisée d'un CMS* — **V1.1 (12/23)**
- **URL** : https://messervices.cyber.gouv.fr/documents-guides/anssi_essentiels_mise-en-oeuvre-securisee-cms_v1.1%20(1).pdf
- **Structure** : fiche 2 pages, **10 bonnes pratiques non numérotées**. La numérotation `[ESS-CMS 1]` à `[ESS-CMS 10]` du module est **un repère DINUM**.
- **Module alimenté** : [`modules/cms.md`](modules/cms.md)
- **Nature** : **document d'aiguillage** — 9 des 10 puces renvoient à un autre guide ANSSI.

### 12. Règles de programmation en langage C — `C RÈGLE|RECOMMANDATION|BONNE PRATIQUE <n>`

- **Titre** : *Règles de programmation pour le développement sécurisé de logiciels en langage C*
- **Référence** : ANSSI-PA-073 — **version 1.2** — 21/07/2020 — 176 pages
- **URL** : https://messervices.cyber.gouv.fr/documents-guides/anssi-guide-regles_de_programmation_pour_le_developpement_securise_de_logiciels_en_langage_c-v1.2.pdf
- **Structure** : **181 énoncés numérotés globalement 1–181** — 120 `RÈGLE`, 52 `RECOMMANDATION`, 9 `BONNE PRATIQUE`. Pas de numérotation par chapitre, donc **pas de forme `R168`** : on écrit `RÈGLE 168`.
- **Module alimenté** : [`modules/langage-c.md`](modules/langage-c.md) — **38 énoncés retenus sur 181**
- **Utile** : chaque section est croisée avec **MISRA C:2012, CERT C et CWE**, ce qui permet de mapper vers `clang-tidy` (`cert-*`) et `cppcheck --addon=misra`.

### 13. Règles de programmation en Rust — `RUST R<n>`

- **Titre** : *Règles de programmation pour le développement d'applications sécurisées en Rust*
- **Référence** : ANSSI-PA-074 — **version 1.0** — 09/06/2020
- **URL** : https://messervices.cyber.gouv.fr/documents-guides/anssi-guide-regles_de_programmation_pour_le_developpement_dapplications_securisees_en_rust-v1.0.pdf
- **Structure** : **51 items R1–R51**, avec deux niveaux imprimés : `RÈGLE` (34, obligatoires) et `RECO` (17)
- **Module alimenté** : [`modules/langage-rust.md`](modules/langage-rust.md) — **36 items retenus sur 51**
- **Source vivante** : le guide est maintenu à ciel ouvert sur https://github.com/ANSSI-FR/rust-guide

> ⚠️ **`miri` et `cargo-fuzz` sont absents** du guide v1.0. Les recommander relève du `[DINUM]`.

---

## Divergences entre guides à connaître

| Sujet | Position A | Position B | Arbitrage retenu |
|-------|-----------|-----------|------------------|
| **Stockage des mots de passe** | `MFA R29` recommande une fonction **memory-hard**, « comme **scrypt** ou **Argon2** », PBKDF2 n'étant que le repli `R29-` | `CRYPTO R15` ne recommande **que PBKDF2**. Argon2, scrypt et bcrypt sont **totalement absents** du guide cryptographique et de PG-083 v3.00 | **`MFA R29` prévaut** : c'est le guide spécialisé sur le sujet, et il est aligné sur l'état de l'art. Voir [`valeurs-anssi.md`](valeurs-anssi.md) |
| **Taille des clés RSA** | `TLS R26` (2020) : ≥ 2048 bits jusqu'en 2030 | `CRYPTO R16` (2021) : ≥ 3072 bits ; `CRYPTO-DIM` (2026) : ≥ 2048 jusqu'à fin 2030, **≥ 3072 à partir de 2031**, avec recommandation de 3072 dès maintenant | **`CRYPTO-DIM` v3.00 prévaut** (document le plus récent) |
| **Conteneurs comme frontière de sécurité** | `CLOIS` : un conteneur **est** une frontière, mais sa robustesse n'est pas acquise a priori — elle dépend de la solution, du durcissement du noyau partagé et de la configuration | — | Ne pas présenter un conteneur non durci comme équivalent à une machine virtuelle. Le guide recommande l'**emboîtement** conteneur-dans-VM |

---

## Rejouer l'extraction

Les guides sont des PDF ; les pages HTML de `messervices.cyber.gouv.fr` n'en sont que des vitrines. Pour mettre à jour ce référentiel après une révision ANSSI :

1. Récupérer le PDF depuis la page vitrine du guide.
2. `pdftotext -layout guide.pdf guide.txt` — plus rapide et plus fiable qu'une lecture page à page.
3. Aller directement à la **liste récapitulative des recommandations**, en fin de document (le guide de cloisonnement en est dépourvu : ses recommandations sont dans le corps du texte).
4. Mettre à jour la version, la date et les libellés ici, puis répercuter dans [`checklist.md`](checklist.md) et [`valeurs-anssi.md`](valeurs-anssi.md).

**Les PDF ne sont pas versionnés dans ce dépôt** : la skill cite les guides, elle ne les redistribue pas.
