# RGAA — Thème 11 : Formulaires (13 critères)

## 11.1 Chaque champ a une étiquette

**Texte officiel 11.1 :** Chaque *champ de formulaire* a-t-il une *étiquette* ?
- **11.1.1** Chaque *champ de formulaire* vérifie-t-il une de ces conditions ?
  - Le *champ de formulaire* possède un attribut WAI-ARIA `aria-labelledby` référençant un *passage de texte* identifié ;
  - Le *champ de formulaire* possède un attribut WAI-ARIA `aria-label` ;
  - Une balise `<label>` ayant un attribut `for` est associée au *champ de formulaire* ;
  - Le *champ de formulaire* possède un attribut `title` ;
  - Un bouton adjacent au *champ de formulaire* lui fournit une étiquette visible et un élément `<label>` visuellement caché ou un attribut WAI-ARIA `aria-label`, `aria-labelledby` ou `title` lui fournit un nom accessible.
- **11.1.2** Chaque *champ de formulaire* associé à une balise `<label>` ayant un attribut `for`, vérifie-t-il ces conditions ?
  - Le *champ de formulaire* possède un attribut `id` ;
  - La valeur de l’attribut `for` est égale à la valeur de l’attribut `id` du *champ de formulaire* associé.
- **11.1.3** Chaque *champ de formulaire* ayant une *étiquette* dont le contenu n’est pas visible ou à proximité (masqué, `aria-label`) ou qui n’est pas *accolé* au champ (`aria-labelledby`), vérifie-t-il une de ses conditions ?
  - Le *champ de formulaire* possède un attribut `title` dont le contenu permet de comprendre la nature de la saisie attendue ;
  - Le *champ de formulaire* est accompagné d’un *passage de texte* accolé au champ qui devient visible à la prise de focus permettant de comprendre la nature de la saisie attendue ;
  - Le *champ de formulaire* est accompagné d’un *passage de texte* visible accolé au champ permettant de comprendre la nature de la saisie attendue.

Chaque champ de formulaire doit avoir une étiquette associée via (ordre de priorité) :
1. `aria-labelledby` référençant un passage de texte
2. `aria-label`
3. `<label for="id">` associé au champ
4. `title`

**Non-conformité type :** `<input type="text" placeholder="Votre nom">` sans `<label>`, ni `aria-label`.
**Impact :** sans étiquette programmatique, le lecteur d'écran annonce une zone de saisie sans intitulé : la personne qui l'utilise ne sait pas quelle donnée renseigner. Saisie bloquée.
**Priorité :** 🔴 Bloquant

---

## 11.2 Étiquette pertinente

**Texte officiel 11.2 :** Chaque *étiquette* associée à un *champ de formulaire* est-elle pertinente (hors cas particuliers) ?
- **11.2.1** Chaque balise `<label>` permet-elle de connaître la fonction exacte du *champ de formulaire* auquel elle est associée ?
- **11.2.2** Chaque attribut `title` permet-il de connaître la fonction exacte du *champ de formulaire* auquel il est associé ?
- **11.2.3** Chaque étiquette implémentée via l’attribut WAI-ARIA `aria-label` permet-elle de connaître la fonction exacte du *champ de formulaire* auquel elle est associée ?
- **11.2.4** Chaque *passage de texte* associé via l’attribut WAI-ARIA `aria-labelledby` permet-il de connaître la fonction exacte du *champ de formulaire* auquel il est associé ?
- **11.2.5** Chaque *champ de formulaire* ayant un *intitulé visible* vérifie-t-il ces conditions (hors cas particuliers) ?
  - S’il est présent, le contenu de l’attribut WAI-ARIA `aria-label` du *champ de formulaire* contient au moins l’*intitulé visible* ;
  - S’il est présent, le *passage de texte* lié au *champ de formulaire* via un attribut WAI-ARIA `aria-labelledby` contient au moins l’*intitulé visible* ;
  - S’il est présent, le contenu de l’attribut `title` du *champ de formulaire* contient au moins l’*intitulé visible* ;
  - S’il est présent le contenu de la balise `<label>` associé au *champ de formulaire* contient au moins l’*intitulé visible*.
