# Nom et prénom : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

## Demande d’un nom et d’un prénom en France

### Défaut

```html
<fieldset class="fr-fieldset" id="firstname-disabled-7883" aria-labelledby="firstname-disabled-7883-legend firstname-disabled-7883-messages">
    <legend class="fr-sr-only" id="firstname-disabled-7883-legend">
        Nom
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7891">
            <label class="fr-label" for="family-name-7885">
                Nom
            </label>
            <input class="fr-input" aria-describedby="family-name-7885-messages" name="family-name" autocomplete="family-name" id="family-name-7885" spellcheck="false" type="text">
            <div class="fr-messages-group" id="family-name-7885-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7892">
            <label class="fr-label" for="given-7890">
                Prénom
            </label>
            <input class="fr-input" aria-describedby="given-7890-messages" name="given-name" autocomplete="given-name" id="given-7890" spellcheck="false" type="text">
            <div class="fr-messages-group" id="given-7890-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="firstname-disabled-7883-messages" aria-live="polite">
    </div>
</fieldset>
```

### Avec prénom désactivé

```html
<fieldset class="fr-fieldset" id="firstname-disabled-7906" aria-labelledby="firstname-disabled-7906-legend firstname-disabled-7906-messages">
    <legend class="fr-sr-only" id="firstname-disabled-7906-legend">
        Nom
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7916">
            <label class="fr-label" for="family-name-7908">
                Nom
            </label>
            <input class="fr-input" aria-describedby="family-name-7908-messages" name="family-name" autocomplete="family-name" id="family-name-7908" spellcheck="false" type="text">
            <div class="fr-messages-group" id="family-name-7908-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <fieldset class="fr-mb-n4v fr-fieldset" id="firstname-fieldset-7914" disabled aria-labelledby="firstname-fieldset-7914-legend firstname-fieldset-7914-messages">
            <legend class="fr-sr-only" id="firstname-fieldset-7914-legend">
                Prénom
            </legend>
            <div class="fr-fieldset__element">
                <div class="fr-input-group" id="input-group-7917">
                    <label class="fr-label" for="given-7913">
                        Prénom
                    </label>
                    <input class="fr-input" aria-describedby="given-7913-messages" name="given-name" autocomplete="given-name" id="given-7913" spellcheck="false" type="text">
                    <div class="fr-messages-group" id="given-7913-messages" aria-live="polite">
                    </div>
                </div>
            </div>
            <div class="fr-messages-group" id="firstname-fieldset-7914-messages" aria-live="polite">
            </div>
        </fieldset>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group fr-checkbox-group--sm">
            <input onclick="toggleDisabled(this, 'firstname-fieldset-7914')" checked name="firstname-disabled" id="disabler-7915" type="checkbox" aria-describedby="disabler-7915-messages">
            <label class="fr-label" for="disabler-7915">
                Je n'ai pas de prénom
            </label>
            <div class="fr-messages-group" id="disabler-7915-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="firstname-disabled-7906-messages" aria-live="polite">
    </div>
</fieldset>
```

### Avec nom d'usage

```html
<fieldset class="fr-fieldset" id="married-name-7930" aria-labelledby="married-name-7930-legend married-name-7930-messages">
    <legend class="fr-sr-only" id="married-name-7930-legend">
        Nom
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7938">
            <label class="fr-label" for="family-name-7932">
                Nom
            </label>
            <input class="fr-input" aria-describedby="family-name-7932-messages" name="family-name" autocomplete="family-name" id="family-name-7932" spellcheck="false" type="text">
            <div class="fr-messages-group" id="family-name-7932-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7939">
            <label class="fr-label" for="married-7935">
                Nom d'usage
                <span class="fr-hint-text">Indication : ancien nom…</span>
            </label>
            <input class="fr-input" aria-describedby="married-7935-messages" name="married-name" autocomplete="family-name" id="married-7935" spellcheck="false" type="text">
            <div class="fr-messages-group" id="married-7935-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7940">
            <label class="fr-label" for="given-7937">
                Prénom
            </label>
            <input class="fr-input" aria-describedby="given-7937-messages" name="given-name" autocomplete="given-name" id="given-7937" spellcheck="false" type="text">
            <div class="fr-messages-group" id="given-7937-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="married-name-7930-messages" aria-live="polite">
    </div>
</fieldset>
```

