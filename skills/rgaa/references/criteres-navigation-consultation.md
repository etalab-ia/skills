# RGAA — Thèmes 12–13 : Navigation, Consultation

## Thème 12 — Navigation (11 critères)

### 12.1 Deux systèmes de navigation minimum

Chaque ensemble de pages doit proposer au moins deux parmi :
- Menu de navigation
- Plan du site
- Moteur de recherche

**Test :** Sur chaque ensemble de pages, vérifier la présence de deux systèmes parmi le menu de navigation, le plan du site et le moteur de recherche. Le menu de navigation peut être un menu principal, un menu de sous-rubrique, un menu contextuel ou la table des matières d’un ensemble de pages. Les liens du pied de page (mentions légales, plan du site…) ne forment pas un menu de navigation principal. Le moteur de recherche porte sur les contenus de tout le site : un champ qui filtre une liste ou un catalogue ne compte pas. NA pour un site d’une seule page ou d’un nombre très limité de pages, et pour les pages d’un processus (démarche, paiement).
**Non-conformité type :** Site sans plan du site ni moteur de recherche, avec uniquement un menu de navigation.
**Impact :** avec un seul moyen de navigation, la personne qui ne peut pas l’utiliser (menu trop long à parcourir au clavier, au lecteur d’écran ou en fort zoom) n’a pas d’autre chemin vers les pages du site.
**Priorité :** 🟠 Majeur

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
                <input class="fr-input" aria-describedby="recherche-input-messages" placeholder="Rechercher" id="recherche-input" type="search">
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

---

### 12.2 Menu et barres de navigation à la même place

**Test :** Comparer deux pages d’un même ensemble : le menu et les barres de navigation (menu de navigation, fil d’Ariane, navigation d’une liste de résultats, liens d’évitement) sont à la même place dans la présentation et dans le même ordre relatif dans le code source. NA pour la page d’accueil, un site d’une seule page, les pages d’un processus (démarche, paiement), et un changement initié par la personne.
**Non-conformité type :** Menu en haut sur la page d’accueil, en latéral sur les pages intérieures ; ordre des entrées qui change selon les pages.
**Impact :** un menu qui change de place ou d’ordre oblige la personne qui navigue au lecteur d’écran, en fort zoom ou avec une commande vocale à le rechercher sur chaque page.
**Priorité :** 🟠 Majeur

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

---

### 12.3–12.5 Plan du site et moteur de recherche

12.3 : la page plan du site représente l’architecture générale du site, et ses liens mènent aux pages annoncées. 12.4 : elle s’atteint par la même fonctionnalité, à la même place et dans le même ordre relatif du code sur chaque ensemble de pages. 12.5 : même exigence pour le moteur de recherche. Sans page plan du site, 12.3 et 12.4 sont NA, et l’absence pèse sur 12.1. Sans moteur de recherche, 12.5 est NA. Un lien vers le plan du site absent d’une seule page relève de 12.4, pas de 12.3. Un champ qui filtre une liste n’est pas le moteur de recherche du site.

Les trois critères sont en jugement humain : NT, jamais C. L’absence de lien dans un gabarit ne prouve pas l’absence de plan du site sur le site : le NA ne vaut que si l’absence est connue (déclaration d’accessibilité, plan d’action).

**Test :** Parcourir le plan du site : il représente l’architecture générale du site (une page atteignable depuis l’accueil de sa rubrique peut ne pas y figurer), ses liens fonctionnent et mènent à la page qu’annonce leur intitulé. Comparer ensuite deux pages d’un même ensemble : l’accès au plan du site et l’accès au moteur de recherche passent par le même élément (lien, bouton, champ), à la même place dans la présentation et dans le même ordre relatif du code source.
**Non-conformité type :** Plan du site incomplet ou avec des liens cassés ; lien « Plan du site » dans le pied de page d’une page, dans l’en-tête d’une autre ; moteur de recherche absent de l’en-tête de certaines pages.
**Impact :** un plan du site incomplet, ou un accès qui change de place, prive de sa vue d’ensemble du site la personne qui ne peut pas parcourir les menus (au lecteur d’écran, en fort zoom).
**Priorité :** 🟡 Mineur

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

---

### 12.6 Zones de regroupement atteignables ou évitables

