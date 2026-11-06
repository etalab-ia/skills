# RGAA — Thèmes 1 à 3 : Images, Cadres, Couleurs

## Thème 1 — Images (9 critères)

### 1.1 Chaque image porteuse d'information a-t-elle une alternative textuelle ?

**Texte officiel 1.1 :** Chaque *image porteuse d’information* a-t-elle une *alternative textuelle* ?
- **1.1.1** Chaque image (balise `<img>` ou balise possédant l’attribut WAI-ARIA `role="img"`) *porteuse d’information* a-t-elle une *alternative textuelle* ?
- **1.1.2** Chaque *zone* d’une *image réactive* (balise `<area>`) *porteuse d’information* a-t-elle une *alternative textuelle* ?
- **1.1.3** Chaque bouton de type `image` (balise `<input>` avec l’attribut `type="image"`) a-t-il une *alternative textuelle* ?
- **1.1.4** Chaque *zone cliquable* d’une image réactive côté serveur est-elle doublée d’un mécanisme utilisable quel que soit le dispositif de pointage utilisé et permettant d’accéder à la même destination ?
- **1.1.5** Chaque image vectorielle (balise `<svg>`) *porteuse d’information*, vérifie-t-elle ces conditions ?
  - La balise `<svg>` possède un attribut WAI-ARIA `role="img"` ;
  - La balise `<svg>` a une *alternative textuelle*.
- **1.1.6** Chaque *image objet* (balise `<object>` avec l’attribut `type="image/…"`) *porteuse d’information*, vérifie-t-elle une de ces conditions ?
  - La balise `<object>` possède une *alternative textuelle* et un attribut `role="img"` ;
  - L’élément `<object>` est immédiatement suivi d’un *lien ou bouton adjacent* permettant d’accéder à un *contenu alternatif* ;
  - Un mécanisme permet à l’utilisateur de remplacer l’élément `<object>` par un *contenu alternatif*.
- **1.1.7** Chaque image embarquée (balise `<embed>` avec l’attribut `type="image/…"`) *porteuse d’information*, vérifie-t-elle une de ces conditions ?
  - La balise `<embed>` possède une *alternative textuelle* et un attribut `role="img"` ;
  - L’élément `<embed>` est immédiatement suivi d’un *lien ou bouton adjacent* permettant d’accéder à un *contenu alternatif* ;
  - Un mécanisme permet à l’utilisateur de remplacer l’élément `<embed>` par un *contenu alternatif*.
- **1.1.8** Chaque image bitmap (balise `<canvas>`) *porteuse d’information*, vérifie-t-elle une de ces conditions ?
  - La balise `<canvas>` possède une *alternative textuelle* et un attribut `role="img"` ;
  - Un *contenu alternatif* est présent entre les balises `<canvas>` et `</canvas>` ;
  - L’élément `<canvas>` est immédiatement suivi d’un *lien ou bouton adjacent* permettant d’accéder à un *contenu alternatif* ;
  - Un mécanisme permet à l’utilisateur de remplacer l’élément `<canvas>` par un *contenu alternatif*.

Balises concernées : `<img>`, `role="img"`, `<area>`, `<input type="image">`, `<svg>`, `<object type="image/...">`, `<embed type="image/...">`, `<canvas>`.

- `<img>` / `role="img"` : alternative via `alt`, `aria-label`, `aria-labelledby` ou `title`
- `<svg>` : doit avoir `role="img"` + alternative textuelle
- `<input type="image">` : attribut `alt`

**Non-conformité type :** `<img src="chart.png">` sans attribut `alt` ; `<svg>` sans `role="img"` ni `aria-label`.
**Impact :** sans alternative, le lecteur d’écran ignore l’image ou lit son nom de fichier : la personne qui l’utilise perd l’information qu’elle porte.
**Priorité :** 🔴 Bloquant

---

### 1.2 Chaque image de décoration est-elle correctement ignorée ?

**Texte officiel 1.2 :** Chaque *image de décoration* est-elle correctement ignorée par les technologies d’assistance ?
- **1.2.1** Chaque image (balise `<img>`) *de décoration*, sans *légende*, vérifie-t-elle une de ces conditions ?
  - La balise `<img>` possède un attribut `alt` vide (`alt=""`) et est dépourvue de tout autre attribut permettant de fournir une *alternative textuelle* ;
  - La balise `<img>` possède un attribut WAI-ARIA `aria-hidden="true"` ou `role="presentation"`.
- **1.2.2** Chaque *zone non cliquable* (balise `<area>` sans attribut `href`) *de décoration*, vérifie-t-elle une de ces conditions ?
  - La balise `<area>` possède un attribut `alt` vide (`alt=""`) et est dépourvue de tout autre attribut permettant de fournir une *alternative textuelle* ;
  - La balise `<area>` possède un attribut WAI-ARIA `aria-hidden="true"` ou `role="presentation"`.
- **1.2.3** Chaque *image objet* (balise `<object>` avec l’attribut `type="image/…"`) *de décoration*, sans *légende*, vérifie-t-elle ces conditions ?
  - La balise `<object>` possède un attribut WAI-ARIA `aria-hidden="true"` ;
  - La balise `<object>` est dépourvue d’alternative textuelle ;
  - Il n’y a aucun texte faisant office d’alternative textuelle entre `<object>` et `</object>`.
- **1.2.4** Chaque image vectorielle (balise `<svg>`) *de décoration*, sans *légende*, vérifie-t-elle ces conditions ?
  - La balise `<svg>` possède un attribut WAI-ARIA `aria-hidden="true"` ;
  - La balise `<svg>` et ses enfants sont dépourvus d’*alternative textuelle* ;
  - Les balises `<title>` et `<desc>` sont absentes ou vides ;
  - La balise `<svg>` et ses enfants sont dépourvus d’attribut `title`.
