# Classement des critères — thèmes 4 à 7

Classement provisoire, en attente de l’avis du pôle accessibilité numérique. Proposé par Isabelle Lafont.

- **code** : le verdict (C, NC ou NA) se tranche à la lecture du code.
- **mixte** : le code prouve une NC, ou une conformité quand la ligne le prévoit (critères « si nécessaire », contrastes entièrement déterminés dans le code) ; chaque ligne dit laquelle. Sans preuve dans le code, NT.
- **conditions réelles** : une vérification posée en phase 2 suffit ; sans réponse, NT.
- **jugement humain** : toujours NT, jamais C ; NA si le critère est sans objet.

## Thème 4 — Multimédia

- **4.1** Transcription textuelle ou audiodescription si nécessaire — mixte. Le code prouve : C quand une transcription est reliée ou adjacente au média, ou qu’une piste `<track kind="descriptions">` est présente. Reste : sans alternative, écouter ou voir le média pour dire s’il en exige une.
- **4.2** Transcription textuelle ou audiodescription pertinente — jugement humain. Reste : comparer la transcription ou l’audiodescription au contenu du média.
- **4.3** Sous-titres synchronisés si nécessaire — mixte. Le code prouve : C quand une piste `<track kind="captions">` est présente ; NC quand la piste de sous-titres porte un autre `kind`. Reste : sans piste, vérifier dans le lecteur si des sous-titres sont incrustés ou fournis par un lecteur tiers.
- **4.4** Sous-titres synchronisés pertinents — jugement humain. Reste : regarder le média pour comparer les sous-titres aux dialogues et aux sons porteurs d’information.
- **4.5** Audiodescription synchronisée si nécessaire — mixte. Le code prouve : C quand une piste `<track kind="descriptions">` ou une version audiodécrite reliée est présente. Reste : sans audiodescription, voir la vidéo pour dire si l’image porte une information absente de la bande-son.
- **4.6** Audiodescription synchronisée pertinente — jugement humain. Reste : regarder la version audiodécrite pour juger qu’elle restitue l’information visuelle.
- **4.7** Média temporel clairement identifiable — mixte. Le code prouve : NC quand aucun texte adjacent (titre, légende) n’identifie le média. Reste : juger que le texte adjacent identifie clairement le contenu du média.
- **4.8** Alternative d’un média non temporel si nécessaire — mixte. Le code prouve : C quand une alternative est reliée ou adjacente au média (`<canvas>`, `<object>`, `<embed>`, `<svg>` interactif). Reste : sans alternative, voir le média pour dire s’il en exige une.
- **4.9** Alternative d’un média non temporel pertinente — jugement humain. Reste : vérifier que l’alternative donne accès au même contenu et à des fonctionnalités similaires.
- **4.10** Son déclenché automatiquement contrôlable — mixte. Le code prouve : NC sur un `<audio>` ou une `<video>` en `autoplay`, non `muted`, sans `controls` ni bouton d’arrêt. Reste : écouter la page au chargement, un son lancé par un script ou un lecteur tiers ne se lit pas toujours dans le code ; une séquence de 3 secondes au plus est conforme.
- **4.11** Consultation d’un média temporel contrôlable au clavier et au pointeur — mixte (question « Clavier »). Le code prouve : NC sur un `<audio>` ou une `<video>` sans `controls` ni commandes personnalisées. Reste : utiliser au clavier et au pointeur chaque commande du lecteur (lecture, pause, volume, sous-titres).
- **4.12** Consultation d’un média non temporel contrôlable au clavier et au pointeur — mixte (question « Clavier »). Le code prouve : NC sur un `<canvas>`, un `<object>` ou un `<embed>` interactif sans élément focalisable ni alternative. Reste : utiliser chaque fonctionnalité du média au clavier et au pointeur.
- **4.13** Média compatible avec les technologies d’assistance — mixte. Le code prouve : NC sur un lecteur personnalisé dont les commandes n’ont ni nom accessible ni rôle (`<div>` cliquable, icône seule). Reste : vérifier avec un lecteur d’écran la restitution du média et de ses commandes, ou la présence d’une alternative compatible.

