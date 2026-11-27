# Tuile : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### tuile verticale md, taille par défaut

dans une grille sur 3 à 6 colonnes en version desktop

```html
<div class="fr-tile fr-enlarge-link" id="tile-7519">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__desc">Lorem [...] elit ut.</p>
            <p class="fr-tile__detail">Détail (optionel)</p>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### tuile taille sm

dans une grille sur 2 à 4 colonnes en version desktop

```html
<div class="fr-tile fr-tile--sm fr-enlarge-link" id="tile-7522">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__desc">Lorem [...] elit ut.</p>
            <p class="fr-tile__detail">Détail (optionel)</p>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile sans image cas max

```html
<div class="fr-tile fr-enlarge-link" id="tile-7526">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__desc">Lorem [...] elit ut.</p>
            <p class="fr-tile__detail">Détail (optionel)</p>
            <div class="fr-tile__start">
                <p class="fr-badge fr-badge--purple-glycine">Libellé badge</p>
            </div>
        </div>
    </div>
</div>
```

### Tuile sans image, minimum

```html
<div class="fr-tile fr-enlarge-link" id="tile-7529">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
        </div>
    </div>
</div>
```

### Tuile titre et description

```html
<div class="fr-tile fr-enlarge-link" id="tile-7532">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__desc">Lorem [...] elit ut.</p>
        </div>
    </div>
</div>
```

### Tuile titre et détails

```html
<div class="fr-tile fr-enlarge-link" id="tile-7535">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__detail">Détail (optionel)</p>
        </div>
    </div>
</div>
```

### Tuile verticale avec badge dans le contenu

```html
<div class="fr-tile fr-enlarge-link" id="tile-7539">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__desc">Lorem [...] elit ut.</p>
            <div class="fr-tile__start">
                <p class="fr-badge fr-badge--purple-glycine">Libellé badge</p>
            </div>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile verticale avec tag dans le contenu

```html
<div class="fr-tile fr-enlarge-link" id="tile-7542">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__desc">Lorem [...] elit ut.</p>
            <div class="fr-tile__start">
                <p class="fr-tag">Libellé tag</p>
            </div>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile verticale avec détail

```html
<div class="fr-tile fr-enlarge-link" id="tile-7545">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__detail">Détail (optionel)</p>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile verticale sm avec détails et badge

```html
<div class="fr-tile fr-tile--sm fr-enlarge-link" id="tile-7548">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__desc">Lorem [...] elit ut.</p>
            <p class="fr-tile__detail">Détail (optionel)</p>
            <div class="fr-tile__start">
                <p class="fr-badge fr-badge--purple-glycine">Libellé badge</p>
            </div>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile verticale sm avec détails et tag

```html
<div class="fr-tile fr-tile--sm fr-enlarge-link" id="tile-7551">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__desc">Lorem [...] elit ut.</p>
            <p class="fr-tile__detail">Détail (optionel)</p>
            <div class="fr-tile__start">
                <p class="fr-tag">Libellé tag</p>
            </div>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile verticale variation accentuée en contrast grey

```html
<div class="fr-tile fr-tile--grey fr-enlarge-link" id="tile-7555">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__desc">Lorem [...] elit ut.</p>
            <div class="fr-tile__start">
                <p class="fr-badge fr-badge--purple-glycine">Libellé badge</p>
            </div>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile verticale variation sans bordure

```html
<div class="fr-tile fr-tile--no-border fr-enlarge-link" id="tile-7558">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__desc">Lorem [...] elit ut.</p>
            <div class="fr-tile__start">
                <p class="fr-badge fr-badge--purple-glycine">Libellé badge</p>
            </div>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile verticale variation sans fond

```html
<div class="fr-tile fr-tile--no-background fr-enlarge-link" id="tile-7561">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__desc">Lorem [...] elit ut.</p>
            <div class="fr-tile__start">
                <p class="fr-badge fr-badge--purple-glycine">Libellé badge</p>
            </div>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile verticale variation ombre portée

```html
<div class="fr-tile fr-tile--shadow fr-enlarge-link" id="tile-7564">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__desc">Lorem [...] elit ut.</p>
            <div class="fr-tile__start">
                <p class="fr-badge fr-badge--purple-glycine">Libellé badge</p>
            </div>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile avec bouton, taille par défaut

dans une grille sur 3 à 6 colonnes en version desktop

```html
<div class="fr-tile fr-enlarge-button" id="tile-7568">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <button type="button">Intitulé de la tuile</button>
            </h3>
            <p class="fr-tile__desc">Lorem [...] elit ut.</p>
            <p class="fr-tile__detail">Détail (optionel)</p>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile avec bouton verticale variation accentuée en contrast grey

