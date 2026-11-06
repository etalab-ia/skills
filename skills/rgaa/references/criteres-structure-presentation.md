# RGAA — Thèmes 8 à 10 : Éléments obligatoires, Structure, Présentation

## Thème 8 — Éléments obligatoires (10 critères)

### 8.1 Doctype présent et valide

**Test :** Vérifier que `<!DOCTYPE html>` est présent en première ligne du document HTML, avant la balise `<html>`.
**Non-conformité type :** DOCTYPE absent, malformé (`<!DOCTYPE>`), ou placé après la balise `<html>`.
**Impact :** sans type de document valide, le navigateur passe en mode de compatibilité : l’affichage et la restitution par les aides techniques deviennent imprévisibles.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```html
<!-- index.html : première ligne du document -->
<!DOCTYPE html>
```

#### Correction — Rails / ERB

```erb
<%# app/views/layouts/application.html.erb : première ligne %>
<!DOCTYPE html>
```

---

### 8.2 Code source valide

- Balises correctement imbriquées et fermées
- Attributs `id` uniques dans la page
- Pas d'attributs dupliqués sur un même élément
- Valeurs d'attributs entre guillemets

**Test :** Passer le code dans le validateur W3C ou chercher les `id` dupliqués dans le code (`document.querySelectorAll('[id]')` en console). Vérifier l'imbrication des balises.
**Non-conformité type :** Deux éléments avec le même `id` dans la page ; balises non fermées.
**Impact :** un `id` en double casse les relations `for`, `aria-describedby` ou `aria-labelledby` : le lecteur d’écran annonce le mauvais texte, ou rien.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```tsx
// ❌ <input id="email" /> rendu deux fois dans la page
// ✅ un id propre à chaque instance
const id = useId();
<label htmlFor={id}>Adresse e-mail</label>
<input id={id} type="email" />
```

#### Correction — Rails / ERB

```erb
<%# ❌ un id fixe dans un partial rendu plusieurs fois %>
<%# ✅ un id propre à chaque instance, ici avec l’index passé au partial %>
<label class="fr-label" for="email_<%= index %>">Adresse e-mail</label>
<input class="fr-input" type="email" id="email_<%= index %>" name="email">
```

---

### 8.3–8.4 Langue par défaut présente et pertinente

8.3 : la langue est indiquée. 8.4 : son code est valide et correspond à la langue de la page.

**Test :** Vérifier la présence de l'attribut `lang` sur la balise `<html>` (ou sur chaque élément de texte) et que sa valeur est un code de langue valide (ISO 639-1 : `fr`, `en`, `de`...).
**Non-conformité type :** `<html>` sans `lang` ; `lang="français"` au lieu de `lang="fr"`.
**Impact :** sans langue déclarée, la synthèse vocale peut lire le français avec la prononciation d’une autre langue : le texte devient incompréhensible.
**Priorité :** 🔴 Bloquant

#### Correction — React / JSX

```html
<!-- index.html, ou layout racine -->
<html lang="fr">
```

#### Correction — Rails / ERB

```erb
<html lang="<%= I18n.locale %>">
```

---

### 8.5–8.6 Titre de page présent et pertinent

8.5 : la balise existe et n’est pas vide. 8.6 : son contenu identifie la page.

**Test :** Vérifier la présence d'une balise `<title>` non vide. Vérifier que son contenu identifie clairement la page et inclut le nom du site (format recommandé : "Nom de la page - Nom du site").
**Non-conformité type :** `<title>` absent ; `<title>Index</title>` ou `<title>Page</title>` non descriptif ; même `<title>` sur toutes les pages.
**Impact :** le titre est la première chose annoncée au lecteur d’écran : sans lui, la personne ne sait pas sur quelle page elle arrive, ni à quoi correspond chaque onglet ouvert.
**Priorité :** 🔴 Bloquant

#### Correction — React / JSX

```tsx
// React 19, ou react-helmet selon le projet ; à mettre à jour à chaque route
<title>Mes demandes - Nom du site</title>
```

#### Correction — Rails / ERB

```erb
<%# si le projet a déjà un mécanisme de titre, l’utiliser et le renseigner sur chaque page %>
<%# layout %>
<title><%= content_for(:title) %> - Nom du site</title>

<%# vue %>
<% content_for :title, "Mes demandes" %>
```

