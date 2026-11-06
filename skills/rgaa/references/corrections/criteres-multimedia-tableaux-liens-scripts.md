# Corrections RGAA — Thèmes 4 à 7 : Multimédia, Tableaux, Liens, Scripts

Blocs de correction par stack, à lire seulement pour rédiger la correction d’une NC. Le texte officiel et le reste de chaque critère sont dans `../criteres-multimedia-tableaux-liens-scripts.md`.

### 4.1–4.2 Transcription textuelle ou audiodescription présente et pertinente

#### Correction — React / JSX

```tsx
<audio controls src="/entretien.mp3" />
<a href="/entretien/transcription">Transcription textuelle de l’entretien</a>
```

#### Correction — Rails / ERB

```erb
<audio controls src="/entretien.mp3"></audio>
<a class="fr-link" href="/entretien/transcription">Transcription textuelle de l’entretien</a>
```

### 4.3–4.4 Sous-titres synchronisés présents et pertinents

#### Correction — React / JSX

```tsx
<figure>
  <video controls>
    <source src="/video.mp4" type="video/mp4" />
    <track kind="captions" src="/sous-titres.vtt" srcLang="fr" label="Français" default />
  </video>
  <figcaption>Présentation du service — <a href="/transcription">Transcription textuelle</a></figcaption>
</figure>
```

#### Correction — Rails / ERB

```erb
<figure class="fr-content-media" role="group">
  <video class="fr-responsive-vid" controls>
    <source src="/video.mp4" type="video/mp4">
    <track kind="captions" src="/sous-titres.vtt" srclang="fr" label="Français" default>
  </video>
  <figcaption class="fr-content-media__caption">
    Présentation du service
    <a class="fr-link" href="/transcription">Transcription textuelle</a>
  </figcaption>
</figure>
```

### 4.5–4.6 Audiodescription synchronisée présente et pertinente

#### Correction — React / JSX

```tsx
<figure>
  <video controls>
    <source src="/demarche.mp4" type="video/mp4" />
  </video>
  <figcaption>Déposer une demande en ligne — <a href="/demarche-audiodecrite">Version audiodécrite de la vidéo</a></figcaption>
</figure>
```

#### Correction — Rails / ERB

```erb
<figure class="fr-content-media" role="group">
  <video class="fr-responsive-vid" controls>
    <source src="/demarche.mp4" type="video/mp4">
  </video>
  <figcaption class="fr-content-media__caption">
    Déposer une demande en ligne
    <a class="fr-link" href="/demarche-audiodecrite">Version audiodécrite de la vidéo</a>
  </figcaption>
</figure>
```

### 4.7 Média clairement identifiable

#### Correction — React / JSX

```tsx
<h3>Présentation du service en deux minutes</h3>
<video controls src="/video.mp4" />
```

#### Correction — Rails / ERB

```erb
<h3 class="fr-h3">Présentation du service en deux minutes</h3>
<video class="fr-responsive-vid" controls src="/video.mp4"></video>
```

### 4.8–4.9 Média non temporel : alternative présente et pertinente

#### Correction — React / JSX

```tsx
<canvas id="carte" width={600} height={400} aria-hidden="true" />
<a href="/agences">Liste des agences par département</a>
```

#### Correction — Rails / ERB

```erb
<canvas id="carte" width="600" height="400" aria-hidden="true"></canvas>
<a class="fr-link" href="/agences">Liste des agences par département</a>
```

### 4.10 Son automatique contrôlable

#### Correction — React / JSX

```tsx
// ❌ <video autoPlay src="/video.mp4" />
// ✅ la lecture part à la demande
<video controls src="/video.mp4" />
```

#### Correction — Rails / ERB

```erb
<%# ❌ <video autoplay src="/video.mp4"></video> %>
<%# ✅ la lecture part à la demande %>
<video class="fr-responsive-vid" controls src="/video.mp4"></video>
```

### 4.11 Média temporel contrôlable au clavier et au pointeur

