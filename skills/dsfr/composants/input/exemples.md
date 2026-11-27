# Champ de saisie : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Champ de type "text"

```html
<div class="fr-input-group" id="input-group-1518">
    <label class="fr-label" for="text-input-text">
        Libellé champ de saisie
    </label>
    <input class="fr-input" aria-describedby="text-input-text-messages" id="text-input-text" type="text">
    <div class="fr-messages-group" id="text-input-text-messages" aria-live="polite">
    </div>
</div>
```

### Champ de type "number"

```html
<div class="fr-input-group" id="input-group-1521">
    <label class="fr-label" for="text-input-number">
        Libellé champ de saisie
    </label>
    <input class="fr-input" pattern="[0-9]*" inputmode="numeric" aria-describedby="text-input-number-messages" id="text-input-number" type="number">
    <div class="fr-messages-group" id="text-input-number-messages" aria-live="polite">
    </div>
</div>
```

### Champ de type "search"

```html
<div class="fr-input-group" id="input-group-1524">
    <label class="fr-label" for="text-input-search">
        Libellé champ de saisie
    </label>
    <input class="fr-input" aria-describedby="text-input-search-messages" id="text-input-search" type="search">
    <div class="fr-messages-group" id="text-input-search-messages" aria-live="polite">
    </div>
</div>
```

### Champ de type "date"

```html
<div class="fr-input-group" id="input-group-1527">
    <label class="fr-label" for="text-input-date">
        Libellé champ de saisie
    </label>
    <input class="fr-input" aria-describedby="text-input-date-messages" id="text-input-date" type="date">
    <div class="fr-messages-group" id="text-input-date-messages" aria-live="polite">
    </div>
</div>
```

### Champ de type "textarea"

```html
<div class="fr-input-group" id="input-group-1530">
    <label class="fr-label" for="textarea">
        Libellé champ de saisie
    </label>
    <textarea class="fr-input" aria-describedby="textarea-messages" id="textarea"></textarea>
    <div class="fr-messages-group" id="textarea-messages" aria-live="polite">
    </div>
</div>
```

### Champ de type "password"

```html
<div class="fr-input-group" id="input-group-1533">
    <label class="fr-label" for="text-input-password">
        Libellé champ de saisie
    </label>
    <input class="fr-input" aria-describedby="text-input-password-messages" id="text-input-password" type="password">
    <div class="fr-messages-group" id="text-input-password-messages" aria-live="polite">
    </div>
</div>
```

### Combo champ + bouton d'envoi

```html
<div class="fr-input-group" id="input-group-1536">
    <label class="fr-label" for="text-input-button">
        Libellé champ de saisie
    </label>
    <div class="fr-input-wrap fr-input-wrap--addon">
        <input class="fr-input" aria-describedby="text-input-button-messages" id="text-input-button" type="text">
        <button type="submit" class="fr-btn">Envoyer</button>
    </div>
    <div class="fr-messages-group" id="text-input-button-messages" aria-live="polite">
    </div>
</div>
```

### Combo champ + bouton d'action

```html
<div class="fr-input-group" id="input-group-1539">
    <label class="fr-label" for="text-input-action">
        Libellé champ de saisie
    </label>
    <div class="fr-input-wrap fr-input-wrap--action">
        <input class="fr-input" aria-describedby="text-input-action-messages" id="text-input-action" type="text">
        <button type="button" class="fr-btn fr-icon-delete-line fr-btn--secondary">Supprimer le champ</button>
    </div>
    <div class="fr-messages-group" id="text-input-action-messages" aria-live="polite">
    </div>
</div>
```

### Champ avec placeholder

```html
<div class="fr-input-group" id="input-group-1542">
    <label class="fr-label" for="text-input-placeholder">
        Libellé champ de saisie
    </label>
    <input class="fr-input" aria-describedby="text-input-placeholder-messages" placeholder="placeholder" id="text-input-placeholder" type="text">
    <div class="fr-messages-group" id="text-input-placeholder-messages" aria-live="polite">
    </div>
</div>
```

### Champ avec valeur initiale

```html
<div class="fr-input-group" id="input-group-1545">
    <label class="fr-label" for="text-input-value">
        Libellé champ de saisie
    </label>
    <input class="fr-input" value="value" aria-describedby="text-input-value-messages" id="text-input-value" type="text">
    <div class="fr-messages-group" id="text-input-value-messages" aria-live="polite">
    </div>
</div>
```

### Champ avec icône personalisée

```html
<div class="fr-input-group" id="input-group-1548">
    <label class="fr-label" for="text-input-icon">
        Libellé champ de saisie
        <span class="fr-hint-text">Texte de description additionnel</span>
    </label>
    <div class="fr-input-wrap fr-icon-alert-line">
        <input class="fr-input" aria-describedby="text-input-icon-messages" id="text-input-icon" type="text">
    </div>
    <div class="fr-messages-group" id="text-input-icon-messages" aria-live="polite">
    </div>
</div>
```

### Champ désactivé

```html
<div class="fr-input-group fr-input-group--disabled" id="input-group-1551">
    <label class="fr-label" for="text-input-disabled">
        Libellé champ de saisie
    </label>
    <input class="fr-input" aria-describedby="text-input-disabled-messages" disabled id="text-input-disabled" type="text">
    <div class="fr-messages-group" id="text-input-disabled-messages" aria-live="polite">
    </div>
</div>
```

### Champ avec texte additionnel

```html
<div class="fr-input-group" id="input-group-1554">
    <label class="fr-label" for="text-input-hint">
        Libellé champ de saisie
        <span class="fr-hint-text">Texte de description additionnel</span>
    </label>
    <input class="fr-input" aria-describedby="text-input-hint-messages" id="text-input-hint" type="text">
    <div class="fr-messages-group" id="text-input-hint-messages" aria-live="polite">
    </div>
</div>
```

### Champ valide avec texte de succès

```html
<div class="fr-input-group fr-input-group--valid" id="input-group-1557">
    <label class="fr-label" for="text-input-valid">
        Libellé champ de saisie
    </label>
    <input class="fr-input" aria-describedby="text-input-valid-messages" id="text-input-valid" type="text">
    <div class="fr-messages-group" id="text-input-valid-messages" aria-live="polite">
        <p class="fr-message fr-message--valid" id="text-input-valid-message-valid">Texte de validation</p>
    </div>
</div>
```

### Champ en erreur avec texte d'erreur

```html
<div class="fr-input-group fr-input-group--error" id="input-group-1560">
    <label class="fr-label" for="text-input-error">
        Libellé champ de saisie
    </label>
    <input class="fr-input" aria-describedby="text-input-error-messages" id="text-input-error" type="text">
    <div class="fr-messages-group" id="text-input-error-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="text-input-error-message-error">Texte d’erreur obligatoire</p>
    </div>
</div>
```
