# Classement des critères — thèmes 1 à 3

Classement provisoire, en attente de l’avis du pôle accessibilité numérique. Proposé par Isabelle Lafont.

- **code** : le verdict (C, NC ou NA) se tranche à la lecture du code.
- **mixte** : le code prouve une NC, ou une conformité quand la ligne le prévoit (critères « si nécessaire », contrastes entièrement déterminés dans le code) ; chaque ligne dit laquelle. Sans preuve dans le code, NT.
- **conditions réelles** : une vérification posée en phase 2 suffit ; sans réponse, NT.
- **jugement humain** : toujours NT, jamais C ; NA si le critère est sans objet.

## Thème 1 — Images

- **1.1** Alternative textuelle des images porteuses d’information — code
- **1.2** Images de décoration ignorées par les aides techniques — mixte. Le code prouve : NC sur une image sans `alt`, un `<svg>` sans `aria-hidden="true"`. Reste : voir l’image pour confirmer qu’elle est décorative ; une image à `alt=""` qui porte une information est NC en 1.1.
- **1.3** Alternative textuelle pertinente — mixte. Le code prouve : NC sur une alternative générique (« image », « photo », nom de fichier) ou qui redit le texte voisin. Reste : juger, image sous les yeux, que l’alternative transmet l’information.
- **1.4** CAPTCHA : alternative qui en identifie la nature et la fonction — mixte. Le code prouve : NC sur un CAPTCHA sans alternative ou dont l’alternative donne la réponse. Reste : un CAPTCHA tiers est injecté par script, son alternative ne se lit pas dans le code audité.
- **1.5** CAPTCHA : autre solution d’accès — conditions réelles (question « CAPTCHA »). Reste : vérifier dans le navigateur qu’une forme non graphique (audio, question) est proposée.
- **1.6** Description détaillée si nécessaire — mixte. Le code prouve : C quand une description est reliée (`aria-describedby`, lien ou texte adjacent). Reste : sans description, voir l’image pour dire si elle en exige une (graphique, schéma, carte).
- **1.7** Description détaillée pertinente — jugement humain. Reste : comparer la description au contenu de l’image (valeurs, tendances, légende).
- **1.8** Images texte remplacées par du texte stylé — jugement humain. Reste : voir l’image pour savoir si elle contient du texte ; le nom de fichier ou l’`alt` n’en sont qu’un indice.
- **1.9** Légende d’image correctement reliée — code

## Thème 2 — Cadres

- **2.1** Titre de cadre — code
- **2.2** Titre de cadre pertinent — mixte. Le code prouve : NC sur un titre générique ou technique (« iframe », « cadre1 », nom de fichier). Reste : juger, contenu du cadre sous les yeux, que le titre en dit la nature.

## Thème 3 — Couleurs

- **3.1** Information pas donnée uniquement par la couleur — mixte. Le code prouve : NC quand un état (erreur, champ obligatoire, élément actif) ne se distingue que par une classe de couleur ou une propriété de couleur (`color`, `background-color`, `border-color`), sans texte, icône ni attribut qui le porte. Des indices visuels cumulés (couleur et graisse, couleur et bordure) sans texte, icône ni attribut (`aria-current`, `aria-invalid`…) qui les restitue restent une NC, ici et en 10.9. Reste : voir le rendu pour repérer une information portée par la seule couleur (graphique, légende, lien dans un texte).
- **3.2** Contraste entre le texte et son arrière-plan — mixte (question « Contrastes »). Le code prouve : C ou NC quand la couleur du texte et celle de son fond sont toutes deux déterminées dans le code audité (valeurs écrites en dur ou variables résolues dans ce code), sans transparence ni image ou dégradé de fond : C si le rapport atteint 4,5:1 (3:1 pour le texte de grande taille), NC sinon. Reste : mesurer le contraste rendu quand le fond est hérité hors du code audité, ou que les couleurs viennent de variables non résolues, d’un thème, d’une transparence ou d’une image de fond.
- **3.3** Contraste des composants d’interface et des éléments graphiques — mixte (question « Contrastes »). Le code prouve : C ou NC quand la couleur d’une bordure de champ, d’une icône ou d’un tracé porteur d’information et celle de son fond sont toutes deux déterminées dans le code audité, sans transparence : C si le rapport atteint 3:1, NC sinon. Reste : mesurer le contraste rendu des composants et de leurs états (focus, survol, sélection).