### Avec nom d'usage + prénom désactivé

```html
<fieldset class="fr-fieldset" id="married-and-firstname-disabled-7955" aria-labelledby="married-and-firstname-disabled-7955-legend married-and-firstname-disabled-7955-messages">
    <legend class="fr-sr-only" id="married-and-firstname-disabled-7955-legend">
        Nom
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7965">
            <label class="fr-label" for="family-name-7957">
                Nom
            </label>
            <input class="fr-input" aria-describedby="family-name-7957-messages" name="family-name" autocomplete="family-name" id="family-name-7957" spellcheck="false" type="text">
            <div class="fr-messages-group" id="family-name-7957-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7966">
            <label class="fr-label" for="married-7960">
                Nom d'usage
                <span class="fr-hint-text">Indication : ancien nom…</span>
            </label>
            <input class="fr-input" aria-describedby="married-7960-messages" name="married-name" autocomplete="family-name" id="married-7960" spellcheck="false" type="text">
            <div class="fr-messages-group" id="married-7960-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <fieldset class="fr-mb-n4v fr-fieldset" id="firstname-fieldset-7963" disabled aria-labelledby="firstname-fieldset-7963-legend firstname-fieldset-7963-messages">
            <legend class="fr-sr-only" id="firstname-fieldset-7963-legend">
                Prénom
            </legend>
            <div class="fr-fieldset__element">
                <div class="fr-input-group" id="input-group-7967">
                    <label class="fr-label" for="given-7962">
                        Prénom
                    </label>
                    <input class="fr-input" aria-describedby="given-7962-messages" name="given-name" autocomplete="given-name" id="given-7962" spellcheck="false" type="text">
                    <div class="fr-messages-group" id="given-7962-messages" aria-live="polite">
                    </div>
                </div>
            </div>
            <div class="fr-messages-group" id="firstname-fieldset-7963-messages" aria-live="polite">
            </div>
        </fieldset>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group fr-checkbox-group--sm">
            <input onclick="toggleDisabled(this, 'firstname-fieldset-7963')" checked name="firstname-disabled" id="disabler-7964" type="checkbox" aria-describedby="disabler-7964-messages">
            <label class="fr-label" for="disabler-7964">
                Je n'ai pas de prénom
            </label>
            <div class="fr-messages-group" id="disabler-7964-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="married-and-firstname-disabled-7955-messages" aria-live="polite">
    </div>
</fieldset>
```

### Avec bouton

```html
<fieldset class="fr-fieldset" id="button-7981" aria-labelledby="button-7981-legend button-7981-messages">
    <legend class="fr-sr-only" id="button-7981-legend">
        Nom
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-7991">
            <label class="fr-label" for="family-name-7983">
                Nom
            </label>
            <input class="fr-input" aria-describedby="family-name-7983-messages" name="family-name" autocomplete="family-name" id="family-name-7983" spellcheck="false" type="text">
            <div class="fr-messages-group" id="family-name-7983-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <fieldset class="fr-mb-n4v fr-fieldset" id="firstname-fieldset-7989" aria-labelledby="firstname-fieldset-7989-legend firstname-fieldset-7989-messages">
            <legend class="fr-sr-only" id="firstname-fieldset-7989-legend">
                Prénom
            </legend>
            <div class="fr-fieldset__element">
                <div class="fr-input-group" id="input-group-7992">
                    <label class="fr-label" for="given-7988">
                        Prénom
                    </label>
                    <input class="fr-input" aria-describedby="given-7988-messages" name="given-name" autocomplete="given-name" id="given-7988" spellcheck="false" type="text">
                    <div class="fr-messages-group" id="given-7988-messages" aria-live="polite">
                    </div>
                </div>
            </div>
            <div class="fr-fieldset__element">
                <button onclick="addFirstname(this, 'given-7988')" type="button" class="fr-btn fr-btn--sm fr-icon-add-line fr-btn--icon-left fr-btn--secondary">Ajouter un prénom</button>
            </div>
            <div class="fr-messages-group" id="firstname-fieldset-7989-messages" aria-live="polite">
            </div>
        </fieldset>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group fr-checkbox-group--sm">
            <input onclick="toggleDisabled(this, 'firstname-fieldset-7989')" name="firstname-disabled" id="disabler-7990" type="checkbox" aria-describedby="disabler-7990-messages">
            <label class="fr-label" for="disabler-7990">
                Je n'ai pas de prénom
            </label>
            <div class="fr-messages-group" id="disabler-7990-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="button-7981-messages" aria-live="polite">
    </div>
</fieldset>
```

