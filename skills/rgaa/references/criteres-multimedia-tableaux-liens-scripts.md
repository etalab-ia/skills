# RGAA — Thèmes 4 à 7 : Multimédia, Tableaux, Liens, Scripts

## Thème 4 — Multimédia (13 critères)

### 4.1–4.2 Transcription textuelle ou audiodescription présente et pertinente

**Texte officiel 4.1 :** Chaque *média temporel* pré-enregistré a-t-il, si nécessaire, une *transcription textuelle* ou une *audiodescription* (hors cas particuliers) ?
- **4.1.1** Chaque *média temporel* pré-enregistré seulement audio, vérifie-t-il, si nécessaire, l’une de ces conditions (hors cas particuliers) ?
  - Il existe une *transcription textuelle* accessible via un *lien ou bouton adjacent* ;
  - Il existe une *transcription textuelle* adjacente clairement identifiable.
- **4.1.2** Chaque *média temporel* pré-enregistré seulement vidéo vérifie-t-il, si nécessaire, l’une de ces conditions (hors cas particuliers) ?
  - Il existe une *version alternative « audio seulement »* accessible via un *lien ou bouton adjacent* ;
  - Il existe une *version alternative « audio seulement »* adjacente clairement identifiable ;
  - Il existe une *transcription textuelle* accessible via un *lien ou bouton adjacent* ;
  - Il existe une *transcription textuelle* adjacente clairement identifiable ;
  - Il existe une *audiodescription* synchronisée ;
  - Il existe une version alternative avec une *audiodescription* synchronisée accessible via un *lien ou bouton adjacent*.
- **4.1.3** Chaque *média temporel* synchronisé pré-enregistré vérifie-t-il, si nécessaire, une de ces conditions (hors cas particuliers) ?
  - Il existe une *transcription textuelle* accessible via un *lien ou bouton adjacent* ;
  - Il existe une *transcription textuelle* adjacente clairement identifiable ;
  - Il existe une *audiodescription* synchronisée ;
  - Il existe une version alternative avec une *audiodescription* synchronisée accessible via un *lien ou bouton adjacent*.
- *Cas particuliers :*
  - Il existe une gestion de cas particulier lorsque :
    - - Le *média temporel* est utilisé à des fins décoratives (c’est-à-dire qu’il n’apporte aucune information) ;
    - - Le *média temporel* est lui-même une alternative à un contenu de la page (une vidéo en langue des signes ou la vocalisation d’un texte, par exemple) ;
    - - Le *média temporel* est utilisé pour accéder à une version agrandie ;
    - - Le *média temporel* est utilisé comme un *CAPTCHA* ;
    - - Le *média temporel* fait partie d’un test qui deviendrait inutile si la *transcription textuelle*, les *sous-titres synchronisés* ou l’*audiodescription* étaient communiqués ;
    - - Pour les services de l’État, les collectivités territoriales et leurs établissements : si le *média temporel* a été publié entre le 23 septembre 2019 et le 23 septembre 2020 sur un site internet, intranet ou extranet créé depuis le 23 septembre 2018, il est exempté de l’obligation d’accessibilité ;
    - - Pour les personnes de droit privé mentionnées aux 2° à 4° du I de l’article 47 de la loi du 11 février 2005 : si le *média temporel* a été publié avant le 23 septembre 2020, il est exempté de l’obligation d’accessibilité.
  - Dans ces situations, le critère est non applicable.
  - Ce cas particulier s’applique également aux critères 4.2, 4.3, 4.5.

**Texte officiel 4.2 :** Pour chaque *média temporel* pré-enregistré ayant une *transcription textuelle* ou une *audiodescription* synchronisée, celles-ci sont-elles pertinentes (hors cas particuliers) ?

4.1 : l’alternative existe, si le média en a besoin. 4.2 : elle restitue le contenu du média.

**Non-conformité type :** `<audio>` sans transcription ; transcription absente ou accessible uniquement après téléchargement.
**Impact :** sans transcription, la personne sourde ou malentendante, ou qui utilise une plage braille, n’accède pas au contenu parlé du média.
**Priorité :** 🔴 Bloquant

---

### 4.3–4.4 Sous-titres synchronisés présents et pertinents

**Texte officiel 4.3 :** Chaque *média temporel* synchronisé pré-enregistré a-t-il, si nécessaire, des *sous-titres synchronisés* (hors cas particuliers) ?
- **4.3.1** Chaque *média temporel* synchronisé pré-enregistré vérifie-t-il, si nécessaire, l’une de ces conditions (hors cas particuliers) ?
  - Le *média temporel* synchronisé possède des *sous-titres synchronisés* ;
  - Il existe une version alternative possédant des *sous-titres synchronisés* accessible via un *lien ou bouton adjacent*.
- **4.3.2** Pour chaque *média temporel* synchronisé pré-enregistré possédant des *sous-titres synchronisés* diffusés via une balise `<track>`, la balise `<track>` possède-t-elle un attribut `kind="captions"` ?
- *Cas particuliers :*
  - Voir cas particuliers critère 4.1.

**Texte officiel 4.4 :** Pour chaque *média temporel* synchronisé pré-enregistré ayant des *sous-titres synchronisés*, ces sous-titres sont-ils pertinents ?

