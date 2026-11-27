# Carte : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Carte verticale md, taille par défaut

dans une grille sur 4 à 6 colonnes en version desktop

```html
<div id="card-1135" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte taille sm

dans une grille sur 3 à 4 colonnes en version desktop

```html
<div id="card-1138" class="fr-card fr-enlarge-link fr-card--sm">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte taille lg

dans une grille sur 6 à 12 colonnes en version desktop

```html
<div id="card-1141" class="fr-card fr-enlarge-link fr-card--lg">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte sans icône

```html
<div id="card-1145" class="fr-card fr-enlarge-link fr-card--no-icon">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte avec icône lien externe

```html
<div id="card-1148" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a title="Intitulé de la carte (sur lequel se trouve le lien) - nouvelle fenêtre" href="#" target="_blank" rel="noopener external">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale variation accentuée en contrast grey

```html
<div id="card-1152" class="fr-card fr-enlarge-link fr-card--grey">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale variation sans bordure

```html
<div id="card-1155" class="fr-card fr-enlarge-link fr-card--no-border">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale variation sans fond

```html
<div id="card-1158" class="fr-card fr-enlarge-link fr-card--no-background">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale variation ombre portée

```html
<div id="card-1161" class="fr-card fr-enlarge-link fr-card--shadow">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte avec bouton, taille par défaut

dans une grille sur 4 à 6 colonnes en version desktop

```html
<div id="card-1165" class="fr-card fr-enlarge-button">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <button type="button">Intitulé de la carte (sur lequel se trouve le bouton)</button>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte avec bouton taille sm

dans une grille sur 3 à 4 colonnes en version desktop

```html
<div id="card-1168" class="fr-card fr-enlarge-button fr-card--sm">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <button type="button">Intitulé de la carte (sur lequel se trouve le bouton)</button>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte avec bouton taille lg

dans une grille sur 6 à 12 colonnes en version desktop

```html
<div id="card-1171" class="fr-card fr-enlarge-button fr-card--lg">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <button type="button">Intitulé de la carte (sur lequel se trouve le bouton)</button>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte avec bouton verticale variation accentuée en contrast grey

```html
<div id="card-1174" class="fr-card fr-enlarge-button fr-card--grey">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <button type="button">Intitulé de la carte (sur lequel se trouve le bouton)</button>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte avec bouton sans icône

```html
<div id="card-1177" class="fr-card fr-enlarge-button fr-card--no-icon">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <button type="button">Intitulé de la carte (sur lequel se trouve le bouton)</button>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte sans image

```html
<div id="card-1181" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
    </div>
</div>
```

### Carte verticale avec image au ratio d'aspect 32x9

```html
<div id="card-1185" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img fr-ratio-32x9" src="../../../example/img/placeholder.32x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale avec image au ratio d'aspect 3x2

```html
<div id="card-1188" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img fr-ratio-3x2" src="../../../example/img/placeholder.3x2.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale avec image au ratio d'aspect 4x3

```html
<div id="card-1191" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img fr-ratio-4x3" src="../../../example/img/placeholder.4x3.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale avec image au ratio d'aspect 1x1

```html
<div id="card-1194" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img fr-ratio-1x1" src="../../../example/img/placeholder.1x1.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale avec image au ratio d'aspect 3x4

```html
<div id="card-1197" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img fr-ratio-3x4" src="../../../example/img/placeholder.3x4.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale avec image au ratio d'aspect 2x3

```html
<div id="card-1200" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img fr-ratio-2x3" src="../../../example/img/placeholder.2x3.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale avec taxonomie dans le header

```html
<div id="card-1204" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
        <ul class="fr-badges-group">
            <li>
                <span class="fr-badge">Libellé badge</span>
            </li>
        </ul>
    </div>
</div>
```

### Carte verticale avec badges dans le contenu

```html
<div id="card-1208" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <ul class="fr-badges-group">
                    <li>
                        <span class="fr-badge fr-badge--purple-glycine">Libellé badge</span>
                    </li>
                    <li>
                        <span class="fr-badge fr-badge--purple-glycine">Libellé badge</span>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale avec tags dans le contenu

```html
<div id="card-1211" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <ul class="fr-tags-group">
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale avec détail

