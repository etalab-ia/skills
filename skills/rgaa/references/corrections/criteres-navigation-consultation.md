# Corrections RGAA — Thèmes 12–13 : Navigation, Consultation

Blocs de correction par stack, à lire seulement pour rédiger la correction d’une NC. Le texte officiel et le reste de chaque critère sont dans `../criteres-navigation-consultation.md`.

### 12.1 Deux systèmes de navigation minimum

#### Correction — React / JSX

```tsx
// Layout partagé : menu principal et moteur de recherche sur chaque page, plan du site en pied de page
<header>
  <nav aria-label="Menu principal">
    <ul>
      <li><a href="/demandes" aria-current="page">Mes demandes</a></li>
      <li><a href="/aide">Aide</a></li>
    </ul>
  </nav>
  <form role="search" action="/recherche">
    <label htmlFor="recherche-site">Rechercher sur le site</label>
    <input id="recherche-site" type="search" name="q" />
    <button type="submit">Rechercher</button>
  </form>
</header>
<main id="content">{children}</main>
<footer>
  <a href="/plan-du-site">Plan du site</a>
</footer>
```

#### Correction — Rails / ERB

```erb
<%# Layout : composants En-tête (avec sa barre de recherche), Navigation principale et Pied de page du DSFR %>
<header role="banner" class="fr-header">
  <div class="fr-header__body">
    <div class="fr-container">
      <div class="fr-header__body-row">
        <div class="fr-header__brand fr-enlarge-link">
          <div class="fr-header__brand-top">
            ...
            <div class="fr-header__navbar">
              <button data-fr-opened="false" aria-controls="header-search" title="Rechercher" type="button" id="bouton-recherche" class="fr-btn--search fr-btn">Rechercher</button>
              <button data-fr-opened="false" aria-controls="header-navigation" title="Menu" type="button" id="bouton-menu" class="fr-btn--menu fr-btn">Menu</button>
            </div>
          </div>
          ...
        </div>
        <div class="fr-header__tools">
          <div class="fr-header__search fr-modal" id="header-search" aria-labelledby="bouton-recherche">
            <div class="fr-container fr-container-lg--fluid">
              <button aria-controls="header-search" title="Fermer" type="button" id="bouton-fermer-recherche" class="fr-btn--close fr-btn">Fermer</button>
              <div class="fr-search-bar" id="recherche" role="search">
                <label class="fr-label" for="recherche-input">
                  Rechercher
                </label>
                <input class="fr-input" aria-describedby="recherche-input-messages" placeholder="Rechercher" id="recherche-input" name="q" type="search">
                <div class="fr-messages-group" id="recherche-input-messages" aria-live="polite">
                </div>
                <button title="Rechercher" type="button" id="recherche-btn" class="fr-btn">Rechercher</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="fr-header__menu fr-modal" id="header-navigation" aria-labelledby="bouton-menu">
    <div class="fr-container">
      <button aria-controls="header-navigation" title="Fermer" type="button" id="bouton-fermer-menu" class="fr-btn--close fr-btn">Fermer</button>
      <nav class="fr-nav" id="navigation" role="navigation" aria-label="Menu principal">
        <ul class="fr-nav__list">
          <li class="fr-nav__item">
            <a href="/demandes" class="fr-nav__link" aria-current="page">Mes demandes</a>
          </li>
          <li class="fr-nav__item">
            <a href="/aide" class="fr-nav__link">Aide</a>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</header>
...
<footer class="fr-footer" role="contentinfo" id="footer">
  <div class="fr-container">
    ...
    <div class="fr-footer__bottom">
      <ul class="fr-footer__bottom-list">
        <li class="fr-footer__bottom-item">
          <a href="/plan-du-site" class="fr-footer__bottom-link">Plan du site</a>
        </li>
        ...
      </ul>
    </div>
  </div>
</footer>
```

### 12.2 Menu et barres de navigation à la même place

#### Correction — React / JSX