4.3 : les sous-titres existent, si le média en a besoin. 4.4 : ils restituent les dialogues et les sons porteurs d’information.

**Non-conformité type :** vidéo parlée sans aucun sous-titre, ni piste, ni incrustation, ni version alternative ; `<track kind="subtitles">` utilisée pour les sous-titres d’accessibilité.
**Impact :** sans sous-titres, la personne sourde ou malentendante perd le contenu parlé et les sons porteurs d’information.
**Priorité :** 🔴 Bloquant

---

### 4.5–4.6 Audiodescription synchronisée présente et pertinente

**Texte officiel 4.5 :** Chaque *média temporel* pré-enregistré a-t-il, si nécessaire, une *audiodescription* synchronisée (hors cas particuliers) ?
- **4.5.1** Chaque *média temporel* pré-enregistré seulement vidéo vérifie-t-il, si nécessaire, une de ces conditions (hors cas particuliers) ?
  - Il existe une *audiodescription* synchronisée ;
  - Il existe une version alternative avec une *audiodescription* synchronisée.
- **4.5.2** Chaque *média temporel* synchronisé pré-enregistré vérifie-t-il, si nécessaire, une de ces conditions (hors cas particuliers) ?
  - Il existe une *audiodescription* synchronisée ;
  - Il existe une version alternative avec une *audiodescription* synchronisée.
- *Cas particuliers :*
  - Voir cas particuliers critère 4.1.

**Texte officiel 4.6 :** Pour chaque *média temporel* pré-enregistré ayant une *audiodescription* synchronisée, celle-ci est-elle pertinente ?

4.5 : l’audiodescription existe, si l’image porte une information absente de la bande-son. 4.6 : elle restitue cette information.

**Non-conformité type :** Vidéo sans parole qui présente une démarche à l’écran, sans audiodescription ni version audiodécrite.
**Impact :** sans audiodescription, la personne aveugle ou malvoyante n’accède pas à ce qui n’est transmis que par l’image.
**Priorité :** 🟠 Majeur

---

### 4.7 Média clairement identifiable

**Texte officiel 4.7 :** Chaque *média temporel* est-il clairement identifiable (hors cas particuliers) ?
- **4.7.1** Pour chaque *média temporel* seulement son, seulement vidéo ou synchronisé, le contenu textuel adjacent permet-il d’identifier clairement le *média temporel* (hors cas particuliers) ?
- *Cas particuliers :*
  - Il existe une gestion de cas particulier lorsque le *média temporel* est utilisé à des fins décoratives (c’est-à-dire qu’il n’apporte aucune information). Dans cette situation, le critère est non applicable.

**Non-conformité type :** `<video>` seule dans la page, sans titre ni légende.
**Impact :** sans texte adjacent, la personne qui utilise un lecteur d’écran ne sait pas quel média elle s’apprête à lancer.
**Priorité :** 🟡 Mineur

---

### 4.8–4.9 Média non temporel : alternative présente et pertinente

**Texte officiel 4.8 :** Chaque *média non temporel* a-t-il, si nécessaire, une alternative (hors cas particuliers) ?
- **4.8.1** Chaque *média non temporel* vérifie-t-il, si nécessaire, une de ces conditions (hors cas particuliers) ?
  - Un *lien ou un bouton adjacent*, clairement identifiable, permet d’accéder à une page contenant une alternative ;
  - Un *lien ou un bouton adjacent*, clairement identifiable, permet d’accéder à une alternative dans la page.
- **4.8.2** Chaque *média non temporel* associé à une alternative vérifie-t-il une de ces conditions (hors cas particuliers) ?
  - La page référencée par le *lien ou bouton adjacent* est accessible ;
  - L’alternative dans la page, référencée par le *lien ou bouton adjacent*, est accessible.
- *Cas particuliers :*
  - Il existe une gestion de cas particulier lorsque :
    - - Le *média non temporel* est utilisé à des fins décoratives (c’est-à-dire qu’il n’apporte aucune information) ;
    - - Le *média non temporel* est diffusé dans un *environnement maîtrisé* ;
    - - Le *média non temporel* est inséré via JavaScript en vérifiant la présence et la version du plug-in, en remplacement d’un *contenu alternatif* déjà présent.
  - Dans ces situations, le critère est non applicable.

**Texte officiel 4.9 :** Pour chaque *média non temporel* ayant une alternative, cette alternative est-elle pertinente ?

4.8 : l’alternative existe, si le média en a besoin. 4.9 : elle donne accès au même contenu et à des fonctionnalités similaires.

**Non-conformité type :** Carte interactive en `<canvas>` sans lien vers une liste équivalente.
**Impact :** sans alternative, la personne qui ne peut pas utiliser le média (lecteur d’écran, clavier seul) n’a aucun accès à son contenu.
**Priorité :** 🟠 Majeur

---

### 4.10 Son automatique contrôlable

**Texte officiel 4.10 :** Chaque son déclenché automatiquement est-il *contrôlable* par l’utilisateur ?
- **4.10.1** Chaque séquence sonore déclenchée automatiquement via une balise `<object>`, `<video>`, `<audio>`, `<embed>`, `<bgsound>` ou un code JavaScript vérifie-t-elle une de ces conditions ?
  - La séquence sonore a une durée inférieure ou égale à 3 secondes ;
  - La séquence sonore peut être stoppée sur action de l’utilisateur ;
  - Le volume de la séquence sonore peut être contrôlé par l’utilisateur indépendamment du contrôle de volume du système.

