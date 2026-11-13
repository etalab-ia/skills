# Case à cocher : Code

## HTML

### Structure du composant

Le composant **Case à cocher**, ci-après nommée **Checkbox**, est un élément interactif permettant de sélectionner une ou plusieurs options. Sa structure est la suivante :

- La checkbox doit être **contenu** dans un élément HTML `<div>` défini par la classe `fr-checkbox-group`.
- La checkbox est un élément HTML `<input>` de type `checkbox` défini par la classe `fr-checkbox`.
- La checkbox doit être associée à un **label** `<label>` avec la classe `fr-label`.
- Une **description additionnelle** de l'option - optionnelle - peut être ajoutée dans le label, elle est définie par un élément `<span>` et la classe utilitaire `fr-hint-text`.
- Un **message** d'erreur ou de succès peut être associé à la checkbox en utilisant un élément `<div>` avec la classe `fr-messages-group` dans lequel on peut ajouter un message `fr-message`. Son attribut`id` doit être associé à l'attribut `aria-describedby` de la checkbox. Ce bloc peut être placé vide et être rempli dynamiquement, auquel cas il doit être annoncé à l'utilisateur en utilisant l'attribut `aria-live="polite"`.

**Exemple de structure HTML simple**

```html
<div class="fr-checkbox-group">
    <input id="checkbox" type="checkbox" aria-describedby="checkbox-messages">
    <label class="fr-label" for="checkbox">
        Libellé checkbox
        <span class="fr-hint-text">Description optionnelle</span>
    </label>
    <div class="fr-messages-group" id="checkbox-messages" aria-live="polite">
    </div>
</div>
```

### Groupe de checkboxes

Pour **regrouper plusieurs checkboxes liées**, utilisez un élément `<fieldset>` avec une légende `<legend>`. Cela permet de structurer les options de manière accessible.

- L'élément `<fieldset>` est défini par la classe `fr-fieldset`.
- La légende `<legend>` est définie par la classe `fr-fieldset__legend`. Par défaut une légende sera en gras car le fieldset est utilisé pour regroupé plusieurs champs ayant chacun un label. Dans le cas des checkboxes la légende est visuellement perçue comme le label du groupe de checkboxes. On ajoutera donc la classe `fr-fieldset__legend--regular` pour repasser la légende sur une graisse standard.
- Une description additionnelle pour la légende - optionnelle - peut être ajoutée dans la légende, elle est définie par un élément `<span>` et la classe utilitaire `fr-hint-text`.
- Chaque élément de checkbox est contenu dans un élément `<div>` défini par la classe `fr-fieldset__element`. Ces éléments peuvent être placés en ligne avec la classe `fr-fieldset__element--inline`.
- Comme pour chaque checkbox, le groupe de checkbox, représenté par un fieldset, peut contenir un message d'erreur/information/succès via un bloc `fr-messages-group`.

**Exemple de groupe de checkboxes**

**Déplier pour voir le code**

```html
<fieldset class="fr-fieldset" aria-labelledby="checkboxes-legend checkboxes-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkboxes-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkboxes-1" id="checkboxes-1" type="checkbox">
            <label class="fr-label" for="checkboxes-1">
                Libellé case à cocher
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input checked name="checkboxes-2" id="checkboxes-2" type="checkbox">
            <label class="fr-label" for="checkboxes-2">
                Libellé case à cocher
            </label>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
            <input name="checkboxes-3" id="checkboxes-3" type="checkbox">
            <label class="fr-label" for="checkboxes-3">
                Libellé case à cocher
            </label>
        </div>
    </div>
    <div class="fr-messages-group" id="checkboxes-messages" aria-live="polite">
    </div>
</fieldset>
```

---

## CSS

### Installation du CSS

Pour fonctionner correctement le style CSS du composant et de ses dépendances doivent être importés. L'import doit se faire avant le contenu de la page dans la partie `<head>`, et de préférence avec les fichiers minifiés, car plus légers.

Il est possible d'importer les fichiers CSS avec un niveau de granularité adapté à vos besoins. Voir le découpage des fichiers CSS du DSFR dans la [documentation dédiée](../../demarrage.md).

**Dépendances CSS**

| Dépendance | Obligatoire |
|------------|-------------|
| Core       | Oui         |
| Form       | Oui         |
| Checkbox   | Oui         |

**Exemple d'imports CSS**

```html
<link href="dist/core/core.min.css" rel="stylesheet">
<link href="dist/component/form/form.min.css" rel="stylesheet">
<link href="dist/component/checkbox/checkbox.min.css" rel="stylesheet">
```