---

### 8.7–8.8 Changements de langue indiqués et pertinents

8.7 : le changement de langue est indiqué. 8.8 : son code est valide et correspond à la langue du passage.

**Test :** Identifier les passages de texte dans une langue différente de la langue par défaut. Vérifier qu'ils ont un attribut `lang` avec la bonne valeur.
**Non-conformité type :** Citation ou terme en anglais sans `lang="en"` ; `lang` avec une valeur incorrecte.
**Impact :** sans indication, la synthèse vocale lit le passage avec la prononciation du français : il devient difficile à comprendre.
**Priorité :** 🟡 Mineur

#### Correction — React / JSX

```tsx
<p>Le service est disponible en <span lang="en">open source</span>.</p>
```

#### Correction — Rails / ERB

```erb
<p>Le service est disponible en <span lang="en">open source</span>.</p>
```

**Exceptions :** noms propres, termes techniques sans traduction courante.

---

### 8.9 Balises non utilisées uniquement à des fins de présentation

**Test :** Vérifier que les balises sémantiques (`<h1>`–`<h6>`, `<blockquote>`, `<ul>`, `<strong>`, `<em>`...) ne sont utilisées que pour leur sens, pas pour leur rendu visuel.
**Non-conformité type :** `<h3>` utilisé pour augmenter la taille d'un texte sans signification de titre ; `<blockquote>` pour indenter visuellement.
**Impact :** une balise détournée annonce au lecteur d’écran une structure qui n’existe pas : un faux titre, par exemple, brouille la navigation par titres.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```tsx
// ❌ <h3>Texte simplement mis en avant</h3>
// ✅ la taille vient du CSS, la balise garde son sens
<p className="fr-h3">Texte simplement mis en avant</p>
```

#### Correction — Rails / ERB

```erb
<%# ❌ <h3>Texte simplement mis en avant</h3> %>
<%# ✅ la taille vient du CSS, la balise garde son sens %>
<p class="fr-h3">Texte simplement mis en avant</p>
```

---

### 8.10 Sens de lecture signalé

**Test :** Vérifier que les passages de texte en langue à écriture de droite à gauche (arabe, hébreu...) ont `dir="rtl"`.
**Non-conformité type :** Texte arabe affiché sans `dir="rtl"` entraînant un affichage incorrect.
**Impact :** sans `dir`, un texte écrit de droite à gauche s’affiche et se lit dans le désordre, notamment autour de la ponctuation et des chiffres.
**Priorité :** 🟡 Mineur

#### Correction — React / JSX

```tsx
<p lang="ar" dir="rtl">نص بالعربية</p>
```

#### Correction — Rails / ERB

```erb
<p lang="ar" dir="rtl">نص بالعربية</p>
```

---

## Thème 9 — Structuration de l'information (4 critères)

### 9.1 Hiérarchie des titres pertinente

- Utiliser `<h1>` à `<h6>` dans l'ordre hiérarchique
- Un seul `<h1>` par page (bonne pratique)
- Pas de saut de niveau (h1 → h3 sans h2)
- Le contenu de chaque titre doit être pertinent
- Tout passage qui joue le rôle de titre doit être balisé comme tel

**Test :** Extraire tous les titres (`<h1>`–`<h6>`, `role="heading"` avec `aria-level`) et reconstituer la hiérarchie. Vérifier l'absence de sauts de niveaux et la cohérence logique de l'arborescence.
**Non-conformité type :** `<h1>` suivi directement d'un `<h3>` ; titre visuel en `<div>` stylée, sans balise de titre.
**Impact :** la navigation par titres est le principal moyen de survoler une page au lecteur d’écran : sans hiérarchie fiable, la personne qui l’utilise perd ce repère.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```tsx
<h1>Titre principal de la page</h1>
  <h2>Section</h2>
    <h3>Sous-section</h3>
  <h2>Autre section</h2>
```

#### Correction — Rails / ERB

```erb
<h1>Titre principal de la page</h1>
  <h2>Section</h2>
    <h3>Sous-section</h3>
  <h2>Autre section</h2>
```

---

### 9.2 Structure du document cohérente