### Avec bouton + prénom désactivé

```html
<fieldset class="fr-fieldset" id="button-and-firstname-disabled-8006" aria-labelledby="button-and-firstname-disabled-8006-legend button-and-firstname-disabled-8006-messages">
    <legend class="fr-sr-only" id="button-and-firstname-disabled-8006-legend">
        Nom
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-8016">
            <label class="fr-label" for="family-name-8008">
                Nom
            </label>
            <input class="fr-input" aria-describedby="family-name-8008-messages" name="family-name" autocomplete="family-name" id="family-name-8008" spellcheck="false" type="text">
            <div class="fr-messages-group" id="family-name-8008-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <fieldset class="fr-mb-n4v fr-fieldset" id="firstname-fieldset-8014" disabled aria-labelledby="firstname-fieldset-8014-legend firstname-fieldset-8014-messages">
            <legend class="fr-sr-only" id="firstname-fieldset-8014-legend">
                Prénom
            </legend>
            <div class="fr-fieldset__element">
                <div class="fr-input-group" id="input-group-8017">
                    <label class="fr-label" for="given-8013">
                        Prénom
                    </label>
                    <input class="fr-input" aria-describedby="given-8013-messages" name="given-name" autocomplete="given-name" id="given-8013" spellcheck="false" type="text">
                    <div class="fr-messages-group" id="given-8013-messages" aria-live="polite">
                    </div>
                </div>
            </div>
            <div class="fr-fieldset__element">
                <button onclick="addFirstname(this, 'given-8013')" type="button" class="fr-btn fr-btn--sm fr-icon-add-line fr-btn--icon-left fr-btn--secondary">Ajouter un prénom</button>
            </div>
            <div class="fr-messages-group" id="firstname-fieldset-8014-messages" aria-live="polite">
            </div>
        </fieldset>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group fr-checkbox-group--sm">
            <input onclick="toggleDisabled(this, 'firstname-fieldset-8014')" checked name="firstname-disabled" id="disabler-8015" type="checkbox" aria-describedby="disabler-8015-messages">
            <label class="fr-label" for="disabler-8015">
                Je n'ai pas de prénom
            </label>
            <div class="fr-messages-group" id="disabler-8015-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="button-and-firstname-disabled-8006-messages" aria-live="polite">
    </div>
</fieldset>
```

## Demande d’un nom et d’un prénom à l’international

### Défaut