```html
<div id="card-1214" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <p class="fr-card__detail">détail (optionnel)</p>
            </div>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale avec détail et icon

```html
<div id="card-1217" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale avec détail en bas

```html
<div id="card-1220" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__end">
                <p class="fr-card__detail">détail (optionnel)</p>
            </div>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale avec détails en haut et en bas

```html
<div id="card-1223" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
            <div class="fr-card__end">
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale avec détails et badges

```html
<div id="card-1226" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <ul class="fr-badges-group">
                    <li>
                        <span class="fr-badge fr-badge--purple-glycine">Libellé badge</span>
                    </li>
                    <li>
                        <span class="fr-badge fr-badge--purple-glycine">Libellé badge</span>
                    </li>
                </ul>
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
            <div class="fr-card__end">
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale avec détails et tags

```html
<div id="card-1229" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <ul class="fr-tags-group">
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                </ul>
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
            <div class="fr-card__end">
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale sm avec détails et badges

```html
<div id="card-1232" class="fr-card fr-enlarge-link fr-card--sm">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <ul class="fr-badges-group">
                    <li>
                        <span class="fr-badge fr-badge--purple-glycine">Libellé badge</span>
                    </li>
                    <li>
                        <span class="fr-badge fr-badge--purple-glycine">Libellé badge</span>
                    </li>
                </ul>
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
            <div class="fr-card__end">
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale sm avec détails et tags

```html
<div id="card-1235" class="fr-card fr-enlarge-link fr-card--sm">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <ul class="fr-tags-group">
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                </ul>
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
            <div class="fr-card__end">
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale lg avec détails et badges

```html
<div id="card-1238" class="fr-card fr-enlarge-link fr-card--lg">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <ul class="fr-badges-group">
                    <li>
                        <span class="fr-badge fr-badge--purple-glycine">Libellé badge</span>
                    </li>
                    <li>
                        <span class="fr-badge fr-badge--purple-glycine">Libellé badge</span>
                    </li>
                </ul>
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
            <div class="fr-card__end">
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale lg avec détails et tags

```html
<div id="card-1241" class="fr-card fr-enlarge-link fr-card--lg">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <ul class="fr-tags-group">
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                </ul>
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
            <div class="fr-card__end">
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte sans lien

```html
<div id="card-1245" class="fr-card">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                Intitulé de la carte
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale sans lien étendu à la carte

```html
<div id="card-1249" class="fr-card">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale sans lien étendu et ouverture dans une nouvelle fenêtre

```html
<div id="card-1252" class="fr-card">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a title="Intitulé de la carte (sur lequel se trouve le lien) - nouvelle fenêtre" href="#" target="_blank" rel="noopener external">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale SM sans lien étendu et ouverture dans une nouvelle fenêtre

```html
<div id="card-1255" class="fr-card fr-card--sm">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a title="Intitulé de la carte (sur lequel se trouve le lien) - nouvelle fenêtre" href="#" target="_blank" rel="noopener external">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale LG sans lien étendu et ouverture dans une nouvelle fenêtre

```html
<div id="card-1258" class="fr-card fr-card--lg">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a title="Intitulé de la carte (sur lequel se trouve le lien) - nouvelle fenêtre" href="#" target="_blank" rel="noopener external">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte avec lien désactivé (a sans href)

```html
<div id="card-1262" class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a aria-disabled="true" role="link">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte avec bouton désactivé (disabled)

```html
<div id="card-1265" class="fr-card fr-enlarge-button">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <button type="button" disabled>Intitulé de la carte (sur lequel se trouve le bouton)</button>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale avec zone d'action

dans une grille sur 4 à 6 colonnes en version desktop

```html
<div id="card-1269" class="fr-card">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
        </div>
        <div class="fr-card__footer">
            <ul class="fr-btns-group fr-btns-group--inline-reverse fr-btns-group--inline-lg">
                <li>
                    <button type="button" class="fr-btn fr-btn--secondary">Libellé</button>
                </li>
                <li>
                    <button type="button" class="fr-btn">Libellé</button>
                </li>
            </ul>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale avec zone d'action boutons

