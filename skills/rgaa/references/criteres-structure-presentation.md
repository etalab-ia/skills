# RGAA — Thèmes 8 à 10 : Éléments obligatoires, Structure, Présentation

## Thème 8 — Éléments obligatoires (10 critères)

### 8.1 Doctype présent et valide

**Texte officiel 8.1 :** Chaque page web est-elle définie par un *type de document* ?
- **8.1.1** Pour chaque page web, le *type de document* (balise `doctype`) est-il présent ?
- **8.1.2** Pour chaque page web, le *type de document* (balise `doctype`) est-il valide ?
- **8.1.3** Pour chaque page web possédant une déclaration de *type de document*, celle-ci est-elle située avant la balise `<html>` dans le code source ?

**Non-conformité type :** DOCTYPE absent, malformé (`<!DOCTYPE>`), ou placé après la balise `<html>`.
**Impact :** sans type de document valide, le navigateur passe en mode de compatibilité : l’affichage et la restitution par les aides techniques deviennent imprévisibles.
**Priorité :** 🟠 Majeur

---

### 8.2 Code source valide

**Texte officiel 8.2 :** Pour chaque page web, le code source généré est-il valide selon le *type de document* spécifié ?
- **8.2.1** Pour chaque déclaration de *type de document*, le code source généré de la page vérifie-t-il ces conditions ?
  - Les balises, attributs et valeurs d’attributs respectent les *règles d’écriture* ;
  - L’imbrication des balises est conforme ;
  - L’ouverture et la fermeture des balises sont conformes ;
  - Les valeurs d’attribut id sont uniques dans la page ;
  - Les attributs ne sont pas doublés sur un même élément.

- Balises correctement imbriquées et fermées
- Attributs `id` uniques dans la page
- Pas d'attributs dupliqués sur un même élément
- Valeurs d'attributs entre guillemets

**Non-conformité type :** Deux éléments avec le même `id` dans la page ; balises non fermées.
**Impact :** un `id` en double casse les relations `for`, `aria-describedby` ou `aria-labelledby` : le lecteur d’écran annonce le mauvais texte, ou rien.
**Priorité :** 🟠 Majeur

---

### 8.3–8.4 Langue par défaut présente et pertinente

**Texte officiel 8.3 :** Dans chaque page web, la *langue par défaut* est-elle présente ?
- **8.3.1** Pour chaque page web, l’indication de langue par défaut vérifie-t-elle une de ces conditions ?
  - L’indication de la langue de la page (attribut `lang` et/ou `xml:lang`) est donnée pour l’élément `html` ;
  - L’indication de la langue de la page (attribut `lang` et/ou `xml:lang`) est donnée sur chaque élément de texte ou sur l’un des éléments parents.

**Texte officiel 8.4 :** Pour chaque page web ayant une *langue par défaut*, le *code de langue* est-il pertinent ?
- **8.4.1** Pour chaque page web ayant une langue par défaut, le code de langue vérifie-t-il ces conditions ?
  - Le code de langue est valide ;
  - Le code de langue est pertinent.

8.3 : la langue est indiquée. 8.4 : son code est valide et correspond à la langue de la page.

**Non-conformité type :** `<html>` sans `lang` ; `lang="français"` au lieu de `lang="fr"`.
**Impact :** sans langue déclarée, la synthèse vocale peut lire le français avec la prononciation d’une autre langue : le texte devient incompréhensible.
**Priorité :** 🔴 Bloquant

---

### 8.5–8.6 Titre de page présent et pertinent

**Texte officiel 8.5 :** Chaque page web a-t-elle un *titre de page* ?
- **8.5.1** Chaque page web a-t-elle un *titre de page* (balise `<title>`) ?

**Texte officiel 8.6 :** Pour chaque page web ayant un *titre de page*, ce titre est-il pertinent ?
- **8.6.1** Pour chaque page web ayant un *titre de page* (balise `<title>`), le contenu de cette balise est-il pertinent ?

8.5 : la balise existe et n’est pas vide. 8.6 : son contenu identifie la page.

**Non-conformité type :** `<title>` absent ; `<title>Index</title>` ou `<title>Page</title>` non descriptif ; même `<title>` sur toutes les pages.
**Impact :** le titre est la première chose annoncée au lecteur d’écran : sans lui, la personne ne sait pas sur quelle page elle arrive, ni à quoi correspond chaque onglet ouvert.
**Priorité :** 🔴 Bloquant