```tsx
// ❌ un <Menu /> rendu par chaque page, en haut sur l’une, en bas sur l’autre
// ✅ un layout unique rend la navigation dans le même ordre sur toutes les pages
export function Layout({ children }) {
  return (
    <>
      <LiensEvitement />
      <Header />
      <main id="content">{children}</main>
      <Footer />
    </>
  );
}
```

#### Correction — Rails / ERB

```erb
<%# ❌ un content_for(:menu) rendu avant l’en-tête dans certaines vues seulement %>
<%# ✅ app/views/layouts/application.html.erb : même ordre sur toutes les pages %>
<body>
  <%= render "layouts/liens_evitement" %>
  <%= render "layouts/header" %>
  <main role="main" id="content">
    <%= yield %>
  </main>
  <%= render "layouts/footer" %>
</body>
```

### 12.3–12.5 Plan du site et moteur de recherche

#### Correction — React / JSX

```tsx
// Page plan du site : l’architecture en listes imbriquées
<nav aria-label="Plan du site">
  <ul>
    <li>
      <a href="/demandes">Mes demandes</a>
      <ul>
        <li><a href="/demandes/nouvelle">Nouvelle demande</a></li>
      </ul>
    </li>
    <li><a href="/aide">Aide</a></li>
  </ul>
</nav>

// Layout partagé : le lien vers le plan du site, au même endroit sur toutes les pages
<footer>
  <a href="/plan-du-site">Plan du site</a>
</footer>
```

#### Correction — Rails / ERB

```erb
<%# Page plan du site : le DSFR n’a pas de composant dédié, listes imbriquées et liens fr-link %>
<nav role="navigation" aria-label="Plan du site">
  <ul>
    <li>
      <a class="fr-link" href="/demandes">Mes demandes</a>
      <ul>
        <li><a class="fr-link" href="/demandes/nouvelle">Nouvelle demande</a></li>
      </ul>
    </li>
    <li><a class="fr-link" href="/aide">Aide</a></li>
  </ul>
</nav>

<%# Partial de pied de page partagé : lien du composant Pied de page du DSFR %>
<li class="fr-footer__bottom-item">
  <a href="/plan-du-site" class="fr-footer__bottom-link">Plan du site</a>
</li>
<%# Moteur de recherche : la barre fr-header__search du partial d’en-tête partagé (voir 12.1) %>
```

### 12.6 Zones de regroupement atteignables ou évitables

#### Correction — React / JSX

```tsx
// Les rôles explicites sont redondants avec les éléments HTML, mais sans effet néfaste (le DSFR les pose aussi)
<header role="banner">...</header>
<nav role="navigation" aria-label="Menu principal">...</nav>
<main role="main" id="content">...</main>
<footer role="contentinfo">...</footer>
<form role="search" aria-label="Rechercher sur le site">...</form>

// Bonne pratique : plusieurs <nav> différenciés par aria-label
<nav aria-label="Menu principal">...</nav>
<nav aria-label="Fil d’Ariane">...</nav>
```

#### Correction — Rails / ERB

```erb
<%# Layout : composants En-tête, Barre de recherche, Fil d’Ariane et Pied de page du DSFR %>
<header role="banner" class="fr-header">
  <div class="fr-header__body">
    ...
          <div class="fr-header__search fr-modal" id="header-search" aria-labelledby="bouton-recherche">
            ...
              <div class="fr-search-bar" id="recherche" role="search">...</div>
            ...
          </div>
    ...
  </div>
  <div class="fr-header__menu fr-modal" id="header-navigation" aria-labelledby="bouton-menu">
    ...
      <nav class="fr-nav" id="navigation" role="navigation" aria-label="Menu principal">...</nav>
    ...
  </div>
</header>
<main role="main" id="content">
  <nav role="navigation" class="fr-breadcrumb" aria-label="vous êtes ici :">
    <button type="button" class="fr-breadcrumb__button" aria-expanded="false" aria-controls="fil-ariane">Voir le fil d’Ariane</button>
    <div class="fr-collapse" id="fil-ariane">
      <ol class="fr-breadcrumb__list">
        <li>
          <a class="fr-breadcrumb__link" href="/">Accueil</a>
        </li>
        <li>
          <a class="fr-breadcrumb__link" aria-current="page">Mes demandes</a>
        </li>
      </ol>
    </div>
  </nav>
  ...
</main>
<footer class="fr-footer" role="contentinfo" id="footer">...</footer>
```

