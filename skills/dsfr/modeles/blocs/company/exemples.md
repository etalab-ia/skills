# Société : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Demande d'un numéro de SIRET

```html
<fieldset class="fr-fieldset" id="siret-8074" aria-labelledby="siret-8074-legend siret-8074-messages">
    <legend class="fr-sr-only" id="siret-8074-legend">
        SIRET de l'entreprise
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-8076">
            <label class="fr-label" for="siret-8075">
                Numéro de SIRET
            </label>
            <input class="fr-input" aria-describedby="siret-8075-messages" name="siret" id="siret-8075" type="text">
            <div class="fr-messages-group" id="siret-8075-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-mt-n1v fr-fieldset__element">
        <a title="Annuaire des entreprises - nouvelle fenêtre" target="_blank" rel="noopener" id="link-8077" href="https://annuaire-entreprises.data.gouv.fr/" class="fr-link">Annuaire des entreprises</a>
    </div>
    <div class="fr-messages-group" id="siret-8074-messages" aria-live="polite">
    </div>
</fieldset>
```

### Demande d’une adresse de siège social

Extrait complet : [exemples/demande-d-une-adresse-de-siege-social-1.html](exemples/demande-d-une-adresse-de-siege-social-1.html) (5 ko)

### Demande d’un type de société

```html
<fieldset class="fr-fieldset" id="structure-8114" aria-labelledby="structure-8114-legend structure-8114-messages">
    <legend class="fr-sr-only" id="structure-8114-legend">
        Type de société
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-select-group">
            <label class="fr-label" for="structure-8115">
                Type de société
            </label>
            <select class="fr-select" aria-describedby="structure-8115-messages" id="structure-8115" name="structure">
                <option value="" selected disabled>Sélectionner une option</option>
                <option value="EI">Entrepreneur individuel (EI)</option>
                <option value="EURL">Entreprise unipersonnelle à responsabilité limitée (EURL)</option>
                <option value="SARL">Société à responsabilité limitée (SARL)</option>
                <option value="SASU">Société par actions simplifiée unipersonnelle (SASU)</option>
                <option value="SAS">Société par actions simplifiée (SAS)</option>
                <option value="SA">Société anonyme (SA)</option>
                <option value="SNC">Société en nom collectif (SNC)</option>
                <option value="SCS">Société en commandite simple (SCS)</option>
                <option value="SCA">Société en commandite par actions (SCA)</option>
            </select>
            <div class="fr-messages-group" id="structure-8115-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="structure-8114-messages" aria-live="polite">
    </div>
</fieldset>
```

### Demande d’un représentant moral

```html
<fieldset class="fr-fieldset" id="representative-8130" aria-labelledby="representative-8130-legend representative-8130-messages">
    <legend class="fr-sr-only" id="representative-8130-legend">
        Représentant moral de l'entreprise
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-8139">
            <label class="fr-label" for="usual-8133">
                Nom d'usage
            </label>
            <input class="fr-input" aria-describedby="usual-8133-messages" name="usual-name" autocomplete="family-name" id="usual-8133" spellcheck="false" type="text">
            <div class="fr-messages-group" id="usual-8133-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-8140">
            <label class="fr-label" for="birth-8134">
                Nom de naissance
                <span class="fr-hint-text">Indication : nom de famille non rectifié après décision du tribunal.</span>
            </label>
            <input class="fr-input" aria-describedby="birth-8134-messages" name="birth-name" autocomplete="family-name" id="birth-8134" spellcheck="false" type="text">
            <div class="fr-messages-group" id="birth-8134-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-8141">
            <label class="fr-label" for="givens-8136">
                Prénom
            </label>
            <input class="fr-input" aria-describedby="givens-8136-messages" name="given-names" autocomplete="given-name" id="givens-8136" spellcheck="false" type="text">
            <div class="fr-messages-group" id="givens-8136-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group" id="input-group-8142">
            <label class="fr-label" for="representative-8138">
                Fonction dans la société
            </label>
            <input class="fr-input" aria-describedby="representative-8138-messages" name="position" autocomplete="organization-title" id="representative-8138" type="text">
            <div class="fr-messages-group" id="representative-8138-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="representative-8130-messages" aria-live="polite">
    </div>
</fieldset>
```