Son automatique interdit sauf durée de 3 secondes au plus, ou possibilité de l’arrêter ou d’en régler le volume indépendamment du système.

**Non-conformité type :** Vidéo ou audio en autoplay sans contrôle de volume/pause accessible.
**Impact :** un son lancé tout seul couvre la voix du lecteur d’écran : la personne qui l’utilise n’entend plus rien et ne trouve plus comment l’arrêter.
**Priorité :** 🟠 Majeur

---

### 4.11 Média temporel contrôlable au clavier et au pointeur

**Texte officiel 4.11 :** La consultation de chaque *média temporel* est-elle, si nécessaire, *contrôlable par le clavier et tout dispositif de pointage* ?
- **4.11.1** Chaque *média temporel* a-t-il, si nécessaire, les fonctionnalités de *contrôle de sa consultation* ?
- **4.11.2** Pour chaque *média temporel*, chaque fonctionnalité vérifie-t-elle une de ces conditions ?
  - La fonctionnalité est *accessible par le clavier et tout dispositif de pointage* ;
  - Une fonctionnalité *accessible par le clavier et tout dispositif de pointage* permettant de réaliser la même action est présente dans la page.
- **4.11.3** Pour chaque *média temporel*, chaque fonctionnalité vérifie-t-elle une de ces conditions ?
  - La fonctionnalité est *activable par le clavier et tout dispositif de pointage* ;
  - Une fonctionnalité *activable par le clavier et tout dispositif de pointage* permettant de réaliser la même action est présente dans la page.

Au minimum lecture et pause ou stop ; activation et désactivation du son si le média en a ; des sous-titres et de l’audiodescription s’il en a.

**Non-conformité type :** Lecteur vidéo custom dont les boutons ne sont pas focusables au clavier.
**Impact :** sans commande utilisable au clavier, la personne qui ne se sert pas de la souris ne peut ni lancer ni arrêter le média.
**Priorité :** 🔴 Bloquant

---

### 4.12 Média non temporel contrôlable au clavier et au pointeur

**Texte officiel 4.12 :** La consultation de chaque *média non temporel* est-elle *contrôlable par le clavier et tout dispositif de pointage* ?
- **4.12.1** Pour chaque *média non temporel*, chaque fonctionnalité vérifie-t-elle une de ces conditions ?
  - La fonctionnalité est *accessible par le clavier et tout dispositif de pointage* ;
  - Une fonctionnalité *accessible par le clavier et tout dispositif de pointage* permettant de réaliser la même action est présente dans la page.
- **4.12.2** Pour chaque *média non temporel*, chaque fonctionnalité vérifie-t-elle une de ces conditions ?
  - La fonctionnalité est *activable par le clavier et tout dispositif de pointage* ;
  - Une fonctionnalité *activable par le clavier et tout dispositif de pointage* permettant de réaliser la même action est présente dans la page.

**Non-conformité type :** Carte en `<canvas>` qui ne se déplace qu’à la souris, sans commande ni alternative.
**Impact :** une fonctionnalité réservée à la souris reste hors d’atteinte pour la personne qui navigue au clavier.
**Priorité :** 🔴 Bloquant

---

### 4.13 Média compatible avec les technologies d’assistance

**Texte officiel 4.13 :** Chaque *média temporel* et *non temporel* est-il *compatible avec les technologies d’assistance* (hors cas particuliers) ?
- **4.13.1** Chaque *média temporel* et *non temporel* vérifie-t-il une de ces conditions (hors cas particuliers) ?
  - Le nom, le rôle, la valeur, le paramétrage et les changements d’états des composants d’interfaces sont accessibles aux technologies d’assistance via une API d’accessibilité ;
  - Une alternative *compatible avec une API d’accessibilité* permet d’accéder aux mêmes fonctionnalités.
- **4.13.2** Chaque *média temporel* et *non temporel* qui possède une alternative *compatible avec les technologies d’assistance*, vérifie-t-il une de ces conditions ?
  - L’alternative est adjacente au *média temporel* ou *non temporel* ;
  - L’alternative est accessible via un *lien ou bouton adjacent* ;
  - Un mécanisme permet de remplacer le *média temporel* ou *non temporel* par son alternative.
- *Cas particuliers :*
  - Il existe une gestion de cas particulier lorsque le *média temporel* ou *non temporel* est utilisé à des fins décoratives (c’est-à-dire qu’il n’apporte aucune information).
  - Dans ces situations, le critère est non applicable.

**Non-conformité type :** Lecteur personnalisé dont les commandes sont des `<div>` cliquables ou des icônes sans nom accessible.
**Impact :** une commande sans nom ni rôle est annoncée au lecteur d’écran, au mieux, comme un simple élément : la personne qui l’utilise ne sait pas à quoi elle sert.
**Priorité :** 🟠 Majeur

---

## Thème 5 — Tableaux (8 critères)

### 5.1–5.2 Tableau complexe : résumé présent et pertinent