---

### 8.7–8.8 Changements de langue indiqués et pertinents

**Texte officiel 8.7 :** Dans chaque page web, chaque *changement de langue* est-il indiqué dans le code source (hors cas particuliers) ?
- **8.7.1** Dans chaque page web, chaque texte écrit dans une langue différente de la *langue par défaut* vérifie-t-il une de ces conditions (hors cas particuliers) ?
  - L’indication de langue est donnée sur l’élément contenant le texte (attribut `lang` et/ou `xml:lang`) ;
  - L’indication de langue est donnée sur un des éléments parents (attribut `lang` et/ou `xml:lang`)
- *Cas particuliers :*
  - Il y a une gestion de cas particuliers sur le changement de langue pour les cas suivants :
    - - Nom propre, le critère est non applicable ;
    - - Nom commun de langue étrangère présent dans le dictionnaire officiel de la langue (voir note 1 ci-dessous) par défaut de la page web, le critère est non applicable ;
    - - Le terme de langue étrangère soumis, via un *champ de formulaire* et rappelé dans la page (par exemple comme indication du terme recherché dans le cas d’un moteur de recherche), le critère est non applicable ;
    - - Passage de texte dont la langue ne peut pas être déterminée : le critère est non applicable ;
    - - Terme ou passage de texte issus d’une langue morte ou imaginaire pour laquelle il n’existe pas d’interprétation vocale : le critère est non applicable.
  - Note 1 : le dictionnaire officiel est celui recommandé par l’académie en charge de la langue en question. Pour la France, par exemple, le lien vers le dictionnaire officiel se trouve sur le site de l’Académie française à l’adresse suivante : http://www.academie-francaise.fr/le-dictionnaire/la-9e-edition. Pour toute demande auprès du service du dictionnaire de l’Académie française, utiliser le formulaire de contact du service du dictionnaire.
  - Note 2 : pour les noms communs de langue étrangère, absents dans le dictionnaire officiel de la langue par défaut de la page web, et qui sont passés dans le langage commun (exemple : newsletter) : le critère est applicable, uniquement lorsque l’absence d’indication de langue peut provoquer une incompréhension pour la restitution.

**Texte officiel 8.8 :** Dans chaque page web, le code de langue de chaque *changement de langue* est-il valide et pertinent ?
- **8.8.1** Pour chaque page web, le code de langue de chaque *changement de langue* vérifie-t-il ces conditions ?
  - Le code de langue est valide ;
  - Le code de langue est pertinent.

8.7 : le changement de langue est indiqué. 8.8 : son code est valide et correspond à la langue du passage.

**Non-conformité type :** Citation ou terme en anglais sans `lang="en"` ; `lang` avec une valeur incorrecte.
**Impact :** sans indication, la synthèse vocale lit le passage avec la prononciation du français : il devient difficile à comprendre.
**Priorité :** 🟡 Mineur

---

### 8.9 Balises non utilisées uniquement à des fins de présentation

**Texte officiel 8.9 :** Dans chaque page web, les balises ne doivent pas être utilisées *uniquement à des fins de présentation*. Cette règle est-elle respectée ?
- **8.9.1** Dans chaque page web les balises (à l’exception de `<div>`, `<span>` et `<table>`) ne doivent pas être utilisées *uniquement à des fins de présentation*. Cette règle est-elle respectée ?

**Non-conformité type :** `<h3>` utilisé pour augmenter la taille d'un texte sans signification de titre ; `<blockquote>` pour indenter visuellement.
**Impact :** une balise détournée annonce au lecteur d’écran une structure qui n’existe pas : un faux titre, par exemple, brouille la navigation par titres.
**Priorité :** 🟠 Majeur

---

### 8.10 Sens de lecture signalé

**Texte officiel 8.10 :** Dans chaque page web, les changements du *sens de lecture* sont-ils signalés ?
- **8.10.1** Dans chaque page web, chaque texte dont le sens de lecture est différent du *sens de lecture* par défaut est contenu dans une balise possédant un attribut `dir` ?
- **8.10.2** Dans chaque page web, chaque changement du *sens de lecture* (attribut `dir`) vérifie-t-il ces conditions ?
  - La valeur de l’attribut `dir` est conforme (`rtl` ou `ltr`) ;
  - La valeur de l’attribut `dir` est pertinente.