```html
<div id="card-1272" class="fr-card">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
        <div class="fr-card__footer">
            <ul class="fr-btns-group fr-btns-group--inline-reverse fr-btns-group--inline-lg">
                <li>
                    <button type="button" class="fr-btn fr-btn--secondary">Libellé</button>
                </li>
                <li>
                    <button type="button" class="fr-btn">Libellé</button>
                </li>
            </ul>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale sm avec zone d'action boutons

```html
<div id="card-1275" class="fr-card fr-card--sm">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
        <div class="fr-card__footer">
            <ul class="fr-btns-group fr-btns-group--inline-reverse fr-btns-group--inline-lg">
                <li>
                    <button type="button" class="fr-btn fr-btn--secondary">Libellé</button>
                </li>
                <li>
                    <button type="button" class="fr-btn">Libellé</button>
                </li>
            </ul>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale lg avec zone d'action boutons

```html
<div id="card-1278" class="fr-card fr-card--lg">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
        <div class="fr-card__footer">
            <ul class="fr-btns-group fr-btns-group--inline-reverse fr-btns-group--inline-lg">
                <li>
                    <button type="button" class="fr-btn fr-btn--secondary">Libellé</button>
                </li>
                <li>
                    <button type="button" class="fr-btn">Libellé</button>
                </li>
            </ul>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte verticale avec zone d'action liens

```html
<div id="card-1283" class="fr-card">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
        <div class="fr-card__footer">
            <ul class="fr-links-group fr-links-group--inline">
                <li>
                    <a id="link-1284" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé</a>
                </li>
                <li>
                    <a id="link-1285" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé</a>
                </li>
            </ul>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte horizontale avec détails et tags

dans une grille sur 6 à 8 colonnes en version desktop

```html
<div id="card-1289" class="fr-card fr-enlarge-link fr-card--horizontal">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <ul class="fr-tags-group">
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                </ul>
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
            <div class="fr-card__end">
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte horizontale sm avec détails et tags

dans une grille sur 4 à 6 colonnes en version desktop

```html
<div id="card-1292" class="fr-card fr-enlarge-link fr-card--sm fr-card--horizontal">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <ul class="fr-tags-group">
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                </ul>
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
            <div class="fr-card__end">
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte horizontale lg avec détails et tags

dans une grille sur 8 à 12 colonnes en version desktop

```html
<div id="card-1295" class="fr-card fr-enlarge-link fr-card--lg fr-card--horizontal">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <ul class="fr-tags-group">
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                </ul>
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
            <div class="fr-card__end">
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte horizontale avec zone d'action, détails et tags

```html
<div id="card-1298" class="fr-card fr-card--horizontal">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <ul class="fr-tags-group">
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                </ul>
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
        <div class="fr-card__footer">
            <ul class="fr-btns-group fr-btns-group--inline-reverse fr-btns-group--inline-lg">
                <li>
                    <button type="button" class="fr-btn fr-btn--secondary">Libellé</button>
                </li>
                <li>
                    <button type="button" class="fr-btn">Libellé</button>
                </li>
            </ul>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte horizontale sm avec zone d'action, détails et tags

```html
<div id="card-1301" class="fr-card fr-card--sm fr-card--horizontal">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <ul class="fr-tags-group">
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                </ul>
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
        <div class="fr-card__footer">
            <ul class="fr-btns-group fr-btns-group--inline-reverse fr-btns-group--inline-lg">
                <li>
                    <button type="button" class="fr-btn fr-btn--secondary">Libellé</button>
                </li>
                <li>
                    <button type="button" class="fr-btn">Libellé</button>
                </li>
            </ul>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte horizontale lg avec zone d'action, détails et tags

```html
<div id="card-1304" class="fr-card fr-card--lg fr-card--horizontal">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <ul class="fr-tags-group">
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                </ul>
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
        <div class="fr-card__footer">
            <ul class="fr-btns-group fr-btns-group--inline-reverse fr-btns-group--inline-lg">
                <li>
                    <button type="button" class="fr-btn fr-btn--secondary">Libellé</button>
                </li>
                <li>
                    <button type="button" class="fr-btn">Libellé</button>
                </li>
            </ul>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte horizontale image proportion de moitié avec zone d'action, détails et tags

