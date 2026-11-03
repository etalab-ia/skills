# Case à cocher : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Case à cocher seule

```html
<div class="fr-checkbox-group">
    <input id="checkbox" type="checkbox" aria-describedby="checkbox-messages">
    <label class="fr-label" for="checkbox">
        Libellé checkbox
    </label>
    <div class="fr-messages-group" id="checkbox-messages" aria-live="polite">
    </div>
</div>
```

### Case à cocher seule, exemple avec indice et exposant

```html
<div class="fr-checkbox-group">
    <input id="checkbox-sup-sub" type="checkbox" aria-describedby="checkbox-sup-sub-messages">
    <label class="fr-label" for="checkbox-sup-sub">
        <span>Libellé checkbox <sub>sub</sub> et <sup>sup</sup>
        </span>
    </label>
    <div class="fr-messages-group" id="checkbox-sup-sub-messages" aria-live="polite">
    </div>
</div>
```

### Case à cocher avec texte d’aide

```html
<div class="fr-checkbox-group">
    <input id="checkbox-hint" type="checkbox" aria-describedby="checkbox-hint-messages">
    <label class="fr-label" for="checkbox-hint">
        Libellé checkbox
        <span class="fr-hint-text">Texte de description additionnel</span>
    </label>
    <div class="fr-messages-group" id="checkbox-hint-messages" aria-live="polite">
    </div>
</div>
```

### Case à cocher seule, validée

```html
<div class="fr-checkbox-group fr-checkbox-group--valid">
    <input aria-describedby="checkbox-valid-messages" id="checkbox-valid" type="checkbox">
    <label class="fr-label" for="checkbox-valid">
        Libellé checkbox
    </label>
    <div class="fr-messages-group" id="checkbox-valid-messages" aria-live="polite">
        <p class="fr-message fr-message--valid" id="checkbox-valid-message-valid">Texte de validation</p>
    </div>
</div>
```

### Case à cocher seule avec erreur

```html
<div class="fr-checkbox-group fr-checkbox-group--error">
    <input aria-describedby="checkbox-error-messages" id="checkbox-error" type="checkbox">
    <label class="fr-label" for="checkbox-error">
        Libellé checkbox
    </label>
    <div class="fr-messages-group" id="checkbox-error-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="checkbox-error-message-error">Texte d’erreur obligatoire</p>
    </div>
</div>
```

### Case à cocher seule, indéterminée

```html
<div class="fr-checkbox-group">
    <input id="checkbox-mixed-indeterminate-indeterminate" type="checkbox" aria-describedby="checkbox-mixed-indeterminate-messages">
    <label class="fr-label" for="checkbox-mixed-indeterminate">
        Libellé checkbox
    </label>
    <div class="fr-messages-group" id="checkbox-mixed-indeterminate-messages" aria-live="polite">
    </div>
</div>
```

### Ensemble de cases à cocher

```html
<fieldset class="fr-fieldset" id="checkboxes" aria-labelledby="checkboxes-legend checkboxes-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkboxes-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkboxes-1" id="checkboxes-1-indeterminate" type="checkbox" aria-describedby="checkboxes-1-indeterminate-messages">
            <label class="fr-label" for="checkboxes-1-indeterminate">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-1-indeterminate-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input checked name="checkboxes-2" id="checkboxes-2" type="checkbox" aria-describedby="checkboxes-2-messages">
            <label class="fr-label" for="checkboxes-2">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-2-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkboxes-3" id="checkboxes-3" type="checkbox" aria-describedby="checkboxes-3-messages">
            <label class="fr-label" for="checkboxes-3">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-3-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="checkboxes-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de cases à cocher, petite taille

```html
<fieldset class="fr-fieldset" id="checkboxes-small" aria-labelledby="checkboxes-small-legend checkboxes-small-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkboxes-small-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group fr-checkbox-group--sm">
            <input name="checkboxes-small-1" id="checkboxes-small-1-indeterminate" type="checkbox" aria-describedby="checkboxes-small-1-indeterminate-messages">
            <label class="fr-label" for="checkboxes-small-1-indeterminate">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-small-1-indeterminate-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group fr-checkbox-group--sm">
            <input checked name="checkboxes-small-2" id="checkboxes-small-2" type="checkbox" aria-describedby="checkboxes-small-2-messages">
            <label class="fr-label" for="checkboxes-small-2">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-small-2-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group fr-checkbox-group--sm">
            <input name="checkboxes-small-3" id="checkboxes-small-3" type="checkbox" aria-describedby="checkboxes-small-3-messages">
            <label class="fr-label" for="checkboxes-small-3">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-small-3-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="checkboxes-small-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de cases à cocher désactivées

