# Adresse électronique : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Demande d'une adresse électronique

```html
<div class="fr-input-group" id="input-group-7849">
    <label class="fr-label" for="email-7848">
        Adresse électronique
        <span class="fr-hint-text">Format attendu : nom@example.com</span>
    </label>
    <input class="fr-input" spellcheck="false" autocomplete="email" aria-describedby="email-7848-messages" id="email-7848" type="email">
    <div class="fr-messages-group" id="email-7848-messages" aria-live="polite">
    </div>
</div>
```

### Demande d'une adresse électronique - Erreur

```html
<div class="fr-input-group fr-input-group--error" id="input-group-7854">
    <label class="fr-label" for="email-7853">
        Adresse électronique
        <span class="fr-hint-text">Format attendu : nom@example.com</span>
    </label>
    <input class="fr-input" spellcheck="false" autocomplete="email" aria-describedby="email-7853-messages" id="email-7853" type="email">
    <div class="fr-messages-group" id="email-7853-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="email-7853-message-error">Le format de l’adresse electronique saisie n’est pas valide. Le format attendu est : nom@example.com</p>
    </div>
</div>
```

### Demande et indication de traitement d’une adresse électronique

```html
<div class="fr-input-group" id="input-group-7859">
    <label class="fr-label" for="email-7858">
        Adresse électronique
        <span class="fr-hint-text">Indication : cette adresse est utilisée uniquement pour la connexion au service.</span>
        <span class="fr-hint-text">Format attendu : nom@example.com</span>
    </label>
    <input class="fr-input" spellcheck="false" autocomplete="email" aria-describedby="email-7858-messages" id="email-7858" type="email">
    <div class="fr-messages-group" id="email-7858-messages" aria-live="polite">
    </div>
</div>
```

### Demande et indication de traitement d’une adresse électronique - Erreur

```html
<div class="fr-input-group fr-input-group--error" id="input-group-7864">
    <label class="fr-label" for="email-7863">
        Adresse électronique
        <span class="fr-hint-text">Indication : cette adresse est utilisée uniquement pour la connexion au service.</span>
        <span class="fr-hint-text">Format attendu : nom@example.com</span>
    </label>
    <input class="fr-input" spellcheck="false" autocomplete="email" aria-describedby="email-7863-messages" id="email-7863" type="email">
    <div class="fr-messages-group" id="email-7863-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="email-7863-message-error">Le format de l’adresse electronique saisie n’est pas valide. Le format attendu est : nom@example.com</p>
    </div>
</div>
```
