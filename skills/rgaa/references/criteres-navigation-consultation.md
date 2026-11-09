# RGAA — Thèmes 12–13 : Navigation, Consultation

## Thème 12 — Navigation (11 critères)

### 12.1 Deux systèmes de navigation minimum

**Texte officiel 12.1 :** Chaque *ensemble de pages* dispose-t-il de deux *systèmes de navigation* différents, au moins (hors cas particuliers) ?

Chaque ensemble de pages doit proposer au moins deux parmi :
- Menu de navigation
- Plan du site
- Moteur de recherche

**Non-conformité type :** Site sans plan du site ni moteur de recherche, avec uniquement un menu de navigation.
**Impact :** avec un seul moyen de navigation, la personne qui ne peut pas l’utiliser (menu trop long à parcourir au clavier, au lecteur d’écran ou en fort zoom) n’a pas d’autre chemin vers les pages du site.
**Priorité :** 🟠 Majeur

---

### 12.2 Menu et barres de navigation à la même place

**Texte officiel 12.2 :** Dans chaque *ensemble de pages*, le *menu et les barres de navigation* sont-ils toujours à la même place (hors cas particuliers) ?

**Non-conformité type :** Menu en haut sur la page d’accueil, en latéral sur les pages intérieures ; ordre des entrées qui change selon les pages.
**Impact :** un menu qui change de place ou d’ordre oblige la personne qui navigue au lecteur d’écran, en fort zoom ou avec une commande vocale à le rechercher sur chaque page.
**Priorité :** 🟠 Majeur

---

### 12.3–12.5 Plan du site et moteur de recherche

**Texte officiel 12.3 :** La *page « plan du site »* est-elle pertinente ?

**Texte officiel 12.4 :** Dans chaque *ensemble de pages*, la *page « plan du site »* est-elle accessible à partir d’une fonctionnalité identique ?

**Texte officiel 12.5 :** Dans chaque *ensemble de pages*, le *moteur de recherche* est-il atteignable de manière identique ?

12.3 : la page plan du site représente l’architecture générale du site, et ses liens mènent aux pages annoncées. 12.4 : elle s’atteint par la même fonctionnalité, à la même place et dans le même ordre relatif du code sur chaque ensemble de pages. 12.5 : même exigence pour le moteur de recherche. Sans page plan du site, 12.3 et 12.4 sont NA, et l’absence pèse sur 12.1. Sans moteur de recherche, 12.5 est NA. Un lien vers le plan du site absent d’une seule page relève de 12.4, pas de 12.3. Un champ qui filtre une liste n’est pas le moteur de recherche du site.

Les trois critères sont en jugement humain : NT, jamais C. L’absence de lien dans un gabarit ne prouve pas l’absence de plan du site sur le site : le NA ne vaut que si l’absence est connue (déclaration d’accessibilité, plan d’action).

**Non-conformité type :** Plan du site incomplet ou avec des liens cassés ; lien « Plan du site » dans le pied de page d’une page, dans l’en-tête d’une autre ; moteur de recherche absent de l’en-tête de certaines pages.
**Impact :** un plan du site incomplet, ou un accès qui change de place, prive de sa vue d’ensemble du site la personne qui ne peut pas parcourir les menus (au lecteur d’écran, en fort zoom).
**Priorité :** 🟡 Mineur

---

### 12.6 Zones de regroupement atteignables ou évitables

**Texte officiel 12.6 :** Les zones de regroupement de contenus présentes dans plusieurs pages web (zones d’*en-tête*, de *navigation principale*, de *contenu principal*, de *pied de page* et de *moteur de recherche*) peuvent-elles être atteintes ou évitées ?
- **12.6.1** Dans chaque page web où elles sont présentes, la zone d’*en-tête*, de *navigation principale*, de *contenu principal*, de *pied de page* et de *moteur de recherche* respectent-elles au moins une de ces conditions ?
  - La zone possède un rôle WAI-ARIA de type *landmark* correspondant à sa nature ;
  - La zone possède un titre dont le contenu permet de comprendre la nature du contenu de la zone ;
  - La zone peut être masquée par le biais d’un bouton précédent directement la zone dans l’ordre du code source ;
  - La zone peut être évitée par le biais d’un *lien d’évitement* précédent directement la zone dans l’ordre du code source ;
  - La zone peut être atteinte par le biais d’un *lien d’accès rapide* visible ou, à défaut, visible à la prise de focus.

