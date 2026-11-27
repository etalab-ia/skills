# En-tête : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Header minimal

```html
<header role="banner" class="fr-header">
    <div class="fr-header__body">
        <div class="fr-container">
            <div class="fr-header__body-row">
                <div class="fr-header__brand fr-enlarge-link">
                    <div class="fr-header__brand-top">
                        <div class="fr-header__logo">
                            <a href="/" title="Accueil - Nom de l’entité (ministère, secrétariat d‘état, gouvernement)">
                                <p class="fr-logo">
                                    Intitulé
                                    <br>officiel
                                </p>
                            </a>
                        </div>
                        <div class="fr-header__navbar">
                            <button data-fr-opened="false" aria-controls="modal-1860" title="Menu" type="button" id="button-1861" class="fr-btn--menu fr-btn">Menu</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="fr-header__menu fr-modal" id="modal-1860" aria-labelledby="button-1861">
        <div class="fr-container">
            <button aria-controls="modal-1860" title="Fermer" type="button" id="button-1863" class="fr-btn--close fr-btn">Fermer</button>
            <div class="fr-header__menu-links">
            </div>
            <nav class="fr-nav" id="navigation-1864" role="navigation" aria-label="Menu principal">
                <ul class="fr-nav__list">
                    <li class="fr-nav__item">
                        <a id="nav-1865" type="link" href="#" class="fr-nav__link">accès direct nav-1865</a>
                    </li>
                    <li class="fr-nav__item">
                        <a id="nav-1866" type="link" href="#" class="fr-nav__link">accès direct nav-1866</a>
                    </li>
                    <li class="fr-nav__item">
                        <a id="nav-1867" type="link" href="#" class="fr-nav__link">accès direct nav-1867</a>
                    </li>
                    <li class="fr-nav__item">
                        <a id="nav-1868" type="link" href="#" class="fr-nav__link">accès direct nav-1868</a>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</header>
```

### Header sans navigation

```html
<header role="banner" class="fr-header">
    <div class="fr-header__body">
        <div class="fr-container">
            <div class="fr-header__body-row">
                <div class="fr-header__brand fr-enlarge-link">
                    <div class="fr-header__brand-top">
                        <div class="fr-header__logo">
                            <p class="fr-logo">
                                Intitulé
                                <br>officiel
                            </p>
                        </div>
                    </div>
                    <div class="fr-header__service">
                        <a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - Nom de l’entité (ministère, secrétariat d‘état, gouvernement)">
                            <p class="fr-header__service-title">
                                Nom du site / service
                            </p>
                        </a>
                        <p class="fr-header__service-tagline">baseline - précisions sur l‘organisation</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</header>
```

### Header sans navigation avec un seul raccourci

```html
<header role="banner" class="fr-header">
    <div class="fr-header__body">
        <div class="fr-container">
            <div class="fr-header__body-row">
                <div class="fr-header__brand fr-enlarge-link">
                    <div class="fr-header__brand-top">
                        <div class="fr-header__logo">
                            <p class="fr-logo">
                                Intitulé
                                <br>officiel
                            </p>
                        </div>
                        <div class="fr-header__navbar">
                            <button data-fr-opened="false" aria-controls="modal-1874" title="Menu" type="button" id="button-1875" class="fr-btn--menu fr-btn">Menu</button>
                        </div>
                    </div>
                    <div class="fr-header__service">
                        <a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - Nom de l’entité (ministère, secrétariat d‘état, gouvernement)">
                            <p class="fr-header__service-title">
                                Nom du site / service
                            </p>
                        </a>
                        <p class="fr-header__service-tagline">baseline - précisions sur l‘organisation</p>
                    </div>
                </div>
                <div class="fr-header__tools">
                    <div class="fr-header__tools-links">
                        <div class="fr-btns-group">
                            <a href="[url - à modifier]" class="fr-btn--account fr-btn fr-btn">Espace particulier</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="fr-header__menu fr-modal" id="modal-1874" aria-labelledby="button-1875">
        <div class="fr-container">
            <button aria-controls="modal-1874" title="Fermer" type="button" id="button-1876" class="fr-btn--close fr-btn">Fermer</button>
            <div class="fr-header__menu-links">
            </div>
        </div>
    </div>
</header>
```

### Header sans navigation avec une liste de raccourcis

