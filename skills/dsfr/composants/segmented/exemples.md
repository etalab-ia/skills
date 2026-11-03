# Contrôle segmenté : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Contrôle segmenté simple

```html
<fieldset class="fr-segmented">
    <legend class="fr-segmented__legend">
        Légende
    </legend>
    <div class="fr-segmented__elements">
        <div class="fr-segmented__element">
            <input value="1" type="radio" id="segmented-1768-1" name="segmented-1768">
            <label class="fr-label" for="segmented-1768-1">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="2" checked type="radio" id="segmented-1768-2" name="segmented-1768">
            <label class="fr-label" for="segmented-1768-2">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="3" type="radio" id="segmented-1768-3" name="segmented-1768">
            <label class="fr-label" for="segmented-1768-3">
                Libellé
            </label>
        </div>
    </div>
</fieldset>
```

### Contrôle segmenté taille SM

```html
<fieldset class="fr-segmented fr-segmented--sm">
    <legend class="fr-segmented__legend">
        Légende
    </legend>
    <div class="fr-segmented__elements">
        <div class="fr-segmented__element">
            <input value="1" type="radio" id="segmented-1771-1" name="segmented-1771">
            <label class="fr-label" for="segmented-1771-1">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="2" checked type="radio" id="segmented-1771-2" name="segmented-1771">
            <label class="fr-label" for="segmented-1771-2">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="3" type="radio" id="segmented-1771-3" name="segmented-1771">
            <label class="fr-label" for="segmented-1771-3">
                Libellé
            </label>
        </div>
    </div>
</fieldset>
```

### Contrôle segmenté avec légende en ligne

```html
<fieldset class="fr-segmented">
    <legend class="fr-segmented__legend fr-segmented__legend--inline">
        Légende
    </legend>
    <div class="fr-segmented__elements">
        <div class="fr-segmented__element">
            <input value="1" type="radio" id="segmented-1774-1" name="segmented-1774">
            <label class="fr-label" for="segmented-1774-1">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="2" checked type="radio" id="segmented-1774-2" name="segmented-1774">
            <label class="fr-label" for="segmented-1774-2">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="3" type="radio" id="segmented-1774-3" name="segmented-1774">
            <label class="fr-label" for="segmented-1774-3">
                Libellé
            </label>
        </div>
    </div>
</fieldset>
```

### Contrôle segmenté avec texte d'aide

```html
<fieldset class="fr-segmented">
    <legend class="fr-segmented__legend">
        Légende
        <span class="fr-hint-text">texte additionel</span>
    </legend>
    <div class="fr-segmented__elements">
        <div class="fr-segmented__element">
            <input value="1" type="radio" id="segmented-1777-1" name="segmented-1777">
            <label class="fr-label" for="segmented-1777-1">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="2" checked type="radio" id="segmented-1777-2" name="segmented-1777">
            <label class="fr-label" for="segmented-1777-2">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="3" type="radio" id="segmented-1777-3" name="segmented-1777">
            <label class="fr-label" for="segmented-1777-3">
                Libellé
            </label>
        </div>
    </div>
</fieldset>
```

### Contrôle segmenté avec icônes

```html
<fieldset class="fr-segmented">
    <legend class="fr-segmented__legend">
        Légende
    </legend>
    <div class="fr-segmented__elements">
        <div class="fr-segmented__element">
            <input value="1" type="radio" id="segmented-1780-1" name="segmented-1780">
            <label class="fr-icon-road-map-line fr-label" for="segmented-1780-1">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="2" checked type="radio" id="segmented-1780-2" name="segmented-1780">
            <label class="fr-icon-road-map-line fr-label" for="segmented-1780-2">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="3" type="radio" id="segmented-1780-3" name="segmented-1780">
            <label class="fr-icon-road-map-line fr-label" for="segmented-1780-3">
                Libellé
            </label>
        </div>
    </div>
</fieldset>
```

### Contrôle segmenté sans légende

```html
<fieldset class="fr-segmented fr-segmented--no-legend">
    <legend class="fr-segmented__legend">
        Légende
    </legend>
    <div class="fr-segmented__elements">
        <div class="fr-segmented__element">
            <input value="1" type="radio" id="segmented-1783-1" name="segmented-1783">
            <label class="fr-label" for="segmented-1783-1">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="2" checked type="radio" id="segmented-1783-2" name="segmented-1783">
            <label class="fr-label" for="segmented-1783-2">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="3" type="radio" id="segmented-1783-3" name="segmented-1783">
            <label class="fr-label" for="segmented-1783-3">
                Libellé
            </label>
        </div>
    </div>
</fieldset>
```

### Contrôle segmenté désactivé

```html
<fieldset class="fr-segmented">
    <legend class="fr-segmented__legend">
        Légende
    </legend>
    <div class="fr-segmented__elements">
        <div class="fr-segmented__element">
            <input value="1" type="radio" id="segmented-1786-1" name="segmented-1786">
            <label class="fr-label" for="segmented-1786-1">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="2" checked type="radio" id="segmented-1786-2" name="segmented-1786">
            <label class="fr-label" for="segmented-1786-2">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="3" disabled type="radio" id="segmented-1786-3" name="segmented-1786">
            <label class="fr-label" for="segmented-1786-3">
                Libellé
            </label>
        </div>
    </div>
</fieldset>
```

### Contrôle segmenté cas maximum (non recommandé)

Lorsque la largeur du contrôle segmenté dépasse celle de son conteneur, la légende ne reste pas sur la même ligne. Si cela ne rentre toujours pas, les boutons passent en vertical. Réduisez la fenêtre pour voir le comportement de ce script.

```html
<fieldset class="fr-segmented" id="segmented-max">
    <legend class="fr-segmented__legend fr-segmented__legend--inline">
        Légende
    </legend>
    <div class="fr-segmented__elements">
        <div class="fr-segmented__element">
            <input value="1" type="radio" id="segmented-max-1" name="segmented-max">
            <label class="fr-icon-star-line fr-label" for="segmented-max-1">
                Libellé long
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="2" checked type="radio" id="segmented-max-2" name="segmented-max">
            <label class="fr-icon-time-line fr-label" for="segmented-max-2">
                Libellé trop long
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="3" type="radio" id="segmented-max-3" name="segmented-max">
            <label class="fr-icon-road-map-line fr-label" for="segmented-max-3">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="4" type="radio" id="segmented-max-4" name="segmented-max">
            <label class="fr-icon-road-map-line fr-label" for="segmented-max-4">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="5" type="radio" id="segmented-max-5" name="segmented-max">
            <label class="fr-icon-road-map-line fr-label" for="segmented-max-5">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="6" type="radio" id="segmented-max-6" name="segmented-max">
            <label class="fr-icon-road-map-line fr-label" for="segmented-max-6">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="7" type="radio" id="segmented-max-7" name="segmented-max">
            <label class="fr-icon-road-map-line fr-label" for="segmented-max-7">
                Libellé
            </label>
        </div>
        <div class="fr-segmented__element">
            <input value="8" type="radio" id="segmented-max-8" name="segmented-max">
            <label class="fr-icon-road-map-line fr-label" for="segmented-max-8">
                Libellé
            </label>
        </div>
    </div>
</fieldset>
```