**Texte officiel 5.1 :** Chaque *tableau de données complexe* a-t-il un *résumé* ?
- **5.1.1** Pour chaque *tableau de données complexe*, un *résumé* est-il disponible ?
- *Notes techniques :*
  - La spécification HTML propose plusieurs *méthodes pour lier un résumé à un tableau* (tableau lié à un passage de texte avec l’attribut `aria-describedby`, tableau groupé dans un élément `figure` avec un résumé présent dans un élément `figcaption` ou un élément `p`, résumé présent dans un élément `details` contenu dans l’élément `caption`). Ces méthodes n’ont pas un support suffisant pour être utilisées actuellement.

**Texte officiel 5.2 :** Pour chaque *tableau de données complexe* ayant un *résumé*, celui-ci est-il pertinent ?

Un tableau complexe (en-têtes multi-niveaux) nécessite un résumé expliquant sa structure. 5.1 : le résumé existe. 5.2 : il explique la structure du tableau.

**Non-conformité type :** Tableau avec en-têtes croisés sans aucun résumé de lecture.
**Impact :** sans résumé, la personne qui utilise un lecteur d’écran découvre la structure cellule par cellule et peine à comprendre comment lire le tableau.
**Priorité :** 🟠 Majeur

---

### 5.3 Tableau de mise en forme : contenu linéarisé compréhensible

**Texte officiel 5.3 :** Pour chaque *tableau de mise en forme*, le contenu linéarisé reste-t-il compréhensible ?
- **5.3.1** Chaque *tableau de mise en forme* vérifie-t-il ces conditions ?
  - Le contenu linéarisé reste compréhensible ;
  - La balise `<table>` possède un attribut `role="presentation"`.

Tableau de mise en forme : `role="presentation"` obligatoire, pas de `<th>`, `<caption>`, `<thead>`, `<tfoot>`.

**Non-conformité type :** `<table>` de mise en page sans `role="presentation"` ; utilisation de `<th>` dans un tableau de présentation.
**Impact :** sans `role="presentation"`, le lecteur d’écran annonce un tableau de données qui n’en est pas un, et fait perdre le fil du contenu.
**Priorité :** 🟠 Majeur

---

### 5.4–5.5 Titre de tableau correctement associé et pertinent

**Texte officiel 5.4 :** Pour chaque *tableau de données ayant un titre*, le titre est-il correctement associé au tableau de données ?
- **5.4.1** Pour chaque *tableau de données ayant un titre*, le titre est-il correctement associé au tableau de données ?

**Texte officiel 5.5 :** Pour chaque *tableau de données ayant un titre*, celui-ci est-il pertinent ?
- **5.5.1** Pour chaque *tableau de données ayant un titre*, ce titre permet-il d’identifier le contenu du *tableau de données* de manière claire et concise ?

Via `<caption>`, `aria-label`, `aria-labelledby` ou `title`. 5.4 : le titre est associé au tableau. 5.5 : il identifie son contenu. Ces deux critères ne visent que les tableaux qui ont un titre : un tableau sans titre est NA ici, le RGAA n’en impose pas.

**Non-conformité type :** Titre visible dans un `<p>` au-dessus du tableau, sans lien avec lui ; `<caption>Tableau 1</caption>` non descriptif.
**Impact :** un titre non associé n’est pas annoncé avec le tableau : la personne qui parcourt les tableaux au lecteur d’écran ne sait pas ce que chacun contient.
**Priorité :** 🟡 Mineur

---

### 5.6–5.7 En-têtes correctement déclarés et associés

**Texte officiel 5.6 :** Pour chaque *tableau de données*, chaque *en-tête de colonne* et chaque *en-tête de ligne* sont-ils correctement déclarés ?
- **5.6.1** Pour chaque *tableau de données*, chaque *en-tête de colonne* s’appliquant à la totalité de la colonne vérifie-t-il une de ces conditions ?
  - L’*en-tête de colonnes* est structuré au moyen d’une balise `<th>` ;
  - L’*en-tête de colonnes* est structuré au moyen d’une balise pourvue d’un attribut WAI-ARIA `role="columnheader"`.
- **5.6.2** Pour chaque *tableau de données*, chaque *en-tête de ligne* s’appliquant à la totalité de la ligne vérifie-t-il une de ces conditions ?
  - L’*en-tête de lignes* est structuré au moyen d’une balise `<th>` ;
  - L’*en-tête de lignes* est structuré au moyen d’une balise pourvue d’un attribut WAI-ARIA `role="rowheader"`.
- **5.6.3** Pour chaque *tableau de données*, chaque en-tête ne s’appliquant pas à la totalité de la ligne ou de la colonne est-il structuré au moyen d’une balise `<th>` ?
- **5.6.4** Pour chaque *tableau de données*, chaque cellule associée à plusieurs en-têtes est-elle structurée au moyen d’une balise `<td>` ou `<th>` ?

**Texte officiel 5.7 :** Pour chaque *tableau de données*, la technique appropriée permettant d’associer chaque cellule avec ses *en-têtes* est-elle utilisée (hors cas particuliers) ?
- **5.7.1** Pour chaque contenu de balise `<th>` s’appliquant à la totalité de la ligne ou de la colonne, la balise `<th>` respecte-t-elle une de ces conditions (hors cas particuliers) ?
  - La balise `<th>` possède un attribut `id` unique ;
  - La balise `<th>` possède un attribut `scope` ;
  - La balise `<th>` possède un attribut WAI-ARIA `role="rowheader"` ou `role="columnheader"`.
