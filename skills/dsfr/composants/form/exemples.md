# Formulaire : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Ensemble de champs de saisie

```html
<fieldset class="fr-fieldset" id="text" aria-labelledby="text-legend text-messages">
    <legend class="fr-fieldset__legend" id="text-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-3767">
            <label class="fr-label" for="text-1">
                Libellé champ de saisie
            </label>
            <input class="fr-input" aria-describedby="text-1-messages" name="text-1" id="text-1" type="text">
            <div class="fr-messages-group" id="text-1-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-3768">
            <label class="fr-label" for="text-2">
                Libellé champ de saisie
            </label>
            <input class="fr-input" aria-describedby="text-2-messages" name="text-2" id="text-2" type="text">
            <div class="fr-messages-group" id="text-2-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-3769">
            <label class="fr-label" for="text-3">
                Libellé champ de saisie
            </label>
            <input class="fr-input" aria-describedby="text-3-messages" name="text-3" id="text-3" type="text">
            <div class="fr-messages-group" id="text-3-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="text-messages" aria-live="polite">
    </div>
</fieldset>
```

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
            <input value="2" type="radio" id="radio-2" name="radio">
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

### Ensemble de cases à cocher

```html
<fieldset class="fr-fieldset" id="checkbox" aria-labelledby="checkbox-legend checkbox-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkbox-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkbox-1" id="checkbox-1" type="checkbox" aria-describedby="checkbox-1-messages">
            <label class="fr-label" for="checkbox-1">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkbox-1-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkbox-2" id="checkbox-2" type="checkbox" aria-describedby="checkbox-2-messages">
            <label class="fr-label" for="checkbox-2">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkbox-2-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkbox-3" id="checkbox-3" type="checkbox" aria-describedby="checkbox-3-messages">
            <label class="fr-label" for="checkbox-3">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkbox-3-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="checkbox-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de boutons radio, en ligne

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

### Ensemble de cases à cocher, en ligne

```html
<fieldset class="fr-fieldset" id="checkbox-inline" aria-labelledby="checkbox-inline-legend checkbox-inline-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkbox-inline-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-checkbox-group">
            <input name="checkbox-inline-1" id="checkbox-inline-1" type="checkbox" aria-describedby="checkbox-inline-1-messages">
            <label class="fr-label" for="checkbox-inline-1">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkbox-inline-1-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-checkbox-group">
            <input name="checkbox-inline-2" id="checkbox-inline-2" type="checkbox" aria-describedby="checkbox-inline-2-messages">
            <label class="fr-label" for="checkbox-inline-2">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkbox-inline-2-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline">
        <div class="fr-checkbox-group">
            <input name="checkbox-inline-3" id="checkbox-inline-3" type="checkbox" aria-describedby="checkbox-inline-3-messages">
            <label class="fr-label" for="checkbox-inline-3">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkbox-inline-3-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="checkbox-inline-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de boutons radio avec erreur

```html
<fieldset class="fr-fieldset fr-fieldset--error" id="radio-error" role="group" aria-labelledby="radio-error-legend radio-error-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-error-legend">
        Légende pour l’ensemble des éléments
        <span class="fr-hint-text">Texte de description additionnel</span>
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

### Ensemble de boutons radio riches

```html
<fieldset class="fr-fieldset" id="radio-rich" aria-labelledby="radio-rich-legend radio-rich-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-rich-legend">
        Légende pour l’ensemble des éléments
        <span class="fr-hint-text">Texte de description additionnel</span>
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="1" type="radio" id="radio-rich-1" name="radio-rich">
            <label class="fr-label" for="radio-rich-1">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="2" type="radio" id="radio-rich-2" name="radio-rich">
            <label class="fr-label" for="radio-rich-2">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-rich">
            <input value="3" type="radio" id="radio-rich-3" name="radio-rich">
            <label class="fr-label" for="radio-rich-3">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-rich-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de cases à cocher, avec erreur

```html
<fieldset class="fr-fieldset fr-fieldset--error" id="checkbox-error" role="group" aria-labelledby="checkbox-error-legend checkbox-error-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkbox-error-legend">
        Légende pour l’ensemble des éléments
        <span class="fr-hint-text">Texte de description additionnel</span>
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkbox-error-1" id="checkbox-error-1" type="checkbox" aria-describedby="checkbox-error-1-messages">
            <label class="fr-label" for="checkbox-error-1">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkbox-error-1-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkbox-error-2" id="checkbox-error-2" type="checkbox" aria-describedby="checkbox-error-2-messages">
            <label class="fr-label" for="checkbox-error-2">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkbox-error-2-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkbox-error-3" id="checkbox-error-3" type="checkbox" aria-describedby="checkbox-error-3-messages">
            <label class="fr-label" for="checkbox-error-3">
                Libellé case à cocher
            </label>
            <div class="fr-messages-group" id="checkbox-error-3-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="checkbox-error-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="checkbox-error-message-error">Texte d’erreur obligatoire</p>
    </div>
</fieldset>
```