#### Correction — React / JSX

```tsx
// ❌ <div onClick={togglePlay}>Lecture</div>
// ✅ lecteur natif
<video controls src="/video.mp4" />

// ✅ lecteur personnalisé : de vrais boutons
<button type="button" onClick={togglePlay}>Lecture</button>
```

#### Correction — Rails / ERB

```erb
<%# ✅ lecteur natif %>
<video class="fr-responsive-vid" controls src="/video.mp4"></video>

<%# ✅ lecteur personnalisé : de vrais boutons %>
<button class="fr-btn" type="button">Lecture</button>
```

### 4.12 Média non temporel contrôlable au clavier et au pointeur

#### Correction — React / JSX

```tsx
<canvas id="carte" width={600} height={400} aria-hidden="true" />
<button type="button" onClick={zoomIn}>Zoomer sur la carte</button>
<button type="button" onClick={zoomOut}>Dézoomer sur la carte</button>
```

#### Correction — Rails / ERB

```erb
<canvas id="carte" width="600" height="400" aria-hidden="true"></canvas>
<button class="fr-btn" type="button">Zoomer sur la carte</button>
<button class="fr-btn" type="button">Dézoomer sur la carte</button>
```

### 4.13 Média compatible avec les technologies d’assistance

#### Correction — React / JSX

```tsx
<button type="button" aria-pressed={isMuted} onClick={toggleMute}>
  <svg aria-hidden="true" focusable="false">...</svg>
  Couper le son
</button>
```

#### Correction — Rails / ERB

```erb
<button class="fr-btn" type="button" aria-pressed="false">
  <svg aria-hidden="true" focusable="false">...</svg>
  Couper le son
</button>
```

### 5.1–5.2 Tableau complexe : résumé présent et pertinent

#### Correction — React / JSX

```tsx
<p id="resume-effectifs">Effectifs par année en colonnes, par département et par service en lignes.</p>
<table aria-describedby="resume-effectifs">
  {/* ... */}
</table>
```

#### Correction — Rails / ERB

```erb
<p id="resume-effectifs">Effectifs par année en colonnes, par département et par service en lignes.</p>
<table aria-describedby="resume-effectifs">
  <%# ... %>
</table>
```

### 5.3 Tableau de mise en forme : contenu linéarisé compréhensible

#### Correction — React / JSX

```tsx
<table role="presentation">
  <tbody>
    <tr>
      <td>Colonne de gauche</td>
      <td>Colonne de droite</td>
    </tr>
  </tbody>
</table>
```

#### Correction — Rails / ERB

```erb
<table role="presentation">
  <tbody>
    <tr>
      <td>Colonne de gauche</td>
      <td>Colonne de droite</td>
    </tr>
  </tbody>
</table>
```

### 5.4–5.5 Titre de tableau correctement associé et pertinent

#### Correction — React / JSX

```tsx
<table>
  <caption>Liste des agents par département</caption>
  {/* ... */}
</table>
```

#### Correction — Rails / ERB

```erb
<table>
  <caption>Liste des agents par département</caption>
  <%# ... %>
</table>
```

### 5.6–5.7 En-têtes correctement déclarés et associés

#### Correction — React / JSX

```tsx
<table>
  <caption>Liste des agents par département</caption>
  <thead>
    <tr>
      <th scope="col">Nom</th>
      <th scope="col">Département</th>
      <th scope="col">Rôle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Dupont</td>
      <td>Paris</td>
      <td>Admin</td>
    </tr>
  </tbody>
</table>
```

#### Correction — Rails / ERB

```erb
<div class="fr-table">
  <div class="fr-table__wrapper">
    <div class="fr-table__container">
      <div class="fr-table__content">
        <table>
          <caption>Liste des agents par département</caption>
          <thead>
            <tr>
              <th scope="col">Nom</th>
              <th scope="col">Département</th>
              <th scope="col">Rôle</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Dupont</td>
              <td>Paris</td>
              <td>Admin</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
```

