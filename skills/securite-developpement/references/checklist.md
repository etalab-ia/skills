# Checklist de sécurité — les 14 domaines du socle

Référentiel parcouru par le workflow d'audit (voir [`../SKILL.md`](../SKILL.md)) et consulté domaine par domaine en mode conseil. Pour chaque domaine, attribuer un statut **OK / KO / NA / Partiel** et, pour chaque **KO**, qualifier l'exploitabilité (voir [`rapport.md`](rapport.md)).

Chaque règle porte sa source entre crochets — identifiants résolus dans [`sources.md`](sources.md). `[DINUM]` signale une bonne pratique **sans équivalent dans les guides ANSSI** : utile, mais à ne jamais présenter comme une exigence de l'ANSSI.

Les valeurs chiffrées (tailles de clés, suites, longueurs, durées) ne sont pas répétées ici : elles sont dans [`valeurs-anssi.md`](valeurs-anssi.md), qui fait foi.

Les modules conditionnels — [langage C](modules/langage-c.md), [Rust](modules/langage-rust.md), [CMS](modules/cms.md) — ne sont chargés que si le projet est concerné.

---

## 1. TLS / HTTPS

- [ ] HTTPS sur tous les échanges, aucun HTTP en production — [WEB R1] [HYGIENE M18, M21]
- [ ] **TLS 1.3 pris en charge et privilégié, TLS 1.2 accepté** — [TLS R3]
- [ ] SSLv2, SSLv3, TLS 1.0 et TLS 1.1 désactivés — [TLS R4]
- [ ] Suites cryptographiques limitées à celles de [`valeurs-anssi.md`](valeurs-anssi.md) §1 — [TLS R9, R10, R12]
- [ ] **Confidentialité persistante (PFS) assurée** : ECDHE, ou DHE à défaut — [TLS R6, R7]
- [ ] Ordre de suites du serveur prioritaire sur celui du client — [TLS R13]
- [ ] Certificats valides, renouvelés avant expiration, durée ≤ 825 jours — [TLS R25]
- [ ] Extensions `KeyUsage`, `ExtendedKeyUsage`, `SubjectAlternativeName` correctement renseignées — [TLS R27, R28, R29]
- [ ] Sources de révocation présentes (CRLDP ou AIA), agrafage OCSP préféré — [TLS R33, R35]
- [ ] Compression TLS désactivée — [TLS R19]
- [ ] Tickets de session à durée de vie ≤ 24 h — [TLS R20]
- [ ] Données 0-RTT refusées côté serveur — [TLS R23]
- [ ] **HSTS activé** avec `max-age` d'un an et `includeSubDomains` — [WEB R2]
- [ ] Composants TLS maintenus à jour — [TLS R2]
- [ ] Certificats surveillés dans les *Certificate Transparency logs* — [WEB R3]

## 2. Cryptographie

- [ ] **Aucune construction cryptographique maison** — bibliothèques éprouvées uniquement — [CRYPTO §2.2.5, §2.2.6]
- [ ] Chiffrement symétrique : **AES** ou **ChaCha20**, clé ≥ 128 bits — [CRYPTO R1, R2] [CRYPTO-DIM RègleTailleCléSym]
- [ ] **Mode de chiffrement authentifié** (GCM, CCM, EAX, ChaCha20-Poly1305, Encrypt-then-MAC) — jamais un mode de chiffrement seul — [CRYPTO R4, R12]
- [ ] Si GCM : IV de **96 bits exactement**, construction déterministe, jamais réutilisé, MAC non tronqué — [CRYPTO notes 4.5.c à 4.5.f]
- [ ] Unicité de la paire (clé, IV/nonce) garantie pour tout mode à flot ou authentifié — [CRYPTO notes 3.2.a, 4.1.b]
- [ ] Hachage : **SHA-2 ou SHA-3, sortie ≥ 256 bits**. SHA-1 et MD5 absents — [CRYPTO R3]
- [ ] MAC : CMAC, HMAC (clé ≥ 128 bits) ou GMAC ; troncature ≥ 96 bits — [CRYPTO R7, R8, R9, R10]
- [ ] Tailles de clés asymétriques conformes à [`valeurs-anssi.md`](valeurs-anssi.md) §2 — [CRYPTO R16, R17, R18] [CRYPTO-DIM]
- [ ] `RSA PKCS#1 v1.5` non utilisé (chiffrement comme signature) — [CRYPTO R20, R21]
- [ ] **Aléa issu d'un DRBG conforme** (HMAC-DRBG, Hash-DRBG, CTR-DRBG), germe ≥ 128 bits d'entropie — [CRYPTO R23]
- [ ] Aucun générateur non cryptographique pour un usage de sécurité (`Math.random`, `rand()`) — [CRYPTO R23]
- [ ] **« Une clé, un usage »** : clés distinctes pour chiffrement, MAC, signature, authentification — [CRYPTO §2.2.3]
- [ ] Si la donnée doit rester protégée **au-delà de 2030** : dimensionnement post-quantique, et tout mécanisme post-quantique **hybridé** avec un schéma classique — [CRYPTO R19] [CRYPTO-DIM RecoSécuLongTerme]

