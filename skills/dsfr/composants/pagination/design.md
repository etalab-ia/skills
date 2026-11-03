# Pagination : Design

- Un bouton tertiaire avec icône seule permettant de se rendre directement à la première ou à la dernière page

- Un bouton tertiaire avec icône permettant de revenir à la page précédente ou de passer à la page suivante (obligatoire)

- Un bouton primaire indiquant la page active (obligatoire)

- Des boutons tertiaires de numéros de page (obligatoire)

- Un bouton troncature (sous forme de points de suspension pour éviter d’afficher tous les numéros de page lorsqu’ils sont nombreux)

## Variations

**Responsive**

- Conserver le même fonctionnel sur les différentes tailles d'écran.
- Cacher certains numéros de page pour alléger l'affichage sur les écrans mobiles.
- Limiter le nombre de pages visibles pour pouvoir idéalement afficher l’ensemble des éléments de la pagination sur une seule ligne.
- Privilégier les icônes “<“ et “>” pour les actions “Précédent” et “Suivant”.

## Tailles

La largeur de la pagination s’adapte à la taille de son conteneur.

## États

**État désactivé**

L’état désactivé indique que l'usager ne peut pas interagir avec un lien.

- Appliquer cet état aux liens “Précédent” et "première page" lorsque vous êtes sur la première page et sur les liens “Suivant” et "dernière page" lorsque vous êtes sur la dernière page.

**État au survol**

L’état au survol correspond au comportement constaté par l’usager lorsqu’il survole un des liens avec sa souris.

**État courant**

L’état courant permet d’indiquer à l’usager la page active, soit celle sur laquelle il se situe.

## Personnalisation

La pagination n’est pas personnalisable.

Toutefois, certains éléments sont optionnels - voir la structure du composant.

**✅ À faire** : Mettre en évidence la page active en appliquant un fond bleu derrière le numéro de page.

**❌ À ne pas faire** : Ne pas personnaliser la couleur du fond qui indique la page active.
