# Numéro de téléphone : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Demande d'un numéro de téléphone

```html
<div class="fr-input-group" id="input-group-8148">
    <label class="fr-label" for="tel-8147">
        Numéro de téléphone
        <span class="fr-hint-text">Format attendu : (+33) 5 36 49 68 27</span>
    </label>
    <input class="fr-input" autocomplete="tel" aria-describedby="tel-8147-messages" id="tel-8147" type="tel">
    <div class="fr-messages-group" id="tel-8147-messages" aria-live="polite">
    </div>
</div>
```

### Demande d'un numéro de téléphone - Erreur

```html
<div class="fr-input-group fr-input-group--error" id="input-group-8153">
    <label class="fr-label" for="tel-8152">
        Numéro de téléphone
        <span class="fr-hint-text">Format attendu : (+33) 5 36 49 68 27</span>
    </label>
    <input class="fr-input" autocomplete="tel" aria-describedby="tel-8152-messages" id="tel-8152" type="tel">
    <div class="fr-messages-group" id="tel-8152-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="tel-8152-message-error">Le format de numéro de téléphone saisie n’est pas valide. Le format attendu est : (+33) 5 36 49 68 27</p>
    </div>
</div>
```