- **5.7.2** Pour chaque contenu de balise `<th>` s’appliquant à la totalité de la ligne ou de la colonne et possédant un attribut `scope`, la balise `<th>` vérifie-t-elle une de ces conditions ?
  - La balise `<th>` possède un attribut `scope` avec la valeur `"row"` pour les *en-têtes de ligne* ;
  - La balise `<th>` possède un attribut `scope` avec la valeur `"col"` pour les *en-têtes de colonne*.
- **5.7.3** Pour chaque contenu de balise `<th>` ne s’appliquant pas à la totalité de la ligne ou de la colonne, la balise `<th>` vérifie-t-elle ces conditions ?
  - La balise `<th>` ne possède pas d’attribut `scope` ;
  - La balise `<th>` ne possède pas d’attribut WAI-ARIA `role="rowheader"` ou `role="columnheader"` ;
  - La balise `<th>` possède un attribut `id` unique.
- **5.7.4** Pour chaque contenu de balise `<td>` ou `<th>` associée à un ou plusieurs en-têtes possédant un attribut `id`, la balise vérifie-t-elle ces conditions ?
  - La balise possède un attribut `headers` ;
  - L’attribut `headers` possède la liste des valeurs d’attribut `id` des *en-têtes* associés.
- **5.7.5** Pour chaque balise pourvue d’un attribut WAI-ARIA `role="rowheader"` ou `role="columnheader"` dont le contenu s’applique à la totalité de la ligne ou de la colonne, la balise vérifie-t-elle une de ces conditions ?
  - La balise possède un attribut WAI-ARIA `role="rowheader"` pour les *en-têtes de ligne* ;
  - La balise possède un attribut WAI-ARIA `role="columnheader"` pour les *en-têtes de colonne*.
- *Cas particuliers :*
  - Dans le cas de tableaux de données ayant des en-têtes sur une seule ligne ou une seule colonne, les en-têtes peuvent être structurés à l’aide de balise `<th>` sans attribut `scope`.
- *Notes techniques :*
  - Si l’attribut `headers` est implémenté sur une cellule déjà reliée à un en-tête (de ligne ou de colonne) avec l’attribut `scope` (avec la valeur `col` ou `row`), c’est l’en-tête ou les en-têtes référencés par l’attribut `headers` qui seront restitués aux technologies d’assistance. Les en-têtes reliés avec l’attribut `scope` seront ignorés.

- En-têtes de colonnes : `<th scope="col">`
- En-têtes de lignes : `<th scope="row">`
- Tableaux complexes : `<th id="...">` + `<td headers="...">`

5.6 : les en-têtes sont des `<th>` (ou portent le rôle correspondant). 5.7 : les cellules sont reliées à leurs en-têtes.

**Non-conformité type :** En-têtes de colonnes en `<td>` stylés en gras au lieu de `<th scope="col">` ; absence de `scope` sur les `<th>`.
**Impact :** sans en-têtes associés, le lecteur d’écran annonce les cellules sans leur en-tête de ligne ou de colonne : les données n’ont plus de sens.
**Priorité :** 🟠 Majeur

---

### 5.8 Tableau de mise en forme sans éléments de données

**Texte officiel 5.8 :** Chaque *tableau de mise en forme* ne doit pas utiliser d’éléments propres aux  *tableaux de données*. Cette règle est-elle respectée ?
- **5.8.1** Chaque *tableau de mise en forme* (balise `<table>`) vérifie-t-il ces conditions ?
  - Le tableau de mise en forme (balise `<table>`) n’a pas d’attribut `summary` (sinon vide) et ne contient pas de balises `<caption>`, `<th>`, `<thead>`, `<tfoot>` ou de balises ayant un attribut WAI-ARIA `role="rowheader"`, `role="columnheader"` ;
  - Les cellules du tableau de mise en forme (balises `<td>`) ne possèdent pas d’attributs `scope`, `headers` et `axis`.

**Non-conformité type :** `<table>` de mise en page contenant des `<th>`.
**Impact :** des éléments de tableau de données dans une mise en page font annoncer des en-têtes et un titre sans objet au lecteur d’écran.
**Priorité :** 🟠 Majeur

---

## Thème 6 — Liens (2 critères)

### 6.1 Chaque lien est-il explicite ?

**Texte officiel 6.1 :** Chaque *lien* est-il explicite (hors cas particuliers) ?
- **6.1.1** Chaque *lien texte* vérifie-t-il une de ces conditions (hors cas particuliers) ?
  - L’*intitulé de lien* seul permet d’en comprendre la fonction et la destination ;
  - L’*intitulé de lien* additionné au *contexte du lien* permet d’en comprendre la fonction et la destination.
- **6.1.2** Chaque *lien image* vérifie-t-il une de ces conditions (hors cas particuliers) ?
  - L’*intitulé de lien* seul permet d’en comprendre la fonction et la destination ;
  - L’*intitulé de lien* additionné au *contexte du lien* permet d’en comprendre la fonction et la destination.
- **6.1.3** Chaque *lien composite* vérifie-t-il une de ces conditions (hors cas particuliers) ?
  - L’*intitulé de lien* seul permet d’en comprendre la fonction et la destination ;
  - L’*intitulé de lien* additionné au *contexte du lien* permet d’en comprendre la fonction et la destination.
