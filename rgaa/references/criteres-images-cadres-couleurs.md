# RGAA — Thèmes 1 à 3 : Images, Cadres, Couleurs

## Thème 1 — Images (9 critères)

### 1.1 Chaque image porteuse d'information a-t-elle une alternative textuelle ?

Balises concernées : `<img>`, `role="img"`, `<area>`, `<input type="image">`, `<svg>`, `<object type="image/...">`, `<embed type="image/...">`, `<canvas>`.

- `<img>` / `role="img"` : alternative via `alt`, `aria-label`, `aria-labelledby` ou `title`
- `<svg>` : doit avoir `role="img"` + alternative textuelle
- `<input type="image">` : attribut `alt`

**React :**
```tsx
// Image porteuse d'information
<img src="/chart.png" alt="Évolution du chiffre d'affaires 2024 : +15%" />

// SVG porteuse d'information
<svg role="img" aria-label="Logo du service">...</svg>

// Bouton image
<input type="image" src="/search.png" alt="Rechercher" />
```

### 1.2 Chaque image de décoration est-elle correctement ignorée ?

- `<img>` : `alt=""` (vide, pas absent)
- `<svg>` : `aria-hidden="true"` + pas de `role="img"`
- Ou `role="presentation"` sur l'image

**React :**
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

### 1.3 L'alternative textuelle est-elle pertinente ?

L'alternative doit être courte, concise (≤80 caractères recommandé) et décrire la fonction/information de l'image, pas son apparence.

### 1.4 CAPTCHA : l'alternative identifie-t-elle la nature et la fonction ?

Alternative type : "Code de sécurité anti-spam" (pas la réponse au CAPTCHA).

### 1.5 CAPTCHA : une solution d'accès alternatif existe-t-elle ?

Au moins une alternative d'un autre type (audio si visuel, etc.).

### 1.6 Image porteuse d'information : description détaillée si nécessaire ?

Pour les images complexes (graphiques, schémas), fournir une description détaillée via :
- `aria-describedby` référençant un passage de texte
- Lien/bouton adjacent vers la description
- Description adjacente visible

### 1.7 La description détaillée est-elle pertinente ?

La description détaillée doit contenir toute l'information véhiculée par l'image.

### 1.8 Les images texte sont-elles remplacées par du texte stylé ?

Préférer du texte CSS quand c'est possible. Exception : logos, marques.

### 1.9 Chaque légende d'image est-elle correctement reliée ?

Utiliser `<figure>` + `<figcaption>` :
```tsx
<figure>
  <img src="/photo.jpg" alt="Vue du bâtiment" />
  <figcaption>Le nouveau siège inauguré en 2024</figcaption>
</figure>
```

---

## Thème 2 — Cadres (2 critères)

### 2.1 Chaque cadre a-t-il un titre ?

Chaque `<iframe>` doit avoir un attribut `title`.

### 2.2 Le titre de cadre est-il pertinent ?

Le titre doit décrire le contenu du cadre.

```tsx
<iframe src="/map" title="Carte interactive de localisation des agences" />
```

---

## Thème 3 — Couleurs (3 critères)

### 3.1 L'information n'est pas donnée uniquement par la couleur

Toute information véhiculée par la couleur doit aussi être accessible par un autre moyen (texte, icône, motif, épaisseur de bordure...).

**React :**
```tsx
// ❌ Mauvais : statut uniquement par couleur
<span style={{ color: "red" }}>Erreur</span>

// ✅ Bon : couleur + texte + icône
<span style={{ color: "red" }}>
  <svg aria-hidden="true">...</svg> Erreur : champ obligatoire
</span>
```

### 3.2 Contraste texte/arrière-plan suffisant

| Type de texte | Ratio minimum |
|---|---|
| Texte < 24px (ou < 18.5px gras) | **4.5:1** |
| Texte ≥ 24px (ou ≥ 18.5px gras) | **3:1** |

### 3.3 Contraste des composants d'interface et éléments graphiques

Ratio minimum **3:1** entre :
- Les couleurs d'un composant d'interface et son arrière-plan
- Les couleurs contiguës d'un élément graphique porteur d'information
