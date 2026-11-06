# RGAA — Thèmes 1 à 3 : Images, Cadres, Couleurs

## Thème 1 — Images (9 critères)

### 1.1 Chaque image porteuse d'information a-t-elle une alternative textuelle ?

Balises concernées : `<img>`, `role="img"`, `<area>`, `<input type="image">`, `<svg>`, `<object type="image/...">`, `<embed type="image/...">`, `<canvas>`.

- `<img>` / `role="img"` : alternative via `alt`, `aria-label`, `aria-labelledby` ou `title`
- `<svg>` : doit avoir `role="img"` + alternative textuelle
- `<input type="image">` : attribut `alt`

**Test :** Vérifier que chaque `<img>` informatif possède un attribut `alt` non vide et présent. Vérifier que chaque `<svg>` informatif a `role="img"` + `aria-label` ou un `<title>` enfant. Vérifier que `<input type="image">` a un `alt`.
**Non-conformité type :** `<img src="chart.png">` sans attribut `alt` ; `<svg>` sans `role="img"` ni `aria-label`.
**Impact :** sans alternative, le lecteur d’écran ignore l’image ou lit son nom de fichier : la personne qui l’utilise perd l’information qu’elle porte.
**Priorité :** 🔴 Bloquant

#### Correction — React / JSX

```tsx
// Image porteuse d'information
<img src="/chart.png" alt="Évolution du chiffre d'affaires 2024 : +15%" />

// SVG porteuse d'information
<svg role="img" aria-label="Logo du service">...</svg>

// Bouton image
<input type="image" src="/search.png" alt="Rechercher" />
```

#### Correction — Rails / ERB

```erb
<%# Image porteuse d’information — classe fr-* du DSFR %>
<img class="fr-responsive-img" src="/chart.png" alt="Évolution du chiffre d’affaires 2024 : +15 %">

<%# SVG porteuse d’information %>
<svg role="img" aria-label="Logo du service">...</svg>

<%# Bouton image %>
<input type="image" src="/search.png" alt="Rechercher">
```

---

### 1.2 Chaque image de décoration est-elle correctement ignorée ?

- `<img>` : `alt=""` (vide, pas absent)
- `<svg>` : `aria-hidden="true"` + pas de `role="img"`
- Ou `role="presentation"` sur l'image

**Test :** Vérifier que chaque `<img>` décoratif a `alt=""` (attribut présent mais vide). Vérifier que les `<svg>` décoratifs ont `aria-hidden="true"`.
**Non-conformité type :** `<img src="decoration.png">` sans attribut `alt` (attribut absent) ; `<svg>` décoratif sans `aria-hidden`.
**Impact :** une image décorative non ignorée est annoncée, parfois par son nom de fichier : ce bruit ralentit la lecture au lecteur d’écran et laisse croire à une information.
**Priorité :** 🔴 Bloquant

#### Correction — React / JSX

```tsx
// Image décorative
<img src="/decoration.png" alt="" />

// SVG décorative
<svg aria-hidden="true" focusable="false">...</svg>

// Icône décorative dans un bouton avec texte
<button>
  <svg aria-hidden="true" focusable="false">...</svg>
  Rechercher
</button>
```

#### Correction — Rails / ERB

```erb
<%# Image décorative : alt présent et vide %>
<img src="/decoration.png" alt="">

<%# SVG décorative %>
<svg aria-hidden="true" focusable="false">...</svg>

<%# Icône décorative dans un bouton avec texte %>
<button class="fr-btn">
  <svg aria-hidden="true" focusable="false">...</svg>
  Rechercher
</button>
```

---

### 1.3 L'alternative textuelle est-elle pertinente ?

L'alternative doit être courte, concise (≤80 caractères recommandé) et décrire la fonction ou l'information de l'image, pas son apparence.