- **1.2.5** Chaque image bitmap (balise `<canvas>`) *de décoration*, sans *légende*, vérifie-t-elle ces conditions ?
  - La balise `<canvas>` possède un attribut WAI-ARIA `aria-hidden="true"` ;
  - La balise `<canvas>` et ses enfants sont dépourvus d’*alternative textuelle* ;
  - Il n’y a aucun texte faisant office d’*alternative textuelle* entre `<canvas>` et `</canvas>`.
- **1.2.6** Chaque image embarquée (balise `<embed>` avec l’attribut `type="image/…"`) *de décoration*, sans *légende*, vérifie-t-elle ces conditions ?
  - La balise `<embed>` possède un attribut WAI-ARIA `aria-hidden="true"` ;
  - La balise `<embed>` et ses enfants sont dépourvus d’*alternative textuelle*.
- *Notes techniques :*
  - Lorsqu'une image est associée à une *légende*, la note technique WCAG recommande de prévoir systématiquement une *alternative textuelle* (cf. critère 1.9). Dans ce cas le critère 1.2 est non applicable.
  - Dans le cas d'une image vectorielle (balise `<svg>`) de décoration qui serait affichée au travers d'un élément `<use href="…">` enfant de l'élément `<svg>`, le test 1.2.4 s'appliquera également à l'élément `<svg>` associée par le biais de l'élément `<use>`.
  - Un attribut WAI-ARIA `role="presentation"` peut être utilisé sur les images de décoration et les zones non cliquables de décoration. Le rôle `"none"` introduit en ARIA 1.1 et synonyme du rôle `"presentation"` peut être aussi utilisé. Il reste préférable cependant d'utiliser le rôle `"presentation"` en attendant un support satisfaisant du rôle `"none"`.

- `<img>` : `alt=""` (vide, pas absent)
- `<svg>` : `aria-hidden="true"` + pas de `role="img"`
- Ou `role="presentation"` sur l'image

**Non-conformité type :** `<img src="decoration.png">` sans attribut `alt` (attribut absent) ; `<svg>` décoratif sans `aria-hidden`.
**Impact :** une image décorative non ignorée est annoncée, parfois par son nom de fichier : ce bruit ralentit la lecture au lecteur d’écran et laisse croire à une information.
**Priorité :** 🟡 Mineur

---

### 1.3 L'alternative textuelle est-elle pertinente ?

**Texte officiel 1.3 :** Pour chaque image *porteuse d’information* ayant une *alternative textuelle*, cette alternative est-elle pertinente (hors cas particuliers) ?
- **1.3.1** Chaque image (balise `<img>` ou balise possédant l’attribut WAI-ARIA `role="img"`) *porteuse d’information*, ayant une *alternative textuelle*, cette alternative est-elle pertinente (hors cas particuliers) ?
  - S’il est présent, le contenu de l’attribut `alt` est pertinent ;
  - S’il est présent, le contenu de l’attribut `title` est pertinent ;
  - S’il est présent, le contenu de l’attribut WAI-ARIA `aria-label` est pertinent ;
  - S’il est présent, le *passage de texte* associé via l’attribut WAI-ARIA `aria-labelledby` est pertinent.
- **1.3.2** Pour chaque *zone* (balise `<area>`) d’une *image réactive* *porteuse d’information*, ayant une *alternative textuelle*, cette alternative est-elle pertinente (hors cas particuliers) ?
  - S’il est présent, le contenu de l’attribut `alt` est pertinent ;
  - S’il est présent, le contenu de l’attribut `title` est pertinent ;
  - S’il est présent, le contenu de l’attribut WAI-ARIA `aria-label` est pertinent ;
  - S’il est présent, le *passage de texte* associé via l’attribut WAI-ARIA `aria-labelledby` est pertinent.
- **1.3.3** Pour chaque *bouton* de type `image` (balise `<input>` avec l’attribut `type="image"`), ayant une *alternative textuelle*, cette alternative est-elle pertinente (hors cas particuliers) ?
  - S’il est présent, le contenu de l’attribut `alt` est pertinent ;
  - S’il est présent, le contenu de l’attribut `title` est pertinent ;
  - S’il est présent, le contenu de l’attribut WAI-ARIA `aria-label` est pertinent ;
  - S’il est présent, le *passage de texte* associé via l’attribut WAI-ARIA `aria-labelledby` est pertinent.
- **1.3.4** Pour chaque *image objet* (balise `<object>` avec l’attribut `type="image/…"`) *porteuse d’information*, ayant une *alternative textuelle* ou un *contenu alternatif*, cette alternative est-elle pertinente (hors cas particuliers) ?
  - S’il est présent, le contenu de l’attribut `title` est pertinent ;
  - S’il est présent, le contenu de l’attribut WAI-ARIA `aria-label` est pertinent ;
  - S’il est présent, le *passage de texte* associé via l’attribut WAI-ARIA `aria-labelledby` est pertinent ;
  - S’il est présent le *contenu alternatif* est pertinent.
- **1.3.5** Pour chaque image embarquée (balise `<embed>` avec l’attribut `type="image/…"`) *porteuse d’information*, ayant une *alternative textuelle* ou un *contenu alternatif*, cette alternative est-elle pertinente (hors cas particuliers) ?
  - S’il est présent, le contenu de l’attribut `title` est pertinent ;
  - S’il est présent, le contenu de l’attribut WAI-ARIA `aria-label` est pertinent ;
  - S’il est présent, le *passage de texte* associé via l’attribut WAI-ARIA `aria-labelledby` est pertinent ;
  - S’il est présent le *contenu alternatif* est pertinent.