- **11.2.6** Chaque bouton adjacent au *champ de formulaire* qui fournit une étiquette visible permet-il de connaître la fonction exacte du *champ de formulaire* auquel il est associé ?
- *Cas particuliers :*
  - Il existe une gestion de cas particuliers pour le test 11.2.5 lorsque :
    - - La ponctuation et les lettres majuscules sont présentes dans le texte de l’*intitulé visible* : elles peuvent être ignorées dans le nom accessible sans porter à conséquence ;
    - - Le texte de l’*intitulé visible* sert de symbole : le texte ne doit pas être interprété littéralement au niveau du nom accessible. Le nom doit exprimer la fonction véhiculée par le symbole (par exemple, “B” au niveau d’un éditeur de texte aura pour nom accessible “Mettre en gras”, le signe “>” en fonction du contexte signifiera “Suivant” ou “Lancer la vidéo”). Le cas des symboles mathématiques fait cependant exception (voir la note ci-dessous).
  - Note : si l’étiquette visible représente une expression mathématique, les symboles mathématiques peuvent être repris littéralement pour servir d’étiquette au nom accessible (ex. : “A>B”). Il est laissé à l’utilisateur le soin d’opérer la correspondance entre l’expression et ce qu’il doit épeler compte tenu de la connaissance qu’il a du fonctionnement de son logiciel de saisie vocale (“A plus grand que B” ou “A supérieur à B”).
  - Ce cas particulier s’applique également au test 11.9.2.

L'étiquette doit permettre de comprendre la fonction exacte du champ. Si un intitulé visible existe, le nom accessible doit le contenir.

**Non-conformité type :** `<label>Saisir :</label>` ; `aria-label="field1"` alors que le label visible dit "Adresse email".
**Impact :** un intitulé vague, restitué hors contexte dans la liste des champs du lecteur d'écran, ne permet pas de savoir quelle donnée renseigner.
**Priorité :** 🟠 Majeur

---

## 11.3 Étiquettes cohérentes

**Texte officiel 11.3 :** Dans chaque *formulaire*, chaque *étiquette* associée à un *champ de formulaire* ayant la même fonction et répétée plusieurs fois dans une même page ou dans un *ensemble de pages* est-elle *cohérente* ?

Les champs de même fonction (ex: "Email" dans formulaire de contact et d'inscription) doivent avoir des étiquettes formulées de manière cohérente.

**Non-conformité type :** "Adresse email" sur une page, "Courriel" sur une autre pour le même type de champ.
**Impact :** des intitulés divergents pour une même donnée d'un formulaire à l'autre obligent à se demander s’il s’agit de la même information : la personne qui s’appuie sur des repères constants pour remplir un formulaire perd ces repères.
**Priorité :** 🟡 Mineur

> Pas de correction locale : critère trans-pages. Harmoniser les libellés à l'échelle du site (centraliser dans les locales i18n côté Rails, dans un dictionnaire de libellés côté React).

---

## 11.4 Étiquette et champ accolés

**Texte officiel 11.4 :** Dans chaque *formulaire*, chaque *étiquette de champ* et son champ associé sont-ils *accolés* (hors cas particuliers) ?

- Champs texte/select : étiquette au-dessus ou à gauche
- Checkbox/radio : étiquette en-dessous ou à droite

**Non-conformité type :** Label en haut de page référençant un champ en bas de page ; label séparé du champ par un autre élément.
**Impact :** un label éloigné de son champ rompt l'association, notamment en agrandissement (zoom 200 %, loupe) où l'on perd le lien visuel entre les deux.
**Priorité :** 🟠 Majeur

---

## 11.5–11.7 Regroupement de champs

**Texte officiel 11.5 :** Dans chaque *formulaire*, les *champs de même nature* sont-ils regroupés, si nécessaire ?
- **11.5.1** Les *champs de même nature* vérifient-ils l’une de ces conditions, si nécessaire ?
  - Les *champs de même nature* sont regroupés dans une balise `<fieldset>` ;
  - Les *champs de même nature* sont regroupés dans une balise possédant un attribut WAI-ARIA `role="group"` ;
  - Les *champs de même nature* de type radio (`<input type="radio">`) ou balises possédant un attribut WAI-ARIA `role="radio"`) sont regroupés dans une balise possédant un attribut WAI-ARIA `role="radiogroup"` ou `role="group"`.

