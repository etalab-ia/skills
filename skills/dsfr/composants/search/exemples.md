# Barre de recherche : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Barre de recherche MD (par défaut)

```html
<div class="fr-search-bar" id="search-955" role="search">
    <label class="fr-label" for="search-955-input">
        Rechercher
    </label>
    <input class="fr-input" aria-describedby="search-955-input-messages" placeholder="Rechercher" id="search-955-input" type="search">
    <div class="fr-messages-group" id="search-955-input-messages" aria-live="polite">
    </div>
    <button title="Rechercher" type="submit" id="search-btn-956" class="fr-btn">Rechercher</button>
</div>
```

### Barre de recherche LG

```html
<div class="fr-search-bar fr-search-bar--lg" id="search-960" role="search">
    <label class="fr-label" for="search-960-input">
        Rechercher
    </label>
    <input class="fr-input" aria-describedby="search-960-input-messages" placeholder="Rechercher" id="search-960-input" type="search">
    <div class="fr-messages-group" id="search-960-input-messages" aria-live="polite">
    </div>
    <button type="submit" id="search-btn-961" class="fr-btn">Rechercher</button>
</div>
```

### Barre de recherche avec libellé

```html
<div class="fr-search-bar fr-search-bar--labelled" id="search-965" role="search">
    <label class="fr-label" for="search-965-input">
        Rechercher un xxx
    </label>
    <input class="fr-input" aria-describedby="search-965-input-messages" placeholder="Rechercher" id="search-965-input" type="search">
    <div class="fr-messages-group" id="search-965-input-messages" aria-live="polite">
    </div>
    <button title="Rechercher" type="submit" id="search-btn-966" class="fr-btn">Rechercher</button>
</div>
```

### Barre de recherche avec message d'erreur

```html
<div class="fr-search-bar" id="search-970" role="search">
    <label class="fr-label" for="search-970-input">
        Rechercher
    </label>
    <input class="fr-input fr-input--error" aria-describedby="search-970-input-messages" placeholder="Rechercher" id="search-970-input" type="search">
    <div class="fr-messages-group" id="search-970-input-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="search-970-input-message-error">Message d'erreur</p>
    </div>
    <button title="Rechercher" type="submit" id="search-btn-971" class="fr-btn">Rechercher</button>
</div>
```