**Non-conformité type :** En-tête, contenu principal et pied de page dans des `<div>`, sans landmark, sans titre et sans lien d’évitement ou d’accès rapide.
**Impact :** impossible d’aller directement au contenu principal ou à la navigation : la personne qui utilise un lecteur d’écran parcourt toute la page pour les trouver.
**Priorité :** 🟠 Majeur

---

### 12.7 Lien d’évitement ou d’accès rapide au contenu principal

**Texte officiel 12.7 :** Dans chaque page web, un *lien d’évitement ou d’accès rapide* à la *zone de contenu principal* est-il présent (hors cas particuliers) ?
- **12.7.1** Dans chaque page web, un lien permet-il d’éviter la *zone de contenu principal* ou d’y accéder (hors cas particuliers) ?
- **12.7.2** Dans chaque ensemble de pages, le *lien d’évitement ou d’accès rapide* à la *zone de contenu principal* vérifie-t-il ces conditions (hors cas particuliers) ?
  - Le lien est situé à la même place dans la présentation ;
  - Le lien se présente toujours dans le même ordre relatif dans le code source ;
  - Le lien est visible ou, à défaut, visible à la prise de focus ;
  - Le lien est fonctionnel.
- *Cas particuliers :*
  - Il existe une gestion de cas particuliers lorsque le site web est constitué d’une seule page.
  - Dans ce cas de figure, l’obligation de la présence d’un lien d’accès rapide est liée au contexte de la page : présence ou absence de navigation ou de contenus additionnels, par exemple. Le critère peut être considéré comme non applicable lorsqu’il est avéré qu’un lien d’accès rapide est inutile.

**Non-conformité type :** Aucun lien d’évitement ni d’accès rapide ; lien dont la cible n’existe pas (`href="#contenu"` sans `id="contenu"`).
**Impact :** il faut traverser toute la navigation sur chaque page avant d’atteindre le contenu : la personne qui navigue au clavier répète des dizaines de tabulations à chaque page.
**Priorité :** 🔴 Bloquant

---

### 12.8 Ordre de tabulation cohérent

**Texte officiel 12.8 :** Dans chaque page web, l’*ordre de tabulation* est-il *cohérent* ?
- **12.8.1** Dans chaque page web, l’*ordre de tabulation* dans le contenu est-il *cohérent* ?
- **12.8.2** Pour chaque *script* qui met à jour ou insère un contenu, l’*ordre de tabulation* reste-t-il *cohérent* ?

**Non-conformité type :** `tabindex="5"` qui fait passer un élément avant ceux qui le précèdent ; contenu inséré en fin de page, loin de son déclencheur, sans déplacement du focus ; modale ouverte dont le focus part vers la page située derrière (défaut aussi rattaché à 7.1 dans `impacts.md`).
**Impact :** le parcours saute d’une zone à l’autre et devient incompréhensible pour la personne qui navigue au clavier.
**Priorité :** 🟠 Majeur

---

### 12.9 Pas de piège au clavier

**Texte officiel 12.9 :** Dans chaque page web, la navigation ne doit pas contenir de piège au clavier. Cette règle est-elle respectée ?
- **12.9.1** Dans chaque page web, chaque *élément recevant le focus* vérifie-t-il une de ces conditions ?
  - Il est possible d’atteindre l’élément suivant ou précédent pouvant recevoir le focus avec la touche de tabulation ;
  - L’utilisateur est informé d’un mécanisme fonctionnel permettant d’atteindre au clavier l’élément suivant ou précédent pouvant recevoir le focus.