**Texte officiel 11.6 :** Dans chaque *formulaire*, chaque regroupement de *champs de même nature* a-t-il une *légende* ?
- **11.6.1** Chaque regroupement de *champs de même nature* possède-t-il une *légende* ?

**Texte officiel 11.7 :** Dans chaque *formulaire*, chaque *légende* associée à un regroupement de *champs de même nature* est-elle pertinente ?
- **11.7.1** Chaque *légende* associée à un regroupement de *champs de même nature* est-elle pertinente ?

Regrouper les champs de même nature avec `<fieldset>` + `<legend>`.

**Non-conformité type :** Groupe de boutons radio sans `<fieldset>` ; groupe de champs d'adresse sans légende de groupe.
**Impact :** sans `fieldset`/`legend`, le groupe est restitué champ par champ sans son intitulé commun : on ne sait pas à quelle question le choix se rapporte.
**Priorité :** 🟠 Majeur

---

## 11.8 Items de liste de choix regroupés

**Texte officiel 11.8 :** Dans chaque *formulaire*, les *items de même nature d’une liste de choix* sont-ils regroupés de manière pertinente ?
- **11.8.1** Pour chaque balise `<select>`, les *items de même nature d’une liste de choix* sont-ils regroupés avec une balise `<optgroup>`, si nécessaire ?
- **11.8.2** Dans chaque balise `<select>`, chaque balise `<optgroup>` possède-t-elle un attribut `label` ?
- **11.8.3** Pour chaque balise `<optgroup>` ayant un attribut `label`, le contenu de l’attribut `label` est-il pertinent ?
- *Notes techniques :*
  - Il est possible d’utiliser une balise ayant un attribut WAI-ARIA `role="listbox"` en remplacement d’une balise `<select>`. En revanche, il est impossible de créer des groupes d’options via l’utilisation de WAI-ARIA. De ce fait, une liste nécessitant un regroupement d’options structurée à l’aide d’une balise ayant un attribut WAI-ARIA `role="listbox"` sera considérée comme non conforme au critère 11.8.

**Non-conformité type :** `<select>` avec 20+ options sans aucun `<optgroup>` alors que les options relèvent de catégories distinctes.
**Impact :** une longue liste sans regroupement allonge la navigation et alourdit la charge cognitive, surtout au clavier ou au lecteur d'écran.
**Priorité :** 🟡 Mineur

---

## 11.9 Intitulé de bouton pertinent

**Texte officiel 11.9 :** Dans chaque *formulaire*, l’intitulé de chaque *bouton* est-il pertinent (hors cas particuliers) ?
- **11.9.1** L’intitulé de chaque *bouton* vérifie-t-il ces conditions (hors cas particuliers) ?
  - S’il est présent, le contenu de l’attribut WAI-ARIA `aria-label` est pertinent ;
  - S’il est présent, le *passage de texte* lié au bouton via un attribut WAI-ARIA `aria-labelledby` est pertinent ;
  - S’il est présent, le contenu de l’attribut `value` d’une balise `<input>` de type `submit`, `reset` ou `button` est pertinent ;
  - S’il est présent, le contenu de la balise `<button>` est pertinent ;
  - S’il est présent, le contenu de l’attribut `alt` d’une balise `<input>` de type `image` est pertinent ;
  - S’il est présent, le contenu de l’attribut `title` est pertinent.