**Non-conformité type :** Texte arabe affiché sans `dir="rtl"` entraînant un affichage incorrect.
**Impact :** sans `dir`, un texte écrit de droite à gauche s’affiche et se lit dans le désordre, notamment autour de la ponctuation et des chiffres.
**Priorité :** 🟡 Mineur

---

## Thème 9 — Structuration de l'information (4 critères)

### 9.1 Hiérarchie des titres pertinente

**Texte officiel 9.1 :** Dans chaque page web, l’information est-elle structurée par l’utilisation appropriée de *titres* ?
- **9.1.1** Dans chaque page web, la hiérarchie entre les *titres* (balise `<hx>` ou balise possédant un attribut WAI-ARIA `role="heading"` associé à un attribut WAI-ARIA `aria-level`) est-elle pertinente ?
- **9.1.2** Dans chaque page web, le contenu de chaque *titre* (balise `<hx>` ou balise possédant un attribut WAI-ARIA `role="heading"` associé à un attribut WAI-ARIA `aria-level`) est-il pertinent ?
- **9.1.3** Dans chaque page web, chaque passage de texte constituant un *titre* est-il structuré à l’aide d’une balise `<hx>` ou d’une balise possédant un attribut WAI-ARIA `role="heading"` associé à un attribut WAI-ARIA `aria-level` ?
- *Notes techniques :*
  - WAI-ARIA permet de définir des titres via le rôle `heading` et l’attribut `aria-level` (indication du niveau de titre). Bien qu’il soit préférable d’utiliser l’élément de titre natif en HTML `<hx>`, l’utilisation du rôle WAI-ARIA `heading` est compatible avec l’accessibilité.

- Utiliser `<h1>` à `<h6>` dans l'ordre hiérarchique
- Un seul `<h1>` par page (bonne pratique)
- Pas de saut de niveau (h1 → h3 sans h2)
- Le contenu de chaque titre doit être pertinent
- Tout passage qui joue le rôle de titre doit être balisé comme tel

**Non-conformité type :** `<h1>` suivi directement d'un `<h3>` ; titre visuel en `<div>` stylée, sans balise de titre.
**Impact :** la navigation par titres est le principal moyen de survoler une page au lecteur d’écran : sans hiérarchie fiable, la personne qui l’utilise perd ce repère.
**Priorité :** 🟠 Majeur

---

### 9.2 Structure du document cohérente

**Texte officiel 9.2 :** Dans chaque page web, la *structure du document* est-elle cohérente (hors cas particuliers) ?
- **9.2.1** Dans chaque page web, la *structure du document* vérifie-t-elle ces conditions (hors cas particuliers) ?
  - La *zone d’en-tête de la page* est structurée via une balise `<header>` ;
  - Les *zones de navigation principales et secondaires* sont structurées via une balise `<nav>` ;
  - La balise `<nav>` est réservée à la structuration des *zones de navigation principales et secondaires* ;
  - La *zone de contenu principal* est structurée via une balise `<main>` ;
  - La *structure du document* utilise une balise `<main>` visible unique ;
  - La *zone de pied de page* est structurée via une balise `<footer>`.
- *Cas particuliers :*
  - Lorsque le doctype déclaré dans la page n’est pas le doctype HTML5, ce critère est non applicable.
- *Notes techniques :*
  - La balise `<main>` peut être utilisée plusieurs fois dans le même document HTML. Néanmoins, il ne peut y avoir en permanence qu’une seule balise visible et lisible par les technologies d’assistances, les autres devant disposer d’un attribut `hidden` ou d’un style permettant de les masquer aux technologies d’assistances. À noter cependant que l’utilisation d’un style seul restera insuffisante pour assurer l’unicité d’une balise `<main>` visible en cas de désactivation des feuilles de styles.

**Non-conformité type :** Absence de `<main>` ; plusieurs `<main>` visibles ; `<nav>` utilisé pour tout groupe de liens, ou rendu vide.
**Impact :** sans ces zones, la personne qui utilise un lecteur d’écran ne peut pas sauter directement au contenu principal ou à la navigation.
**Priorité :** 🟠 Majeur

---

### 9.3 Listes correctement structurées