**Test :** Pour chaque zone présente dans la page (en-tête, navigation principale, contenu principal, pied de page, moteur de recherche), vérifier au moins une de ces conditions : un rôle landmark correspondant à sa nature (`banner`, `navigation`, `main`, `contentinfo`, `search`, implicite ou explicite) ; un titre qui en dit la nature ; un bouton qui précède directement la zone et permet de la masquer ; un lien d’évitement qui précède directement la zone ; un lien d’accès rapide visible, ou visible au focus. Différencier plusieurs `<nav>` par `aria-label` est une bonne pratique, pas une condition du critère. 9.2 juge la structure (un `<main>` unique et visible) ; 12.6 juge si chaque zone s’atteint ou s’évite : un contenu principal dans un simple `<div>` n’est NC en 12.6 que si aucun des cinq moyens ne permet de l’atteindre.
**Non-conformité type :** En-tête, contenu principal et pied de page dans des `<div>`, sans landmark, sans titre et sans lien d’évitement ou d’accès rapide.
**Impact :** impossible d’aller directement au contenu principal ou à la navigation : la personne qui utilise un lecteur d’écran parcourt toute la page pour les trouver.
**Priorité :** 🟠 Majeur

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

---

### 12.7 Lien d’évitement ou d’accès rapide au contenu principal

**Test :** Vérifier qu’un lien d’évitement précède directement le contenu principal (le `<main>` visible) dans l’ordre du code, ou qu’un lien d’accès rapide mène au contenu principal et devient visible au focus. Sur l’ensemble de pages, le lien est à la même place dans la présentation et dans le même ordre relatif du code, visible au focus, et fonctionnel : sa cible existe. Le placer en premier lien de la page est une bonne pratique, pas une exigence. NA possible pour un site d’une seule page, quand le lien est avéré inutile (ni navigation ni contenu additionnel).
**Non-conformité type :** Aucun lien d’évitement ni d’accès rapide ; lien dont la cible n’existe pas (`href="#contenu"` sans `id="contenu"`).
**Impact :** il faut traverser toute la navigation sur chaque page avant d’atteindre le contenu : la personne qui navigue au clavier répète des dizaines de tabulations à chaque page.
**Priorité :** 🔴 Bloquant

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

---

### 12.8 Ordre de tabulation cohérent

**Test :** Parcourir la page à la touche Tab puis Maj+Tab : l’ordre du focus reste cohérent avec le contenu. Suivre l’ordre de lecture naturel (de gauche à droite, de haut en bas) n’est pas obligatoire tant que l’ordre reste cohérent. Dans une modale ouverte, l’ordre ne considère que les éléments de la modale. Pour chaque contenu inséré ou mis à jour par script (élément affiché, réponse Ajax, Turbo Stream), activer le déclencheur et vérifier que le focus est repositionné de façon cohérente.
**Non-conformité type :** `tabindex="5"` qui fait passer un élément avant ceux qui le précèdent ; contenu inséré en fin de page, loin de son déclencheur, sans déplacement du focus ; modale ouverte dont le focus part vers la page située derrière (défaut aussi rattaché à 7.1 dans `impacts.md`).
**Impact :** le parcours saute d’une zone à l’autre et devient incompréhensible pour la personne qui navigue au clavier.
**Priorité :** 🟠 Majeur

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

---

### 12.9 Pas de piège au clavier

**Test :** Depuis chaque élément qui reçoit le focus, vérifier qu’on atteint l’élément focalisable suivant et le précédent avec Tab et Maj+Tab, ou par une autre interaction clavier dont la personne est informée. Pour un composant composite (groupe de boutons radio, liste de sélection, onglets, widget ARIA), les flèches servent à se déplacer à l’intérieur : le test se limite à vérifier qu’on atteint le composant à la tabulation et qu’on en sort vers le composant suivant ou précédent. Une modale qui garde le focus en son sein et se ferme par Échap ou par un bouton n’est pas un piège.
**Non-conformité type :** Liste déroulante personnalisée dont l’écouteur `keydown` annule Tab (`preventDefault`) quand elle est ouverte, sans la fermer ni rendre le focus ; widget tiers (éditeur riche, `<iframe>`) dont on ne sort pas au clavier, sans consigne.
**Impact :** impossible de sortir du composant : pour la personne qui navigue au clavier ou au contacteur, la suite de la page est hors d’atteinte.
**Priorité :** 🔴 Bloquant

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

---

### 12.10 Raccourcis clavier à une seule touche contrôlables

