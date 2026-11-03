# Curseur

> Sélection d’une valeur sur une échelle

Voir aussi : [Design](design.md) · [Code](code.md) · [Accessibilité](accessibilite.md) · [Exemples](exemples.md)

Le curseur est un élément d’interaction avec l’interface permettant à l’usager de délimiter manuellement une sélection par rapport à une valeur minimale et maximale.

## Quand utiliser ce composant ?

**Utiliser un curseur lorsque la valeur saisie est imprécise ou à déterminer**, par exemple, la luminosité d’un écran. Il sert à montrer en temps réel l’impact des options choisies et à éclairer la prise de décision.

> [!NOTE]
> Préférer un [champ de saisie](../input/index.md) ou une [liste déroulante](../select/index.md) lorsque la valeur à renseigner est précise, comme une année de naissance par exemple, ou que le nombre de valeurs spécifiques parmi lesquelles choisir est important.

Le curseur n’a pas vocation à communiquer un état d’avancement quelconque. Pour ce type d’usage, utiliser l’[indicateur d’étapes](../stepper/index.md).

## Comment utiliser ce composant ?

- **Eviter d’intégrer un curseur au sein d’un formulaire**, sauf cas exceptionnel.
- **Lier l’usage du curseur à une actualisation du résultat en temps réel**, en fonction de la valeur sélectionnée. Par exemple, en tant que filtre déterminant l’affichage de donnée dans une liste ou un tableau.
- **Considérer que la valeur du curseur est toujours en nombre**. Des unités peuvent ensuite y être ajoutées (k€, €, kg, etc).

**✅ À faire** : Proposer une fourchette de valeurs exclusivement en nombre.

**❌ À ne pas faire** : Ne pas proposer des valeurs littérales et approximatives.

- **Proposer des échelles de valeur adaptées,** ni trop petites ni trop larges.

**✅ À faire** : Utiliser des cases à cocher ou des boutons radios, en cas d’échelle de valeur trop petite.

**❌ À ne pas faire** : Ne pas proposer une échelle de valeur non-adaptée, ici trop petite.

**✅ À faire** : Proposer des échelles de valeur adaptées, ni trop petites ni trop larges.

**❌ À ne pas faire** : Ne pas proposer une échelle de valeur non-adaptée, ici trop grande.

- **Utiliser le curseur lorsque vous avez l’espace de le faire**, notamment lorsque l’échelle de valeur est large. Si l’espace est limité, un [champ de saisie](../input/index.md) est certainement un meilleur choix.

**✅ À faire** : Utiliser un champ de saisie est certainement un meilleur choix lorsque l’échelle de valeur est large et l’espace limité.

## Règles éditoriales

Le curseur n’est régit par aucune règle éditoriale spécifique.