**Texte officiel 9.3 :** Dans chaque page web, chaque *liste* est-elle correctement structurée ?
- **9.3.1** Dans chaque page web, les informations regroupées visuellement sous forme de *liste* non ordonnée vérifient-elles une de ces conditions ?
  - La liste utilise les balises HTML `<ul>` et `<li>` ;
  - La liste utilise les attributs WAI-ARIA `role="list"` et `role="listitem"`.
- **9.3.2** Dans chaque page web, les informations regroupées visuellement sous forme de *liste* ordonnée vérifient-elles une de ces conditions ?
  - La liste utilise les balises HTML `<ol>` et `<li>` ;
  - La liste utilise les attributs WAI-ARIA `role="list"` et `role="listitem"`.
- **9.3.3** Dans chaque page web, les informations regroupées sous forme de *liste* de description utilisent-elles les balises `<dl>` et `<dt>/<dd>` ?
- *Notes techniques :*
  - Les attributs WAI-ARIA `role="list"` et `role="listitem"` peuvent nécessiter l’utilisation des attributs WAI-ARIA `aria-setsize` et `aria-posinset` dans le cas où l’ensemble de la liste n’est pas disponible via le DOM généré au moment de la consultation.
  - Les attributs WAI-ARIA `role="tree"`, `role="tablist"`, `role="menu"`, `role="combobox"` et `role="listbox"` ne sont pas équivalents à une liste HTML `<ul>` ou `<ol>`.

**Non-conformité type :** Liste de liens en navigation codée avec des `<div>` au lieu de `<ul><li>` ; liste ordonnée codée en `<ul>`.
**Impact :** sans balisage de liste, le lecteur d’écran n’annonce ni le début de la liste ni le nombre d’éléments : la personne ne peut pas estimer son contenu ni la passer.
**Priorité :** 🟡 Mineur

---

### 9.4 Citations correctement indiquées

**Texte officiel 9.4 :** Dans chaque page web, chaque citation est-elle correctement indiquée ?
- **9.4.1** Dans chaque page web, chaque citation courte utilise-t-elle une balise `<q>` ?
- **9.4.2** Dans chaque page web, chaque bloc de citation utilise-t-il une balise `<blockquote>` ?

**Non-conformité type :** Citation longue dans un `<p>` stylé en italique sans `<blockquote>`.
**Impact :** une citation non balisée se lit comme le reste du texte : la personne qui utilise un lecteur d’écran ne sait pas que ces mots viennent d’une autre source.
**Priorité :** 🟡 Mineur

---

## Thème 10 — Présentation de l'information (14 critères)

### 10.1 Présentation contrôlée par CSS

**Texte officiel 10.1 :** Dans le site web, des *feuilles de styles* sont-elles utilisées pour contrôler la *présentation de l’information* ?
- **10.1.1** Dans chaque page web, les balises servant à la *présentation de l’information* ne doivent pas être présentes dans le code source généré des pages. Cette règle est-elle respectée ?
- **10.1.2** Dans chaque page web, les attributs servant à la *présentation de l’information* ne doivent pas être présents dans le code source généré des pages. Cette règle est-elle respectée ?
- **10.1.3** Dans chaque page web, l’utilisation des espaces vérifie-t-elle ces conditions ?
  - Les espaces ne sont pas utilisées pour séparer les lettres d’un mot ;
  - Les espaces ne sont pas utilisées pour simuler des tableaux ;
  - Les espaces ne sont pas utilisées pour simuler des colonnes de texte.

**Non-conformité type :** `<font color="red">texte</font>` ; `<td align="center">`.
**Impact :** une présentation écrite dans le HTML résiste aux feuilles de style personnelles : la personne qui adapte l’affichage (couleurs, contraste, police) ne peut pas la modifier.
**Priorité :** 🟡 Mineur

---

### 10.2–10.3 Contenu présent et compréhensible sans CSS

**Texte officiel 10.2 :** Dans chaque page web, le *contenu visible* porteur d’information reste-t-il présent lorsque les *feuilles de styles* sont désactivées ?
- **10.2.1** Dans chaque page web, l’information reste-t-elle présente lorsque les *feuilles de styles* sont désactivées ?

**Texte officiel 10.3 :** Dans chaque page web, l’information reste-t-elle *compréhensible* lorsque les *feuilles de styles* sont désactivées ?
- **10.3.1** Dans chaque page web, l’information reste-t-elle *compréhensible* lorsque les *feuilles de styles* sont désactivées ?

10.2 : l’information reste présente sans feuille de style. 10.3 : l’ordre de lecture reste compréhensible.