**Test :** Vérifier la présence des landmarks HTML5 : `<header>` unique en tête, `<nav>` pour les navigations, `<main>` unique et visible, `<footer>` en pied. Vérifier que `<main>` n'est pas utilisé plusieurs fois ou caché.
**Non-conformité type :** Absence de `<main>` ; plusieurs `<main>` visibles ; `<nav>` utilisé pour tout groupe de liens, ou rendu vide.
**Impact :** sans ces zones, la personne qui utilise un lecteur d’écran ne peut pas sauter directement au contenu principal ou à la navigation.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```tsx
<header>  {/* Zone d'en-tête — role="banner" implicite */}
<nav>     {/* Navigation principale et secondaire */}
<main>    {/* Contenu principal — unique et visible */}
<footer>  {/* Pied de page — role="contentinfo" implicite */}
```

#### Correction — Rails / ERB

```erb
<%# Layout : structure des composants En-tête et Pied de page du DSFR %>
<header role="banner" class="fr-header">
  <nav class="fr-nav" id="navigation" role="navigation" aria-label="Menu principal">...</nav>
</header>
<main role="main" id="content">...</main>
<footer class="fr-footer" role="contentinfo" id="footer">...</footer>
```

---

### 9.3 Listes correctement structurées

**Test :** Identifier les listes visuelles (puces, numérotées, de définitions). Vérifier qu'elles utilisent `<ul>`, `<ol>` ou `<dl>` selon le type, ou les rôles `list` et `listitem`, et que les enfants directs sont des `<li>` ou `<dt>`/`<dd>`. Une liste d’options en `role="listbox"` et `role="option"` est un composant d’interface : elle relève de 7.1, pas de ce critère.
**Non-conformité type :** Liste de liens en navigation codée avec des `<div>` au lieu de `<ul><li>` ; liste ordonnée codée en `<ul>`.
**Impact :** sans balisage de liste, le lecteur d’écran n’annonce ni le début de la liste ni le nombre d’éléments : la personne ne peut pas estimer son contenu ni la passer.
**Priorité :** 🟡 Mineur

#### Correction — React / JSX

```tsx
// ❌ <div><a href="/aide">Aide</a></div><div><a href="/contact">Contact</a></div>
// ✅
<ul>
  <li><a href="/aide">Aide</a></li>
  <li><a href="/contact">Contact</a></li>
</ul>
```

#### Correction — Rails / ERB

```erb
<%# ❌ <div><a href="/aide">Aide</a></div><div><a href="/contact">Contact</a></div> %>
<%# ✅ %>
<ul>
  <li><a class="fr-link" href="/aide">Aide</a></li>
  <li><a class="fr-link" href="/contact">Contact</a></li>
</ul>
```

---

### 9.4 Citations correctement indiquées

**Test :** Identifier les citations dans le contenu. Vérifier que les citations courtes utilisent `<q>` et les blocs de citation `<blockquote>`.
**Non-conformité type :** Citation longue dans un `<p>` stylé en italique sans `<blockquote>`.
**Impact :** une citation non balisée se lit comme le reste du texte : la personne qui utilise un lecteur d’écran ne sait pas que ces mots viennent d’une autre source.
**Priorité :** 🟡 Mineur

#### Correction — React / JSX

```tsx
<p>Le guide précise : <q>une personne, un accès</q>.</p>

<blockquote>
  <p>Texte de la citation longue, rapporté tel quel.</p>
</blockquote>
```

#### Correction — Rails / ERB

```erb
<p>Le guide précise : <q>une personne, un accès</q>.</p>

<blockquote>
  <p>Texte de la citation longue, rapporté tel quel.</p>
</blockquote>
```

---

## Thème 10 — Présentation de l'information (14 critères)

### 10.1 Présentation contrôlée par CSS

**Test :** Vérifier l'absence de balises de présentation dépréciées (`<center>`, `<font>`, `<big>`, `<blink>`, `<marquee>`) et d'attributs de présentation (`align`, `bgcolor`, `border`, `color`, `valign`...) dans le HTML.
**Non-conformité type :** `<font color="red">texte</font>` ; `<td align="center">`.
**Impact :** une présentation écrite dans le HTML résiste aux feuilles de style personnelles : la personne qui adapte l’affichage (couleurs, contraste, police) ne peut pas la modifier.
**Priorité :** 🟡 Mineur

#### Correction — React / JSX

```tsx
// ❌ <font color="red">texte</font>
// ✅ la présentation passe par une classe
<p className="fr-text--bold">texte</p>
```

