# Glossaire officiel du RGAA 4.1.2

Généré par `scripts/officiel.py` depuis `sources/glossaire.json` : ne pas modifier à la main.
Chercher le terme en italique d’un texte officiel parmi les titres `###` ci-dessous.

### Accessible et activable par le clavier et tout dispositif de pointage

- Un composant d’interface (lien, bouton…) est accessible au clavier et par tout dispositif de pointage lorsque l’utilisateur peut prendre, indifféremment, le focus par un pointeur ou la touche tabulation ;
- Un composant d’interface (lien, bouton…) est activable au clavier et par tout dispositif de pointage lorsque l’utilisateur peut enclencher, indifféremment, l’action prévue par le composant d’interface par une pression du pointeur ou la touche entrée du clavier ;
- Attention : pour certains composants d’interface comme les `sliders` (bouton coulissant ou rotatif…), il n’est pas possible de contrôler le composant par la seule touche d’entrée. Dans ces situations, d’autres touches (comme les touches de direction) peuvent être utilisées. En particulier pour les éléments ayant un rôle WAI-ARIA correspondant à un motif de conception il est recommandé de considérer le document WAI-ARIA 1.1 Authoring Practices lors de leur implémentation.
Dans le référentiel, l’expression « contrôlable par le clavier et tout dispositif de pointage » se rapporte également à la présente définition.
Note importante : le recours à certaines technologies peut rendre la gestion du focus trop complexe ou trop instable pour ne reposer que sur la tabulation, les touches de direction et la touche entrée. Dans ce cas, la mise à disposition de raccourcis clavier peut être la seule solution pour rendre le composant utilisable.
Le critère ne peut être considéré comme conforme qu’à la condition que les raccourcis clavier utilisés soient correctement documentés, qu’ils soient fonctionnels et qu’ils respectent le critère 12.10.

### Accolés (étiquette et champ accolés)

Il faut que l’étiquette et son champ soient visuellement proches de manière à ce que la relation entre les deux ne puisse pas prêter à confusion.

### Alternative (à script)

Texte ou procédé associé au script via une technique appropriée et permettant de mettre à disposition une fonction ou un contenu similaire à celui proposé par script.
Note : lorsqu’une alternative à un procédé ou une fonctionnalité JavaScript est proposée, le moyen d’y accéder doit être fourni par le site lui-même. Il peut s’agir d’un lien ou d’un bouton permettant d’accéder à une page alternative fonctionnant sans JavaScript ou permettant de remplacer le(s) composant(s) par un composant alternatif fonctionnant sans JavaScript par exemple.

### Alternative courte et concise

Les conditions de restitution d’une alternative textuelle via des technologies d’assistance (par exemple une loupe d’écran) nécessitent qu’elle soit la plus courte possible. Une longueur maximale de 80 caractères est fortement recommandée ; elle limitera le nombre de manipulations nécessaires pour lire l’alternative par les utilisateurs de plages braille ou de loupes d’écran notamment.

### Alternative textuelle (image)

« Nom accessible » restitué par les technologies d’assistance pour les éléments graphiques de type :
- Image (balise `<img>` ou balise ouvrante possédant un attribut WAI-ARIA `role="img"`) ;
- Zone d’image réactive (balise `<area>`) ;
- Bouton de type image (balise `<input>` avec l’attribut `type="image"`) ;
- Image objet (balise `<object type="image/…">`) ;
- Image vectorielle (balise `<svg>`) ;
- Image bitmap (balise `<canvas>`) ;
- Image embarquée (balise `<embed>`).
Dans le cas d’un élément graphique, le « nom accessible » est obtenu selon l’ordre suivant :
- Passage de texte associé via l’attribut WAI-ARIA `aria-labelledby` pour les balises :
- `<img>` ;
- `<input type="image">` ;
- `<svg>` ;
- `<object type="image/…">` ;
- `<embed type="image/…">` ;
- `<canvas>` ;
- balises possédant un attribut WAI-ARIA `role="img"`.
- Sinon, contenu de l’attribut WAI-ARIA `aria-label` pour les éléments :
- `<img>` ;
- `<area>` ;
- `<input type="image">` ;
- `<svg>` ;
- `<object type="image/…">` ;
- `<embed type="image/…">` ;
- `<canvas>` ;
- balises ouvrantes possédant un attribut WAI-ARIA `role="img"`.
- Sinon, contenu de l’attribut `alt` pour les balises :
- `<img>` ;
- `<area>` ;
- `<input type="image">`.
- Sinon, contenu de l’attribut `title` pour les balises :
- `<img>` ;
- `<input type="image">` ;
- `<object type="image/…">` ;
- `<embed type="image/…">`.
Cet ordre doit être utilisé pour déterminer ce qui constitue l’alternative textuelle.
Néanmoins, en cas de support partiel de l’algorithme de calcul du « nom accessible », c’est la valeur réellement restituée par les technologies d’assistance utilisées dans l’environnement de test (ou « base de référence ») qu’il faudra considérer comme alternative textuelle.
Par exemple :
- En cas de présence conjointe d’un attribut WAI-ARIA `aria-label` et d’un attribut WAI-ARIA `aria-labelledby` sur une balise `<img>`, c’est le passage de texte référencé par l’attribut WAI-ARIA `aria-labelledby` qui doit être considérée comme alternative textuelle si le contenu du passage de texte est réellement restitué par les technologies d’assistance utilisées dans l’environnement de test ;
- En cas de présence conjointe d’un attribut WAI-ARIA `aria-label` et d’un attribut `alt` sur une balise `<img>`, c’est le contenu de l’attribut WAI-ARIA `aria-label` qui doit être considéré comme alternative textuelle si le contenu de l’attribut WAI-ARIA `aria-label` est réellement restitué par les technologies d’assistance utilisées dans l’environnement de test.
Référence : Accessible name and description calculation.
RGAA considère trois types d’alternatives textuelles liées à la nature de l’image :
- Pour une image porteuse d’information, l’alternative textuelle apporte l’information nécessaire à la compréhension du contenu qu’elle véhicule ;
- Pour une image de décoration, aucune alternative textuelle ne doit être restituée ;
- Pour une image CAPTCHA ou une image-test, l’alternative textuelle décrit seulement la nature et la fonction de l’image. En effet, l’alternative textuelle ne peut apporter l’information véhiculée par l’image sans rendre la fonction associée inopérante.
Note 1 : pour une image CAPTCHA l’alternative peut être, par exemple : « Code de sécurité anti-spam » ou « code pour vérifier que vous êtes un humain » ou toute autre alternative permettant à l’utilisateur de comprendre la nature et la fonction de l’image.
Note 2 : pour un groupe d’images, par exemple un système de vote constitué de plusieurs images d’étoile, il est fortement conseillé d’utiliser soit la première image du groupe pour donner une alternative cohérente au groupe d’image (voir la technique WCAG2.1 G196), soit une balise conteneur pourvue d’un rôle WAI-ARIA `img` et d’une alternative textuelle. Dans le premier cas, les autres images du groupe sont considérées comme des images de décoration. Dans le second cas, toutes les images du groupe sont considérées comme des images de décoration.
Note 3 : pour les image-lien, l’alternative doit permettre de comprendre la fonction et la destination du lien ; ce cas est traité dans la thématique liens.
Note 4 : pour les images vectorielles (balise `<svg>`) l’alternative textuelle pourrait se trouver aussi présente dans une balise `<title>` ou dans une balise `<text>` que cette dernière balise soit ou non visible, même si ce n’est pas le rôle dévolu à cet élément en SVG.
Note 5 : l’utilisation de l’attribut `alt` étant la seule technique totalement supportée par les aides techniques il est recommandé de privilégier cette solution lors de la mise en œuvre d’une alternative à une balise `<img>`, `<area>` et `<input type="image">`.
Note 6 : bien que l’attribut `title` soit considéré comme une possibilité d’alternative textuelle à une image, son usage peut poser problème, notamment du fait qu’une image avec un attribut `alt` absent ou vide est considérée comme une image pourvue d’un `role=“présentation”` par WAI-ARIA : https://www.w3.org/TR/html-aam-1.0/#details-id-54. Il faut s’assurer que les assistances techniques présentes dans l’environnement de test retenu restituent correctement l’alternative proposée par l’attribut `title`.

### Ambigu pour tout le monde

L’intention ne peut être déterminée à partir du lien et de toute l’information de la page web présentée à l’utilisateur en même temps que ce lien (c’est-à-dire qu’un lecteur sans limitation fonctionnelle ne connaîtrait pas la fonction d’un lien avant de l’activer). Exemple : le mot « goyave » dans la phrase suivante utilisé comme lien : « L’une des exportations importantes est la goyave ». Ce lien pourrait conduire à une définition de la goyave, à un graphe présentant une liste des quantités de goyaves exportées ou à une photo de personnes récoltant la goyave. Jusqu’à ce que le lien soit activé, tout utilisateur est dans l’incertitude et une personne handicapée n’est donc pas désavantagée.

### Audiodescription synchronisée (média temporel)

Narration ajoutée (via un fichier son) à une piste sonore pour décrire les détails visuels importants qui ne peuvent être compris à partir de la piste sonore principale seulement. L’audiodescription doit être synchronisée avec le média temporel par un dispositif applicatif lié au lecteur lui-même ou fourni par le développement par exemple avec JavaScript.
Note 1 : l’audiodescription d’une vidéo fournit de l’information à propos des actions, des personnages, des changements de scènes, du texte apparaissant à l’écran et d’autres contenus visuels.
Note 2 : dans une audiodescription standard, la narration est ajoutée durant les pauses qui existent dans le dialogue. (Voir aussi audiodescription étendue.)
Note 3 : lorsque toute l’information de la vidéo est déjà donnée dans la piste audio, aucune audiodescription supplémentaire n’est requise.

### Bouton (formulaire)

Élément d’un formulaire qui permet d’effectuer une action prédéfinie. Par exemple, le bouton de soumission d’un formulaire permet l’envoi au serveur des informations collectées pour leur traitement. L’intitulé d’un bouton doit décrire l’action qui résulte de son activation (par exemple : « Lancer votre recherche », « Envoyer votre message »).
En HTML, il y a trois types de boutons de formulaire :
- Balise `<input>` de type `submit`, `reset` ou `button` ;
- Balise `<input>` de type `image` ;
- Balise `<button>`.
Il est également possible de restituer un bouton à l’aide du rôle WAI-ARIA `button`.
L’intitulé du bouton peut être de six types :
- Le contenu du passage de texte associé au bouton via l’attribut WAI-ARIA `aria-labelledby` lorsqu’il est présent ;
- Le contenu de l’attribut `aria-label` lorsqu’il est présent ;
- Le contenu de l’attribut `alt` d’un bouton de type `image` ;
- Le contenu de l’attribut `value` des boutons de type `submit`, `reset` ou `button` ;
- Le contenu de la balise `<button>` ;
- Le contenu de l’attribut `title` lorsqu’il est présent.
Note importante : lorsque plusieurs de ces techniques sont présentes sur un même bouton, le calcul du « nom accessible », c’est-à-dire ce qui sera restitué, obéit à un ordre strict :
- `aria-labelledby` ;
- Sinon `aria-label` ;
- Sinon `alt` pour le cas des input `image` ;
- Sinon `value` pour le cas des input `submit`, `reset` ou `button` ;
- Sinon contenu de la balise `<button>` ;
- Sinon `title`.
Cet ordre doit être utilisé pour l’évaluation de la pertinence du « nom accessible » du bouton. Par exemple, même dans le cas de la présence d’un `title` et d’un passage de texte référencé par `aria-labelledby` sur le même bouton, c’est le passage de texte référencé par `aria-labelledby` qui doit être évalué.
Référence : Accessible name and description calculation.
Par ailleurs, un « nom accessible » sera considéré comme non-pertinent s’il ne reprend pas le texte visible du bouton. Par exemple : `<button aria-label="confirmer la saisie">valider la saisie</button>` sera considéré comme non conforme au critère 11.9.

