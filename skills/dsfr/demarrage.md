# Démarrer une page DSFR

## Installation

CDN, toujours avec la version explicite (la même partout dans la page) :

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.15.4/dist/dsfr.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.15.4/dist/utility/utility.min.css">
```

`utility.min.css` apporte les icônes `fr-icon-*` et les utilitaires de couleur : sans lui, les icônes ne s'affichent pas.

Les pictogrammes et illustrations (`<svg>` avec des `<use href="….svg#artwork-major">`) ne fonctionnent pas depuis le CDN : le navigateur refuse un `<use>` vers une autre origine. Utiliser le dossier `artwork/` du projet s'il existe, sinon copier `dist/artwork/` sur le site et pointer vers ces fichiers, ou, pour une page autonome, insérer dans la page le contenu du SVG ([fondamentaux/pictogram](fondamentaux/pictogram/index.md)).

npm : `npm install @gouvfr/dsfr@1.15.4`, puis les mêmes fichiers depuis `node_modules/@gouvfr/dsfr/dist/`. Pour n'importer que certains composants, chaque composant a ses fichiers dans `dist/component/<nom>/` et liste ses dépendances (« Dépendances CSS ») dans son `code.md`.

## Squelette de page

Toute page d'un site de l'État a des liens d'évitement, un en-tête avec le bloc Marque, un `main` et un pied de page :

```html
<!doctype html>
<html lang="fr" data-fr-scheme="system">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="format-detection" content="telephone=no,date=no,address=no,email=no,url=no">
  <meta name="theme-color" content="#000091">
  <title>Titre de la page - Nom du site</title>
  <link rel="apple-touch-icon" href="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.15.4/dist/favicon/apple-touch-icon.png">
  <link rel="icon" href="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.15.4/dist/favicon/favicon.svg" type="image/svg+xml">
  <link rel="shortcut icon" href="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.15.4/dist/favicon/favicon.ico" type="image/x-icon">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.15.4/dist/dsfr.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.15.4/dist/utility/utility.min.css">
</head>
<body>
  <div class="fr-skiplinks">
    <nav role="navigation" aria-label="Accès rapide" class="fr-container">
      <ul class="fr-skiplinks__list">
        <li><a class="fr-link" href="#content">Contenu</a></li>
        <li><a class="fr-link" href="#footer">Pied de page</a></li>
      </ul>
    </nav>
  </div>

  <header role="banner" class="fr-header">
    <div class="fr-header__body">
      <div class="fr-container">
        <div class="fr-header__body-row">
          <div class="fr-header__brand fr-enlarge-link">
            <div class="fr-header__brand-top">
              <div class="fr-header__logo">
                <p class="fr-logo">République<br>Française</p>
              </div>
            </div>
            <div class="fr-header__service">
              <a href="/" title="Accueil - Nom du site - Nom de l'entité">
                <p class="fr-header__service-title">Nom du site</p>
              </a>
              <p class="fr-header__service-tagline">Précision sur l'organisation</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>

  <main role="main" id="content">
    <div class="fr-container fr-my-7w">
      <h1>Titre de la page</h1>
    </div>
  </main>

  <footer class="fr-footer" role="contentinfo" id="footer">
    <div class="fr-container">
      <div class="fr-footer__body">
        <div class="fr-footer__brand fr-enlarge-link">
          <a href="/" title="Retour à l'accueil du site - Nom du site - Nom de l'entité">
            <p class="fr-logo">République<br>Française</p>
          </a>
        </div>
        <div class="fr-footer__content">
          <ul class="fr-footer__content-list">
            <li class="fr-footer__content-item"><a class="fr-footer__content-link" target="_blank" rel="noopener external" title="info.gouv.fr - nouvelle fenêtre" href="https://info.gouv.fr">info.gouv.fr</a></li>
            <li class="fr-footer__content-item"><a class="fr-footer__content-link" target="_blank" rel="noopener external" title="service-public.gouv.fr - nouvelle fenêtre" href="https://service-public.gouv.fr">service-public.gouv.fr</a></li>
            <li class="fr-footer__content-item"><a class="fr-footer__content-link" target="_blank" rel="noopener external" title="legifrance.gouv.fr - nouvelle fenêtre" href="https://legifrance.gouv.fr">legifrance.gouv.fr</a></li>
            <li class="fr-footer__content-item"><a class="fr-footer__content-link" target="_blank" rel="noopener external" title="data.gouv.fr - nouvelle fenêtre" href="https://data.gouv.fr">data.gouv.fr</a></li>
          </ul>
        </div>
      </div>
      <div class="fr-footer__bottom">
        <ul class="fr-footer__bottom-list">
          <li class="fr-footer__bottom-item"><a class="fr-footer__bottom-link" href="/plan-du-site">Plan du site</a></li>
          <li class="fr-footer__bottom-item"><a class="fr-footer__bottom-link" href="/accessibilite">Accessibilité : non conforme</a></li>
          <li class="fr-footer__bottom-item"><a class="fr-footer__bottom-link" href="/mentions-legales">Mentions légales</a></li>
          <li class="fr-footer__bottom-item"><a class="fr-footer__bottom-link" href="/donnees-personnelles">Données personnelles</a></li>
          <li class="fr-footer__bottom-item"><a class="fr-footer__bottom-link" href="/cookies">Gestion des cookies</a></li>
        </ul>
        <div class="fr-footer__bottom-copy">
          <p>Sauf mention explicite de propriété intellectuelle détenue par des tiers, les contenus de ce site sont proposés sous <a href="https://github.com/etalab/licence-ouverte/blob/master/LO.md" target="_blank" rel="noopener external" title="Licence etalab - nouvelle fenêtre">licence etalab-2.0</a></p>
        </div>
      </div>
    </div>
  </footer>

  <script type="module" src="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.15.4/dist/dsfr.module.min.js"></script>
  <script type="text/javascript" nomodule src="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.15.4/dist/dsfr.nomodule.min.js"></script>
