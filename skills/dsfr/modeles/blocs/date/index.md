# Date unique

> Bloc pour la saisie d'une date unique dans un formulaire

Voir aussi : [Exemples](exemples.md)

Le bloc fonctionnel de "demande de date unique" permet de demander à l'utilisateur une date unique dans sa vie ou celle d'un proche (date de naissance, de mariage, de décès, de permis de conduire). Il est à utiliser dans le cadre d'un formulaire (inscription, démarche...)

## Structure du bloc

Le bloc fonctionnel est composé de :

- Label général ("Date de naissance") - obligatoire
- Label unique par sous-champ ("Jour", "Mois", "Année") - obligatoire
- Exemple en hint-text pour chaque champ "Exemple : 12" - obligatoire
- Placeholder avec le format attendu - optionnel

<div class="dsfr-doc-preview">
<fieldset class="fr-fieldset" id="date-default-1578-fieldset" role="group" aria-labelledby="date-default-1578-fieldset-legend date-default-1578-fieldset-messages">
    <legend class="fr-fieldset__legend" id="date-default-1578-fieldset-legend">
        Date de naissance
        <span class="fr-hint-text">Texte de description additionnel</span>
    </legend>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--number">
        <div class="fr-input-group">
            <label class="fr-label" for="date-default-1578-bday-day">
                Jour
                <span class="fr-hint-text">Exemple : 14</span>
            </label>
            <input class="fr-input" name="day" id="date-default-1578-bday-day" type="text">
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--number">
        <div class="fr-input-group">
            <label class="fr-label" for="date-default-1578-bday-month">
                Mois
                <span class="fr-hint-text">Exemple : 12</span>
            </label>
            <input class="fr-input" name="month" id="date-default-1578-bday-month" type="text">
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--inline-grow fr-fieldset__element--year">
        <div class="fr-input-group">
            <label class="fr-label" for="date-default-1578-bday-year">
                Année
                <span class="fr-hint-text">Exemple : 1984</span>
            </label>
            <input class="fr-input" name="year" id="date-default-1578-bday-year" type="text">
        </div>
    </div>
    <div class="fr-messages-group" id="date-default-1578-fieldset-messages" aria-live="polite">
    </div>
</fieldset>
</div>

**Extrait de code**

```html
<fieldset class="fr-fieldset" id="date-default-1578-fieldset" role="group" aria-labelledby="date-default-1578-fieldset-legend date-default-1578-fieldset-messages">
    <legend class="fr-fieldset__legend" id="date-default-1578-fieldset-legend">
        Date de naissance
        <span class="fr-hint-text">Texte de description additionnel</span>
    </legend>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--number">
        <div class="fr-input-group">
            <label class="fr-label" for="date-default-1578-bday-day">
                Jour
                <span class="fr-hint-text">Exemple : 14</span>
            </label>
            <input class="fr-input" name="day" id="date-default-1578-bday-day" type="text">
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--number">
        <div class="fr-input-group">
            <label class="fr-label" for="date-default-1578-bday-month">
                Mois
                <span class="fr-hint-text">Exemple : 12</span>
            </label>
            <input class="fr-input" name="month" id="date-default-1578-bday-month" type="text">
        </div>
    </div>
    <div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--inline-grow fr-fieldset__element--year">
        <div class="fr-input-group">
            <label class="fr-label" for="date-default-1578-bday-year">
                Année
                <span class="fr-hint-text">Exemple : 1984</span>
            </label>
            <input class="fr-input" name="year" id="date-default-1578-bday-year" type="text">
        </div>
    </div>
    <div class="fr-messages-group" id="date-default-1578-fieldset-messages" aria-live="polite">
    </div>
</fieldset>
```

## Bonnes pratiques

- Préciser le format attendu dans la description de chaque champ de saisie
- Les messages d'erreurs/succès spécifiques à chaque champs (ex : jour invalide) doivent être liés indépendamment via un attribut `aria-describedby` sur chaque `input`. Si l'erreur est général (ex : date invalide), la liaison se fait au niveau du `fieldset`.

## Accessibilité

- [Suivre les recommandations d'accessibilité d'un champ de saisie](../../../composants/input/index.md)
- [On peut aussi utiliser un champ unique de type="date"](../../../composants/input/index.md)