### Cadre

Cadre : élément HTML (balise `<frame>`) permettant d’afficher un contenu dans la page web dans laquelle il est implémenté.
Cadre en ligne : élément HTML (balise `<iframe>`) permettant d’afficher un contenu dans la page web dans laquelle il est implémenté.

### CAPTCHA

Un CAPTCHA est un test utilisé pour distinguer un utilisateur humain d’un ordinateur. Le test utilise souvent des images contenant du texte déformé, mélangé avec d’autres formes ou utilisant des jeux de couleur altérées, que l’utilisateur est invité à retaper. D’autres formes de CAPTCHA peuvent être basées sur des questions logiques ou des extraits sonores.

### Champ de saisie de formulaire

Objet d’un formulaire permettant à l’utilisateur :
- De saisir des données textuelles ou préformatées :
- `input type="text"` ;
- `input type="password"` ;
- `input type="search"` ;
- `input type="email"` ;
- `input type="number"` ;
- `input type="tel"` ;
- `input type="url"` ;
- `textarea`.
- De sélectionner des valeurs prédéfinies :
- `input type="checkbox"` ;
- `input type="radio"` ;
- `input type="date"` ;
- `input type="range"` ;
- `input type="color"` ;
- `input type="time"` ;
- `input type="month"` ;
- `input type="week"` ;
- `input type="datetime-local"` ;
- `select` ;
- `datalist` ;
- `optgroup` ;
- `option`.
- De télécharger des fichiers :
- `input type="file"`.
- Ou d’afficher des résultats :
- `output` ;
- `progress` ;
- `meter`.
- Les balises possédant un rôle WAI-ARIA permettant de restituer un champ de formulaire sont également couvertes par cette définition :
- `progressbar` ;
- `slider` ;
- `spinbutton` ;
- `textbox` ;
- `listbox` ;
- `searchbox` ;
- `combobox` ;
- `option` ;
- `checkbox` ;
- `radio` ;
- `switch`.
- Les objets de formulaires et rôle WAI-ARIA suivants ne sont pas considérés comme des champs de formulaires :
- `input type="submit"` ;
- `input type="reset"` ;
- `input type="hidden"` ;
- `input type="image"` ;
- `input type="button"` ;
- `button` ;
- attribut WAI-ARIA `role="button"`.

### Champs de même nature

Dans un formulaire, ensemble des champs pouvant être regroupés par la nature des informations attendues. Le regroupement vise à identifier les champs devant être traités comme un ensemble.
Quelques exemples :
- Trois champs successifs pour saisir une date (jour/mois/année) ;
- Champs successifs pour un numéro de téléphone ;
- Un bloc destiné à saisir l’identité et l’adresse de l’utilisateur, lorsque le formulaire contient plusieurs blocs de contact ;
- Un ensemble de boutons radio ou de cases à cocher qui se rapportent à une question.
Ces champs doivent être regroupés lorsque les intitulés de label ne sont pas suffisants pour informer l’utilisateur que les champs font partie d’un regroupement.

### Changement brusque de luminosité ou effet de flash

Alternance de luminance relative qui peut causer des crises chez certaines personnes si leur taille est suffisamment importante dans une gamme de fréquences spécifiques.

### Changement de contexte

Changements majeurs dans le contenu d’une page web qui, s’ils sont faits sans que l’utilisateur n’en soit conscient, peuvent désorienter l’utilisateur qui ne peut voir l’ensemble de la page en même temps. Les changements de contexte comprennent les changements :
- d’agent utilisateur ;
- d’espace de restitution ;
- de focus ;
- de contenu qui modifie la signification de la page web.
Note : Un changement de contenu n’est pas toujours un changement de contexte. Un changement dans le contenu comme le déploiement d’une arborescence, un menu dynamique ou un déplacement de tabulation ne change pas nécessairement le contexte à moins qu’il ne change aussi l’un des éléments énumérés ci-dessus (le focus, par exemple).
Par exemple, l’ouverture d’une nouvelle fenêtre, le déplacement du focus sur un composant différent, le déplacement vers une nouvelle page (y compris tout ce qui, pour l’utilisateur, aurait l’air d’un déplacement vers une autre page) ou la réorganisation significative du contenu d’une page sont autant d’illustrations d’un changement de contexte.

### Changement de langue

L’indication des changements de langue est nécessaire pour indiquer aux technologies d’assistance de modifier la restitution vocale d’un élément. Les changements de langue concernent tous les contenus, y compris les valeurs de certains attributs comme `title`.
Note : il n’est pas possible d’indiquer des changements de langue dans une valeur d’attribut elle-même, dans ce cas le changement de langue est indiqué sur l’élément qui contient l’attribut. Par exemple un lien affecté d’un `title` en anglais devra comporter un attribut `lang="en"`. Lorsque l’attribut contient plusieurs passages de texte dans des langues différentes, le critère est non applicable.

### Code de langue

Code de 2 caractères (ISO 639-1) ou 3 caractères (ISO 639-2 et suivants) permettant d’indiquer la langue d’un document ou d’un passage de texte. L’indication du code de langue est constituée de deux parties séparées par un tiret sur le modèle `lang="[code]-[option]"`.
- [code] représente un code de langue valide sur 2 ou 3 caractères ;
- [option] est une indication laissée à l’appréciation de l’auteur.
Lorsqu’un code de pays est utilisé comme option, il peut servir à indiquer une régionalisation de la langue, l’indication “en-us” indique la langue américaine, par exemple. L’indication du code de langue ne concerne que la partie [code] avant le tiret.

### Compatible avec les technologies d’assistance

Un contenu ou une fonctionnalité doit être compatible avec les technologies d’assistance des utilisateurs ainsi qu’avec les fonctions d’accessibilité des navigateurs et des autres agents utilisateurs via une API d’accessibilité.
Cela concerne, à la fois, la technologie, ses fonctionnalités et ses usages :
- La façon dont la technologie Web est utilisée doit être compatible avec les technologies d’assistance des utilisateurs. Cela signifie que la façon dont la technologie est utilisée a été testée dans une perspective d’interopérabilité avec des utilisateurs des technologies d’assistance dans la ou les langues du contenu ;
- La technologie fonctionne de façon native dans des agents utilisateurs largement distribués qui sont, eux-mêmes, compatibles avec l’accessibilité (comme HTML et CSS) ou avec un module d’extension largement distribué qui est, lui-même, compatible avec l’accessibilité.
La vérification de la compatibilité avec les technologies d’assistance nécessite de réaliser un certain nombre de tests spécifiques à la technologie utilisée, par exemple :
- Vérifier le nom, le rôle, le paramétrage et les changements d’états des composants d’interface ;
- Vérifier que la restitution d’un composant d’interface est correcte pour la ou les technologies d’assistance utilisées.

### Composant d’interface

Un composant d’interface est un élément avec lequel l’utilisateur peut interagir, par exemple un bouton, un lien, une zone de saisie. Certains composants peuvent être plus complexes comme un menu, une fenêtre de dialogue, un système d’onglets. Enfin, un composant d’interface peut être basé sur des éléments natifs de HTML ou développés de toutes pièces en JavaScript et des attributs WAI-ARIA. En particulier pour les éléments ayant des attributs WAI-ARIA correspondant à un motif de conception il est recommandé de considérer le document WAI-ARIA 1.1 Authoring Practices lors de leur implémentation.

### Compréhensible (ordre de lecture)

Un contenu compréhensible est lisible (l’ordre des éléments est logique) et cohérent (l’enchaînement de la lecture est cohérent).

### Contenu alternatif

Contenu venant se substituer à un autre apportant la même information mais pouvant être présenté de façon différente. Ce contenu peut être de forme textuelle mais également être lui-même structuré à l’aide de balises. Un contenu alternatif devra respecter l’ensemble des critères du RGAA qui lui sont applicables pour être considéré comme une alternative accessible à l’élément qu’il remplace. Exemple : un tableau de données peut être le contenu alternatif d’une image bitmap (balise `<canvas>`) affichant un graphique statistique.

### Contenu caché

Les technologies d’assistance (notamment les lecteurs d’écran) ne restituent pas le contenu masqué via les propriétés :
- `display` avec la valeur `none` (`display: none`) ;
- `visibility` avec la valeur `hidden` (`visibility: hidden`) ;
- `font-size` avec la valeur `0` (`font-size:0`) ;
- Attribut HTML5 `hidden` ;
- Attribut WAI-ARIA `aria-hidden="true"`.
Tous les contenus utilisant une ou plusieurs de ces propriétés et attributs sont applicables pour le critère 10.8.

### Contenu visible

Pour le test 12.2.1 : « Contenu présent » signifie que le contenu visible reste présent lorsque CSS est désactivé. Par exemple, une image porteuse d’information en propriété de fond CSS invalide ce test car l’information n’est plus « présente » lorsque CSS est désactivé. En revanche, une image porteuse d’information en propriété de fond CSS mais accompagnée d’un texte caché valide ce test car l’information est bien « présente » lorsque CSS est désactivé.
Note : la pratique qui consiste à gérer des images en propriété de fond d’éléments via CSS est formellement déconseillée, même si elle est accompagnée d’un texte caché.

### Contexte du lien

Le contexte du lien représente les informations supplémentaires (on parle d’informations de contexte) qui peuvent être mises en relation par un programme informatique avec l’intitulé du lien. Les informations de contexte qui permettent de compléter l’intitulé du lien sont les suivantes :
- Le contenu de la phrase dans laquelle le lien texte est présent ;
- Le contenu du paragraphe (balise `<p>`) dans lequel le lien texte est présent ;
- Le contenu de l’item de liste (balise `<li>`) ou le contenu d’un item de liste parent (balise `<li>`) dans lequel le lien texte est présent ;
- Le contenu du titre (balise `<hx>`) précédent le lien texte ;
- Le contenu de la ou les cellule(s) d’en-tête de tableau (balise(s) `<th>`) associée(s) à la cellule de donnée (balise `<td>`) dans laquelle le lien texte est présent ;
- Le contenu de la cellule de donnée (balise `<td>`) dans laquelle le lien texte est présent.
Note 1 : l’un des 6 contextes de lien combiné à l’intitulé du lien doit permettre de comprendre la fonction et la destination du lien.
Note 2 : RGAA considère qu’une adresse e-mail de type `xxx@xxx.yyy` est un texte de lien suffisant pour comprendre la fonction du lien et ne requiert pas de signaler plus explicitement l’action.

### Contraste

Opposition marquée entre la luminosité d’une couleur de premier plan et d’une couleur d’arrière-plan. Le rapport de contraste est basé sur la différence de luminance relative entre l’arrière-plan et le premier plan selon la règle : (L1 + 0,05) / (L2 + 0,05) où L1 est la luminance relative la plus claire et L2 la luminance relative la plus sombre. La luminosité est calculée selon la formule suivante : L = 0,2126 * R + 0,7152 * G + 0,0722 * B. Où R, G et B sont définis par :
- Si R sRGB ≤ 0,03928 alors R = R sRGB /12,92 sinon R = ((R sRGB +0,055)/1,055) ^ 2,4 ;
- Si G sRGB ≤ 0,03928 alors G = G sRGB /12,92 sinon G = ((G sRGB +0,055)/1,055) ^ 2,4 ;
- Si B sRGB ≤ 0,03928 alors B = B sRGB /12.92 sinon B = ((B sRGB +0,055)/1,055) ^ 2,4.
et R sRGB, G sRGB et B sRGB sont définis par :
- R sRGB = R8bit/255 ;
- G sRGB = G8bit/255 ;
- B sRGB = B8bit/255.
Le caractère « ^ » est l’opérateur de puissance.
Note : la mesure de contraste concerne le texte, le texte en image, le texte et le texte en image dans les animations, le texte de sous-titrage et le texte incrusté dans les vidéos. Pour le texte et le texte en image dans les animations, le texte de sous-titrage et le texte incrusté dans les vidéos, la taille de la police doit être mesurée par rapport à la taille d’affichage par défaut (telle qu’affichée). Les textes présents dans les éléments d’une image ou d’une vidéo (par exemple un écriteau, une affiche…) ne sont pas concernés.
Source (en anglais) : Procédure de calcul de contraste des WCAG.

