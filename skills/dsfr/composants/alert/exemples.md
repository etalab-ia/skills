# Alerte : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

## Alerte statique

### Alerte par défaut

```html
<div id="alert-685" class="fr-alert">
    <h3 class="fr-alert__title">Titre</h3>
    <p>Description</p>
</div>
```

### Alerte succès

```html
<div id="alert-687" class="fr-alert fr-alert--success">
    <h3 class="fr-alert__title">Succès de l&#39;envoi</h3>
    <p>Description</p>
</div>
```

### Alerte erreur

```html
<div id="alert-689" class="fr-alert fr-alert--error">
    <h3 class="fr-alert__title">Erreur détectée dans le formulaire</h3>
    <p>Description</p>
</div>
```

### Alerte info

```html
<div id="alert-691" class="fr-alert fr-alert--info">
    <h3 class="fr-alert__title">Information Covid</h3>
    <p>Description</p>
</div>
```

### Alerte attention

```html
<div id="alert-693" class="fr-alert fr-alert--warning">
    <h3 class="fr-alert__title">Attention</h3>
    <p>Description</p>
</div>
```

### Alerte sans titre

```html
<div id="alert-695" class="fr-alert fr-alert--info">
    <p>Information : titre de l&#39;information</p>
</div>
```

### Alerte avec bouton fermer

```html
<div id="alert-698" class="fr-alert fr-alert--info">
    <h3 class="fr-alert__title">Information Covid</h3>
    <p>Cliquer sur la croix pour fermer l&#39;alerte</p>
    <button title="Masquer le message" onclick="const alert = this.parentNode; alert.parentNode.removeChild(alert)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>
```

### Alerte taille SM

```html
<div id="alert-700" class="fr-alert fr-alert--info fr-alert--sm">
    <h3 class="fr-alert__title">Titre</h3>
    <p>Description</p>
</div>
```

### Alerte taille SM sans titre

```html
<div id="alert-702" class="fr-alert fr-alert--info fr-alert--sm">
    <p>Information : titre de l&#39;information</p>
</div>
```

### Alerte taille SM refermable

```html
<div id="alert-705" class="fr-alert fr-alert--info fr-alert--sm">
    <p>Information : cliquer sur la croix pour fermer l&#39;alerte</p>
    <button title="Masquer le message" onclick="const alert = this.parentNode; alert.parentNode.removeChild(alert)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>
```

### Alerte icône personnalisée

```html
<div id="alert-707" class="fr-alert fr-icon-lock-fill">
    <h3 class="fr-alert__title">Titre</h3>
    <p>Description</p>
</div>
```

## Alerte dynamique

### Alerte ajoutée dynamiquement (type)

Ajouter l'attribut role="alert" lorsque les alertes sont ajoutées dynamiquement dans le DOM (en js après le chargement de la page)

```html
<div id="alert-710" role="alert" class="fr-alert fr-alert--error">
    <h3 class="fr-alert__title">Erreur détectée dans le formulaire</h3>
    <p>Cliquer sur la croix pour fermer l&#39;alerte</p>
    <button title="Masquer le message" onclick="const alert = this.parentNode; alert.parentNode.removeChild(alert)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>
```

## Dépréciation

### Alerte avec bouton fermer

Les exemples suivants sont dépréciés, ne pas utiliser comme référence Pour support des versions précédentes

```html
<div class="fr-alert fr-alert--info">
    <p class="fr-alert__title">Information Covid</p>
    <p>Cliquer sur la croix pour fermer l&#39;alerte</p>
    <button title="Masquer le message" onclick="const alert = this.parentNode; alert.parentNode.removeChild(alert)" id="link-715" class="fr-link--close fr-link">Masquer le message</button>
</div>
```