### 12.7 Lien d’évitement ou d’accès rapide au contenu principal

#### Correction — React / JSX

```tsx
<body>
  <a href="#content" className="lien-evitement">Aller au contenu principal</a>
  <header>...</header>
  <nav aria-label="Menu principal">...</nav>
  <main id="content">...</main>
</body>
```

```css
/* Masqué visuellement hors focus, visible quand il reçoit le focus */
.lien-evitement:not(:focus) {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}
```

#### Correction — Rails / ERB

```erb
<%# Composant Liens d’évitement du DSFR, avant l’en-tête ; chaque cible existe dans le layout %>
<div class="fr-skiplinks">
  <nav role="navigation" aria-label="Accès rapide" class="fr-container">
    <ul class="fr-skiplinks__list">
      <li>
        <a class="fr-link" href="#content">Contenu</a>
      </li>
      <li>
        <a class="fr-link" href="#header-navigation">Menu</a>
      </li>
      <li>
        <a class="fr-link" href="#footer">Pied de page</a>
      </li>
    </ul>
  </nav>
</div>
<header role="banner" class="fr-header">
  ...
  <div class="fr-header__menu fr-modal" id="header-navigation" aria-labelledby="bouton-menu">...</div>
</header>
<main role="main" id="content">...</main>
<footer class="fr-footer" role="contentinfo" id="footer">...</footer>
```

### 12.8 Ordre de tabulation cohérent

#### Correction — React / JSX

```tsx
// ❌ <button tabIndex={3}>Valider</button>
// ✅ ordre du DOM ; après l’insertion, focus sur le titre du contenu inséré
const titreRef = useRef(null);
useEffect(() => {
  if (resultats) titreRef.current?.focus();
}, [resultats]);

<h2 ref={titreRef} tabIndex={-1}>Résultats de la recherche</h2>
```

#### Correction — Rails / ERB

```erb
<%# ❌ <button tabindex="3">Valider</button> %>
<%# ✅ contenu inséré par Turbo Stream juste après son déclencheur, focus déplacé sur son titre %>
<div id="resultats" data-controller="focus-insertion">
  <h2 tabindex="-1" data-focus-insertion-target="titre">Résultats de la recherche</h2>
  ...
</div>

<%# ✅ modale : le composant Modale du DSFR garde le focus dans la fenêtre tant qu’elle est ouverte %>
<button data-fr-opened="false" aria-controls="modale-details" id="bouton-modale-details" type="button" class="fr-btn">Voir le détail</button>
<dialog id="modale-details" class="fr-modal" aria-labelledby="modale-details-titre">
  <div class="fr-container fr-container--fluid fr-container-md">
    <div class="fr-grid-row fr-grid-row--center">
      <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
        <div class="fr-modal__body">
          <div class="fr-modal__header">
            <button aria-controls="modale-details" title="Fermer" type="button" id="bouton-fermer-details" class="fr-btn--close fr-btn">Fermer</button>
          </div>
          <div class="fr-modal__content">
            <h2 id="modale-details-titre" class="fr-modal__title">
              Détail de la demande
            </h2>
            <p>...</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</dialog>
```

```javascript
// app/javascript/controllers/focus_insertion_controller.js
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static targets = ["titre"]

  titreTargetConnected(titre) {
    titre.focus()
  }
}
```

### 12.9 Pas de piège au clavier

#### Correction — React / JSX

```tsx
// Liste déroulante personnalisée (combobox de 7.1)
function onKeyDown(e) {
  // ❌ if (e.key === "Tab") e.preventDefault();
  if (e.key === "Tab") {
    setIsOpen(false); // pas de preventDefault : le focus passe à l’élément suivant
  }
  if (e.key === "Escape") {
    setIsOpen(false); // le focus reste sur le champ (ou revient au bouton qui a ouvert la liste)
  }
}

<input
  id="ville"
  role="combobox"
  aria-autocomplete="list"
  aria-expanded={isOpen}
  aria-controls="villes"
  aria-activedescendant={activeId}
  onKeyDown={onKeyDown}
/>
```