**Non-conformité type :** Liste déroulante personnalisée dont l’écouteur `keydown` annule Tab (`preventDefault`) quand elle est ouverte, sans la fermer ni rendre le focus ; widget tiers (éditeur riche, `<iframe>`) dont on ne sort pas au clavier, sans consigne.
**Impact :** impossible de sortir du composant : pour la personne qui navigue au clavier ou au contacteur, la suite de la page est hors d’atteinte.
**Priorité :** 🔴 Bloquant

---

### 12.10 Raccourcis clavier à une seule touche contrôlables

**Texte officiel 12.10 :** Dans chaque page web, les *raccourcis clavier* n’utilisant qu’une seule touche (lettre minuscule ou majuscule, ponctuation, chiffre ou symbole) sont-ils contrôlables par l’utilisateur ?
- **12.10.1** Dans chaque page web, chaque *raccourci clavier* n’utilisant qu’une seule touche (lettre minuscule ou majuscule, ponctuation, chiffre ou symbole) vérifie-t-il l’une de ces conditions ?
  - Un mécanisme est disponible pour désactiver le *raccourci clavier* ;
  - Un mécanisme est disponible pour configurer la touche de *raccourci clavier* au moyen des touches de modification (Ctrl, Alt, Maj, etc.) ;
  - Dans le cas d’un *composant d’interface* utilisateur, le *raccourci clavier* qui lui est associé ne peut être activé que si le focus clavier est sur ce composant.

**Non-conformité type :** Application avec des raccourcis `j` / `k` écoutés sur toute la page, qui se déclenchent pendant la saisie dans un champ de recherche.
**Impact :** un raccourci d’une seule touche se déclenche quand la personne dicte un texte avec une commande vocale, ou quand elle tape une touche par erreur au clavier : l’action part sans qu’elle l’ait voulue.
**Priorité :** 🟠 Majeur

---

### 12.11 Contenus additionnels atteignables au clavier

**Texte officiel 12.11 :** Dans chaque page web, les contenus additionnels apparaissant au survol, à la prise de focus ou à l’activation d’un *composant d’interface* sont-ils si nécessaire atteignables au clavier ?
- **12.11.1** Dans chaque page web, les contenus additionnels apparaissant au survol, à la prise de focus ou à l’activation d’un *composant d’interface* sont-ils si nécessaire atteignables au clavier ?
- *Notes techniques :*
  - Ce critère adresse les situations où un contenu additionnel contient des *composants d’interface* avec lesquels il doit être possible d’interagir au clavier. Par exemple, une infobulle personnalisée qui propose un lien dans son contenu.

**Non-conformité type :** Sous-menu affiché seulement au survol (`mouseenter`, `:hover`), dont les liens ne s’atteignent pas au clavier ; liste déroulante personnalisée ouverte au clic, dont les options (`<li>` ou `<div>` sans `tabindex`, sans gestion des flèches) ne s’atteignent pas au clavier.
**Impact :** les liens ou les options d’un contenu affiché au survol ou au clic restent hors d’atteinte pour la personne qui navigue au clavier ou au contacteur.
**Priorité :** 🟠 Majeur

---

## Thème 13 — Consultation (12 critères)

### 13.1 Limites de temps contrôlables

**Texte officiel 13.1 :** Pour chaque page web, l’utilisateur a-t-il le contrôle de chaque limite de temps modifiant le contenu (hors cas particuliers) ?
- **13.1.1** Pour chaque page web, chaque *procédé de rafraîchissement* (balise `<object>`, balise `<embed>`, balise `<svg>`, balise `<canvas>`, balise `<meta>`) vérifie-t-il une de ces conditions (hors cas particuliers) ?
  - L’utilisateur peut arrêter ou relancer le rafraîchissement ;
  - L’utilisateur peut augmenter la limite de temps entre deux rafraîchissements de dix fois, au moins ;
  - L’utilisateur est averti de l’imminence du rafraîchissement et dispose de vingt secondes, au moins, pour augmenter la limite de temps avant le prochain rafraîchissement ;
  - La limite de temps entre deux rafraîchissements est de vingt heures, au moins.
