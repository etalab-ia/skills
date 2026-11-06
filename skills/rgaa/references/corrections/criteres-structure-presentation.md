# Corrections RGAA — Thèmes 8 à 10 : Éléments obligatoires, Structure, Présentation

Blocs de correction par stack, à lire seulement pour rédiger la correction d’une NC. Le texte officiel et le reste de chaque critère sont dans `../criteres-structure-presentation.md`.

### 8.1 Doctype présent et valide

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

### 8.2 Code source valide

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

### 8.3–8.4 Langue par défaut présente et pertinente

#### Correction — React / JSX

```html
<!-- index.html, ou layout racine -->
<html lang="fr">
```

#### Correction — Rails / ERB

```erb
<html lang="<%= I18n.locale %>">
```

### 8.5–8.6 Titre de page présent et pertinent

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

### 8.7–8.8 Changements de langue indiqués et pertinents

#### Correction — React / JSX

```tsx
<p>Le service est disponible en <span lang="en">open source</span>.</p>
```

#### Correction — Rails / ERB

```erb
<p>Le service est disponible en <span lang="en">open source</span>.</p>
```

**Exceptions :** noms propres, termes techniques sans traduction courante.

### 8.9 Balises non utilisées uniquement à des fins de présentation

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

### 8.10 Sens de lecture signalé

#### Correction — React / JSX

```tsx
<p lang="ar" dir="rtl">نص بالعربية</p>
```

#### Correction — Rails / ERB

```erb
<p lang="ar" dir="rtl">نص بالعربية</p>
```

### 9.1 Hiérarchie des titres pertinente

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

### 9.2 Structure du document cohérente

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

### 9.3 Listes correctement structurées

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

### 9.4 Citations correctement indiquées

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

### 10.1 Présentation contrôlée par CSS

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

### 10.2–10.3 Contenu présent et compréhensible sans CSS

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

### 10.4 Texte lisible à 200% de zoom

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

### 10.5 Couleurs de fond et de texte couplées

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

### 10.6 Liens visibles par rapport au texte

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

### 10.7 Focus visible

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

### 10.8 Contenus cachés correctement gérés

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

### 10.9–10.10 Information pas uniquement par forme, taille ou position

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

### 10.11 Reflow : pas de scroll horizontal à 320px / vertical à 256px

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

### 10.12 Espacement du texte modifiable

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

### 10.13 Contenus additionnels (tooltips) contrôlables

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

### 10.14 Contenus CSS additionnels accessibles au clavier

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

