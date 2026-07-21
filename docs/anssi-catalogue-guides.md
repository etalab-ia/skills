# Catalogue des guides ANSSI

> **Note** : ce document est le compte-rendu de travail du scan. La version exploitable du catalogue — celle qui fait foi et qui est maintenue — vit dans la skill [`anssi-guides`](../skills/anssi-guides/references/catalogue.md).

**Date de consultation : 20 juillet 2026.** Source du scan : le catalogue [messervices.cyber.gouv.fr/guides](https://messervices.cyber.gouv.fr/guides), qui est aujourd'hui le point d'entrée canonique — `cyber.gouv.fr/publications` n'est plus qu'une page d'aiguillage et renvoie vers ce catalogue.

---

## 1. Les 13 guides retenus pour la skill `securite-developpement`

Dates et références issues des PDF eux-mêmes (voir [`sources.md`](../skills/securite-developpement/references/sources.md)), recoupées avec la date de publication affichée au catalogue.

| # | Guide | Référence / version | Date | Thématique | URL |
|---|---|---|---|---|---|
| 1 | Guide d'hygiène informatique (42 mesures) | v2.0 | sept. 2017 ⚠️ | Socle SSI généraliste : 42 mesures / 10 thèmes, niveaux standard et renforcé | [lien](https://messervices.cyber.gouv.fr/guides/guide-dhygiene-informatique) |
| 2 | Sécuriser un site web | ANSSI-PA-009 v2.0 | 28/04/2021 | Sécurité côté navigateur : TLS/HSTS, XSS, CSP, cookies, CORS, iframes — 63 recommandations | [lien](https://messervices.cyber.gouv.fr/guides/securiser-un-site-web) |
| 3 | Authentification multifacteur et mots de passe | ANSSI-PG-078 v2.0 | 08/10/2021 | MFA, facteurs d'authentification, stockage et politique de mots de passe — 42 recommandations | [lien](https://messervices.cyber.gouv.fr/documents-guides/anssi-guide-authentification_multifacteur_et_mots_de_passe.pdf) |
| 4a | Guide de sélection d'algorithmes cryptographiques | ANSSI-PA-079 v1.0 | 08/03/2021 | Choix d'algorithmes côté développeur — 27 recommandations | [lien](https://messervices.cyber.gouv.fr/guides/mecanismes-cryptographiques) |
| 4b | Choix et dimensionnement des mécanismes cryptographiques | ANSSI-PG-083 v3.00 | 20/03/2026 | Tailles de clés, durées de vie, **menace quantique** — prévaut sur 4a en cas de divergence | [lien](https://messervices.cyber.gouv.fr/guides/mecanismes-cryptographiques) |
| 5 | Recommandations de sécurité relatives à TLS | SDE-NT-35 v1.2 | 26/03/2020 | Versions TLS, suites cryptographiques, certificats, configuration serveur — 39 recommandations | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-de-securite-relatives-tls) |
| 6 | Architecture d'un système de journalisation | ANSSI-PA-012 v2.0 | 28/01/2022 | Collecte, centralisation, rétention, socle minimal d'événements, détection — 31 recommandations | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-de-securite-pour-larchitecture-dun-systeme-de-journalisation) |
| 7 | Cloisonnement système | ANSSI-PG-040 v1.0 | 14/12/2017 ⚠️ | Méthode d'analyse du cloisonnement, conteneurs, VM, emboîtement — 25 recommandations | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-pour-la-mise-en-place-de-cloisonnement-systeme) |
| 8 | Essentiel « DevSecOps » | V1.0 (02/24) | 13/03/2024 | CI/CD, secrets, dépendances, tests de sécurité automatisés, signature d'artefacts — 13 puces | [lien](https://messervices.cyber.gouv.fr/guides/devsecops) |
| 9 | Essentiel « Bases de données relationnelles » | V1.0 (12/24) | 31/01/2025 | Comptes et privilèges, durcissement SGBD, chiffrement, sauvegarde, requêtes préparées — 10 recos | [lien](https://messervices.cyber.gouv.fr/guides/bases-de-donnees-relationnelles) |
| 10 | Essentiel « Sélection d'un logiciel libre » | V1.0 (05/25) | 02/05/2025 | Critères de choix d'une dépendance : MCO/MCS, SBOM, audit des contributions — 10 critères | [lien](https://messervices.cyber.gouv.fr/guides/selection-dun-logiciel-libre) |
| 11 | Essentiel « Mise en œuvre sécurisée d'un CMS » | V1.1 (12/23) | 15/12/2023 | Choix, mise à jour, extensions, comptes d'administration d'un CMS — 10 bonnes pratiques | [lien](https://messervices.cyber.gouv.fr/guides/mise-en-oeuvre-securisee-dun-cms) |
| 12 | Règles de programmation — langage C | ANSSI-PA-073 v1.2 | 21/07/2020 | 181 énoncés (120 règles, 52 recommandations, 9 bonnes pratiques), croisés MISRA C / CERT C / CWE | [lien](https://messervices.cyber.gouv.fr/guides/regles-de-programmation-pour-le-developpement-securise-de-logiciels-en-langage-c) |
| 13 | Règles de programmation — Rust | ANSSI-PA-074 v1.0 | 09/06/2020 | 51 items (34 règles, 17 recommandations) ; maintenu sur [GitHub](https://github.com/ANSSI-FR/rust-guide) | [lien](https://messervices.cyber.gouv.fr/guides/regles-de-programmation-pour-le-developpement-dapplications-securisees-en-rust) |

### Écarts de date relevés pendant le scan

| Guide | Date du PDF | Date affichée au catalogue | Lecture |
|---|---|---|---|
| Hygiène informatique | v2.0, septembre 2017 | 23 janvier 2017 | Le catalogue affiche la date de **première mise en ligne**, pas celle de la v2.0. Se fier au PDF. |
| Cloisonnement système | 14/12/2017 | 22 décembre 2017 | Écart de mise en ligne, sans incidence. |
| Mécanismes cryptographiques | PA-079 : 08/03/2021 / PG-083 : 20/03/2026 | 20 mars 2026 | Une seule page vitrine pour **deux documents distincts** ; la date affichée est celle de PG-083. |

⚠️ Les URLs `cyber.gouv.fr/publications/...` de ta liste initiale renvoient un **301** vers `messervices.cyber.gouv.fr`. Les URLs ci-dessus sont les cibles finales.

---

## 2. Scan complet du catalogue ANSSI

**178 fiches** au catalogue, dont **128 en français** et 50 traductions anglaises. Toutes ont l'ANSSI pour source (aucun co-portage tiers dans ce catalogue).

### Guides pertinents pour le développement applicatif, hors des 13 retenus

Ce sont les candidats les plus directs à une extension future de la skill :

| Guide | Publication | Pourquoi c'est pertinent |
|---|---|---|
| Transition post-quantique de TLS 1.3 | 2 février 2026 | Complète le guide TLS v1.2 (2020), muet sur l'hybridation post-quantique |
| Transition post-quantique de SSHv2 | 2 février 2026 | Même sujet, côté accès administrateur |
| Recommandations de sécurité pour un système d'IA générative | 29 avril 2024 | Directement pertinent pour les produits IA de l'État |
| Dénis de service distribués (DDoS) — Les essentiels | 26 avril 2024 | Disponibilité, non couverte par les 13 |
| Recommandations relatives aux architectures des services DNS | 20 août 2024 | DNS, absent des 13 |
| Sauvegarde des systèmes d'information | 6 décembre 2023 | Le guide BDD n'effleure que le paramétrage des sauvegardes |
| Sécuriser la journalisation en environnement Microsoft Active Directory | 28 janvier 2022 | Compagnon direct du guide Journalisation |
| Recommandations de sécurité relatives au déploiement de conteneurs Docker | 24 décembre 2020 | Comble le vide technique du guide Cloisonnement (2017) |
| Sécurisation de la mise en œuvre du protocole OpenID Connect | 8 septembre 2020 | Authentification déléguée / SSO — angle mort des 13 guides |
| Bonnes pratiques pour l'acquisition et l'exploitation de noms de domaine | 10 novembre 2017 | Cycle de vie des domaines |

Le plus notable : **OpenID Connect** et **conteneurs Docker**, qui couvrent deux sujets où la skill s'appuie aujourd'hui sur des règles `[DINUM]` faute de source ANSSI — alors qu'un guide existe.

### Catalogue complet — 128 guides en français

Trié du plus récent au plus ancien.

| Guide | Publication | Collection | Thématique | URL |
|---|---|---|---|---|
| Défense en profondeur | 1 juillet 2026 | Les essentiels | Les essentiels | [lien](https://messervices.cyber.gouv.fr/guides/essentiels-defense-profondeur) |
| Recommandations de sécurité relatives à la gestion technique et centralisée du bâtiment (gtb/gtc) | 4 juin 2026 | Systèmes industriels | Systèmes industriels | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-gestion-technique-batiment) |
| Anticiper et gérer sa communication de crise cyber | 4 juin 2026 | Crise cyber | Crise cyber | [lien](https://messervices.cyber.gouv.fr/guides/anticiper-et-gerer-sa-communication-de-crise-cyber) |
| Recommandations pour la mise en œuvre du vote par Internet pour les élections non politiques | 24 avril 2026 | Sécurité du vote électronique | — | [lien](https://messervices.cyber.gouv.fr/guides/vote-internet-elections-non-politiques) |
| The security accreditation guide for information systems | 26 mars 2026 | Gestion des risques cyber | Gestion des risques cyber | [lien](https://messervices.cyber.gouv.fr/guides/the-security-accreditation-guide-for-information-systems) |
| Mécanismes cryptographiques | 20 mars 2026 | Cryptographie | Cryptographie | [lien](https://messervices.cyber.gouv.fr/guides/mecanismes-cryptographiques) |
| Guide de cybersécurité à l’usage des start-up du numérique | 26 février 2026 | Cybersécurité des start-up | — | [lien](https://messervices.cyber.gouv.fr/guides/guide-cybersecurite-start-up-numerique) |
| Sécurisation du poste de travail multi-environnements (non classifiés) | 20 février 2026 | Les fondamentaux | Les fondamentaux | [lien](https://messervices.cyber.gouv.fr/guides/fondamentaux-poste-multi-environnements) |
| Transition post-quantique d’IPsec | 2 février 2026 | Cryptographie post-quantique | Cryptographie | [lien](https://messervices.cyber.gouv.fr/guides/Transition-post-quantique-protocole-IPsec) |
| Transition post-quantique de SSHv2 | 2 février 2026 | Cryptographie post-quantique | Cryptographie | [lien](https://messervices.cyber.gouv.fr/guides/Transition-post-quantique-protocole-SSHv2) |
| Transition post-quantique de TLS 1.3 | 2 février 2026 | Cryptographie post-quantique | Cryptographie | [lien](https://messervices.cyber.gouv.fr/guides/Transition-post-quantique-protocole-TLS-1-3) |
| Sécurisation d’une infrastructure VMware | 26 janvier 2026 | Les fondamentaux | Les fondamentaux | [lien](https://messervices.cyber.gouv.fr/guides/securisation-dune-infrastructure-vmware) |
| Securing a VMware infrastructure  | 26 janvier 2026 | Les fondamentaux | Les fondamentaux | [lien](https://messervices.cyber.gouv.fr/guides/securing-wmware-infrastructure) |
| Sécuriser une migration numérique | 23 janvier 2026 | Migration | Les essentiels | [lien](https://messervices.cyber.gouv.fr/guides/migration) |
| ANSSI views on crypto agility  | 19 janvier 2026 | Cryptographie post-quantique | Cryptographie | [lien](https://messervices.cyber.gouv.fr/guides/ANSSI-views-on-crypto-agility) |
| Préparer la remédiation | 16 janvier 2026 | Cyberattaques et remédiation | Remédiation | [lien](https://messervices.cyber.gouv.fr/guides/cyberattaques-et-remediation-preparer-la-remedation) |
| Outil de pilotage du projet de remédiation | 1 janvier 2026 | Gestion des risques cyber | Remédiation | [lien](https://messervices.cyber.gouv.fr/guides/outil-pilotage-projet-remediation) |
| La cybersécurité des systèmes industriels - Mesures détaillées | 19 décembre 2025 | Systèmes industriels | Systèmes industriels | [lien](https://messervices.cyber.gouv.fr/guides/la-cybersecurite-des-systemes-industriels-mesures-detaillees) |
| Mise en œuvre sécurisée d’un serveur Windows | 3 octobre 2025 | Les essentiels | Les essentiels | [lien](https://messervices.cyber.gouv.fr/guides/mise-en-oeuvre-securisee-dun-serveur-windows) |
| Piloter un projet de supervision | 12 septembre 2025 | La supervision de sécurité | Supervision de sécurité | [lien](https://messervices.cyber.gouv.fr/guides/la-supervision-de-securite-piloter-un-projet-de-supervision) |
| Les clés de décision | 26 août 2025 | La supervision de sécurité | Supervision de sécurité | [lien](https://messervices.cyber.gouv.fr/guides/la-supervision-de-securite-les-cles-de-decision) |
| Architecture sécurisée de SI | 8 août 2025 | Les essentiels | Les essentiels | [lien](https://messervices.cyber.gouv.fr/guides/architecture-securisee-de-si) |
| Infrastructure de gestion de clés (IGC) | 1 août 2025 | Les essentiels | Les essentiels | [lien](https://messervices.cyber.gouv.fr/guides/infrastructure-de-gestion-de-cles-igc) |
| Modèle Zero Trust | 20 juin 2025 | Les fondamentaux | Les fondamentaux | [lien](https://messervices.cyber.gouv.fr/guides/zero-trust) |
| Modèle Zero Trust | 20 juin 2025 | Les essentiels | Les essentiels | [lien](https://messervices.cyber.gouv.fr/guides/modele-zero-trust) |
| Approche SSI pour l’Internet des objets industriels | 30 mai 2025 | Internet des objets | Systèmes industriels | [lien](https://messervices.cyber.gouv.fr/guides/approche-ssi-pour-linternet-des-objets-industriels) |
| Sélection d’un logiciel libre | 2 mai 2025 | Les essentiels | Les essentiels | [lien](https://messervices.cyber.gouv.fr/guides/selection-dun-logiciel-libre) |
| La cybersécurité des systèmes industriels - Méthode de classification | 11 avril 2025 | Systèmes industriels | Systèmes industriels | [lien](https://messervices.cyber.gouv.fr/guides/la-cybersecurite-des-systemes-industriels) |
| Hygiène numérique des téléphones mobiles | 3 avril 2025 | Les essentiels | Les essentiels | [lien](https://messervices.cyber.gouv.fr/guides/hygiene-numerique-des-telephones-mobiles) |
| L’homologation de sécurité des systèmes d’information | 1 avril 2025 | Gestion des risques cyber | Gestion des risques cyber | [lien](https://messervices.cyber.gouv.fr/guides/lhomologation-de-securite-des-systemes-dinformation) |
| Données et traitements sensibles | 28 mars 2025 | Les essentiels | Les essentiels | [lien](https://messervices.cyber.gouv.fr/guides/donnees-traitements-sensibles) |
| Développer la confiance dans l’IA par une approche par les risques cyber. | 7 février 2025 | Gestion des risques cyber | Intelligence artificielle | [lien](https://messervices.cyber.gouv.fr/guides/developper-la-confiance-dans-lia-par-une-approche-par-les-risques-cyber) |
| Bases de données relationnelles | 31 janvier 2025 | Les essentiels | Les essentiels | [lien](https://messervices.cyber.gouv.fr/guides/bases-de-donnees-relationnelles) |
| Se protéger des fuites de données | 28 janvier 2025 | Les essentiels | Les essentiels | [lien](https://messervices.cyber.gouv.fr/guides/se-proteger-des-fuites-de-donnees) |
| Automatisation de la gestion des certificats avec ACME | 24 janvier 2025 | Les fondamentaux | Les fondamentaux | [lien](https://messervices.cyber.gouv.fr/guides/automatisation-de-la-gestion-des-certificats-avec-acme) |
| Recommandations pour les architectures des interconnexions multiniveaux | 25 octobre 2024 | Interconnexions multiniveaux | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-pour-les-architectures-des-interconnexions-multiniveaux) |
| Recommandations relatives aux architectures des services DNS | 20 août 2024 | Services DNS | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-relatives-aux-architectures-des-services-dns) |
| Le Cyberdico de l'ANSSI | 15 juillet 2024 | Définitions | — | [lien](https://messervices.cyber.gouv.fr/guides/cyberdico-quest-ce-que-cest) |
| Recommandations pour l’hébergement dans le cloud des SI sensibles  | 9 juillet 2024 | Cloud et SI sensibles | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-pour-lhebergement-des-si-sensibles-dans-le-cloud) |
| Recommandations de déploiement d’un service IAAS OpenStack SecNumCloud | 3 mai 2024 | OpenStack | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-de-deploiement-dun-service-iaas-openstack-secnumcloud) |
| Recommandations de sécurité pour un système d’IA générative | 29 avril 2024 | IA générative | Intelligence artificielle | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-de-securite-pour-un-systeme-dia-generative) |
| Dénis de service distribués (DDoS) | 26 avril 2024 | Les essentiels | Les essentiels | [lien](https://messervices.cyber.gouv.fr/guides/denis-de-service-distribues-ddos) |
| La remédiation du Tier 0 Active Directory | 18 mars 2024 | Cyberattaques et remédiation | Remédiation | [lien](https://messervices.cyber.gouv.fr/guides/cyberattaques-et-remediation-la-remediation-du-tier-0-active-directory) |
| Piloter la remédiation | 18 mars 2024 | Cyberattaques et remédiation | Remédiation | [lien](https://messervices.cyber.gouv.fr/guides/cyberattaques-et-remediation-piloter-la-remediation) |
| DevSecOps | 13 mars 2024 | Les essentiels | Les essentiels | [lien](https://messervices.cyber.gouv.fr/guides/devsecops) |
| Virtualisation | 20 février 2024 | Les essentiels | Les essentiels | [lien](https://messervices.cyber.gouv.fr/guides/virtualisation) |
| Les clés de décision | 16 janvier 2024 | Cyberattaques et remédiation | Remédiation | [lien](https://messervices.cyber.gouv.fr/guides/cyberattaques-et-remediation-les-cles-de-decision) |
| Avis de l’ANSSI sur la migration vers la cryptographie post-quantique | 15 janvier 2024 | Cryptographie post-quantique | Cryptographie | [lien](https://messervices.cyber.gouv.fr/guides/avis-de-lanssi-sur-la-migration-vers-la-cryptographie-post-quantique-0) |
| Mise en œuvre sécurisée d’un CMS | 15 décembre 2023 | Les essentiels | Les essentiels | [lien](https://messervices.cyber.gouv.fr/guides/mise-en-oeuvre-securisee-dun-cms) |
| Sauvegarde des systèmes d’information | 6 décembre 2023 | Les essentiels | Les essentiels | [lien](https://messervices.cyber.gouv.fr/guides/sauvegarde-des-systemes-dinformation) |
| Recommandations sur le nomadisme numérique | 14 novembre 2023 | Mobilité | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-sur-le-nomadisme-numerique) |
| Sauvegarde des systèmes d’information | 25 octobre 2023 | Les fondamentaux | Les fondamentaux | [lien](https://messervices.cyber.gouv.fr/guides/fondamentaux-sauvegarde-systemes-dinformation) |
| Recommandations pour l’administration sécurisée des SI reposant sur AD | 18 octobre 2023 | Active Directory | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-pour-ladministration-securisee-des-si-reposant-sur-ad) |
| Recommandations pour le reconditionnement des ordinateurs de bureau ou portables | 3 octobre 2023 | Reconditionnement | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-pour-le-reconditionnement-des-ordinateurs-de-bureau-ou-portables) |
| Les Mesures Cyber Préventives Prioritaires | 17 mai 2023 | Gestion des risques cyber | Gestion des risques cyber | [lien](https://messervices.cyber.gouv.fr/guides/les-mesures-cyber-preventives-prioritaires) |
| Avis de l’ANSSI sur la migration vers la cryptographie post-quantique | 11 avril 2022 | Cryptographie post-quantique | Cryptographie | [lien](https://messervices.cyber.gouv.fr/guides/avis-de-lanssi-sur-la-migration-vers-la-cryptographie-post-quantique) |
| Recommandations de configuration des commutateurs et pare-feux Siemens Scalance | 11 février 2022 | Siemens Scalance | Systèmes industriels | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-de-configuration-des-commutateurs-et-pare-feux-siemens-scalance) |
| Recommandations de configuration des commutateurs et pare-feux Hirschmann | 11 février 2022 | Hirschmann | Systèmes industriels | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-de-configuration-des-commutateurs-et-pare-feux-hirschmann) |
| Recommandations de sécurité pour l’architecture d’un système de journalisation | 28 janvier 2022 | Journalisation | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-de-securite-pour-larchitecture-dun-systeme-de-journalisation) |
| Sécuriser la journalisation dans un environnement Microsoft Active Directory | 28 janvier 2022 | Journalisation | — | [lien](https://messervices.cyber.gouv.fr/guides/securiser-la-journalisation-dans-un-environnement-microsoft-active-directory) |
| Crise cyber, les clés d’une gestion opérationnelle et stratégique | 6 décembre 2021 | Crise cyber | Crise cyber | [lien](https://messervices.cyber.gouv.fr/guides/crise-cyber-les-cles-dune-gestion-operationnelle-et-strategique) |
| Recommandations relatives à l’authentification multifacteur et aux mots de passe | 8 octobre 2021 | MFA et mots de passe | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-relatives-lauthentification-multifacteur-et-aux-mots-de-passe) |
| Recommandations pour les architectures des SI sensibles ou DR | 24 septembre 2021 | SI sensibles et DR | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-pour-les-architectures-des-si-sensibles-ou-dr) |
| Recommandations relatives à la sécurité des (systèmes d’)objets connectés | 27 août 2021 | Objets connectés | Systèmes industriels | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-relatives-la-securite-des-systemes-dobjets-connectes) |
| Recommandations relatives à l’administration sécurisée des SI | 11 mai 2021 | Administration sécurisée | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-relatives-ladministration-securisee-des-si) |
| Sécuriser un site web | 28 avril 2021 | Sites web | — | [lien](https://messervices.cyber.gouv.fr/guides/securiser-un-site-web) |
| Recommandations pour une configuration sécurisée d’un pare-feu Stormshield Network Security (SNS) en version 3.7.17 | 2 avril 2021 | Stormshield Network Security | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-pour-une-configuration-securisee-dun-pare-feu-stormshield-network) |
| La cybersécurité pour les TPE/PME en treize questions | 18 février 2021 | Gestion des risques cyber | Gestion des risques cyber | [lien](https://messervices.cyber.gouv.fr/guides/la-cybersecurite-pour-les-tpepme-en-treize-questions) |
| Recommandations de sécurité relatives au déploiement de conteneurs Docker | 24 décembre 2020 | Conteneurs Docker | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-de-securite-relatives-au-deploiement-de-conteneurs-docker) |
| Recommandations pour la protection des systèmes d’information essentiels | 22 décembre 2020 | SI essentiels | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-pour-la-protection-des-systemes-dinformation-essentiels) |
| Doctrine de détection pour les systèmes industriels | 3 décembre 2020 | Systèmes industriels | Systèmes industriels | [lien](https://messervices.cyber.gouv.fr/guides/doctrine-de-detection-pour-les-systemes-industriels) |
| Cybersécurité : toutes les communes et intercommunalités sont concernées | 20 novembre 2020 | Gestion des risques cyber | Gestion des risques cyber | [lien](https://messervices.cyber.gouv.fr/guides/cybersecurite-toutes-les-communes-et-intercommunalites-sont-concernees) |
| Organiser un exercice de gestion de crise cyber | 14 octobre 2020 | Crise cyber | Crise cyber | [lien](https://messervices.cyber.gouv.fr/guides/organiser-un-exercice-de-gestion-de-crise-cyber) |
| Recommandations pour la sécurisation de la mise en oeuvre du protocole OpenID Connect | 8 septembre 2020 | OpenID Connect | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-pour-la-securisation-de-la-mise-en-oeuvre-du-protocole-openid-connect) |
| Attaques par rançongiciels, tous concernés. | 4 septembre 2020 | Rançongiciels | Crise cyber | [lien](https://messervices.cyber.gouv.fr/guides/attaques-par-rancongiciels-tous-concernes) |
| Règles de programmation pour le développement sécurisé de logiciels en langage C | 21 juillet 2020 | Langage C | — | [lien](https://messervices.cyber.gouv.fr/guides/regles-de-programmation-pour-le-developpement-securise-de-logiciels-en-langage-c) |
| Profil de fonctionnalités et de sécurité - Sas et station blanche (réseaux non classifiés) | 1 juillet 2020 | Profil de fonctionnalités et de sécurité | — | [lien](https://messervices.cyber.gouv.fr/guides/profil-de-fonctionnalites-et-de-securite-sas-et-station-blanche-reseaux-non-classifies) |
| Recommandations relatives à l’interconnexion d’un SI à Internet | 19 juin 2020 | Interconnexion à internet | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-relatives-linterconnexion-dun-si-internet) |
| Règles de programmation pour le développement d’applications sécurisées en Rust | 9 juin 2020 | Rust | — | [lien](https://messervices.cyber.gouv.fr/guides/regles-de-programmation-pour-le-developpement-dapplications-securisees-en-rust) |
| Recommandations de sécurité relatives à TLS | 26 mars 2020 | TLS | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-de-securite-relatives-tls) |
| Sécurisation des systèmes de contrôle d’accès physique et vidéoprotection | 4 mars 2020 | Accès physique et vidéoprotection | — | [lien](https://messervices.cyber.gouv.fr/guides/securisation-des-systemes-de-controle-dacces-physique-et-videoprotection) |
| Sécurité numérique des collectivités territoriales : l’essentiel de la réglementation | 28 janvier 2020 | Réglementation | Gestion des risques cyber | [lien](https://messervices.cyber.gouv.fr/guides/securite-numerique-des-collectivites-territoriales-lessentiel-de-la-reglementation) |
| Maîtrise du risque numérique - l’atout confiance | 18 novembre 2019 | Gestion des risques cyber | Gestion des risques cyber | [lien](https://messervices.cyber.gouv.fr/guides/maitrise-du-risque-numerique-latout-confiance) |
| Recommandations pour une utilisation sécurisée de Zed! | 14 novembre 2019 | Zed! | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-pour-une-utilisation-securisee-de-zed) |
| Exigences de sécurité matérielles | 8 novembre 2019 | Sécurité matérielle | — | [lien](https://messervices.cyber.gouv.fr/guides/exigences-de-securite-materielles) |
| Bonnes pratiques à l’usage des professionnels en déplacement  | 17 mai 2019 | Gestion des risques cyber | Gestion des risques cyber | [lien](https://messervices.cyber.gouv.fr/guides/bonnes-pratiques-lusage-des-professionnels-en-deplacement) |
| Recommandations de configuration d'un système GNU/Linux | 22 février 2019 | GNU/Linux | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-de-securite-relatives-un-systeme-gnulinux) |
| Cartographie du système d’information | 21 novembre 2018 | Cartographie | Gestion des risques cyber | [lien](https://messervices.cyber.gouv.fr/guides/cartographie-du-systeme-dinformation) |
| La méthode EBIOS Risk Manager - Le guide | 9 octobre 2018 | Gestion des risques cyber | Gestion des risques cyber | [lien](https://messervices.cyber.gouv.fr/guides/la-methode-ebios-risk-manager-le-guide) |
| Recommandations de déploiement du protocole 802.1X | 17 août 2018 | Protocole 802.1X | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-de-deploiement-du-protocole-8021x) |
| Protection du potentiel scientifique et technique de la nation | 17 mai 2018 | PPST | — | [lien](https://messervices.cyber.gouv.fr/guides/protection-du-potentiel-scientifique-et-technique-de-la-nation) |
| Recommandations pour choisir des pare-feux maîtrisés dans les zones exposées à Internet | 26 janvier 2018 | Pare-feux | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-pour-choisir-des-pare-feux-maitrises-dans-les-zones-exposees-internet) |
| Recommandations pour la mise en place de cloisonnement système | 22 décembre 2017 | Cloisonnement | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-pour-la-mise-en-place-de-cloisonnement-systeme) |
| Mise en œuvre des fonctionnalités de sécurité de Windows 10 reposant sur la virtualisation | 10 novembre 2017 | Virtualisation | — | [lien](https://messervices.cyber.gouv.fr/guides/mise-en-oeuvre-des-fonctionnalites-de-securite-de-windows-10-reposant-sur-la) |
| Bonnes pratiques pour l’acquisition et l’exploitation de noms de domaine | 10 novembre 2017 | Noms de domaine | — | [lien](https://messervices.cyber.gouv.fr/guides/bonnes-pratiques-pour-lacquisition-et-lexploitation-de-noms-de-domaine) |
| Restreindre la collecte de données sous Windows 10 | 6 juillet 2017 | Windows 10 | — | [lien](https://messervices.cyber.gouv.fr/guides/restreindre-la-collecte-de-donnees-sous-windows-10) |
| Guide d’élaboration d’une charte d’utilisation des moyens informatiques et des outils numériques | 19 juin 2017 | Charte | — | [lien](https://messervices.cyber.gouv.fr/guides/guide-delaboration-dune-charte-dutilisation-des-moyens-informatiques-et-des-outils) |
| Élections législatives : Candidats, assurez votre sécurité numérique ! | 24 mai 2017 | Elections | — | [lien](https://messervices.cyber.gouv.fr/guides/elections-legislatives-candidats-assurez-votre-securite-numerique) |
| Recommandations pour une utilisation sécurisée de Cryhod | 12 mai 2017 | CryHod | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-pour-une-utilisation-securisee-de-cryhod) |
| Guide d’hygiène informatique | 23 janvier 2017 | Gestion des risques cyber | Gestion des risques cyber | [lien](https://messervices.cyber.gouv.fr/guides/guide-dhygiene-informatique) |
| Mettre en œuvre une politique de restrictions logicielles sous Windows | 16 janvier 2017 | Restriction logicielle | — | [lien](https://messervices.cyber.gouv.fr/guides/mettre-en-oeuvre-une-politique-de-restrictions-logicielles-sous-windows) |
| La télé-assistance sécurisée | 16 janvier 2017 | La télé-assistance sécurisée | — | [lien](https://messervices.cyber.gouv.fr/guides/la-tele-assistance-securisee) |
| CRYPTO : LE WEBDOC’ | 10 octobre 2016 | Crypto | Cryptographie | [lien](https://messervices.cyber.gouv.fr/guides/crypto-le-webdoc) |
| Guide des bonnes pratiques de sécurité informatique à bord des navires | 4 octobre 2016 | Maritime | — | [lien](https://messervices.cyber.gouv.fr/guides/guide-des-bonnes-pratiques-de-securite-informatique-bord-des-navires) |
| Recommandations et méthodologie pour le nettoyage d’une politique de filtrage réseau d’un pare-feu | 9 août 2016 | Filtrage | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-et-methodologie-pour-le-nettoyage-dune-politique-de-filtrage-reseau) |
| Sécuriser un environnement d’exécution Java sous Windows | 28 juillet 2016 | Java | — | [lien](https://messervices.cyber.gouv.fr/guides/securiser-un-environnement-dexecution-java-sous-windows) |
| Recommandations de sécurité pour les architectures basées sur VMware vSphere ESXi | 12 juillet 2016 | VMware vSphere ESXi | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-de-securite-pour-les-architectures-basees-sur-vmware-vsphere-esxi) |
| Recommandations pour la sécurisation d’un commutateur de desserte | 12 juillet 2016 | Commutateur de desserte | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-pour-la-securisation-dun-commutateur-de-desserte) |
| Définition d’une politique de filtrage réseau d'un pare-feu | 5 avril 2016 | Pare-feu | — | [lien](https://messervices.cyber.gouv.fr/guides/definition-dune-politique-de-pare-feu) |
| Référentiel d’exigences de sécurité pour les prestataires d’intégration et de maintenance de systèmes industriels | 9 mars 2016 | Systèmes industriels | Systèmes industriels | [lien](https://messervices.cyber.gouv.fr/guides/referentiel-dexigences-de-securite-pour-les-prestataires-dintegration-et-de) |
| Recommandations de sécurité relatives à IPsec | 3 août 2015 | IPsec | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-de-securite-relatives-ipsec) |
| Sécuriser son ordiphone | 15 juillet 2015 | Ordiphone smartphone | — | [lien](https://messervices.cyber.gouv.fr/guides/securiser-son-ordiphone) |
| Recommandations de configuration matérielle de postes clients et serveurs x86 | 31 mars 2015 | x86 | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-de-configuration-materielle-de-postes-clients-et-serveurs-x86) |
| Comprendre et anticiper les attaques DDoS | 20 mars 2015 | DDos | — | [lien](https://messervices.cyber.gouv.fr/guides/comprendre-et-anticiper-les-attaques-ddos) |
| Guide pour une formation sur la cybersécurité des systèmes industriels | 5 mars 2015 | Systèmes industriels | Systèmes industriels | [lien](https://messervices.cyber.gouv.fr/guides/guide-pour-une-formation-sur-la-cybersecurite-des-systemes-industriels) |
| Profils de protection pour les systèmes industriels | 3 mars 2015 | PP | Systèmes industriels | [lien](https://messervices.cyber.gouv.fr/guides/profils-de-protection-pour-les-systemes-industriels) |
| Achat de produits de sécurité et de services de confiance qualifiés dans le cadre du RGS | 12 février 2015 | RGS | — | [lien](https://messervices.cyber.gouv.fr/guides/achat-de-produits-de-securite-et-de-services-de-confiance-qualifies-dans-le-cadre-du) |
| Recommandations de sécurité concernant l’analyse des flux HTTPS | 2 octobre 2014 | Flux HTTPS | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-de-securite-concernant-lanalyse-des-flux-https) |
| Recommandations de sécurité relatives à Active Directory | 29 août 2014 | Active Directory | — | [lien](https://messervices.cyber.gouv.fr/guides/recommandations-de-securite-relatives-active-directory) |
| Usage sécurisé d’(Open)SSH | 23 janvier 2014 | (Open)SSH | — | [lien](https://messervices.cyber.gouv.fr/guides/usage-securise-dopenssh) |
| Sécuriser une architecture de téléphonie sur IP | 21 janvier 2014 | Téléphonie sur IP | — | [lien](https://messervices.cyber.gouv.fr/guides/securiser-une-architecture-de-telephonie-sur-ip) |
| Le guide des bonnes pratiques de configuration de BGP | 1 octobre 2013 | BGP | — | [lien](https://messervices.cyber.gouv.fr/guides/le-guide-des-bonnes-pratiques-de-configuration-de-bgp) |
| Sécuriser les accès Wi-Fi | 3 avril 2013 | Wi-Fi | — | [lien](https://messervices.cyber.gouv.fr/guides/securiser-les-acces-wi-fi) |
| Sécurité des systèmes de virtualisation | 13 juillet 2012 | Virtualisation | — | [lien](https://messervices.cyber.gouv.fr/guides/securite-des-systemes-de-virtualisation) |
| La défense en profondeur appliquée aux systèmes d’information | 2 février 2011 | Cyberdéfense | — | [lien](https://messervices.cyber.gouv.fr/guides/la-defense-en-profondeur-appliquee-aux-systemes-dinformation) |
| Externalisation et sécurité des systèmes d’information : un guide pour maîtriser les risques | 3 décembre 2010 | Externalisation | Gestion des risques cyber | [lien](https://messervices.cyber.gouv.fr/guides/externalisation-et-securite-des-systemes-dinformation-un-guide-pour-maitriser-les) |
| TDBSSI — Guide d’élaboration de tableaux de bord de sécurité des systèmes d’information | 9 juillet 2009 | TDBSSI | — | [lien](https://messervices.cyber.gouv.fr/guides/tdbssi-guide-delaboration-de-tableaux-de-bord-de-securite-des-systemes-dinformation) |
| Guide relatif à la maturité SSI | 9 juillet 2009 | Maturité SSI | — | [lien](https://messervices.cyber.gouv.fr/guides/guide-relatif-la-maturite-ssi) |
---

## Méthode du scan

1. `curl` sur `https://messervices.cyber.gouv.fr/guides` — la page rend les 178 fiches en une seule fois, sans pagination.
2. Extraction des attributs `data-cible` (titre), `detailend` (date), `detailstart` (collection), `badges` (thématique) et `href` de chaque `<dsfr-card>`.
3. Filtrage des 50 traductions anglaises (slugs préfixés `en-`).
4. Recoupement des 13 guides de la skill avec les métadonnées des PDF (`sources.md`).

À rejouer après toute révision ANSSI. Le catalogue ne fournit ni numéro de version ni référence ANSSI-PA/PG : ces informations ne se trouvent que dans les PDF.