**Test :** Lire les valeurs `alt` et vérifier qu'elles transmettent l'information utile (pas "image", "photo", le nom du fichier, ni une redite du texte adjacent).
**Non-conformité type :** `alt="image"`, `alt="logo.png"`, `alt="Photo"`, ou `alt` reprenant mot pour mot le texte adjacent.
**Impact :** une alternative générique est bien annoncée au lecteur d’écran, mais elle ne transmet rien : la personne qui l’utilise ignore ce que l’image apporte. Une alternative qui redit le texte voisin lui fait entendre deux fois la même chose.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```tsx
// ❌ <img src="/logo.png" alt="logo.png" />
// ✅ l'alternative dit la fonction de l'image
<a href="/">
  <img src="/logo.png" alt="Accueil du service" />
</a>

// ❌ <img src="/etape.svg" alt="Être habilité" /> à côté du texte « Être habilité »
// ✅ si l'image n'ajoute rien au texte voisin, elle est décorative (voir 1.2)
<img src="/etape.svg" alt="" />
<span>Être habilité</span>
```

#### Correction — Rails / ERB

```erb
<%# ❌ <img src="/logo.png" alt="logo.png"> %>
<%# ✅ l’alternative dit la fonction de l’image %>
<a href="/">
  <img src="/logo.png" alt="Accueil du service">
</a>

<%# ❌ <img src="/etape.svg" alt="Être habilité"> à côté du texte « Être habilité » %>
<%# ✅ si l’image n’ajoute rien au texte voisin, elle est décorative (voir 1.2) %>
<img src="/etape.svg" alt="">
<span>Être habilité</span>
```

---

### 1.4 CAPTCHA : l'alternative identifie-t-elle la nature et la fonction ?

Alternative type : "Code de sécurité anti-spam" (pas la réponse au CAPTCHA).

**Test :** Vérifier que l'image CAPTCHA a un `alt` décrivant ce qu'elle est ("Code de vérification visuel") sans en révéler la réponse.
**Non-conformité type :** CAPTCHA sans `alt`, ou `alt` vide.
**Impact :** sans alternative qui dit sa nature, la personne qui utilise un lecteur d’écran ne comprend pas qu’un contrôle lui est demandé et reste bloquée avant d’envoyer le formulaire.
**Priorité :** 🔴 Bloquant

#### Correction — React / JSX

```tsx
// ✅ nature et fonction, sans la réponse
<img src="/captcha" alt="Code de vérification visuel anti-spam" />
```

#### Correction — Rails / ERB

```erb
<%# ✅ nature et fonction, sans la réponse %>
<img src="/captcha" alt="Code de vérification visuel anti-spam">
```

---

### 1.5 CAPTCHA : une solution d'accès alternatif existe-t-elle ?

Au moins une alternative d'un autre type (audio si visuel, etc.).

**Test :** Vérifier qu'un CAPTCHA visuel propose un CAPTCHA audio ou une autre méthode accessible.
**Non-conformité type :** CAPTCHA visuel unique sans alternative.
**Impact :** un CAPTCHA seulement visuel arrête toute personne qui ne peut pas le lire, par exemple au lecteur d’écran : le service lui reste fermé.
**Priorité :** 🔴 Bloquant

#### Correction — React / JSX

```tsx
// ✅ une autre forme d'accès, ici audio
<img src="/captcha" alt="Code de vérification visuel anti-spam" />
<a href="/captcha/audio">Écouter le code de vérification</a>
```

#### Correction — Rails / ERB

```erb
<%# ✅ une autre forme d’accès, ici audio %>
<img src="/captcha" alt="Code de vérification visuel anti-spam">
<a class="fr-link" href="/captcha/audio">Écouter le code de vérification</a>
```

---

### 1.6 Image porteuse d'information : description détaillée si nécessaire ?

Pour les images complexes (graphiques, schémas, cartes), fournir une description détaillée via :
- `aria-describedby` référençant un passage de texte
- Lien/bouton adjacent vers la description
- Description adjacente visible