#### Correction — Rails / ERB

```erb
<%# ✅ d’abord : la liste native du composant Liste déroulante du DSFR, sans piège possible %>
<div class="fr-select-group">
  <label class="fr-label" for="statut">
    Statut de la demande
  </label>
  <select class="fr-select" aria-describedby="statut-messages" id="statut" name="statut">
    <option value="" selected disabled>Sélectionner une option</option>
    <option value="brouillon">Brouillon</option>
    <option value="envoyee">Envoyée</option>
  </select>
  <div class="fr-messages-group" id="statut-messages" aria-live="polite">
  </div>
</div>

<%# ✅ sinon, si la liste personnalisée est gardée : la combobox de 7.1 et un contrôleur qui libère Tab %>
<div class="fr-input-group" data-controller="liste">
  <label class="fr-label" for="ville">Ville</label>
  <input class="fr-input" type="text" id="ville" name="ville" role="combobox" aria-autocomplete="list" aria-expanded="true" aria-controls="villes" aria-activedescendant="ville-paris" data-liste-target="champ" data-action="keydown->liste#clavier">
  <ul id="villes" role="listbox" aria-label="Villes proposées" data-liste-target="liste">
    <li id="ville-paris" role="option" aria-selected="true">Paris</li>
  </ul>
</div>
```

```javascript
// app/javascript/controllers/liste_controller.js
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static targets = ["champ", "liste"]

  clavier(event) {
    // ❌ jamais event.preventDefault() sur Tab : le focus doit pouvoir sortir
    if (event.key === "Tab" || event.key === "Escape") this.fermer()
  }

  fermer() {
    this.listeTarget.hidden = true
    this.champTarget.setAttribute("aria-expanded", "false")
  }
}
```

### 12.10 Raccourcis clavier à une seule touche contrôlables

#### Correction — React / JSX

```tsx
// ❌ window.addEventListener("keydown", (e) => { if (e.key === "j") suivante(); });
// ✅ le raccourci n’agit que quand la liste a le focus, et une option le désactive
<label>
  <input type="checkbox" checked={raccourcisActifs} onChange={() => setRaccourcisActifs(!raccourcisActifs)} />
  Activer les raccourcis clavier
</label>
<section
  aria-label="Liste des demandes"
  tabIndex={0}
  onKeyDown={(e) => {
    if (!raccourcisActifs) return;
    if (e.key === "j") suivante();
  }}
>
  ...
</section>
```

#### Correction — Rails / ERB

```erb
<%# ❌ data-action="keydown@window->liste#raccourci" %>
<%# ✅ écouteur posé sur le composant, et composant Interrupteur du DSFR pour désactiver les raccourcis %>
<div data-controller="liste">
  <div class="fr-toggle">
    <%# sans name : piloté en JavaScript (Stimulus), jamais envoyé %>
    <input type="checkbox" class="fr-toggle__input" id="raccourcis-actifs" aria-describedby="raccourcis-actifs-messages" checked data-liste-target="interrupteur">
    <label class="fr-toggle__label" for="raccourcis-actifs">Activer les raccourcis clavier</label>
    <div class="fr-messages-group" id="raccourcis-actifs-messages" aria-live="polite">
    </div>
  </div>
  <section aria-label="Liste des demandes" tabindex="0" data-action="keydown->liste#raccourci">
    ...
  </section>
</div>
```

```javascript
// app/javascript/controllers/liste_controller.js
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static targets = ["interrupteur"]

  raccourci(event) {
    if (!this.interrupteurTarget.checked) return
    if (event.key === "j") this.suivante()
  }
}
```

### 12.11 Contenus additionnels atteignables au clavier

#### Correction — React / JSX

