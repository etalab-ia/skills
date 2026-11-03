# Bouton radio : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

## Bouton radio simple

### Ensemble de boutons radio

```html
<fieldset class="fr-fieldset" id="radio" aria-labelledby="radio-legend radio-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="1" type="radio" id="radio-1" name="radio">
            <label class="fr-label" for="radio-1">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="2" checked type="radio" id="radio-2" name="radio">
            <label class="fr-label" for="radio-2">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="3" type="radio" id="radio-3" name="radio">
            <label class="fr-label" for="radio-3">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de boutons radio, petite taille

```html
<fieldset class="fr-fieldset" id="radio-small" aria-labelledby="radio-small-legend radio-small-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-small-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-group--sm">
            <input value="1" type="radio" id="radio-small-1" name="radio-small">
            <label class="fr-label" for="radio-small-1">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-group--sm">
            <input value="2" checked type="radio" id="radio-small-2" name="radio-small">
            <label class="fr-label" for="radio-small-2">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-group--sm">
            <input value="3" type="radio" id="radio-small-3" name="radio-small">
            <label class="fr-label" for="radio-small-3">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-small-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de boutons radio désactivées

```html
<fieldset class="fr-fieldset" id="radio-disabled" aria-labelledby="radio-disabled-legend radio-disabled-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-disabled-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="1" disabled type="radio" id="radio-disabled-1" name="radio-disabled">
            <label class="fr-label" for="radio-disabled-1">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="2" disabled checked type="radio" id="radio-disabled-2" name="radio-disabled">
            <label class="fr-label" for="radio-disabled-2">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="3" disabled type="radio" id="radio-disabled-3" name="radio-disabled">
            <label class="fr-label" for="radio-disabled-3">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-disabled-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de boutons radio en ligne

```html
<fieldset class="fr-fieldset" id="radio-inline" aria-labelledby="radio-inline-legend radio-inline-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-inline-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group">
            <input value="1" type="radio" id="radio-inline-1" name="radio-inline">
            <label class="fr-label" for="radio-inline-1">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group">
            <input value="2" type="radio" id="radio-inline-2" name="radio-inline">
            <label class="fr-label" for="radio-inline-2">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group">
            <input value="3" type="radio" id="radio-inline-3" name="radio-inline">
            <label class="fr-label" for="radio-inline-3">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-inline-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de boutons radio avec texte d‘aide

```html
<fieldset class="fr-fieldset" id="radio-hint" aria-labelledby="radio-hint-legend radio-hint-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-hint-legend">
        Légende pour l’ensemble des éléments
        <span class="fr-hint-text">Texte de description additionnel</span>
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="1" type="radio" id="radio-hint-1" name="radio-hint">
            <label class="fr-label" for="radio-hint-1">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="2" type="radio" id="radio-hint-2" name="radio-hint">
            <label class="fr-label" for="radio-hint-2">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="3" type="radio" id="radio-hint-3" name="radio-hint">
            <label class="fr-label" for="radio-hint-3">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-hint-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de boutons radio avec erreur

```html
<fieldset class="fr-fieldset fr-fieldset--error" id="radio-error" role="group" aria-labelledby="radio-error-legend radio-error-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-error-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="1" type="radio" id="radio-error-1" name="radio-error">
            <label class="fr-label" for="radio-error-1">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="2" type="radio" id="radio-error-2" name="radio-error">
            <label class="fr-label" for="radio-error-2">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="3" type="radio" id="radio-error-3" name="radio-error">
            <label class="fr-label" for="radio-error-3">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-error-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="radio-error-message-error">Texte d’erreur obligatoire</p>
    </div>
</fieldset>
```

### Ensemble de boutons radio avec erreur, en ligne

```html
<fieldset class="fr-fieldset fr-fieldset--error" id="radio-error-inline" role="group" aria-labelledby="radio-error-inline-legend radio-error-inline-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-error-inline-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group">
            <input value="1" type="radio" id="radio-error-inline-1" name="radio-error-inline">
            <label class="fr-label" for="radio-error-inline-1">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group">
            <input value="2" type="radio" id="radio-error-inline-2" name="radio-error-inline">
            <label class="fr-label" for="radio-error-inline-2">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group">
            <input value="3" type="radio" id="radio-error-inline-3" name="radio-error-inline">
            <label class="fr-label" for="radio-error-inline-3">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-error-inline-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="radio-error-inline-message-error">Texte d’erreur obligatoire</p>
    </div>