**Test :** Identifier les images complexes (graphiques, tableaux en image, infographies). Vérifier qu'elles ont une description détaillée accessible via `aria-describedby`, un lien adjacent ou un texte visible.
**Non-conformité type :** Graphique complexe avec seulement `alt="Graphique d'évolution"` sans description des données.
**Impact :** une alternative courte ne peut pas porter les données d’un graphique : sans description, la personne qui ne voit pas l’image n’accède pas aux valeurs.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```tsx
// ✅ alternative courte + description reliée
<img
  src="/evolution.png"
  alt="Évolution des demandes en 2024"
  aria-describedby="evolution-description"
/>
<p id="evolution-description">
  Les demandes passent de 1 200 en janvier à 1 800 en décembre.
</p>
```

#### Correction — Rails / ERB

```erb
<%# ✅ alternative courte + description reliée %>
<img class="fr-responsive-img" src="/evolution.png" alt="Évolution des demandes en 2024" aria-describedby="evolution-description">
<p id="evolution-description">
  Les demandes passent de 1 200 en janvier à 1 800 en décembre.
</p>
```

---

### 1.7 La description détaillée est-elle pertinente ?

La description détaillée doit contenir toute l'information véhiculée par l'image.

**Test :** Lire la description détaillée et vérifier qu'elle retranscrit toutes les données/informations de l'image (valeurs, tendances, légendes...).
**Non-conformité type :** Description qui mentionne le titre du graphique mais pas les valeurs.
**Impact :** une description partielle laisse croire que l’information est complète : la personne qui ne voit pas l’image n’a qu’une partie des données et ne le sait pas.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```tsx
// ❌ <p id="evolution-description">Graphique des demandes en 2024.</p>
// ✅ toutes les valeurs de l'image
<p id="evolution-description">
  Demandes par trimestre en 2024 : 1 200, 1 350, 1 500, puis 1 800.
</p>
```

#### Correction — Rails / ERB

```erb
<%# ❌ <p id="evolution-description">Graphique des demandes en 2024.</p> %>
<%# ✅ toutes les valeurs de l’image %>
<p id="evolution-description">
  Demandes par trimestre en 2024 : 1 200, 1 350, 1 500, puis 1 800.
</p>
```

---

### 1.8 Les images texte sont-elles remplacées par du texte stylé ?

Préférer du texte CSS quand c'est possible. Exception : logos, marques.

**Test :** Repérer les `<img>` contenant du texte (bannières, titres en image). Vérifier qu'elles ne peuvent pas être reproduites en CSS/HTML.
**Non-conformité type :** Titre de section rendu comme image PNG au lieu d'un `<h2>` stylé.
**Impact :** le texte en image devient flou à l’agrandissement et ne peut pas être reformaté : la personne qui zoome ou adapte l’affichage (police, espacement, couleurs) le lit mal.
**Priorité :** 🟡 Mineur

#### Correction — React / JSX

```tsx
// ❌ <img src="/titre-nos-services.png" alt="Nos services" />
// ✅ du vrai texte, mis en forme en CSS
<h2>Nos services</h2>
```

#### Correction — Rails / ERB

```erb
<%# ❌ <img src="/titre-nos-services.png" alt="Nos services"> %>
<%# ✅ du vrai texte, mis en forme en CSS %>
<h2 class="fr-h2">Nos services</h2>
```

---

### 1.9 Chaque légende d'image est-elle correctement reliée ?

Utiliser `<figure>` avec `role="figure"` ou `role="group"`, un `aria-label` identique au contenu de la légende, et `<figcaption>`.

**Test :** Vérifier que les images accompagnées d'une légende sont dans un `<figure>` avec `role="figure"` ou `role="group"`, un `aria-label` identique au contenu de la légende et un `<figcaption>` enfant.
**Non-conformité type :** `<img>` suivi d'un `<p>` comme légende sans structure `<figure>` ; `<figure>` sans `role` ni `aria-label`.
**Impact :** une légende non reliée est lue comme un paragraphe sans rapport : la personne qui utilise un lecteur d’écran ne sait pas qu’elle se rapporte à l’image.
**Priorité :** 🟡 Mineur

