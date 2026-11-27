# Bloc fonctionnel de nationalité : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Demande de nationalité

```html
<fieldset class="fr-fieldset" id="nationality-7870" aria-labelledby="nationality-7870-legend nationality-7870-messages">
    <legend class="fr-sr-only" id="nationality-7870-legend">
        Nationalité
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-select-group">
            <label class="fr-label" for="nationality-select-7869">
                Nationalité
            </label>
            <select class="fr-select" aria-describedby="nationality-select-7869-messages" id="nationality-select-7869" name="country">
                <option value="" selected disabled>Sélectionner une option</option>
                <option value="FR">Française</option>
                <option value="DE">Allemande</option>
                <option value="IT">Italienne</option>
                <option value="ES">Espagnole</option>
            </select>
            <div class="fr-messages-group" id="nationality-select-7869-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="nationality-7870-messages" aria-live="polite">
    </div>
</fieldset>
```
