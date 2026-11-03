---
name: dsfr
description: Système de design de l'État français (DSFR) 1.15.4 en HTML et CSS - 51 composants, fondamentaux (grille, couleurs, typographie, icônes, espacements), modèles de pages et de formulaires, accessibilité de chaque composant, avec le HTML officiel et les classes `fr-*`. À utiliser pour créer, modifier ou vérifier le HTML d'un site ou service de l'État, sans framework ou avec un moteur de gabarits, quand l'utilisateur mentionne le DSFR, le design system de l'État, systeme-de-design.gouv.fr, Marianne ou un site en .gouv.fr, ou quand le projet charge `@gouvfr/dsfr`. Pour un projet React avec `@codegouvfr/react-dsfr`, ou pour un audit de conformité RGAA complet, préférer un skill dédié s'il est installé (react-dsfr, rgaa). Also use for French government design system / DSFR questions in English.
---

# DSFR 1.15.4

Documentation officielle convertie depuis `@gouvfr/dsfr@1.15.4`. Les classes et la structure HTML changent d'une version à l'autre : lire le fichier du composant avant d'écrire son HTML, ne pas se fier à sa mémoire.

Dans un projet existant, partir de son intégration du DSFR : version installée (`package.json`, `node_modules/@gouvfr/dsfr`, dossier `dist` copié), chemins des assets (dont `artwork/` pour les pictogrammes), gabarits et composants déjà écrits. Si la version installée n'est pas 1.15.4, le signaler : les classes et la structure peuvent différer de cette documentation. Elle prime alors : reprendre le balisage des composants déjà présents dans le projet, et pour un nouveau composant vérifier dans le [CHANGELOG du DSFR](https://github.com/GouvernementFR/dsfr/blob/main/CHANGELOG.md) que ses classes existent dans cette version avant de suivre `exemples.md` ; proposer la montée de version plutôt que de mélanger deux versions.

## Usage réservé à l'État

