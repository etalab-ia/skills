# Classement des critères — thèmes 12 et 13

Classement provisoire, en attente de l’avis du pôle accessibilité numérique. Proposé par Isabelle Lafont.

- **code** : le verdict (C, NC ou NA) se tranche à la lecture du code.
- **mixte** : le code prouve une NC, ou une conformité quand la ligne le prévoit (critères « si nécessaire », contrastes entièrement déterminés dans le code) ; chaque ligne dit laquelle. Sans preuve dans le code, NT.
- **conditions réelles** : une vérification posée en phase 2 suffit ; sans réponse, NT.
- **jugement humain** : toujours NT, jamais C ; NA si le critère est sans objet.

## Thème 12 — Navigation

En mode composant, ces critères ne sont pas évalués : ni verdict ni question de phase 2. Le piège au clavier d’un composant se vérifie au 7.3.

- **12.1** Deux systèmes de navigation différents — jugement humain. Reste : vérifier sur l’ensemble de pages la présence de deux systèmes parmi le menu, le plan du site et le moteur de recherche.
- **12.2** Menu et barres de navigation toujours à la même place — jugement humain. Reste : comparer plusieurs pages de l’ensemble (place à l’écran, ordre dans le code).
- **12.3** Page « plan du site » pertinente — jugement humain. Reste : parcourir le plan du site pour vérifier qu’il représente l’architecture du site et que ses liens mènent aux pages annoncées.
- **12.4** Plan du site accessible par une fonctionnalité identique — jugement humain. Reste : comparer plusieurs pages de l’ensemble (même lien, même place, même ordre dans le code).
- **12.5** Moteur de recherche atteignable de manière identique — jugement humain. Reste : comparer plusieurs pages de l’ensemble (même fonctionnalité, même place, même ordre dans le code).
- **12.6** Zones de regroupement atteignables ou évitables — code
- **12.7** Lien d’évitement ou d’accès rapide au contenu principal — mixte. Le code prouve : NC sans lien vers le contenu principal, ou sur un lien dont la cible n’existe pas (`href="#contenu"` sans `id="contenu"`). Reste : vérifier au clavier que le lien est visible au focus et fonctionne, et qu’il garde la même place sur l’ensemble de pages.
- **12.8** Ordre de tabulation cohérent — mixte (question « Clavier »). Le code prouve : NC sur un `tabindex` positif, ou sur un contenu inséré par script loin de son déclencheur dans l’ordre du code. Reste : parcourir la page à la touche Tab et comparer l’ordre du focus à l’ordre de lecture.
- **12.9** Pas de piège au clavier — conditions réelles (question « Clavier »). Reste : vérifier qu’on atteint l’élément suivant et précédent depuis chaque élément focalisable (Tab, Maj+Tab, Échap).
- **12.10** Raccourcis clavier à une seule touche contrôlables — mixte. Le code prouve : NC sur un écouteur clavier qui déclenche une action sur une touche seule, sans modificateur, sans moyen de le désactiver ou de le reconfigurer, et actif hors du focus du composant. Reste : vérifier les raccourcis ajoutés par des bibliothèques hors du code audité.
- **12.11** Contenus additionnels atteignables au clavier — mixte (question « Clavier »). Le code prouve : NC sur un sous-menu ou un panneau affiché seulement au survol (`mouseenter`, `:hover`) dont le contenu interactif n’est pas atteignable au clavier. Reste : vérifier au clavier que chaque contenu additionnel s’affiche et s’atteint.

## Thème 13 — Consultation

- **13.1** Contrôle des limites de temps — mixte. Le code prouve : NC sur un `<meta http-equiv="refresh">` à délai non nul, ou sur un script qui recharge ou redirige après un délai sans moyen de l’arrêter ou de le prolonger. Reste : vérifier la durée de session côté serveur (moins de vingt heures sans moyen de la prolonger ou de la supprimer).
- **13.2** Nouvelle fenêtre pas ouverte sans action de l’utilisateur — code
- **13.3** Version accessible des documents bureautiques si nécessaire — jugement humain. Reste : ouvrir chaque document en téléchargement, ou sa version alternative, pour vérifier qu’il est accessible.
- **13.4** Version accessible qui offre la même information — jugement humain. Reste : comparer le document et sa version accessible.
- **13.5** Alternative aux contenus cryptiques — mixte. Le code prouve : NC sur une émoticône, un art ASCII ou une syntaxe cryptique sans attribut `title` ni définition adjacente. Reste : juger, contenu sous les yeux, ce qui est cryptique pour la personne qui le lit.
- **13.6** Alternative aux contenus cryptiques pertinente — jugement humain. Reste : juger que l’alternative explique le contenu cryptique.
- **13.7** Changements brusques de luminosité et effets de flash — mixte. Le code prouve : NC sur une animation CSS ou un script qui alterne fond clair et fond sombre plus de 3 fois par seconde. Reste : observer au rendu les vidéos, images animées et animations (fréquence, surface de l’effet).
- **13.8** Contenu en mouvement ou clignotant contrôlable — mixte. Le code prouve : NC sur un carrousel à défilement automatique, un `<marquee>` ou une animation infinie sans bouton pour l’arrêter ou le masquer. Reste : observer la page au chargement pour repérer les mouvements de plus de 5 secondes lancés par un script ou une image animée.
- **13.9** Contenu consultable quelle que soit l’orientation de l’écran — conditions réelles (question « Orientation »). Reste : consulter le contenu en portrait puis en paysage et vérifier qu’il reste complet.
- **13.10** Gestes complexes doublés d’un geste simple — mixte. Le code prouve : NC sur une fonctionnalité accessible seulement par un geste multipoint ou de trajectoire (glisser, pincer, balayer) sans bouton équivalent. Reste : vérifier sur un écran tactile les gestes gérés par des bibliothèques hors du code audité.
- **13.11** Actions au pointeur sur un point unique annulables — mixte. Le code prouve : NC sur une action déclenchée à l’appui (`mousedown`, `pointerdown`, `touchstart`) sans annulation au relâchement ni moyen d’annuler. Reste : vérifier au pointeur les actions gérées par des bibliothèques (glisser-déposer) et leur annulation.
- **13.12** Fonctionnalités par mouvement de l’appareil réalisables autrement — mixte. Le code prouve : NC sur un écouteur `devicemotion` ou `deviceorientation` qui déclenche une fonctionnalité sans composant d’interface équivalent ni moyen de désactiver la détection. Reste : vérifier sur un appareil mobile les détections de mouvement ajoutées par des bibliothèques.