- **13.1.2** Pour chaque page web, chaque procédé de *redirection* effectué via une balise `<meta>` est-il immédiat (hors cas particuliers) ?
- **13.1.3** Pour chaque page web, chaque procédé de *redirection* effectué via un *script* vérifie-t-il une de ces conditions (hors cas particuliers) ?
  - L’utilisateur peut arrêter ou relancer la redirection ;
  - L’utilisateur peut augmenter la limite de temps avant la redirection de dix fois, au moins ;
  - L’utilisateur est averti de l’imminence de la redirection et dispose de vingt secondes, au moins, pour augmenter la limite de temps avant la prochaine redirection ;
  - La limite de temps avant la redirection est de vingt heures, au moins.
- **13.1.4** Pour chaque page web, chaque procédé limitant le temps d’une session vérifie-t-il une de ces conditions (hors cas particuliers) ?
  - L’utilisateur peut supprimer la limite de temps ;
  - L’utilisateur peut augmenter la limite de temps ;
  - La limite de temps avant la fin de la session est de vingt heures au moins.
- *Cas particuliers :*
  - Il existe une gestion de cas particuliers lorsque la limite de temps est essentielle, notamment lorsqu’elle ne pourrait pas être supprimée sans changer fondamentalement le contenu ou les fonctionnalités liées au contenu.
  - Dans ces situations, le critère est non applicable. Par exemple, le rafraîchissement d’un flux RSS dans une page n’est pas une limite de temps essentielle ; le critère est applicable. En revanche, une redirection automatique qui amène vers la nouvelle version d’une page à partir d’une URL obsolète est essentielle ; le critère est non applicable.

**Non-conformité type :** Démarche en ligne qui expire après 30 minutes sans moyen de prolonger la session ; `<meta http-equiv="refresh" content="300">` qui recharge la page toutes les 5 minutes.
**Impact :** les données saisies sont perdues quand la session expire ou que la page se recharge : la personne qui lit ou saisit lentement, au lecteur d’écran, à la commande vocale ou au contacteur, n’a pas le temps de finir.
**Priorité :** 🔴 Bloquant

---

### 13.2 Pas d’ouverture de nouvelle fenêtre sans action de l’utilisateur

**Texte officiel 13.2 :** Dans chaque page web, l’ouverture d’une nouvelle fenêtre ne doit pas être déclenchée sans action de l’utilisateur. Cette règle est-elle respectée ?
- **13.2.1** Dans chaque page web, l’ouverture d’une nouvelle fenêtre ne doit pas être déclenchée sans action de l’utilisateur. Cette règle est-elle respectée ?

**Non-conformité type :** Pop-up publicitaire ou d’alerte ouverte au chargement de la page.
**Impact :** une fenêtre ouverte sans action déplace le focus et la lecture ailleurs : la personne qui utilise un lecteur d’écran, ou qui zoome et ne voit qu’une partie de l’écran, perd la page qu’elle consultait.
**Priorité :** 🟡 Mineur

**Hors critère :** un lien `target="_blank"` que la personne active n’est pas une NC au titre de 13.2, ni au titre de 6.1 tant que son intitulé reste explicite. Signaler la nouvelle fenêtre reste une bonne pratique. Si on la signale par un attribut `title`, il reprend l’intitulé visible du lien (exigence de 6.1).

---

### 13.3–13.4 Documents bureautiques accessibles

**Texte officiel 13.3 :** Dans chaque page web, chaque document bureautique en téléchargement possède-t-il, si nécessaire, une *version accessible* (hors cas particuliers) ?

**Texte officiel 13.4 :** Pour chaque document bureautique ayant une *version accessible*, cette version offre-t-elle la même information ?