```html
<header role="banner" class="fr-header">
    <div class="fr-header__body">
        <div class="fr-container">
            <div class="fr-header__body-row">
                <div class="fr-header__brand fr-enlarge-link">
                    <div class="fr-header__brand-top">
                        <div class="fr-header__logo">
                            <p class="fr-logo">
                                Intitulé
                                <br>officiel
                            </p>
                        </div>
                        <div class="fr-header__navbar">
                            <button data-fr-opened="false" aria-controls="modal-1881" title="Menu" type="button" id="button-1882" class="fr-btn--menu fr-btn">Menu</button>
                        </div>
                    </div>
                    <div class="fr-header__service">
                        <a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - Nom de l’entité (ministère, secrétariat d‘état, gouvernement)">
                            <p class="fr-header__service-title">
                                Nom du site / service
                            </p>
                        </a>
                        <p class="fr-header__service-tagline">baseline - précisions sur l‘organisation</p>
                    </div>
                </div>
                <div class="fr-header__tools">
                    <div class="fr-header__tools-links">
                        <ul class="fr-btns-group">
                            <li>
                                <a href="[url - à modifier]" class="fr-btn--team fr-btn">Contact</a>
                            </li>
                            <li>
                                <a href="[url - à modifier]" class="fr-btn--briefcase fr-btn">Espace recruteur</a>
                            </li>
                            <li>
                                <a href="[url - à modifier]" class="fr-btn--account fr-btn">Espace particulier</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="fr-header__menu fr-modal" id="modal-1881" aria-labelledby="button-1882">
        <div class="fr-container">
            <button aria-controls="modal-1881" title="Fermer" type="button" id="button-1883" class="fr-btn--close fr-btn">Fermer</button>
            <div class="fr-header__menu-links">
            </div>
        </div>
    </div>
</header>
```

### Header avec Navigation complète

Extrait complet : [exemples/header-avec-navigation-complete-1.html](exemples/header-avec-navigation-complete-1.html) (41 ko)

### Header avec selecteur de langues

Extrait complet : [exemples/header-avec-selecteur-de-langues-2.html](exemples/header-avec-selecteur-de-langues-2.html) (41 ko)

### Header avec selecteur de langues et raccourcis

Extrait complet : [exemples/header-avec-selecteur-de-langues-et-raccourcis-3.html](exemples/header-avec-selecteur-de-langues-et-raccourcis-3.html) (42 ko)

### Header avec selecteur de langues et paramètre d'affichage

Extrait complet : [exemples/header-avec-selecteur-de-langues-et-parametre-d-af-4.html](exemples/header-avec-selecteur-de-langues-et-parametre-d-af-4.html) (42 ko)

### Header avec nom de service, lien d’accès

```html
<header role="banner" class="fr-header">
    <div class="fr-header__body">
        <div class="fr-container">
            <div class="fr-header__body-row">
                <div class="fr-header__brand fr-enlarge-link">
                    <div class="fr-header__brand-top">
                        <div class="fr-header__logo">
                            <p class="fr-logo">
                                Intitulé
                                <br>officiel
                            </p>
                        </div>
                        <div class="fr-header__navbar">
                            <button data-fr-opened="false" aria-controls="modal-3190" title="Menu" type="button" id="button-3191" class="fr-btn--menu fr-btn">Menu</button>
                        </div>
                    </div>
                    <div class="fr-header__service">
                        <a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - Nom de l’entité (ministère, secrétariat d‘état, gouvernement)">
                            <p class="fr-header__service-title">
                                Nom du site / service
                            </p>
                        </a>
                        <p class="fr-header__service-tagline">baseline - précisions sur l‘organisation</p>
                    </div>
                </div>
                <div class="fr-header__tools">
                    <div class="fr-header__tools-links">
                        <ul class="fr-btns-group">
                            <li>
                                <a href="[url - à modifier]" class="fr-btn--team fr-btn">Contact</a>
                            </li>
                            <li>
                                <a href="[url - à modifier]" class="fr-btn--briefcase fr-btn">Espace recruteur</a>
                            </li>
                            <li>
                                <a href="[url - à modifier]" class="fr-btn--account fr-btn">Espace particulier</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="fr-header__menu fr-modal" id="modal-3190" aria-labelledby="button-3191">
        <div class="fr-container">
            <button aria-controls="modal-3190" title="Fermer" type="button" id="button-3193" class="fr-btn--close fr-btn">Fermer</button>
            <div class="fr-header__menu-links">
            </div>
            <nav class="fr-nav" id="navigation-3194" role="navigation" aria-label="Menu principal">
                <ul class="fr-nav__list">
                    <li class="fr-nav__item">
                        <a id="nav-3195" type="link" href="#" class="fr-nav__link">accès direct nav-3195</a>
                    </li>
                    <li class="fr-nav__item">
                        <a id="nav-3196" type="link" href="#" class="fr-nav__link">accès direct nav-3196</a>
                    </li>
                    <li class="fr-nav__item">
                        <a id="nav-3197" type="link" href="#" class="fr-nav__link">accès direct nav-3197</a>
                    </li>
                    <li class="fr-nav__item">
                        <a id="nav-3198" type="link" href="#" class="fr-nav__link">accès direct nav-3198</a>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</header>
```