#### Correction — Rails / ERB

```erb
<%# ❌ <font color="red">texte</font> %>
<%# ✅ la présentation passe par une classe %>
<p class="fr-text--bold">texte</p>
```

---

### 10.2–10.3 Contenu présent et compréhensible sans CSS

10.2 : l’information reste présente sans feuille de style. 10.3 : l’ordre de lecture reste compréhensible.

**Test :** Désactiver les CSS et vérifier que le contenu textuel reste lisible et que l'information n'est pas transmise uniquement via des pseudo-éléments CSS (`::before`/`::after`) ou des `background-image`.
**Non-conformité type :** Icône informative affichée uniquement via `background-image` CSS ; texte généré uniquement via `::before`.
**Impact :** un contenu porté par le seul CSS disparaît pour la personne qui remplace ou désactive les styles, et n’est pas toujours restitué au lecteur d’écran.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```tsx
// ❌ <span className="statut-refuse" /> avec le texte dans ::before
// ✅ le texte est dans le code
<p>Statut : <span className="statut-refuse">refusée</span></p>
```

#### Correction — Rails / ERB

```erb
<%# ❌ <span class="statut-refuse"></span> avec le texte dans ::before %>
<%# ✅ le texte est dans le code, composant Badge du DSFR %>
<p class="fr-badge fr-badge--error">Refusée</p>
```

---

### 10.4 Texte lisible à 200% de zoom

