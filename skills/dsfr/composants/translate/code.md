# Sélecteur de langues : Code

## HTML

### Structure du composant

Le composant **Sélecteur de langue** permet de choisir la langue de l'interface.
Sa structure, reposant sur le modèle du composant **Navigation principale** est la suivante :

- Le sélecteur de langue est un élément HTML `<div>` défini par les classes `fr-translate` et `fr-nav`.
- Il doit contenir un élément HTML `<div>` défini par la classe `fr-nav__item`, contenant :
  - Un `<button>` de type "button".
    - Il est défini par les classes `fr-translate__btn`, `fr-btn` et `fr-btn--tertiary`.
    - Le libellé du bouton doit reprendre l'abréviation de la langue active (ex: "FR") ainsi que hors écran le libellé explicite de la langue active (ex: `<span class="fr-hidden-lg">&nbsp;- Français</span>`)
    - Le bouton dispose d'un attribut `title`, sa valeur doit être "Sélectionner une langue".
    - Le bouton dispose d'un attribut `aria-expanded`, sa valeur [true|false] défini si le collapse est ouvert ou fermé
    - Le bouton est lié au collapse via l'attribut `aria-controls`, sa valeur doit correspondre à l'attribut `id` du collapse.
  - Un bloc refermable, défini par les classes `fr-collapse`, `fr-translate__menu` et `fr-menu`, est une `<div>` placée après le bouton. Il s'agit d'un élément générique du core utilisé par d'autres composants tels que la navigation ou la transcription.
    - Il dispose d'un attribut `id` obligatoire, pour être lié au bouton d'ouverture.
    - Son contenu est composé d'une liste d'éléments `<ul>` définie par la classe `fr-menu__list` :
      - Chaque langue cible dans le menu est un élément `<li>`, contenant un lien `<a>` défini par les classes `fr-translate__language` et `fr-nav__link`.
      - Le libellé des liens est composé de l'abréviation de la langue et du libellé explicite de la langue (ex: "FR - Français").
      - Les liens disposent d'un attribut `hreflang` et un attribut `lang`, dont les valeurs spécifient la langue cible.
      - La langue active dispose d'un attribut `aria-current="true"`.

**Exemple de structure HTML**

```html
<div class="fr-translate fr-nav">
    <div class="fr-nav__item">
        <button aria-controls="translate-menu" aria-expanded="false" title="Sélectionner une langue" type="button" class="fr-translate__btn fr-btn fr-btn--tertiary">FR<span class="fr-hidden-lg">&nbsp;- Français</span>
        </button>
        <div class="fr-collapse fr-translate__menu fr-menu" id="translate-menu">
            <ul class="fr-menu__list">
                <li>
                    <a class="fr-translate__language fr-nav__link" hreflang="fr" lang="fr" href="/fr/" aria-current="true">FR - Français</a>
                </li>
                <li>
                    <a class="fr-translate__language fr-nav__link" hreflang="en" lang="en" href="/en/">EN - English</a>
                </li>
            </ul>
        </div>
    </div>
</div>
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
| Button     | Oui         |
| Navigation | Oui         |
| Translate  | Oui         |

**Exemple d'imports CSS**

```html
<link href="dist/core/core.min.css" rel="stylesheet">
<link href="dist/component/button/button.min.css" rel="stylesheet">
<link href="dist/component/navigation/navigation.min.css" rel="stylesheet">
<link href="dist/component/translate/translate.min.css" rel="stylesheet">
```

### Variantes de sélecteur de langue sans bordure

Le sélecteur de langue peut être utilisé avec un bouton sans bordure avec l'utilisation de la classe `fr-btn--tertiary-no-outline` sur le bouton.

**Exemples de sélecteur de langue sans bordure**

```html
<div class="fr-translate fr-nav">
    <div class="fr-nav__item">
        <button aria-controls="translate" aria-expanded="false" type="button" class="fr-translate__btn fr-btn fr-btn--tertiary-no-outline">FR<span class="fr-hidden-lg">&nbsp;- Français</span>
        </button>
        <!-- Liste des langues -->
    </div>
