# Sommaire : Code

## HTML

### Structure du composant

Le composant **Sommaire** est un élément interactif permettant de naviguer entre différentes sections de contenu.

Sa structure est la suivante :

- Le conteneur du sommaire est une balise `<div>` avec la classe `fr-summary` et le rôle `navigation`.
  - Le sommaire dispose d'un attribut `aria-labelledby` défini sur l'ID du titre du sommaire.
- Le titre du sommaire, obligatoire, est défini par la classe `fr-summary__title`. Son niveau de titre est personnalisable ou peut être un `<p>`.
- Les éléments de la liste d'ancre, obligatoire, sont contenus dans une balise `<ol>`.
  - Chaque élément de la liste `<li>` contient un lien `<a>` défini par la classe `fr-summary__link`.

**Exemple de structure HTML**

```html
<nav class="fr-summary" role="navigation" aria-labelledby="fr-summary-title">
    <h2 class="fr-summary__title" id="fr-summary-title">Sommaire</h2>
    <ol>
        <li>
            <a class="fr-summary__link" id="summary-link-1" href="#anchor-1">Libellé du lien 1</a>
            <ol>
                <li>
                    <a class="fr-summary__link" id="summary-link-1-1" href="#anchor-1.1">Libellé du lien 1.1</a>
                </li>
                <li>
                    <a class="fr-summary__link" id="summary-link-1-2" href="#anchor-1.2">Libellé du lien 1.2</a>
                </li>
                <li>
                    <a class="fr-summary__link" id="summary-link-1-3" href="#anchor-1.3">Libellé du lien 1.3</a>
                </li>
            </ol>
        </li>
        <li>
            <a class="fr-summary__link" id="summary-link-2" href="#anchor-2">Libellé du lien 2</a>
        </li>
    </ol>
</nav>
```

## CSS

### Installation du CSS

Pour fonctionner correctement le style CSS du composant et de ses dépendances doivent être importés. L'import doit se faire avant le contenu de la page dans la partie `<head>`, et de préférence avec les fichiers minifiés, car plus légers.

Il est possible d'importer les fichiers CSS avec un niveau de granularité adapté à vos besoins. Voir le découpage des fichiers CSS du DSFR dans la [documentation dédiée](../../demarrage.md).

**Dépendances CSS**

| Dépendance | Obligatoire |
|------------|-------------|
| Core       | Oui         |
| Summary    | Oui         |

**Exemple d'imports CSS**

```html
<link href="dist/core/core.min.css" rel="stylesheet">
<link href="dist/component/summary/summary.min.css" rel="stylesheet">
```

---

## JavaScript

Le composant Sommaire **ne nécessite pas l'utilisation de JavaScript** pour son fonctionnement de base.

---

## Note de version

[Voir les évolutions sur github](https://github.com/GouvernementFR/dsfr/pulls?q=is%3Apr+is%3Aclosed+is%3Amerged+summary+)