### 5.8 Tableau de mise en forme sans éléments de données

#### Correction — React / JSX

```tsx
// ❌ <table role="presentation"><thead><tr><th>Menu</th></tr></thead>...</table>
// ✅ des cellules simples, ou mieux une mise en page en CSS
<table role="presentation">
  <tbody>
    <tr>
      <td>Menu</td>
    </tr>
  </tbody>
</table>
```

#### Correction — Rails / ERB

```erb
<%# ❌ <table role="presentation"><thead><tr><th>Menu</th></tr></thead>...</table> %>
<%# ✅ des cellules simples, ou mieux une mise en page en CSS %>
<table role="presentation">
  <tbody>
    <tr>
      <td>Menu</td>
    </tr>
  </tbody>
</table>
```

### 6.1 Chaque lien est-il explicite ?

#### Correction — React / JSX

```tsx
// ❌ Mauvais
<a href="/rapport">Cliquez ici</a>
<a href="/rapport">En savoir plus</a>

// ✅ Bon
<a href="/rapport">Consulter le rapport annuel 2024 (PDF, 2 Mo)</a>

// ✅ Acceptable avec contexte
<p>Le rapport annuel est disponible. <a href="/rapport">Télécharger le rapport (PDF, 2 Mo)</a></p>

// ✅ Lien image : alt pertinent
<a href="/accueil"><img src="/logo.png" alt="Retour à l'accueil" /></a>

// ✅ Lien répété : intitulé complété par un texte masqué
<a href="/demandes/123">Consulter<span className="fr-sr-only"> la demande 123</span></a>
```

#### Correction — Rails / ERB

```erb
<%# ❌ <a href="/rapport">En savoir plus</a> %>
<%# ✅ intitulé explicite %>
<a class="fr-link" href="/rapport">Consulter le rapport annuel 2024 (PDF, 2 Mo)</a>

<%# ✅ lien image : alt pertinent %>
<a href="/accueil"><img src="/logo.png" alt="Retour à l’accueil"></a>

<%# ✅ lien répété : intitulé complété par un texte masqué %>
<a class="fr-link" href="/demandes/123">Consulter<span class="fr-sr-only"> la demande 123</span></a>
```

### 6.2 Chaque lien a-t-il un intitulé ?

#### Correction — React / JSX

```tsx
// ❌ Lien vide
<a href="/page"></a>

// ✅ Texte masqué visuellement, icône ignorée
<a href="/page">
  <svg aria-hidden="true" focusable="false">...</svg>
  <span className="fr-sr-only">Accéder à la page détails</span>
</a>
```

#### Correction — Rails / ERB

```erb
<%# ❌ <a href="/page"></a> %>
<%# ✅ Texte masqué visuellement, icône ignorée %>
<a href="/page">
  <svg aria-hidden="true" focusable="false">...</svg>
  <span class="fr-sr-only">Accéder à la page détails</span>
</a>
```

### 7.1 Script compatible avec les technologies d'assistance

#### Correction — React / JSX

```tsx
// Accordéon
<button
  aria-expanded={isOpen}
  aria-controls="panel-1"
  onClick={() => setIsOpen(!isOpen)}
>
  Détails
</button>
<div id="panel-1" role="region" hidden={!isOpen}>
  Contenu du panneau
</div>

// Combobox : le champ garde le focus, la liste a un nom
<label htmlFor="ville">Ville</label>
<input
  id="ville"
  role="combobox"
  aria-autocomplete="list"
  aria-expanded={isOpen}
  aria-controls="villes"
  aria-activedescendant={activeId}
/>
<ul id="villes" role="listbox" aria-label="Villes proposées" hidden={!isOpen}>
  <li id="ville-paris" role="option" aria-selected={activeId === "ville-paris"}>Paris</li>
</ul>
```

#### Correction — Rails / ERB

