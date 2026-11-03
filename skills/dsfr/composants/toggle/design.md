# Interrupteur : Design

- Une légende décrivant le contexte (obligatoire, uniquement dans le cadre d'un groupe d'interrupteurs)

- Une description additionnelle pour la légende

- Un interrupteur (obligatoire)

- Un libellé (obligatoire, associé à l'interrupteur)

- Un texte "état" décrivant l'état de l'interrupteur (activé / désactivé) (placé en dessous du bouton et conseillé afin de faciliter la compréhension de l'usager)

- Un séparateur

- Un texte additionnel (accompagnant chaque interrupteur / libellé)

## Variations

**Interrupteur simple**

**Interrupteur avec description**

**Interrupteur avec état**

**Groupe d’interrupteurs**

Utiliser l’interrupteur en groupe pour constituer une liste d’actions de même nature.

Lorsqu’il est utilisé en groupe, l’interrupteur doit toujours respecter le même format. Si le premier interrupteur affiche l'état, une description, ou le séparateur optionnel, alors l’ensemble des interrupteurs du groupe devront également afficher ces éléments.

**Groupe d’interrupteurs avec séparateurs**

## Tailles

La largeur de l’interrupteur s’adapte à la taille de son conteneur. Si l’interrupteur se trouve dans un conteneur large avec le bouton à droite du libellé, attention à ce qu’il ne s’en détache pas visuellement.

## États

**État d’erreur**

L'état d’erreur est signalé par un changement de couleur ainsi que l’affichage d’une ligne rouge (cf. couleurs système : le rouge est la couleur de l’état erreur) et d’un message d’erreur en-dessous du composant.

**Etat de succès**

L'état de succès est signalé par un changement de couleur ainsi que l’affichage d’une ligne verte (cf. couleurs système : le vert est la couleur de l’état succès) et d’un message de succès en-dessous du composant.

**État désactivé**

L’état désactivé indique que l'usager ne peut pas interagir avec le bouton.

Dans le cas d’un interrupteur, il permet d’afficher un choix déjà effectué et/ou ne pouvant être modifié par l’usager.

## Personnalisation

Les interrupteurs ne sont pas personnalisables.

Toutefois, certains éléments sont optionnels - voir [la structure du composant](index.md).

**✅ À faire** : Utiliser uniquement la couleur bleu pour les interrupteurs.

**❌ À ne pas faire** : Ne pas personnaliser la couleur des interrupteurs.

**✅ À faire** : Conserver la coche lorsque l’interrupteur est activé.

**❌ À ne pas faire** : Ne pas supprimer ou personnaliser l’icône de l’interrupteur.