### Contrôle (contenu en mouvement ou clignotant)

Possibilité pour l’utilisateur de contrôler l’affichage ou la lecture d’un contenu en mouvement ou clignotant par le clavier et la souris, au moins.
Tous les contenus en mouvement, à l’exception des médias temporels pris en charge par la thématique multimédia, sont concernés : les images animées (par exemple un gif animé), les contenus en mouvement proposés via une balise `<object>`, du code JavaScript ou des effets CSS par exemple.
Note 1 : lorsque c’est approprié, la méthode de contrôle devrait être disponible comme premier élément de la page.
Note 2 : la méthode de contrôle du contenu en mouvement ou clignotant doit permettre à l’utilisateur d’interagir avec le reste de la page. En conséquence, l’arrêt ou la mise en pause via un événement déclenché uniquement sur la prise de focus ne permet pas de valider le critère.
Note 3 : Dans certains cas, le mouvement fait partie intégrante du composant et il n’est pas possible d’en donner le contrôle à l’utilisateur, par exemple une barre de progression dont la fonction est d’indiquer par un mouvement la progression d’un évènement comme un téléchargement. Dans ce cas le critère est Non Applicable.

### Contrôle de la consultation (d’un média temporel)

Possibilité pour l’utilisateur de contrôler la consultation d’un média temporel par le clavier et tout dispositif de pointage, au moins. Les points suivants doivent être respectés :
- Liste des fonctionnalités obligatoires de contrôle de la consultation :
- L’objet multimédia doit toujours avoir les fonctionnalités suivantes, au minimum : lecture, pause ou stop ;
- Si l’objet multimédia a du son, il doit avoir une fonctionnalité d’activation / désactivation du son ;
- Si l’objet multimédia a des sous-titres non incrustés, il doit avoir une fonctionnalité de contrôle de l’apparition / disparition des sous-titres ;
- Si l’objet multimédia a une audiodescription, il doit avoir une fonctionnalité de contrôle de l’apparition / disparition de l’audiodescription.
- Chaque fonctionnalité doit être accessible par le clavier, via la touche de tabulation, et par tout dispositif de pointage au moins.
- Chaque fonctionnalité doit être activable par le clavier et par tout dispositif de pointage, au moins.
Note : s’il n’y a pas de son à un média temporel, il n’est pas utile de mettre une fonctionnalité d’activation / désactivation du son. Si cette fonctionnalité est cependant présente et qu’elle nécessite une alternative textuelle pour être comprise par certains utilisateurs, il faut alors lui en donner une puisque l’utilisateur est susceptible d’y accéder et de vouloir l’activer.

### Contrôle de saisie (formulaire)

Ensemble des processus qui permettent de prévenir l’utilisateur des champs obligatoires, des indications de type ou de format attendus et des erreurs de saisie dans un formulaire. Ces contrôles de saisie peuvent être implémentés par l’auteur des contenus ou s’appuyer sur des attributs (comme `required` ou `pattern`), des attributs WAI-ARIA (comme `aria-required`) ou des types de champ qui produisent de manière automatique des indications de saisie ou d’erreurs (comme les types `url`, `email`, `date`, `time` par exemple).

### Contrôle (son déclenché automatiquement)

Possibilité pour l’utilisateur d’arrêter ou de relancer un son déclenché automatiquement.
Note : la méthode de contrôle du son devrait être disponible comme premier élément de la page.

### Correctement restitué (par les technologies d’assistance)

Lorsqu’un critère, un test ou une condition de test demande de vérifier la restitution d’un dispositif, il faut s’assurer que ladite restitution est compatible avec l’accessibilité.
Le test consiste à vérifier que la restitution est pertinente pour au moins une des combinaisons de l’environnement de test (ou « base de référence ») utilisé pour déclarer qu’un élément, un dispositif ou une alternative est « compatible avec l’accessibilité ».
Par exemple : le test 1.3.8 demande de vérifier que l’alternative d’une image bitmap (balise `<canvas>`) porteuse d’information est correctement restituée.
On procède alors à un test avec les outils de l’environnement de test défini pour le site.
Si on constate que l’alternative est correctement restituée, le test est validé.

### Couleur d’arrière-plan contiguë et couleur contiguë

Couleur d’arrière-plan contiguë : couleur d’arrière-plan directement en contact avec le bord extérieur du composant d’interface ou de l’élément graphique.
Exemples :
- Pour un bouton blanc avec une bordure bleue sur un fond blanc, le fond blanc à l’extérieur de la bordure bleue correspond à la couleur d’arrière-plan contiguë ;
- Pour un bouton rouge sur fond blanc, le fond blanc à l’extérieur du rouge correspond à la couleur d’arrière-plan contiguë ;
- Pour un bouton blanc avec une bordure verte qui devient noire à la prise de focus et au survol, le fond blanc à l’extérieur de la bordure verte de l’état par défaut et de la bordure noire de l’état au survol et au focus correspond à la couleur d’arrière-plan contiguë.
Couleur contiguë : couleur directement en contact avec une autre couleur. Exemple dans un panneau de « sens interdit » le rouge du panneau est la couleur contiguë au trait blanc au centre du panneau.
Note 1 : dans le cas de la présence d’un dégradé, c’est la couleur contiguë la moins contrastée du dégradé qui sera à considérer comme la couleur contiguë ou couleur d’arrière-plan contiguë.
Note 2 : dans le cas de la présence de plusieurs couleurs, c’est l’ensemble des couleurs qui seront à considérer comme couleur contiguë ou couleur d’arrière-plan contiguë.

### Description détaillée (image)

Contenu associé à une image en complément de son alternative textuelle afin de décrire en totalité l’information véhiculée par l’image. La description détaillée peut être associée à l’image via :
- Un attribut `longdesc` qui contient l’adresse d’une page ou d’un emplacement dans la page contenant la description détaillée ;
- Une référence à une description détaillée adjacente à l’image dans l’alternative textuelle ;
- Un lien ou un bouton adjacent qui permet d’accéder à la description détaillée dans la page ou dans une autre page ;
- Un ou plusieurs passages de texte identifiés par un id et liés par un attribut WAI-ARIA `aria-describedby` sur le modèle `aria-describedby="ID1 ID2 ID3…"`.
Note 1 : Si le support de l’attribut `aria-describedby` fait défaut, il est possible d’utiliser un ou plusieurs passages de texte identifiés par un `id` et liés par un attribut WAI-ARIA `aria-labelledby` à la suite de l’alternative textuelle.
Note 2 : Pour assurer une compatibilité maximum avec les agents utilisateurs, notamment Internet Explorer 11, il est recommandé d’implémenter un `tabindex="-1"` sur les balises qui contiennent un passage de texte et qui ne sont pas des éléments interactifs (bouton, liens, éléments de formulaires, etc.).

### Élément graphique

Élément faisant appel à une représentation visuelle telle que des images, des pictogrammes ou des graphiques.
Cet élément peut être composé d’une ou plusieurs parties dont la visibilité est nécessaire à sa compréhension (par exemple chaque point sur chaque ligne d’un graphique de statistiques).

### En-tête de colonne ou de ligne

Contenu d’une cellule dans un tableau de données (la première cellule d’une colonne ou d’une ligne, généralement) qui sert d’intitulé pour la totalité ou une partie des cellules de la colonne ou de la ligne. Une colonne ou une ligne peut contenir plusieurs en-têtes (en-tête intermédiaire). Lorsque les en-têtes s’appliquent à l’ensemble d’une ligne ou d’une colonne, ils peuvent être structurés avec une balise `<th>` ou une balise pourvue d’un attribut WAI-ARIA `role="rowheader"` ou `role="columnheader"`. Dans le cas contraire, seule une balise `<th>` peut être utilisée.
Note : seule la balise `<th>` étant totalement supportée par l’ensemble des technologies d’assistance, il est fortement recommandé de privilégier cette solution lors de la mise en œuvre afin d’éviter de nombreuses vérifications dans les différentes combinaisons prévues dans l’environnement de test (ou « base de référence »).

### Ensemble de pages

Pages web liées les unes aux autres par des liens et constituant un ensemble cohérent à l’intérieur d’un site web. Par exemple, les pages d’une rubrique spécifique, les pages d’un blog, les pages d’administration d’un compte client sont autant d’ensembles de page.
Note : la page d’accueil d’un site web peut constituer, à elle seule, un « ensemble de pages » du fait de son unicité.

### Environnement maîtrisé

Tout environnement dans lequel l’accès à l’information, les technologies, les conditions d’utilisation et le profil des utilisateurs peuvent être connus et maîtrisés. Les principaux éléments dont la maîtrise est essentielle sont :
- Le type et la version des navigateurs ;
- Les technologies supportées, leur version et leur activation (JavaScript, WAI-ARIA, Flash, Silverlight…) ;
- Les technologies d’assistance et tout dispositif utilisé de manière spécifique par les utilisateurs handicapés ;
- Les systèmes d’exploitation et les APIs d’accessibilité supportées ;
- La formation des utilisateurs de technologies d’assistance à l’utilisation de tout dispositif particulier (interface, application en ligne…).
Les auteurs et les administrateurs doivent garantir la compatibilité des technologies utilisées et de leurs usages par les utilisateurs et leurs technologies (y compris les technologies d’assistance). Les services d’information ou les sites Web, quel que soit leur statut, qui offrent un accès public ne peuvent pas être considérés comme des environnements maîtrisés.

### Étiquette de champ de formulaire

Texte à proximité du champ de formulaire permettant d’en connaître la nature, le type ou le format des informations attendues. L’étiquette peut être associée au champ de formulaire de plusieurs manières :
- Par l’utilisation d’une balise `<label>` ;
- Par l’utilisation de l’attribut WAI-ARIA `aria-label` ;
- Par l’utilisation d’une liaison entre le texte et le champ par l’attribut WAI-ARIA `aria-labelledby` ;
- Par l’utilisation de l’attribut `title`.
Note importante : lorsque plusieurs de ces techniques sont présentes sur un même champ, le calcul du « nom accessible », c’est-à-dire ce qui sera restitué, obéit à un ordre strict :
- `aria-labelledby` ;
- Sinon `aria-label` ;
- Sinon `<label>` ;
- Sinon `title`.
Cet ordre doit être utilisé pour l’évaluation de la pertinence de l’étiquette (critère 11.2). Par exemple, même dans le cas de la présence d’un `<label>`, c’est le passage de texte référencé par `aria-labelledby` qui doit être pris en compte.
Référence : Accessible name and description calculation.
Note importante au sujet de l’utilisation de `placeholder` : lorsque l’attribut `placeholder` est présent, il est susceptible d’être restitué à la place de l’attribut `title`. Par conséquent, lorsque ces deux attributs `title` et `placeholder` sont présents, ils doivent être identiques.
Note au sujet des étiquettes liées par `aria-labelledby` : Il s’agit d’un ou de plusieurs passages de texte identifiés par des `id` et liés par `aria-labelledby` sur le modèle suivant : `aria-labelledby="ID1 ID2 ID3…"`. Pour assurer une compatibilité maximum avec les agents utilisateurs, notamment Internet Explorer 11, il est recommandé d’implémenter un `tabindex="-1"` sur les passages de textes qui ne sont pas des éléments interactifs (bouton, liens, éléments de formulaires, etc.).
Note : l’attribut `aria-label` ne peut pas être utilisé pour indiquer le caractère obligatoire d’un champ.

### Étiquettes cohérentes

