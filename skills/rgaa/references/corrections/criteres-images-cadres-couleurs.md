# Corrections RGAA — Thèmes 1 à 3 : Images, Cadres, Couleurs

Blocs de correction par stack, à lire seulement pour rédiger la correction d’une NC. Le texte officiel et le reste de chaque critère sont dans `../criteres-images-cadres-couleurs.md`.

### 1.1 Chaque image porteuse d'information a-t-elle une alternative textuelle ?

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

### 1.2 Chaque image de décoration est-elle correctement ignorée ?

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

### 1.3 L'alternative textuelle est-elle pertinente ?

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

### 1.4 CAPTCHA : l'alternative identifie-t-elle la nature et la fonction ?

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

### 1.5 CAPTCHA : une solution d'accès alternatif existe-t-elle ?

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

### 1.6 Image porteuse d'information : description détaillée si nécessaire ?

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

### 1.7 La description détaillée est-elle pertinente ?

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

### 1.8 Les images texte sont-elles remplacées par du texte stylé ?

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

### 1.9 Chaque légende d'image est-elle correctement reliée ?

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

### 2.1 Chaque cadre a-t-il un titre ?

#### Correction — React / JSX

```tsx
<iframe src="/map" title="Carte interactive de localisation des agences" />
```

#### Correction — Rails / ERB

```erb
<iframe src="/map" title="Carte interactive de localisation des agences"></iframe>
```

### 2.2 Le titre de cadre est-il pertinent ?

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

### 3.1 L'information n'est pas donnée uniquement par la couleur

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

### 3.2 Contraste texte/arrière-plan suffisant

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

### 3.3 Contraste des composants d'interface et éléments graphiques

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