- **11.9.2** Chaque *bouton* affichant un *intitulé visible* vérifie-t-il ces conditions (hors cas particuliers) ?
  - S’il est présent, le contenu de l’attribut WAI-ARIA `aria-label `contient au moins l’*intitulé visible* ;
  - S’il est présent, le *passage de texte* lié au bouton via un attribut WAI-ARIA `aria-labelledby` contient au moins l’*intitulé visible* ;
  - S’il est présent, le contenu de l’attribut value d’une balise `<input>` de type `submit`, `reset` ou `button` contient au moins l’*intitulé visible* ;
  - S’il est présent, le contenu de la balise `<button>` contient au moins l’*intitulé visible* ;
  - S’il est présent, le contenu de l’attribut `alt` d’une balise `<input>` de type `image` contient au moins l’*intitulé visible* ;
  - S’il est présent, le contenu de l’attribut `title` contient au moins l’*intitulé visible*.
- *Cas particuliers :*
  - Pour le test 11.9.2, voir cas particuliers critère 11.2.

Chaque bouton doit avoir un intitulé décrivant son action.

**Non-conformité type :** `<button>OK</button>` ; `<button>Envoyer</button>` quand plusieurs formulaires sont présents sur la page.
**Impact :** un intitulé vague restitué hors contexte (« OK », « Envoyer ») ne dit pas quelle action sera déclenchée.
**Priorité :** 🟠 Majeur

---

## 11.10 Contrôle de saisie

**Texte officiel 11.10 :** Dans chaque *formulaire*, le *contrôle de saisie* est-il utilisé de manière pertinente (hors cas particuliers) ?
- **11.10.1** Les *indications du caractère obligatoire* de la saisie des champs vérifient-elles une de ces conditions (hors cas particuliers) ?
  - Une *indication de champ obligatoire* est visible et permet d’identifier nommément le champ concerné préalablement à la validation du formulaire ;
  - Le champ obligatoire dispose de l’attribut `aria-required="true"` ou `required` préalablement à la validation du formulaire.
- **11.10.2** Les champs obligatoires ayant l’attribut `aria-required="true"` ou `required` vérifient-ils une de ces conditions ?
  - Une *indication de champ obligatoire* est visible et située dans l’étiquette associée au champ préalablement à la validation du formulaire ;
  - Une *indication de champ obligatoire* est visible et située dans le *passage de texte* associé au champ préalablement à la validation du formulaire.
- **11.10.3** Les messages d’erreur indiquant l’absence de saisie d’un champ obligatoire vérifient-ils une de ces conditions ?
  - Le message d’erreur indiquant l’absence de saisie d’un champ obligatoire est visible et permet d’identifier nommément le champ concerné ;
  - Le champ obligatoire dispose de l’attribut `aria-invalid="true"`.
- **11.10.4** Les champs obligatoires ayant l’attribut `aria-invalid="true"` vérifient-ils une de ces conditions ?
  - Le message d’erreur indiquant le caractère invalide de la saisie est visible et situé dans l’étiquette associée au champ ;
  - Le message d’erreur indiquant le caractère invalide de la saisie est visible et situé dans le *passage de texte* associé au champ.
- **11.10.5** Les instructions et indications du type de données et/ou de format obligatoires vérifient-elles une de ces conditions ?
  - Une instruction ou une indication du type de données et/ou de format obligatoire est visible et permet d’identifier nommément le champ concerné préalablement à la validation du formulaire ;
  - Une instruction ou une indication du type de données et/ou de format obligatoire est visible dans l’étiquette ou le *passage de texte* associé au champ préalablement à la validation du formulaire.
- **11.10.6** Les messages d’erreurs fournissant une instruction ou une indication du type de données et/ou de format obligatoire des champs vérifient-ils une de ces conditions ?
  - Le message d’erreur fournissant une instruction ou une indication du type de données et/ou de format obligatoires est visible et identifie le champ concerné ;
  - Le champ dispose de l’attribut `aria-invalid="true"`.
- **11.10.7** Les champs ayant l’attribut `aria-invalid="true"` dont la saisie requiert un type de données et/ou de format obligatoires vérifient-ils une de ces conditions ?
  - Une instruction ou une indication du type de données et/ou de format obligatoire est visible et située dans la balise `<label>` associée au champ ;
  - Une instruction ou une indication du type de données et/ou de format obligatoire est visible et située dans le *passage de texte* associé au champ.