Les étiquettes de champs de formulaire présentes dans une même page ou dans un ensemble de pages et réclamant la saisie d’une même information doivent être formulées sans ambiguïté pour que l’utilisateur sache que l’information qu’il doit communiquer est la même.

### Feuille de style

Le langage CSS destiné à la mise en forme des éléments du contenu (exemples : couleur du fond de la page, taille / police / couleur des caractères, positionnement de l’information dans la page web…). Les styles CSS peuvent être externes (fichier CSS), embarqués (déclarés dans l’en-tête de la page) ou en ligne (déclarés via l’attribut `style` d’une balise).

### Formulaire

Balise `<form>` ou balise possédant un attribut WAI-ARIA `role="form"`.

### Gestes complexes et gestes simples

Un geste simple implique un contact en un point unique de l’écran. Il peut s’agir d’une pression ou d’un clic simple, d’une double-pression ou d’un double-clic, d’une pression prolongée.
Un geste complexe peut être à la fois un geste impliquant plusieurs points de contact sur l’écran (exemple : un geste avec deux doigts sur l’écran pour zoomer ou dézoomer une carte) et un geste basé sur le suivi d’une trajectoire sur l’écran (exemple : fonction JavaScript permettant de détection le déplacement d’un doigt vers la gauche ou droite sur une surface tactile pour déclencher le passage à l’item précédent / suivant d’un carrousel).

### Image de décoration

Image n’ayant aucune fonction et ne véhiculant aucune information particulière par rapport au contenu auquel elle est associée.
Exemples :
- Une image précédant chaque item d’une liste ;
- Une image servant à caler la mise en page ;
- Une image de coin arrondie pour habiller un bloc d’information ;
- Une image d’illustration n’apportant aucune information nécessaire à la compréhension du texte auquel elle est associée.
Note : les balises possédant un attribut WAI-ARIA `role="img"` ne peuvent faire office d’image de décoration qu’à la condition qu’elles possèdent un attribut WAI-ARIA `aria-hidden="true"`.

### Image objet

Image incorporée ou générée par une balise `<object>`.

### Image porteuse d’information

Image qui véhicule une information nécessaire à la compréhension du contenu auquel elle est associée.
Note 1 : lorsque l’image est le seul contenu d’un lien, son alternative est l’intitulé du lien. Dans ce cas, l’alternative de l’image devrait être évaluée avec la thématique « Liens ».
Note 2 : lorsqu’un bouton de formulaire, inséré avec l’élément `<button>`, ne contient qu’une image (balise `<img>`, `<object>`, `<embed>`, `<canvas>` ou `<svg>`), l’alternative de l’image est l’intitulé du bouton. Deux cas peuvent se présenter :
- Le bouton est contrôlé par son type, par exemple, le type `submit` ou `reset`, et fait partie d’un formulaire. Dans ce cas, le bouton image doit être évalué avec la thématique « Formulaires » ;
- Le bouton est contrôlé par un dispositif JavaScript. Dans ce cas, le bouton image doit être évalué avec la thématique « Scripts ».

### Image réactive

- Image réactive côté client (attribut `usemap`) : image divisée en zones cliquables ou neutres (attribut `nohref`) ;
- Image réactive côté serveur (attribut `ismap`) : image pour laquelle le navigateur transmet au serveur les coordonnées du pointeur, chaque jeu de coordonnées correspondant à une ressource (page web). L’image réactive côté serveur est extrêmement rare.
Note : en HTML5, l’attribut `ismap` est obsolète et non conforme pour les boutons de type `image` (`input type="image"`).

### Image-test

Image servant dans un test, captcha ou une image servant de test dans un quiz ou un jeu.
Exemple : une série d’images présente un détail issu de tableaux célèbres ; il faut reconnaître le titre et le peintre de chaque tableau. Dans cette situation, il n’est pas possible de donner une alternative pertinente (par exemple le nom du tableau et/ou du peintre) sans rendre le test inutilisable. L’alternative doit alors se contenter de donner la possibilité d’identifier l’image, par exemple “image 1 du test”.

### Image texte objet

Image générée par la balise `<object>` et affichant du texte.

### Image texte

Image affichant du texte.
Note : il n’est pas recommandé d’utiliser des images-textes. Lorsqu’il est possible de reproduire les mêmes effets en CSS, le critère 1.8 impose que le texte soit reproduit en texte CSS, ou qu’un mécanisme de remplacement permette à l’utilisateur de remplacer ces images par du texte stylé en CSS.

### Image véhiculant une information (donnée par la couleur)

Image dont tout ou partie du contenu transmet visuellement une information par l’intermédiaire d’une couleur uniquement.

### Indication de champ obligatoire

Indication textuelle ou graphique (icône) permettant à l’utilisateur de savoir que la saisie d’un champ est obligatoire préalablement à la saisie.
Note : Dans le cas où cette indication n’est pas réalisée de manière textuelle explicite (icône, “*”, “!”, etc.), l’explication de la signification de cette indication doit se situer, visuellement et dans l’ordre du code source, avant la première utilisation de l’indication.

### Indication donnée par la forme, la taille ou la position

Il peut s’agir, par exemple :
- De la présence d’un marqueur visuel, pour indiquer la page active dans un menu de navigation (indication donnée par la position) ;
- D’une mise en avant-plan pour indiquer un onglet actif (indication donnée par la forme) ;
- D’une modification de la taille de police dans un nuage de tags (indication donnée par la taille).
Ou de tout autre effet graphique similaire.

### Indication du type de données et/ou de format

Indication textuelle permettant à l’utilisateur de savoir quel est le type de donnée et/ou le format de saisie requis par un champ obligatoire, préalablement à son renseignement.
Exemples :
- Courriel (format : vous@domaine.com) ;
- Code postal (format : 00000) ;
- Date (format : JJ/MM/AAAA).

### Information (donnée par la couleur)

Information transmise visuellement par l’intermédiaire d’une couleur. L’indication que les champs en rouge sont obligatoires dans un formulaire, l’utilisation d’un fond bleu pour indiquer la page en cours de consultation dans un menu avec le fond vert, le changement de couleur d’un nom d’article pour indiquer son indisponibilité dans une liste d’articles sont autant d’exemples d’indication donnée par la couleur.
Lorsqu’une information donnée par la couleur est accompagnée d’une autre méthode à destination des utilisateurs qui ne voient pas ou perçoivent mal les couleurs ou leurs associations, le critère sera considéré comme non applicable.
Les moyens de transmettre une information autrement que par la couleur peuvent être :
- Une indication textuelle visible ;
- Un moyen faisant intervenir du graphisme (pictogramme, image de fond, forme, style de bordure différent, etc.) et par le biais d’un complément au niveau du code (`aria-label`, `title`, texte masqué, `aria-current`, etc.) ;
- Un autre style typographique (gras, italique, taille de texte, autre police, etc) et par le biais d’un complément au niveau du code (`aria-label`, `title`, texte masqué, `aria-current`, etc.).

### Intitulé (ou nom accessible) de lien

« Nom accessible » restitué par les technologies d’assistance.
Dans le cas d’un lien HTML, le « nom accessible » est obtenu selon l’ordre suivant :
- passage de texte associé par l’attribut WAI-ARIA `aria-labelledby` ;
- sinon, contenu de l’attribut WAI-ARIA `aria-label` ;
- sinon, contenu du lien ;
- sinon, contenu de l’attribut `title`.
Cet ordre doit être utilisé pour déterminer ce qui constitue l’intitulé du lien. Par exemple :
- en cas de présence conjointe d’un attribut WAI-ARIA `aria-label` et d’un attribut WAI-ARIA `aria-labelledby`, c’est le passage de texte référencé par l’attribut WAI-ARIA `aria-labelledby` qui doit être considéré comme l’intitulé ;
- en cas de présence conjointe d’un attribut WAI-ARIA `aria-label` et d’un contenu dans le lien, c’est le contenu de l’attribut WAI-ARIA `aria-label` qui doit être considéré comme l’intitulé.
Référence : Accessible name and description calculation.
Dans le cas où le « nom accessible » est obtenu à partir du contenu du lien, celui-ci sera variable en fonction des cas suivants :
Lien texte :
En HTML, le « nom accessible » correspond au texte constitué à partir :
- du texte contenu dans le lien ;
- du texte contenu dans les éléments enfants du lien.
Lien image :
En HTML, le « nom accessible » correspond au texte constitué à partir de l’alternative textuelle d’une ou plusieurs images dans le lien du type :
- Image (élément `<img>` ou balise ouvrante ayant l’attribut WAI-ARIA `role="img"`) ;
- Image objet (élément `<object>`) ;
- Image bitmap (élément `<canvas>`) ;
- Image vectorielle (élément `<svg>`).
Lien composite :
En HTML, le « nom accessible » correspond au texte constitué à partir de l’ensemble :
- du texte contenu dans le lien ;
- du texte contenu dans les éléments enfant du lien ;
- du contenu de l’alternative textuelle de la ou des images comprises dans le lien.
Dans le cas d’un lien SVG (version 1.1), le « nom accessible » est obtenu comme suit :
- Passage de texte associé par l’attribut WAI-ARIA `aria-labelledby` ;
- Sinon, contenu de l’attribut WAI-ARIA `aria-label` ;
- Sinon, contenu de l’élément `<title>` enfant direct du lien ;
- Sinon, contenu de l’attribut `xlink:title` ;
- Sinon, contenu texte d’un ou plusieurs éléments `<text>`.
Il faut cependant être vigilant car cet algorithme de calcul n’est pas encore pris en compte et effectif au sein des différents lecteurs d’écran. À ce jour, le support est disponible avec VoiceOver, mais incomplet ou lacunaire avec JAWS et NVDA. Si bien que le plus petit dénominateur commun sur lequel il est possible de se reposer pour fournir un intitulé au lien est l’élément `<text>`.
Note 1 : un intitulé de lien sera considéré comme non-explicite dans le cas où le « nom accessible » ne reprend pas l’intitulé visible du lien.
Note 2 : en raison de la configuration possible des aides techniques permettant de forcer la restitution du « nom accessible » issu du contenu de l’attribut `title` au détriment du « nom accessible » issu du contenu du lien. Un intitulé de lien sera considéré comme non-explicite dans le cas où le lien possède un attribut `title` dont la valeur ne reprendrait pas au moins le « nom accessible » issu du contenu du lien.
Note 3 : dans le cas de la présence de plusieurs liens ayant une destination différente dont le « nom accessible » est identique. L’intitulé de lien seul sera considéré comme non-explicite si le contexte de lien ne permet pas de les différencier.
Note 4 : lorsqu’un lien ne comporte aucun contenu, il sera non conforme au regard du critère 10.2 et du critère 6.2.
Note 5 : bien que le calcul du nom accessible d’un lien tienne compte de contenus texte générés en CSS via les pseudo-éléments `::before` et `::after`, cette pratique ne doit pas être utilisée, car elle constitue une non-conformité au critère 1.3.1 des WCAG 2.1 (cf. F87).

### Intitulé visible

Texte affiché faisant office d’intitulé visible à l’écran au sein d’un bouton ou d’un lien.
Texte affiché faisant office d’étiquette pour un champ formulaire.
Ce texte peut être constitué de texte ou d’une image contenant du texte.

### Items de même nature d’une liste de choix

Dans une liste déroulante (balise `<select>`), ensemble d’items (balises `<option>`) pouvant être regroupés par leur nature. Le regroupement vise à identifier les items devant être traités comme un ensemble (par exemple, une liste de départements regroupés par régions).

### Landmarks

