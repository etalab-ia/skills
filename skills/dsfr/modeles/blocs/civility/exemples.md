# Civilité : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Demande du sexe

```html
<fieldset class="fr-fieldset" id="sex-7794" aria-labelledby="sex-7794-legend sex-7794-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="sex-7794-legend">
        Sexe
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-group--sm">
            <input type="radio" id="female-7795" name="sex">
            <label class="fr-label" for="female-7795">
                Feminin
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-group--sm">
            <input type="radio" id="male-7796" name="sex">
            <label class="fr-label" for="male-7796">
                Masculin
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="sex-7794-messages" aria-live="polite">
    </div>
</fieldset>
```

### Demande de situation familiale

```html
<fieldset class="fr-fieldset" id="family-7800" aria-labelledby="family-7800-legend family-7800-messages">
    <legend class="fr-sr-only" id="family-7800-legend">
        Demande de situation familiale
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-select-group">
            <label class="fr-label" for="family-7801">
                Situation familiale
            </label>
            <select class="fr-select" aria-describedby="family-7801-messages" id="family-7801" name="family">
                <option value="" selected disabled>Sélectionner une option</option>
                <option value="1">Célibataire</option>
                <option value="2">Concubinage</option>
                <option value="3">Pacsé</option>
                <option value="4">Marié</option>
                <option value="5">Veuf</option>
                <option value="6">Divorcé</option>
                <option value="7">Sans réponse</option>
            </select>
            <div class="fr-messages-group" id="family-7801-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="family-7800-messages" aria-live="polite">
    </div>
</fieldset>
```

### Demande du titre d’appel

Les boutons radios sont recommandés lorsque l’utilisateur doit choisir un élément parmi 2 à 5 choix possibles.

```html
<fieldset class="fr-fieldset" id="honorific-7807" aria-labelledby="honorific-7807-legend honorific-7807-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="honorific-7807-legend">
        Titre d’appel
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-group--sm">
            <input type="radio" id="honorific-7808" name="honorific">
            <label class="fr-label" for="honorific-7808">
                Docteur
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-group--sm">
            <input type="radio" id="honorific-7809" name="honorific">
            <label class="fr-label" for="honorific-7809">
                Inspecteur
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-radio-group fr-radio-group--sm">
            <input type="radio" id="honorific-7810" name="honorific">
            <label class="fr-label" for="honorific-7810">
                Sans réponse
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="honorific-7807-messages" aria-live="polite">
    </div>
</fieldset>
```

### Demande du titre d’appel

Au delà de 5 choix ou lorsque l’espace n’est pas suffisant, il est préférable d’utiliser une liste déroulante.

```html
<fieldset class="fr-fieldset" id="honorific-7814" aria-labelledby="honorific-7814-legend honorific-7814-messages">
    <legend class="fr-sr-only" id="honorific-7814-legend">
        Demande du titre d’appel
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-select-group">
            <label class="fr-label" for="honorific-7815">
                Titre d’appel
            </label>
            <select class="fr-select" aria-describedby="honorific-7815-messages" id="honorific-7815" name="honorific">
                <option value="" selected disabled>Sélectionner une option</option>
                <option value="1">Recteur</option>
                <option value="2">Inspecteur</option>
                <option value="3">Proviseur</option>
                <option value="4">Professeur</option>
                <option value="5">Docteur</option>
                <option value="6">Principal</option>
                <option value="7">Sans réponse</option>
            </select>
            <div class="fr-messages-group" id="honorific-7815-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="honorific-7814-messages" aria-live="polite">
    </div>
</fieldset>
```