- **1.3.6** Pour chaque image vectorielle (balise `<svg>`) *porteuse d’information*, ayant une *alternative textuelle*, cette alternative est-elle pertinente (hors cas particuliers) ?
  - S’il est présent, le contenu de l'élément `<title>` est pertinent ;
  - S’il est présent, le contenu de l’attribut WAI-ARIA `aria-label` est pertinent ;
  - S’il est présent, le *passage de texte* associé via l’attribut WAI-ARIA `aria-labelledby` est pertinent.
- **1.3.7** Pour chaque image bitmap (balise `<canvas>`) *porteuse d’information*, ayant une *alternative textuelle* ou un *contenu alternatif*, cette alternative est-elle pertinente (hors cas particuliers) ?
  - S’il est présent, le contenu de l’attribut `title` est pertinent ;
  - S’il est présent, le contenu de l’attribut WAI-ARIA `aria-label` est pertinent ;
  - S’il est présent, le *passage de texte* associé via l’attribut WAI-ARIA `aria-labelledby` est pertinent ;
  - S’il est présent le *contenu alternatif* est pertinent.
- **1.3.8** Pour chaque image bitmap (balise `<canvas>`) *porteuse d’information* et ayant  un *contenu alternatif* entre `<canvas>` et `</canvas>`, ce *contenu alternatif* est-il *correctement restitué par les technologies d’assistance* ?
- **1.3.9** Pour chaque image *porteuse d’information* et ayant une *alternative textuelle*, l’*alternative textuelle* est-elle *courte et concise* (hors cas particuliers) ?
- *Cas particuliers :*
  - Il existe une gestion de cas particuliers lorsque l’image est utilisée comme *CAPTCHA* ou comme *image-test*. Dans cette situation, où il n’est pas possible de donner une alternative pertinente sans détruire l’objet du CAPTCHA ou du test, le critère est non applicable.
  - Note : le cas des CAPTCHA et des images-test est traité de manière spécifique par le critère 1.4.

L'alternative doit être courte, concise (≤80 caractères recommandé) et décrire la fonction ou l'information de l'image, pas son apparence.

**Non-conformité type :** `alt="image"`, `alt="logo.png"`, `alt="Photo"`, ou `alt` reprenant mot pour mot le texte adjacent.
**Impact :** une alternative générique est bien annoncée au lecteur d’écran, mais elle ne transmet rien : la personne qui l’utilise ignore ce que l’image apporte. Une alternative qui redit le texte voisin lui fait entendre deux fois la même chose.
**Priorité :** 🟠 Majeur

---

### 1.4 CAPTCHA : l'alternative identifie-t-elle la nature et la fonction ?

**Texte officiel 1.4 :** Pour chaque image utilisée comme *CAPTCHA* ou comme *image-test*, ayant une *alternative textuelle*, cette alternative permet-elle d’identifier la nature et la fonction de l’image ?
- **1.4.1** Pour chaque image (balise `<img>`) utilisée comme *CAPTCHA* ou comme *image-test*, ayant une *alternative textuelle*, cette alternative est-elle pertinente ?
  - S’il est présent, le contenu de l’attribut `alt` est pertinent ;
  - S’il est présent, le contenu de l’attribut `title` est pertinent ;
  - S’il est présent, le contenu de l’attribut WAI-ARIA `aria-label` est pertinent ;
  - S’il est présent, le *passage de texte* associé via l’attribut WAI-ARIA `aria-labelledby` est pertinent.
- **1.4.2** Pour chaque zone (balise `<area>`) d’une image réactive utilisée comme *CAPTCHA* ou comme *image-test*, ayant une *alternative textuelle*, cette alternative est-elle pertinente ?
  - S’il est présent, le contenu de l’attribut `alt` est pertinent ;
  - S’il est présent, le contenu de l’attribut `title` est pertinent ;
  - S’il est présent, le contenu de l’attribut WAI-ARIA `aria-label` est pertinent ;
  - S’il est présent, le *passage de texte* associé via l’attribut WAI-ARIA `aria-labelledby` est pertinent.
- **1.4.3** Pour chaque *bouton* de type image (balise `<input>` avec l’attribut `type="image"`) utilisé comme *CAPTCHA* ou comme *image-test*, ayant une *alternative textuelle*, cette alternative est-elle pertinente ?
  - S’il est présent, le contenu de l’attribut `alt` est pertinent ;
  - S’il est présent, le contenu de l’attribut `title` est pertinent ;
  - S’il est présent, le contenu de l’attribut WAI-ARIA `aria-label` est pertinent ;
  - S’il est présent, le *passage de texte* associé via l’attribut WAI-ARIA `aria-labelledby` est pertinent.
- **1.4.4** Pour chaque *image objet* (balise `<object>` avec l’attribut `type="image/…"`) utilisée comme *CAPTCHA* ou comme *image-test*, ayant une *alternative textuelle* ou un *contenu alternatif*, cette alternative est-elle pertinente ?
  - S’il est présent, le contenu de l’attribut `alt` est pertinent ;
  - S’il est présent, le contenu de l’attribut `title` est pertinent ;
  - S’il est présent, le contenu de l’attribut WAI-ARIA `aria-label` est pertinent ;
  - S’il est présent, le *passage de texte* associé via l’attribut WAI-ARIA `aria-labelledby` est pertinent ;
  - S’il est présent le *contenu alternatif* est pertinent.