- **6.1.4** Chaque *lien SVG* vérifie-t-il une de ces conditions (hors cas particuliers) ?
  - L’*intitulé de lien* seul permet d’en comprendre la fonction et la destination ;
  - L’*intitulé de lien* additionné au *contexte du lien* permet d’en comprendre la fonction et la destination.
- **6.1.5** Pour chaque *lien* ayant un *intitulé visible*, le *nom accessible du lien* contient-il au moins l’*intitulé visible* (hors cas particuliers) ?
- *Cas particuliers :*
  - Il existe une gestion de cas particuliers pour les tests 6.1.1, 6.1.2, 6.1.3 et 6.1.4 lorsque le lien est *ambigu pour tout le monde*. Dans cette situation, où il n’est pas possible de rendre le lien explicite dans son contexte, le critère est non applicable.
  - Il existe une gestion de cas particuliers pour le test 6.1.5 lorsque :
    - - La ponctuation et les lettres majuscules sont présentes dans le texte de l’*intitulé visible* : elles peuvent être ignorées dans le nom accessible sans porter à conséquence ;
    - - Le texte de l’*intitulé visible* sert de symbole : le texte ne doit pas être interprété littéralement au niveau du nom accessible. Le nom doit exprimer la fonction véhiculée par le symbole (par exemple, “B” au niveau d’un éditeur de texte aura pour nom accessible “Mettre en gras”, le signe “>” en fonction du contexte signifiera “Suivant” ou “Lancer la vidéo”). Le cas des symboles mathématiques fait cependant exception (voir la note ci-dessous).
  - Note : si l’étiquette visible représente une expression mathématique, les symboles mathématiques peuvent être repris littéralement pour servir d’étiquette au nom accessible (ex. : “A>B”). Il est laissé à l’utilisateur le soin d’opérer la correspondance entre l’expression et ce qu’il doit épeler compte tenu de la connaissance qu’il a du fonctionnement de son logiciel de saisie vocale (“A plus grand que B” ou “A supérieur à B”).
- *Notes techniques :*
  - Lorsque l’intitulé visible est complété par une autre expression dans le nom accessible :
    - - WCAG insiste sur le placement de l’intitulé visible au début du nom accessible sans toutefois réserver l’exclusivité de cet emplacement ;
    - - WCAG considère comme un cas d’échec une correspondance non exacte de la chaîne de caractères de l’intitulé visible au sein du nom accessible.
  - Par exemple, si l’on considère l’intitulé visible « Commander maintenant » complété dans le nom accessible par l’expression « produit X », on peut avoir les différents cas suivants :
    - - « Commander maintenant produit X » est valide (bonne pratique) ;
    - - « Produit X : commander maintenant » est valide ;
    - - « Commander produit X maintenant » est non valide.

L'intitulé du lien (seul ou avec son contexte) doit permettre de comprendre sa fonction et sa destination.

**Contexte valide :** phrase englobante, paragraphe, élément de liste, titre précédent, cellule d'en-tête de tableau.

**Non-conformité type :** `<a href="/rapport">En savoir plus</a>` sans contexte permettant de comprendre de quel rapport il s'agit.
**Impact :** dans la liste des liens du lecteur d’écran, des intitulés comme « Cliquez ici » se ressemblent tous : la destination reste inconnue tant que le texte autour n’a pas été lu.
**Priorité :** 🟠 Majeur

---

### 6.2 Chaque lien a-t-il un intitulé ?

**Texte officiel 6.2 :** Dans chaque page web, chaque *lien* a-t-il un *intitulé* ?
- **6.2.1** Dans chaque page web, chaque *lien* a-t-il un *intitulé* entre `<a>` et `</a>` ?
- *Notes techniques :*
  - Une ancre n’est pas un lien même si pendant longtemps l’élément `<a>` a servi de support à cette technique. Elle n’est donc pas concernée par le présent critère.

Tout lien (`<a href>` ou `role="link"`) doit contenir un intitulé : du texte, éventuellement masqué visuellement, ou l’alternative d’une image.

**Non-conformité type :** `<a href="/page"><svg>...</svg></a>` sans `aria-label` ni texte.
**Impact :** un lien sans intitulé est annoncé par son adresse, ou sans rien : la personne qui utilise un lecteur d’écran ne sait pas où il mène.
**Priorité :** 🔴 Bloquant

---

## Thème 7 — Scripts (5 critères)

### 7.1 Script compatible avec les technologies d'assistance

**Texte officiel 7.1 :** Chaque *script* est-il, si nécessaire, *compatible avec les technologies d’assistance* ?
- **7.1.1** Chaque *script* qui génère ou contrôle un *composant d’interface* vérifie-t-il, si nécessaire, une de ces conditions ?
  - Le *nom, le rôle, la valeur, le paramétrage et les changements d’états* sont accessibles aux technologies d’assistance via une API d’accessibilité ;
  - Un *composant d’interface* accessible permettant d’accéder aux mêmes fonctionnalités est présent dans la page ;
  - Une *alternative* accessible permet d’accéder aux mêmes fonctionnalités.
