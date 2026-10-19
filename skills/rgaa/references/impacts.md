# Impacts des défauts d’accessibilité, par mécanisme de blocage

Adapté de `impacts.md` du skill `rgaa-dev` ([Isalafont/claude-skill-rgaa-dev](https://github.com/Isalafont/claude-skill-rgaa-dev), Isabelle Lafont, Licence Ouverte 2.0, version du 2026-04-20), réorganisé par mécanisme de blocage. Inspiré de la ressource « Impacts des défauts de conformité au RGAA » d’Ideance : https://ideance-a11y.github.io/rgaa4-impacts-utilisateurs/

Cette table aide à rédiger la ligne « Impact utilisateur » d’une non-conformité. Elle n’est ni exhaustive ni normative : la règle reste le critère RGAA. Chaque impact décrit ce que le défaut empêche de faire et avec quel outil, jamais une catégorie de handicap.

## Lecteur d’écran et plage braille

Pour une personne qui utilise un lecteur d’écran (NVDA, JAWS, VoiceOver, TalkBack), éventuellement couplé à une plage braille, la page n’existe qu’à travers ce que le code restitue.

| Défaut | Impact | Critères |
|--------|--------|----------|
| Image informative sans `alt` | L’image est ignorée, ou son nom de fichier est lu : l’information qu’elle porte est perdue | 1.1 |
| Lien « Cliquez ici » | La destination reste inconnue tant que le texte autour n’a pas été lu ; dans la liste des liens, tous se ressemblent | 6.1 |
| Champ sans étiquette | Le champ est annoncé sans intitulé : on ne sait pas quelle donnée saisir | 11.1 |
| Tableau sans en-têtes associés | Les cellules sont lues sans leur en-tête de ligne ou de colonne : les données n’ont plus de sens | 5.6, 5.7 |
| Message de statut sans `aria-live` ni rôle adapté | Une confirmation, une erreur ou un résultat de recherche apparaît à l’écran sans être annoncé | 7.5 |
| Modale qui laisse le focus sortir | Le parcours sort de la modale et passe dans le contenu situé derrière, sans que rien ne le signale | 7.1 |
| Titres absents ou mal hiérarchisés | La navigation par titres, principal moyen de survoler une page, ne fonctionne pas | 9.1 |
| Zones de la page non identifiées (`main`, `nav`…) | Impossible d’aller directement au contenu principal ou à la navigation | 12.6 |
| Page active du menu signalée uniquement par la couleur ou la forme | Le lien de la page en cours est annoncé comme les autres : impossible de savoir sur quelle page on se trouve | 3.1, 10.9 |
| Information transmise uniquement par la couleur | L’information n’est pas restituée du tout | 3.1 |

## Agrandissement d’écran et zoom

Pour une personne qui agrandit l’affichage (zoom du navigateur à 200 % ou plus, logiciel d’agrandissement comme ZoomText), seule une petite partie de la page est visible à la fois.

| Défaut | Impact | Critères |
|--------|--------|----------|
| Mise en page qui casse au zoom | Contenus coupés ou superposés, défilement horizontal : une partie de la page devient inaccessible | 10.4, 10.11 |
| Texte en image | Le texte devient flou à l’agrandissement et ne peut pas être reformaté | 1.8 |
| Contraste de texte insuffisant | Le texte est difficile, voire impossible, à lire | 3.2 |

## Perception des couleurs et des contrastes

Pour une personne qui ne distingue pas certaines couleurs ou perçoit mal les faibles contrastes, une différence portée par la seule couleur disparaît.

| Défaut | Impact | Critères |
|--------|--------|----------|
| Statut en rouge ou vert sans autre indicateur | Impossible de distinguer un succès d’une erreur | 3.1 |
| Graphique dont les séries ne se distinguent que par la couleur | Les catégories se confondent | 3.1 |
| Lien distingué du texte uniquement par sa couleur | Le lien ne se repère pas dans le paragraphe | 10.6 |
| Contraste insuffisant d’un composant d’interface (bordure de champ, icône) | Le champ ou le bouton ne se repère pas | 3.3 |

## Navigation au clavier et contacteurs

Pour une personne qui navigue au clavier seul, avec un contacteur ou un dispositif de pointage par le regard, chaque élément interactif doit être atteint et activé sans souris.

| Défaut | Impact | Critères |
|--------|--------|----------|
| Focus non visible (`outline: none`) | Impossible de savoir où l’on se trouve dans la page | 10.7 |
| Composant non utilisable au clavier | La fonctionnalité est inaccessible | 7.3 |
| Ordre de tabulation incohérent | Le parcours saute d’une zone à l’autre et devient incompréhensible | 12.8 |
| Pas de lien d’évitement | Il faut traverser toute la navigation sur chaque page avant d’atteindre le contenu | 12.7 |
| Piège au clavier | Impossible de sortir du composant : la suite de la page est hors d’atteinte | 12.9 |

## Commande vocale

Pour une personne qui pilote l’interface à la voix (Dragon, Contrôle vocal de macOS ou iOS), un élément s’active en prononçant son intitulé visible.

| Défaut | Impact | Critères |
|--------|--------|----------|
| Nom accessible qui ne contient pas l’intitulé visible | La commande « cliquer sur Envoyer » ne trouve pas le bouton | 6.1, 11.2 |
| Champ sans `autocomplete` adapté | Le remplissage automatique ne fonctionne pas : chaque donnée personnelle doit être dictée | 11.13 |

## Sous-titres et transcription

Pour une personne qui n’entend pas le son, ou ne peut pas l’écouter, l’information sonore doit exister sous forme de texte.

| Défaut | Impact | Critères |
|--------|--------|----------|
| Vidéo sans sous-titres | Le contenu parlé est perdu | 4.3 |
| Audio sans transcription | Le contenu est inaccessible | 4.1 |

## Compréhension et lecture

Pour une personne qui lit lentement, se fatigue vite ou a besoin de consignes explicites, chaque ambiguïté se paie en erreurs et en tentatives.

| Défaut | Impact | Critères |
|--------|--------|----------|
| Message d’erreur vague (« Erreur 422 ») | Impossible de comprendre quoi corriger | 11.10 |
| Pas de suggestion de correction | Le format attendu doit être deviné | 11.11 |
| Session expirée sans avertissement | Les données saisies sont perdues | 13.1 |
| Absence de structure (titres, listes) | La lecture devient linéaire et la page plus difficile à appréhender | 9.1, 9.3 |

## Animations et clignotements

Pour une personne sensible aux mouvements ou aux flashs, une animation qu’on ne peut pas arrêter empêche de lire, voire met sa santé en danger.

| Défaut | Impact | Critères |
|--------|--------|----------|
| Contenu qui clignote plus de 3 fois par seconde | Risque de crise d’épilepsie | 13.7 |
| Animation impossible à mettre en pause ou à arrêter | Nausées, vertiges, impossibilité de se concentrer sur la lecture | 13.8 |

---

## Priorités de correction

Mêmes niveaux que la grille de priorités du `SKILL.md`.

### 🔴 Bloquant

- Alternatives textuelles aux images informatives
- Étiquettes sur tous les champs de formulaire
- Utilisation au clavier de tous les composants interactifs
- Focus visible
- Liens d’évitement
- Sous-titres des vidéos (Majeur si une transcription donne déjà accès au contenu)

### 🟠 Majeur

- Contraste du texte d’au moins 4,5:1
- Hiérarchie de titres cohérente
- Messages d’erreur explicites, avec suggestion de correction
- Annonce des messages de statut
- Zones de la page identifiées (`header`, `nav`, `main`, `footer`)

### 🟡 Mineur

- Fil d’Ariane
- `aria-current="page"` dans la navigation
- Description détaillée des contenus complexes (graphiques)
- Animations désactivables