**Test :** Repérer les raccourcis clavier d’une seule touche (lettre minuscule ou majuscule, chiffre, ponctuation, symbole). Pour chacun, vérifier qu’un mécanisme permet de le désactiver, ou de le reconfigurer avec une touche de modification (Ctrl, Alt, Maj), ou qu’il n’agit que quand le composant auquel il est associé a le focus. Les `accesskey` ne sont pas concernés : ils exigent déjà une touche de modification.
**Non-conformité type :** Application avec des raccourcis `j` / `k` écoutés sur toute la page, qui se déclenchent pendant la saisie dans un champ de recherche.
**Impact :** un raccourci d’une seule touche se déclenche quand la personne dicte un texte avec une commande vocale, ou quand elle tape une touche par erreur au clavier : l’action part sans qu’elle l’ait voulue.
**Priorité :** 🟠 Majeur

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

---

### 12.11 Contenus additionnels atteignables au clavier

**Test :** Repérer les contenus additionnels qui apparaissent au survol, à la prise de focus ou à l’activation d’un composant (infobulle, sous-menu, liste déroulante personnalisée, panneau). Le critère est « si nécessaire » : il ne vise que les contenus qui contiennent des éléments avec lesquels on interagit (lien dans une infobulle, liens d’un sous-menu, options d’une liste), et vérifie qu’on les atteint au clavier. Une infobulle sans élément interactif rend 12.11 NA : son affichage et sa fermeture relèvent de 10.13 et 10.14. Un sous-menu affiché au seul `:hover` CSS est aussi NC en 10.14 : les deux NC se corrigent ensemble.
**Non-conformité type :** Sous-menu affiché seulement au survol (`mouseenter`, `:hover`), dont les liens ne s’atteignent pas au clavier ; liste déroulante personnalisée ouverte au clic, dont les options (`<li>` ou `<div>` sans `tabindex`, sans gestion des flèches) ne s’atteignent pas au clavier.
**Impact :** les liens ou les options d’un contenu affiché au survol ou au clic restent hors d’atteinte pour la personne qui navigue au clavier ou au contacteur.
**Priorité :** 🟠 Majeur

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

---

## Thème 13 — Consultation (12 critères)

### 13.1 Limites de temps contrôlables

**Test :** Repérer les limites de temps. Rafraîchissement (`<meta http-equiv="refresh">`, `<object>`, `<embed>`, `<svg>`, `<canvas>`) et redirection par script : la personne peut l’arrêter et le relancer, ou multiplier le délai par dix au moins, ou elle est avertie et dispose de 20 secondes au moins pour le prolonger, ou le délai atteint 20 heures au moins. Redirection par `<meta>` : immédiate (`content="0;URL=…"`). Session (après authentification, démarche en ligne) : la personne peut supprimer ou prolonger la limite, ou la session dure 20 heures au moins. L’avertissement 20 secondes avant ne figure que dans les conditions du rafraîchissement et de la redirection. NA quand la limite est essentielle (redirection d’une URL obsolète vers la nouvelle page).
**Non-conformité type :** Démarche en ligne qui expire après 30 minutes sans moyen de prolonger la session ; `<meta http-equiv="refresh" content="300">` qui recharge la page toutes les 5 minutes.
**Impact :** les données saisies sont perdues quand la session expire ou que la page se recharge : la personne qui lit ou saisit lentement, au lecteur d’écran, à la commande vocale ou au contacteur, n’a pas le temps de finir.
**Priorité :** 🔴 Bloquant

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

---

### 13.2 Pas d’ouverture de nouvelle fenêtre sans action de l’utilisateur

**Test :** Vérifier qu’à l’ouverture de la page aucune nouvelle fenêtre (pop-up, pop-under) ne s’ouvre sans action de la personne. Dans le code : `window.open` appelé au chargement (`DOMContentLoaded`, `load`, `useEffect` qui ne dépend d’aucune action, `connect()` d’un contrôleur Stimulus), formulaire `target="_blank"` soumis par script, clic simulé (`element.click()`) au chargement.
**Non-conformité type :** Pop-up publicitaire ou d’alerte ouverte au chargement de la page.
**Impact :** une fenêtre ouverte sans action déplace le focus et la lecture ailleurs : la personne qui utilise un lecteur d’écran, ou qui zoome et ne voit qu’une partie de l’écran, perd la page qu’elle consultait.
**Priorité :** 🟡 Mineur

**Hors critère :** un lien `target="_blank"` que la personne active n’est pas une NC au titre de 13.2, ni au titre de 6.1 tant que son intitulé reste explicite. Signaler la nouvelle fenêtre reste une bonne pratique. Si on la signale par un attribut `title`, il reprend l’intitulé visible du lien (exigence de 6.1).

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

---

### 13.3–13.4 Documents bureautiques accessibles

