# Fil d'Ariane : Code

## HTML

### Structure du composant

Le composant **Fil d’Ariane** permet aux utilisateurs de comprendre leur position dans la hiérarchie d’un site. Sa structure est conçue pour s’adapter aux écrans mobiles et comprend les éléments suivants :

1. Un conteneur principal sous la balise `<nav>` :
    - Doit avoir l’attribut `role="navigation"` pour indiquer sa fonction.
    - Utilise l’attribut `aria-label` pour fournir une description contextuelle, par exemple `aria-label="vous êtes ici :"`.
2. Un bouton d’affichage en mobile :
    - Représenté par un élément `<button>` avec la classe `fr-breadcrumb__button`.
    - Possède les attributs :
      - `aria-expanded` [true|false] pour indiquer si le fil d’Ariane est visible ou non.
      - `aria-controls` pour relier le bouton à l’élément `<div>` qui contient le fil d’Ariane.
3. Une zone de contenu avec le fil d’Ariane :
    - Représentée par une `<div>` avec la classe `fr-collapse`.
    - Doit inclure un identifiant unique (ex. `id="breadcrumb-1"`) pour être liée au bouton.
4. Une liste ordonnée `<ol>` avec la classe `fr-breadcrumb__list`, contenant les éléments du fil d’Ariane dont chaque segment est un élément `<li>` :
    - Les segments avec des liens utilisent une balise `<a>` avec la classe `fr-breadcrumb__link`.
    - Le segment actuel utilise `aria-current="page"` pour indiquer la page courante.

**Exemple de structure HTML**

```html
<nav role="navigation" class="fr-breadcrumb" aria-label="vous êtes ici :">
    <button class="fr-breadcrumb__button" aria-expanded="false" aria-controls="breadcrumb-1">
        Voir le fil d’Ariane
    </button>
    <div class="fr-collapse" id="breadcrumb-1">
        <ol class="fr-breadcrumb__list">
            <li>
                <a class="fr-breadcrumb__link" href="#/">Accueil</a>
            </li>
            <li>
                <a class="fr-breadcrumb__link" href="#/segment-1/">Segment 1</a>
            </li>
            <li>
                <a class="fr-breadcrumb__link" href="#/segment-1/segment-2/">Segment 2</a>
            </li>
            <li>
                <a class="fr-breadcrumb__link" aria-current="page">Page Actuelle</a>
            </li>
        </ol>
    </div>
</nav>
```

### Comportement en mobile

- En affichage mobile, seul le bouton avec la classe `fr-breadcrumb__button` est visible par défaut.
- Lors d’un clic sur ce bouton :
  - L’attribut `aria-expanded` passe de `false` à `true`.
  - La `<div>` avec la classe `fr-collapse` devient visible, affichant le contenu du fil d’Ariane.

---

## CSS

### Installation du CSS

Pour fonctionner correctement le style CSS du composant et de ses dépendances doivent être importés. L'import doit se faire avant le contenu de la page dans la partie `<head>`, et de préférence avec les fichiers minifiés, car plus légers.

Il est possible d'importer les fichiers CSS avec un niveau de granularité adapté à vos besoins. Voir le découpage des fichiers CSS du DSFR dans la [documentation dédiée](../../demarrage.md).

**Dépendances CSS**

| Dépendance | Obligatoire |
|------------|-------------|
| Core       | Oui         |
| Breadcrumb | Oui         |

**Exemple d'imports CSS**

```html
<link href="dist/core/core.min.css" rel="stylesheet">
<link href="dist/component/breadcrumb/breadcrumb.min.css" rel="stylesheet">
```

### Variantes de style

- **Affichage par défaut** : Le fil d’Ariane est masqué sur mobile, seul le bouton est visible.
- **Affichage étendu** : Lorsque l’attribut `aria-expanded` du bouton est à `true`, la classe `fr-collapse--expanded` est ajoutée au conteneur `<div>` pour le rendre visible.

---

## JavaScript

Pour fonctionner le composant fil d’Ariane nécessite l'utilisation de JavaScript.

### Installation du JavaScript

Chaque composant utilisant javascript possède un fichier Js spécifique et requiert le fichier Js du core.

Il est donc nécessaire d'importer ces fichiers à la fin de la page (avant `</body>`) :

```html
<script type="module" src="dist/core/core.module.min.js"></script>
<script type="module" src="dist/component/breadcrumb/breadcrumb.module.min.js"></script>
```

<small>NB: Il est aussi possible d'importer le Js global du DSFR `dsfr.module.min.js`</small>

Pour fonctionner sur Internet Explorer 11, un fichier legacy, en version nomodule ES5, peut aussi être importé :

```html
<script type="text/javascript" nomodule src="dist/legacy/legacy.nomodule.min.js"></script>
<script type="text/javascript" nomodule src="dist/core/core.nomodule.min.js"></script>
<script type="text/javascript" nomodule src="dist/component/breadcrumb/breadcrumb.nomodule.min.js"></script>
```