- **1.4.5** Pour chaque image embarquée (balise `<embed>` avec l’attribut `type="image/…"`) utilisée comme *CAPTCHA* ou comme *image-test*, ayant une *alternative textuelle* ou un *contenu alternatif*, cette alternative est-elle pertinente ?
  - S’il est présent, le contenu de l’attribut `alt` est pertinent ;
  - S’il est présent, le contenu de l’attribut `title` est pertinent ;
  - S’il est présent, le contenu de l’attribut WAI-ARIA `aria-label` est pertinent ;
  - S’il est présent, le *passage de texte* associé via l’attribut WAI-ARIA `aria-labelledby` est pertinent ;
  - S’il est présent le *contenu alternatif* est pertinent.
- **1.4.6** Pour chaque image vectorielle (balise `<svg>`) utilisée comme *CAPTCHA* ou comme *image-test*, ayant une *alternative textuelle*, cette alternative est-elle pertinente ?
  - S’il est présent, le contenu de l’attribut `alt` est pertinent ;
  - S’il est présent, le contenu de l’attribut `title` est pertinent ;
  - S’il est présent, le contenu de l’attribut WAI-ARIA `aria-label` est pertinent ;
  - S’il est présent, le *passage de texte* associé via l’attribut WAI-ARIA `aria-labelledby` est pertinent.
- **1.4.7** Pour chaque image bitmap (balise `<canvas>`) utilisée comme *CAPTCHA* ou comme *image-test*, ayant une *alternative textuelle* ou un *contenu alternatif*, cette alternative est-elle pertinente ?
  - S’il est présent, le contenu de l’attribut `alt` est pertinent ;
  - S’il est présent, le contenu de l’attribut `title` est pertinent ;
  - S’il est présent, le contenu de l’attribut WAI-ARIA `aria-label` est pertinent ;
  - S’il est présent, le *passage de texte* associé via l’attribut WAI-ARIA `aria-labelledby` est pertinent ;
  - S’il est présent le *contenu alternatif* est pertinent.

Alternative type : "Code de sécurité anti-spam" (pas la réponse au CAPTCHA).

**Non-conformité type :** CAPTCHA sans `alt`, ou `alt` vide.
**Impact :** sans alternative qui dit sa nature, la personne qui utilise un lecteur d’écran ne comprend pas qu’un contrôle lui est demandé et reste bloquée avant d’envoyer le formulaire.
**Priorité :** 🔴 Bloquant

---

### 1.5 CAPTCHA : une solution d'accès alternatif existe-t-elle ?

**Texte officiel 1.5 :** Pour chaque image utilisée comme *CAPTCHA*, une solution d’accès alternatif au contenu ou à la fonction du CAPTCHA est-elle présente ?
- **1.5.1** Chaque image (balises `<img>`, `<area>`, `<object>`, `<embed>`, `<svg>`, `<canvas>` ou possédant un attribut WAI-ARIA `role="img"`) utilisée comme *CAPTCHA* vérifie-t-elle une de ces conditions ?
  - Il existe une autre forme de *CAPTCHA* non graphique, au moins ;
  - Il existe une autre solution d’accès à la fonctionnalité qui est sécurisée par le *CAPTCHA*.
- **1.5.2** Chaque bouton associé à une image (balise `input` avec l’attribut `type="image"`) utilisée comme *CAPTCHA* vérifie-t-il une de ces conditions ?
  - Il existe une autre forme de *CAPTCHA* non graphique, au moins ;
  - Il existe une autre solution d’accès à la fonctionnalité sécurisée par le *CAPTCHA*.

Au moins une alternative d'un autre type (audio si visuel, etc.).

**Non-conformité type :** CAPTCHA visuel unique sans alternative.
**Impact :** un CAPTCHA seulement visuel arrête toute personne qui ne peut pas le lire, par exemple au lecteur d’écran : le service lui reste fermé.
**Priorité :** 🔴 Bloquant

---

### 1.6 Image porteuse d'information : description détaillée si nécessaire ?

**Texte officiel 1.6 :** Chaque image *porteuse d’information* a-t-elle, si nécessaire, une *description détaillée* ?
- **1.6.1** Chaque image (balise `<img>`) *porteuse d’information*, qui nécessite une *description détaillée*, vérifie-t-elle une de ces conditions ?
  - Il existe un attribut `longdesc` qui donne l’adresse (URL) d’une page ou d’un emplacement dans la page contenant la *description détaillée* ;
  - Il existe une *alternative textuelle* contenant la référence à une *description détaillée* adjacente à l’image ;
  - Il existe un *lien ou un bouton adjacent* permettant d’accéder à la *description détaillée*.
- **1.6.2** Chaque *image objet* (balise `<object>` avec l’attribut `type="image/…"`) *porteuse d’information*, qui nécessite une *description détaillée*, vérifie-t-elle une de ces conditions ?
  - Il existe un attribut `longdesc` qui donne l’adresse (URL) d’une page ou d’un emplacement dans la page contenant la *description détaillée* ;
  - Il existe une *alternative textuelle* contenant la référence à une *description détaillée* adjacente à l’image ;
  - Il existe un *lien ou un bouton adjacent* permettant d’accéder à la *description détaillée*.
- **1.6.3** Chaque image embarquée (balise `<embed>`) *porteuse d’information*, qui nécessite une *description détaillée*, vérifie-t-elle une de ces conditions ?
  - Il existe un attribut `longdesc` qui donne l’adresse (URL) d’une page ou d’un emplacement dans la page contenant la *description détaillée* ;
  - Il existe une *alternative textuelle* contenant la référence à une *description détaillée* adjacente à l’image ;
  - Il existe un *lien ou un bouton adjacent* permettant d’accéder à la *description détaillée*.