```html
<div class="fr-tile fr-tile--grey fr-enlarge-button" id="tile-7571">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <button type="button">Intitulé de la tuile</button>
            </h3>
            <p class="fr-tile__desc">Lorem [...] elit ut.</p>
            <div class="fr-tile__start">
                <p class="fr-badge fr-badge--purple-glycine">Libellé badge</p>
            </div>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile avec bouton sans icone

```html
<div class="fr-tile fr-tile--no-icon fr-enlarge-button" id="tile-7574">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <button type="button">Intitulé de la tuile</button>
            </h3>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile sans lien

```html
<div class="fr-tile" id="tile-7578">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                Intitulé de la tuile
            </h3>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile verticale sans lien étendu à la tuile

```html
<div class="fr-tile" id="tile-7582">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile verticale sans lien étendu à la tuile, nouvelle fenêtre

```html
<div class="fr-tile" id="tile-7585">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a title="Intitulé de la tuile - nouvelle fenêtre" href="[url - à modifier]" target="_blank" rel="noopener external">Intitulé de la tuile</a>
            </h3>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile avec lien désactivé (a sans href)

```html
<div class="fr-tile fr-enlarge-link" id="tile-7589">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a aria-disabled="true" role="link">Intitulé de la tuile</a>
            </h3>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile avec bouton désactivé (disabled)

```html
<div class="fr-tile fr-enlarge-button" id="tile-7592">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <button type="button" disabled>Intitulé de la tuile</button>
            </h3>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile sans icone

```html
<div class="fr-tile fr-tile--no-icon fr-enlarge-link" id="tile-7596">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile avec icone lien externe

```html
<div class="fr-tile fr-enlarge-link" id="tile-7599">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a title="Intitulé de la tuile - nouvelle fenêtre" href="[url - à modifier]" target="_blank" rel="noopener external">Intitulé de la tuile</a>
            </h3>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile horizontale avec détails et tag

dans une grille sur 4 à 6 colonnes en version desktop

```html
<div class="fr-tile fr-tile--horizontal fr-enlarge-link" id="tile-7603">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__detail">Détail (optionel)</p>
            <div class="fr-tile__start">
                <p class="fr-tag">Libellé tag</p>
            </div>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile sm horizontale avec détails et badge

dans une grille sur 3 à 6 colonnes en version desktop

```html
<div class="fr-tile fr-tile--sm fr-tile--horizontal fr-enlarge-link" id="tile-7606">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__detail">Détail (optionel)</p>
            <div class="fr-tile__start">
                <p class="fr-badge fr-badge--purple-glycine">Libellé badge</p>
            </div>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile horizontale puis vertical à partir du breakpoint md

dans une grille sur 3 à 6 colonnes en version desktop

```html
<div class="fr-tile fr-tile--horizontal fr-tile--vertical@md fr-enlarge-link" id="tile-7609">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__detail">Détail (optionel)</p>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile sm horizontale puis vertical à partir du breakpoint md

dans une grille sur 3 à 6 colonnes en version desktop

```html
<div class="fr-tile fr-tile--sm fr-tile--horizontal fr-tile--vertical@md fr-enlarge-link" id="tile-7612">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__detail">Détail (optionel)</p>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile horizontale puis vertical à partir du breakpoint lg

dans une grille sur 3 à 6 colonnes en version desktop

```html
<div class="fr-tile fr-tile--horizontal fr-tile--vertical@lg fr-enlarge-link" id="tile-7615">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__detail">Détail (optionel)</p>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Tuile sm horizontale puis vertical à partir du breakpoint lg

dans une grille sur 3 à 6 colonnes en version desktop

```html
<div class="fr-tile fr-tile--sm fr-tile--horizontal fr-tile--vertical@lg fr-enlarge-link" id="tile-7618">
    <div class="fr-tile__body">
        <div class="fr-tile__content">
            <h3 class="fr-tile__title">
                <a href="[url - à modifier]">Intitulé de la tuile</a>
            </h3>
            <p class="fr-tile__detail">Détail (optionel)</p>
        </div>
    </div>
    <div class="fr-tile__header">
        <div class="fr-tile__pictogram">
            <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
            </svg>
        </div>
    </div>
</div>
```

### Grilles de tuiles verticales

Extrait complet : [exemples/grilles-de-tuiles-verticales-1.html](exemples/grilles-de-tuiles-verticales-1.html) (5 ko)

### Grilles de tuiles verticales sm

Extrait complet : [exemples/grilles-de-tuiles-verticales-sm-2.html](exemples/grilles-de-tuiles-verticales-sm-2.html) (5 ko)

### Grilles de tuiles horizontales

Extrait complet : [exemples/grilles-de-tuiles-horizontales-3.html](exemples/grilles-de-tuiles-horizontales-3.html) (5 ko)

### Grilles de tuiles horizontales sm

Extrait complet : [exemples/grilles-de-tuiles-horizontales-sm-4.html](exemples/grilles-de-tuiles-horizontales-sm-4.html) (5 ko)
