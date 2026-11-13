# Badge : Code

## HTML

### Structure du composant

Le composant **Badge** est un élément visuel destiné à fournir des informations contextuelles ou des indicateurs d'état.
Sa structure est la suivante :

- Le Badge est un élément HTML `<p>` avec la classe `fr-badge`.
- Son contenu est textuel et doit être succinct (exemple : "Libellé badge").

**Exemple de structure HTML**

```html
<p class="fr-badge">Libellé badge</p>
```

### Groupe de badges

Lorsque plusieurs badges sont utilisés ensemble, ils doivent être regroupés dans un conteneur, de classe `fr-badges-group`, afin de maintenir une cohérence visuelle et fonctionnelle.

```html
<ul class="fr-badges-group">
  <li>
      <span class="fr-badge">Badge 1</span>
  </li>
  <li>
      <span class="fr-badge">Badge 2</span>
  </li>
</ul>
```

---

## CSS

### Installation du CSS

Pour fonctionner correctement le style CSS du composant et de ses dépendances doivent être importés. L'import doit se faire avant le contenu de la page dans la partie `<head>`, et de préférence avec les fichiers minifiés, car plus légers.

Il est possible d'importer les fichiers CSS avec un niveau de granularité adapté à vos besoins. Voir le découpage des fichiers CSS du DSFR dans la [documentation dédiée](../../demarrage.md).

**Dépendances CSS**

| Dépendance | Obligatoire | Remarque |
|------------|-------------|----------|
| Core       | Oui         |          |
| Badge      | Oui         |          |
| Utility    | Non         | Uniquement pour l'ajout d'icône |

**Exemple d'imports CSS**

```html
<link href="dist/core/core.min.css" rel="stylesheet">
<link href="dist/component/badge/badge.min.css" rel="stylesheet">
```

### Variantes systèmes

Les badges systèmes peuvent avoir des styles définis pour différents status. Pour appliquer une variante système, ajoutez une des classes suivantes à l'élément `<p class="fr-badge">` :

- `fr-badge--info` : Indique une information.
- `fr-badge--warning` : Indique un avertissement.
- `fr-badge--error` : Indique une erreur.
- `fr-badge--success` : Indique un succès.
- `fr-badge--new` : Indique une nouveauté

Les badges système sont liés à une icône, celle-ci n'est pas modifiable mais peut être retirée. Pour cela utilisez la classe : `fr-badge--no-icon`

**Exemples de badges systèmes**

```html
<p class="fr-badge fr-badge--info">Information</p>
<p class="fr-badge fr-badge--warning">Avertissement</p>
<p class="fr-badge fr-badge--error">Erreur</p>
<p class="fr-badge fr-badge--success">Succès</p>
<p class="fr-badge fr-badge--new">Nouveau</p>
```

### Variantes d'accentuation

Les badges sont disponibles dans toutes les couleurs d'accentuation via la classe : `fr-badge--NOM-COULEUR`.
Retrouver la liste des couleurs d'accentuation sur la [page couleurs](../../fondamentaux/color/index.md).

**Exemples de badges systèmes**

```html
<p class="fr-badge fr-badge--yellow-moutarde">intitulé</p>
<p class="fr-badge fr-badge--green-menthe">intitulé</p>
```

### Variantes de taille

Les badges peuvent être affichés dans deux tailles différentes. Par défaut, la taille standard est utilisée, mais il est possible d'ajouter la classe suivante pour ajuster la taille :

- `fr-badge--sm` : Petit badge.

**Exemples de tailles de badges**

```html
<p class="fr-badge fr-badge--sm">Petit badge</p>
<p class="fr-badge">Badge moyen</p>
```

---

## JavaScript

Le composant Badge **ne nécessite pas l'utilisation de JavaScript** pour son fonctionnement de base.

---

## Note de version

[Voir les évolutions sur github](https://github.com/GouvernementFR/dsfr/pulls?q=is%3Apr+is%3Aclosed+is%3Amerged+badge+)