</fieldset>
```

### Ensemble de boutons radio validés

```html
<fieldset class="fr-fieldset fr-fieldset--valid" id="radio-valid" role="group" aria-labelledby="radio-valid-legend radio-valid-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-valid-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="1" type="radio" id="radio-valid-1" name="radio-valid">
            <label class="fr-label" for="radio-valid-1">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="2" type="radio" id="radio-valid-2" name="radio-valid">
            <label class="fr-label" for="radio-valid-2">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="3" type="radio" id="radio-valid-3" name="radio-valid">
            <label class="fr-label" for="radio-valid-3">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-valid-messages" aria-live="polite">
        <p class="fr-message fr-message--valid" id="radio-valid-message-valid">Texte de validation</p>
    </div>
</fieldset>
```

### Ensemble de boutons radio validés, en ligne

```html
<fieldset class="fr-fieldset fr-fieldset--valid" id="radio-valid-inline" role="group" aria-labelledby="radio-valid-inline-legend radio-valid-inline-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-valid-inline-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group">
            <input value="1" type="radio" id="radio-valid-inline-1" name="radio-valid-inline">
            <label class="fr-label" for="radio-valid-inline-1">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group">
            <input value="2" type="radio" id="radio-valid-inline-2" name="radio-valid-inline">
            <label class="fr-label" for="radio-valid-inline-2">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group">
            <input value="3" type="radio" id="radio-valid-inline-3" name="radio-valid-inline">
            <label class="fr-label" for="radio-valid-inline-3">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-valid-inline-messages" aria-live="polite">
        <p class="fr-message fr-message--valid" id="radio-valid-inline-message-valid">Texte de validation</p>
    </div>
</fieldset>
```

### Ensemble de boutons radio avec texte d‘aide spécifique

```html
<fieldset class="fr-fieldset" id="radio-hint-element" aria-labelledby="radio-hint-element-legend radio-hint-element-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-hint-element-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="1" type="radio" id="radio-hint-element-1" name="radio-hint-element">
            <label class="fr-label" for="radio-hint-element-1">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="2" type="radio" id="radio-hint-element-2" name="radio-hint-element">
            <label class="fr-label" for="radio-hint-element-2">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="3" type="radio" id="radio-hint-element-3" name="radio-hint-element">
            <label class="fr-label" for="radio-hint-element-3">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-hint-element-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de boutons radio avec texte d‘aide spécifique, petite taille

```html
<fieldset class="fr-fieldset" id="radio-hint-el-sm" aria-labelledby="radio-hint-el-sm-legend radio-hint-el-sm-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-hint-el-sm-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-group--sm">
            <input value="1" type="radio" id="radio-hint-el-sm-1" name="radio-hint-el-sm">
            <label class="fr-label" for="radio-hint-el-sm-1">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-group--sm">
            <input value="2" type="radio" id="radio-hint-el-sm-2" name="radio-hint-el-sm">
            <label class="fr-label" for="radio-hint-el-sm-2">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-group--sm">
            <input value="3" type="radio" id="radio-hint-el-sm-3" name="radio-hint-el-sm">
            <label class="fr-label" for="radio-hint-el-sm-3">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-hint-el-sm-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de boutons radio, libellé en indice et exposant

```html
<fieldset class="fr-fieldset" id="radio-sub" aria-labelledby="radio-sub-legend radio-sub-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-sub-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="1" type="radio" id="radio-sub-1" name="radio-sub">
            <label class="fr-label" for="radio-sub-1">
                <span>Libellé radio <sup>sup</sup>
                    <sub>sub</sub>
                </span>
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="2" type="radio" id="radio-sub-2" name="radio-sub">
            <label class="fr-label" for="radio-sub-2">
                <span>Libellé radio <sup>sup</sup>
                    <sub>sub</sub>
                </span>
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="3" type="radio" id="radio-sub-3" name="radio-sub">
            <label class="fr-label" for="radio-sub-3">
                <span>Libellé radio <sup>sup</sup>
                    <sub>sub</sub>
                </span>
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-sub-messages" aria-live="polite">
    </div>
