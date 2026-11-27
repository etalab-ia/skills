# Carte : Design

- Un badge (placé dans la zone de média)

- Un média (image ou vidéo) (issu ou en lien avec la page de destination)

- Une précision (sous forme de tag (cliquable ou non) ou de badge (jusqu'à 4 éléments maximum))

- Une première zone de détail (comprenant un texte accompagné d’une icône (si souhaité))

- Un titre (obligatoire, reprenant celui de l’objet visé (page de destination, action, site etc.) et comprenant un lien dont la zone de clic peut s’étendre à toute la carte (mais incompatible avec une zone d’action ou des tags cliquables))

- Une description (de 5 lignes maximum (tronquée au-delà))

- Une seconde zone de détail (identique à la première)

- Une zone d’action (composée de bouton ou de liens (jusqu'à 4 éléments maximum) mais incompatible avec la deuxième zone de détail)

## Variations

La carte existe en deux formats (horizontal et vertical) déclinés sur deux supports (desktop et mobile). Les cartes horizontales sont réservées au desktop et à la carte de téléchargement en format mobile. A cette exception près, une carte horizontale devient systématiquement verticale sur mobile.

**Carte verticale**

**Carte horizontale**

Aucun ratio n’est imposé dans une carte horizontale.

La taille de l’image est déduite :

- En hauteur, par la hauteur du contenu.
- En largeur, par les proportions choisies de la carte parmi celles proposées : 33%, 40% et 50%.

Le ratio par défaut est de 40% pour l’image et 60% pour le contenu.

**Carte de téléchargement**

- Utiliser la carte de téléchargement pour mettre à disposition de l’usager un fichier en téléchargement.
- Le titre de la carte de téléchargement reprend le nom du fichier et doit systématiquement être précédé de la mention “Télécharger”. Préciser la langue du document dans le libellé si elle est différente de celle de la page courante.
- La seconde zone de détail affiche obligatoirement le format et le poids du fichier.
- L’icône de téléchargement est ici obligatoire.
- En mobile, la carte de téléchargement est toujours en format horizontal.

**❌ À ne pas faire** : Ne pas cumuler plus de 4 cartes de téléchargement.

**Variantes esthétiques**

- Carte avec fond gris
- Carte avec ombre portée
- Carte sans bordure
- Carte sans fond

## Tailles

La carte est disponible en trois tailles :

- SM pour small
- MD pour medium
- LG pour large

La hauteur de la carte s’adapte à son contenu. La largeur, elle, est définie selon [la grille](../../fondamentaux/grid/index.md) et les recommandations suivantes.

Pour une carte verticale, en desktop :

- SM : 3 à 4 colonnes

- MD : 4 à 6 colonnes

- LG : 6 à 8 colonnes

En mobile, peu importe la taille d’origine, la carte verticale prend systématiquement 12 colonnes de large.

Pour une carte horizontale, en desktop uniquement :

- SM : 4 à 6 colonnes

- MD : 6 à 8 colonnes

- LG : 8 à 12 colonnes

En mobile, seule la carte de téléchargement conserve un format horizontal. Dans ce cas, elle prend systématiquement 12 colonnes de large.

> [!NOTE]
> La taille choisie a une influence sur les espacements, la taille du titre, de l’icône et des tags ou badges au sein de la carte.

## États

**État désactivé**

L’état désactivé indique que l'usager ne peut pas interagir avec la carte.

**État au survol**

L’état au survol correspond au comportement constaté par l’usager lorsqu’il survole la carte avec sa souris.

## Personnalisation

La carte comporte des variantes esthétiques (voir section “Variations”).

L’ensemble des composants imbriqués ([média](../../fondamentaux/media/index.md), [icône](../../fondamentaux/icon/index.md), [tag](../tag/index.md), [badge](../badge/index.md) et [bouton](../button/index.md)) peuvent également être personnalisés selon leurs propres règles de personnalisation.

Par ailleurs, certains éléments sont optionnels - voir la structure du composant.