```tsx
// ❌ <div onClick={ouvrir}>Choisir une ville</div> puis <li onClick={choisir}>Paris</li>, sans tabindex ni flèches
// ✅ sous-menu ouvert à l’activation : le bouton annonce son état, les liens sont focalisables
<button type="button" aria-expanded={isOpen} aria-controls="sous-menu-demarches" onClick={() => setIsOpen(!isOpen)}>
  Démarches
</button>
<ul id="sous-menu-demarches" hidden={!isOpen}>
  <li><a href="/demarches/nouvelle">Nouvelle démarche</a></li>
  <li><a href="/demarches">Mes démarches</a></li>
</ul>
// ✅ liste de choix : la combobox de 7.1, dont les options s’atteignent par les flèches
```

#### Correction — Rails / ERB

```erb
<%# Composant Navigation principale du DSFR : sous-menu ouvert à l’activation, liens focalisables %>
<nav class="fr-nav" id="navigation" role="navigation" aria-label="Menu principal">
  <ul class="fr-nav__list">
    <li class="fr-nav__item">
      <button id="menu-demarches" aria-expanded="false" aria-controls="sous-menu-demarches" type="button" class="fr-nav__btn">Démarches</button>
      <div class="fr-collapse fr-menu" id="sous-menu-demarches">
        <ul class="fr-menu__list">
          <li>
            <a href="/demarches/nouvelle" class="fr-nav__link">Nouvelle démarche</a>
          </li>
          <li>
            <a href="/demarches" class="fr-nav__link">Mes démarches</a>
          </li>
        </ul>
      </div>
    </li>
  </ul>
</nav>
<%# Liste de choix : la liste native fr-select de 12.9 plutôt qu’une liste personnalisée %>
```

### 13.1 Limites de temps contrôlables

#### Correction — React / JSX

```tsx
// ❌ setTimeout(() => location.reload(), 5 * 60 * 1000);
// ✅ avant l’expiration, une modale propose de prolonger la session
const modaleRef = useRef(null);
useEffect(() => {
  const minuteur = setTimeout(() => modaleRef.current.showModal(), DUREE_SESSION - 2 * 60 * 1000);
  return () => clearTimeout(minuteur);
}, [derniereActivite]);

<dialog ref={modaleRef} aria-labelledby="titre-session">
  <h2 id="titre-session">Votre session expire dans 2 minutes</h2>
  <button type="button" onClick={prolongerSession}>Prolonger la session</button>
</dialog>
```

#### Correction — Rails / ERB

```erb
<%# ❌ <meta http-equiv="refresh" content="300"> dans le layout %>
<%# ✅ composant Modale du DSFR, ouvert par le contrôleur avant l’expiration %>
<dialog id="modale-session" class="fr-modal" aria-labelledby="modale-session-titre" data-controller="session" data-session-duree-value="1800">
  <div class="fr-container fr-container--fluid fr-container-md">
    <div class="fr-grid-row fr-grid-row--center">
      <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
        <div class="fr-modal__body">
          <div class="fr-modal__header">
            <button aria-controls="modale-session" title="Fermer" type="button" id="bouton-fermer-session" class="fr-btn--close fr-btn">Fermer</button>
          </div>
          <div class="fr-modal__content">
            <h2 id="modale-session-titre" class="fr-modal__title">
              Votre session expire dans 2 minutes
            </h2>
            <p>Prolongez-la pour garder les informations saisies.</p>
          </div>
          <div class="fr-modal__footer">
            <div class="fr-btns-group fr-btns-group--right fr-btns-group--inline-reverse fr-btns-group--inline-lg">
              <button type="button" class="fr-btn" data-action="click->session#prolonger">Prolonger la session</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</dialog>
```

```javascript
// app/javascript/controllers/session_controller.js
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static values = { duree: Number }

  connect() {
    this.programmer()
  }

  programmer() {
    clearTimeout(this.minuteur)
    this.minuteur = setTimeout(() => window.dsfr(this.element).modal.disclose(), (this.dureeValue - 120) * 1000)
  }

  async prolonger() {
    await fetch("/session/prolonger", { method: "POST", headers: { "X-CSRF-Token": document.querySelector("meta[name=csrf-token]").content } })
    window.dsfr(this.element).modal.conceal()
    this.programmer()
  }

  disconnect() {
    clearTimeout(this.minuteur)
  }
}
```