</fieldset>
```

## Bouton radio riche

### Ensemble de boutons radio riches, simple

```html
<fieldset class="fr-fieldset" id="radio-rich" aria-labelledby="radio-rich-legend radio-rich-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-rich-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="1" type="radio" id="radio-rich-1" name="radio-rich">
            <label class="fr-label" for="radio-rich-1">
                Libellé bouton radio
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="2" checked type="radio" id="radio-rich-2" name="radio-rich">
            <label class="fr-label" for="radio-rich-2">
                Libellé bouton radio
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="3" type="radio" id="radio-rich-3" name="radio-rich">
            <label class="fr-label" for="radio-rich-3">
                Libellé bouton radio
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-rich-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de boutons radio riches, en ligne, simple

```html
<fieldset class="fr-fieldset" id="radio-rich-inline" aria-labelledby="radio-rich-inline-legend radio-rich-inline-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-rich-inline-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group fr-radio-rich">
            <input value="1" type="radio" id="radio-rich-inline-1" name="radio-rich-inline">
            <label class="fr-label" for="radio-rich-inline-1">
                Libellé bouton radio
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group fr-radio-rich">
            <input value="2" type="radio" id="radio-rich-inline-2" name="radio-rich-inline">
            <label class="fr-label" for="radio-rich-inline-2">
                Libellé bouton radio
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group fr-radio-rich">
            <input value="3" type="radio" id="radio-rich-inline-3" name="radio-rich-inline">
            <label class="fr-label" for="radio-rich-inline-3">
                Libellé bouton radio
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-rich-inline-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de boutons radio riches sans pictogramme

```html
<fieldset class="fr-fieldset" id="radio-rich-no-img" aria-labelledby="radio-rich-no-img-legend radio-rich-no-img-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-rich-no-img-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="1" type="radio" id="radio-rich-no-img-1" name="radio-rich-no-img">
            <label class="fr-label" for="radio-rich-no-img-1">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="2" type="radio" id="radio-rich-no-img-2" name="radio-rich-no-img">
            <label class="fr-label" for="radio-rich-no-img-2">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="3" type="radio" id="radio-rich-no-img-3" name="radio-rich-no-img">
            <label class="fr-label" for="radio-rich-no-img-3">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-rich-no-img-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de boutons radio riches sans pictogramme, en ligne

```html
<fieldset class="fr-fieldset" id="radio-rich-no-pictogram-inline" aria-labelledby="radio-rich-no-pictogram-inline-legend radio-rich-no-pictogram-inline-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-rich-no-pictogram-inline-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group fr-radio-rich">
            <input value="1" type="radio" id="radio-rich-no-pictogram-inline-1" name="radio-rich-no-pictogram-inline">
            <label class="fr-label" for="radio-rich-no-pictogram-inline-1">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group fr-radio-rich">
            <input value="2" type="radio" id="radio-rich-no-pictogram-inline-2" name="radio-rich-no-pictogram-inline">
            <label class="fr-label" for="radio-rich-no-pictogram-inline-2">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group fr-radio-rich">
            <input value="3" type="radio" id="radio-rich-no-pictogram-inline-3" name="radio-rich-no-pictogram-inline">
            <label class="fr-label" for="radio-rich-no-pictogram-inline-3">
                Libellé bouton radio
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-rich-no-pictogram-inline-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de boutons radio riches avec textes d'aide

```html
<fieldset class="fr-fieldset" id="radio-rich-hint" aria-labelledby="radio-rich-hint-legend radio-rich-hint-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-rich-hint-legend">
        Légende pour l’ensemble des éléments
        <span class="fr-hint-text">Texte de description additionnel</span>
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="1" type="radio" id="radio-rich-hint-1" name="radio-rich-hint">
            <label class="fr-label" for="radio-rich-hint-1">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="2" type="radio" id="radio-rich-hint-2" name="radio-rich-hint">
            <label class="fr-label" for="radio-rich-hint-2">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="3" type="radio" id="radio-rich-hint-3" name="radio-rich-hint">
            <label class="fr-label" for="radio-rich-hint-3">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-rich-hint-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de boutons radio riches avec textes d'aide, en ligne