13.3 : chaque document bureautique en téléchargement est accessible, ou a une version accessible (bureautique ou HTML). 13.4 : cette version donne la même information. Sans version accessible, la NC va à 13.3 (si le document en exige une) et 13.4 est NA. Une version accessible incomplète rend 13.4 NC, pas 13.3. Un fichier `.txt` n’est jamais une version accessible.

Les deux critères sont en jugement humain : NT, jamais C.

**Non-conformité type :** PDF scanné sans OCR ni balisage d’accessibilité ; DOCX sans structure de titres ; version HTML qui omet une partie du document (NC en 13.4).
**Impact :** un PDF scanné ou sans balisage ne restitue rien d’exploitable au lecteur d’écran ni à la plage braille, et ne se reformate pas à l’agrandissement.
**Priorité :** 🟠 Majeur

---

### 13.5–13.6 Contenus cryptiques avec alternative pertinente

**Texte officiel 13.5 :** Dans chaque page web, chaque contenu cryptique (art ASCII, émoticône, syntaxe cryptique) a-t-il une alternative ?
- **13.5.1** Dans chaque page web, chaque contenu cryptique (art ASCII, émoticône, syntaxe cryptique) vérifie-t-il une de ces conditions ?
  - Un attribut title est disponible ;
  - Une définition est donnée par le contexte adjacent.

**Texte officiel 13.6 :** Dans chaque page web, pour chaque contenu cryptique (art ASCII, émoticône, syntaxe cryptique) ayant une alternative, cette alternative est-elle pertinente ?

13.5 : chaque contenu cryptique (art ASCII, émoticône, syntaxe cryptique) a une alternative : un attribut `title` (sur un lien, un champ, une `<abbr>`) ou une définition dans le contexte adjacent. 13.6 : cette alternative explique le contenu. Sans alternative : NC en 13.5 et NA en 13.6. Alternative présente mais fausse : NC en 13.6.

13.6 est en jugement humain : NT, jamais C.

**Non-conformité type :** Émoticône `:-)` sans attribut `title` ni définition adjacente ; art ASCII sans description.
**Impact :** une émoticône ou un art ASCII est lu caractère par caractère au lecteur d’écran (« deux-points tiret parenthèse ») ; une syntaxe cryptique sans définition reste opaque pour la personne qui a besoin de consignes explicites.
**Priorité :** 🟡 Mineur

---

### 13.7 Pas de flash dangereux

**Texte officiel 13.7 :** Dans chaque page web, *les changements brusques de luminosité ou les effets de flash* sont-ils correctement utilisés ?
- **13.7.1** Dans chaque page web, chaque image ou élément multimédia (balise `<video>`, balise `<img>`, balise `<svg>`, balise `<canvas>`, balise `<embed>` ou balise `<object>`) qui provoque un changement brusque de luminosité ou un effet de flash vérifie-t-il une de ces conditions ?
  - La fréquence de l’effet est inférieure à 3 par seconde ;
  - La surface totale cumulée des effets est inférieure ou égale à 21824 pixels.
- **13.7.2** Dans chaque page web, chaque script qui provoque *un changement brusque de luminosité ou un effet de flash* vérifie-t-il une de ces conditions ?
  - La fréquence de l’effet est inférieure à 3 par seconde ;
  - La surface totale cumulée des effets est inférieure ou égale à 21824 pixels.
- **13.7.3** Dans chaque page web, chaque mise en forme CSS qui provoque *un changement brusque de luminosité ou un effet de flash* vérifie-t-il une de ces conditions ?
  - La fréquence de l’effet est inférieure à 3 par seconde ;
  - La surface totale cumulée des effets est inférieure ou égale à 21824 pixels.

**Non-conformité type :** Fond d’alerte de 400 × 300 px qui clignote 3 fois par seconde ou plus ; effet stroboscopique dans une vidéo.
**Impact :** risque de crise d’épilepsie pour la personne photosensible.
**Priorité :** 🔴 Bloquant

---

### 13.8 Contenus en mouvement contrôlables