- **1.6.4** Chaque *bouton* de type image (balise `<input>` avec l’attribut `type="image"`) *porteur d’information*, qui nécessite une *description détaillée*, vérifie-t-il une de ces conditions ?
  - Il existe un attribut `longdesc` qui donne l’adresse (URL) d’une page ou d’un emplacement dans la page contenant la *description détaillée* ;
  - Il existe une *alternative textuelle* contenant la référence à une *description détaillée* adjacente à l’image ;
  - Il existe un *lien ou un bouton adjacent* permettant d’accéder à la *description détaillée*.
- **1.6.5** Chaque image vectorielle (balise `<svg>`) *porteuse d’information*, qui nécessite une *description détaillée*, vérifie-t-elle une de ces conditions ?
  - Il existe un attribut WAI-ARIA `aria-label` contenant l’alternative textuelle et une référence à une *description détaillée* adjacente ;
  - Il existe un attribut WAI-ARIA `aria-labelledby` associant un *passage de texte* faisant office d’alternative textuelle et un autre faisant office de *description détaillée* ;
  - Il existe un attribut WAI-ARIA `aria-describedby` associant un *passage de texte* faisant office de *description détaillée* ;
  - Il existe un *lien ou un bouton adjacent* permettant d’accéder à la *description détaillée*.
- **1.6.6** Pour chaque image vectorielle (balise `<svg>`) *porteuse d’information*, ayant une *description détaillée*, la référence éventuelle à la *description détaillée* dans l’attribut WAI-ARIA `aria-label` et la *description détaillée* associée par l’attribut WAI-ARIA `aria-labelledby` ou `aria-describedby` sont-elles correctement restituées par les technologies d’assistance ?
- **1.6.7** Chaque image bitmap (balise `<canvas>`), *porteuse d’information*, qui nécessite une *description détaillée*, vérifie-t-elle une de ces conditions ?
  - Il existe un attribut WAI-ARIA `aria-label` contenant l’alternative textuelle et une référence à une *description détaillée* adjacente ;
  - Il existe un attribut WAI-ARIA `aria-labelledby` associant un passage de texte faisant office d’alternative textuelle et un autre faisant office de *description détaillée* ;
  - Il existe un contenu textuel entre `<canvas>` et `</canvas>` faisant référence à une *description détaillée* adjacente à l’image bitmap ;
  - Il existe un contenu textuel entre `<canvas>` et `</canvas>` faisant office de *description détaillée* ;
  - Il existe un *lien ou bouton adjacent* permettant d’accéder à la *description détaillée*.
- **1.6.8** Pour chaque image bitmap (balise `<canvas>`) *porteuse d’information*, qui implémente une référence à une *description détaillée* adjacente, cette référence est-elle correctement restituée par les technologies d’assistance ?
- **1.6.9** Pour chaque image (balise `<img>`, `<input>` avec l’attribut `type="image"`, `<area>`, `<object>`, `<embed>`, `<svg>`, `<canvas>`, ou possédant un attribut WAI-ARIA `role="img"`) *porteuse d’information*, qui est accompagnée d’une *description détaillée* et qui utilise un attribut WAI-ARIA `aria-describedby`, l’attribut WAI-ARIA `aria-describedby` associe-t-il la *description détaillée* ?
- **1.6.10** Chaque balise possédant un attribut WAI-ARIA `role="img"` *porteuse d’information*, qui nécessite une *description détaillée*, vérifie-t-elle une de ces conditions ?
  - Il existe un attribut WAI-ARIA `aria-label` contenant l’*alternative textuelle* et une référence à une *description détaillée* adjacente ;
  - Il existe un attribut WAI-ARIA `aria-labelledby` associant un *passage de texte* faisant office d’*alternative textuelle* et un autre faisant office de *description détaillée* ;
  - Il existe un attribut WAI-ARIA `aria-describedby` associant un *passage de texte* faisant office de *description détaillée* ;
  - Il existe un *lien ou un bouton adjacent* permettant d’accéder à la *description détaillée*.
- *Notes techniques :*
  - Dans le cas du SVG, le manque de support de l’élément `<title>` et `<desc>` par les technologies d’assistance crée une difficulté dans le cas de l’implémentation de l’*alternative textuelle* de l’image et de sa *description détaillée*. Dans ce cas, il est recommandé d’utiliser l’attribut WAI-ARIA `aria-label` pour implémenter à la fois l’*alternative textuelle* courte et la référence à la *description détaillée* adjacente ou l’attribut WAI-ARIA `aria-labelledby` pour associer les passages de texte faisant office d’alternative courte et de *description détaillée*.
  - L’utilisation de l’attribut WAI-ARIA aria-describedby n’est pas recommandée pour lier une image (`<img>`, `<object>`, `<embed>`, `<canvas>`) à sa *description détaillée*, par manque de support des technologies d’assistance. Néanmoins, lorsqu’il est utilisé, l’attribut devra nécessairement faire référence à l’`id` de la zone contenant la *description détaillée*.
  - La *description détaillée* adjacente peut être implémentée via une balise `<figcaption>`, dans ce cas le critère 1.9 doit être vérifié (utilisation de `<figure>` et des attributs WAI-ARIA `role="figure"` et `aria-label`, notamment).
  - L'attribut `longdesc` qui constitue une des conditions du test 1.6.1 (et dont la pertinence est vérifiée avec le test 1.7.1) est désormais considéré comme obsolète par la spécification HTML en cours. La vérification de cet attribut ne sera donc requise que pour les versions de la spécification HTML antérieure à HTML 5.

Pour les images complexes (graphiques, schémas, cartes), fournir une description détaillée via :
- `aria-describedby` référençant un passage de texte
- Lien/bouton adjacent vers la description
- Description adjacente visible

**Non-conformité type :** Graphique complexe avec seulement `alt="Graphique d'évolution"` sans description des données.
**Impact :** une alternative courte ne peut pas porter les données d’un graphique : sans description, la personne qui ne voit pas l’image n’accède pas aux valeurs.
**Priorité :** 🟠 Majeur

