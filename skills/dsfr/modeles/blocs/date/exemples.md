# Date unique : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Défaut

```html
<fieldset class="fr-fieldset" id="date-7822" aria-labelledby="date-7822-legend date-7822-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="date-7822-legend">
        Date de naissance
        <span class="fr-hint-text">Indication : texte de description additionnel</span>
    </legend>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--number">
        <div class="fr-input-group" id="input-group-7823">
            <label class="fr-label" for="date-7822-bday-day">
                Jour
                <span class="fr-hint-text">Exemple : 14</span>
            </label>
            <input class="fr-input" name="day" autocomplete="bday-day" id="date-7822-bday-day" type="text">
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--number">
        <div class="fr-input-group" id="input-group-7824">
            <label class="fr-label" for="date-7822-bday-month">
                Mois
                <span class="fr-hint-text">Exemple : 12</span>
            </label>
            <input class="fr-input" name="month" autocomplete="bday-month" id="date-7822-bday-month" type="text">
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--inline-grow fr-fieldset__element--year">
        <div class="fr-input-group" id="input-group-7825">
            <label class="fr-label" for="date-7822-bday-year">
                Année
                <span class="fr-hint-text">Exemple : 1984</span>
            </label>
            <input class="fr-input" name="year" autocomplete="bday-year" id="date-7822-bday-year" type="text">
        </div>
    </div>
    <div class="fr-messages-group" id="date-7822-messages" aria-live="polite">
    </div>
</fieldset>
```

### Erreur unitaire

```html
<fieldset class="fr-fieldset fr-fieldset--error" id="date-error-7831" role="group" aria-labelledby="date-error-7831-legend date-error-7831-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="date-error-7831-legend">
        Date de naissance
        <span class="fr-hint-text">Indication : texte de description additionnel</span>
    </legend>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--number">
        <div class="fr-input-group" id="input-group-7832">
            <label class="fr-label" for="date-error-7831-bday-day">
                Jour
                <span class="fr-hint-text">Exemple : 14</span>
            </label>
            <input class="fr-input" name="day" value="00" autocomplete="bday-day" id="date-error-7831-bday-day" type="text">
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--number">
        <div class="fr-input-group" id="input-group-7833">
            <label class="fr-label" for="date-error-7831-bday-month">
                Mois
                <span class="fr-hint-text">Exemple : 12</span>
            </label>
            <input class="fr-input" name="month" value="13" autocomplete="bday-month" id="date-error-7831-bday-month" type="text">
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--inline-grow fr-fieldset__element--year">
        <div class="fr-input-group" id="input-group-7834">
            <label class="fr-label" for="date-error-7831-bday-year">
                Année
                <span class="fr-hint-text">Exemple : 1984</span>
            </label>
            <input class="fr-input" name="year" value="1995e" autocomplete="bday-year" id="date-error-7831-bday-year" type="text">
        </div>
    </div>
    <div class="fr-messages-group" id="date-error-7831-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="date-error-7831-message-error-1">Le jour est invalide</p>
        <p class="fr-message fr-message--error" id="date-error-7831-message-error-2">Le mois est invalide</p>
        <p class="fr-message fr-message--error" id="date-error-7831-message-error-3">L’année est invalide</p>
    </div>
</fieldset>
```

### Erreur globale

```html
<fieldset class="fr-fieldset fr-fieldset--error" id="date-error-7840" role="group" aria-labelledby="date-error-7840-legend date-error-7840-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="date-error-7840-legend">
        Date de naissance
        <span class="fr-hint-text">Indication : texte de description additionnel</span>
    </legend>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--number">
        <div class="fr-input-group" id="input-group-7841">
            <label class="fr-label" for="date-error-7840-bday-day">
                Jour
                <span class="fr-hint-text">Exemple : 14</span>
            </label>
            <input class="fr-input" name="day" value="03" autocomplete="bday-day" id="date-error-7840-bday-day" type="text">
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--number">
        <div class="fr-input-group" id="input-group-7842">
            <label class="fr-label" for="date-error-7840-bday-month">
                Mois
                <span class="fr-hint-text">Exemple : 12</span>
            </label>
            <input class="fr-input" name="month" value="03" autocomplete="bday-month" id="date-error-7840-bday-month" type="text">
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--inline-grow fr-fieldset__element--year">
        <div class="fr-input-group" id="input-group-7843">
            <label class="fr-label" for="date-error-7840-bday-year">
                Année
                <span class="fr-hint-text">Exemple : 1984</span>
            </label>
            <input class="fr-input" name="year" value="2525" autocomplete="bday-year" id="date-error-7840-bday-year" type="text">
        </div>
    </div>
    <div class="fr-messages-group" id="date-error-7840-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="date-error-7840-message-error">La date est postérieure à aujourd’hui</p>
    </div>
</fieldset>
```