### Ensemble de champs de saisie désactivés

```html
<fieldset class="fr-fieldset" id="text-disabled" disabled aria-labelledby="text-disabled-legend text-disabled-messages">
    <legend class="fr-fieldset__legend" id="text-disabled-legend">
        Légende pour l’ensemble des éléments
        <span class="fr-hint-text">Texte de description additionnel</span>
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-3781">
            <label class="fr-label" for="text-disabled-1">
                Libellé champ de saisie
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <input class="fr-input" aria-describedby="text-disabled-1-messages" name="text-disabled-1" id="text-disabled-1" type="text">
            <div class="fr-messages-group" id="text-disabled-1-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-3782">
            <label class="fr-label" for="text-disabled-2">
                Libellé champ de saisie
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <input class="fr-input" aria-describedby="text-disabled-2-messages" name="text-disabled-2" id="text-disabled-2" type="text">
            <div class="fr-messages-group" id="text-disabled-2-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-3783">
            <label class="fr-label" for="text-disabled-3">
                Libellé champ de saisie
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <input class="fr-input" aria-describedby="text-disabled-3-messages" name="text-disabled-3" id="text-disabled-3" type="text">
            <div class="fr-messages-group" id="text-disabled-3-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="text-disabled-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de boutons radio désactivés

```html
<fieldset class="fr-fieldset" id="radio-disabled" disabled aria-labelledby="radio-disabled-legend radio-disabled-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-disabled-legend">
        Légende pour l’ensemble des éléments
        <span class="fr-hint-text">Texte de description additionnel</span>
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="1" type="radio" id="radio-disabled-1" name="radio-disabled">
            <label class="fr-label" for="radio-disabled-1">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="2" type="radio" id="radio-disabled-2" name="radio-disabled">
            <label class="fr-label" for="radio-disabled-2">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group">
            <input value="3" type="radio" id="radio-disabled-3" name="radio-disabled">
            <label class="fr-label" for="radio-disabled-3">
                Libellé bouton radio
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="radio-disabled-messages" aria-live="polite">
    </div>
</fieldset>
```

### Ensemble de cases à cocher désactivés

```html
<fieldset class="fr-fieldset" id="checkbox-disabled" disabled aria-labelledby="checkbox-disabled-legend checkbox-disabled-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkbox-disabled-legend">
        Légende pour l’ensemble des éléments
        <span class="fr-hint-text">Texte de description additionnel</span>
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkbox-disabled-1" id="checkbox-disabled-1" type="checkbox" aria-describedby="checkbox-disabled-1-messages">
            <label class="fr-label" for="checkbox-disabled-1">
                Libellé case à cocher
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-messages-group" id="checkbox-disabled-1-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkbox-disabled-2" id="checkbox-disabled-2" type="checkbox" aria-describedby="checkbox-disabled-2-messages">
            <label class="fr-label" for="checkbox-disabled-2">
                Libellé case à cocher
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-messages-group" id="checkbox-disabled-2-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkbox-disabled-3" id="checkbox-disabled-3" type="checkbox" aria-describedby="checkbox-disabled-3-messages">
            <label class="fr-label" for="checkbox-disabled-3">
                Libellé case à cocher
                <span class="fr-hint-text">Texte de description additionnel</span>
            </label>
            <div class="fr-messages-group" id="checkbox-disabled-3-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="checkbox-disabled-messages" aria-live="polite">
    </div>
</fieldset>
```

### Bouton type submit

```html
<button title="Envoyer le formulaire" type="submit" class="fr-btn">Envoyer</button>
```

### Input type submit

```html
<input title="Envoyer le formulaire" type="submit" value="Envoyer" class="fr-btn">
```

### Messages de formulaire

```html
<div class="fr-messages-group" id="message-group" aria-live="polite">
    <p class="fr-message" id="message-neutral">Message neutre</p>
    <p class="fr-message fr-message--info" id="message-info">Message d'information</p>
    <p class="fr-message fr-message--valid" id="message-valid">Message de succès</p>
    <p class="fr-message fr-message--warning" id="message-warning">Message d'avertissement</p>
    <p class="fr-message fr-message--error" id="message-error">Message d'erreur</p>
</div>
```