WAI-ARIA propose des rôles permettant d’indiquer les zones principales (régions) du document. Ces rôles sont très profitables aux utilisateurs de lecteurs d’écran notamment, mais également aux utilisateurs de la navigation au clavier qui peuvent ainsi bénéficier de fonctionnalités de navigation rapide dans la structure du document.
Les rôles doivent être définis dans le document en fonction de la nature de la zone :
- La zone d’en-tête doit avoir un attribut WAI-ARIA `role="banner"` ;
- Le menu de navigation principal doit avoir un attribut WAI-ARIA `role="navigation"` ;
- La zone de contenu principal doit avoir un attribut WAI-ARIA `role="main"` ;
- La zone de pied de page doit avoir un attribut WAI-ARIA `role="contentinfo"` ;
- La zone de moteur de recherche sur le site doit avoir un attribut WAI-ARIA `role="search"`.
Note 1 : Si la plupart des lecteurs d’écran mettent à disposition ces fonctionnalités, les navigateurs n’ont pas encore proposé de fonctionnalité de navigation dédiée pour les utilisateurs qui ne peuvent pas utiliser la souris. La mise en place des liens d’évitement reste donc à privilégier par rapport aux landmarks.
Note 2 : Les rôles WAI-ARIA `banner`, `main` et `contentinfo` doivent être uniques dans la page. Le rôle WAI-ARIA `navigation` est réservé aux zones de navigations principales et secondaires. Lorsqu’il y a plusieurs rôles WAI-ARIA `navigation`, il peut être utile de les différencier en précisant un nom à chacune des zones via l’attribut WAI-ARIA `aria-label` ou `aria-labelledby`.

### Langue par défaut

Indication de la langue de traitement principale du document qui peut être présente sur l’élément racine `html` ou sur chaque élément de la page concerné via les attributs `lang` et/ou `xml:lang` selon le schéma suivant :
- Pour HTML jusqu’à la version 4.01 : attribut `lang` obligatoire, attribut `xml:lang` non supporté ;
- Pour XHTML 1.0 servi en `"text/html"` : attribut `lang` et `xml:lang` obligatoires ;
- Pour XHTML 1.0 servi en `"application/xhtml+xml"` : attribut `xml:lang` obligatoire, attribut `lang` recommandé ;
- Pour XHTML 1.1 : attribut `xml:lang` obligatoire, attribut `lang` non supporté ;
- Pour HTML5 : attribut `lang` obligatoire.

### Le nom, le rôle, la valeur, le paramétrage et les changements d’états

Un composant doit avoir un rôle et un nom appropriés. Ses valeurs, états et paramètres éventuels doivent également être accessibles et correctement transmis aux APIs d’accessibilité notamment.
Un composant peut s’appuyer sur un élément interactif HTML ou sur un élément non interactif surchargé par WAI-ARIA via un rôle ad hoc. Important : les boutons (balises `<button>` ou `<input type="button">`) lorsqu’ils sont contrôlés via JavaScript sont à évaluer avec le critère 7.1.
Le nom peut être l’intitulé du composant (l’intitulé d’un bouton, par exemple).
La valeur est, par exemple, l’élément sélectionné d’une liste déroulante ou la valeur actuelle d’un curseur (`slider`).
Le rôle correspond au type d’élément défini par la spécification HTML ou WAI-ARIA (comme la balise `<button>` ou l’attribut WAI-ARIA `role="button"`).
Le paramétrage correspond aux informations particulières d’un composant, généralement mis à disposition par WAI-ARIA. Par exemple `aria-controls` est un paramètre qui transmet aux APIs l’information que le composant contrôle tel ou tel contenu (référencé par son identifiant -- attribut `id`).
Les changements d’état sont également mis à disposition par WAI-ARIA. Par exemple `aria-expanded` est un état permettant de signaler aux APIs que le composant est « ouvert » ou « fermé ». À noter qu’un état peut également être transmis via le nom, lorsque l’intitulé est changé dynamiquement pour correspondre à l’état de la zone contrôlée notamment.
Ces paramètres ne sont pas obligatoires mais peuvent être requis s’ils sont indispensables pour rendre le composant accessible. C’est à l’auditeur de considérer les cas où ces paramètres sont indispensables en fonction du contexte lié à l’utilisation du composant.
L’auditeur doit également vérifier que, lorsqu’ils sont présents, ces paramètres sont correctement utilisés.
Pour ce faire (s’il juge cela pertinent compte tenu du contexte d’implémentation des composants et des choix ergonomiques mis en œuvre) il peut s’appuyer sur les recommandations d’utilisation de WAI-ARIA pour les composants ayant des attributs WAI-ARIA correspondant à un motif de conception tel que décrit dans le document WAI-ARIA 1.1 Authoring Practices.
Note : les rôles, propriétés et états WAI-ARIA s’implémentent via des attributs, par exemple `role="banner"`, `aria-hidden="true"`.

### Légende d’image

Lorsqu’un texte, adjacent à une image, contient des informations sur l’image (par exemple un copyright, une date, un auteur…) ou est destiné à compléter les informations apportées par l’image (par exemple un texte associé à une image dans une galerie d’images), on parle de légende d’image.
Lorsqu’une image est légendée il est nécessaire d’associer la légende de l’image à l’image par une relation de structure, de telle sorte que les technologies d’assistance puissent traiter l’image et sa légende comme un ensemble unique.
HTML5 propose d’associer une légende à une image via les éléments `figure` (l’ensemble de l’image et la légende) et `figcaption` (la légende).
Une image sans légende peut définir :
- Une image qui n’est pas insérée dans un élément `figure` ;
- Une image insérée dans un élément `figure` sans élément `figcaption`.
Note : lorsque le texte adjacent à l’image peut faire office de texte de remplacement, il n’est pas obligatoire de recourir à l’ensemble `figure`, `figcaption`, l’image pouvant être simplement traitée comme une image de décoration.
Vous pouvez consulter, à ce sujet, la note en anglais Requirements for providing text to act as an alternative for images du W3C.

### Légende

HTML propose un dispositif permettant de titrer les groupes de champs de même nature par l’intermédiaire des éléments `<fieldset>` et `<legend>`.
Il est également possible de créer des regroupements avec le rôle WAI-ARIA `group` et un passage de texte, faisant office de légende, lié par l’attribut WAI-ARIA `aria-labelledby` ou fourni par un attribut WAI-ARIA `aria-label`.
Note 1 : Les regroupements de champs peuvent utiliser d’autres méthodes qui associent l’information du regroupement directement dans l’étiquette du champ. Par exemple, par l’intermédiaire d’un attribut `title`, d’un attribut WAI-ARIA `aria-label`, d’une liaison `aria-labelledby` faisant office d’étiquette ou encore par l’attribut WAI-ARIA `aria-describedby` associant un texte complémentaire. Dans ce cas, le regroupement de champs devient inutile puisque les labels sont suffisamment pertinents.
Note 2 : Lorsque le formulaire est constitué d’un seul bloc d’informations de même nature (l’identité et l’adresse de l’utilisateur, par exemple) ou d’un champ unique (un moteur de recherche, par exemple), le regroupement des champs n’est pas obligatoire.

### Lien composite

En HTML, lien contenant à la fois du texte et un ou plusieurs enfants de type image :
- Image (balise `<img>` ou balise ouvrante ayant l’attribut WAI-ARIA `role="img"`) ;
- Zone cliquable (balise `<area>`) possédant un attribut `href` ;
- Image objet (balise `<object>`) ;
- Image bitmap (balise `<canvas>`) ;
- Image vectorielle (balise `<svg>`).
Note importante : il est rappelé que l’utilisation de deux liens adjacents (lien image et lien texte) et identiques constitue une gêne importante pour l’utilisateur. Même si cela ne constitue pas une non-conformité, cet usage devrait être évité. Une manière de traiter ce type de liens est d’inclure l’image dans le lien texte de façon à constituer un lien composite, ce qui évitera la redondance.
Vous pouvez consulter à ce sujet la technique H2 : Combining adjacent image and text links for the same resource.

### Lien dont la nature n’est pas évidente

Lien qui peut être confondu avec un texte normal lorsqu’il est signalé uniquement par la couleur par certains types d’utilisateurs ne percevant pas ou mal les couleurs. Par exemple, dans ce texte “Nouvelle grève à la SNCF”, si le mot “grève” est un lien signalé uniquement par la couleur, sa nature peut être ignorée par les utilisateurs ne percevant pas la couleur et accédant au contenu CSS activé.
Note : “signalés uniquement par la couleur” signifie que le lien n’est accompagné d’aucun marqueur visuel (icône, soulignement, bordure…). En conséquence, un lien de la même couleur que le texte environnant est concerné par ce critère.

### Lien image

En HTML, lien contenant uniquement un ou plusieurs enfants de type image :
- Image (balise `<img>` ou balise ouvrante ayant l’attribut WAI-ARIA `role="img"`) ;
- Zone cliquable (balise `<area>`) possédant un attribut `href` ;
- Image objet (balise `<object>`) ;
- Image bitmap (balise `<canvas>`) ;
- Image vectorielle (balise `<svg>`).

### Lien ou bouton adjacent

Lien ou bouton présenté de manière adjacente à un élément dans la page. Le lien ou bouton doit être adjacent visuellement dans la représentation graphique (CSS activé) et dans le code HTML. Dans le code HTML, le lien ou bouton doit se situer juste avant ou juste après l’élément auquel il est adjacent.

### Lien SVG

Lien contenu dans un élément `<svg>`.
Dans le cas d’un lien SVG (version 1.1), le « nom accessible » est obtenu comme suit :
- Passage de texte associé par l’attribut WAI-ARIA `aria-labelledby` ;
- Sinon, contenu de l’attribut WAI-ARIA `aria-label` ;
- Sinon, contenu de l’élément `<title>` enfant direct du lien ;
- Sinon, contenu de l’attribut `xlink:title` ;
- Sinon, contenu texte d’un ou plusieurs éléments `<text>`.
Il faut cependant être vigilant car cet algorithme de calcul n’est pas encore pris en compte et effectif au sein des différents lecteurs d’écran. À ce jour, le support est disponible avec VoiceOver, mais incomplet ou lacunaire avec JAWS et NVDA. Si bien que le plus petit dénominateur commun sur lequel il est possible de se reposer pour fournir un intitulé au lien est l’élément `<text>`.

### Lien texte

En HTML, lien ne contenant aucun élément enfant de type :
- Image (balise `<img>` ou balise ouvrante ayant l’attribut WAI-ARIA `role="img"`) ;
- Image objet (balise `<object>`) ;
- Image bitmap (balise `<canvas>`) ;
- Image vectorielle (balise `<svg>`).

### Lien

En HTML :
- Balise `<a>` possédant un attribut `href` ;
- Balise possédant un attribut WAI-ARIA `role="link"` et dont l’action de navigation est prise en charge par un script.
En SVG :
- Balise `<a>` possédant un attribut `xlink:href` en SVG 1.1.

### Liens d’évitement ou d’accès rapide

Liens dont la fonction est de permettre de naviguer à l’intérieur de la page (lien d’évitement, lien d’accès au formulaire de recherche ou au menu…). Ces liens peuvent soit permettre d’accéder à une zone de la page (lien d’accès rapide) ou de sauter une zone dans la page (lien d’évitement).
Note 1 : Un lien d’évitement ou d’accès rapide fonctionnel est un lien dont l’activation permet de reprendre la lecture et la navigation clavier à partir de la cible du lien lors de l’utilisation des navigateurs et des aides techniques retenus dans l’environnement de test (ou « base de référence ») de l’audit.
Note 2 : les liens d’évitements ou d’accès rapide doivent être situés à la même place dans la présentation et dans le même ordre relatif dans le code source afin de satisfaire au critère 12.2.

### Liste des valeurs possibles pour l’attribut `autocomplete`