- *Cas particuliers :*
  - Le test 11.10.1 et le test 11.10.2 seront considérés comme non applicables lorsque le formulaire comporte un seul *champ de formulaire* ou qu’il indique les champs optionnels de manière :
    - - Visible ;
    - - Dans la balise `<label>` ou dans la *légende* associée au champ.
  - Dans le cas où l’ensemble des champs d’un formulaire sont obligatoires, les tests 11.10.1 et 11.10.2 restent applicables.
- *Notes techniques :*
  - Dans un long formulaire dont la majorité des champs sont obligatoires, on pourrait constater que ce sont les quelques champs restés facultatifs qui sont explicitement signalés comme tels. Dans ce cas, il faudrait s’assurer que :
    - - Un message précise visuellement en haut de formulaire que “tous les champs sont obligatoires sauf ceux indiqués comme étant facultatifs” ;
    - - Une mention “facultatif” est présente visuellement dans le libellé des champs facultatifs ou dans la légende d’un groupe de champs facultatifs ;
    - - Un attribut `required` ou `aria-required="true"` reste associé à chaque champ qui n’est pas concerné par ce caractère facultatif.

### Champs obligatoires

**Non-conformité type :** Champ obligatoire sans `required` ; obligation signalée visuellement (couleur seule) sans attribut ARIA.
**Impact :** une obligation signalée par la seule couleur n'est ni restituée par le lecteur d'écran, ni perçue quand cette couleur ne se distingue pas ; l'envoi échoue sans qu'on sache quel champ compléter.
**Priorité :** 🔴 Bloquant

### Messages d'erreur

**Non-conformité type :** Message d'erreur visible mais pas lié au champ via `aria-describedby` ; `aria-invalid` absent.
**Impact :** un message d'erreur non rattaché au champ n'est pas restitué au bon endroit par le lecteur d'écran : la personne qui l'utilise ne sait pas quel champ corriger ni pourquoi.
**Priorité :** 🔴 Bloquant

### Indications de format

**Non-conformité type :** Champ de date sans indication du format attendu (JJ/MM/AAAA).
**Impact :** sans indication de format en amont, la contrainte n'est découverte qu'après l'erreur, ce qui multiplie les tentatives ; chaque nouvel essai coûte davantage à la personne qui dicte sa saisie ou qui a besoin de consignes explicites.
**Priorité :** 🟠 Majeur

---

## 11.11 Suggestions de correction

**Texte officiel 11.11 :** Dans chaque *formulaire*, le *contrôle de saisie* est-il accompagné, si nécessaire, de suggestions facilitant la correction des erreurs de saisie ?
- **11.11.1** Pour chaque erreur de saisie, les types et les formats de données sont-ils suggérés, si nécessaire ?
- **11.11.2** Pour chaque erreur de saisie, des exemples de valeurs attendues sont-ils suggérés, si nécessaire ?
- *Notes techniques :*
  - Certains types de contrôles en HTML5 proposent des messages d’aide à la saisie automatique : par exemple le type `email` affiche un message du type « veuillez saisir une adresse e-mail valide » dans le cas où l’adresse e-mail saisie ne correspond pas au format attendu. Ces messages sont personnalisables via l’API Constraint Validation, ce qui permet de personnaliser les messages d’erreur et de valider le critère. L’attribut `pattern` permet d’effectuer automatiquement des contrôles de format (via des expressions régulières) et affiche un message d’aide personnalisable via l’attribut `title` : ce dispositif valide également le critère.

En cas d'erreur, suggérer le type de données attendu et donner un exemple.

**Non-conformité type :** Message "Format invalide" sans préciser le format attendu.
**Impact :** une erreur sans piste de correction (« Format invalide ») laisse la personne sans moyen de savoir comment corriger.
**Priorité :** 🟠 Majeur

---

## 11.12 Données modifiables/récupérables (conséquences financières/juridiques)