---

### 1.7 La description détaillée est-elle pertinente ?

**Texte officiel 1.7 :** Pour chaque image *porteuse d’information* ayant une *description détaillée*, cette description est-elle pertinente ?

La description détaillée doit contenir toute l'information véhiculée par l'image.

**Non-conformité type :** Description qui mentionne le titre du graphique mais pas les valeurs.
**Impact :** une description partielle laisse croire que l’information est complète : la personne qui ne voit pas l’image n’a qu’une partie des données et ne le sait pas.
**Priorité :** 🟠 Majeur

---

### 1.8 Les images texte sont-elles remplacées par du texte stylé ?

**Texte officiel 1.8 :** Chaque *image texte* *porteuse d’information*, en l’absence d’un *mécanisme de remplacement*, doit si possible être remplacée par du *texte stylé*. Cette règle est-elle respectée (hors cas particuliers) ?

Préférer du texte CSS quand c'est possible. Exception : logos, marques.

**Non-conformité type :** Titre de section rendu comme image PNG au lieu d'un `<h2>` stylé.
**Impact :** le texte en image devient flou à l’agrandissement et ne peut pas être reformaté : la personne qui zoome ou adapte l’affichage (police, espacement, couleurs) le lit mal.
**Priorité :** 🟡 Mineur

---

### 1.9 Chaque légende d'image est-elle correctement reliée ?

**Texte officiel 1.9 :** Chaque *légende d’image* est-elle, si nécessaire, correctement reliée à l’image correspondante ?
- **1.9.1** Chaque image pourvue d’une *légende* (balise `<img>`, `<input>` avec l’attribut `type="image"` ou possédant un attribut WAI-ARIA `role="img"` associée à une *légende* adjacente), vérifie-t-elle, si nécessaire, ces conditions ?
  - L’image (balise `<img>`, `<input>` avec l’attribut `type="image"` ou possédant un attribut WAI-ARIA `role="img"`) et sa *légende* adjacente sont contenues dans une balise `<figure>` ;
  - La balise `<figure>` possède un attribut WAI-ARIA `role="figure"` ou `role="group"` ;
  - La balise `<figure>` possède un attribut WAI-ARIA `aria-label` dont le contenu est identique au contenu de la *légende* ;
  - La *légende* est contenue dans une balise `<figcaption>`.
- **1.9.2** Chaque *image objet* pourvue d’une *légende* (balise `<object>` avec l’attribut `type="image/…"` associée à une *légende* adjacente), vérifie-t-elle, si nécessaire, ces conditions ?
  - L’*image objet* et sa *légende* adjacente sont contenues dans une balise `<figure>` ;
  - La balise `<figure>` possède un attribut WAI-ARIA `role="figure"` ou `role="group"` ;
  - La balise `<figure>` possède un attribut WAI-ARIA `aria-label` dont le contenu est identique au contenu de la *légende* ;
  - La *légende* est contenue dans une balise `<figcaption>`.
- **1.9.3** Chaque image embarquée pourvue d’une *légende* (balise `<embed>` associée à une *légende* adjacente), vérifie-t-elle, si nécessaire, ces conditions ?
  - L’image embarquée (balise `<embed>`) et sa *légende* adjacente sont contenues dans une balise `<figure>` ;
  - La balise `<figure>` possède un attribut WAI-ARIA `role="figure"` ou `role="group"` ;
  - La balise `<figure>` possède un attribut WAI-ARIA `aria-label` dont le contenu est identique au contenu de la *légende* ;
  - La *légende* est contenue dans une balise `<figcaption>`.
- **1.9.4** Chaque image vectorielle pourvue d’une *légende* (balise `<svg>` associée à une *légende* adjacente), vérifie-t-elle, si nécessaire, ces conditions ?
  - L’image vectorielle (balise `<svg>`) et sa *légende* adjacente sont contenues dans une balise `<figure>` ;
  - La balise `<figure>` possède un attribut WAI-ARIA `role="figure"` ou `role="group"` ;
  - La balise `<figure>` possède un attribut WAI-ARIA `aria-label` dont le contenu est identique au contenu de la *légende* ;
  - La *légende* est contenue dans une balise `<figcaption>`.
- **1.9.5** Chaque image bitmap pourvue d’une *légende* (balise `<canvas>` associée à une *légende* adjacente), vérifie-t-elle, si nécessaire, ces conditions ?
  - L’image bitmap (balise `<canvas>`) et sa *légende* adjacente sont contenues dans une balise `<figure>` ;
  - La balise `<figure>` possède un attribut WAI-ARIA `role="figure"` ou `role="group"` ;
  - La balise `<figure>` possède un attribut WAI-ARIA `aria-label` dont le contenu est identique au contenu de la *légende* ;
  - La *légende* est contenue dans une balise `<figcaption>`.
- *Notes techniques :*
  - L’implémentation d’un attribut WAI-ARIA `role="group"` ou `role="figure"` sur l’élément parent `<figure>` est destiné à pallier le manque de support actuel des éléments `<figure>` par les technologies d’assistance. L’utilisation d’un élément `<figcaption>` pour associer une *légende* à une image impose au minimum l’utilisation d’un attribut WAI-ARIA `aria-label` sur l’élément parent `<figure>` dont le contenu sera identique au contenu de l’élément `<figcaption>`. Pour s’assurer d’un support optimal, il peut également être fait une association explicite entre le contenu de l’*alternative textuelle* de l’image et le contenu de l’élément `<figcaption>`, par exemple :
  - `<img src="image.png" alt="Photo : soleil couchant" /><figcaption>Photo : crédit xxx</figcaption>`
  - Les attributs WAI-ARIA `aria-labelledby` et `aria-describedby` ne peuvent pas être utilisés actuellement par manque de support par les technologies d’assistance.
  - Note : les images légendées doivent par ailleurs respecter le critère 1.1 et le critère 1.3 relatifs aux images porteuses d’information.

