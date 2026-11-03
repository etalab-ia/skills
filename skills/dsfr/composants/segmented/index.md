# Contrôle segmenté

> Sélection de vues avec un contrôle segmenté.

Voir aussi : [Design](design.md) · [Code](code.md) · [Accessibilité](accessibilite.md) · [Exemples](exemples.md)

Le contrôle segmenté est un élément d’interaction avec l’interface permettant à l'usager de choisir un type de vue parmi plusieurs options d'affichage disponibles.

## Quand utiliser ce composant ?

Utiliser le contrôle segmenté pour proposer différents types d’affichage d’une même vue (exemple : liste versus carte).

> [!NOTE]
> Le contrôle segmenté n’est pas un système de filtre et ne doit donc pas être utilisé comme tel. Préférer des tags sélectionnables ou listes déroulantes, selon les cas d’usage.

## Comment utiliser ce composant ?

- **Minimiser le nombre de segments proposés.** Il est recommandé de se limiter à 2 ou 3 bien que le maximum possible soit de 5.
- **Définir une valeur par défaut** qui sera la vue présentée à l’usager lors de son arrivée sur la page.

**✅ À faire** : Sélectionner une valeur par défaut lorsque vous proposez le contrôle segmenté.

**❌ À ne pas faire** : Ne pas proposer le contrôle segmenté sans valeur par défaut. Il faut obligatoirement une vue pré-sélectionnée pour l’usager.

- **Conserver un libellé pour chaque segment** afin de rendre l’action réalisée par l’usager explicite. L’utilisation d’un segment avec une icône seule n’est pas autorisée.

**✅ À faire** : Conserver le libellé pour chaque segment. L’action réalisée par l’usager doit être explicite.

**❌ À ne pas faire** : Ne pas proposer de segments sans libellé, avec icône seule.

- **Harmoniser les segments** en utilisant le même format pour tous (avec ou sans icône). Il n'est pas autorisé de mélanger des segments de formats différents dans le même composant.

**✅ À faire** : Harmoniser les segments en utilisant le même format pour tous.

**❌ À ne pas faire** : Ne pas mélanger des segments de formats différents.

- **Le changement de vue a une conséquence directe sur la page consultée**, un seul segment peut être sélectionné à la fois.

## Règles éditoriales

- **Rédiger des libellés de segment clairs et concis**. L’usager doit comprendre facilement ses options.
- Des libellés courts permettent également d’éviter que les éléments ne passent en vertical.