La liste des valeurs disponibles est fournie par la spécification WCAG 2.1 :
- `name` -- Nom complet ;
- `honorific-prefix` -- Abréviation, civilité ou titre ;
- `given-name` -- Prénom ;
- `additional-name` -- Prénoms additionnels ;
- `family-name` -- Nom de famille ;
- `honorific-suffix` -- Suffixe honorifique ;
- `nickname` -- Surnom, diminutif ;
- `organization-title` -- Fonction, intitulé de poste ;
- `username` -- Nom d’utilisateur ;
- `new-password` -- Nouveau mot de passe (par exemple, lors de la création d’un compte ou d’un changement de mot de passe) ;
- `current-password` -- Mot de passe actuel pour le compte identifié par le champ `username` (par exemple, lors d’une connexion) ;
- `organization` -- Nom de l’organisation correspondant à la personne, à l’adresse ou à l’information de contact dans les autres champs associés avec ce champ ;
- `street-address` -- Adresse postale (multiligne, nouvelles lignes conservées) ;
- `address-line1` -- Adresse postale (une ligne par champ, ligne 1) ;
- `address-line2` -- Adresse postale (une ligne par champ, ligne 2) ;
- `address-line3` -- Adresse postale (une ligne par champ, ligne 3) ;
- `address-level4` -- Le niveau administratif le plus détaillé, pour les adresses pourvues de quatre niveaux administratifs ;
- `address-level3` -- Le troisième niveau administratif, pour les adresses pourvues d’au moins trois niveaux administratifs ;
- `address-level2` -- Le deuxième niveau administratif, pour les adresses pourvues d’au moins deux niveaux administratifs ;
- `address-level1` -- Le plus large niveau administratif d’une adresse, c’est-à-dire la province dans laquelle se trouve la localité ;
- `country` -- Code pays ;
- `country-name` -- Nom de pays ;
- `postal-code` -- Code postal, code CEDEX (si le CEDEX est présent, ajouter “CEDEX”, et ce qui le suit doit être ajouté dans le champ `address-level2`) ;
- `cc-name` -- Nom complet figurant sur le moyen de paiement ;
- `cc-given-name` -- Prénom figurant sur le moyen de paiement ;
- `cc-additional-name` -- Prénoms additionnels figurant sur le moyen de paiement ;
- `cc-family-name` -- Nom de famille figurant sur le moyen de paiement ;
- `cc-number` -- Code identifiant le moyen de paiement (e.g., un numéro de carte bancaire) ;
- `cc-exp` -- Date d’expiration du moyen de paiement ;
- `cc-exp-month` -- Le mois de la date d’expiration du moyen de paiement ;
- `cc-exp-year` -- L’année de la date d’expiration du moyen de paiement ;
- `cc-csc` -- Code de sécurité du moyen de paiement (also known as the card security code (CSC), card validation code (CVC), card verification value (CVV), signature panel code (SPC), credit card ID (CCID), etc.) ;
- `cc-type` -- Type de moyen de paiement (e.g. Visa) ;
- `transaction-currency` -- La devise qui a la préférence de l’utilisateur lors d’une transaction ;
- `transaction-amount` -- Le montant qui a la préférence de l’utilisateur lors d’une transaction (e.g., en réponse à une enchère ou à un prix soldé) ;
- `language` -- Langue préférée ;
- `bday` -- Date d’anniversaire ;
- `bday-day` -- Le jour de la date d’anniversaire ;
- `bday-month` -- Le mois de la date d’anniversaire ;
- `bday-year` -- L’année de la date d’anniversaire ;
- `sex` -- Identité de genre ;
- `url` -- Page d’accueil ou une autre page Web correspondant à l’organisation, la personne, l’adresse ou à l’information de contact dans les autres champs associés avec ce champ ;
- `photo` -- Photographie, icône ou une autre image correspondant à l’organisation, la personne, l’adresse ou à l’information de contact dans les autres champs associés avec ce champ ;
- `tel` -- Numéro de téléphone complet, y compris le code pays ;
- `tel-country-code` -- Code pays du numéro de téléphone ;
- `tel-national` -- Numéro de téléphone sans la partie code pays, avec un préfixe interne au pays, s’il y a lieu ;
- `tel-area-code` -- Indicatif régional du numéro de téléphone, avec un préfixe interne au pays, s’il y a lieu ;
- `tel-local` -- Numéro de téléphone sans la partie code pays ni l’indicatif régional ;
- `tel-local-prefix` -- La première partie du composant du numéro de téléphone qui suit l’indicatif régional, lorsque ce composant est scindé en deux parties ;
- `tel-local-suffix` -- La seconde partie du composant du numéro de téléphone qui suit l’indicatif régional, lorsque ce composant est scindé en deux parties ;
- `tel-extension` -- Numéro de téléphone d’un poste interne ;
- `email` -- Adresse électronique ;
- `impp` -- URL correspondant d’un protocole de messagerie instantanée (par exemple, `"aim:goim?screenname=example"` ou `"xmpp:fred@example.net"`).

### Listes