```html
<fieldset class="fr-fieldset" id="checkboxes-disabled" aria-labelledby="checkboxes-disabled-legend checkboxes-disabled-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkboxes-disabled-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input disabled name="checkboxes-disabled-1" id="checkboxes-disabled-1-indeterminate" type="checkbox" aria-describedby="checkboxes-disabled-1-indeterminate-messages">
            <label class="fr-label" for="checkboxes-disabled-1-indeterminate">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-disabled-1-indeterminate-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input checked disabled name="checkboxes-disabled-2" id="checkboxes-disabled-2" type="checkbox" aria-describedby="checkboxes-disabled-2-messages">
            <label class="fr-label" for="checkboxes-disabled-2">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-disabled-2-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input disabled name="checkboxes-disabled-3" id="checkboxes-disabled-3" type="checkbox" aria-describedby="checkboxes-disabled-3-messages">
            <label class="fr-label" for="checkboxes-disabled-3">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-disabled-3-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="checkboxes-disabled-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de cases à cocher en ligne

```html
<fieldset class="fr-fieldset" id="checkboxes-inline" aria-labelledby="checkboxes-inline-legend checkboxes-inline-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkboxes-inline-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-checkbox-group">
            <input name="checkboxes-inline-1" id="checkboxes-inline-1" type="checkbox" aria-describedby="checkboxes-inline-1-messages">
            <label class="fr-label" for="checkboxes-inline-1">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-inline-1-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-checkbox-group">
            <input name="checkboxes-inline-2" id="checkboxes-inline-2" type="checkbox" aria-describedby="checkboxes-inline-2-messages">
            <label class="fr-label" for="checkboxes-inline-2">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-inline-2-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-checkbox-group">
            <input name="checkboxes-inline-3" id="checkboxes-inline-3" type="checkbox" aria-describedby="checkboxes-inline-3-messages">
            <label class="fr-label" for="checkboxes-inline-3">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-inline-3-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="checkboxes-inline-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de cases à cocher avec texte d’aide

```html
<fieldset class="fr-fieldset" id="checkboxes-hint" aria-labelledby="checkboxes-hint-legend checkboxes-hint-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkboxes-hint-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkboxes-hint-1" id="checkboxes-hint-1" type="checkbox" aria-describedby="checkboxes-hint-1-messages">
            <label class="fr-label" for="checkboxes-hint-1">
                Libellé case à cocher
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-messages-group" id="checkboxes-hint-1-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkboxes-hint-2" id="checkboxes-hint-2" type="checkbox" aria-describedby="checkboxes-hint-2-messages">
            <label class="fr-label" for="checkboxes-hint-2">
                Libellé case à cocher
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-messages-group" id="checkboxes-hint-2-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkboxes-hint-3" id="checkboxes-hint-3" type="checkbox" aria-describedby="checkboxes-hint-3-messages">
            <label class="fr-label" for="checkboxes-hint-3">
                Libellé case à cocher
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-messages-group" id="checkboxes-hint-3-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="checkboxes-hint-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de cases à cocher avec erreur

```html
<fieldset class="fr-fieldset fr-fieldset--error" id="checkboxes-error" role="group" aria-labelledby="checkboxes-error-legend checkboxes-error-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkboxes-error-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkboxes-error-1" id="checkboxes-error-1" type="checkbox" aria-describedby="checkboxes-error-1-messages">
            <label class="fr-label" for="checkboxes-error-1">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-error-1-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkboxes-error-2" id="checkboxes-error-2" type="checkbox" aria-describedby="checkboxes-error-2-messages">
            <label class="fr-label" for="checkboxes-error-2">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-error-2-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkboxes-error-3" id="checkboxes-error-3" type="checkbox" aria-describedby="checkboxes-error-3-messages">
            <label class="fr-label" for="checkboxes-error-3">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-error-3-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="checkboxes-error-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="checkboxes-error-message-error">Texte d’erreur obligatoire</p>
    </div>
</fieldset>
```

### Ensemble de cases à cocher validées

```html
<fieldset class="fr-fieldset fr-fieldset--valid" id="checkboxes-valid" role="group" aria-labelledby="checkboxes-valid-legend checkboxes-valid-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkboxes-valid-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkboxes-valid-1" id="checkboxes-valid-1" type="checkbox" aria-describedby="checkboxes-valid-1-messages">
            <label class="fr-label" for="checkboxes-valid-1">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-valid-1-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkboxes-valid-2" id="checkboxes-valid-2" type="checkbox" aria-describedby="checkboxes-valid-2-messages">
            <label class="fr-label" for="checkboxes-valid-2">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-valid-2-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkboxes-valid-3" id="checkboxes-valid-3" type="checkbox" aria-describedby="checkboxes-valid-3-messages">
            <label class="fr-label" for="checkboxes-valid-3">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-valid-3-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="checkboxes-valid-messages" aria-live="polite">
        <p class="fr-message fr-message--valid" id="checkboxes-valid-message-valid">Texte de validation</p>
    </div>