13.3 : chaque document bureautique en téléchargement est accessible, ou a une version accessible (bureautique ou HTML). 13.4 : cette version donne la même information. Sans version accessible, la NC va à 13.3 (si le document en exige une) et 13.4 est NA. Une version accessible incomplète rend 13.4 NC, pas 13.3. Un fichier `.txt` n’est jamais une version accessible.

Les deux critères sont en jugement humain : NT, jamais C.

**Test :** Repérer les liens et les contrôles de formulaire qui téléchargent un document bureautique (PDF, DOCX, ODT, EPUB). Ouvrir chaque document, ou sa version alternative, et vérifier qu’il est accessible (PAC pour un PDF, vérificateur d’accessibilité de Microsoft Office pour un DOCX). Comparer ensuite le document et sa version accessible : ils donnent la même information.
**Non-conformité type :** PDF scanné sans OCR ni balisage d’accessibilité ; DOCX sans structure de titres ; version HTML qui omet une partie du document (NC en 13.4).
**Impact :** un PDF scanné ou sans balisage ne restitue rien d’exploitable au lecteur d’écran ni à la plage braille, et ne se reformate pas à l’agrandissement.
**Priorité :** 🟠 Majeur

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

---

### 13.5–13.6 Contenus cryptiques avec alternative pertinente

13.5 : chaque contenu cryptique (art ASCII, émoticône, syntaxe cryptique) a une alternative : un attribut `title` (sur un lien, un champ, une `<abbr>`) ou une définition dans le contexte adjacent. 13.6 : cette alternative explique le contenu. Sans alternative : NC en 13.5 et NA en 13.6. Alternative présente mais fausse : NC en 13.6.

13.6 est en jugement humain : NT, jamais C.

**Test :** Repérer les contenus cryptiques (art ASCII, émoticône, sigle ou syntaxe cryptique). Pour chacun, vérifier qu’une définition est donnée par un attribut `title`, ou par le contexte adjacent, immédiatement avant ou après. Juger ensuite que cette définition explique le contenu. `role="img"` avec `aria-label` n’est pas une des deux conditions : il sert le lecteur d’écran, mais ne donne aucune définition à la personne qui lit l’écran. Le garder seulement en complément d’une définition visible.
**Non-conformité type :** Émoticône `:-)` sans attribut `title` ni définition adjacente ; art ASCII sans description.
**Impact :** une émoticône ou un art ASCII est lu caractère par caractère au lecteur d’écran (« deux-points tiret parenthèse ») ; une syntaxe cryptique sans définition reste opaque pour la personne qui a besoin de consignes explicites.
**Priorité :** 🟡 Mineur

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

---

### 13.7 Pas de flash dangereux

**Test :** Repérer les contenus qui provoquent un changement brusque de luminosité ou un effet de flash, selon leur origine : image ou élément multimédia (`<video>`, `<img>`, `<svg>`, `<canvas>`, `<embed>`, `<object>`, test 13.7.1), script (13.7.2) ou mise en forme CSS (13.7.3). Pour chacun, vérifier une de ces conditions : la fréquence de l’effet est inférieure à 3 par seconde, ou la surface totale cumulée des effets est inférieure ou égale à 21 824 pixels. L’effet est non conforme seulement si les deux conditions échouent. Lorsque l’effet est géré par un script ou au moyen de CSS, l’analyse du code est suffisante (note de la méthodologie du test 13.7.1) : la fréquence se déduit de la durée de l’animation ou de l’intervalle du script (une paire de changements opposés de luminosité compte pour un flash : une animation de 0,2 s par cycle, ou une bascule toutes les 100 ms, donne 5 flashs par seconde ; compter les passages au sombre dans les keyframes : trois passages dans un cycle d’1 s font 3 flashs par seconde), la surface des dimensions des éléments qui changent en même temps. Quand ces valeurs ne se lisent pas dans le code (variable CSS, calcul à l’exécution, dimensions en `vw` ou `%`, `rem` ou `em` sans taille de police de référence fixée en `px`), NT. Les vidéos et images animées s’observent au rendu (l’outil PEAT analyse par exemple les vidéos au format .avi).
**Non-conformité type :** Fond d’alerte de 400 × 300 px qui clignote 3 fois par seconde ou plus ; effet stroboscopique dans une vidéo.
**Impact :** risque de crise d’épilepsie pour la personne photosensible.
**Priorité :** 🔴 Bloquant

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

---

### 13.8 Contenus en mouvement contrôlables

