# Citation : Design

- Une icône (obligatoire, permettant d’informer l’usager qu’il s’agit de la mise en avant d’une citation)

- Le texte de la citation (obligatoire)

- Une image d’illustration (pour incarner la citation)

- Un séparateur (obligatoire)

- Une signature (pour préciser l’auteur de la citation)

- Une zone de détails (pour préciser l’origine du texte cité)

## Variations

**Citation sans illustration**

- Utiliser la citation sans illustration lorsqu’il n’est pas nécessaire ou possible d’incarner l’auteur de la citation.

En version mobile, le séparateur passe en dessous de la zone de détails.

**Citation avec illustration**

- Utiliser la citation avec illustration pour incarner l’auteur.

En version mobile, le comportement du séparateur est le même que pour la variation sans illustration. En complément, l’illustration est affichée en dessous du texte de la citation.

## Tailles

La largeur de la citation s’adapte à la taille de son conteneur.

Toutefois, il est recommandé de ne pas excéder une largeur de 8 colonnes, s’agissant d’un composant de mise en forme de contenu.

Le texte de la citation est quant à lui disponible en 3 tailles :

- MD pour medium - taille par défaut.

- LG pour large.

- XL pour extra large.

## États

La citation n’est sujette à aucun changement d’état.

## Personnalisation

Seule la couleur de l’icône de la citation est personnalisable. Elle peut utiliser l’ensemble des couleurs illustratives en indice $main uniquement.

**✅ À faire** : Personnaliser la couleur de l’icône de la citation parmi les couleurs illustratives, en indice $main.

**❌ À ne pas faire** : Ne pas utiliser une couleur illustrative d’un indice autre que $main.

**Titre du tableau**

|  Éléments | Indice thème clair | Indice thème sombre |
|:-----|:-----|:-----|
| **Icône `$artwork-minor-blue-france`** | Indice **main**<br> exemple : `$pink-tuile-main-556` | Indice **main**<br> exemple : `$pink-tuile-main-556` |

Par ailleurs, certains éléments sont optionnels - voir la structure du composant.