Utiliser `<figure>` avec `role="figure"` ou `role="group"`, un `aria-label` identique au contenu de la légende, et `<figcaption>`.

**Non-conformité type :** `<img>` suivi d'un `<p>` comme légende sans structure `<figure>` ; `<figure>` sans `role` ni `aria-label`.
**Impact :** une légende non reliée est lue comme un paragraphe sans rapport : la personne qui utilise un lecteur d’écran ne sait pas qu’elle se rapporte à l’image.
**Priorité :** 🟡 Mineur

---

## Thème 2 — Cadres (2 critères)

### 2.1 Chaque cadre a-t-il un titre ?

**Texte officiel 2.1 :** Chaque *cadre* a-t-il un *titre de cadre* ?
- **2.1.1** Chaque cadre (balise `<iframe>` ou `<frame>`) a-t-il un attribut `title` ?

Chaque `<iframe>` doit avoir un attribut `title`.

**Non-conformité type :** `<iframe src="/map">` sans attribut `title`.
**Impact :** sans titre, le lecteur d’écran annonce un cadre sans nom, ou son adresse : la personne qui l’utilise ne sait pas s’il vaut la peine d’y entrer.
**Priorité :** 🔴 Bloquant

---

### 2.2 Le titre de cadre est-il pertinent ?

**Texte officiel 2.2 :** Pour chaque *cadre* ayant un *titre de cadre*, ce titre de cadre est-il pertinent ?
- **2.2.1** Pour chaque cadre (balise `<iframe>` ou `<frame>`) ayant un attribut `title`, le contenu de cet attribut est-il pertinent ?

Le titre doit décrire le contenu du cadre.

**Non-conformité type :** `title="iframe1"` ou `title="Cadre"`.
**Impact :** un titre générique, restitué seul dans la liste des cadres du lecteur d’écran, ne dit pas ce que le cadre contient.
**Priorité :** 🟠 Majeur

---

## Thème 3 — Couleurs (3 critères)

### 3.1 L'information n'est pas donnée uniquement par la couleur

**Texte officiel 3.1 :** Dans chaque page web, l’*information* ne doit pas être donnée uniquement par la couleur. Cette règle est-elle respectée ?
- **3.1.1** Pour chaque mot ou ensemble de mots dont la mise en couleur est porteuse d’information, l’*information* ne doit pas être donnée uniquement par la couleur. Cette règle est-elle respectée ?
- **3.1.2** Pour chaque indication de couleur donnée par un texte, l’*information* ne doit pas être donnée uniquement par la couleur. Cette règle est-elle respectée ?
- **3.1.3** Pour chaque image *véhiculant une information*, l’*information* ne doit pas être donnée uniquement par la couleur. Cette règle est-elle respectée ?
- **3.1.4** Pour chaque *propriété CSS déterminant une couleur* et *véhiculant une information*, l’*information* ne doit pas être donnée uniquement par la couleur. Cette règle est-elle respectée ?
- **3.1.5** Pour chaque *média temporel* *véhiculant une information*, l’*information* ne doit pas être donnée uniquement par la couleur. Cette règle est-elle respectée ?
- **3.1.6** Pour chaque *média non temporel* *véhiculant une information*, l’*information* ne doit pas être donnée uniquement par la couleur. Cette règle est-elle respectée ?

Toute information véhiculée par la couleur doit aussi être transmise autrement (entrée « Information (donnée par la couleur) » du glossaire) :

- par une indication textuelle visible, qui suffit seule ;
- ou par un moyen graphique (pictogramme, forme, style de bordure) ou un autre style typographique (gras, italique, taille), à condition de l’accompagner d’un complément dans le code (`aria-label`, `title`, texte masqué, `aria-current`…).

**Non-conformité type :** Erreur de formulaire signalée uniquement par un fond rouge, sans icône ni texte explicatif ; page active du menu signalée par la couleur et le gras, sans `aria-current`.
**Impact :** l’information n’est pas restituée au lecteur d’écran, et la personne qui distingue mal les couleurs ne perçoit pas la différence, par exemple entre un succès et une erreur.
**Priorité :** 🟠 Majeur

---

### 3.2 Contraste texte/arrière-plan suffisant

**Texte officiel 3.2 :** Dans chaque page web, le *contraste* entre la couleur du texte et la couleur de son arrière-plan est-il suffisamment élevé (hors cas particuliers) ?
- **3.2.1** Dans chaque page web, le texte et le texte en image sans effet de graisse d’une taille restituée inférieure à 24px vérifient-ils une de ces conditions (hors cas particuliers) ?
  - Le rapport de *contraste* entre le texte et son arrière-plan est de 4.5:1, au moins ;
  - Un mécanisme permet à l’utilisateur d’afficher le texte avec un rapport de *contraste* de 4.5:1, au moins.
- **3.2.2** Dans chaque page web, le texte et le texte en image en gras d’une taille restituée inférieure à 18,5px vérifient-ils une de ces conditions (hors cas particuliers) ?
  - Le rapport de *contraste* entre le texte et son arrière-plan est de 4.5:1, au moins ;
  - Un mécanisme permet à l’utilisateur d’afficher le texte avec un rapport de *contraste* de 4.5:1, au moins.
