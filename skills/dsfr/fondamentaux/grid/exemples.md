# Grille et points de rupture : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Grille sans gouttières

```html
<div class="fr-container">
    <div class="fr-grid-row">
        <div class="fr-col-12">
            <div class="col-demo">Lorem [...] elit ut.</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">col</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">col</div>
        </div>
    </div>
</div>
```

### Grille sans gouttières 4 col

```html
<div class="fr-container">
    <div class="fr-grid-row">
        <div class="fr-col">
            <div class="col-demo">1/4</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">1/4</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">1/4</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">1/4</div>
        </div>
    </div>
</div>
```

### Grille sans gouttières 6 col

```html
<div class="fr-container">
    <div class="fr-grid-row">
        <div class="fr-col">
            <div class="col-demo">1/6</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">1/6</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">1/6</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">1/6</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">1/6</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">1/6</div>
        </div>
    </div>
</div>
```

### Grille avec gouttières

```html
<div class="fr-container">
    <div class="fr-grid-row fr-grid-row--gutters">
        <div class="fr-col-12">
            <div class="col-demo">Lorem [...] elit ut.</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">col</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">col</div>
        </div>
    </div>
</div>
```

### Grille avec gouttières 4 col

```html
<div class="fr-container">
    <div class="fr-grid-row fr-grid-row--gutters">
        <div class="fr-col">
            <div class="col-demo">1/4</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">1/4</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">1/4</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">1/4</div>
        </div>
    </div>
</div>
```

### Grille avec gouttières 6 col

```html
<div class="fr-container">
    <div class="fr-grid-row fr-grid-row--gutters">
        <div class="fr-col">
            <div class="col-demo">1/6</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">1/6</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">1/6</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">1/6</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">1/6</div>
        </div>
        <div class="fr-col">
            <div class="col-demo">1/6</div>
        </div>
    </div>
</div>
```

### Grille sans gouttières avec taille de colonnes

```html
<div class="fr-container">
    <div class="fr-grid-row">
        <div class="fr-col-3">
            <div class="col-demo">3/12</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">3/12</div>
        </div>
        <div class="fr-col-2">
            <div class="col-demo">2/12</div>
        </div>
        <div class="fr-col-4">
            <div class="col-demo">4/12</div>
        </div>
        <div class="fr-col-5">
            <div class="col-demo">5/12</div>
        </div>
        <div class="fr-col-7">
            <div class="col-demo">7/12</div>
        </div>
        <div class="fr-col-9">
            <div class="col-demo">9/12</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">3/12</div>
        </div>
        <div class="fr-col-5">
            <div class="col-demo">5/12</div>
        </div>
        <div class="fr-col-5">
            <div class="col-demo">5/12</div>
        </div>
        <div class="fr-col-2">
            <div class="col-demo">2/12</div>
        </div>
        <div class="fr-col-12">
            <div class="col-demo">12/12</div>
        </div>
    </div>
</div>
```

### Grille avec gouttières avec taille de colonnes

```html
<div class="fr-container">
    <div class="fr-grid-row fr-grid-row--gutters">
        <div class="fr-col-3">
            <div class="col-demo">3/12</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">3/12</div>
        </div>
        <div class="fr-col-2">
            <div class="col-demo">2/12</div>
        </div>
        <div class="fr-col-4">
            <div class="col-demo">4/12</div>
        </div>
        <div class="fr-col-5">
            <div class="col-demo">5/12</div>
        </div>
        <div class="fr-col-7">
            <div class="col-demo">7/12</div>
        </div>
        <div class="fr-col-9">
            <div class="col-demo">9/12</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">3/12</div>
        </div>
        <div class="fr-col-5">
            <div class="col-demo">5/12</div>
        </div>
        <div class="fr-col-5">
            <div class="col-demo">5/12</div>
        </div>
        <div class="fr-col-2">
            <div class="col-demo">2/12</div>
        </div>
        <div class="fr-col-12">
            <div class="col-demo">12/12</div>
        </div>
    </div>
</div>
```

### Grille sans gouttières imbrication (1ère imbriquée avec gouttière, 2nde sans gouttières)

```html
<div class="fr-container">
    <div class="fr-grid-row">
        <div class="fr-col-8">
            <div class="fr-grid-row fr-grid-row--gutters">
                <div class="fr-col-6">
                    <div class="col-demo">6/12</div>
                </div>
                <div class="fr-col-6">
                    <div class="col-demo">6/12</div>
                </div>
            </div>
        </div>
        <div class="fr-col-4">
            <div class="col-demo">4/12</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">3/12</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">3/12</div>
        </div>
        <div class="fr-col-6">
            <div class="fr-grid-row">
                <div class="fr-col-4">
                    <div class="col-demo">4/12</div>
                </div>
                <div class="fr-col-4">
                    <div class="col-demo">4/12</div>
                </div>
                <div class="fr-col-4">
                    <div class="col-demo">4/12</div>
                </div>
            </div>
        </div>
    </div>
</div>
```

### Grille avec gouttières imbrication (1ère imbriquée avec gouttière, 2nde sans gouttières)

