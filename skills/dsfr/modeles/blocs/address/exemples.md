# Bloc fonctionnel d'adresse postale : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Demande d’une adresse postale nationale

```html
<fieldset class="fr-fieldset" id="address-7730" aria-labelledby="address-7730-legend address-7730-messages">
    <legend class="fr-sr-only" id="address-7730-legend">
        Adresse postale
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7731">
            <label class="fr-label" for="address-7725">
                Adresse
                <span class="fr-hint-text">Indication : numéro et voie</span>
            </label>
            <input class="fr-input" aria-describedby="address-7725-messages" name="address-line1" autocomplete="address-line1" id="address-7725" type="text">
            <div class="fr-messages-group" id="address-7725-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7732">
            <label class="fr-label" for="complement-7726">
                Complément d’adresse (optionnel)
                <span class="fr-hint-text">Indication : bâtiment, immeuble, escalier et numéro d’appartement</span>
            </label>
            <input class="fr-input" aria-describedby="complement-7726-messages" name="address-line2" autocomplete="address-line2" id="complement-7726" type="text">
            <div class="fr-messages-group" id="complement-7726-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--postal">
        <div class="fr-input-group" id="input-group-7733">
            <label class="fr-label" for="postal-7727">
                Code postal
                <span class="fr-hint-text">Format attendu : 5 chiffres</span>
            </label>
            <input class="fr-input" aria-describedby="postal-7727-messages" name="postal-code" autocomplete="postal-code" id="postal-7727" type="text">
            <div class="fr-messages-group" id="postal-7727-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline@md fr-fieldset__element--inline-grow">
        <div class="fr-input-group" id="input-group-7734">
            <label class="fr-label" for="city-7728">
                Ville ou commune
                <span class="fr-hint-text">Exemple : Montpellier</span>
            </label>
            <input class="fr-input" aria-describedby="city-7728-messages" name="address-level2" autocomplete="address-level2" id="city-7728" type="text">
            <div class="fr-messages-group" id="city-7728-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="address-7730-messages" aria-live="polite">
    </div>
</fieldset>
```

### Demande d’une adresse postale nationale + Lieu-dit, commune déléguée ou boîte postale

```html
<fieldset class="fr-fieldset" id="address-7754" aria-labelledby="address-7754-legend address-7754-messages">
    <legend class="fr-sr-only" id="address-7754-legend">
        Adresse postale
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7755">
            <label class="fr-label" for="address-7748">
                Adresse
                <span class="fr-hint-text">Indication : numéro et voie</span>
            </label>
            <input class="fr-input" aria-describedby="address-7748-messages" name="address-line1" autocomplete="address-line1" id="address-7748" type="text">
            <div class="fr-messages-group" id="address-7748-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7756">
            <label class="fr-label" for="complement-7749">
                Complément d’adresse (optionnel)
                <span class="fr-hint-text">Indication : bâtiment, immeuble, escalier et numéro d’appartement</span>
            </label>
            <input class="fr-input" aria-describedby="complement-7749-messages" name="address-line2" autocomplete="address-line2" id="complement-7749" type="text">
            <div class="fr-messages-group" id="complement-7749-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7757">
            <label class="fr-label" for="locality-7750">
                Lieu-dit, commune déléguée ou boîte postale
            </label>
            <input class="fr-input" aria-describedby="locality-7750-messages" name="address-level3" autocomplete="address-line3" id="locality-7750" type="text">
            <div class="fr-messages-group" id="locality-7750-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--postal">
        <div class="fr-input-group" id="input-group-7758">
            <label class="fr-label" for="postal-7751">
                Code postal
                <span class="fr-hint-text">Format attendu : 5 chiffres</span>
            </label>
            <input class="fr-input" aria-describedby="postal-7751-messages" name="postal-code" autocomplete="postal-code" id="postal-7751" type="text">
            <div class="fr-messages-group" id="postal-7751-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline@md fr-fieldset__element--inline-grow">
        <div class="fr-input-group" id="input-group-7759">
            <label class="fr-label" for="city-7752">
                Ville ou commune
                <span class="fr-hint-text">Exemple : Montpellier</span>
            </label>
            <input class="fr-input" aria-describedby="city-7752-messages" name="address-level2" autocomplete="address-level2" id="city-7752" type="text">
            <div class="fr-messages-group" id="city-7752-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="address-7754-messages" aria-live="polite">
    </div>
</fieldset>
```

### Complément d'adresse

```html
<fieldset class="fr-fieldset" id="address-7782" aria-labelledby="address-7782-legend address-7782-messages">
    <legend class="fr-sr-only" id="address-7782-legend">
        Complément d'adresse postale
    </legend>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--inline-grow fr-fieldset__element--number">
        <div class="fr-input-group" id="input-group-7783">
            <label class="fr-label" for="number-7776">
                Numéro
            </label>
            <input class="fr-input" aria-describedby="number-7776-messages" name="number" id="number-7776" type="text">
            <div class="fr-messages-group" id="number-7776-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--inline-grow">
        <div class="fr-input-group" id="input-group-7784">
            <label class="fr-label" for="street-7777">
                Voie
            </label>
            <input class="fr-input" aria-describedby="street-7777-messages" name="street" id="street-7777" type="text">
            <div class="fr-messages-group" id="street-7777-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7785">
            <label class="fr-label" for="building-7778">
                Bâtiment
            </label>
            <input class="fr-input" aria-describedby="building-7778-messages" name="building" id="building-7778" type="text">
            <div class="fr-messages-group" id="building-7778-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7786">
            <label class="fr-label" for="block-7779">
                Immeuble
            </label>
            <input class="fr-input" aria-describedby="block-7779-messages" name="block" id="block-7779" type="text">
            <div class="fr-messages-group" id="block-7779-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7787">
            <label class="fr-label" for="stare-7780">
                Escalier
            </label>
            <input class="fr-input" aria-describedby="stare-7780-messages" name="stare" id="stare-7780" type="text">
            <div class="fr-messages-group" id="stare-7780-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7788">
            <label class="fr-label" for="apartment-7781">
                Numéro d'appartement
            </label>
            <input class="fr-input" aria-describedby="apartment-7781-messages" name="apartment" id="apartment-7781" type="text">
            <div class="fr-messages-group" id="apartment-7781-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="address-7782-messages" aria-live="polite">
    </div>
</fieldset>
```