Une fois le JavaScript chargé, le composant fonctionne automatiquement.

### Instances

Sur le fil d’Ariane, les éléments suivants sont instanciés :

- Le bouton d'ouverture, via la classe `fr-breadcrumb__button`
- Le collapse, via la classe `fr-collapse`

Une fois chargé, le Js ajoute un attribut `data-fr-js-NOM_INSTANCE="true"` sur chacun des éléments instanciés

### API

Il est possible d'interagir avec les instances du composants en JavaScript via une API.

Cette API est disponible depuis la méthode `window.dsfr(instance)` du core.

Exemple :

```javascript
const elem = document.getElementById('ID_COLLAPSE');
dsfr(elem).collapse.disclose();
```

L'ensemble des propriétés et méthodes disponibles sont définies ci-après :

##### breadcrumb

**disclose**

| | |
|-------|----------------|
| **Description** | Ouvre le fil d’Ariane. |
| **Type** | function |
| **Arguments** | Aucun |
| **Retour** | Aucun |
| **Exemple** | dsfr(breadcrumb).breadcrumb.disclose() |

**node**

| | |
|-------|----------------|
| **Description** | Retourne le noeud HTML de l'élément `<nav>`. |
| **Type** | property |
| **Retour** | DOMElement |
| **Exemple** | dsfr(breadcrumb).breadcrumb.node |

##### collapseButton

**focus**

| | |
|-------|----------------|
| **Description** | Replace le focus sur le bouton. |
| **Type** | function |
| **Arguments** | Aucun |
| **Retour** | Aucun |
| **Exemple** | dsfr(breadcrumbButton).breadcrumbButton.focus() |

**node**

| | |
|-------|----------------|
| **Description** | Retourne le noeud HTML correspondant au bouton. |
| **Type** | property |
| **Retour** | DOMElement |
| **Exemple** | dsfr(breadcrumbButton).breadcrumbButton.node |

##### collapse

**conceal**

| | |
|:-----|:-----|
| **Description** | Ferme le collapse |
| **Type** | function |
| **Arguments** | none |
| **Retour** | none |
| **Exemple** | `dsfr(elem).collapse.conceal()` |

**disclose**

| | |
|:-----|:-----|
| **Description** | Ouvre le collapse |
| **Type** | function |
| **Arguments** | none |
| **Retour** | none |
| **Exemple** | `dsfr(elem).collapse.disclose()` |

**isDisclosed**

| | |
|:-----|:-----|
| **Description** | Retourne vrai si le collapse est ouvert |
| **Type** | property |
| **Retour** | Boolean |
| **Exemple** | `dsfr(elem).collapse.isDisclosed` |

**isEnabled**

| | |
|------|-----|
| **Description** | Défini si le fonctionnement du collapse est activé ou non |
| **Type** | property |
| **Retour** | Boolean |
| **Exemple** | `dsfr(elem).collapse.isEnabled = false` |

**buttons**

| | |
|:-----|:-----|
| **Description** | Retourne un tableau de boutons d'ouverture du collapse |
| **Type** | property |
| **Retour** | Array |
| **Exemple** | `dsfr(elem).collapse.buttons` |

**focus**

| | |
|:------|:-----|
| **Description** | Replace le focus sur le bouton du collapse |
| **Type** | function |
| **Arguments** | none |
| **Retour** | Boolean |
| **Exemple** | `dsfr(elem).collapse.focus()` |

**parent**

| | |
|:-----|:-----|
| **Description** | Retourne l'instance du dsfr parent, ici le breadcrumb |
| **Type** | property |
| **Retour** | object \| null |
| **Exemple** | `dsfr(elem).parent` |

**children**

| | |
|:-----|:-----|
| **Description** | Renvoie un tableau d'instances enfants |
| **Type** | property |
| **Retour** | Array |
| **Exemple** | `dsfr(elem).children` |

**node**

| | |
|------|-----|
| **Description** | Renvoie le noeud HTML de l'élément. |
| **Type** | property |
| **Retour** | DOMElement |
| **Exemple** | `dsfr(elem).collapse.node` |

### Événements

Le Système de Design fournit des événements personnalisés pour les actions uniques de la part de certains composants réactifs listés sur la page de l'[API Javascript](../../demarrage.md).

Sur le Fil d’Ariane, en mode mobile les événements suivants sont disponibles :

**événements**

| Événement | Action | Élément | Attribut |
|------|------|------|------|
| `dsfr.conceal` | Fermeture de l'élément | Collapse | `data-fr-js-collapse` |
| `dsfr.disclose` | Ouverture de l'élément | Collapse | `data-fr-js-collapse` |
| `dsfr.click` | Click sur le bouton d'ouverture | CollapseButton | `data-fr-js-collapse-button` |

---

## Note de version

[Voir les évolutions sur github](https://github.com/GouvernementFR/dsfr/pulls?q=is%3Apr+is%3Aclosed+is%3Amerged+breadcrumb+)