**Texte officiel 11.12 :** Pour chaque *formulaire* qui modifie ou supprime des données, ou qui transmet des réponses à un test ou à un examen, ou dont la validation a des conséquences financières ou juridiques, les données saisies peuvent-elles être modifiées, mises à jour ou récupérées par l’utilisateur ?
- **11.12.1** Pour chaque formulaire qui modifie ou supprime des données, ou qui transmet des réponses à un test ou un examen, ou dont la validation a des conséquences financières ou juridiques, la saisie des données vérifie-t-elle une de ces conditions ?
  - L’utilisateur peut *modifier ou annuler les données et les actions effectuées* sur ces données après la validation du formulaire ;
  - L’utilisateur peut vérifier et corriger les données avant la validation d’un formulaire en plusieurs étapes ;
  - Un mécanisme de confirmation explicite, via une case à cocher (balise `<input>` de type `checkbox` ou balise ayant un attribut WAI-ARIA `role="checkbox"`) ou une étape supplémentaire, est présent.
- **11.12.2** Chaque formulaire dont la validation modifie ou supprime des données à caractère financier, juridique ou personnel vérifie-t-il une de ces conditions ?
  - Un mécanisme permet de récupérer les données supprimées ou modifiées par l’utilisateur ;
  - Un mécanisme de demande de confirmation explicite de la suppression ou de la modification, via un *champ de formulaire* ou une étape supplémentaire, est proposé.

Pour les formulaires avec conséquences financières, juridiques ou de suppression :
- Permettre de modifier/annuler après validation
- OU étape de vérification/confirmation avant envoi
- OU case à cocher de confirmation explicite

**Non-conformité type :** Formulaire de paiement sans étape de confirmation ni possibilité d'annulation.
**Impact :** une action irréversible sans étape de vérification expose à des conséquences lourdes (paiement, suppression) en cas d'erreur de manipulation — tremblements, fatigue, restitution partielle.
**Priorité :** 🔴 Bloquant

---

## 11.13 Autocomplete pour les champs utilisateur

**Texte officiel 11.13 :** La finalité d’un champ de saisie peut-elle être déduite pour faciliter le remplissage automatique des champs avec les données de l’utilisateur ?
- **11.13.1** Chaque *champ de formulaire* dont l’objet se rapporte à une information concernant l’utilisateur vérifie-t-il ces conditions ?
  - Le *champ de formulaire* possède un attribut `autocomplete `;
  - L’attribut `autocomplete` est pourvu d’une valeur présente dans la *liste des valeurs possibles pour l’attribut `autocomplete`* associés à un *champ de formulaire* ;
  - La valeur indiquée pour l’attribut `autocomplete` est pertinente au regard du type d’information attendu.
- *Notes techniques :*
  - La *liste des valeurs possibles pour l’attribut `autocomplete`* repose sur la liste des valeurs présentes dans la spécification WCAG2.1 qui reprend elle-même la liste des valeurs de type “field name” de la spécification HTML5.2. Le critère WCAG demande à ce que l’une de ces valeurs soit présente pour qualifier un champ de saisie concernant l’utilisateur.
  - Ce que le critère WCAG laisse implicite, ce sont les différentes règles de construction possibles pour obtenir une valeur (simple ou composée) pour l’attribut `autocomplete`. C’est cependant l’affaire du développeur de fournir à l’attribut `autocomplete` une valeur ou un ensemble de valeurs valides au regard des exigences de l’algorithme fourni par la spécification HTML5.2. Ainsi, un attribut `autocomplete` ne peut contenir qu’une seule valeur de type `“field name”`, comme `"name"` ou `"street-address"`. On peut avoir également un ensemble composé de différentes valeurs comme, par exemple, `autocomplete="shipping name"` ou `autocomplete="section-software shipping street-address"` : `"section-software"` renvoie à une valeur de type “scope” et `"shipping"` à une valeur de type “hint set”, mais toujours une seule valeur de type “field name”.

Champs concernant l'utilisateur : attribut `autocomplete` avec la bonne valeur.

**Non-conformité type :** `<input type="email" name="email">` sans `autocomplete="email"`.
**Impact :** sans `autocomplete`, le remplissage automatique ne fonctionne pas : chaque donnée personnelle doit être tapée ou dictée, un surcoût important pour qui saisit avec un contacteur, à la voix, ou peine à mémoriser ses informations.
**Priorité :** 🟡 Mineur

