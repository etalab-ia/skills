# Module conditionnel — CMS

**Charger uniquement si** un CMS est détecté : `wp-config.php` (WordPress), Drupal, Joomla, ou hébergement CMS géré.

Dérivé de l'Essentiel *Mise en œuvre sécurisée d'un CMS* (ANSSI, V1.1, 12/2023) — voir [`../sources.md`](../sources.md).

## Comment citer ce guide

Cet Essentiel **ne numérote pas ses recommandations** : c'est une fiche recto-verso de dix bonnes pratiques présentées en puces. La numérotation 1 à 10 ci-dessous est **ajoutée par la DINUM pour la traçabilité** et ne figure pas dans le document. On cite donc `[ESS-CMS 3]` en sachant que le « 3 » est notre repère, le libellé exact faisant foi (reproduit dans [`../sources.md`](../sources.md)).

> **C'est un document d'aiguillage, pas un référentiel autonome** : 9 des 10 puces renvoient à un autre guide ANSSI. Les règles ci-dessous restituent l'Essentiel ; le détail opérationnel se trouve dans les domaines du socle qu'elles pointent.

---

## 1. Choix et installation

- [ ] Offre CMS évaluée au regard des critères de sécurité de ce module avant adoption — [ESS-CMS 1]
- [ ] **HTTPS activé** conformément à l'annexe B du guide TLS ; configuration vérifiée par un outil de test automatisé (ex. Mozilla Observatory) — [ESS-CMS 2] → domaine 1
- [ ] **Utilisateur par défaut du CMS désactivé** (il est généralement administrateur) — [ESS-CMS 5]
- [ ] Valeurs par défaut changées (comptes, secrets) — [ESS-CMS 5] → domaine 4

## 2. Extensions et thèmes

C'est la surface d'exposition la plus large d'un CMS, et la seule recommandation que l'Essentiel y consacre.

- [ ] Extensions (*plugins*) et thèmes limités **au strict nécessaire** — [ESS-CMS 3]
- [ ] Extensions et thèmes utilisés sont **activement maintenus** — [ESS-CMS 3]
- [ ] Extensions et thèmes ont fait l'objet d'une **validation de la part de l'éditeur** — [ESS-CMS 3]

> **Limite à connaître.** L'Essentiel **ne formule aucune obligation explicite de mise à jour des extensions**, ni du cœur du CMS : le maintien à jour n'y est couvert qu'indirectement, par le critère « activement maintenus » et par le renvoi au *maintien en condition de sécurité*. Une règle exigeant une politique de mise à jour datée relève donc du `[DINUM]`, pas de l'ANSSI. Le détail est délégué au chapitre 6 du guide *Recommandations pour la mise en œuvre d'un site Web*.

## 3. Administration et authentification

- [ ] **MFA en place pour les administrateurs fonctionnels du site** — [ESS-CMS 5] → domaine 4
- [ ] Compatibilité du CMS vérifiée sur : cycle de vie des facteurs d'authentification, limitation des tentatives, innocuité des messages d'erreur, politique de mots de passe, stockage sécurisé des mots de passe — [ESS-CMS 5] → domaine 4
- [ ] Poste d'administration durci, ports en écoute minimisés, protocoles sécurisés (SSH, TLS), **comptes d'administration dédiés**, maintien en condition de sécurité — [ESS-CMS 4]

> **Absent de l'Essentiel** : le changement ou la dissimulation de l'URL d'administration (`/wp-admin`, restriction par IP). Le guide traite la protection de l'interface d'administration par le poste et les comptes, pas par l'URL. Ne pas attribuer cette mesure à l'ANSSI.

## 4. Exposition réseau

- [ ] Flux d'interconnexion du CMS avec Internet et ouverture des ports **identifiés et limités au strict nécessaire** — [ESS-CMS 8]
- [ ] Disponibilité et résilience face au déni de service traitées — [ESS-CMS 8]
- [ ] Cas de la **récupération de contenus externes par le CMS** examiné (chapitre 4 du guide *Interconnexion à Internet*) — [ESS-CMS 8]

## 5. Sécurité côté navigateur

- [ ] **HSTS**, **Content Security Policy** et **sécurisation des cookies de session** mis en œuvre — [ESS-CMS 7] → domaine 8

## 6. Durcissement de l'environnement d'exécution

Moindre privilège appliqué aux trois couches — [ESS-CMS 10] :

- [ ] au **runtime** sous-jacent (ex. manuel de sécurité de PHP)
- [ ] aux **droits de la base de données** → domaine 5
- [ ] à la **configuration système** (niveaux minimal et intermédiaire du guide *Configuration d'un système GNU/Linux*) → domaines 9 et 10

> **Absent de l'Essentiel** : les permissions de fichiers, et le compte de base de données applicatif dédié distinct d'un compte administrateur. Le moindre privilège sur la base en est le fondement, mais la mesure n'est pas formulée — la qualifier `[DINUM]` si on l'exige.

## 7. Journalisation et sauvegarde

- [ ] **Journaux du CMS collectés, analysés, avec alertes** (annexes A et C du guide journalisation) — [ESS-CMS 9] → domaine 7
- [ ] **Contenu du site et configuration du CMS sauvegardés** (export de la base de données et des fichiers de configuration) — [ESS-CMS 6] → domaine 13

> L'Essentiel ne donne ni fréquence, ni durée de rétention, ni règle 3-2-1 pour les sauvegardes : tout est délégué aux publications dédiées de l'ANSSI.