## Thème 5 — Tableaux

- **5.1** Résumé d’un tableau de données complexe — mixte. Le code prouve : C quand un résumé est relié au tableau (`<caption>`, `aria-describedby`) ; NC sur un tableau dont les en-têtes à plusieurs niveaux se voient dans le code, sans résumé. Reste : juger la complexité d’un tableau dont les en-têtes ne sont pas balisés.
- **5.2** Résumé pertinent — jugement humain. Reste : lire le résumé, tableau sous les yeux, pour juger qu’il en explique la structure.
- **5.3** Contenu linéarisé compréhensible d’un tableau de mise en forme — mixte. Le code prouve : NC sur un tableau de mise en forme sans `role="presentation"`, ou dont l’ordre des cellules ne suit pas l’ordre de lecture. Reste : lire le contenu dans l’ordre du code pour juger qu’il reste compréhensible.
- **5.4** Titre de tableau de données correctement associé — code
- **5.5** Titre de tableau de données pertinent — mixte. Le code prouve : NC sur un titre générique (« Tableau », « Données », « Liste »). Reste : juger que le titre identifie le contenu du tableau de manière claire et concise.
- **5.6** En-têtes de colonne et de ligne correctement déclarés — code
- **5.7** Association des cellules à leurs en-têtes — code
- **5.8** Tableau de mise en forme sans éléments propres aux tableaux de données — code

## Thème 6 — Liens

- **6.1** Lien explicite — mixte. Le code prouve : NC sur un intitulé non explicite (« cliquez ici », « en savoir plus ») sans contexte ni nom accessible qui le complète, ou sur un nom accessible qui ne contient pas l’intitulé visible. Reste : juger, contexte sous les yeux, que l’intitulé et son contexte disent la destination.
- **6.2** Intitulé de lien — code

## Thème 7 — Scripts

- **7.1** Script compatible avec les technologies d’assistance si nécessaire — mixte. Le code prouve : NC sur un composant scripté sans rôle cohérent ou sans nom (`<div>` cliquable, bouton icône sans nom), ou dont l’état n’est pas exposé (`aria-expanded` absent sur un bouton qui affiche ou masque un contenu). Reste : vérifier avec un lecteur d’écran la restitution du composant et de ses changements d’état.
- **7.2** Alternative à un script pertinente — mixte. Le code prouve : NC sur un `<noscript>` vide. Reste : juger que l’alternative donne accès au même contenu et aux mêmes fonctionnalités ; NA quand le script n’a pas d’alternative.
- **7.3** Script contrôlable au clavier et au pointeur — mixte (question « Clavier »). Le code prouve : NC sur un gestionnaire d’événement posé sur un élément non focalisable (`<div>` cliquable sans `tabindex` ni gestion de Entrée), sur un gestionnaire souris sans équivalent clavier, ou sur un script qui retire le focus (`blur()`). Reste : parcourir au clavier (Tab, Entrée, Espace, flèches, Échap) et au pointeur chaque élément scripté ; en mode composant, vérifier aussi qu’on sort du composant au clavier (12.9).
- **7.4** Changement de contexte : avertir ou laisser le contrôle — mixte. Le code prouve : NC sur un changement de contexte déclenché sans bouton ni lien explicite (`onchange` d’un `<select>` qui navigue ou soumet, déplacement du focus non demandé). Reste : vérifier dans le navigateur qu’aucun script hors du code audité ne change le contexte (soumission automatique, rechargement partiel).
- **7.5** Messages de statut restitués — mixte. Le code prouve : NC sur un message de succès, d’erreur ou de progression inséré sans `role="status"`, `role="alert"`, `role="log"` ni `role="progressbar"`. Reste : repérer dans le navigateur les messages ajoutés par des scripts hors du code audité, et vérifier avec un lecteur d’écran qu’ils sont annoncés.
