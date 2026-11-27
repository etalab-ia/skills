# Espacement : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Espacements

Des classes utilitaires sont disponibles pour gérer les marges intérieures et extérieures d'un élément html. Celles-ci suivent la structure suivante (entre crochets les valeurs, facultatives, possibles):

- Le prefix : 'fr-', - la lettre 'm' pour margin ou 'p' pour padding, - l'orientation avec 't', 'r', 'b', 'l' (top, right, bottom, left) ou 'x', 'y' (horizontal, vertical), - un séparateur : '-', - le token d'espacement (nb: le signe '-' des nombres négatifs est remplacé par la lettre 'n', et 0 n'a pas d'unité 'v')

Il est possible de définir le breakpoint à partir du quel on applique l'espacement. Il suffit d'ajouter à la classe le breakpoint (md) avant la valeur du token. ex: fr-p-md-4v

Pour adapter les espacements à la taille de l'écran, on peut ainsi combiner les classes en partant du mobile puis en surchargeant en md

```html
<button type="button" class="fr-px-4v fr-px-md-16v fr-btn fr-btn">4v en mobile / 16v en md</button>
```