**Test :** Repérer les contenus en mouvement ou clignotants lancés automatiquement (au chargement, ou à l’affichage d’un contenu) par une image, un script ou du CSS. Pour chacun, vérifier que le mouvement dure 5 secondes au plus, ou qu’un mécanisme (un bouton, par exemple) permet de l’arrêter et de le relancer, ou de masquer et de réafficher le contenu, ou d’afficher toute l’information sans mouvement. Une pause seulement au survol ou à la prise de focus n’est pas conforme. NA quand le mouvement ne peut pas être arrêté (barre de progression). Respecter `prefers-reduced-motion` est une bonne pratique : il ne remplace pas le bouton.
**Non-conformité type :** Carrousel à défilement automatique sans bouton pause ; carrousel qui ne s’arrête qu’au survol ou au focus.
**Impact :** un contenu qui bouge sans pouvoir l’arrêter provoque nausées et vertiges, et empêche de se concentrer sur la lecture ; la personne qui lit lentement ou au lecteur d’écran voit le contenu changer avant la fin de sa lecture.
**Priorité :** 🟠 Majeur

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

---

### 13.9 Contenu consultable en portrait et en paysage

**Test :** Consulter la page en portrait puis en paysage : la consultation est possible dans les deux orientations, et le contenu reste le même, même si sa présentation change. Dans le code, repérer un blocage de l’orientation : `screen.orientation.lock()`, ou une media query `orientation` qui masque le contenu. NA quand l’orientation est essentielle (jeu, piano, dépôt de chèque).
**Non-conformité type :** Application bloquée en portrait, avec le message « Veuillez tourner votre appareil », sans justification fonctionnelle.
**Impact :** l’écran fixé sur un support, par exemple sur un fauteuil roulant, ne peut pas pivoter : un contenu bloqué dans une orientation reste inaccessible à la personne qui l’utilise.
**Priorité :** 🟠 Majeur

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

---

### 13.10 Gestes complexes doublés par un geste simple

**Test :** Repérer les fonctionnalités utilisables par un contact multipoint (pincer pour zoomer) ou par une trajectoire (balayer, glisser, tracer). Pour chacune, vérifier qu’elle reste disponible par un contact en un point unique : boutons « précédent » et « suivant », « plus » et « moins », pressions successives. Hors champ : les gestes du navigateur ou du système, et les gestes essentiels (tracé d’une signature).
**Non-conformité type :** Carrousel navigable uniquement par balayage, sans boutons précédent et suivant.
**Impact :** la personne qui pointe avec un seul doigt, un stylet, une souris de tête ou une commande vocale ne peut pas balayer ni pincer : la fonctionnalité lui reste inaccessible.
**Priorité :** 🟠 Majeur

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

---

### 13.11 Actions au pointeur annulables

**Test :** Repérer les actions déclenchées au pointeur sur un point unique (clic, toucher). Pour chacune, vérifier que l’action part au relâchement (c’est le cas de `click`, de `onClick`, d’un lien ou d’un bouton natif), ou qu’elle part à l’appui et s’annule au relâchement, ou qu’un mécanisme permet de l’abandonner avant la fin ou de l’annuler après (modale de confirmation, glisser-déposer abandonné quand on relâche hors de la cible). Un écouteur d’appui (`mousedown`, `pointerdown`, `touchstart`) qui ne déclenche aucune action, par exemple pour mémoriser le point de départ d’un clic sur le fond d’une modale, n’est pas une NC. NA quand l’action doit partir à l’appui (clavier virtuel dont les touches agissent à la pression).
**Non-conformité type :** Bouton de suppression déclenché au `mousedown`, sans confirmation possible.
**Impact :** la personne qui a des tremblements, ou qui pointe avec un dispositif peu précis, déclenche une action en posant le pointeur au mauvais endroit, sans pouvoir l’annuler en le glissant hors du bouton.
**Priorité :** 🟠 Majeur

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

---

### 13.12 Fonctionnalités basées sur le mouvement de l’appareil

**Test :** Repérer les fonctionnalités déclenchées en bougeant l’appareil (secousse, inclinaison) ou par un geste en direction de l’appareil. Pour chacune, vérifier qu’un composant d’interface permet d’accomplir la même chose, et que la personne peut désactiver la détection du mouvement pour éviter un déclenchement accidentel. Hors champ : le mouvement essentiel à la fonctionnalité (podomètre), et la détection utilisée à travers une interface compatible avec l’accessibilité.
**Non-conformité type :** Fonctionnalité « secouer pour annuler » sans bouton équivalent dans l’interface.
**Impact :** la personne dont l’appareil est fixé sur un support ne peut pas le secouer ni l’incliner ; celle qui a des mouvements involontaires déclenche la fonctionnalité sans le vouloir.
**Priorité :** 🟠 Majeur

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
