# Curseur : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Curseur simple

```html
<div class="fr-range-group" id="range-1793-group">
    <label class="fr-label" id="range-1792-label" for="range-1792">
        Libellé
        <span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
    </label>
    <div class="fr-range">
        <span class="fr-range__output" aria-hidden="true">50</span>
        <input id="range-1792" name="range-1792" type="range" max="100" value="50" aria-describedby="range-1792-messages">
        <span class="fr-range__min" aria-hidden="true">0</span>
        <span class="fr-range__max" aria-hidden="true">100</span>
    </div>
    <div class="fr-messages-group" id="range-1792-messages" aria-live="polite">
    </div>
</div>
```

### Curseur simple taille SM

```html
<div class="fr-range-group" id="range-1798-group">
    <label class="fr-label" id="range-1797-label" for="range-1797">
        Libellé
        <span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
    </label>
    <div class="fr-range fr-range--sm">
        <span class="fr-range__output" aria-hidden="true">50</span>
        <input id="range-1797" name="range-1797" type="range" max="100" value="50" aria-describedby="range-1797-messages">
        <span class="fr-range__min" aria-hidden="true">0</span>
        <span class="fr-range__max" aria-hidden="true">100</span>
    </div>
    <div class="fr-messages-group" id="range-1797-messages" aria-live="polite">
    </div>
</div>
```

### Curseur simple sans les indicateurs min/max

```html
<div class="fr-range-group" id="range-1803-group">
    <label class="fr-label" id="range-1802-label" for="range-1802">
        Libellé
        <span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
    </label>
    <div class="fr-range">
        <span class="fr-range__output" aria-hidden="true">50</span>
        <input id="range-1802" name="range-1802" type="range" max="100" value="50" aria-describedby="range-1802-messages">
    </div>
    <div class="fr-messages-group" id="range-1802-messages" aria-live="polite">
    </div>
</div>
```

### Curseur avec étapes

```html
<div class="fr-range-group" id="range-1808-group">
    <label class="fr-label" id="range-1807-label" for="range-1807">
        Libellé
        <span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
    </label>
    <div class="fr-range fr-range--step">
        <span class="fr-range__output" aria-hidden="true">50</span>
        <input id="range-1807" name="range-1807" type="range" max="100" value="50" step="10" aria-describedby="range-1807-messages">
        <span class="fr-range__min" aria-hidden="true">0</span>
        <span class="fr-range__max" aria-hidden="true">100</span>
    </div>
    <div class="fr-messages-group" id="range-1807-messages" aria-live="polite">
    </div>
</div>
```

### Curseur avec étapes taille SM

```html
<div class="fr-range-group" id="range-1813-group">
    <label class="fr-label" id="range-1812-label" for="range-1812">
        Libellé
        <span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
    </label>
    <div class="fr-range fr-range--sm fr-range--step">
        <span class="fr-range__output" aria-hidden="true">50</span>
        <input id="range-1812" name="range-1812" type="range" max="100" value="50" step="10" aria-describedby="range-1812-messages">
        <span class="fr-range__min" aria-hidden="true">0</span>
        <span class="fr-range__max" aria-hidden="true">100</span>
    </div>
    <div class="fr-messages-group" id="range-1812-messages" aria-live="polite">
    </div>
</div>
```

### Curseur double avec valeurs min et max

```html
<div class="fr-range-group" id="range-1818-group">
    <label class="fr-label" id="range-1817-label">
        Libellé
        <span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
    </label>
    <div class="fr-range fr-range--double">
        <span class="fr-range__output" aria-hidden="true">25</span>
        <input id="range-1817" name="range-1817" type="range" aria-label="Valeur minimale" aria-labelledby="range-1817 range-1817-label" max="100" value="25" aria-describedby="range-1817-messages">
        <input id="range-1817-2" name="range-1817-2" type="range" aria-label="Valeur maximale" aria-labelledby="range-1817-2 range-1817-label" max="100" value="75" aria-describedby="range-1817-messages">
        <span class="fr-range__min" aria-hidden="true">0</span>
        <span class="fr-range__max" aria-hidden="true">100</span>
    </div>
    <div class="fr-messages-group" id="range-1817-messages" aria-live="polite">
    </div>
</div>
```

### Curseur double taille SM

