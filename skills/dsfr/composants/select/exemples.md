# Liste déroulante : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Liste déroulante par défaut

```html
<div class="fr-select-group">
    <label class="fr-label" for="select">
        Libellé pour liste déroulante
    </label>
    <select class="fr-select" aria-describedby="select-messages" id="select" name="select">
        <option value="" selected disabled>Sélectionner une option</option>
        <option value="1">Option 1</option>
        <option value="2">Option 2</option>
        <option value="3">Option 3</option>
        <option value="4">Option 4</option>
    </select>
    <div class="fr-messages-group" id="select-messages" aria-live="polite">
    </div>
</div>
```

### Liste déroulante désactivée

```html
<div class="fr-select-group fr-select-group--disabled">
    <label class="fr-label" for="select-disabled">
        Libellé pour liste déroulante
    </label>
    <select class="fr-select" aria-describedby="select-disabled-messages" disabled id="select-disabled" name="select-disabled">
        <option value="" selected disabled>Sélectionner une option</option>
        <option value="1">Option 1</option>
        <option value="2">Option 2</option>
        <option value="3">Option 3</option>
        <option value="4">Option 4</option>
    </select>
    <div class="fr-messages-group" id="select-disabled-messages" aria-live="polite">
    </div>
</div>
```

### Liste déroulante avec texte de description

```html
<div class="fr-select-group">
    <label class="fr-label" for="select-hint">
        Libellé pour liste déroulante
        <span class="fr-hint-text">Texte de description additionnel</span>
    </label>
    <select class="fr-select" aria-describedby="select-hint-messages" id="select-hint" name="select-hint">
        <option value="" selected disabled>Sélectionner une option</option>
        <option value="1">Option 1</option>
        <option value="2">Option 2</option>
        <option value="3">Option 3</option>
        <option value="4">Option 4</option>
    </select>
    <div class="fr-messages-group" id="select-hint-messages" aria-live="polite">
    </div>
</div>
```

### Liste déroulante valide

```html
<div class="fr-select-group fr-select-group--valid">
    <label class="fr-label" for="select-valid">
        Libellé pour liste déroulante
    </label>
    <select class="fr-select" aria-describedby="select-valid-messages" id="select-valid" name="select-valid">
        <option value="" selected disabled>Sélectionner une option</option>
        <option value="1">Option 1</option>
        <option value="2">Option 2</option>
        <option value="3">Option 3</option>
        <option value="4">Option 4</option>
    </select>
    <div class="fr-messages-group" id="select-valid-messages" aria-live="polite">
        <p class="fr-message fr-message--valid" id="select-valid-message-valid">Texte de validation</p>
    </div>
</div>
```

### Liste déroulante erreur

```html
<div class="fr-select-group fr-select-group--error">
    <label class="fr-label" for="select-error">
        Libellé pour liste déroulante
    </label>
    <select class="fr-select" aria-describedby="select-error-messages" id="select-error" name="select-error">
        <option value="" selected disabled>Sélectionner une option</option>
        <option value="1">Option 1</option>
        <option value="2">Option 2</option>
        <option value="3">Option 3</option>
        <option value="4">Option 4</option>
    </select>
    <div class="fr-messages-group" id="select-error-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="select-error-message-error">Texte d’erreur obligatoire</p>
    </div>
</div>
```

### Liste déroulante avec groupe d'options

```html
<div class="fr-select-group">
    <label class="fr-label" for="select-group">
        Libellé pour liste déroulante
    </label>
    <select class="fr-select" aria-describedby="select-group-messages" id="select-group" name="select-group">
        <option value="" selected disabled>Selectionnez une option</option>
        <optgroup label="Groupe 1">
            <option value="1">Option 1</option>
            <option value="2">Option 2</option>
            <option value="3">Option 3</option>
            <option value="4">Option 4</option>
        </optgroup>
        <optgroup label="Groupe 2">
            <option value="5">Option 5</option>
            <option value="6">Option 6</option>
            <option value="7">Option 7</option>
        </optgroup>
    </select>
    <div class="fr-messages-group" id="select-group-messages" aria-live="polite">
    </div>
</div>
```
