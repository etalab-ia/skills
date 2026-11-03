# Badge : Design

- Une icône (uniquement pour les badges système)

- Un libellé (obligatoire, en majuscule)

- Un fond (obligatoire)

## Variations

**Badge standard**

**Badge système avec icône**

- Succès
- Avertissement
- Erreur
- Information
- Nouveauté

Utiliser cette variation pour préciser l’information donnée par le texte du badge avec l’icône correspondante.

L’ajout d’une icône est autorisée, et automatique en code, uniquement pour les badges système.

**Badge système sans icône**

Il est possible d’utiliser un badge système sans icône.

## Tailles

Le badge est disponible en 2 tailles :

- SM pour small

- MD pour medium - taille par défaut

## États

Le badge n’est sujet à aucun changement d’état.

## Personnalisation

Les badges systèmes ne sont pas personnalisables.

**✅ À faire** : Utiliser l’icône et la couleur système correspondantes à l’information fournie.

**❌ À ne pas faire** : Ne pas changer l’icône et la couleur d’un badge système.

La couleur des badges standard peut être personnalisée, parmi les couleurs illustratives autorisées uniquement.

**Tableau personnalisation design**

| Éléments | Indice thème clair | Indice thème sombre |
|:-----|:-----|:-----|
| **Fond** | Indice **950**<br>_exemple : `$pink-tuile-950`_ | Indice **100**<br>_exemple : `$pink-tuile-100`_ |
| **Texte** | Indice **sun**<br>_exemple : `$pink-tuile-sun-425`_ | Indice **moon**<br>_exemple : `$pink-tuile-moon-750`_ |

**✅ À faire** : Utiliser une couleur illustrative sur un badge standard (exemple : `$Pink-tuile`).

**❌ À ne pas faire** : Ne pas utiliser une icône dans un badge standard.

**❌ À ne pas faire** : Ne pas utiliser une couleur système pour un badge standard.
