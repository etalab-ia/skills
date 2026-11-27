# Indicateur d’étapes : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

## Informations générales

### Exemple d'indicateur d'étape 1 sur 3

```html
<div class="fr-stepper">
    <h2 class="fr-stepper__title">
        Titre de l’étape en cours
        <span class="fr-stepper__state">Étape 1 sur 3</span>
    </h2>
    <div class="fr-stepper__steps" data-fr-current-step="1" data-fr-steps="3"></div>
    <p class="fr-stepper__details">
        <span class="fr-text--bold">Étape suivante :</span> Titre de la prochaine étape
    </p>
</div>
```

### Exemple d'indicateur d'étape 2 sur 8

```html
<div class="fr-stepper">
    <h2 class="fr-stepper__title">
        Titre de l’étape en cours
        <span class="fr-stepper__state">Étape 2 sur 8</span>
    </h2>
    <div class="fr-stepper__steps" data-fr-current-step="2" data-fr-steps="8"></div>
    <p class="fr-stepper__details">
        <span class="fr-text--bold">Étape suivante :</span> Titre de la prochaine étape
    </p>
</div>
```