```html
<div id="card-1307" class="fr-card fr-card--horizontal-half">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <ul class="fr-tags-group">
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                </ul>
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
        <div class="fr-card__footer">
            <ul class="fr-btns-group fr-btns-group--inline-reverse fr-btns-group--inline-lg">
                <li>
                    <button type="button" class="fr-btn fr-btn--secondary">Libellé</button>
                </li>
                <li>
                    <button type="button" class="fr-btn">Libellé</button>
                </li>
            </ul>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte horizontale image proportion du tiers moitié avec zone d'action, détails et tags

```html
<div id="card-1310" class="fr-card fr-card--horizontal-tier">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <ul class="fr-tags-group">
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                </ul>
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
        <div class="fr-card__footer">
            <ul class="fr-btns-group fr-btns-group--inline-reverse fr-btns-group--inline-lg">
                <li>
                    <button type="button" class="fr-btn fr-btn--secondary">Libellé</button>
                </li>
                <li>
                    <button type="button" class="fr-btn">Libellé</button>
                </li>
            </ul>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Carte horizontale avec ratio d'image particulier en mobile

```html
<div id="card-1313" class="fr-card fr-card--horizontal">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Intitulé de la carte (sur lequel se trouve le lien)</a>
            </h3>
            <p class="fr-card__desc">Lorem [...] elit ut.</p>
            <div class="fr-card__start">
                <ul class="fr-tags-group">
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                    <li>
                        <p class="fr-tag">Libellé tag</p>
                    </li>
                </ul>
                <p class="fr-card__detail fr-icon-warning-fill">détail (optionnel)</p>
            </div>
        </div>
        <div class="fr-card__footer">
            <ul class="fr-btns-group fr-btns-group--inline-reverse fr-btns-group--inline-lg">
                <li>
                    <button type="button" class="fr-btn fr-btn--secondary">Libellé</button>
                </li>
                <li>
                    <button type="button" class="fr-btn">Libellé</button>
                </li>
            </ul>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img fr-ratio-32x9" src="../../../example/img/placeholder.32x9.png" alt="[À MODIFIER - vide ou texte alternatif de l’image]" />
            <!-- L’alternative de l’image (attribut alt) doit toujours être présente, sa valeur peut-être vide (image n’apportant pas de sens supplémentaire au contexte) ou non (porteuse de texte ou apportant du sens) selon votre contexte -->
        </div>
    </div>
</div>
```

### Grilles de cartes verticales

Extrait complet : [exemples/grilles-de-cartes-verticales-1.html](exemples/grilles-de-cartes-verticales-1.html) (8 ko)

### Grilles de cartes verticales sm

Extrait complet : [exemples/grilles-de-cartes-verticales-sm-2.html](exemples/grilles-de-cartes-verticales-sm-2.html) (9 ko)

### Grilles de cartes verticales lg

Extrait complet : [exemples/grilles-de-cartes-verticales-lg-3.html](exemples/grilles-de-cartes-verticales-lg-3.html) (8 ko)

### Grilles de cartes horizontales

Extrait complet : [exemples/grilles-de-cartes-horizontales-4.html](exemples/grilles-de-cartes-horizontales-4.html) (8 ko)

### Grilles de cartes horizontales sm

Extrait complet : [exemples/grilles-de-cartes-horizontales-sm-5.html](exemples/grilles-de-cartes-horizontales-sm-5.html) (9 ko)

### Grilles de cartes horizontales lg

Extrait complet : [exemples/grilles-de-cartes-horizontales-lg-6.html](exemples/grilles-de-cartes-horizontales-lg-6.html) (9 ko)