**Test :** Zoomer à 200% dans le navigateur (Ctrl/Cmd + zoom ou réglages d'accessibilité). Vérifier que le texte reste lisible, que les contenus ne se chevauchent pas et que les fonctionnalités restent utilisables.
**Non-conformité type :** Texte tronqué ou contenu caché à 200% de zoom ; boutons dont le texte déborde du conteneur.
**Impact :** contenus coupés ou superposés : une partie de la page devient inaccessible à la personne malvoyante qui agrandit le texte.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```css
/* ❌ .carte { height: 80px; overflow: hidden; } */
/* ✅ le conteneur grandit avec le texte */
.carte { min-height: 5rem; }
```

#### Correction — Rails / ERB

```css
/* ❌ .carte { height: 80px; overflow: hidden; } */
/* ✅ le conteneur grandit avec le texte */
.carte { min-height: 5rem; }
```

---

### 10.5 Couleurs de fond et de texte couplées

Une déclaration `color` s’accompagne d’une couleur de fond, et inversement, au moins héritée d’un parent. Le test officiel porte sur la valeur calculée : si le parent n’est pas dans le code audité, le code seul ne permet pas de conclure.

**Test :** Vérifier que les règles CSS définissant `color` définissent aussi `background-color` sur le même élément ou son ancêtre, et vice versa.
**Non-conformité type :** `.texte-blanc { color: white; }` sans `background-color` défini, ni sur l’élément ni sur un parent, rendant le texte illisible selon le fond de l'utilisateur.
**Impact :** si seule une des deux couleurs est déclarée, la personne qui impose ses propres couleurs peut obtenir un texte illisible, par exemple blanc sur blanc.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```css
/* ❌ .encart { color: #fff; } */
/* ✅ */
.encart { color: #fff; background-color: #000091; }
```

#### Correction — Rails / ERB

```css
/* ❌ .encart { color: #fff; } */
/* ✅ */
.encart { color: #fff; background-color: #000091; }
```

---

### 10.6 Liens visibles par rapport au texte

**Test :** Identifier les liens dans du texte courant dont la nature n’est pas évidente. Si leur distinction par rapport au texte est uniquement colorimétrique, vérifier : contraste lien/texte ≥ 3:1 ET indication visuelle autre qu’un changement de couleur au survol ET au focus.
**Non-conformité type :** Lien dans un paragraphe différencié uniquement par une couleur peu contrastée, sans soulignement ni au survol ni au focus.
**Impact :** un lien signalé par sa seule couleur ne se repère pas dans le paragraphe pour la personne qui distingue mal les couleurs.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```css
/* ❌ p a { text-decoration: none; } */
/* ✅ le plus simple : garder le soulignement */
p a { text-decoration: underline; }
```

#### Correction — Rails / ERB

```css
/* ❌ p a { text-decoration: none; } */
/* ✅ le plus simple : garder le soulignement */
p a { text-decoration: underline; }
```

---

### 10.7 Focus visible

**Test :** Parcourir la page au clavier (Tab). Vérifier que chaque élément focusé a un indicateur visuel clairement visible (outline, bordure, surlignage). Vérifier l'absence de `outline: none` sans remplacement.
**Non-conformité type :** `*:focus { outline: none; }` dans le CSS sans focus personnalisé de remplacement.
**Impact :** sans focus visible, la personne qui navigue au clavier ne sait pas où elle se trouve dans la page.
**Priorité :** 🔴 Bloquant

#### Correction — React / JSX

```css
/* ❌ Ne jamais faire */
*:focus { outline: none; }

/* ✅ Personnaliser le focus visiblement */
:focus-visible {
  outline: 2px solid #000091;
  outline-offset: 2px;
}
```

#### Correction — Rails / ERB

```css
/* ❌ Ne jamais faire */
*:focus { outline: none; }

/* ✅ Personnaliser le focus visiblement */
:focus-visible {
  outline: 2px solid #000091;
  outline-offset: 2px;
}
```

---

### 10.8 Contenus cachés correctement gérés

Un contenu caché doit soit avoir vocation à être ignoré par les aides techniques, soit leur devenir accessible après une action au clavier ou au pointeur, ou après un déplacement du focus.

**Test :** Vérifier que les contenus masqués visuellement mais destinés aux AT utilisent bien `.sr-only`/`.visually-hidden` (et non `display:none`). Vérifier que les contenus cachés aux AT utilisent `aria-hidden="true"` ou `display:none`.
**Non-conformité type :** Texte alternatif pour icône caché avec `display:none` (inaccessible aux lecteurs d'écran) ; `aria-hidden="true"` sur un élément focalisable ou porteur d’information.
**Impact :** un contenu mal caché est soit perdu pour le lecteur d’écran, soit annoncé alors qu’il ne devrait pas l’être : avec `aria-hidden` sur un élément focalisable, le focus se pose sur un élément muet.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```tsx
// ❌ <span style={{ display: "none" }}>Supprimer le document</span>
// ✅ masqué à l'écran, restitué au lecteur d'écran
<button type="button">
  <svg aria-hidden="true" focusable="false">...</svg>
  <span className="fr-sr-only">Supprimer le document</span>
</button>
```

#### Correction — Rails / ERB

```erb
<%# ❌ <span style="display: none">Supprimer le document</span> %>
<%# ✅ masqué à l’écran, restitué au lecteur d’écran %>
<button type="button">
  <svg aria-hidden="true" focusable="false">...</svg>
  <span class="fr-sr-only">Supprimer le document</span>
</button>
```

---

### 10.9–10.10 Information pas uniquement par forme, taille ou position

10.9 : l’information a un autre moyen d’être récupérée. 10.10 : ce moyen transmet la même information.

**Test :** Vérifier que l'information n'est pas transmise uniquement par la position ("le bouton à droite"), la forme ou la taille (élément "plus grand" = important).
**Non-conformité type :** Instructions "Cliquez sur le bouton rond" sans autre identification ; page active du menu signalée par un simple trait sous le lien, sans `aria-current`.
**Impact :** la personne qui ne voit pas la page ou la consulte en fort zoom ne perçoit ni la forme ni la position : la consigne ou l’état lui échappe.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```tsx
// ❌ <p>Cliquez sur le bouton rond à droite.</p>
// ✅ la consigne nomme le bouton
<p>Cliquez sur le bouton « Valider ma demande ».</p>

// ✅ l'état est aussi dans le code
<a href="/aide" aria-current="page">Aide</a>
```

#### Correction — Rails / ERB

```erb
<%# ❌ <p>Cliquez sur le bouton rond à droite.</p> %>
<%# ✅ la consigne nomme le bouton %>
<p>Cliquez sur le bouton « Valider ma demande ».</p>

<%# ✅ l’état est aussi dans le code %>
<a class="fr-link" href="/aide" aria-current="page">Aide</a>
```

---

### 10.11 Reflow : pas de scroll horizontal à 320px / vertical à 256px

**Test :** Pour un contenu dont le sens de lecture est horizontal (le français), réduire la fenêtre à 320px de largeur (ou utiliser les DevTools) et vérifier que le contenu ne nécessite pas de défilement horizontal ; le défilement vertical reste normal. Pour un contenu dont le sens de lecture est vertical (écriture verticale, conçu pour défiler horizontalement), réduire la fenêtre à 256px de hauteur et vérifier l’absence de défilement vertical. Une page en français n’est pas concernée par ce second contrôle. Exception : tableaux de données, cartes interactives, interfaces nécessitant deux dimensions.
**Non-conformité type :** Barre de navigation horizontale qui déborde à 320px.
**Impact :** à fort zoom, la personne malvoyante doit faire défiler la page dans les deux sens à chaque ligne, et perd facilement le fil.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```css
/* ❌ .menu { display: flex; width: 960px; } */
/* ✅ le contenu passe à la ligne */
.menu { display: flex; flex-wrap: wrap; max-width: 100%; }
```

#### Correction — Rails / ERB

```css
/* ❌ .menu { display: flex; width: 960px; } */
/* ✅ le contenu passe à la ligne */
.menu { display: flex; flex-wrap: wrap; max-width: 100%; }
```

---

### 10.12 Espacement du texte modifiable

**Test :** Appliquer via les DevTools : `line-height: 1.5em; letter-spacing: 0.12em; word-spacing: 0.16em;` sur `body` et un espacement de `2em` après les paragraphes. Vérifier que le contenu reste lisible et que rien ne se cache ou se chevauche.
**Non-conformité type :** Conteneur avec hauteur fixe en pixels qui tronque le texte quand l'interligne augmente.
**Impact :** la personne qui augmente l’espacement pour mieux lire, notamment en cas de dyslexie, voit son texte coupé ou superposé.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```css
/* ❌ .encart { height: 40px; overflow: hidden; } */
/* ✅ */
.encart { min-height: 2.5rem; }
```

#### Correction — Rails / ERB

```css
/* ❌ .encart { height: 40px; overflow: hidden; } */
/* ✅ */
.encart { min-height: 2.5rem; }
```

---

### 10.13 Contenus additionnels (tooltips) contrôlables

**Test :** Identifier les tooltips et contenus apparaissant au survol ou au focus. Vérifier qu'ils peuvent être masqués sans déplacer le focus (touche Échap), qu'ils persistent lors du survol souris, et qu'ils restent visibles tant que nécessaire.
**Non-conformité type :** Tooltip disparaissant immédiatement quand la souris le survole ; tooltip ne pouvant pas être fermé par Échap.
**Impact :** une infobulle qu’on ne peut pas fermer masque le contenu voisin pour la personne qui zoome ; une infobulle qui disparaît au survol ne peut pas être lue à son rythme.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```tsx
<button
  type="button"
  aria-describedby="infobulle-siret"
  onKeyDown={(e) => { if (e.key === "Escape") setIsOpen(false); }}
>
  Information sur le SIRET
</button>
{/* le pointeur peut passer sur l'infobulle sans la fermer */}
<span id="infobulle-siret" role="tooltip" hidden={!isOpen}>
  Numéro à 14 chiffres de votre établissement.
</span>
```

#### Correction — Rails / ERB

```erb
<%# Composant Infobulle du DSFR %>
<button aria-describedby="infobulle-siret" type="button" class="fr-btn--tooltip fr-btn">Information sur le SIRET</button>
<span class="fr-tooltip fr-placement" id="infobulle-siret" role="tooltip">Numéro à 14 chiffres de votre établissement.</span>
```

---

### 10.14 Contenus CSS additionnels accessibles au clavier

**Test :** Pour chaque élément révélant du contenu au `:hover`, vérifier que le même contenu est accessible au `:focus` (ou via un mécanisme clavier équivalent).
**Non-conformité type :** Menu déroulant qui s'ouvre au `:hover` CSS mais pas au focus clavier.
**Impact :** un contenu affiché seulement au survol reste hors d’atteinte pour la personne qui navigue au clavier.
**Priorité :** 🔴 Bloquant

#### Correction — React / JSX

```css
/* ❌ .menu:hover .sous-menu { display: block; } */
/* ✅ */
.menu:hover .sous-menu,
.menu:focus-within .sous-menu { display: block; }
```

#### Correction — Rails / ERB

```css
/* ❌ .menu:hover .sous-menu { display: block; } */
/* ✅ */
.menu:hover .sous-menu,
.menu:focus-within .sous-menu { display: block; }
```
