# Curseur : Design

- Un libellé (obligatoire, associé au curseur)

- Un texte de description additionnel

- Une piste avec poignée et valeur sélectionnée (obligatoire)

- Une valeur minimale et maximale

## Variations

**Curseur simple**

- Utiliser le curseur simple pour permettre à l’usager de choisir une plage, en partant d’un minimum fixe prédéfini.

**Curseur double**

- Utiliser le curseur double pour permettre à l’usager de choisir une plage, sans valeur prédéfinie.

**Curseur cranté**

- Utiliser le curseur cranté pour permettre à l’usager de choisir une plage, en contraignant les valeurs possibles.

**Sans indicateurs minimum et maximum**

**Avec préfixe et suffixe**

## Tailles

Le curseur est disponible en 2 tailles :

- SM pour small
- MD pour medium

En desktop, la taille minimum est de 180 px et la taille maximum est de 588 px.

En mobile, la taille minimum est de 136 px et la taille maximum est de 288 px mais il est conseillé de préférer la version MD.

## États

**État désactivé**

L’état désactivé indique que l'usager ne peut pas interagir avec le curseur.

> [!WARNING]
> N’utiliser cet état que très ponctuellement, pour indiquer à l’usager qu’il doit procéder à une action en amont par exemple.

**Etat d’erreur**

L'état d’erreur est signalé par un changement de couleur du libellé ainsi que l’affichage d’une ligne rouge (cf. couleurs fonctionnelles : le rouge est la couleur de l’état erreur) et d’un message d’erreur en-dessous du composant.

**Etat de succès**

L'état de succès est signalé par un changement de couleur du libellé ainsi que l’affichage d’une ligne verte (cf. couleurs fonctionnelles : le vert est la couleur de l’état succès) et d’un message de succès en-dessous du composant.

## Personnalisation

Le curseur n’est pas personnalisable.

Toutefois, certains éléments sont optionnels - voir la structure du composant.

**❌ À ne pas faire** : Ne pas personnaliser la couleur de la piste.

**❌ À ne pas faire** : Ne pas personnaliser la forme de la poignée.