#### Correction — React / JSX

```tsx
<figure role="figure" aria-label="Le nouveau siège inauguré en 2024">
  <img src="/photo.jpg" alt="Vue du bâtiment" />
  <figcaption>Le nouveau siège inauguré en 2024</figcaption>
</figure>
```

#### Correction — Rails / ERB

```erb
<figure class="fr-content-media" role="group" aria-label="Le nouveau siège inauguré en 2024">
  <div class="fr-content-media__img">
    <img class="fr-responsive-img" src="/photo.jpg" alt="Vue du bâtiment">
  </div>
  <figcaption class="fr-content-media__caption">Le nouveau siège inauguré en 2024</figcaption>
</figure>
```

---

## Thème 2 — Cadres (2 critères)

### 2.1 Chaque cadre a-t-il un titre ?

Chaque `<iframe>` doit avoir un attribut `title`.

**Test :** Vérifier que chaque `<iframe>` dans le code a un attribut `title` présent et non vide.
**Non-conformité type :** `<iframe src="/map">` sans attribut `title`.
**Impact :** sans titre, le lecteur d’écran annonce un cadre sans nom, ou son adresse : la personne qui l’utilise ne sait pas s’il vaut la peine d’y entrer.
**Priorité :** 🔴 Bloquant

#### Correction — React / JSX

```tsx
<iframe src="/map" title="Carte interactive de localisation des agences" />
```

#### Correction — Rails / ERB

```erb
<iframe src="/map" title="Carte interactive de localisation des agences"></iframe>
```

---

### 2.2 Le titre de cadre est-il pertinent ?

Le titre doit décrire le contenu du cadre.

**Test :** Lire les valeurs `title` des `<iframe>` et vérifier qu'elles décrivent le contenu (pas "iframe", "frame", "cadre").
**Non-conformité type :** `title="iframe1"` ou `title="Cadre"`.
**Impact :** un titre générique, restitué seul dans la liste des cadres du lecteur d’écran, ne dit pas ce que le cadre contient.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```tsx
// ❌ <iframe src="/map" title="iframe1" />
// ✅ le titre décrit le contenu du cadre
<iframe src="/map" title="Carte interactive de localisation des agences" />
```

#### Correction — Rails / ERB

```erb
<%# ❌ <iframe src="/map" title="iframe1"></iframe> %>
<%# ✅ le titre décrit le contenu du cadre %>
<iframe src="/map" title="Carte interactive de localisation des agences"></iframe>
```

---

## Thème 3 — Couleurs (3 critères)

### 3.1 L'information n'est pas donnée uniquement par la couleur

Toute information véhiculée par la couleur doit aussi être transmise autrement (entrée « Information (donnée par la couleur) » du glossaire) :

- par une indication textuelle visible, qui suffit seule ;
- ou par un moyen graphique (pictogramme, forme, style de bordure) ou un autre style typographique (gras, italique, taille), à condition de l’accompagner d’un complément dans le code (`aria-label`, `title`, texte masqué, `aria-current`…).

**Test :** Identifier les éléments dont l'état ou l'information est signalé par une couleur (rouge = erreur, vert = succès, champ obligatoire en rouge...). Vérifier qu’une indication textuelle visible est présente, ou un moyen graphique ou typographique accompagné d’un complément dans le code.
**Non-conformité type :** Erreur de formulaire signalée uniquement par un fond rouge, sans icône ni texte explicatif ; page active du menu signalée par la couleur et le gras, sans `aria-current`.
**Impact :** l’information n’est pas restituée au lecteur d’écran, et la personne qui distingue mal les couleurs ne perçoit pas la différence, par exemple entre un succès et une erreur.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```tsx
// ❌ Erreur signalée uniquement par la couleur
<label htmlFor="email">Adresse e-mail</label>
<input id="email" type="email" style={{ borderColor: "#ce0500" }} />

// ✅ Indication textuelle visible
<label htmlFor="email">Adresse e-mail</label>
<input id="email" type="email" aria-invalid="true" aria-describedby="email-error" />
<p id="email-error">Erreur : saisissez une adresse e-mail valide.</p>

// ✅ Couleur et gras accompagnés d'un complément dans le code
<a href="/aide" aria-current="page" style={{ color: "#000091", fontWeight: "bold" }}>Aide</a>
```