### 13.2 Pas d’ouverture de nouvelle fenêtre sans action de l’utilisateur

#### Correction — React / JSX

```tsx
// ❌ fenêtre ouverte sans action de la personne
useEffect(() => { window.open("/promo"); }, []);

// ✅ la personne choisit d’ouvrir le lien
<a href="/promo">Voir l’offre du moment</a>

// Bonne pratique, hors critère : signaler la nouvelle fenêtre par un texte masqué
<a href="/rapport.pdf" target="_blank" rel="noopener">
  Rapport annuel (PDF, 2 Mo)<span className="fr-sr-only"> - nouvelle fenêtre</span>
</a>
```

#### Correction — Rails / ERB

```erb
<%# ❌ contrôleur Stimulus dont connect() appelle window.open : voir le bloc JavaScript %>
<%# ✅ lien que la personne active %>
<a class="fr-link" href="/promo">Voir l’offre du moment</a>

<%# Bonne pratique, hors critère : le CSS du DSFR ajoute déjà une icône aux liens target="_blank" ; le texte masqué la complète au lecteur d’écran %>
<a class="fr-link" href="/rapport.pdf" target="_blank" rel="noopener">Rapport annuel (PDF, 2 Mo)<span class="fr-sr-only"> - nouvelle fenêtre</span></a>
```

```javascript
// ❌ app/javascript/controllers/promo_controller.js : fenêtre ouverte dès la connexion du contrôleur
connect() {
  window.open("/promo")
}
```

### 13.3–13.4 Documents bureautiques accessibles

#### Correction — React / JSX

```tsx
<a href="/rapport-2024.pdf" download>
  Télécharger le rapport annuel 2024 (PDF, 1,2 Mo)
</a>
<a href="/rapport-2024">Rapport annuel 2024, version HTML accessible</a>
```

#### Correction — Rails / ERB

```erb
<%# Composant Lien de téléchargement du DSFR, puis lien vers la version HTML %>
<a download="true" href="/rapport-2024.pdf" class="fr-link fr-link--download">Télécharger le rapport annuel 2024 <span class="fr-link__detail">PDF – 1,2 Mo</span>
</a>
<a class="fr-link" href="/rapport-2024">Rapport annuel 2024, version HTML accessible</a>

<%# Document dans une autre langue : hreflang, et la langue en toutes lettres dans le détail %>
<a hreflang="en" download="true" href="/annual-report-2024.pdf" class="fr-link fr-link--download">Télécharger le rapport annuel 2024 <span class="fr-link__detail">PDF – 1,1 Mo - Anglais</span>
</a>
```

### 13.5–13.6 Contenus cryptiques avec alternative pertinente

#### Correction — React / JSX

```tsx
// ❌ <span role="img" aria-label="Content">:-)</span> seul : rien n’est défini à l’écran
// ✅ attribut title sur une abréviation
<abbr title="Système d’immatriculation des véhicules">SIV</abbr>
// ✅ émoticône suivie de sa définition adjacente
<p>Votre demande est envoyée :-) (sourire)</p>
```

#### Correction — Rails / ERB

```erb
<%# ❌ <span role="img" aria-label="Content">:-)</span> seul : rien n’est défini à l’écran %>
<%# ✅ attribut title sur une abréviation %>
<abbr title="Système d’immatriculation des véhicules">SIV</abbr>
<%# ✅ émoticône suivie de sa définition adjacente %>
<p>Votre demande est envoyée :-) (sourire)</p>
```

### 13.7 Pas de flash dangereux

#### Correction — React / JSX

```css
/* ❌ fond de 400 × 300 px (120 000 px) qui alterne 5 fois par seconde */
.alerte { width: 400px; height: 300px; animation: clignote 0.2s infinite; }

/* ✅ au moins 1 s par cycle, ou pas de clignotement du tout */
.alerte { width: 400px; height: 300px; animation: clignote 1s 3; }

@keyframes clignote {
  50% { background-color: #000091; }
}
```

