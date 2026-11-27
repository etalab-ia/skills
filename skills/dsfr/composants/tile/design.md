# Tuile : Design

- Un pictogramme

- Une première zone de détail (composée d’une précision sous forme de tags (cliquables ou non) ou de badges (jusqu'à 4 éléments))

- Un titre reprenant celui de l’objet visé (obligatoire, (page de destination, action réalisée, site etc.))

- Une description

- Une deuxième zone de détail (composée d’un texte)

- Une icône illustrative ((par défaut, une flèche))

- Une bordure (obligatoire, bleue lorsque la tuile est cliquable et noire lorsqu’elle est non cliquable)

## Variations

**Tuile horizontale**

- Cliquable

- Non cliquable

**Tuile verticale**

- Cliquable

- Non cliquable

**Tuile de téléchargement**

- Utiliser la tuile de téléchargement pour mettre à disposition de l’usager un fichier en téléchargement.
- Le titre de la tuile de téléchargement reprend le nom du fichier et doit systématiquement être précédé de la mention “Télécharger”.
- La seconde zone de détail affiche obligatoirement le format et le poids du fichier.
- L’icône de téléchargement est ici obligatoire.

**Variantes esthétiques**

- Tuile avec fond gris
- Tuile avec ombre portée
- Tuile sans bordure
- Tuile sans fond

## Tailles

La tuile est disponible en 2 tailles :

- SM pour small

En desktop, elle occupe un maximum de 3 à 4 colonnes de large.

- MD pour medium

En desktop, elle occupe entre 4 et 6 colonnes de large.

En version mobile, les deux tailles SM et MD occupent l’intégralité de la largeur de la grille.

Par ailleurs, la hauteur de la tuile s’adapte à son contenu.

## États

**État désactivé**

L’état désactivé indique que l'usager ne peut pas interagir avec la tuile.

**État au survol**

L’état au survol correspond au comportement constaté par l’usager lorsqu’il survole la tuile avec sa souris.

## Personnalisation

La tuile comporte des variantes esthétiques (voir section “Variations”).

L’ensemble des composants imbriqués ([pictogramme](../../fondamentaux/pictogram/index.md) et [badge](../badge/index.md)) peuvent également être personnalisés selon leurs propres règles de personnalisation.

Par ailleurs, certains éléments sont optionnels - voir la structure du composant.

**✅ À faire** : Proposer une tuile avec un fond par défaut.

**❌ À ne pas faire** : Ne pas personnaliser le fond de la tuile avec une autre couleur illustrative.

**✅ À faire** : Choisir la couleur secondaire du pictogramme parmi celles disponibles dans les couleurs illustratives.

**❌ À ne pas faire** : Ne pas personnaliser la couleur primaire du pictogramme.

**✅ À faire** : S’affranchir du contour de la tuile.

**❌ À ne pas faire** : Ne pas supprimer ou personnaliser la couleur de la bordure qui traduit le caractère cliquable ou non cliquable de la tuile.