Le DSFR porte l'identité graphique de l'État. Ses [modalités d'utilisation](https://github.com/GouvernementFR/dsfr/blob/main/doc/legal/cgu.md) le réservent aux sites en .gouv.fr et aux applications mobiles des services de l'État (et des opérateurs agréés par leur ministère de tutelle). Hors de ce cadre, il peut créer une confusion avec un service public officiel, réprimée par l'article 433-13 du code pénal.

- Avant de produire une interface, vérifier que le projet relève de l'État : domaine en .gouv.fr, dépôt ou organisation d'une administration, service public de l'État nommé dans la demande. Si le contexte ne permet pas de le savoir, rappeler en une phrase que le DSFR est réservé à l'État, puis continuer.
- Pour un projet qui n'en relève pas (site privé, association, collectivité territoriale, projet personnel), ne pas utiliser le DSFR : l'expliquer et proposer un autre système de design.
- Refuser toute demande qui imite un service public sans en être un : faux site administratif, page de paiement ou de collecte de données aux couleurs de l'État, copie d'un site officiel.
- Répondre aux questions sur le DSFR ou auditer un site existant reste possible.

## Règles

1. Partir du balisage de `exemples.md` du composant et l'adapter, plutôt que de l'écrire de mémoire.
2. Ne jamais inventer de classe : toute classe `fr-*` doit figurer dans `reference/classes.txt`, toute icône dans `reference/icones.md`.
3. Rendre les `id` uniques dans la page : les exemples réutilisent les mêmes. Chaque `aria-controls`, `aria-labelledby`, `aria-describedby` et `for` doit pointer vers un `id` existant.
4. Sans DSFR installé dans le projet, charger le CDN versionné (`@gouvfr/dsfr@1.15.4`), jamais `@gouvfr/dsfr` sans version.
5. Un seul bouton primaire par groupe d'actions, les autres en secondaire ou tertiaire.
6. Formulaires : champ dans `fr-input-group`, `<label class="fr-label">` lié par `for`, aide dans un `<span class="fr-hint-text">` à l'intérieur du label, messages dans `fr-messages-group` relié par `aria-describedby`, erreur avec `fr-input-group--error` et `fr-message--error`.
7. Icônes décoratives en `aria-hidden="true"`. Lien qui ouvre une nouvelle fenêtre : `target="_blank" rel="noopener"` et `title="Libellé - nouvelle fenêtre"`.
8. Ne pas surcharger couleurs, typographie ou espacements en CSS : passer par les variantes, tokens et classes utilitaires documentés. Couleurs et thème sombre : `fondamentaux/color`.

## Où chercher

| Besoin | Fichier |
|---|---|
| Créer une page (imports, squelette, thème, JS, frameworks) | [demarrage.md](demarrage.md) |
| Quand utiliser un composant, règles éditoriales | `composants/<nom>/index.md` |
| HTML, classes, dépendances CSS, API et événements JS | `composants/<nom>/code.md` |
| Clavier, ARIA, critères RGAA | `composants/<nom>/accessibilite.md` |
| Anatomie, variantes, tailles, états | `composants/<nom>/design.md` |
| HTML officiel prêt à adapter | `composants/<nom>/exemples.md` |
| Grille, couleurs, typographie, espacements, icônes | `fondamentaux/<nom>/` |
| Pages complètes et blocs de formulaire | `modeles/pages/<nom>/`, `modeles/blocs/<nom>/` |
| Auditer une page existante | [audit.md](audit.md) et `node scripts/verifier.mjs page.html` |

Les fichiers `exemples.md` sont longs : lister les variantes avec `grep -n '^###' composants/<nom>/exemples.md` puis ne lire que la section utile.

Avec `@codegouvfr/react-dsfr` ou `@gouvminint/vue-dsfr`, utiliser les composants de la bibliothèque ; ce skill sert alors de référence pour les règles d'usage et d'accessibilité.

Les composants marqués *(sans code)* n'existent qu'en maquette ou sont dépréciés : ne pas les implémenter avec des classes inventées, proposer l'alternative indiquée dans leur `index.md`. Le marquage analytics (Eulerian) n'est pas couvert : renvoyer vers https://www.systeme-de-design.gouv.fr/.

## Composants

- `accordion` [Accordéon](composants/accordion/index.md) : Masquer ou révéler du contenu textuel
- `alert` [Alerte](composants/alert/index.md) : Relayer une information importante
- `badge` [Badge](composants/badge/index.md) : Affichage d’un statut informatif
- `breadcrumb` [Fil d'Ariane](composants/breadcrumb/index.md) : Se repérer dans l’arborescence avec le fil d’Ariane.
- `button` [Bouton](composants/button/index.md) : Déclenchement d’une action dans l’interface
- `callout` [Mise en avant](composants/callout/index.md) : Mettre en valeur une information secondaire.
- `card` [Carte](composants/card/index.md) : Carte cliquable redirigeant vers une page éditoriale avec aperçu.
- `checkbox` [Case à cocher](composants/checkbox/index.md) : Sélection multiple dans une liste
- `combobox` [Liste déroulante riche](composants/combobox/index.md) : Composant de sélection multiple enrichi avec fonctions de recherche. *(sans code)*
- `composition` [Zone d'expression visuelle](composants/composition/index.md) : Une section riche et impactante pour mettre en avant un message ou une action. *(sans code)*
- `connect` [Boutons FranceConnect et ProConnect](composants/connect/index.md) : Authentification avec FranceConnect et/ou ProConnect
- `consent` [Gestionnaire de consentement](composants/consent/index.md) : Gérer le consentement des usagers sur les cookies et données personnelles.
- `content` [Contenu médias](composants/content/index.md) : Structurer visuellement une page avec des contenus média.
- `display` [Paramètres d'affichage](composants/display/index.md) : Choisir le thème clair ou sombre d’un site.
- `download` [Téléchargement de fichier](composants/download/index.md) : Composant obsolète remplacé par les variations des composants carte, lien et tuile. *(sans code)*
- `dropdown` [Menu déroulant](composants/dropdown/index.md) : Afficher des actions contextuelles sans encombrer l’interface *(sans code)*
- `follow` [Lettre d'information et réseaux sociaux](composants/follow/index.md) : Inscription à une lettre d’info et accès aux réseaux sociaux.
- `footer` [Pied de page](composants/footer/index.md) : Informations complémentaires en bas de page
- `form` [Formulaire](composants/form/index.md) : Gestion de l'agencement des éléments de formulaire.
- `header` [En-tête](composants/header/index.md) : Identification du site et accès rapides
- `highlight` [Mise en exergue](composants/highlight/index.md) : Mettre en évidence une information essentielle.
- `input` [Champ de saisie](composants/input/index.md) : Saisie de données dans une interface.
- `link` [Lien](composants/link/index.md) : Navigation secondaire vers d’autres contenus
- `logo` [Bloc marque](composants/logo/index.md) : Élément de la charte graphique de l'État français utilisé pour représenter l'identité visuelle de l'État.
- `modal` [Modale](composants/modal/index.md) : Affichage focalisé d’un contenu secondaire
- `navigation` [Navigation principale](composants/navigation/index.md) : Orienter l’usager dans les sections du site.
- `notice` [Bandeau d'information importante](composants/notice/index.md) : Afficher une alerte temporaire prioritaire.
- `pagination` [Pagination](composants/pagination/index.md) : Navigation entre plusieurs pages d’une liste
- `password` [Mot de passe](composants/password/index.md) : Saisie ou création de mot de passe, avec affichage masqué et recommandations de sécurité.
- `quote` [Citation](composants/quote/index.md) : Citer un texte dans un contenu éditorial.
- `radio` [Bouton radio](composants/radio/index.md) : Sélection d’une option unique
- `range` [Curseur](composants/range/index.md) : Sélection d’une valeur sur une échelle
- `search` [Barre de recherche](composants/search/index.md) : Accès rapide à un contenu par mot clé
- `segmented` [Contrôle segmenté](composants/segmented/index.md) : Sélection de vues avec un contrôle segmenté.
- `select` [Liste déroulante](composants/select/index.md) : Sélectionner une option dans une liste.
- `share` [Partage](composants/share/index.md) : Partager un contenu via différents canaux
- `sidemenu` [Menu latéral](composants/sidemenu/index.md) : Naviguer entre pages liées avec un menu latéral.
- `skiplink` [Liens d'évitement](composants/skiplink/index.md) : Accéder rapidement au contenu avec le clavier.
- `stepper` [Indicateur d’étapes](composants/stepper/index.md) : Suivi d’un parcours en plusieurs étapes
- `summary` [Sommaire](composants/summary/index.md) : Navigation entre les sections d’une page
- `tab` [Onglet](composants/tab/index.md) : Structuration de contenu avec des onglets
- `table` [Tableau](composants/table/index.md) : Présentation du composant Tableau pour organiser et comparer des données.
- `tabnav` [Navigation tertiaire](composants/tabnav/index.md) : Composant de navigation de 3e niveau en complément du menu latéral *(sans code)*
- `tag` [Tag](composants/tag/index.md) : Le tag sert à classer ou filtrer les contenus.
- `tile` [Tuile](composants/tile/index.md) : Rediriger l’usager vers du contenu via des tuiles.
- `toggle` [Interrupteur](composants/toggle/index.md) : Basculer entre deux états opposés
- `tooltip` [Infobulle](composants/tooltip/index.md) : Afficher une aide contextuelle discrète.
- `transcription` [Transcription](composants/transcription/index.md) : Affichage de texte lié à un contenu média
- `translate` [Sélecteur de langues](composants/translate/index.md) : Choisir la langue d’affichage du site.
- `upload` [Ajout de fichier](composants/upload/index.md) : Sélection et envoi de fichiers
- `user` [En-tête connectée](composants/user/index.md) : Variante de l’En-tête dédiée aux usagers connectés *(sans code)*

## Fondamentaux

- `base` [Les principes à respecter](fondamentaux/base/index.md) : Les règles fondamentales pour créer des interfaces conformes au DSFR.
- `color` [Couleur](fondamentaux/color/index.md) : Palette de couleurs officielle du DSFR
- `display` [Classes CSS d’affichage](fondamentaux/display/index.md) : Classes CSS pour gérer l’affichage et la visibilité
- `elevation` [Système d'ombre et d'élévation](fondamentaux/elevation/index.md) : Présentation des niveaux d’élévation et des ombres dans le DSFR.
- `favicon` [Icône de favori](fondamentaux/favicon/index.md) : Guide d’intégration du favicon dans vos projets.
- `grid` [Grille et points de rupture](fondamentaux/grid/index.md) : Structure responsive, points de rupture, alignements et classes CSS du DSFR.
- `icon` [Icône](fondamentaux/icon/index.md) : Présentation des icônes fonctionnelles et de leur intégration
- `media` [Média](fondamentaux/media/index.md) : Intégration des images et vidéos dans le DSFR.
- `pictogram` [Pictogramme](fondamentaux/pictogram/index.md) : Principes, style, couleurs et intégration des pictogrammes dans le DSFR.
- `spacing` [Espacement](fondamentaux/spacing/index.md) : Système d’espacement fondé sur la grille 8 points
- `typography` [Typographie](fondamentaux/typography/index.md) : Typographies officielles et styles de texte du DSFR

## Modèles de pages

- `login` [Page de connexion](modeles/pages/login/index.md) : Modèle de page de connexion à un service
- `register` [Page de création de compte](modeles/pages/register/index.md) : Modèle et règles pour une page de création de compte
- `response` [Page d’erreurs](modeles/pages/response/index.md) : Modèles standardisés de pages d’erreurs 404, 500 et 503

## Modèles de blocs de formulaire

- `address` [Bloc fonctionnel d'adresse postale](modeles/blocs/address/exemples.md)
- `civility` [Civilité](modeles/blocs/civility/index.md) : Bloc de demande de civilité avec options de personnalisation
- `company` [Société](modeles/blocs/company/index.md) : Bloc de saisie des données relatives à une société
- `date` [Date unique](modeles/blocs/date/index.md) : Bloc pour la saisie d'une date unique dans un formulaire
- `email` [Adresse électronique](modeles/blocs/email/index.md) : Champ de saisie pour adresse électronique
- `forms` [Formulaires](modeles/blocs/forms/index.md) : Règles et modèles pour la création de formulaires
- `name` [Nom et prénom](modeles/blocs/name/index.md) : Bloc de saisie du nom et des prénoms
- `nationality` [Bloc fonctionnel de nationalité](modeles/blocs/nationality/exemples.md)
- `tel` [Numéro de téléphone](modeles/blocs/tel/index.md) : Champ de saisie de numéro de téléphone avec validation