### Header avec nom de service, recherche

```html
<header role="banner" class="fr-header">
    <div class="fr-header__body">
        <div class="fr-container">
            <div class="fr-header__body-row">
                <div class="fr-header__brand fr-enlarge-link">
                    <div class="fr-header__brand-top">
                        <div class="fr-header__logo">
                            <p class="fr-logo">
                                Intitulé
                                <br>officiel
                            </p>
                        </div>
                        <div class="fr-header__navbar">
                            <button data-fr-opened="false" aria-controls="modal-3216" title="Rechercher" type="button" id="button-3217" class="fr-btn--search fr-btn">Rechercher</button>
                            <button data-fr-opened="false" aria-controls="modal-3218" title="Menu" type="button" id="button-3219" class="fr-btn--menu fr-btn">Menu</button>
                        </div>
                    </div>
                    <div class="fr-header__service">
                        <a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - Nom de l’entité (ministère, secrétariat d‘état, gouvernement)">
                            <p class="fr-header__service-title">
                                Nom du site / service
                            </p>
                        </a>
                    </div>
                </div>
                <div class="fr-header__tools">
                    <div class="fr-header__search fr-modal" id="modal-3216" aria-labelledby="button-3217">
                        <div class="fr-container fr-container-lg--fluid">
                            <button aria-controls="modal-3216" title="Fermer" type="button" id="button-3221" class="fr-btn--close fr-btn">Fermer</button>
                            <div class="fr-search-bar" id="search-3215" role="search">
                                <label class="fr-label" for="search-3215-input">
                                    Rechercher
                                </label>
                                <input class="fr-input" aria-describedby="search-3215-input-messages" placeholder="Rechercher" id="search-3215-input" type="search">
                                <div class="fr-messages-group" id="search-3215-input-messages" aria-live="polite">
                                </div>
                                <button title="Rechercher" type="submit" id="search-btn-3223" class="fr-btn">Rechercher</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="fr-header__menu fr-modal" id="modal-3218" aria-labelledby="button-3219">
        <div class="fr-container">
            <button aria-controls="modal-3218" title="Fermer" type="button" id="button-3224" class="fr-btn--close fr-btn">Fermer</button>
            <div class="fr-header__menu-links">
            </div>
            <nav class="fr-nav" id="navigation-3225" role="navigation" aria-label="Menu principal">
                <ul class="fr-nav__list">
                    <li class="fr-nav__item">
                        <a id="nav-3226" type="link" href="#" class="fr-nav__link">accès direct nav-3226</a>
                    </li>
                    <li class="fr-nav__item">
                        <a id="nav-3227" type="link" href="#" class="fr-nav__link">accès direct nav-3227</a>
                    </li>
                    <li class="fr-nav__item">
                        <a id="nav-3228" type="link" href="#" class="fr-nav__link">accès direct nav-3228</a>
                    </li>
                    <li class="fr-nav__item">
                        <a id="nav-3229" type="link" href="#" class="fr-nav__link">accès direct nav-3229</a>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</header>
```

### Header avec logo opérateur vertical, recherche

Extrait complet : [exemples/header-avec-logo-operateur-vertical-recherche-5.html](exemples/header-avec-logo-operateur-vertical-recherche-5.html) (4 ko)

### Header avec logo opérateur horizontal, nom de service, lien d’accès, recherche

Extrait complet : [exemples/header-avec-logo-operateur-horizontal-nom-de-servi-6.html](exemples/header-avec-logo-operateur-horizontal-nom-de-servi-6.html) (5 ko)

### Header avec raccourcis dupliqués, pour Angular, React et Vue

