# Tableau : Design

- Un titre (obligatoire, qui peut être positionné en haut (par défaut), en bas ou hors écran (balise caption))

- Un bouton de tri par colonne

- Une case à cocher de sélection de colonne

- Une ou plusieurs données (par cellule)

- Une barre d’actions haute (pouvant contenir (uniquement et dans cet ordre) - le nombre de lignes sélectionnées, une barre de recherche, des boutons d’actions liés à la sélection de lignes et un contrôle segmenté)

- Une ligne d’en-tête de colonne (obligatoire)

- Plusieurs lignes de corps (obligatoire)

- Des bordures horizontales entre les lignes (obligatoire)

- Une barre d’actions basse (pouvant contenir (uniquement et dans cet ordre) - le nombre total de lignes du tableau, une liste déroulante, une pagination et des boutons d’actions agissants sur tout le tableau)

- Une colonne de sélection de ligne (toujours ferrée à gauche)

- Des bordure verticales entre les colonnes (uniquement obligatoire dans le cas d’un tableau complexe)

## Variations

**Tableau non scrollable**

**Tableau avec retour à la ligne automatique dans les cellules**

**Tableau avec largeur de colonnes minimales**

**Tableau avec première colonne fixée**

**Tableau complexe avec cellules fusionnées**

**Tableau avec filtre et différents types de données**

## Variantes esthétiques

**Bordures horizontales (par défaut)**

**Bordures horizontales et verticales**

## Densité

Le tableau prend automatiquement la taille de son conteneur.

Ce conteneur peut être scrollable horizontalement. Ceci est courant sur les écrans plus petits où il peut être impossible d'afficher le tableau complet sur l'écran de l'appareil. Le conteneur est donc responsive par défaut.

Toutefois, prenez garde à ce que les informations clés soient visibles au premier coup d’œil même sur un écran de petite taille.

Par défaut, la largeur des cellules s’adapte automatiquement à leur contenu. En revanche, il existe 3 niveaux de densité :

**SM pour small**

**MD pour medium**

**LG pour large**

Ainsi si la taille des composants intégrés dans les cellules ne change pas, cela vous permet toutefois de varier la densité d’affichage de votre tableau en fonction de son contenu.

## Ligne sélectionnable

> [!NOTE]
> Les états désactivé, focus et cliqué sont propres aux composants intégrés au sein des cellules.

## Personnalisation

Le tableau n’est pas personnalisable.

Toutefois, l’ensemble des composants imbriqués (icône, pictogramme, tag, badge, bouton, lien, champ de saisie, infobulle, interrupteur et liste déroulante) peuvent être personnalisés selon leurs propres règles de personnalisation.

Par ailleurs, certains éléments sont optionnels - voir la structure du composant.