- **7.1.2** Chaque *script* qui génère ou contrôle un *composant d’interface* respecte-t-il une de ces conditions ?
  - Le *composant d’interface* est *correctement restitué* par les technologies d’assistance ;
  - Une *alternative* accessible permet d’accéder aux mêmes fonctionnalités.
- **7.1.3** Chaque *script* qui génère ou contrôle un *composant d’interface* vérifie-t-il ces conditions (hors cas particuliers) ?
  - Le composant possède un nom pertinent ;
  - Le nom accessible du composant contient au moins l’*intitulé visible* ;
  - Le composant possède un rôle pertinent.
- *Cas particuliers :*
  - Il existe une gestion de cas particuliers pour le test 7.1.3 lorsque :
    - - La ponctuation et les lettres majuscules sont présentes dans le texte de l’intitulé visible : elles peuvent être ignorées dans le nom accessible sans porter à conséquence ;
    - - Le texte de l’intitulé visible sert de symbole : le texte ne doit pas être interprété littéralement au niveau du nom accessible. Le nom doit exprimer la fonction véhiculée par le symbole (par exemple, “B” au niveau d’un éditeur de texte aura pour nom accessible “Mettre en gras”, le signe “>” en fonction du contexte signifiera “Suivant” ou “Lancer la vidéo”). Le cas des symboles mathématiques fait cependant exception (voir la note ci-dessous).
  - Note : si l’étiquette visible représente une expression mathématique, les symboles mathématiques peuvent être repris littéralement pour servir d’étiquette au nom accessible (ex. : “A>B”). Il est laissé à l’utilisateur le soin d’opérer la correspondance entre l’expression et ce qu’il doit épeler compte tenu de la connaissance qu’il a du fonctionnement de son logiciel de saisie vocale (“A plus grand que B” ou “A supérieur à B”).
- *Notes techniques :*
  - Le critère 7.1 implémente la notion de « compatible avec les technologies d’assistance » telle que définie par les WCAG, ainsi que le recours à WAI-ARIA pour rendre un composant ou une fonctionnalité accessible. Le bon usage de WAI-ARIA est vérifié via les tests 7.1.1, 7.1.2, 7.1.3.
  - Note importante : dans un environnement HTML5, beaucoup de composants peuvent nécessiter JavaScript pour fonctionner ; en conséquence la fourniture d’une alternative à un composant JavaScript qui ne pourrait pas être rendu accessible devra bénéficier d’une méthode spécifique au composant en cause, permettant de le remplacer par une alternative accessible (et de le réactiver). Cela signifie que la désactivation de JavaScript pour l’ensemble de la page ne sera pas acceptée comme une méthode valable, à moins qu’elle ne remette pas en cause l’utilisation des autres composants.

Tout composant généré par script doit exposer : nom, rôle, valeur, paramétrage et changements d'états via l'API d'accessibilité.

**Non-conformité type :** Accordéon custom sans `aria-expanded` sur le bouton ; menu déroulant sans `aria-haspopup` ; liste `role="listbox"` sans nom accessible.
**Impact :** un composant sans rôle, sans nom ou sans état annoncé ne dit rien au lecteur d’écran : la personne qui l’utilise ne sait ni ce qu’il fait, ni s’il est ouvert.
**Priorité :** 🟠 Majeur

---

### 7.2 Alternative pertinente au script

**Texte officiel 7.2 :** Pour chaque *script* ayant une *alternative*, cette alternative est-elle pertinente ?
- **7.2.1** Chaque *script* débutant par la balise `<script>` et ayant une *alternative* vérifie-t-il une de ces conditions ?
  - L’*alternative* entre `<noscript>` et `</noscript>` permet d’accéder à des contenus et des fonctionnalités similaires ;
  - La page affichée, lorsque JavaScript est désactivé, permet d’accéder à des contenus et des fonctionnalités similaires ;
  - La page alternative permet d’accéder à des contenus et des fonctionnalités similaires ;
  - Le langage de script côté serveur permet d’accéder à des contenus et des fonctionnalités similaires ;
  - L’alternative présente dans la page permet d’accéder à des contenus et des fonctionnalités similaires.
- **7.2.2** Chaque élément non textuel mis à jour par un *script* (dans la page, ou dans un *cadre*) et ayant une *alternative* vérifie-t-il ces conditions ?
  - L’alternative de l’élément non textuel est mise à jour ;
  - L’alternative mise à jour est pertinente.

Le critère ne porte que sur les scripts qui ont une alternative : elle doit donner accès à des contenus et à des fonctionnalités similaires. Un script sans alternative relève des autres critères du thème (NA ici) : le RGAA n’exige pas de fonctionnement sans JavaScript.

**Non-conformité type :** `<noscript>` vide ; alternative qui ne donne accès qu’à une partie de la fonctionnalité.
**Impact :** une alternative vide ou partielle laisse sans solution la personne qui en dépend, parce que le script ne fonctionne pas dans son environnement.
**Priorité :** 🟠 Majeur

---

### 7.3 Script contrôlable au clavier et au pointeur

**Texte officiel 7.3 :** Chaque *script* est-il *contrôlable par le clavier et par tout dispositif de pointage* (hors cas particuliers) ?
- **7.3.1** Chaque élément possédant un gestionnaire d’événement contrôlé par un script vérifie-t-il une de ces conditions (hors cas particuliers) ?
  - L’élément est *accessible par le clavier et tout dispositif de pointage* ;
  - Un élément *accessible par le clavier et tout dispositif de pointage* permettant de réaliser la même action est présent dans la page.
