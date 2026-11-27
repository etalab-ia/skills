# Liens d'évitement : Code

## HTML

### Structure du composant

Le composant **Liens d'évitement** permet aux utilisateurs de naviguer rapidement vers les sections principales de la page.

**Toujours placé en haut de la page**, sa structure est la suivante :

- Le conteneur des liens d'évitement est un élément HTML `<div>` défini par la classe `fr-skiplinks`.
- Les liens d'évitement sont entourés par un élément HTML `<nav>` défini par la classe `fr-container` avec le rôle `navigation` et comportant un attribut `aria-label` dont la valeur est "Accès rapide".
- La liste des liens d'évitement est un élément HTML `<ul>` défini par la classe `fr-skiplinks__list`.
- Chaque élément `<li>` de la liste contient :
  - Un lien d'évitement, un élément HTML `<a>` défini par la classe `fr-link`.

> [!WARNING]
> Les liens d'évitement pointent vers des ancres (`#intitulé`), qui doivent être présentes dans la page.
> Par exemple, Le lien `<a class="fr-link" href="#content">Contenu</a>` ne peut fonctionner que si un élément avec l’id “content” est présent dans la page (comme `<main id=”content”>`), à l’endroit souhaité.

**Exemple de structure HTML**

```html
<div class="fr-skiplinks">
    <nav role="navigation" aria-label="Accès rapide" class="fr-container">
        <ul class="fr-skiplinks__list">
            <li>
                <a class="fr-link" href="#content">Contenu</a>
            </li>
            <li>
                <a class="fr-link" href="#header-navigation">Menu</a>
            </li>
            <li>
                <a class="fr-link" href="#header-search">Recherche</a>
            </li>
            <li>
                <a class="fr-link" href="#footer">Pied de page</a>
            </li>
        </ul>
    </nav>
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
| Link       | Oui         |
| Skiplink   | Oui         |

**Exemple d'imports CSS**

```html
<link href="dist/core/core.min.css" rel="stylesheet">
<link href="dist/component/link/link.min.css" rel="stylesheet">
<link href="dist/component/skiplink/skiplink.min.css" rel="stylesheet">
```

---

## JavaScript

Le composant Liens d'évitement **ne nécessite pas l'utilisation de JavaScript** pour son fonctionnement de base.

---

## Note de version

[Voir les évolutions sur github](https://github.com/GouvernementFR/dsfr/pulls?q=is%3Apr+is%3Aclosed+is%3Amerged+skiplink+)