</body>
</html>
```

Points à adapter :

- Le bloc Marque (`fr-logo`) contient l'intitulé officiel de l'entité, découpé sur plusieurs lignes avec `<br>`.
- La mention d'accessibilité du pied de page reflète l'état réel : non, partiellement ou totalement conforme.
- En-tête avec navigation, recherche, accès rapides : [composants/header/exemples.md](composants/header/exemples.md) et [composants/navigation](composants/navigation/index.md).
- Pied de page complet : [composants/footer/exemples.md](composants/footer/exemples.md).
- Modèles complets de pages (connexion, inscription, erreurs 404/500) : [modeles/pages](modeles/pages/).

## Mise en page

Contenu dans `fr-container`, colonnes avec `fr-grid-row` et `fr-col-*` (12 colonnes, points de rupture `sm`, `md`, `lg`, `xl`) :

```html
<div class="fr-container">
  <div class="fr-grid-row fr-grid-row--gutters">
    <div class="fr-col-12 fr-col-md-8">Contenu</div>
    <div class="fr-col-12 fr-col-md-4">Encart</div>
  </div>
</div>
```

Espacements par classes utilitaires (`fr-mt-4w`, `fr-py-2v`…, unité `v` = 4px, `w` = 8px) : [fondamentaux/spacing](fondamentaux/spacing/index.md). Grille détaillée : [fondamentaux/grid](fondamentaux/grid/index.md).

## Thème clair / sombre

`data-fr-scheme` sur `<html>` active la gestion du thème : `system` suit les préférences de l'utilisateur, `light` ou `dark` le fixe. Sans cet attribut, la page reste en clair et le composant Paramètres d'affichage ne fonctionne pas. Ne jamais écrire `data-fr-theme` à la main : le JS le calcule. Composant : [composants/display](composants/display/index.md).

Les couleurs se prennent dans les tokens et classes utilitaires (`fr-background-*`, `fr-text-*`) qui s'adaptent au thème, jamais en valeurs fixes : [fondamentaux/color](fondamentaux/color/index.md).

## JavaScript

`dsfr.module.min.js` initialise tous les composants interactifs (accordéon, modale, onglets, navigation…) au chargement, via les attributs `aria-controls`, `aria-expanded` et `data-fr-*`. Aucun JS à écrire pour leur comportement de base.

API : `window.dsfr(element).<composant>.<méthode>`, par exemple `dsfr(document.getElementById('ma-modale')).modal.disclose()`. Les méthodes et événements de chaque composant sont dans son `code.md`.

Configuration avant le chargement du script :

```html
<script>window.dsfr = { mode: 'manual', production: true }</script>
<script type="module" src="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.15.4/dist/dsfr.module.min.js"></script>
```

Modes : `auto` (défaut), `loaded` (au DOMContentLoaded), `runtime` (immédiat), `manual` (appeler `dsfr.start()`), `react`, `vue`, `angular` (le DSFR ne manipule plus le DOM, pour les SPA). `production: true` coupe les logs.

## Frameworks

Si le projet utilise déjà une bibliothèque DSFR, utiliser ses composants plutôt que du HTML brut :

- React / Next.js : `@codegouvfr/react-dsfr`
- Vue : `@gouvminint/vue-dsfr`

Ce skill reste la référence pour les règles d'usage, l'accessibilité et le HTML attendu en sortie.