## 3. Gestion des secrets

- [ ] **Aucun secret dans le code source** (clés d'API, mots de passe, jetons) — [ESS-DEVSECOPS 4]
- [ ] Aucun secret dans les **journaux de *jobs*** ni dans l'historique du dépôt — [ESS-DEVSECOPS 4]
- [ ] **Gestionnaire de secrets distinct par environnement** (hors production / production) — [ESS-DEVSECOPS 4]
- [ ] Fichiers `.env` et équivalents dans `.gitignore` — [DINUM]
- [ ] Détection automatique de secrets en pré-commit ou en CI — [DINUM]
- [ ] Éléments d'authentification par défaut changés sur tous les équipements et services — [HYGIENE M12]
- [ ] Mots de passe stockés protégés sur les systèmes — [HYGIENE M11]
- [ ] **Capacité à révoquer et régénérer un secret en urgence**, procédure connue — [DINUM]
- [ ] Rotation périodique des secrets planifiée — [DINUM]

> Un secret exposé accidentellement doit être **révoqué et régénéré**, pas seulement retiré du code : l'historique Git le conserve.

## 4. Authentification, MFA et mots de passe

- [ ] **MFA sur tous les accès à privilèges** — administration, dépôts de code, cloud, back-office — [MFA R1] [ESS-DEVSECOPS 8] [HYGIENE M13]
- [ ] Les facteurs relèvent de **catégories différentes** (connaissance / possession / inhérent) — [MFA §2.4]
- [ ] **SMS non utilisé** comme canal de réception d'un facteur — [MFA R8]
- [ ] Biométrie jamais employée comme facteur unique — [MFA R40, R41]
- [ ] Longueurs de mots de passe conformes au niveau de sensibilité — [MFA R21]
- [ ] **Aucune longueur maximale contraignante** imposée — [MFA R22]
- [ ] **Sel aléatoire ≥ 128 bits par compte** — [MFA R28]
- [ ] **Dérivation *memory-hard*** (Argon2, scrypt) ; PBKDF2 à forte itération en repli — [MFA R29, R29-]
- [ ] Politique d'expiration adaptée : pas d'expiration par défaut sur les comptes ordinaires, expiration sur les comptes à privilèges — [MFA R24, R25]
- [ ] **Limitation des tentatives** d'authentification sur une période donnée — [MFA R10]
- [ ] **Messages d'erreur non discriminants** : ne pas révéler quel facteur a échoué ni si le compte existe — [MFA R14]
- [ ] Durée de session limitée, invalidation côté serveur à la déconnexion — [MFA R12]
- [ ] Authentification réalisée au travers d'un canal sécurisé — [MFA R11]
- [ ] Historique d'utilisation des facteurs conservé — [MFA R9]
- [ ] Processus de **révocation** des facteurs en place, délais définis — [MFA R18, R19]
- [ ] Méthode de recouvrement d'accès prévue, sans transmission du mot de passe en clair — [MFA R30]
- [ ] Chaque personne identifiée nommément, rôles utilisateur et administrateur distincts — [HYGIENE M8]
- [ ] **Moindre privilège** sur les ressources sensibles — [HYGIENE M9] [CLOIS R1]
- [ ] Inventaire des comptes privilégiés tenu à jour — [HYGIENE M5]
- [ ] Procédures d'arrivée, de départ et de changement de fonction appliquées — [HYGIENE M6]

## 5. Validation des entrées et bases de données

- [ ] **Toutes** les entrées validées côté serveur — le client n'est jamais de confiance — [DINUM]
- [ ] Schémas de validation explicites (Zod, Joi, Pydantic…) — [DINUM]
- [ ] Conformité vérifiée pour les données issues de sources externes — [WEB R8]
- [ ] Échappement des contenus inclus vérifié — [WEB R7]
- [ ] **Requêtes préparées / paramétrées**, aucune concaténation de chaînes SQL — [ESS-BDD]
- [ ] Taille des requêtes bornée (corps, téléversements, chaînes de requête) — [DINUM]
- [ ] `Content-Type` explicite sur chaque réponse — [WEB R6]
- [ ] **Comptes de base de données distincts** pour les humains et pour les applications — [ESS-BDD]
- [ ] Droits limités au strict nécessaire, rôles définis — [ESS-BDD] [CLOIS R1]
- [ ] Compte administrateur natif du SGBD réservé au dernier recours — [ESS-BDD]
- [ ] **MFA pour les administrateurs de base de données** — [ESS-BDD]
- [ ] Chiffrement des données **en transit et au repos** — [ESS-BDD]
- [ ] **Aucune donnée de production dans les environnements de développement** ou assimilés — [ESS-BDD]
- [ ] Fonctions avancées du SGBD permettant de lire, écrire ou exécuter des fichiers système **désactivées** — [ESS-BDD]
- [ ] Typage des données imposé au niveau du schéma — [ESS-BDD]
- [ ] Données isolées des fichiers de configuration (partitions ou répertoires distincts) — [ESS-BDD]
- [ ] Accès aux données restreints par des mécanismes internes au SGBD (vues) — [ESS-BDD]
- [ ] SGBD maintenu à jour depuis les dépôts officiels ; extensions et outils d'administration minimisés — [ESS-BDD]
- [ ] Supervision du SGBD en place (stockage, CPU, RAM, événements suspects) — [ESS-BDD]
- [ ] SGBD non exposé directement sur Internet — [DINUM]
- [ ] Migrations de schéma versionnées et réversibles — [DINUM]

## 6. Dépendances et composants tiers

- [ ] **Nombre de dépendances directes minimisé** — [ESS-DEVSECOPS 5] [WEB R61]
- [ ] Dépendances **évaluées avant adoption** sur la vitalité du projet, le MCO et le MCS — [ESS-LIBRE]
- [ ] Réactivité du projet amont sur les vulnérabilités vérifiée : point de contact sécurité, procédure publique de divulgation, délai de correction — [ESS-LIBRE]
- [ ] **Correctifs de sécurité appliqués avant déploiement** — [ESS-DEVSECOPS 5]
- [ ] Composants tiers maintenus à jour — [WEB R62] [HYGIENE M34]
- [ ] **Cœur des composants tiers jamais modifié** (sinon les mises à jour deviennent impossibles) — [WEB R63]
- [ ] **SBOM disponible** au format SPDX ou CycloneDX — [ESS-LIBRE]
- [ ] Outil de gestion des dépendances enrichi en données de vulnérabilité (`npm audit`, `pip-audit`, Dependabot, `trivy`) — [ESS-LIBRE]
- [ ] **Audit régulier de l'évolution des contributions** du projet amont, analyse manuelle et outillée — [ESS-LIBRE]
- [ ] Fin de maintenance anticipée, adhérences logicielles limitées — [HYGIENE M35]
- [ ] Fichier de verrouillage présent et versionné (`package-lock.json`, `poetry.lock`, `Cargo.lock`) — [DINUM]
- [ ] Versions épinglées, mises à jour revues plutôt qu'automatiques en production — [DINUM]
- [ ] Risques propres aux registres pris en compte : typosquatting, compromission de compte de publication, scripts `postinstall` — [DINUM]
- [ ] Bibliothèques publiques obscurcies effectuant des appels CORS écartées, ou isolées — [WEB R42, R42-]

> **Ce que l'ANSSI ne dit pas.** Le guide *Sélection d'un logiciel libre* ne traite ni la **licence**, ni la **réversibilité / plan de sortie**, ni les risques propres aux registres de paquets. Ces critères restent pertinents mais relèvent du `[DINUM]`.

## 7. Journalisation

- [ ] Journalisation prise en compte **dès la conception** du projet — [LOG R1, §2.1]
- [ ] **Socle minimal couvert** : authentification, gestion des comptes, stratégies de sécurité, accès aux ressources sensibles, activité des processus et des systèmes — [LOG annexe A]
- [ ] Événements liés à la sécurité **et** activité du service journalisés — [LOG §2.1]
- [ ] Granularité de journalisation explicitement choisie — [LOG R6]
- [ ] **Horodatage sur tous les événements**, paramètres homogènes, précision ≥ seconde — [LOG R3, R4]
- [ ] Horloges synchronisées sur des sources cohérentes — [LOG R5]
- [ ] Format **interprétable** : champs fixes, grammaire définie, source identifiable et intelligible — [LOG §2.1]
- [ ] **Aucune donnée personnelle superflue**, mécanisme de suppression automatique prévu — [LOG §2.1, R25]
- [ ] **Aucun secret dans les journaux** ; modes `debug`/`verbose` désactivés en production — [LOG §2.1]
- [ ] Journaux **centralisés** — [LOG R9, R9-] [HYGIENE M36]
- [ ] Transfert **en temps réel**, sur TCP, via un canal chiffré et authentifié — [LOG R14, R16, R17]
- [ ] Durées de rétention conformes à la réglementation — [LOG R25]
- [ ] Politique de rotation définie et appliquée — [LOG R24]
- [ ] Droits d'accès aux journaux restreints en **écriture**, **suppression** et **lecture** — [LOG R26, R26+, R27]
- [ ] Espace disque de stockage supervisé — [LOG R22]
- [ ] Couverture de la chaîne de collecte contrôlée régulièrement — [LOG R12]
- [ ] Alertes sur les événements anormaux (pics de 401/403, tentatives de force brute) — [DINUM]

## 8. Sécurité navigateur et API

- [ ] **CSP déclarée par en-tête HTTP**, avec `default-src` définie et jamais à `*` — [WEB R14, R16]
- [ ] CSP sans `'unsafe-inline'`, `'unsafe-eval'` ni `data:` — [WEB R15]
- [ ] Composition des pages dissociée : **pas de CSS ni de JavaScript *inline*** — [WEB R5]
- [ ] Protection anti-*clickjacking* par `frame-ancestors`, complétée par `X-Frame-Options` — [WEB R17, R18]
- [ ] `Referrer-Policy` définie ; stratégie par défaut et `unsafe-url` écartées — [WEB R21]
- [ ] Attributs de cookies corrects : `Secure`, `HttpOnly`, `SameSite` — [WEB R29, R30, R31, R32, R33]
- [ ] **Aucune information sensible en `localStorage`, `sessionStorage`, `IndexedDB` ou cookie** (hors jeton de session) — [WEB R23, R24, R26]
- [ ] **`eval()` et constructions équivalentes proscrites** — [WEB R9, R10]
- [ ] API DOM utilisée sûrement : `textContent` plutôt qu'`innerHTML` — [WEB R4]
- [ ] Intégrité des ressources internes et tierces contrôlée par **SRI** — [WEB R11, R12]
- [ ] `Origin` vérifiée côté serveur pour toute requête CORS ; pas de `Access-Control-Allow-Origin: *` — [WEB R40]
- [ ] **Jeton anti-CSRF d'au moins 128 bits d'entropie** sur les appels modifiants — [WEB R38]
- [ ] `target="_blank"` accompagné de `rel="noopener"` — [WEB R45]
- [ ] `postMessage` avec origine explicite ; origine et format contrôlés en réception — [WEB R54, R55]
- [ ] Écriture de `document.domain` et usage de JSON-P proscrits — [WEB R57, R58]
- [ ] Traitements de faible confiance cloisonnés en iframe `sandbox` ou Web Worker — [WEB R48, R50, R51]
- [ ] **Profils de déploiement distincts par contexte**, profil non durci impossible à déployer en production — [WEB R59, R60]
- [ ] Aucun détail technique dans les messages d'erreur en production — [WEB R59]
- [ ] `X-Content-Type-Options: nosniff` — [DINUM]
- [ ] Authentification sur tous les points d'entrée (hors santé et métadonnées publiques) — [DINUM]
- [ ] **Limitation de débit** (*rate limiting*) en place — [DINUM]
- [ ] Pagination obligatoire sur les points d'entrée de liste — [DINUM]
- [ ] API versionnées (`/v1/`, `/v2/`) — [DINUM]

## 9. Cloisonnement système

- [ ] **Besoins de cloisonnement traités dès l'initiation du projet**, au même titre que les besoins fonctionnels — [CLOIS R2]
- [ ] **Interdiction par défaut**, autorisation explicite du strict nécessaire — [CLOIS R1, R22]
- [ ] Usages identifiés et **cloisonnés entre eux** — [CLOIS R6, R8]
- [ ] **Administration traitée comme un usage à part entière**, dans son propre domaine — [CLOIS §3.2]
- [ ] Surface d'attaque minimisée : chaque domaine n'expose que les interfaces utiles à son usage — [CLOIS R7]
- [ ] Surface de friction minimisée : **appels système inutilisés interdits** — [CLOIS R9]
- [ ] Le mécanisme de cloisonnement s'exécute à un **privilège supérieur** aux tâches cloisonnées — [CLOIS R21]
- [ ] Solutions choisies pour leur prise en compte du moindre privilège — [CLOIS R3]
- [ ] Le composant **ne dégrade pas la sécurité du système hôte** et n'exige pas d'abaisser son durcissement — [CLOIS R25]
- [ ] Cloisonnement **emboîté** en défense en profondeur (ex. conteneur dans machine virtuelle) — [CLOIS §4.2.2]
- [ ] Isolation réseau entre services ; aucune interface réseau exposée à un domaine qui n'en a pas besoin — [CLOIS §5]
- [ ] Services exposés sur Internet cloisonnés du reste du système — [HYGIENE M23]
- [ ] Environnements dev / staging / production séparés, avec des accès distincts — [ESS-DEVSECOPS 9] [DINUM]

> **Ne pas surestimer les conteneurs.** Pour l'ANSSI, un conteneur *est* une frontière de sécurité, mais sa robustesse dépend entièrement de la solution retenue, du **durcissement du noyau partagé** et de la configuration effective. Un conteneur non durci sur noyau standard n'équivaut pas à une machine virtuelle — d'où la recommandation d'emboîtement.

## 10. Conteneurs et déploiement

- [ ] Images basées sur des images **minimales** (Alpine, distroless) — [CLOIS R18] [DINUM]
- [ ] **Processus non exécutés en root** ; aucun conteneur privilégié — [CLOIS R21]
- [ ] Capacités réduites au strict nécessaire — [CLOIS §5]
- [ ] Appels système inutilisés interdits (seccomp) — [CLOIS §5]
- [ ] **Système de fichiers en lecture seule**, sauf répertoire d'écriture explicitement défini — [CLOIS §5]
- [ ] Utilisation des ressources système limitée — [CLOIS §5]
- [ ] Privilèges abandonnés dès qu'ils ne sont plus nécessaires — [CLOIS §5]
- [ ] Techniques de durcissement appliquées (ASLR, W⊕X, canaris) — [CLOIS R19]
- [ ] Règles de durcissement appliquées aux OS hébergeant les applications — [ESS-DEVSECOPS 13]
- [ ] Composants inutilisés supprimés, ou à défaut désactivés par configuration — [CLOIS R18]
- [ ] Images scannées avant déploiement (`trivy image`) — [DINUM]
- [ ] Sondes de vivacité et de disponibilité configurées — [DINUM]

## 11. Chaîne de développement (CI/CD)

- [ ] **La CI/CD de production est traitée comme un système d'administration** : moindre privilège, journalisation et supervision — [ESS-DEVSECOPS 3]
- [ ] Jetons **générés à la demande**, pas de jeton permanent à large portée — [ESS-DEVSECOPS 3]
- [ ] **MFA pour l'accès aux dépôts et la signature des *commits*** — [ESS-DEVSECOPS 8]
- [ ] **Infrastructures CI/CD de développement et de production séparées**, non exposées directement sur Internet — [ESS-DEVSECOPS 9]
- [ ] Infrastructure CI/CD **réinstanciée régulièrement**, sans données persistantes — [ESS-DEVSECOPS 10]
- [ ] Besoins de confidentialité évalués vis-à-vis de l'infrastructure CI/CD (localisation, SaaS public) — [ESS-DEVSECOPS 11]
- [ ] **Tests de sécurité automatisés** dans la CI : non-régression, étanchéité entre profils d'utilisateurs, analyses statique et dynamique, conformité de l'IaC — [ESS-DEVSECOPS 6]
- [ ] **Intégrité du code maintenue de bout en bout** ; tags de version des artefacts signés et signatures vérifiées — [ESS-DEVSECOPS 7]
- [ ] Cartographie des applications, droits, flux et rôles maintenue à jour — [ESS-DEVSECOPS 1]
- [ ] Analyse de risque globale menée, incluant postes des développeurs, sous-traitance et chaîne CI/CD — [ESS-DEVSECOPS 2]
- [ ] Règles de développement sécurisé imposées dans l'équipe — [ESS-DEVSECOPS 12]
- [ ] Branches protégées, revue de code obligatoire avant fusion — [DINUM]
- [ ] Contrôles bloquants positionnés avant le déploiement, pas seulement informatifs — [DINUM]

## 12. Poste de développement

- [ ] **Chiffrement du disque activé** (FileVault, LUKS, BitLocker) — [HYGIENE M31]
- [ ] Niveau de sécurité minimal sur tout le parc : verrouillage de session, mises à jour, antivirus — [HYGIENE M14]
- [ ] Pare-feu local activé et configuré — [HYGIENE M17]
- [ ] **Pas de compte administrateur pour l'usage quotidien** — [HYGIENE M29]
- [ ] Sécurisation physique des terminaux nomades — [HYGIENE M30]
- [ ] Connexion réseau sécurisée en situation de nomadisme (VPN, aucun flux en clair sur Wi-Fi public) — [HYGIENE M32]
- [ ] Équipes opérationnelles formées à la sécurité et au développement sécurisé — [HYGIENE M1]

## 13. Sauvegarde et continuité

- [ ] **Politique de sauvegarde définie et appliquée** sur les composants critiques — [HYGIENE M37]
- [ ] Sauvegarde du contenu et de la configuration paramétrée — [ESS-BDD]
- [ ] **Restauration testée périodiquement** — sans test, une sauvegarde est une hypothèse — [DINUM]
- [ ] Sauvegardes isolées du système sauvegardé (hors ligne ou compte distinct) — [DINUM]
- [ ] Procédure de reprise d'activité documentée — [DINUM]

## 14. Gestion des incidents

- [ ] **Procédure de gestion des incidents de sécurité définie** — [HYGIENE M40]
- [ ] **Référent sécurité désigné** et connu de l'équipe — [HYGIENE M39]
- [ ] Contact CERT ministériel identifié — [DINUM]
- [ ] Capacité à révoquer des accès et rotater des secrets en urgence — [DINUM]
- [ ] Contrôles et audits de sécurité réguliers, avec application des actions correctives — [HYGIENE M38 · *renforcé*]
- [ ] Analyse de risque formelle menée — [HYGIENE M41 · *renforcé*]
- [ ] Produits et services qualifiés par l'ANSSI privilégiés — [HYGIENE M42 · *renforcé*]

> Les mesures 38, 41 et 42 relèvent du niveau **renforcé** du guide d'hygiène : leur absence n'est pas une non-conformité au niveau standard, mais une marge de progression à signaler.