**Non-conformité type :** Icône informative affichée uniquement via `background-image` CSS ; texte généré uniquement via `::before`.
**Impact :** un contenu porté par le seul CSS disparaît pour la personne qui remplace ou désactive les styles, et n’est pas toujours restitué au lecteur d’écran.
**Priorité :** 🟠 Majeur

---

### 10.4 Texte lisible à 200% de zoom

**Texte officiel 10.4 :** Dans chaque page web, le texte reste-t-il lisible lorsque la *taille des caractères* est augmentée jusqu’à 200 %, au moins (hors cas particuliers) ?
- **10.4.1** Dans chaque page web, l’augmentation de la *taille des caractères* jusqu’à 200 %, au moins, ne doit pas provoquer de perte d’information. Cette règle est-elle respectée selon une de ces conditions (hors cas particuliers) ?
  - Lors de l’utilisation de la fonction d’agrandissement du texte du navigateur ;
  - Lors de l’utilisation des fonctions de zoom graphique du navigateur ;
  - Lors de l’utilisation d’un *composant d’interface* propre au site permettant d’agrandir le texte ou de zoomer.
- **10.4.2** Dans chaque page web, l’augmentation de la taille des caractères jusqu’à 200 %, au moins, doit être possible pour l’ensemble du texte dans la page. Cette règle est-elle respectée selon une de ces conditions (hors cas particuliers) ?
  - Lors de l’utilisation de la fonction d’agrandissement du texte du navigateur ;
  - Lors de l’utilisation des fonctions de zoom graphique du navigateur ;
  - Lors de l’utilisation d’un *composant d’interface* propre au site permettant d’agrandir le texte ou de zoomer.
- *Cas particuliers :*
  - Font exception à ce critère, les contenus pour lesquels l’utilisateur n’a pas de possibilité de personnalisation :
    - - Les sous-titres incrustés dans une vidéo ;
    - - Les textes en image ;
    - - Le texte au sein d’une balise `<canvas>`.

**Non-conformité type :** Texte tronqué ou contenu caché à 200% de zoom ; boutons dont le texte déborde du conteneur.
**Impact :** contenus coupés ou superposés : une partie de la page devient inaccessible à la personne malvoyante qui agrandit le texte.
**Priorité :** 🟠 Majeur

---

### 10.5 Couleurs de fond et de texte couplées

**Texte officiel 10.5 :** Dans chaque page web, les déclarations CSS de couleurs de fond d’élément et de police sont-elles correctement utilisées ?
- **10.5.1** Dans chaque page web, chaque déclaration CSS de couleurs de police (`color`), d’un élément susceptible de contenir du texte, est-elle accompagnée d’une déclaration de couleur de fond (`background`, `background-color`), au moins, héritée d’un parent ?
- **10.5.2** Dans chaque page web, chaque déclaration de couleur de fond (`background`, `background-color`), d’un élément susceptible de contenir du texte, est-elle accompagnée d’une déclaration de couleur de police (`color`) au moins, héritée d’un parent ?
- **10.5.3** Dans chaque page web, chaque utilisation d’une image pour créer une couleur de fond d’un élément susceptible de contenir du texte, via CSS (`background`, `background-image`), est-elle accompagnée d’une déclaration de couleur de fond (`background`, `background-color`), au moins, héritée d’un parent ?

Une déclaration `color` s’accompagne d’une couleur de fond, et inversement, au moins héritée d’un parent. Le test officiel porte sur la valeur calculée : si le parent n’est pas dans le code audité, le code seul ne permet pas de conclure.

**Non-conformité type :** `.texte-blanc { color: white; }` sans `background-color` défini, ni sur l’élément ni sur un parent, rendant le texte illisible selon le fond de l'utilisateur.
**Impact :** si seule une des deux couleurs est déclarée, la personne qui impose ses propres couleurs peut obtenir un texte illisible, par exemple blanc sur blanc.
**Priorité :** 🟠 Majeur

---

### 10.6 Liens visibles par rapport au texte

**Texte officiel 10.6 :** Dans chaque page web, chaque *lien dont la nature n’est pas évidente* est-il visible par rapport au texte environnant ?
- **10.6.1** Dans chaque page web, chaque *lien texte* signalé uniquement par la couleur, et dont la nature n’est pas évidente, vérifie-t-il ces conditions ?
  - La couleur du lien a un rapport de *contraste* supérieur ou égal à 3:1 par rapport au texte environnant ;
  - Le lien dispose d’une indication visuelle au survol autre qu’un changement de couleur ;
  - Le lien dispose d’une indication visuelle au focus autre qu’un changement de couleur.

