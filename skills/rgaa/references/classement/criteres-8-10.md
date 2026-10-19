# Classement des critères — thèmes 8 à 10

Classement provisoire, en attente de l’avis du pôle accessibilité numérique. Proposé par Isabelle Lafont.

- **code** : le verdict (C, NC ou NA) se tranche à la lecture du code.
- **mixte** : le code prouve une NC, ou une conformité quand la ligne le prévoit (critères « si nécessaire », contrastes entièrement déterminés dans le code) ; chaque ligne dit laquelle. Sans preuve dans le code, NT.
- **conditions réelles** : une vérification posée en phase 2 suffit ; sans réponse, NT.
- **jugement humain** : toujours NT, jamais C ; NA si le critère est sans objet.

## Thème 8 — Éléments obligatoires

En mode composant, ces critères ne sont pas évalués : ni verdict ni question de phase 2.

- **8.1** Type de document — code
- **8.2** Code source généré valide — mixte. Le code prouve : NC sur un `id` en double, une imbrication interdite (`<div>` dans un `<p>`, élément interactif dans un `<a>` ou un `<button>`), une balise mal fermée ou un attribut doublé. Reste : passer le code source généré de la page au validateur HTML.
- **8.3** Langue par défaut — code
- **8.4** Code de langue par défaut pertinent — code
- **8.5** Titre de page — code
- **8.6** Titre de page pertinent — mixte (question « Titre de la page »). Le code prouve : NC sur un titre vide, générique (« Page », « Sans titre ») ou réduit au nom du site. Reste : juger que le titre identifie la page et son contexte, et qu’il change d’une page à l’autre.
- **8.7** Changement de langue indiqué — mixte. Le code prouve : NC sur un passage écrit dans le code en une autre langue que celle de la page, sans attribut `lang`. Reste : repérer les passages en langue étrangère du contenu dynamique ou traduit, qui ne se lisent pas dans le gabarit.
- **8.8** Code de langue des changements valide et pertinent — code
- **8.9** Balises pas utilisées uniquement à des fins de présentation — code
- **8.10** Changements du sens de lecture signalés — mixte. Le code prouve : NC sur un texte écrit de droite à gauche sans attribut `dir`, ou un `dir` de valeur autre que `rtl` ou `ltr`. Reste : repérer les textes de droite à gauche du contenu dynamique ou traduit.

## Thème 9 — Structuration de l’information

- **9.1** Information structurée par des titres — mixte. Le code prouve : NC sur un saut de niveau, un titre vide, ou un passage stylé comme un titre sans balise `<hx>` ni `role="heading"`. Reste : juger, page sous les yeux, que chaque titre décrit sa section et que chaque titre visuel est balisé.
- **9.2** Structure du document cohérente — code
- **9.3** Listes correctement structurées — mixte. Le code prouve : NC sur une suite présentée comme liste sans `<ul>`, `<ol>`, `<dl>` ni rôles `list` et `listitem` (puces ou tirets en texte, `<br>` successifs), ou un `<ul>` dont les enfants ne sont pas des `<li>`. Reste : voir le rendu pour repérer les contenus présentés visuellement comme une liste.
- **9.4** Citations correctement indiquées — mixte. Le code prouve : NC sur une citation écrite dans le code sans `<q>` ou `<blockquote>`, ou un `<blockquote>` utilisé pour un retrait. Reste : repérer les citations du contenu dynamique ou rédactionnel.

## Thème 10 — Présentation de l’information

- **10.1** Feuilles de styles pour contrôler la présentation — code
- **10.2** Contenu visible porteur d’information présent sans feuille de style — mixte (question « Sans feuille de style »). Le code prouve : NC sur une information donnée seulement par CSS (texte dans `content` d’un pseudo-élément, icône porteuse d’information en image de fond sans texte). Reste : désactiver les styles et vérifier que toute l’information visible reste présente.
- **10.3** Information compréhensible sans feuille de style — conditions réelles (question « Sans feuille de style »). Reste : désactiver les styles et vérifier que l’ordre de lecture reste compréhensible (contenus repositionnés par grille, `order` ou positionnement).
- **10.4** Texte lisible à 200 % — conditions réelles (question « Zoom et reflow »). Reste : agrandir le texte à 200 % et vérifier qu’aucun texte n’est coupé, masqué ou superposé.
- **10.5** Couleurs de fond et de police déclarées ensemble — mixte. Le code prouve : NC sur une déclaration `color` sans couleur de fond, ou l’inverse, ni couleur héritée d’un parent dans les styles audités. Reste : vérifier les couleurs héritées des feuilles de style non auditées (système de design, thème).
- **10.6** Lien visible par rapport au texte environnant — mixte (question « Contrastes »). Le code prouve : NC sur un lien dans un texte dont le soulignement est retiré sans autre indication que la couleur au survol et au focus. Reste : mesurer le contraste du lien avec le texte environnant (3:1) et vérifier son indication au survol et au focus.
- **10.7** Prise de focus visible — mixte (question « Focus visible »). Le code prouve : NC sur `outline: none` ou `outline: 0` sans style de focus de remplacement. Reste : parcourir la page au clavier et vérifier que le focus se voit sur chaque élément.
- **10.8** Contenus cachés destinés à être ignorés — mixte. Le code prouve : NC sur `aria-hidden="true"` posé sur un élément focalisable ou sur un contenu porteur d’information qu’aucune action ne rend restituable, ou sur un `aria-hidden` incohérent avec l’état affiché. Reste : vérifier, après chaque interaction, que l’état affiché et la restitution restent cohérents.
- **10.9** Information pas donnée uniquement par la forme, la taille ou la position — mixte. Le code prouve : NC sur une consigne qui renvoie à une forme ou une position seule (« le bouton rond », « ci-contre à droite »), ou sur un état (élément actif, sélection, erreur) signalé seulement par une bordure, une graisse ou une taille, sans texte, icône ni attribut qui le restitue ; des indices visuels cumulés non restitués restent une NC. Reste : voir le rendu pour repérer une information portée par la seule forme, taille ou position.
- **10.10** Information par la forme, la taille ou la position implémentée de façon pertinente — jugement humain. Reste : juger que le moyen qui double la forme, la taille ou la position (texte, attribut) transmet la même information. NT quand 10.9 est NC faute de tout moyen de doublage : la NC est portée par 10.9.
- **10.11** Contenus sans perte ni défilement à 320 px de large ou 256 px de haut — conditions réelles (question « Zoom et reflow »). Reste : afficher la page dans une fenêtre de 320 px de large et vérifier l’absence de défilement horizontal et de perte d’information ou de fonctionnalité.
- **10.12** Espacement du texte redéfinissable sans perte — conditions réelles (question « Zoom et reflow »). Reste : appliquer les espacements du critère (interlignage 1,5, paragraphes 2, lettres 0,12, mots 0,16) et vérifier qu’aucun texte n’est coupé.
- **10.13** Contenus additionnels au focus ou au survol contrôlables — mixte (question « Clavier »). Le code prouve : NC sur une infobulle ou un menu affiché au survol ou au focus sans moyen de le masquer sans déplacer le pointeur ou le focus (pas de gestion d’Échap). Reste : vérifier au clavier (Échap) et au pointeur (survol du contenu affiché) que le contenu reste visible et se masque à la demande.
- **10.14** Contenus additionnels en CSS visibles au clavier et au pointeur — mixte (question « Clavier »). Le code prouve : NC sur un contenu affiché par `:hover` sans équivalent `:focus` ou `:focus-within`. Reste : vérifier au clavier et au pointeur que chaque contenu additionnel peut s’afficher.