### Variantes de tailles

La checkbox est disponible en deux variantes de tailles :

- En taille MD : par défaut.
- En taille SM : définie par la classe `fr-checkbox-group--sm`.

**Exemples de variantes de tailles**

```html
<div class="fr-checkbox-group fr-checkbox-group--sm">
    <input id="checkbox-sm" type="checkbox">
    <label class="fr-label" for="checkbox-sm">
        Libellé checkbox taille SM
    </label>
</div>
```

### Variantes d'états

La checkbox est disponible en plusieurs variantes d'états :

- La checkbox avec **erreur** : définie par la classe `fr-checkbox-group--error`.
- La checkbox avec **succès** : définie par la classe `fr-checkbox-group--valid`.
- La checkbox **désactivée** : définie par l'attribut `disabled` sur l'élément `<input>`.
- La checkbox **indéterminée** : définie par la propriété du DOM `indeterminate` fixée à `true` sur l'élément `<input>` via du code JavaScript.

Dans le cas d'utilisation d'un groupe de checkboxes, ces états sont définis sur le groupe (le fieldset), et non sur chaque checkbox.

- Groupe en **erreur** : définie par la classe `fr-fieldset--error`.
- Groupe en **succès** : définie par la classe `fr-fieldset--valid`.
- Groupe **désactivée** : définie par l'attribut `disabled` sur l'élément `<fieldset>`.

**Exemples de variantes d'états**

**Déplier pour voir le code**

**Erreur**

```html
<div class="fr-checkbox-group fr-checkbox-group--error">
    <input id="checkbox-error" type="checkbox" aria-describedby="checkbox-messages-error">
    <label class="fr-label" for="checkbox-error">
        Libellé checkbox avec erreur
    </label>
    <div class="fr-messages-group" id="checkbox-messages-error" aria-live="polite">
        <p class="fr-message fr-message--error">Texte d’erreur</p>
    </div>
</div>
```

**Succès**

```html
<div class="fr-checkbox-group fr-checkbox-group--valid">
    <input id="checkbox-valid" type="checkbox" aria-describedby="checkbox-messages-valid">
    <label class="fr-label" for="checkbox-valid">
        Libellé checkbox avec succès
    </label>
    <div class="fr-messages-group" id="checkbox-messages-valid" aria-live="polite">
        <p class="fr-message fr-message--valid">Texte de succès</p>
    </div>
</div>
```

**Désactivé**

```html
<div class="fr-checkbox-group">
    <input id="checkbox-disabled" type="checkbox" disabled>
    <label class="fr-label" for="checkbox-disabled">
        Libellé checkbox désactivée
    </label>
</div>
```

**Exemple de variante d'état au niveau du groupe**

**Déplier pour voir le code**

**Erreur**

```html
<fieldset class="fr-fieldset fr-fieldset--error" aria-labelledby="checkboxes-legend checkboxes-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkboxes-legend">
        Légende pour l’ensemble des éléments en erreur
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">(...)</div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">(...)</div>
    </div>
    <div class="fr-messages-group" id="checkboxes-messages" aria-live="polite">
        <p class="fr-message fr-message--error">Texte d’erreur globale</p>
    </div>
</fieldset>
```

**Succès**

```html
<fieldset class="fr-fieldset fr-fieldset--valid" aria-labelledby="checkboxes-legend checkboxes-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkboxes-legend">
        Légende pour l’ensemble des éléments en succès
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">(...)</div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">(...)</div>
    </div>
    <div class="fr-messages-group" id="checkboxes-messages" aria-live="polite">
        <p class="fr-message fr-message--error">Texte de succès global</p>
    </div>
</fieldset>
```

**Désactivé**

```html
<fieldset class="fr-fieldset" disabled aria-labelledby="checkboxes-legend checkboxes-messages">
    <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkboxes-legend">
        Légende pour l’ensemble des éléments déactivés
    </legend>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">(...)</div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">(...)</div>
    </div>
    <div class="fr-messages-group" id="checkboxes-messages" aria-live="polite">
    </div>
</fieldset>
```

---

## JavaScript

Le composant Case à cocher **ne nécessite pas l'utilisation de JavaScript** pour son fonctionnement de base.

Un script est disponible pour faire remonter les évènements de changement d'état des checkboxes, mais il n'est pas nécessaire pour le fonctionnement du composant.
Ce script est notamment utilisé pour gérer la selection des lignes d'un tableau.

---

## Note de version

[Voir les évolutions sur github](https://github.com/GouvernementFR/dsfr/pulls?q=is%3Apr+is%3Aclosed+is%3Amerged+checkbox+)