```html
<fieldset class="fr-fieldset" id="name-international-8031" aria-labelledby="name-international-8031-legend name-international-8031-messages">
    <legend class="fr-sr-only" id="name-international-8031-legend">
        Nom
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-select-group">
            <label class="fr-label" for="country-8032">
                Pays
            </label>
            <select class="fr-select" aria-describedby="country-8032-messages" id="country-8032" name="country">
                <option value="" selected disabled>Sélectionner une option</option>
                <option value="FR">France</option>
                <option value="DE">Allemagne</option>
                <option value="IT">Italie</option>
                <option value="ES">Espagne</option>
                <option value="GB">Royaume-Uni</option>
            </select>
            <div class="fr-messages-group" id="country-8032-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-8041">
            <label class="fr-label" for="family-name-8033">
                Nom
            </label>
            <input class="fr-input" aria-describedby="family-name-8033-messages" name="family-name" autocomplete="family-name" id="family-name-8033" spellcheck="false" type="text">
            <div class="fr-messages-group" id="family-name-8033-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <fieldset class="fr-mb-n4v fr-fieldset" id="firstname-fieldset-8039" aria-labelledby="firstname-fieldset-8039-legend firstname-fieldset-8039-messages">
            <legend class="fr-sr-only" id="firstname-fieldset-8039-legend">
                Prénom
            </legend>
            <div class="fr-fieldset__element">
                <div class="fr-input-group" id="input-group-8042">
                    <label class="fr-label" for="given-8038">
                        Prénom
                    </label>
                    <input class="fr-input" aria-describedby="given-8038-messages" name="given-name" autocomplete="given-name" id="given-8038" spellcheck="false" type="text">
                    <div class="fr-messages-group" id="given-8038-messages" aria-live="polite">
                    </div>
                </div>
            </div>
            <div class="fr-messages-group" id="firstname-fieldset-8039-messages" aria-live="polite">
            </div>
        </fieldset>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group fr-checkbox-group--sm">
            <input onclick="toggleDisabled(this, 'firstname-fieldset-8039')" name="firstname-disabled" id="disabler-8040" type="checkbox" aria-describedby="disabler-8040-messages">
            <label class="fr-label" for="disabler-8040">
                Je n'ai pas de prénom
            </label>
            <div class="fr-messages-group" id="disabler-8040-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="name-international-8031-messages" aria-live="polite">
    </div>
</fieldset>
```

### Avec prénom désactivé

```html
<fieldset class="fr-fieldset" id="name-international-8056" aria-labelledby="name-international-8056-legend name-international-8056-messages">
    <legend class="fr-sr-only" id="name-international-8056-legend">
        Nom
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-select-group">
            <label class="fr-label" for="country-8057">
                Pays
            </label>
            <select class="fr-select" aria-describedby="country-8057-messages" id="country-8057" name="country">
                <option value="" selected disabled>Sélectionner une option</option>
                <option value="FR">France</option>
                <option value="DE">Allemagne</option>
                <option value="IT">Italie</option>
                <option value="ES">Espagne</option>
                <option value="GB">Royaume-Uni</option>
            </select>
            <div class="fr-messages-group" id="country-8057-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-8066">
            <label class="fr-label" for="family-name-8058">
                Nom
            </label>
            <input class="fr-input" aria-describedby="family-name-8058-messages" name="family-name" autocomplete="family-name" id="family-name-8058" spellcheck="false" type="text">
            <div class="fr-messages-group" id="family-name-8058-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <fieldset class="fr-mb-n4v fr-fieldset" id="firstname-fieldset-8064" disabled aria-labelledby="firstname-fieldset-8064-legend firstname-fieldset-8064-messages">
            <legend class="fr-sr-only" id="firstname-fieldset-8064-legend">
                Prénom
            </legend>
            <div class="fr-fieldset__element">
                <div class="fr-input-group" id="input-group-8067">
                    <label class="fr-label" for="given-8063">
                        Prénom
                    </label>
                    <input class="fr-input" aria-describedby="given-8063-messages" name="given-name" autocomplete="given-name" id="given-8063" spellcheck="false" type="text">
                    <div class="fr-messages-group" id="given-8063-messages" aria-live="polite">
                    </div>
                </div>
            </div>
            <div class="fr-messages-group" id="firstname-fieldset-8064-messages" aria-live="polite">
            </div>
        </fieldset>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group fr-checkbox-group--sm">
            <input onclick="toggleDisabled(this, 'firstname-fieldset-8064')" checked name="firstname-disabled" id="disabler-8065" type="checkbox" aria-describedby="disabler-8065-messages">
            <label class="fr-label" for="disabler-8065">
                Je n'ai pas de prénom
            </label>
            <div class="fr-messages-group" id="disabler-8065-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="name-international-8056-messages" aria-live="polite">
    </div>
</fieldset>
```