Suite d’éléments pouvant être regroupés sous la forme d’une liste structurée ordonnée, non ordonnée ou de définition. Par exemple la suite des liens d’un menu de navigation est une liste de liens non ordonnée, les différentes étapes d’une procédure sont une liste d’éléments ordonnés, le couple terme/description d’un glossaire est une liste de description. En HTML, les listes utilisent les balises suivantes :
- Liste ordonnée : balises `<ol>` et `<li>` (chaque élément de la liste est affecté d’un marqueur indexé) ;
- Liste non ordonnée : balises `<ul>` et `<li>` (chaque élément de la liste est affecté d’un marqueur non-indexé ;
- Liste de description : balises `<dl>`, `<dt>` (terme à décrire) et `<dd>` (description).
Note 1 : En HTML5, la balise `<dl>` ne représente plus seulement une liste de définition, mais de manière générique toute liste de description qui peut comprendre comme groupe de termes-descriptions des noms et des définitions, des questions et réponses, des catégories et des sujets, etc.
Note 2 : Il est également possible de structurer les listes à l’aide des attributs WAI-ARIA `role="list"` et `role="listitem"` pour les listes ordonnées et non ordonnées.
Note 3 : la notion de « regroupés visuellement sous forme de liste » se caractérise par :
- La présence d’un marqueur visuel permettant de faire comprendre qu’il s’agit d’une liste non ordonnée par exemple `-`, `•`, `\*`, etc. ;
- La présence d’un marqueur visuel permettant de faire comprendre qu’il s’agit d’une liste ordonnée par exemple un chiffre, une lettre grecque, etc. ;
- La présence d’une série d’éléments se suivant visuellement les uns les autres, avec une forme visuelle, une nature et un fonctionnement identique, mais sans avoir directement de marqueur visuel de liste (non ordonnée ou ordonnée), par exemple un menu de navigation.
Attention cependant toutes les listes ne nécessitent pas obligatoirement une structure de liste, par exemple une série de termes séparés par une virgule.

### Mécanisme de remplacement

Mécanisme généralement basé sur CSS, permettant à l’utilisateur de remplacer du texte par du texte en image et inversement sur le principe du style switcher. Le mécanisme peut utiliser un langage de script côté serveur ou un langage de script côté client.

### Mécanisme qui permet d’afficher un rapport de contraste conforme

Composant d’interface dont l’activation permet de modifier l’apparence du site ou de la page de manière à afficher les contenus avec un ratio de contraste suffisant. Le design de ce composant d’interface devra être conforme au critère 3.2 et au critère 3.3 sans avoir recours lui-même à un mécanisme permettant d’afficher un rapport de contraste conforme. Ce mécanisme doit conserver à l’identique les contenus et les fonctionnalités du site ou de la page qu’il modifie.

### Média non temporel

Contenu qui ne se déroule pas dans le temps, consultable via un plugin (Flash, Java, Silverlight…) ou via les éléments `svg` et `canvas` ; par exemple, une carte interactive en Flash, une application Flash ou Java, un diaporama sont des médias non temporels. Un média non temporel peut contenir des médias temporels (un lecteur Flash qui propose une liste de vidéos à consulter, par exemple).
Note : l’utilisation du paramètre `wmode` pour un objet Flash avec les valeurs `"transparent"` et `"opaque"` invalide de fait le critère 4.13. En effet, l’utilisation de ces valeurs a pour conséquence que l’animation Flash vue du côté des utilisateurs de lecteur d’écran est invisible.

### Média temporel (type son, vidéo et synchronisé)

- Média temporel seulement audio : contenu sonore (Wav, Mp3…) ;
- Média temporel seulement vidéo : images ou photos en mouvement ou en séquence ;
- Média temporel synchronisé : flux audio ou vidéo synchronisé avec un autre format pour présenter de l’information et/ou comportant des composants temporels interactifs. Un média temporel peut être consulté de 2 manières différentes :
- Fichier à télécharger consultable avec un logiciel externe à la page web ;
- Contenu embarqué dans la page web et consultable dans la page web via :
- Un plugin (par exemple une vidéo diffusée par un lecteur Flash) ;
- L’élément `<video>` (par exemple une vidéo) ;
- L’élément `<audio>` (par exemple un podcast) ;
- L’élément `<svg>` (par exemple un dessin animé vectoriel) ;
- L’élément `<canvas>` (par exemple un dessin animé en image bitmap) ;
- L’élément `<bgsound>` pour diffuser un arrière-plan sonore à la page web.
Un média temporel peut être diffusé en temps réel ou être proposé en lecture de manière asynchrone (média pré-enregistré).
Note 1 : l’utilisation du paramètre `wmode` pour un objet Flash avec les valeurs `"transparent"` et `"opaque"` invalide de fait le critère 4.13. En effet, l’utilisation de ces valeurs a pour conséquence que l’animation Flash vue du côté des utilisateurs de lecteur d’écran est invisible.
Note 2 : les gif animés, les animations d’images réalisées par JavaScript ou CSS ne sont pas considérés comme étant des médias temporels.
Note 3 : l’élément `<bgsound>` est spécifique à Internet Explorer et ne devrait pas être utilisé.

### Menu et barre de navigation

Liste de liens permettant une navigation spécifique dans le site, dans une rubrique ou dans une collection de pages.
Les principales barres de navigation (critère 12.2) sont :
- Un menu de navigation ;
- Un fil d’ariane ;
- Une liste de navigation d’une liste de résultats ;
- Des liens d’évitement.
Il existe différents types de menu de navigation (critère 12.1 et critère 12.2) :
- Menu de navigation principal ;
- Menu de sous-rubrique ;
- Menu contextuel ;
- Table des matières concernant un ensemble de pages.
Note : Les liens de pied de page renvoyant vers les mentions légales, plan du site et autres informations concernant le site ne sont pas considérés comme un menu de navigation principal.

### Message de statut

Un message de statut informe l’utilisateur d’un changement de contenu dans la page sans interrompre son activité principale (il n’y a pas de changement de contexte par exemple un repositionnement du focus sur le message).
Un message de statut peut informer sur :
- Le succès ou le résultat d’une action ;
- L’état occupé d’une application ;
- L’état de progression d’un processus ;
- L’existence d’erreur.

### Modifier ou annuler les données et les actions effectués

Procédés par lesquels un utilisateur peut modifier les données qu’il a saisies, faire annuler sa saisie ou faire annuler les actions découlant de sa saisie par exemple annuler une commande ou un virement bancaire.
Note : La page contenant un formulaire qui modifie ou supprime des données, ou qui transmet des réponses à un test ou un examen, ou dont la validation a des conséquences financières ou juridiques, doit indiquer explicitement la durée pendant laquelle l’utilisateur peut demander l’annulation de sa saisie. Elle devra également contenir la procédure à effectuer pour annuler cette saisie. Cette procédure n’a pas à être obligatoirement réalisable en ligne même si cela reste recommandé.

### Moteur de recherche (interne à un site web)

Zone donnant accès directement (formulaire) ou indirectement (élément d’interface donnant accès au formulaire) au moteur de recherche qui permet d’effectuer des recherches sur les contenus de l’ensemble du site.
Note : Attention à ne pas confondre cette zone de recherche, unique dans le site, avec tout autre moteur de recherche permettant par exemple de faire des recherches sur une partie restreinte du site : un catalogue, les offres sur une section marchés publics…
Voir la définition technique de zone d’en-tête fournie par WAI-ARIA `search(role)`.

### Motif de conception

Un motif de conception (Design Pattern) est un modèle défini dans le document WAI-ARIA 1.1 Authoring Practices qui décrit la structure, les rôles et propriétés et le comportement clavier que doit respecter un composant JavaScript (widget).
Il est recommandé que les composants développés en JavaScript utilisant des attributs WAI-ARIA correspondant à un motif de conception respectent celui-ci. Attention cependant, les motifs de conception ne sont pas tous adaptés à un usage non applicatif, en particulier pour les sites proposant un affichage en contexte mobile.
Note 1 : compte tenu du manque de support de certaines propriétés et de certains rôles WAI-ARIA et de la grande variabilité des situations dans lesquelles un composant JavaScript peut être proposé, il est possible d’adapter des motifs de conception à des contextes ou des utilisations particulières. Dans ce cas, le motif de conception adapté doit :
- Respecter la structure générale : par exemple un ensemble de panneaux (rôle WAI-ARIA `tabpanel`) d’un système d’onglets est forcément lié à un ensemble d’onglets (rôle WAI-ARIA `tablist`) ;
- Utiliser en remplacement d’un rôle ou d’une propriété WAI-ARIA mal supporté, un rôle ou une propriété WAI-ARIA équivalent, offrant un comportement et une restitution similaire.
Note 2 : Le fait d’enrichir un motif de conception de rôles ou propriétés WAI-ARIA supplémentaires dont la compatibilité avec l’accessibilité est contrôlée par le test de restitution sur l’environnement de test (ou « base de référence ») ne constitue pas une adaptation d’un motif de conception. Par exemple l’ajout de l’attribut WAI-ARIA `aria-hidden` sur les panneaux (rôle WAI-ARIA `tabpanel`) d’un système d’onglets ne définit pas un motif de conception adapté.

### Ordre de tabulation

Ordre dans lequel le focus se déplace (vers un élément suivant ou vers un élément précédent). L’ordre naturel est celui qui est implémenté via le code source. Lorsqu’il est modifié par l’utilisation de l’attribut `tabindex` ou par l’utilisation d’une commande JavaScript, c’est l’ordre modifié qui fait référence.
Attention : lorsqu’un élément initie un changement dans la page (changement de contexte, gestion de zones cachées, ajout de contenu, gestion de champs de formulaire…) il est nécessaire d’activer l’élément qui initie le changement pour tester la cohérence de l’ordre de tabulation.

### Page « plan du site »

Page dédiée présentant l’arborescence d’un site web, généralement sous forme de listes de liens organisées en rubriques et sous-rubriques donnant accès à l’ensemble des pages du site.
Note 1 : les liens du plan du site peuvent être constitués de balises `<a>` ou de balises `<area>`.
Note 2 : il n’est pas nécessaire que le plan du site contienne les liens vers toutes les pages du site, en revanche il est nécessaire qu’à partir du plan du site, l’utilisateur puisse atteindre l’ensemble des pages du site.

### Passage de texte lié par `aria-labelledby` ou `aria-describedby`

Il s’agit d’un ou de plusieurs passages de texte identifiés par des `id` dont la valeur est unique dans la page et associés à un élément (champ de formulaire, bouton, etc.) par les attributs WAI-ARIA `aria-labelledby` ou `aria-describedby` sur le modèle suivant : `aria-labelledby="ID1 ID2 ID3…"` où la valeur de l’attribut utilisé est égale à la liste des valeurs d’attributs `id` des passages de texte à associer présents dans la page.
Note 1 : pour assurer une compatibilité maximum avec les agents utilisateurs, notamment Internet Explorer 11, il est recommandé d’implémenter un `tabindex="-1"` sur les passages de textes qui ne sont pas des éléments interactifs (bouton, liens, éléments de formulaires, etc.).
Note 2 : la valeur des attributs WAI-ARIA `aria-labelledby` ou `aria-describedby` ne doivent pas créer de référence récursive (A référence B qui référence A) ou traversante (A qui référence B qui référence C).

### Présentation de l’information

Restitution visuelle des contenus via un navigateur en mode graphique. La présentation concerne le style, la position et les dimensions des éléments HTML et de leur contenu. La présentation de l’information doit être réalisée via CSS. Les éléments (`basefont`, `big`, `blink`, `center`, `font`, `marquee`, `s`, `strike` et `tt`) et les attributs (`align`, `alink`, `background`, `bgcolor`, `border`, `cellpadding`, `cellspacing`, `char`, `charoff`, `clear`, `compact`, `color`, `frameborder`, `hspace`, `link`, `marginheight`, `marginwidth`, `text`, `valign`, `vlink`, `vspace`) sont interdits.
Notes :
- Les attributs `width` et `height` utilisés sur d’autres éléments que les éléments `<img>`, `<object>`, `<embed>`, `<canvas>` et `<svg>` sont également interdits ;
- L'attribut `size` utilisé sur d’autres éléments que l'élément `<select>` est également interdit ;
- L’élément `<u>` est interdit uniquement si le DOCTYPE du document ne correspond pas à HTML 5.

### Pressé ou posé

Correspond aux gestionnaires d’événement JavaScript considérés comme des événements descendants (`mousedown`, `touchstart` par exemple).

### Prise de focus

La prise de focus est l’état renvoyé par un élément qui reçoit l’attention suite à une action de l’utilisateur. Il y a trois moyens en HTML de donner le focus à un élément :
- En activant l’élément par un dispositif de pointage (exemple : souris) ;
- En atteignant l’élément par la touche tabulation ou majuscule + tabulation ;
- En activant l’élément par un raccourci clavier (`accesskey`).
Certains éléments reçoivent naturellement le focus, par exemple : `<a href>`, `<area href>`, `<button>`, `<input>`, `<object>`, `<select>`, `<label>`, `<legend>`, `<optgroup>`, `<option>` et `<textarea>`. Le comportement de l’élément, lors de la prise de focus, dépend de sa nature ; un lien, par exemple, devra être activé après la prise de focus (sauf utilisation de script). En revanche, un élément de formulaire, comme `<textarea>`, devra autoriser la saisie suite à la prise de focus. Les éléments `<label>` et `<legend>` ne reçoivent la prise de focus que via le pointeur souris. Pour l’élément `<label>`, le comportement attendu est de transférer la prise de focus sur l’élément qui lui est associé.
Note 1 : la spécification WAI-ARIA étend le rôle attribué à l’attribut `tabindex` en définissant que tout élément HTML peut acquérir la possibilité de recevoir le focus en lui attribuant la valeur `tabindex="0"`. En revanche, aucun comportement n’est attribué via la seule présence de `tabindex`. De même, la valeur `tabindex="-1"` lorsqu’elle est utilisée sur un élément recevant naturellement le focus retire l’élément qui en est affecté du plan de tabulation en inhibant sa capacité à signaler la « prise de focus ». L’utilisation de `tabindex`, conformément à la spécification WAI-ARIA, peut valider certains tests relatifs à la gestion du focus de tabulation, notamment.
Note 2 : l’indication visuelle du focus du navigateur ne doit pas être supprimée ou dégradée sauf si un style du focus défini par l’auteur est visible et suffisamment contrasté au regard du critère 3.3.

### Procédé de rafraîchissement

Technique visant à modifier le contenu d’un ou de plusieurs éléments de la page web. Le procédé de rafraîchissement peut s’effectuer par rechargement automatique de la page ou de manière dynamique sans rechargement de la page (via AJAX, par exemple). L’utilisateur doit pouvoir contrôler chaque procédé de rafraîchissement de manière indépendante.

### Propriété CSS déterminant une couleur

Cela concerne les propriétés suivantes : `color`, `background-color`, `background`, `border-color`, `border`, `outline-color`, `outline`.
Note : l’utilisation d’une image de fond pour insérer une couleur (propriété `background:url…`) est également concernée.

### Raccourci clavier

Un moyen de déclencher une action associée à un composant de l’interface utilisateur en appuyant sur une ou plusieurs touches.
Note : les « Access keys » (attribut HTML `accesskey`) sont bien des raccourcis clavier, mais ils ne sont pas concernés par le critère 12.10 dans la mesure où leur activation nécessite déjà l’usage de touches de modification (variables suivant les navigateurs).

### Redirection

Procédé qui consiste pour l’affichage d’une page sur le poste client à rediriger l’utilisateur vers une autre page, sur le même domaine ou sur un domaine différent.

### Règles d’écriture

Le code source doit respecter les règles suivantes en accord avec la déclaration de type de document utilisée dans la page :
- Pas de balise ouvrante ou fermante sans `<` ou `>` (exemple d’erreur : `li>vélo`) ;
- pas de balise fermante avec `/` manquant (exemple d’erreur : `<li>vélo<li>`) ;
- pas de valeur d’attribut avec des `“` ou `‘` manquant (exemple d’erreur : `alt="vélo`) ;
- pas de valeurs multiples d’attribut séparées par un espace sans `“` ou `‘` (exemple d’erreur : `alt=mon beau vélo`) ;
- pas d’espace manquant entre les attributs (exemple : `alt=”vélo”title=”vélo”`) ;
- pas de balise fermante manquante pour les éléments qui en exigent une (exemple d’erreur : `<object>` sans `</object>`).

### Relâché ou relevé

Correspond aux gestionnaires d’événement JavaScript considérés comme des événements ascendants (`mouseup`, `touchend` par exemple).

### Résumé (de tableau)

Un résumé est un passage de texte associé à un tableau de données complexe. Il permet de donner des informations sur la nature et la structure du tableau afin d’en faciliter l’utilisation par les utilisateurs de technologies d’assistance par exemple.
Note : en HTML5, la seule technique utilisable actuellement est celle qui consiste à insérer le résumé directement dans le titre (balise `<caption>`) en masquant le résumé via CSS si nécessaire.
Dans les versions précédentes de HTML, le résumé peut être inséré via un attribut `summary` sur la balise `<table>`.
Dans le cas d’une balise avec l’attribut WAI-ARIA `role="table"`, le résumé doit être fourni au moyen d’un attribut `aria-describedby` et être correctement restitué par les technologies d’assistance.

### Script

Code généralement écrit sous forme d’une liste de commandes (par exemple JavaScript). Les langages interprétés côté client nécessitent un navigateur compatible sur lequel l’exécution du langage est active. Les commandes d’un langage de script côté client peuvent être embarquées ou contenues dans un fichier externe. Dans les deux cas, l’insertion se fait via la balise `<script>`.

### Sens de lecture

Indique le sens de lecture du document ou d’un passage de texte via l’attribut `dir`, `dir="ltr"`, par exemple. Les deux valeurs reconnues sont :
- `ltr` (left to right) indique un sens de lecture de gauche à droite ;
- `rtl` (right to left) indique un sens de lecture de droite à gauche.
Note : en l’absence d’indication de sens de lecture via l’attribut `dir` sur l’élément `html`, `body`, ou un des parents du texte analysé, le sens de lecture par défaut est de gauche à droite (valeur `ltr`).

### Site web

Ensemble de toutes les pages web :
- Reliées par des liens web ;
- Appartenant au même nom de domaine (ex : design.numerique.gouv.fr) ;
- Qui constituent un ensemble cohérent du point de vue de l’utilisateur.
Cas particulier des pages web d’un sous-domaine ; un sous-domaine peut :
- Soit appartenir au site web attaché au nom de domaine, si l’utilisateur en a une perception cohérente avec les autres pages du site web (par exemple : même structure, même navigation…) ;
- Soit ne pas appartenir au site web attaché au nom de domaine (par exemple : différents blogs en sous-domaine d’un nom de domaine et sans relation les uns avec les autres).

### Sous-titres synchronisés (objet multimédia)

Texte des informations audio (paroles d’un personnage, bruit important pour comprendre l’action…) présentes dans un média temporel et affiché de manière synchrone avec le flux de l’objet multimédia.
Note 1 : pour différencier les sources sonores (différents personnages, voix off…), il est recommandé d’utiliser un mécanisme approprié (mise entre crochets, mise en italique, annonce explicite du type “voix off : …”).
Note 2 : il ne faut pas confondre le sous-titrage pour la traduction (attribut `kind="subtitles"` de la balise `<track>` en HTML5, par exemple) et le sous-titrage pour sourds et malentendants (attribut `kind="captions"` de la balise `<track>` en HTML5, par exemple). Ces deux types de sous-titrage poursuivent des buts différents. Seule la présence et la pertinence d’un sous-titrage pour sourds et malentendants permet d’être conforme.

### Structure du document

Ensemble d’éléments permettant de définir les grandes zones d’une page HTML telles que la zone d’en-tête de la page, les zones de navigation principale et secondaire, la zone de contenu principal et la zone de pied de page.

### Système de navigation

Tout procédé permettant une navigation dans le site ou dans une page, les systèmes de navigation retenus sont :
- Menu de navigation principal ;
- Table des matières ;
- Plan du site ;
- Moteur de recherche.

### Tableau de données ayant un titre

Tableau de données ayant un attribut ou contenant une balise dont le contenu fait office de titre.
Tableau de données précédé ou suivi d’un passage de texte associé au tableau faisant office de titre.
Dans la mesure où il est bien correctement restitué et associé par les technologies d’assistance au tableau de données, le titre associé peut être :
- Dans une balise `<caption>` ;
- Dans un attribut `title` ;
- Dans un attribut WAI-ARIA `aria-label` ;
- Dans une balise associée au tableau de données via un attribut WAI-ARIA `aria-labelledby` sur le tableau.
Note : seule la balise `<caption>` étant complètement supporté par l’ensemble des technologies d’assistance, il est fortement recommandé de privilégier cette solution lors de la mise en œuvre afin d’éviter de nombreuses vérifications dans les différentes combinaisons prévues par l’environnement de test (ou « base de référence »).

### Tableau de données complexe

Un tableau de données est une structure introduite par une balise `<table>` ou lorsqu’il est correctement restitué par les technologies d’assistance par une balise pourvue d’un attribut WAI-ARIA `role="table"`.
Lorsqu’un tableau de données contient des en-têtes qui ne sont pas répartis uniquement sur la première ligne et/ou la première colonne de la grille ou dont la portée n’est pas valable pour l’ensemble de la colonne ou de la ligne, on parle de tableau de données complexe. Il est alors nécessaire de fournir un « résumé » permettant d’en expliquer sa nature et sa structure afin d’en faciliter la consultation pour des utilisateurs de technologies d’assistance par exemple.

### Tableau de données

Un tableau de données est une structure introduite par une balise `<table>` ou lorsqu’il est correctement restitué par les technologies d’assistance par une balise pourvue d’un attribut WAI-ARIA `role="table"`. Cette balise permet de structurer des informations en lignes et en colonnes via des cellules de données et des cellules d’en-têtes.

### Tableau de mise en forme

Technique qui utilise un élément HTML (balise `<table>`) pour contrôler l’affichage d’informations via des cellules (balise `<td>`).

### Taille des caractères

Valeur attribuée aux polices de caractères présentes sur une page web.

### Texte stylé

Texte dont la mise en forme est contrôlée par une feuille de styles.

### Titre de cadre

Contenu de l’attribut `title` de la balise `<iframe>` ou `<frame>` permettant de connaître la nature du contenu diffusé via le cadre lorsque l’utilisateur navigue de cadre en cadre ou affiche la liste des cadres de la page par exemple.
Note 1 : Certains cadres servent uniquement à des opérations techniques tels que des traitements applicatifs destinés à préparer ou piloter des contenus affichés dans la page comme les cadres utilisés par certains réseaux sociaux comme Facebook par exemple.
Si ces cadres sont dépourvus de titre de cadre fournis par le service distant, ou si les titres de cadres sont jugés non pertinents, des mentions génériques peuvent être utilisées, par exemple `title="contenus techniques Facebook"`.
Note 2 : Si cela ne gêne pas le fonctionnement de ce type de cadre, il est possible de les rendre indisponibles aux technologies d’assistance en utilisant l’attribut WAI-ARIA `aria-hidden="true"`. Dans ce cas le critère 2.1 et le critère 2.2 seront non applicables.

### Titre de page

Contenu de la balise `<title>` d’une page web permettant d’identifier de manière claire, concise et unique les contenus/la nature de la page (« Plan du site www.nomdusite.fr » pour une page présentant le plan du site web, par exemple).

### Titre

Élément HTML (balise `h`) à 6 niveaux de hiérarchie (de `h1` pour le titre le plus important à `h6` pour le moins important) ou élément HTML ayant les attributs WAI-ARIA `role="heading"` et `aria-level` permettant de structurer l’information d’un contenu web.
Assurer une stricte hiérarchie entre les titres d’une page web est une bonne pratique, mais la présence de sauts hiérarchiques n’invalide pas le critère tant que cette hiérarchie plus lâche reste cohérente (un titre `<h3>` peut ainsi venir directement après un titre `<h1>`, par exemple). La hiérarchie de titres ne doit pas obligatoirement contenir un titre `<h1>`. Même si ces pratiques ne sont pas encouragées, elles n’invalident pas le critère.
Note : les titres visuellement cachés via CSS sont considérés comme présents et valident le critère 9.1.

### Transcription textuelle (média temporel)

Contenu textuel associé à un média temporel par la technique appropriée (texte codé en HTML ou dans un fichier texte qui se trouve dans la même page ou consultable suivant un lien). Ce contenu donne accès à l’utilisateur (de manière indépendante de la consultation de l’objet multimédia) à :
- La totalité de ce qui y est exprimé oralement ;
- Toutes les informations descriptives nécessaires à une compréhension équivalente de l’action.
Ces informations textuelles doivent être présentées dans l’ordre chronologique de leur apparition dans le média temporel.
Note : la transcription textuelle doit se situer à l’extérieur de la balise `<object>`.

### Type de document

Ensemble de données de référence qui permet aux agents utilisateurs de connaître les caractéristiques techniques des langages utilisés sur la page web (balise `doctype`).

### Type et format de données

Indication concernant le type et le format des données attendus lors de la saisie d’un champ de formulaire. Par exemple :
- Date (jj/mm/aaaa) ;
- Montant en euros ;
- Code postal (5 chiffres : ex. 75001).
Note importante : lorsque le type de champ de formulaire propose un masque de saisie, par exemple les champs `date` ou `time`, l’indication de format n’est pas nécessaire.

### Uniquement à des fins de présentation

Uniquement à des fins de présentation : utilisation de balises HTML pour une finalité différente de celle prévue dans les spécifications (au regard du type de document déclaré). Exemples : utilisation des balises `h` à seule fin de créer un effet typographique ; utilisation de la balise `<blockquote>` à seule fin de mettre un paragraphe en retrait, etc.
Note 1 : l’utilisation d’éléments `<div>` ou `<span>` ou plusieurs `<br>` pour créer visuellement un paragraphe est considérée comme non conforme et invalide le critère.
Exemple : `<div>`, `paragraphes d’un bloc de texte simulés`, `<br>`, `à l’aide de plusieurs balises <br>`, `</div>`
Note 2 : WAI-ARIA propose un rôle `presentation` permettant de supprimer la sémantique d’un élément, par exemple `<h1 role="presentation">Titre</h1>`. Dans ce cas, le texte sera correctement restitué mais son rôle de titre ne le sera plus. L’utilisation du rôle `presentation` peut être requise lorsque l’on utilise un motif de conception WAI-ARIA.
Le rôle WAI-ARIA `presentation` peut être également utilisé pour supprimer la sémantique d’un élément lorsque ce dernier est utilisé uniquement à des fins de présentation, par exemple `<blockquote role="presentation">` aura le même effet qu’une absence d’élément `<blockquote>`.
Même si cette utilisation est fortement déconseillée (dans le cas de technologie d’assistance qui n’implémenteraient pas WAI-ARIA par exemple) elle peut être considérée comme conforme à WCAG. En revanche l’utilisation d’un rôle WAI-ARIA `presentation` sur un élément dont la nature (par exemple la sémantique) est essentielle à la compréhension du contenu est une violation des règles WCAG (particulièrement de l’échec F92) et invalide le critère.

### Version accessible (pour un document en téléchargement)

Les documents en téléchargement dont les types de format sont reconnus compatibles avec l’accessibilité doivent être rendus accessibles soit directement soit par l’intermédiaire d’une version accessible ou d’une version en HTML. Les formats de document dont la compatibilité est reconnue sont :
- Microsoft Office (Word 2003, OOXML) ;
- Open Office Org (ODF) ;
- Adobe PDF ;
- EPUB/Daisy.
Note : le format texte (txt) ne peut pas être utilisé pour produire une version accessible pour un document en téléchargement.

### Version alternative « audio seulement »

Une version « audio seulement » est une version sonore, sous la forme d’un simple fichier au format MP3 par exemple, utilisée comme alternative à une vidéo seulement (vidéo sans information sonore). Les seuls utilisateurs impactés par l’accessibilité étant les personnes aveugles, qui ne peuvent pas voir la vidéo, WCAG considère comme acceptable de proposer en alternative une version sonore.
La version « audio seulement » doit contenir toutes les informations visuelles importantes de la vidéo.
Généralement il est plus simple de produire une version sonore qu’une version textuelle lorsque la vidéo est très descriptive (la transcription textuelle nécessitant souvent un travail rédactionnel important). Il est rappelé, néanmoins, que seule la transcription textuelle assure un accès universel aux informations diffusées par la vidéo, dans le cas où un utilisateur ne serait pas en capacité de lancer la vidéo par exemple.

### Zone cliquable

Région d’une image réactive à laquelle une action a été associée ; par exemple, le déclenchement d’un événement en cliquant sur un lien (pour une zone cliquable côté client : balise `<area>` avec l’attribut `href`). Les balises `<area>` sont contenues dans la balise `<map>`.
Pour les images réactives côté serveur, les coordonnées sont détenues sur le serveur.

### Zone d’en-tête

Zone située en haut du document et contenant généralement le titre du document, un logo, un slogan…
Note : Attention à ne pas confondre cette zone d’en-tête, unique dans le site, avec tout contenu pouvant être balisé en HTML5 avec l’élément `<header>`.
Voir la définition technique fournie par WAI-ARIA : `Banner (role)`.

### Zone (d’une image réactive)

Zone cliquable ou zone non cliquable d’une image réactive côté client ou zone cliquable d’une image réactive côté serveur.

### Zone de contenu principal

Zone contenant les principaux contenus de la page, là où se trouvent les informations et fonctionnalités de fond (donc en dehors des menus, de la recherche ou des zones secondaires de publicités, actualités connexes…).
Note : Cette zone est unique dans la page. Elle peut être difficile à déterminer sur certaines pages particulières, comme la page d’accueil.
Voir la définition technique fournie par WAI-ARIA : `Main (role)`.

### Zone de pied de page

Il s’agit des informations concernant le fonctionnement du site ou les informations légales. On y trouve par exemple les mentions légales, les crédits, les conditions d’utilisation, le plan du site et éventuellement la page accessibilité.
Note : Attention à ne pas confondre cette zone de pied de page, unique dans le site, avec tout contenu pouvant être balisé en HTML5 avec l’élément `<footer>`.
Voir la définition technique fournie par WAI-ARIA : `Contentinfo (role)`.

### Zone non cliquable

Région d’une image réactive à laquelle aucune action n’est associée. Une zone non cliquable côté client est contenue dans une balise `<area>` :
- Avec l’attribut `nohref` lorsque le code HTML de la page n’est pas du HTML5 ;
- Sans attribut `href` en HTML5.
Les balises `<area>` sont contenus dans la balise `<map>`.