</fieldset>
```

### Ensemble de cases à cocher avec erreur, en ligne

```html
<fieldset class="fr-fieldset fr-fieldset--error" id="checkboxes-error-inline" role="group" aria-labelledby="checkboxes-error-inline-legend checkboxes-error-inline-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkboxes-error-inline-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-checkbox-group">
            <input name="checkboxes-error-inline-1" id="checkboxes-error-inline-1" type="checkbox" aria-describedby="checkboxes-error-inline-1-messages">
            <label class="fr-label" for="checkboxes-error-inline-1">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-error-inline-1-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-checkbox-group">
            <input name="checkboxes-error-inline-2" id="checkboxes-error-inline-2" type="checkbox" aria-describedby="checkboxes-error-inline-2-messages">
            <label class="fr-label" for="checkboxes-error-inline-2">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-error-inline-2-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-checkbox-group">
            <input name="checkboxes-error-inline-3" id="checkboxes-error-inline-3" type="checkbox" aria-describedby="checkboxes-error-inline-3-messages">
            <label class="fr-label" for="checkboxes-error-inline-3">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-error-inline-3-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="checkboxes-error-inline-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="checkboxes-error-inline-message-error">Texte d’erreur obligatoire</p>
    </div>
</fieldset>
```

### Ensemble de cases à cocher validées, en ligne

```html
<fieldset class="fr-fieldset fr-fieldset--valid" id="checkboxes-valid-inline" role="group" aria-labelledby="checkboxes-valid-inline-legend checkboxes-valid-inline-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkboxes-valid-inline-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-checkbox-group">
            <input name="checkboxes-valid-inline-1" id="checkboxes-valid-inline-1" type="checkbox" aria-describedby="checkboxes-valid-inline-1-messages">
            <label class="fr-label" for="checkboxes-valid-inline-1">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-valid-inline-1-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-checkbox-group">
            <input name="checkboxes-valid-inline-2" id="checkboxes-valid-inline-2" type="checkbox" aria-describedby="checkboxes-valid-inline-2-messages">
            <label class="fr-label" for="checkboxes-valid-inline-2">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-valid-inline-2-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-checkbox-group">
            <input name="checkboxes-valid-inline-3" id="checkboxes-valid-inline-3" type="checkbox" aria-describedby="checkboxes-valid-inline-3-messages">
            <label class="fr-label" for="checkboxes-valid-inline-3">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkboxes-valid-inline-3-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="checkboxes-valid-inline-messages" aria-live="polite">
        <p class="fr-message fr-message--valid" id="checkboxes-valid-inline-message-valid">Texte de validation</p>
    </div>
</fieldset>
```

### Ensemble de cases à cocher avec texte d’aide spécifique

```html
<fieldset class="fr-fieldset" id="checkboxes-hint-element" aria-labelledby="checkboxes-hint-element-legend checkboxes-hint-element-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkboxes-hint-element-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkboxes-hint-element-1" id="checkboxes-hint-element-1" type="checkbox" aria-describedby="checkboxes-hint-element-1-messages">
            <label class="fr-label" for="checkboxes-hint-element-1">
                Libellé case à cocher
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-messages-group" id="checkboxes-hint-element-1-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkboxes-hint-element-2" id="checkboxes-hint-element-2" type="checkbox" aria-describedby="checkboxes-hint-element-2-messages">
            <label class="fr-label" for="checkboxes-hint-element-2">
                Libellé case à cocher
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-messages-group" id="checkboxes-hint-element-2-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkboxes-hint-element-3" id="checkboxes-hint-element-3" type="checkbox" aria-describedby="checkboxes-hint-element-3-messages">
            <label class="fr-label" for="checkboxes-hint-element-3">
                Libellé case à cocher
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-messages-group" id="checkboxes-hint-element-3-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="checkboxes-hint-element-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de cases à cocher avec texte d’aide spécifique, petite taille

```html
<fieldset class="fr-fieldset" id="checkboxes-hint-el-sm" aria-labelledby="checkboxes-hint-el-sm-legend checkboxes-hint-el-sm-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkboxes-hint-el-sm-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group fr-checkbox-group--sm">
            <input name="checkboxes-hint-el-sm-1" id="checkboxes-hint-el-sm-1" type="checkbox" aria-describedby="checkboxes-hint-el-sm-1-messages">
            <label class="fr-label" for="checkboxes-hint-el-sm-1">
                Libellé case à cocher
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-messages-group" id="checkboxes-hint-el-sm-1-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group fr-checkbox-group--sm">
            <input name="checkboxes-hint-el-sm-2" id="checkboxes-hint-el-sm-2" type="checkbox" aria-describedby="checkboxes-hint-el-sm-2-messages">
            <label class="fr-label" for="checkboxes-hint-el-sm-2">
                Libellé case à cocher
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-messages-group" id="checkboxes-hint-el-sm-2-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group fr-checkbox-group--sm">
            <input name="checkboxes-hint-el-sm-3" id="checkboxes-hint-el-sm-3" type="checkbox" aria-describedby="checkboxes-hint-el-sm-3-messages">
            <label class="fr-label" for="checkboxes-hint-el-sm-3">
                Libellé case à cocher
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-messages-group" id="checkboxes-hint-el-sm-3-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="checkboxes-hint-el-sm-messages" aria-live="polite">
    </div>
</fieldset>
```
