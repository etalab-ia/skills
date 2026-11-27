# Ajout de fichier : Design

- Un libellé (obligatoire, exprimant clairement l’action attendue pour l’usager (par défaut “Ajouter un fichier"))

- Un texte explicatif (obligatoire, précisant les contraintes au niveau du ou des fichiers attendus (format, poids, nombre de fichiers possible etc.))

- Un bouton “Parcourir” (obligatoire, le texte dépendant du navigateur utilisé)

- Le nom du ou des fichiers (obligatoire, par défaut “Aucun fichier sélectionné”)

Au clic sur “Parcourir”, la boite de dialogue de sélection de fichier s’affiche. Les noms des fichiers sélectionnés viennent s’afficher à la place du texte par défaut.

## Variations

**Ajout multiple**

Utiliser l’ajout multiple dès lors que l’usager doit sélectionner plus d’un fichier.

## Tailles

L’ajout de fichier est disponible dans une seule taille. Sa largeur n’est pas contrainte, toutefois, dans le respect des bonnes pratiques UX, il est recommandé de conserver les éléments textuels sur une largeur de 8 colonnes maximum.

## États

**Etat d’erreur**

L'état d’erreur est signalé par un changement de couleur (cf. couleurs système : le rouge est la couleur de l’état erreur) et l’affichage d’un message d’erreur en-dessous du composant.

**Etat désactivé**

L’état désactivé indique que l'usager ne peut pas interagir avec le bouton.

> [!NOTE]
> **N’utiliser cet état que très ponctuellement**, pour indiquer à l’usager qu’il doit procéder à une action en amont par exemple.

## Personnalisation

L’ajout de fichier n’est pas personnalisable.

**❌ À ne pas faire** : Ne pas personnaliser la couleur du bouton par défaut.

**❌ À ne pas faire** : Ne pas personnaliser la couleur des textes d’accompagnement.
