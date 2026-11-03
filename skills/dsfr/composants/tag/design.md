# Tag : Design

- Une icône

- Un fond de couleur (obligatoire)

- Un libellé (obligatoire)

- Une coche (obligatoire, uniquement s'il s'agit d'un tag sélectionnable en état cliqué)

- Une croix (obligatoire, uniquement s'il s'agit d'un tag supprimable)

## Variations

**Tag non cliquable**

**Tag cliquable**

**Tag sélectionnable**

**Tag supprimable**

> [!NOTE]
> Cette variation n’autorise pas l’utilisation d’icône, autre que la croix de suppression présente par défaut.

**Groupe de tags**

Tous les tags peuvent être utilisés à plusieurs dans des groupes de tags. Dans ce cas-là ils appliquent des espacement préalablement définis par le DSFR.

## Tailles

Toutes les variations de tags sont disponibles en 2 tailles, pour pouvoir s’adapter au contexte d’affichage :

- SM pour small

- MD pour medium - taille par défaut

À noter que pour le groupe de tags en taille SM, le padding autour du tag est plus important que lorsqu’il est utilisé seul pour faciliter le clic en mobile.

## États

Le tag non cliquable est le seul qui n’est sujet à aucun changement d’état.

**Etat au survol**

L’état au survol correspond au comportement constaté par l’usager lorsqu’il survole le tag avec sa souris.

- Tag cliquable

- Tag sélectionnable

- Tag supprimable

**Etat cliqué**

L’état au clic correspond au comportement constaté par l’usager une fois un tag sélectionné, après avoir cliqué dessus.

- Tag sélectionnable

## Personnalisation

Seule la couleur des tags cliquables peut être personnalisée, parmi les couleurs illustratives autorisées uniquement.

**Tableau personnalisation design**

|  Éléments | Indice thème clair | Indice thème sombre |
|:-----|:-----|:-----|
| **Fond** | Indice **925**<br> exemple : `$pink-tuile-925` | Indice **125**<br> exemple : `$pink-tuile-125` |
| **Texte et icône**| Indice **sun**<br> exemple : `$pink-tuile-sun-425` | Indice **moon**<br> exemple : `$pink-tuile-moon-750` |

La personnalisation des tags doit se faire avec parcimonie et avec un objectif précis (permettre d'en faire ressortir un type ou le sens, par exemple).

> [!NOTE]
> Si vous personnalisez la couleur illustrative des badges, attention à la couleur d’arrière-plan sur laquelle ils sont positionnés à travers l’ensemble du site.

**✅ À faire** : Personnaliser uniquement la couleur des tags cliquables.

**❌ À ne pas faire** : Ne pas proposer les autres variations de tags en couleur.

**✅ À faire** : Associer le tag cliquable à une couleur pour valoriser l’information transmise, ici le type de support.

**❌ À ne pas faire** : Ne pas dépasser une ou deux couleurs de tags par page.

**✅ À faire** : Ajouter une icône au tag au besoin.

**❌ À ne pas faire** : Ne pas cumuler la croix du tag supprimable (icône par défaut) avec une seconde icône.
