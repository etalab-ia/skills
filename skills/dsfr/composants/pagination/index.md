# Pagination

> Navigation entre plusieurs pages d’une liste

Voir aussi : [Design](design.md) · [Code](code.md) · [Accessibilité](accessibilite.md) · [Exemples](exemples.md)

La pagination est un système de navigation qui permet à l’usager de naviguer entre les différentes pages d’une liste d’éléments.

## Quand utiliser ce composant ?

**Utiliser la pagination lorsqu’une liste d'éléments est trop importante pour être affichée sur une seule page** (plus de 20 éléments). Il est dès lors préférable de la diviser en plusieurs pages, afin de simplifier le parcours de l’usager au sein de cette liste.

Privilégier la pagination au rechargement automatique ou à un bouton “Voir plus” permet également un meilleur référencement de votre site.

## Comment utiliser ce composant ?

- **Placer systématiquement la pagination en bas de la liste**.
- **Mettre clairement en avant la page sur laquelle l’usager se trouve** grâce à l’état courant disponible.
- **Indiquer la dernière page de la liste comme dernier élément de la pagination** afin que l’usager connaisse le nombre total de pages.
- **Désactiver le lien “Précédent”** lorsque l’usager se trouve sur la première page et le lien “Suivant” lorsqu’il est sur la dernière page.
- **Permettre un accès rapide à la première et dernière page** lorsque celles-ci ne sont pas actives (soit avec les boutons “I<“ et “>I”, soit avec la page “1” et la dernière page).
- **Limiter de 5 à 7 le nombre de pages affichées par défaut dans la pagination**. Au-delà, masquer les autres pages par un système de troncature. La troncature est matérialisée par l’icône “…” qui s’affiche uniquement quand le nombre total de pages de la liste est supérieur à la limite fixée.
- **Envisager la double troncature** lorsque la page consultée est séparée par 5 pages ou plus de la première et de la dernière page.
- **Renvoyer l’usager en haut de page** lorsqu’il change de page à l’aide de la pagination.
- **Conserver le même fonctionnel de pagination** à travers l’intégralité de votre site.

## Règles éditoriales

La pagination n’est régie par aucune règle éditoriale spécifique.