```html
<fieldset class="fr-fieldset" id="radio-rich-hint-inline" aria-labelledby="radio-rich-hint-inline-legend radio-rich-hint-inline-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-rich-hint-inline-legend">
        Légende pour l’ensemble des éléments
        <span class="fr-hint-text">Texte de description additionnel</span>
    </legend>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group fr-radio-rich">
            <input value="1" type="radio" id="radio-rich-hint-inline-1" name="radio-rich-hint-inline">
            <label class="fr-label" for="radio-rich-hint-inline-1">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group fr-radio-rich">
            <input value="2" type="radio" id="radio-rich-hint-inline-2" name="radio-rich-hint-inline">
            <label class="fr-label" for="radio-rich-hint-inline-2">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group fr-radio-rich">
            <input value="3" type="radio" id="radio-rich-hint-inline-3" name="radio-rich-hint-inline">
            <label class="fr-label" for="radio-rich-hint-inline-3">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-rich-hint-inline-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de boutons radio riches avec erreur et textes d'aide

```html
<fieldset class="fr-fieldset fr-fieldset--error" id="radio-rich-error" role="group" aria-labelledby="radio-rich-error-legend radio-rich-error-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-rich-error-legend">
        Légende pour l’ensemble des éléments
        <span class="fr-hint-text">Texte de description additionnel</span>
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="1" type="radio" id="radio-rich-error-1" name="radio-rich-error">
            <label class="fr-label" for="radio-rich-error-1">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="2" type="radio" id="radio-rich-error-2" name="radio-rich-error">
            <label class="fr-label" for="radio-rich-error-2">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="3" type="radio" id="radio-rich-error-3" name="radio-rich-error">
            <label class="fr-label" for="radio-rich-error-3">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-rich-error-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="radio-rich-error-message-error">Texte d’erreur obligatoire</p>
    </div>
</fieldset>
```

### Ensemble de boutons radio riches avec erreur et textes d'aide, en ligne

```html
<fieldset class="fr-fieldset fr-fieldset--error" id="radio-rich-error-inline" role="group" aria-labelledby="radio-rich-error-inline-legend radio-rich-error-inline-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-rich-error-inline-legend">
        Légende pour l’ensemble des éléments
        <span class="fr-hint-text">Texte de description additionnel</span>
    </legend>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group fr-radio-rich">
            <input value="1" type="radio" id="radio-rich-error-inline-1" name="radio-rich-error-inline">
            <label class="fr-label" for="radio-rich-error-inline-1">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group fr-radio-rich">
            <input value="2" type="radio" id="radio-rich-error-inline-2" name="radio-rich-error-inline">
            <label class="fr-label" for="radio-rich-error-inline-2">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-radio-group fr-radio-rich">
            <input value="3" type="radio" id="radio-rich-error-inline-3" name="radio-rich-error-inline">
            <label class="fr-label" for="radio-rich-error-inline-3">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-rich-error-inline-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="radio-rich-error-inline-message-error">Texte d’erreur obligatoire</p>
    </div>
</fieldset>
```

### Ensemble de boutons radio riches désactivés

```html
<fieldset class="fr-fieldset" id="radio-rich-disabled" aria-labelledby="radio-rich-disabled-legend radio-rich-disabled-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-rich-disabled-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="1" disabled type="radio" id="radio-rich-disabled-1" name="radio-rich-disabled">
            <label class="fr-label" for="radio-rich-disabled-1">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="2" disabled checked type="radio" id="radio-rich-disabled-2" name="radio-rich-disabled">
            <label class="fr-label" for="radio-rich-disabled-2">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="3" disabled type="radio" id="radio-rich-disabled-3" name="radio-rich-disabled">
            <label class="fr-label" for="radio-rich-disabled-3">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-radio-rich__pictogram">
                <svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
                    <use class="fr-artwork-decorative" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
                    <use class="fr-artwork-minor" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
                    <use class="fr-artwork-major" href="../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
                </svg>
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-rich-disabled-messages" aria-live="polite">
    </div>
</fieldset>
```