```html
<div class="fr-range-group" id="range-1823-group">
    <label class="fr-label" id="range-1822-label">
        Libellé
        <span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
    </label>
    <div class="fr-range fr-range--sm fr-range--double">
        <span class="fr-range__output" aria-hidden="true">25</span>
        <input id="range-1822" name="range-1822" type="range" aria-label="Valeur minimale" aria-labelledby="range-1822 range-1822-label" max="100" value="25" aria-describedby="range-1822-messages">
        <input id="range-1822-2" name="range-1822-2" type="range" aria-label="Valeur maximale" aria-labelledby="range-1822-2 range-1822-label" max="100" value="75" aria-describedby="range-1822-messages">
        <span class="fr-range__min" aria-hidden="true">0</span>
        <span class="fr-range__max" aria-hidden="true">100</span>
    </div>
    <div class="fr-messages-group" id="range-1822-messages" aria-live="polite">
    </div>
</div>
```

### Curseur avec préfixe et suffixe

```html
<div class="fr-range-group" id="range-1828-group">
    <label class="fr-label" id="range-1827-label" for="range-1827">
        Libellé
        <span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
    </label>
    <div class="fr-range" data-fr-prefix="~" data-fr-suffix="%">
        <span class="fr-range__output" aria-hidden="true">~50%</span>
        <input id="range-1827" name="range-1827" type="range" max="100" value="50" aria-describedby="range-1827-messages">
        <span class="fr-range__min" aria-hidden="true">~0%</span>
        <span class="fr-range__max" aria-hidden="true">~100%</span>
    </div>
    <div class="fr-messages-group" id="range-1827-messages" aria-live="polite">
    </div>
</div>
```

### Curseur désactivé

```html
<div class="fr-range-group fr-range-group--disabled" id="range-1833-group">
    <label class="fr-label" id="range-1832-label" for="range-1832">
        Libellé
        <span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
    </label>
    <div class="fr-range">
        <span class="fr-range__output" aria-hidden="true">50</span>
        <input id="range-1832" name="range-1832" type="range" max="100" value="50" disabled aria-describedby="range-1832-messages">
        <span class="fr-range__min" aria-hidden="true">0</span>
        <span class="fr-range__max" aria-hidden="true">100</span>
    </div>
    <div class="fr-messages-group" id="range-1832-messages" aria-live="polite">
    </div>
</div>
```

### Curseur avec étape désactivé

```html
<div class="fr-range-group fr-range-group--disabled" id="range-1838-group">
    <label class="fr-label" id="range-1837-label" for="range-1837">
        Libellé
        <span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
    </label>
    <div class="fr-range fr-range--step">
        <span class="fr-range__output" aria-hidden="true">50</span>
        <input id="range-1837" name="range-1837" type="range" max="100" value="50" step="10" disabled aria-describedby="range-1837-messages">
        <span class="fr-range__min" aria-hidden="true">0</span>
        <span class="fr-range__max" aria-hidden="true">100</span>
    </div>
    <div class="fr-messages-group" id="range-1837-messages" aria-live="polite">
    </div>
</div>
```

### Curseur double désactivé

```html
<div class="fr-range-group fr-range-group--disabled" id="range-1843-group">
    <label class="fr-label" id="range-1842-label">
        Libellé
        <span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
    </label>
    <div class="fr-range fr-range--double">
        <span class="fr-range__output" aria-hidden="true">20</span>
        <input id="range-1842" name="range-1842" type="range" aria-label="Valeur minimale" aria-labelledby="range-1842 range-1842-label" max="100" value="20" disabled aria-describedby="range-1842-messages">
        <input id="range-1842-2" name="range-1842-2" type="range" aria-label="Valeur maximale" aria-labelledby="range-1842-2 range-1842-label" max="100" value="80" disabled aria-describedby="range-1842-messages">
        <span class="fr-range__min" aria-hidden="true">0</span>
        <span class="fr-range__max" aria-hidden="true">100</span>
    </div>
    <div class="fr-messages-group" id="range-1842-messages" aria-live="polite">
    </div>
</div>
```

### Curseur avec erreur

```html
<div class="fr-range-group fr-range-group--error" id="range-1848-group">
    <label class="fr-label" id="range-1847-label" for="range-1847">
        Libellé
        <span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
    </label>
    <div class="fr-range">
        <span class="fr-range__output" aria-hidden="true">50</span>
        <input id="range-1847" name="range-1847" type="range" max="100" value="50" aria-describedby="range-1847-messages">
        <span class="fr-range__min" aria-hidden="true">0</span>
        <span class="fr-range__max" aria-hidden="true">100</span>
    </div>
    <div class="fr-messages-group" id="range-1847-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="range-1847-message-error">Valeur sélectionnée impossible</p>
    </div>
</div>
```