#### Correction — Rails / ERB

```css
/* ❌ fond de 400 × 300 px (120 000 px) qui alterne 5 fois par seconde */
.alerte { width: 400px; height: 300px; animation: clignote 0.2s infinite; }

/* ✅ au moins 1 s par cycle, ou pas de clignotement du tout */
.alerte { width: 400px; height: 300px; animation: clignote 1s 3; }

@keyframes clignote {
  50% { background-color: #000091; }
}
```

### 13.8 Contenus en mouvement contrôlables

#### Correction — React / JSX

```tsx
// ✅ bouton pour arrêter et relancer le défilement, dont le libellé suit l’état
<button type="button" onClick={() => setEnLecture(!enLecture)}>
  {enLecture ? "Mettre en pause le défilement" : "Relancer le défilement"}
</button>
```

```css
/* Complément : ne remplace pas le bouton */
@media (prefers-reduced-motion: reduce) {
  .carrousel__piste { animation: none; transition: none; }
}
```

#### Correction — Rails / ERB

```erb
<%# Bouton du DSFR avec icône ; le contrôleur change le libellé et l’icône selon l’état %>
<div data-controller="carrousel">
  <button type="button" class="fr-btn fr-icon-pause-circle-line fr-btn--icon-left fr-btn--secondary" data-carrousel-target="bouton" data-action="click->carrousel#basculer">Mettre en pause le défilement</button>
  ...
</div>
```

```javascript
// app/javascript/controllers/carrousel_controller.js
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static targets = ["bouton"]

  connect() {
    this.enLecture = true
    this.minuteur = setInterval(() => { if (this.enLecture) this.suivante() }, 7000)
  }

  basculer() {
    this.enLecture = !this.enLecture
    this.boutonTarget.textContent = this.enLecture ? "Mettre en pause le défilement" : "Relancer le défilement"
    this.boutonTarget.classList.toggle("fr-icon-pause-circle-line", this.enLecture)
    this.boutonTarget.classList.toggle("fr-icon-play-circle-line", !this.enLecture)
  }

  disconnect() {
    clearInterval(this.minuteur)
  }
}
```

```css
/* Complément : ne remplace pas le bouton */
@media (prefers-reduced-motion: reduce) {
  .carrousel__piste { animation: none; transition: none; }
}
```

### 13.9 Contenu consultable en portrait et en paysage

#### Correction — React / JSX

```css
/* ❌ contenu masqué en portrait */
@media (orientation: portrait) {
  .app { display: none; }
}

/* ✅ mise en page fluide, sans condition d’orientation */
.app {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
}
```

```tsx
// ❌ orientation imposée par script
useEffect(() => { screen.orientation.lock("landscape"); }, []);
```

#### Correction — Rails / ERB

```css
/* ❌ contenu masqué en portrait */
@media (orientation: portrait) {
  .app { display: none; }
}

/* ✅ mise en page fluide, sans condition d’orientation */
.app {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
}
```

```javascript
// ❌ orientation imposée par script, par exemple dans le connect() d’un contrôleur Stimulus
screen.orientation.lock("landscape")
```

### 13.10 Gestes complexes doublés par un geste simple

#### Correction — React / JSX

```tsx
// Le balayage reste possible, et des boutons font la même chose en un point unique
<div onTouchStart={debutBalayage} onTouchEnd={finBalayage}>{diapositives}</div>
<button type="button" onClick={precedente}>Diapositive précédente</button>
<button type="button" onClick={suivante}>Diapositive suivante</button>
```

#### Correction — Rails / ERB

```erb
<%# Boutons du DSFR avec icône, qui doublent le balayage %>
<div data-controller="carrousel">
  <div data-action="touchstart->carrousel#debutBalayage touchend->carrousel#finBalayage">...</div>
  <button type="button" class="fr-btn fr-icon-arrow-left-line fr-btn--icon-left fr-btn--tertiary" data-action="click->carrousel#precedente">Diapositive précédente</button>
  <button type="button" class="fr-btn fr-icon-arrow-right-line fr-btn--icon-right fr-btn--tertiary" data-action="click->carrousel#suivante">Diapositive suivante</button>
</div>
```

