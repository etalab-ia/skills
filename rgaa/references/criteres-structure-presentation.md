# RGAA — Thèmes 8 à 10 : Éléments obligatoires, Structure, Présentation

## Thème 8 — Éléments obligatoires (10 critères)

### 8.1 Doctype présent et valide
```html
<!DOCTYPE html>
```
Doit être présent avant `<html>`.

### 8.2 Code source valide
- Balises correctement imbriquées et fermées
- Attributs `id` uniques dans la page
- Pas d'attributs dupliqués sur un même élément
- Valeurs d'attributs entre guillemets

### 8.3–8.4 Langue par défaut présente et pertinente
```html
<html lang="fr">
```
Code ISO 639-1 (2 caractères) ou ISO 639-2 (3 caractères).

### 8.5–8.6 Titre de page présent et pertinent
```html
<title>Nom de la page - Nom du site</title>
```
Le titre doit identifier clairement la page, être unique dans le site.

### 8.7–8.8 Changements de langue indiqués et pertinents
```tsx
<p>Le service est disponible en <span lang="en">open source</span>.</p>
```
Tout texte dans une langue différente de la langue par défaut doit avoir un attribut `lang`.

**Exceptions :** noms propres, termes techniques sans traduction courante.

### 8.9 Balises non utilisées uniquement à des fins de présentation
Ne pas utiliser `<h1>` pour grossir le texte, `<blockquote>` pour indenter, `<ul>` pour le visuel, etc.

### 8.10 Sens de lecture signalé
```tsx
<p lang="ar" dir="rtl">نص بالعربية</p>
```

---

## Thème 9 — Structuration de l'information (4 critères)

### 9.1 Hiérarchie des titres pertinente

- Utiliser `<h1>` à `<h6>` dans l'ordre hiérarchique
- Un seul `<h1>` par page (bonne pratique)
- Pas de saut de niveau (h1 → h3 sans h2)
- Le contenu de chaque titre doit être pertinent

```tsx
<h1>Titre principal de la page</h1>
  <h2>Section</h2>
    <h3>Sous-section</h3>
  <h2>Autre section</h2>
```

### 9.2 Structure du document cohérente

Zones structurelles obligatoires :
```tsx
<header>  {/* Zone d'en-tête — role="banner" implicite */}
<nav>     {/* Navigation principale et secondaire */}
<main>    {/* Contenu principal — unique et visible */}
<footer>  {/* Pied de page — role="contentinfo" implicite */}
```

- `<main>` : unique et visible dans la page
- `<nav>` : réservé aux navigations principales et secondaires
- Ne pas utiliser `<nav>` pour tout groupe de liens

### 9.3 Listes correctement structurées

```tsx
// Liste non ordonnée
<ul>
  <li>Élément 1</li>
  <li>Élément 2</li>
</ul>

// Liste ordonnée
<ol>
  <li>Étape 1</li>
  <li>Étape 2</li>
</ol>

// Liste de description
<dl>
  <dt>Terme</dt>
  <dd>Définition</dd>
</dl>
```

### 9.4 Citations correctement indiquées

```tsx
// Citation courte
<p>Comme le dit le proverbe : <q>Paris ne s'est pas fait en un jour</q>.</p>

// Bloc de citation
<blockquote>
  <p>Le numérique doit être accessible à tous.</p>
</blockquote>
```

---

## Thème 10 — Présentation de l'information (14 critères)

### 10.1 Présentation contrôlée par CSS
- Pas de balises de présentation : `<center>`, `<font>`, `<big>`, `<blink>`, `<marquee>`, `<s>`, `<strike>`, `<tt>`
- Pas d'attributs de présentation : `align`, `bgcolor`, `border`, `cellpadding`, `cellspacing`, `color`, `valign`, `vspace`, `hspace`
- Pas d'espaces pour simuler des colonnes/tableaux/séparations de lettres

### 10.2–10.3 Contenu présent et compréhensible sans CSS

L'information ne doit pas dépendre uniquement des CSS. Pas d'information uniquement via `::before`/`::after` ou `background-image`.

### 10.4 Texte lisible à 200% de zoom

Le contenu doit rester lisible et fonctionnel quand la taille du texte est augmentée à 200%.

### 10.5 Couleurs de fond et de texte couplées

Si on définit `color`, on doit aussi définir `background-color` (et vice-versa), au moins par héritage.

### 10.6 Liens visibles par rapport au texte

Si un lien est signalé uniquement par la couleur :
- Contraste ≥ 3:1 avec le texte environnant
- Indication visuelle au survol (autre que couleur)
- Indication visuelle au focus (autre que couleur)

### 10.7 Focus visible

```css
/* ❌ Ne jamais faire */
*:focus { outline: none; }

/* ✅ Personnaliser le focus visiblement */
:focus-visible {
  outline: 2px solid #000091;
  outline-offset: 2px;
}
```

### 10.8 Contenus cachés correctement gérés

- Contenu caché pour tous (visuellement + AT) : `display: none`, `visibility: hidden`, `hidden`
- Contenu caché visuellement mais accessible aux AT : classe `.sr-only` / `.visually-hidden`
- Contenu caché des AT mais visible : `aria-hidden="true"`

```css
/* Classe pour cacher visuellement mais garder accessible */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

### 10.9–10.10 Information pas uniquement par forme, taille ou position

Ne pas communiquer l'information uniquement par la position, forme ou taille (ex: "le bouton à droite", élément actif uniquement via gras).

### 10.11 Reflow : pas de scroll horizontal à 320px / vertical à 256px

Le contenu doit être consultable sans défilement horizontal dans une fenêtre de 320px de large (sauf tableaux de données, cartes, etc.).

### 10.12 Espacement du texte modifiable

Le contenu doit rester lisible avec :
- `line-height` : 1.5× la taille de police
- Espacement paragraphes : 2× la taille de police
- `letter-spacing` : 0.12× la taille de police
- `word-spacing` : 0.16× la taille de police

### 10.13 Contenus additionnels (tooltips) contrôlables

Contenu apparaissant au survol/focus :
- Doit pouvoir être masqué (Échap) sans déplacer le focus
- Doit pouvoir être survolé par la souris sans disparaître
- Doit rester visible tant que nécessaire

### 10.14 Contenus CSS additionnels accessibles au clavier

Si un contenu apparaît au `:hover`, il doit aussi apparaître au `:focus` (ou via un autre mécanisme clavier).