```html
<div class="fr-container">
    <div class="fr-grid-row fr-grid-row--gutters">
        <div class="fr-col-8">
            <div class="fr-grid-row fr-grid-row--gutters">
                <div class="fr-col-6">
                    <div class="col-demo">6/12</div>
                </div>
                <div class="fr-col-6">
                    <div class="col-demo">6/12</div>
                </div>
            </div>
        </div>
        <div class="fr-col-4">
            <div class="col-demo">4/12</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">3/12</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">3/12</div>
        </div>
        <div class="fr-col-6">
            <div class="fr-grid-row">
                <div class="fr-col-4">
                    <div class="col-demo">4/12</div>
                </div>
                <div class="fr-col-4">
                    <div class="col-demo">4/12</div>
                </div>
                <div class="fr-col-4">
                    <div class="col-demo">4/12</div>
                </div>
            </div>
        </div>
    </div>
</div>
```

### Grille avec gouttières alignement haut

```html
<div class="fr-container">
    <div class="fr-grid-row--top fr-grid-row fr-grid-row--gutters fr-grid-row fr-grid-row--gutters">
        <div class="fr-col-3">
            <div class="col-demo">align top</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">Lorem [...] elit ut.</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">align top</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">align top</div>
        </div>
    </div>
</div>
```

### Grille avec gouttières alignement bas

```html
<div class="fr-container">
    <div class="fr-grid-row--bottom fr-grid-row fr-grid-row--gutters fr-grid-row fr-grid-row--gutters">
        <div class="fr-col-3">
            <div class="col-demo">align bottom</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">Lorem [...] elit ut.</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">align bottom</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">align bottom</div>
        </div>
    </div>
</div>
```

### Grille avec gouttières alignement milieu

```html
<div class="fr-container">
    <div class="fr-grid-row--middle fr-grid-row fr-grid-row--gutters fr-grid-row fr-grid-row--gutters">
        <div class="fr-col-3">
            <div class="col-demo">align middle</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">Lorem [...] elit ut.</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">align middle</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">align middle</div>
        </div>
    </div>
</div>
```

### Grille avec gouttières alignement mélangés

```html
<div class="fr-container">
    <div class="fr-grid-row fr-grid-row--gutters">
        <div class="fr-col-3">
            <div class="col-demo">Lorem [...] elit ut.</div>
        </div>
        <div class="fr-col--top fr-col-3 fr-col-3">
            <div class="col-demo">align top</div>
        </div>
        <div class="fr-col--middle fr-col-3 fr-col-3">
            <div class="col-demo">align middle</div>
        </div>
        <div class="fr-col--bottom fr-col-3 fr-col-3">
            <div class="col-demo">align bottom</div>
        </div>
    </div>
</div>
```

### Grille avec gouttières alignement gauche

```html
<div class="fr-container">
    <div class="fr-grid-row--left fr-grid-row fr-grid-row--gutters fr-grid-row fr-grid-row--gutters">
        <div class="fr-col-3">
            <div class="col-demo">align left</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">align left</div>
        </div>
    </div>
</div>
```

### Grille avec gouttières alignement droite

```html
<div class="fr-container">
    <div class="fr-grid-row--right fr-grid-row fr-grid-row--gutters fr-grid-row fr-grid-row--gutters">
        <div class="fr-col-3">
            <div class="col-demo">align left</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">align left</div>
        </div>
    </div>
</div>
```

### Grille avec gouttières alignement centré

```html
<div class="fr-container">
    <div class="fr-grid-row--center fr-grid-row fr-grid-row--gutters fr-grid-row fr-grid-row--gutters">
        <div class="fr-col-3">
            <div class="col-demo">align center</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">align center</div>
        </div>
    </div>
</div>
```

### Grille avec écart

```html
<div class="fr-container">
    <div class="fr-grid-row fr-grid-row--gutters">
        <div class="fr-col-3">
            <div class="col-demo">3/12</div>
        </div>
        <div class="fr-col-3 fr-col-offset-3">
            <div class="col-demo">3/12</div>
        </div>
        <div class="fr-col-3">
            <div class="col-demo">3/12</div>
        </div>
    </div>
</div>
```

### Grille avec colonne à taille variable suivant les points de ruptures

```html
<div class="fr-container">
    <div class="fr-grid-row fr-grid-row--gutters">
        <div class="fr-col-12 fr-col-sm-10 fr-col-md-8 fr-col-lg-6 fr-col-xl-4">
            <div class="col-demo">12 / sm-10 / md-8 / lg-6 / xl-4</div>
        </div>
    </div>
</div>
```

### Grille avec conteneur fluide

```html
<div class="fr-container--fluid">
    <div class="fr-grid-row">
        <div class="fr-col-1">
            <div class="col-demo">1/12</div>
        </div>
        <div class="fr-col-1">
            <div class="col-demo">1/12</div>
        </div>
        <div class="fr-col-1">
            <div class="col-demo">1/12</div>
        </div>
        <div class="fr-col-1">
            <div class="col-demo">1/12</div>
        </div>
        <div class="fr-col-1">
            <div class="col-demo">1/12</div>
        </div>
        <div class="fr-col-1">
            <div class="col-demo">1/12</div>
        </div>
        <div class="fr-col-1">
            <div class="col-demo">1/12</div>
        </div>
        <div class="fr-col-1">
            <div class="col-demo">1/12</div>
        </div>
        <div class="fr-col-1">
            <div class="col-demo">1/12</div>
        </div>
        <div class="fr-col-1">
            <div class="col-demo">1/12</div>
        </div>
        <div class="fr-col-1">
            <div class="col-demo">1/12</div>
        </div>
        <div class="fr-col-1">
            <div class="col-demo">1/12</div>
        </div>
    </div>
</div>
```