### 13.11 Actions au pointeur annulables

#### Correction — React / JSX

```tsx
// ❌ <button type="button" onMouseDown={supprimer}>Supprimer la demande</button>
// ✅ onClick part au relâchement
<button type="button" onClick={supprimer}>Supprimer la demande</button>
// ✅ action destructrice : confirmation avant, ou annulation après coup
<button type="button" onClick={() => confirmationRef.current.showModal()}>Supprimer la demande</button>
```

#### Correction — Rails / ERB

```erb
<%# ❌ data-action="mousedown->ligne#supprimer" %>
<%# ✅ click part au relâchement %>
<button type="button" class="fr-btn fr-btn--secondary" data-action="click->ligne#supprimer">Supprimer la demande</button>

<%# ✅ action destructrice : le bouton ouvre le composant Modale du DSFR, qui demande confirmation %>
<button data-fr-opened="false" aria-controls="modale-suppression" id="bouton-modale-suppression" type="button" class="fr-btn fr-btn--secondary">Supprimer la demande</button>
<dialog id="modale-suppression" class="fr-modal" aria-labelledby="modale-suppression-titre">
  <div class="fr-container fr-container--fluid fr-container-md">
    <div class="fr-grid-row fr-grid-row--center">
      <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
        <div class="fr-modal__body">
          <div class="fr-modal__header">
            <button aria-controls="modale-suppression" title="Fermer" type="button" id="bouton-fermer-suppression" class="fr-btn--close fr-btn">Fermer</button>
          </div>
          <div class="fr-modal__content">
            <h2 id="modale-suppression-titre" class="fr-modal__title">
              Supprimer la demande ?
            </h2>
            <p>La demande et ses pièces jointes seront supprimées.</p>
          </div>
          <div class="fr-modal__footer">
            <div class="fr-btns-group fr-btns-group--right fr-btns-group--inline-reverse fr-btns-group--inline-lg">
              <%= button_to "Confirmer la suppression", demande_path(@demande), method: :delete, class: "fr-btn" %>
              <button aria-controls="modale-suppression" type="button" class="fr-btn fr-btn--secondary">Annuler</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</dialog>
```

### 13.12 Fonctionnalités basées sur le mouvement de l’appareil

#### Correction — React / JSX

```tsx
// ✅ la même action par un bouton, et la détection du mouvement désactivable
useEffect(() => {
  if (!secousseActive) return;
  window.addEventListener("devicemotion", surSecousse);
  return () => window.removeEventListener("devicemotion", surSecousse);
}, [secousseActive]);

<button type="button" onClick={annulerDerniereAction}>Annuler la dernière action</button>
<label>
  <input type="checkbox" checked={secousseActive} onChange={() => setSecousseActive(!secousseActive)} />
  Annuler en secouant l’appareil
</label>
```

#### Correction — Rails / ERB

```erb
<%# Bouton du DSFR, et composant Interrupteur du DSFR pour désactiver la détection %>
<div data-controller="secousse" data-action="devicemotion@window->secousse#surMouvement">
  <button type="button" class="fr-btn" data-action="click->secousse#annuler">Annuler la dernière action</button>
  <div class="fr-toggle">
    <%# sans name : piloté en JavaScript (Stimulus), jamais envoyé %>
    <input type="checkbox" class="fr-toggle__input" id="secousse-active" aria-describedby="secousse-active-messages" data-secousse-target="interrupteur">
    <label class="fr-toggle__label" for="secousse-active">Annuler en secouant l’appareil</label>
    <div class="fr-messages-group" id="secousse-active-messages" aria-live="polite">
    </div>
  </div>
</div>
```

```javascript
// app/javascript/controllers/secousse_controller.js
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static targets = ["interrupteur"]

  surMouvement(event) {
    if (!this.interrupteurTarget.checked) return // détection désactivée : rien ne se déclenche
    if (this.estUneSecousse(event)) this.annuler()
  }
}
```