```erb
<%# Accordéon DSFR %>
<section class="fr-accordion">
  <h3 class="fr-accordion__title">
    <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="panel-1">Détails</button>
  </h3>
  <div class="fr-collapse" id="panel-1">
    Contenu du panneau
  </div>
</section>

<%# Combobox ouverte : le champ garde le focus, aria-activedescendant désigne l’option active, la liste a un nom %>
<div class="fr-input-group">
  <label class="fr-label" for="ville">Ville</label>
  <input class="fr-input" type="text" id="ville" name="ville" role="combobox" aria-autocomplete="list" aria-expanded="true" aria-controls="villes" aria-activedescendant="ville-paris">
  <ul id="villes" role="listbox" aria-label="Villes proposées">
    <li id="ville-paris" role="option" aria-selected="true">Paris</li>
  </ul>
</div>
```

### 7.2 Alternative pertinente au script

#### Correction — React / JSX

```tsx
// ❌ <noscript></noscript>
// ✅ l'alternative donne accès à la même fonctionnalité
<noscript>
  <a href="/recherche-simple">Accéder au formulaire de recherche sans JavaScript</a>
</noscript>
```

#### Correction — Rails / ERB

```erb
<%# ❌ <noscript></noscript> %>
<%# ✅ l’alternative donne accès à la même fonctionnalité %>
<noscript>
  <a class="fr-link" href="/recherche-simple">Accéder au formulaire de recherche sans JavaScript</a>
</noscript>
```

### 7.3 Script contrôlable au clavier et au pointeur

#### Correction — React / JSX

```tsx
// ❌ Mauvais : div cliquable non accessible
<div onClick={handleClick}>Action</div>

// ✅ Bon : bouton natif
<button onClick={handleClick}>Action</button>

// ✅ Si div nécessaire : rôle + tabindex + clavier
<div
  role="button"
  tabIndex={0}
  onClick={handleClick}
  onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') handleClick(); }}
>
  Action
</div>
```

#### Correction — Rails / ERB

```erb
<%# ❌ <div data-action="click->panneau#ouvrir">Action</div> %>
<%# ✅ bouton natif %>
<button class="fr-btn" type="button" data-action="click->panneau#ouvrir">Action</button>
```

### 7.4 Changement de contexte : utilisateur averti ou en contrôle

#### Correction — React / JSX

```tsx
// ❌ <select onChange={(e) => navigate(e.target.value)}>...</select>
// ✅ le changement part d'un bouton explicite
<form onSubmit={handleSubmit}>
  <label htmlFor="departement">Département</label>
  <select id="departement" name="departement">
    <option value="75">Paris</option>
  </select>
  <button type="submit">Afficher les agences du département</button>
</form>
```

#### Correction — Rails / ERB

```erb
<%# ✅ le changement part d’un bouton explicite %>
<form action="/agences" method="get">
  <div class="fr-select-group">
    <label class="fr-label" for="departement">Département</label>
    <select class="fr-select" id="departement" name="departement">
      <option value="75">Paris</option>
    </select>
  </div>
  <button class="fr-btn" type="submit">Afficher les agences du département</button>
</form>
```

### 7.5 Messages de statut restitués

#### Correction — React / JSX

```tsx
// Message de succès
<div role="status">Formulaire envoyé avec succès.</div>

// Message d'erreur
<div role="alert">Erreur : le champ email est invalide.</div>

// Barre de progression
<div role="progressbar" aria-label="Envoi du fichier" aria-valuenow={75} aria-valuemin={0} aria-valuemax={100}>
  75%
</div>
```

#### Correction — Rails / ERB

```erb
<%# Message de succès %>
<div role="status">Formulaire envoyé avec succès.</div>

<%# Résultats mis à jour : la zone reste hors du cadre remplacé %>
<div role="status" id="resultats-nombre">12 résultats</div>
<turbo-frame id="resultats">...</turbo-frame>

<%# Message d’erreur %>
<div role="alert">Erreur : le champ e-mail est invalide.</div>

<%# Barre de progression %>
<div role="progressbar" aria-label="Envoi du fichier" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  75 %
</div>
```