**Non-conformité type :** Lien dans un paragraphe différencié uniquement par une couleur peu contrastée, sans soulignement ni au survol ni au focus.
**Impact :** un lien signalé par sa seule couleur ne se repère pas dans le paragraphe pour la personne qui distingue mal les couleurs.
**Priorité :** 🟠 Majeur

---

### 10.7 Focus visible

**Texte officiel 10.7 :** Dans chaque page web, pour chaque élément recevant le focus, la *prise de focus* est-elle visible ?
- **10.7.1** Pour chaque élément recevant le focus, la *prise de focus* vérifie-t-elle une de ces conditions ?
  - Le style du focus natif du navigateur n’est pas supprimé ou dégradé ;
  - Un style du focus défini par l’auteur est visible.

**Non-conformité type :** `*:focus { outline: none; }` dans le CSS sans focus personnalisé de remplacement.
**Impact :** sans focus visible, la personne qui navigue au clavier ne sait pas où elle se trouve dans la page.
**Priorité :** 🔴 Bloquant

---

### 10.8 Contenus cachés correctement gérés

**Texte officiel 10.8 :** Pour chaque page web, les *contenus cachés* ont-ils vocation à être ignorés par les technologies d’assistance ?
- **10.8.1** Dans chaque page web, chaque contenu caché vérifie-t-il une de ces conditions ?
  - Le *contenu caché* a vocation à être ignoré par les technologies d’assistance ;
  - Le *contenu caché* n’a pas vocation à être ignoré par les technologies d’assistance et est rendu restituable par les technologies d’assistance suite à une action de l’utilisateur réalisable au clavier ou par tout dispositif de pointage sur un élément précédent le contenu caché ou suite à un repositionnement du focus dessus.
- *Notes techniques :*
  - WAI-ARIA propose un attribut `aria-hidden` (`true` ou `false`) qui permet d’inhiber la restitution d’un contenu en direction des technologies d’assistance, sans action sur sa visibilité en direction des agents utilisateurs : un contenu avec `aria-hidden="true"` ne sera donc plus vocalisable, mais restera visible.
  - Sauf si le contenu contrôlé par `aria-hidden` n’a pas vocation à être restitué par les technologies d’assistance, la valeur de l’attribut `aria-hidden` doit être cohérente avec l’état affiché ou masqué du contenu à l’écran.
  - La spécification HTML5 propose un attribut `hidden` qui permet de rendre indisponible (quand l’attribut `hidden` est présent) un contenu dans le DOM généré (de manière similaire au `type="hidden"` sur un contrôle de formulaire).
  - Il est possible d’avoir des situations où un contenu contrôlé par `hidden` ou `aria-hidden` se trouve momentanément dans un état incohérent avec le statut affiché ou masqué du contenu, par exemple si l’on désire rendre disponible un élément, mais que son affichage à l’écran reste dépendant d’une action ultérieure. Dans ce cas, c’est l’état final du contenu qui doit être considéré.

Un contenu caché doit soit avoir vocation à être ignoré par les aides techniques, soit leur devenir accessible après une action au clavier ou au pointeur, ou après un déplacement du focus.

