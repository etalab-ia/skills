# Mot de passe : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Mot de passe

```html
<div class="fr-password" id="password-6168">
    <label class="fr-password__label fr-label" for="password-6168-input">
        Mot de passe
    </label>
    <div class="fr-input-wrap">
        <input class="fr-password__input fr-input" autocapitalize="off" autocorrect="off" aria-describedby="password-6168-input-messages" aria-required="true" name="password" autocomplete="new-password" id="password-6168-input" type="password">
    </div>
    <div class="fr-messages-group" id="password-6168-input-messages" aria-live="polite">
        <p class="fr-message" id="password-6168-input-message">Votre mot de passe doit contenir :</p>
        <p class="fr-message fr-message--info" data-fr-valid="validé" data-fr-error="en erreur" id="password-6168-input-message-info">12 caractères minimum</p>
        <p class="fr-message fr-message--info" data-fr-valid="validé" data-fr-error="en erreur" id="password-6168-input-message-info-1">1 caractère spécial minimum</p>
        <p class="fr-message fr-message--info" data-fr-valid="validé" data-fr-error="en erreur" id="password-6168-input-message-info-2">1 chiffre minimum</p>
    </div>
    <div class="fr-password__checkbox fr-checkbox-group fr-checkbox-group--sm">
        <input aria-label="Afficher le mot de passe" id="password-6168-show" type="checkbox">
        <label class="fr--password__checkbox fr-label" for="password-6168-show">
            Afficher
        </label>
    </div>
</div>
```

### Mot de passe avec description

```html
<div class="fr-password" id="password-6171">
    <label class="fr-password__label fr-label" for="password-6171-input">
        Mot de passe
        <span class="fr-hint-text">Texte de description additionnel</span>
    </label>
    <div class="fr-input-wrap">
        <input class="fr-password__input fr-input" autocapitalize="off" autocorrect="off" aria-describedby="password-6171-input-messages" aria-required="true" name="password" autocomplete="new-password" id="password-6171-input" type="password">
    </div>
    <div class="fr-messages-group" id="password-6171-input-messages" aria-live="polite">
        <p class="fr-message" id="password-6171-input-message">Votre mot de passe doit contenir :</p>
        <p class="fr-message fr-message--info" data-fr-valid="validé" data-fr-error="en erreur" id="password-6171-input-message-info">12 caractères minimum</p>
        <p class="fr-message fr-message--info" data-fr-valid="validé" data-fr-error="en erreur" id="password-6171-input-message-info-1">1 caractère spécial minimum</p>
        <p class="fr-message fr-message--info" data-fr-valid="validé" data-fr-error="en erreur" id="password-6171-input-message-info-2">1 chiffre minimum</p>
    </div>
    <div class="fr-password__checkbox fr-checkbox-group fr-checkbox-group--sm">
        <input aria-label="Afficher le mot de passe" id="password-6171-show" type="checkbox">
        <label class="fr--password__checkbox fr-label" for="password-6171-show">
            Afficher
        </label>
    </div>
</div>
```

### Mot de passe après validation

```html
<div class="fr-password" id="password-6174">
    <label class="fr-password__label fr-label" for="password-6174-input">
        Mot de passe
    </label>
    <div class="fr-input-wrap">
        <input class="fr-password__input fr-input" autocapitalize="off" autocorrect="off" aria-describedby="password-6174-input-messages" aria-required="true" name="password" value="x8A@" autocomplete="new-password" id="password-6174-input" type="password">
    </div>
    <div class="fr-messages-group" id="password-6174-input-messages" aria-live="polite">
        <p class="fr-message" id="password-6174-input-message">Votre mot de passe doit contenir :</p>
        <p class="fr-message fr-message--error" data-fr-valid="validé" data-fr-error="en erreur" id="password-6174-input-message-error">12 caractères minimum</p>
        <p class="fr-message fr-message--valid" data-fr-valid="validé" data-fr-error="en erreur" id="password-6174-input-message-valid">1 caractère spécial minimum</p>
        <p class="fr-message fr-message--valid" data-fr-valid="validé" data-fr-error="en erreur" id="password-6174-input-message-valid-1">1 chiffre minimum</p>
    </div>
    <div class="fr-password__checkbox fr-checkbox-group fr-checkbox-group--sm">
        <input aria-label="Afficher le mot de passe" id="password-6174-show" type="checkbox">
        <label class="fr--password__checkbox fr-label" for="password-6174-show">
            Afficher
        </label>
    </div>
</div>
```

### Mot de passe de connexion

```html
<div class="fr-password" id="password-6177">
    <label class="fr-password__label fr-label" for="password-6177-input">
        Mot de passe
    </label>
    <div class="fr-input-wrap">
        <input class="fr-password__input fr-input" autocapitalize="off" autocorrect="off" aria-describedby="password-6177-input-messages" aria-required="true" name="password" autocomplete="current-password" id="password-6177-input" type="password">
    </div>
    <div class="fr-messages-group" id="password-6177-input-messages" aria-live="polite">
    </div>
    <div class="fr-password__checkbox fr-checkbox-group fr-checkbox-group--sm">
        <input aria-label="Afficher le mot de passe" id="password-6177-show" type="checkbox">
        <label class="fr--password__checkbox fr-label" for="password-6177-show">
            Afficher
        </label>
    </div>
    <p>
        <a href="[À MODIFIER - url de la page de récupération]" class="fr-link">Mot de passe oublié ?</a>
    </p>
</div>
```