- **7.3.2** Un *script* ne doit pas supprimer le focus d’un élément qui le reçoit. Cette règle est-elle respectée (hors cas particuliers) ?
- *Cas particuliers :*
  - Il existe une gestion de cas particuliers lorsque la fonctionnalité dépend de l’utilisation d’un gestionnaire d’événement sans équivalent universel ; par exemple, une application de dessin à main levée ne pourra pas être rendue contrôlable au clavier. Dans ces situations, le critère est non applicable.

Tout élément interactif créé par script doit être focusable et activable au clavier et au pointeur, à moins qu’un autre élément accessible de ces deux façons réalise la même action dans la page.

**Non-conformité type :** `<div onClick={handleClick}>Action</div>` non focusable ; composant React custom non opérable au clavier.
**Impact :** une action réservée à la souris est inaccessible à la personne qui navigue au clavier, avec une commande vocale ou un contacteur.
**Priorité :** 🔴 Bloquant

---

### 7.4 Changement de contexte : utilisateur averti ou en contrôle

**Texte officiel 7.4 :** Pour chaque *script* qui initie un *changement de contexte*, l’utilisateur est-il averti ou en a-t-il le contrôle ?
- **7.4.1** Chaque *script* qui initie un *changement de contexte* vérifie-t-il une de ces conditions ?
  - L’utilisateur est averti par un texte de l’action du script et du type de changement avant son déclenchement ;
  - Le changement de contexte est initié par un bouton (input de type `submit`, `button` ou `image` ou balise `<button>`) explicite ;
  - Le changement de contexte est initié par un lien explicite.

Un script qui initie un changement de contexte doit être déclenché par un bouton ou un lien explicite, ou annoncé avant par un texte qui décrit l’action et le type de changement.

Un changement de contexte modifie l’agent utilisateur, la zone de restitution, le focus, ou un contenu qui change la signification de la page. Un changement de contenu n’en est pas toujours un : déployer un menu ou une arborescence n’en est pas un.

**Non-conformité type :** Navigation ou soumission automatique au changement de valeur d'un `<select>`, sans bouton de validation ni texte qui l’annonce. La simple mise à jour d’un détail secondaire de la page n’en est pas une.
**Impact :** un changement sans avertissement désoriente la personne qui ne voit pas toute la page, au lecteur d’écran ou en fort zoom : elle ne comprend pas ce qui vient de changer.
**Priorité :** 🟠 Majeur

---

### 7.5 Messages de statut restitués

**Texte officiel 7.5 :** Dans chaque page web, les *messages de statut* sont-ils correctement restitués par les technologies d’assistance ?
- **7.5.1** Chaque *message de statut* qui informe de la réussite, du résultat d’une action ou bien de l’état d’une application utilise-t-il l’attribut WAI-ARIA `role="status"` ?
- **7.5.2** Chaque *message de statut* qui présente une suggestion, ou avertit de l’existence d’une erreur utilise-t-il l’attribut WAI-ARIA `role="alert"` ?
- **7.5.3** Chaque *message de statut* qui indique la progression d’un processus utilise-t-il l’un des attributs WAI-ARIA `role="log"`, `role="progressbar"` ou `role="status"` ?
- *Notes techniques :*
  - Les rôles WAI-ARIA `log`, `status` et `alert` ont implicitement une valeur d’attribut WAI-ARIA `aria-live` et `aria-atomic`. On pourra donc considérer (conformément à la spécification WAI-ARIA 1.1) que :
    - - Un attribut WAI-ARIA `aria-live="polite"` associé à un message de statut peut valoir pour un rôle WAI-ARIA `log` ;
    - - Un attribut WAI-ARIA `aria-live="polite"` et un attribut WAI-ARIA `aria-atomic="true"` associés à un message de statut peuvent valoir pour un rôle WAI-ARIA `status` ;
    - - Un attribut WAI-ARIA `aria-live="assertive"` et un attribut WAI-ARIA `aria-atomic="true"` associés à un message de statut peuvent valoir pour un rôle WAI-ARIA `alert`.
  - C’est sous réserve que la nature du message de statut satisfasse bien à la correspondance implicitement établie. Dans le cas d’un message de statut indiquant la progression d’un processus et matérialisé graphiquement par une barre de progression, un rôle WAI-ARIA `progressbar` explicite est nécessaire.

| Type de message | Attribut ARIA |
|---|---|
| Succès, résultat d'action | `role="status"` ou `aria-live="polite" aria-atomic="true"` |
| Erreur, avertissement | `role="alert"` ou `aria-live="assertive" aria-atomic="true"` |
| Progression | `role="progressbar"` ou `role="log"` ou `role="status"` |

**Non-conformité type :** Message de confirmation "Formulaire envoyé" apparaissant visuellement mais sans `role="status"` ni `aria-live`.
**Impact :** une confirmation, une erreur ou un résultat de recherche apparaît à l’écran sans être annoncé : la personne qui utilise un lecteur d’écran ne sait pas que quelque chose a changé.
**Priorité :** 🟠 Majeur