**Non-conformité type :** Texte alternatif pour icône caché avec `display:none` (inaccessible aux lecteurs d'écran) ; `aria-hidden="true"` sur un élément focalisable ou porteur d’information.
**Impact :** un contenu mal caché est soit perdu pour le lecteur d’écran, soit annoncé alors qu’il ne devrait pas l’être : avec `aria-hidden` sur un élément focalisable, le focus se pose sur un élément muet.
**Priorité :** 🟠 Majeur

---

### 10.9–10.10 Information pas uniquement par forme, taille ou position

**Texte officiel 10.9 :** Dans chaque page web, l’information ne doit pas être donnée uniquement *par la forme, taille ou position*. Cette règle est-elle respectée ?
- **10.9.1** Dans chaque page web, pour chaque texte ou ensemble de textes, l’information ne doit pas être donnée uniquement *par la forme, taille ou position*. Cette règle est-elle respectée ?
- **10.9.2** Dans chaque page web, pour chaque image ou ensemble d’images, l’information ne doit pas être donnée uniquement *par la forme, taille ou position*. Cette règle est-elle respectée ?
- **10.9.3** Dans chaque page web, pour chaque *média temporel*, l’information ne doit pas être donnée uniquement *par la forme, taille ou position*. Cette règle est-elle respectée ?
- **10.9.4** Dans chaque page web, pour chaque *média non temporel*, l’information ne doit pas être donnée uniquement *par la forme, taille ou position*. Cette règle est-elle respectée ?

**Texte officiel 10.10 :** Dans chaque page web, l’information ne doit pas être donnée *par la forme, taille ou position* uniquement. Cette règle est-elle implémentée de façon pertinente ?

10.9 : l’information a un autre moyen d’être récupérée. 10.10 : ce moyen transmet la même information.

**Non-conformité type :** Instructions "Cliquez sur le bouton rond" sans autre identification ; page active du menu signalée par un simple trait sous le lien, sans `aria-current`.
**Impact :** la personne qui ne voit pas la page ou la consulte en fort zoom ne perçoit ni la forme ni la position : la consigne ou l’état lui échappe.
**Priorité :** 🟠 Majeur

---

### 10.11 Reflow : pas de scroll horizontal à 320px / vertical à 256px

**Texte officiel 10.11 :** Pour chaque page web, les contenus peuvent-ils être présentés sans perte d’information ou de fonctionnalité et sans avoir recours soit à un défilement vertical pour une fenêtre ayant une hauteur de 256 px, soit à un défilement horizontal pour une fenêtre ayant une largeur de 320 px (hors cas particuliers) ?
- **10.11.1** Pour chaque page web, lorsque le contenu dont le sens de lecture est horizontal est affiché dans une fenêtre réduite à une largeur de 320 px, l’ensemble des informations et des fonctionnalités sont-elles disponibles sans aucun défilement horizontal (hors cas particuliers) ?
- **10.11.2** Pour chaque page web, lorsque le contenu dont le sens de lecture est vertical est affiché dans une fenêtre réduite à une hauteur de 256 px, l’ensemble des informations et des fonctionnalités sont-elles disponibles sans aucun défilement vertical (hors cas particuliers) ?
- *Cas particuliers :*
  - L'objectif de ce critère est de garantir un défilement dans une unique direction pour une lecture facilitée selon le sens de l'écriture.
  - Font exception à ce critère, les contenus dont l'agencement requiert deux dimensions pour être compris ou utilisés comme :
    - - Les images, les graphiques ou les vidéos ;
    - - Les jeux (jeux de plateforme, par exemple) ;
    - - Les présentations (type diaporama, par exemple) ;
    - - Les tableaux de données ;
    - - Les interfaces où il est nécessaire d'avoir un ascenseur horizontal lors de la manipulation de l'interface.
  - Note : la majorité des navigateurs sur les systèmes d'exploitation sur mobile (Android, iOS) ne gère pas correctement la redistribution en cas de zoom. Dans ce contexte, le critère sera considéré comme non applicable sur ces environnements.
- *Notes techniques :*
  - Lorsqu'il est ici question de pixel, il s'agit du pixel CSS tel que défini par le W3C https://www.w3.org/TR/css3-values/

**Non-conformité type :** Barre de navigation horizontale qui déborde à 320px.
**Impact :** à fort zoom, la personne malvoyante doit faire défiler la page dans les deux sens à chaque ligne, et perd facilement le fil.
**Priorité :** 🟠 Majeur

---

### 10.12 Espacement du texte modifiable

**Texte officiel 10.12 :** Dans chaque page web, les propriétés d’espacement du texte peuvent-elles être redéfinies par l’utilisateur sans perte de contenu ou de fonctionnalité (hors cas particuliers) ?
- **10.12.1** Dans chaque page web, le texte reste-t-il lisible lorsque l’affichage est modifié selon ces conditions (hors cas particuliers) ?
  - L’espacement entre les lignes (`line-height`) est augmenté jusqu’à 1,5 fois la taille de la police ;
  - L’espacement suivant les paragraphes (balise `<p>`) est augmenté jusqu’à 2 fois la taille de la police ;
  - L’espacement des lettres (`letter-spacing`) est augmenté jusqu’à 0,12 fois la taille de la police ;
  - L’espacement des mots (`word-spacing`) est augmenté jusqu’à 0,16 fois la taille de la police.
- *Cas particuliers :*
  - Font exception à ce critère, les contenus pour lesquels l’utilisateur n’a pas de possibilité de personnalisation :
    - - Les sous-titres directement intégrés à une vidéo ;
    - - Les images texte ;
    - - Le texte au sein d’une balise `<canvas>`.

**Non-conformité type :** Conteneur avec hauteur fixe en pixels qui tronque le texte quand l'interligne augmente.
**Impact :** la personne qui augmente l’espacement pour mieux lire, notamment en cas de dyslexie, voit son texte coupé ou superposé.
**Priorité :** 🟠 Majeur

---

### 10.13 Contenus additionnels (tooltips) contrôlables

**Texte officiel 10.13 :** Dans chaque page web, les contenus additionnels apparaissant à la prise de focus ou au survol d’un *composant d’interface* sont-ils contrôlables par l’utilisateur (hors cas particuliers) ?
- **10.13.1** Chaque contenu additionnel devenant visible à la prise de focus ou au survol d’un *composant d’interface* peut-il être masqué par une action de l’utilisateur sans déplacer le focus ou le pointeur de la souris (hors cas particuliers) ?
- **10.13.2** Chaque contenu additionnel qui apparait au survol d’un *composant d’interface* peut-il être survolé par le pointeur de la souris sans disparaître (hors cas particuliers) ?
- **10.13.3** Chaque contenu additionnel qui apparaît à la prise de focus ou au survol d’un *composant d’interface* vérifie-t-il une de ces conditions (hors cas particuliers) ?
  - Le contenu additionnel reste visible jusqu’à ce que l’utilisateur retire le pointeur souris ou le focus du contenu additionnel et du *composant d’interface* ayant déclenché son apparition ;
  - Le contenu additionnel reste visible jusqu’à ce que l’utilisateur déclenche une action masquant ce contenu sans déplacer le focus ou le pointeur de la souris du *composant d’interface* ayant déclenché son apparition ;
  - Le contenu additionnel reste visible jusqu’à ce qu’il ne soit plus valide.
- *Cas particuliers :*
  - Lorsque le contenu additionnel est contrôlé par l’agent utilisateur (par exemple, attribut `title` ou validation native de formulaire) ou correspond à une fenêtre modale conforme au *motif de conception* WAI-ARIA `dialog`, le critère 10.13 est non applicable.
  - Lorsque le contenu additionnel ne masque ou ne remplace aucun contenu porteur d’information, le test 10.13.1 est non applicable.

**Non-conformité type :** Tooltip disparaissant immédiatement quand la souris le survole ; tooltip ne pouvant pas être fermé par Échap.
**Impact :** une infobulle qu’on ne peut pas fermer masque le contenu voisin pour la personne qui zoome ; une infobulle qui disparaît au survol ne peut pas être lue à son rythme.
**Priorité :** 🟠 Majeur

---

### 10.14 Contenus CSS additionnels accessibles au clavier

**Texte officiel 10.14 :** Dans chaque page web, les contenus additionnels apparaissant via les styles CSS uniquement peuvent-ils être rendus visibles au clavier et par tout dispositif de pointage ?
- **10.14.1** Dans chaque page web, les contenus additionnels apparaissant au survol d’un *composant d’interface* via les styles CSS respectent-ils si nécessaire une de ces conditions ?
  - Les contenus additionnels apparaissent également à l’activation du composant via le clavier et tout dispositif de pointage ;
  - Les contenus additionnels apparaissent également à la prise de focus du composant ;
  - Les contenus additionnels apparaissent également par le biais de l’activation ou de la prise de focus d’un autre composant.
- **10.14.2** Dans chaque page web, les contenus additionnels apparaissant au focus d’un *composant d’interface* via les styles CSS respectent-ils si nécessaire une de ces conditions ?
  - Les contenus additionnels apparaissent également à l’activation du composant via le clavier et tout dispositif de pointage ;
  - Les contenus additionnels apparaissent également au survol du composant ;
  - Les contenus additionnels apparaissent également par le biais de l’activation ou du survol d’un autre composant.

**Non-conformité type :** Menu déroulant qui s'ouvre au `:hover` CSS mais pas au focus clavier.
**Impact :** un contenu affiché seulement au survol reste hors d’atteinte pour la personne qui navigue au clavier.
**Priorité :** 🔴 Bloquant