**Texte officiel 13.8 :** Dans chaque page web, chaque contenu en mouvement ou clignotant est-il *contrôlable* par l’utilisateur ?
- **13.8.1** Dans chaque page web, chaque contenu en mouvement déclenché automatiquement, vérifie-t-il une de ces conditions ?
  - La durée du mouvement est inférieure ou égale à 5 secondes ;
  - L’utilisateur peut arrêter et relancer le mouvement ;
  - L’utilisateur peut afficher et masquer le contenu en mouvement ;
  - L’utilisateur peut afficher la totalité de l’information sans le mouvement.
- **13.8.2** Dans chaque page web, chaque contenu clignotant déclenché automatiquement, vérifie-t-il une de ces conditions ?
  - La durée du clignotement est inférieure ou égale à 5 secondes ;
  - L’utilisateur peut arrêter et relancer le clignotement ;
  - L’utilisateur peut afficher et masquer le contenu clignotant ;
  - L’utilisateur peut afficher la totalité de l’information sans le clignotement.

**Non-conformité type :** Carrousel à défilement automatique sans bouton pause ; carrousel qui ne s’arrête qu’au survol ou au focus.
**Impact :** un contenu qui bouge sans pouvoir l’arrêter provoque nausées et vertiges, et empêche de se concentrer sur la lecture ; la personne qui lit lentement ou au lecteur d’écran voit le contenu changer avant la fin de sa lecture.
**Priorité :** 🟠 Majeur

---

### 13.9 Contenu consultable en portrait et en paysage

**Texte officiel 13.9 :** Dans chaque page web, le contenu proposé est-il consultable quelle que soit l’orientation de l’écran (portrait ou paysage) (hors cas particuliers) ?
- **13.9.1** Dans chaque page web, chaque contenu vérifie-t-il ces conditions (hors cas particuliers) ?
  - La consultation est possible quel que soit le mode d’orientation de l’écran ;
  - Le contenu proposé reste le même quel que soit le mode d’orientation de l’écran utilisé même si sa présentation et le moyen d’y accéder peut différer.
- *Cas particuliers :*
  - Il existe des interfaces pour lesquelles l’orientation du périphérique est essentielle à leur utilisation.
  - Dans ces situations, le critère est non applicable. Il peut s’agir d’interfaces de jeu, de piano, de dépôt de chèques bancaires, etc.
  - Si l’interface est le seul moyen d’accéder au service proposé, une alternative devrait être mise en place pour pallier cette carence.

**Non-conformité type :** Application bloquée en portrait, avec le message « Veuillez tourner votre appareil », sans justification fonctionnelle.
**Impact :** l’écran fixé sur un support, par exemple sur un fauteuil roulant, ne peut pas pivoter : un contenu bloqué dans une orientation reste inaccessible à la personne qui l’utilise.
**Priorité :** 🟠 Majeur

---

### 13.10 Gestes complexes doublés par un geste simple

**Texte officiel 13.10 :** Dans chaque page web, les fonctionnalités utilisables ou disponibles au moyen d’un *geste complexe* peuvent-elles être également disponibles au moyen d’un *geste simple* (hors cas particuliers) ?
- **13.10.1** Dans chaque page web, chaque fonctionnalité utilisable ou disponible suite à un contact multipoint est-elle également utilisable ou disponible suite à un contact en un point unique de l’écran (hors cas particuliers).
- **13.10.2** Dans chaque page web, chaque fonctionnalité utilisable ou disponible suite à un geste basé sur le suivi d’une trajectoire sur l’écran est-elle également utilisable ou disponible suite à un contact en un point unique de l’écran (hors cas particuliers).
- *Cas particuliers :*
  - Il existe une gestion de cas particuliers dans deux types de situation :
    - - Le critère ne s’applique qu’à des fonctionnalités mises en place par l’auteur du site. Il ne concerne donc pas les gestes requis par l’agent utilisateur ou le système d’exploitation ;
    - - Le critère ne s’applique pas aux fonctionnalités dont la réalisation d’un geste complexe est essentielle (exécuter le tracé d’une signature, par exemple).