#### Correction — Rails / ERB

```erb
<%# ✅ Indication textuelle visible — classes fr-* du DSFR %>
<div class="fr-input-group fr-input-group--error">
  <label class="fr-label" for="email">Adresse e-mail</label>
  <input class="fr-input" type="email" id="email" name="email" aria-invalid="true" aria-describedby="email-messages">
  <div class="fr-messages-group" id="email-messages" aria-live="polite">
    <p class="fr-message fr-message--error" id="email-error">Saisissez une adresse e-mail valide.</p>
  </div>
</div>

<%# ✅ Couleur et gras accompagnés d’un complément dans le code %>
<a class="fr-link" href="/aide" aria-current="page" style="font-weight: bold">Aide</a>
```

---

### 3.2 Contraste texte/arrière-plan suffisant

| Type de texte | Ratio minimum |
|---|---|
| Texte < 24px (ou < 18.5px gras) | **4.5:1** |
| Texte ≥ 24px (ou ≥ 18.5px gras) | **3:1** |

**Test :** Identifier les couleurs de texte et d'arrière-plan dans le CSS. Calculer le ratio de contraste (outil : WebAIM Contrast Checker). Vérifier les seuils selon la taille et le graissage. Les textes sur images ou dégradés nécessitent une vérification visuelle.
**Non-conformité type :** Texte gris clair `#999` sur fond blanc `#fff` (ratio ≈ 2.8:1, insuffisant pour texte normal).
**Impact :** un contraste insuffisant rend le texte difficile, voire impossible, à lire pour une personne malvoyante, ou sur un écran en plein soleil.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```tsx
// ❌ style={{ color: "#999", backgroundColor: "#fff" }} : ratio ≈ 2.8:1
// ✅ #666 sur #fff : ratio ≈ 5.7:1
<p style={{ color: "#666", backgroundColor: "#fff" }}>Dernière mise à jour : 12 mars</p>
```

#### Correction — Rails / ERB

```erb
<%# ❌ style="color: #999; background-color: #fff" : ratio ≈ 2.8:1 %>
<%# ✅ #666 sur #fff : ratio ≈ 5.7:1 %>
<p style="color: #666; background-color: #fff">Dernière mise à jour : 12 mars</p>
```

---

### 3.3 Contraste des composants d'interface et éléments graphiques

Ratio minimum **3:1** entre :
- Les couleurs d'un composant d'interface et son arrière-plan
- Les couleurs contiguës d'un élément graphique porteur d'information

**Test :** Vérifier le contraste des bordures de champs de formulaire, boutons, icônes informatives, et éléments graphiques par rapport à leur arrière-plan.
**Non-conformité type :** Bordure de champ de formulaire `#ccc` sur fond blanc `#fff` (ratio ≈ 1.6:1, insuffisant).
**Impact :** un contour trop pâle empêche la personne malvoyante de repérer le champ ou le bouton : elle ne voit pas où agir.
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```tsx
// ❌ borderColor: "#ccc" sur fond #fff : ratio ≈ 1.6:1
// ✅ #767676 sur #fff : ratio ≈ 4.5:1
<label htmlFor="ville">Ville</label>
<input id="ville" type="text" style={{ border: "1px solid #767676", backgroundColor: "#fff" }} />
```

#### Correction — Rails / ERB

```erb
<%# ❌ border-color: #ccc sur fond #fff : ratio ≈ 1.6:1 %>
<%# ✅ #767676 sur #fff : ratio ≈ 4.5:1 %>
<label class="fr-label" for="ville">Ville</label>
<input type="text" id="ville" name="ville" style="border: 1px solid #767676; background-color: #fff">
```