- **3.2.3** Dans chaque page web, le texte et le texte en image sans effet de graisse d’une taille restituée supérieure ou égale à 24px vérifient-ils une de ces conditions (hors cas particuliers) ?
  - Le rapport de *contraste* entre le texte et son arrière-plan est de 3:1, au moins ;
  - Un mécanisme permet à l’utilisateur d’afficher le texte avec un rapport de *contraste* de 3:1, au moins.
- **3.2.4** Dans chaque page web, le texte et le texte en image en gras d’une taille restituée supérieure ou égale à 18,5px vérifient-ils une de ces conditions (hors cas particuliers) ?
  - Le rapport de *contraste* entre le texte et son arrière-plan est de 3:1, au moins ;
  - Un mécanisme permet à l’utilisateur d’afficher le texte avec un rapport de *contraste* de 3:1, au moins.
- **3.2.5** Dans le *mécanisme qui permet d’afficher un rapport de contraste* conforme, le rapport de contraste entre le texte et la couleur d’arrière-plan est-il suffisamment élevé ?
- *Cas particuliers :*
  - Dans ces situations, les critères sont non applicables pour ces éléments :
    - - Le texte fait partie d’un logo ou d’un nom de marque d’un organisme ou d’une société ;
    - - Le texte ou l’image de texte est purement décoratif ;
    - - Le texte fait partie d’une image véhiculant une information mais le texte lui-même n’apporte aucune information essentielle ;
    - - Le texte ou l’image de texte fait partie d’un élément d’interface sur lequel aucune action n’est possible (par exemple un bouton avec l’attribut `disabled`).

| Type de texte | Ratio minimum |
|---|---|
| Texte < 24px (ou < 18.5px gras) | **4.5:1** |
| Texte ≥ 24px (ou ≥ 18.5px gras) | **3:1** |

**Non-conformité type :** Texte gris clair `#999` sur fond blanc `#fff` (ratio ≈ 2.8:1, insuffisant pour texte normal).
**Impact :** un contraste insuffisant rend le texte difficile, voire impossible, à lire pour une personne malvoyante, ou sur un écran en plein soleil.
**Priorité :** 🟠 Majeur

---

### 3.3 Contraste des composants d'interface et éléments graphiques

**Texte officiel 3.3 :** Dans chaque page web, les couleurs utilisées dans les *composants d’interface* ou les éléments graphiques porteurs d’informations sont-elles suffisamment contrastées (hors cas particuliers) ?
- **3.3.1** Dans chaque page web, le rapport de *contraste* entre les couleurs d’un *composant d’interface* dans ses différents états et la *couleur d’arrière-plan contiguë* vérifie-t-il une de ces conditions (hors cas particuliers) ?
  - Le rapport de *contraste* est de 3:1, au moins ;
  - Un *mécanisme* permet un rapport de *contraste* de 3:1, au moins.
- **3.3.2** Dans chaque page web, le rapport de *contraste* des différentes couleurs composant un *élément graphique*, lorsqu’elles sont nécessaires à sa compréhension, et la *couleur d’arrière-plan contiguë*, vérifie-t-il une de ces conditions (hors cas particuliers) ?
  - Le rapport de *contraste* est de 3:1, au moins ;
  - Un *mécanisme* permet un rapport de *contraste* de 3:1, au moins.
- **3.3.3** Dans chaque page web, le rapport de *contraste* des différentes *couleurs contiguës* entre elles d’un *élément graphique*, lorsqu’elles sont nécessaires à sa compréhension, vérifie-t-il une de ces conditions (hors cas particuliers) ?
  - Le rapport de *contraste* est de 3:1, au moins ;
  - Un *mécanisme* permet un rapport de *contraste* de 3:1, au moins.
- **3.3.4** Dans le *mécanisme qui permet d’afficher un rapport de contraste* conforme, les couleurs du composant ou des éléments graphiques porteurs d’informations qui le composent, sont-elles suffisamment contrastées ?
- *Cas particuliers :*
  - Les cas suivants sont non applicables pour ce critère :
    - - Composant d’interface inactif (par exemple, un bouton avec un attribut `disabled`) sur lequel aucune action n’est possible ;
    - - Composant d’interface pour lequel l’apparence est gérée par les styles natifs du navigateur sans aucune modification par l’auteur (par exemple, le style au focus natif dans Chrome ou Firefox) ;
    - - Composant d’interface pour lequel la couleur n’est pas nécessaire pour identifier le composant ou son état (par exemple, un groupe de liens faisant office de navigation dont la position dans la page, la taille et la couleur du texte permettent de comprendre qu’il s’agit de liens même si la couleur du soulignement des liens avec le fond blanc n’a pas un ratio de 3:1 et que le texte lui a un ratio de 4.5:1) ;
    - - *Élément graphique* ou parties d’élément graphique non porteur d’information ou ayant une alternative (description longue, informations identiques visibles dans la page) ;
    - - *Élément graphique* ou parties d’élément graphique faisant partie d’un logo ou du nom de marque d’un organisme ou d’une société ;
    - - *Élément graphique* ou parties d’élément graphique dont la présentation est essentielle à l’information véhiculée (par exemple, drapeaux, logotypes, photos de personnes ou de scènes, captures d’écran, diagrammes médicaux, carte de chaleurs) ;
    - - *Élément graphique* ou parties d’élément graphique dynamiques dont le contraste au survol / focus est suffisant.

Ratio minimum **3:1** entre :
- Les couleurs d'un composant d'interface et son arrière-plan
- Les couleurs contiguës d'un élément graphique porteur d'information

**Non-conformité type :** Bordure de champ de formulaire `#ccc` sur fond blanc `#fff` (ratio ≈ 1.6:1, insuffisant).
**Impact :** un contour trop pâle empêche la personne malvoyante de repérer le champ ou le bouton : elle ne voit pas où agir.
**Priorité :** 🟠 Majeur

