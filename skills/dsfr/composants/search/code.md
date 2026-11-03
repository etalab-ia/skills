# Barre de recherche : Code

## HTML

### Structure du composant

Le composant **Barre de recherche** est un système de navigation qui permet à l'utilisateur d’accéder rapidement à un contenu en lançant une recherche sur un mot clé ou une expression.
Le composant doit être utilisé dans un formulaire `<form>`, pour permettre un fonctionnement sans JS.

Sa structure est la suivante :

- Le conteneur de la barre de recherche doit être un élément HTML `<div>` avec le rôle `search` défini par la classe `fr-search-bar`.
- Le champ de recherche est un élément HTML `<input>` de type `search` défini par la classe `fr-input`.
- Le champ de recherche doit être associée à un libellé `<label>` avec la classe `fr-label`.
- Le bouton de recherche est un élément HTML `<button>` défini par la classe `fr-btn` et dispose d'un attribut `title` indiquant son action. Son type doit être défini à `submit` pour soumettre le formulaire au click ou avec la touche "entrée".
- Un message d'erreur ou de succès peut être associé au champ de recherche en utilisant un élément HTML `<div>` avec la classe `fr-messages-group` dans lequel on peut ajouter un message : un élément `<p>` avec la classe `fr-message`, et un <span lang="en">modifier</span> `fr-message--error` ou `fr-message--valid`.
  - Son attribut`id` doit être associé à l'attribut `aria-describedby` du champ de recherche.
  - Ce bloc peut être placé vide et être rempli dynamiquement, auquel cas il doit être annoncé à l'utilisateur en utilisant l'attribut `aria-live="polite"`.

**Exemple de structure HTML**

```html
<div class="fr-search-bar" role="search">
    <label class="fr-label" for="search-input">
        Rechercher
    </label>
    <input class="fr-input" aria-describedby="search-input-messages" placeholder="Rechercher" id="search-input" type="search">
    <div class="fr-messages-group" id="search-input-messages" aria-live="polite">
    </div>
    <button title="Rechercher" type="submit" class="fr-btn">Rechercher</button>
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
| Input      | Oui         |
| Button     | Oui         |
| Search     | Oui         |

**Exemple d'imports CSS**

```html
<link href="dist/core/core.min.css" rel="stylesheet">
<link href="dist/component/input/input.min.css" rel="stylesheet">
<link href="dist/component/button/button.min.css" rel="stylesheet">
<link href="dist/component/search/search.min.css" rel="stylesheet">
```

### Variante de taille

La barre de recherche est disponible en deux variantes de tailles pour s'adapter à différents contextes d'utilisation.
Pour appliquer une variante de taille, ajoutez une des classes suivantes à l'élément `<div class="fr-search-bar">` :

- En taille MD : par défaut.
- En taille LG : définie par la classe `fr-search-bar--lg`.

**Exemple de variante de taille**

```html
<div class="fr-search-bar fr-search-bar--lg" role="search">
  <!-- Contenu de la barre de recherche -->
</div>
```

### Variante avec libellé

Par défaut, le libellé du champ de recherche est positionné hors écran. Pour rendre le libellé visible, ajoutez la classe `fr-search-bar--labelled` à l'élément `<div class="fr-search-bar">`.
Ne pas utiliser cette variante dans le cas d'une recherche globale dans la page (dans le header), car le libellé est déjà présent dans le bouton de recherche.

**Exemple de variante avec libellé**

```html
<div class="fr-search-bar fr-search-bar--labelled" role="search">
  <!-- Contenu de la barre de recherche -->
</div>
```

---

## JavaScript

Le composant Barre de recherche **ne nécessite pas l'utilisation de JavaScript** pour son fonctionnement de base.

---

## Note de version

[Voir les évolutions sur github](https://github.com/GouvernementFR/dsfr/pulls?q=is%3Apr+is%3Aclosed+is%3Amerged+search+)