```html
<header role="banner" class="fr-header">
    <div class="fr-header__body">
        <div class="fr-container">
            <div class="fr-header__body-row">
                <div class="fr-header__brand fr-enlarge-link">
                    <div class="fr-header__brand-top">
                        <div class="fr-header__logo">
                            <a href="/" title="Accueil - Nom de l’entité (ministère, secrétariat d‘état, gouvernement)">
                                <p class="fr-logo">
                                    Intitulé
                                    <br>officiel
                                </p>
                            </a>
                        </div>
                        <div class="fr-header__navbar">
                            <button data-fr-opened="false" aria-controls="modal-3296" title="Menu" type="button" id="button-3297" class="fr-btn--menu fr-btn">Menu</button>
                        </div>
                    </div>
                </div>
                <div class="fr-header__tools">
                    <div class="fr-header__tools-links">
                        <ul class="fr-btns-group">
                            <li>
                                <a href="[url - à modifier]" class="fr-btn--team fr-btn">Contact</a>
                            </li>
                            <li>
                                <a href="[url - à modifier]" class="fr-btn--briefcase fr-btn">Espace recruteur</a>
                            </li>
                            <li>
                                <a href="[url - à modifier]" class="fr-btn--account fr-btn">Espace particulier</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="fr-header__menu fr-modal" id="modal-3296" aria-labelledby="button-3297">
        <div class="fr-container">
            <button aria-controls="modal-3296" title="Fermer" type="button" id="button-3298" class="fr-btn--close fr-btn">Fermer</button>
            <div class="fr-header__menu-links">
                <ul class="fr-btns-group">
                    <li>
                        <a href="[url - à modifier]" class="fr-btn--team fr-btn fr-btn">Contact</a>
                    </li>
                    <li>
                        <a href="[url - à modifier]" class="fr-btn--briefcase fr-btn fr-btn">Espace recruteur</a>
                    </li>
                    <li>
                        <a href="[url - à modifier]" class="fr-btn--account fr-btn fr-btn">Espace particulier</a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</header>
```

### Header avec bandeau BETA

Extrait complet : [exemples/header-avec-bandeau-beta-7.html](exemples/header-avec-bandeau-beta-7.html) (5 ko)

### Header logo opérateur + bandeau BETA

Extrait complet : [exemples/header-logo-operateur-bandeau-beta-8.html](exemples/header-logo-operateur-bandeau-beta-8.html) (5 ko)

### Header min avec bandeau BETA

```html
<header role="banner" class="fr-header">
    <div class="fr-header__body">
        <div class="fr-container">
            <div class="fr-header__body-row">
                <div class="fr-header__brand fr-enlarge-link">
                    <div class="fr-header__brand-top">
                        <div class="fr-header__logo">
                            <a href="/" title="Accueil - Nom de l’entité (ministère, secrétariat d‘état, gouvernement)">
                                <p class="fr-logo">
                                    Intitulé
                                    <br>officiel
                                </p>
                            </a>
                        </div>
                        <div class="fr-header__navbar">
                            <button data-fr-opened="false" aria-controls="modal-3371" title="Menu" type="button" id="button-3372" class="fr-btn--menu fr-btn">Menu</button>
                        </div>
                    </div>
                    <div class="fr-header__service">
                        <p class="fr-header__service-title">
                            <span class="fr-badge fr-badge--sm fr-badge--green-emeraude">BETA</span>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="fr-header__menu fr-modal" id="modal-3371" aria-labelledby="button-3372">
        <div class="fr-container">
            <button aria-controls="modal-3371" title="Fermer" type="button" id="button-3374" class="fr-btn--close fr-btn">Fermer</button>
            <div class="fr-header__menu-links">
            </div>
            <nav class="fr-nav" id="navigation-3375" role="navigation" aria-label="Menu principal">
                <ul class="fr-nav__list">
                    <li class="fr-nav__item">
                        <a id="nav-3376" type="link" href="#" class="fr-nav__link">accès direct nav-3376</a>
                    </li>
                    <li class="fr-nav__item">
                        <a id="nav-3377" type="link" href="#" class="fr-nav__link">accès direct nav-3377</a>
                    </li>
                    <li class="fr-nav__item">
                        <a id="nav-3378" type="link" href="#" class="fr-nav__link">accès direct nav-3378</a>
                    </li>
                    <li class="fr-nav__item">
                        <a id="nav-3379" type="link" href="#" class="fr-nav__link">accès direct nav-3379</a>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</header>
```

## Dépréciation

### Header déprécié

Les exemples suivants sont dépréciés, ne pas utiliser comme référence Pour support des versions précédentes

Extrait complet : [exemples/header-deprecie-9.html](exemples/header-deprecie-9.html) (41 ko)