</div>
```

---

## JavaScript

Pour fonctionner le composant Sélecteur de langue nécessite l'utilisation de JavaScript.
Ses fonctionnalités sont disponibles dans le core et le composant [Navigation](../navigation/code.md).

Il est donc nécessaire d'importer ces fichiers js à la fin de la page (avant `</body>`) :

```html
<script type="module" src="dist/core/core.module.min.js"></script>
<script type="module" src="dist/component/navigation/navigation.module.min.js"></script>
```

<small>NB: Il est aussi possible d'importer le Js global du DSFR `dsfr.module.min.js`</small>

Pour fonctionner sur Internet Explorer 11, un fichier legacy, en version nomodule ES5, peut aussi être importé :

```html
<script type="text/javascript" nomodule src="dist/legacy/legacy.nomodule.min.js" ></script>
<script type="text/javascript" nomodule src="dist/core/core.nomodule.min.js"></script>
<script type="text/javascript" nomodule src="dist/component/navigation/navigation.nomodule.min.js"></script>
```

### Instances

Sur le sélecteur de langue, les éléments suivants sont instanciés :

- La navigation, via la classe : `fr-nav`
- L'element de navigation, via la classe : `fr-nav__item`
- Le bouton d'ouverture, via la classe `fr-translate__btn`
- Le collapse, via la classe `fr-collapse`

Une fois chargé, le Js ajoute un attribut `data-fr-js-NOM_INSTANCE="true"` sur chacun des éléments instanciés

### API

Il est possible d'interagir avec les instances du composants en JavaScript via une API.

Cette API est disponible depuis la méthode `window.dsfr(instance)` du core.

Exemple :

```js
const elem = document.getElementById('ID_COLLAPSE');
dsfr(elem).collapse.disclose();
```

L'ensemble des propriétés et méthodes disponibles sont définies ci-après :

#### navigation

**current**

| | |
|------|-----|
| **Description** | Retourne l'API du collapse ouvert. <br>_Si aucun collapse n'est ouvert, ou si plusieurs collapses sont ouverts, renvoie `null`._|
| **Type** | property |
| **Retour** | object \| null |
| **Exemple** | `dsfr(elem).navigation.current` |

**index**

| | |
|------|-----|
| **Description** | Retourne ou modifie l'index de l'accordéon courant. <br>_Si aucun collapse n'est ouvert, l'index vaut 0._ |
| **Type** | property |
| **Retour** | Number |
| **Exemple** | `dsfr(elem).navigation.index` <br> `dsfr(elem).navigation.index = -1` |

**isEnabled**

| | |
|------|-----|
| **Description** | Défini si le fonctionnement du sélecteur de langue est activé ou non |
| **Type** | property |
| **Retour** | Boolean |
| **Exemple** | `dsfr(elem).navigation.isEnabled = false` |

**hasFocus**

| | |
|------|-----|
| **Description** | Renvoie vrai si le focus est sur un des éléments du groupe. |
| **Type** | property |
| **Retour** | Boolean |
| **Exemple** | `dsfr(elem).navigation.hasFocus` |

#### navigationItem

**isEnabled**

| | |
|------|-----|
| **Description** | Défini si le fonctionnement de la navigation est activé ou non |
| **Type** | property |
| **Retour** | Boolean |
| **Exemple** | `dsfr(elem).navigationItem.isEnabled = false` |

#### collapseButton

**focus**

| | |
|:------|:-----|
| **Description** | Replace le focus sur le bouton |
| **Type** | function |
| **Arguments** | none |
| **Retour** | Boolean |
| **Exemple** | `dsfr(elem).collapseButton.focus()` |

**parent**

| | |
|:-----|:-----|
| **Description** | Retourne l'instance du dsfr parente, ici le sélecteur de langue |
| **Type** | property |
| **Retour** | object \| null |
| **Exemple** | `dsfr(elem).parent` |

**node**

| | |
|------|-----|
| **Description** | Renvoie le noeud HTML de l'élément. |
| **Type** | property |
| **Retour** | DOMElement |
| **Exemple** | `dsfr(elem).collapseButton.node` |

#### collapse

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
| **Description** | Défini si le fonctionnement du sélecteur de langue est activé ou non |
| **Type** | property |
| **Retour** | Boolean |
| **Exemple** | `dsfr(elem).collapse.isEnabled = false` |

**group**

| | |
|:-----|:-----|
| **Description** | Retourne l'API du groupe, ou null s'il n'y a pas de groupe |
| **Type** | property |
| **Retour** | object \| null |
| **Exemple** | `dsfr(elem).collapse.group` |

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
| **Description** | Retourne l'instance du dsfr parent, ici le sélecteur de langue |
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

---

## Note de version

[Voir les évolutions sur github](https://github.com/GouvernementFR/dsfr/pulls?q=is%3Apr+is%3Aclosed+is%3Amerged+translate)