**Non-conformité type :** Carrousel navigable uniquement par balayage, sans boutons précédent et suivant.
**Impact :** la personne qui pointe avec un seul doigt, un stylet, une souris de tête ou une commande vocale ne peut pas balayer ni pincer : la fonctionnalité lui reste inaccessible.
**Priorité :** 🟠 Majeur

---

### 13.11 Actions au pointeur annulables

**Texte officiel 13.11 :** Dans chaque page web, les actions déclenchées au moyen d’un dispositif de pointage sur un point unique de l’écran peuvent-elles faire l’objet d’une annulation (hors cas particuliers) ?
- **13.11.1** Dans chaque page web, les actions déclenchées au moyen d’un dispositif de pointage sur un point unique de l’écran vérifient-elles l’une de ces conditions (hors cas particuliers) ?
  - L’action est déclenchée au moment où le dispositif de pointage est *relâché ou relevé* ;
  - L’action est déclenchée au moment où le dispositif de pointage est *pressé ou posé* puis annulée lorsque le dispositif de pointage est *relâché ou relevé* ;
  - Un mécanisme est disponible pour abandonner (avant achèvement de l’action) ou annuler (après achèvement) l’exécution de l’action.
- *Cas particuliers :*
  - Il existe une gestion de cas particulier lorsque la fonctionnalité nécessite que le comportement attendu soit réalisé lors d’un événement descendant, par exemple, un émulateur de clavier dont les touches doivent s’activer à la pression comme sur un clavier physique. Dans ces situations, le critère est non applicable.
- *Notes techniques :*
  - Deux exemples de mécanisme mis en place pour annuler ou abandonner une action déclenchée au moyen d’un dispositif de pointage sur un point unique de l’écran :
    - - Une fenêtre modale permettant d’annuler l’action après son achèvement ;
    - - Pour une fonction de glisser/déposer, le fait d’abandonner l’action si l’utilisateur relâche l’élément en dehors de la zone cible.

**Non-conformité type :** Bouton de suppression déclenché au `mousedown`, sans confirmation possible.
**Impact :** la personne qui a des tremblements, ou qui pointe avec un dispositif peu précis, déclenche une action en posant le pointeur au mauvais endroit, sans pouvoir l’annuler en le glissant hors du bouton.
**Priorité :** 🟠 Majeur

---

### 13.12 Fonctionnalités basées sur le mouvement de l’appareil

**Texte officiel 13.12 :** Dans chaque page web, les fonctionnalités qui impliquent un mouvement de l’appareil ou vers l’appareil peuvent-elles être satisfaites de manière alternative (hors cas particuliers) ?
- **13.12.1** Dans chaque page web, les fonctionnalités disponibles en bougeant l’appareil peuvent-elles être accomplies avec des *composants d’interface* utilisateur (hors cas particuliers) ?
- **13.12.2** Dans chaque page web, les fonctionnalités disponibles en faisant un geste en direction de l’appareil peuvent-elles être accomplies avec des *composants d’interface* utilisateur (hors cas particuliers) ?
- **13.12.3** L’utilisateur a-t-il la possibilité de désactiver la détection du mouvement pour éviter un déclenchement accidentel de la fonctionnalité (hors cas particuliers) ?
- *Cas particuliers :*
  - Il existe une gestion de cas particulier lorsque :
    - - Le mouvement est essentiel à l’accomplissement de la fonctionnalité (ex. podomètre) ;
    - - La détection du mouvement est utilisée pour contrôler une fonctionnalité au travers d’une interface compatible avec l’accessibilité.

**Non-conformité type :** Fonctionnalité « secouer pour annuler » sans bouton équivalent dans l’interface.
**Impact :** la personne dont l’appareil est fixé sur un support ne peut pas le secouer ni l’incliner ; celle qui a des mouvements involontaires déclenche la fonctionnalité sans le vouloir.
**Priorité :** 🟠 Majeur

