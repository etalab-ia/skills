# RGAA — Thèmes 4 à 7 : Multimédia, Tableaux, Liens, Scripts

## Thème 4 — Multimédia (13 critères)

### Critères principaux

| Critère | Exigence |
|---------|----------|
| 4.1 | Média pré-enregistré : transcription textuelle ou audiodescription |
| 4.2 | Transcription/audiodescription pertinente |
| 4.3 | Sous-titres synchronisés pour média synchronisé pré-enregistré |
| 4.4 | Sous-titres pertinents |
| 4.5 | Audiodescription synchronisée si nécessaire |
| 4.6 | Audiodescription pertinente |
| 4.7 | Média clairement identifiable (texte adjacent) |
| 4.8 | Média non temporel : alternative accessible |
| 4.9 | Alternative pertinente |
| 4.10 | Son automatique contrôlable (≤3s ou stop/volume) |
| 4.11 | Contrôle clavier : lecture, pause, son, sous-titres, audiodescription |
| 4.12 | Média non temporel contrôlable au clavier |
| 4.13 | Compatible technologies d'assistance (API accessibilité) |

**React — Vidéo accessible :**
```tsx
<figure>
  <video controls>
    <source src="/video.mp4" type="video/mp4" />
    <track kind="captions" src="/sous-titres.vtt" srcLang="fr" label="Français" default />
    <track kind="descriptions" src="/audiodesc.vtt" srcLang="fr" label="Audiodescription" />
  </video>
  <figcaption>Présentation du service — <a href="/transcription">Transcription textuelle</a></figcaption>
</figure>
```

**Points clés :**
- `<track kind="captions">` (pas `subtitles`) pour les sous-titres d'accessibilité
- Son automatique interdit sauf ≤3 secondes ou contrôle immédiat
- Tout contrôle (lecture, pause, volume) doit être accessible au clavier

---

## Thème 5 — Tableaux (8 critères)

### 5.1–5.2 Tableau complexe : résumé présent et pertinent

Un tableau complexe (en-têtes multi-niveaux) nécessite un résumé expliquant sa structure.

### 5.3 Tableau de mise en forme : contenu linéarisé compréhensible

Tableau de mise en forme : `role="presentation"` obligatoire, pas de `<th>`, `<caption>`, `<thead>`, `<tfoot>`.

### 5.4–5.5 Titre de tableau correctement associé et pertinent

Via `<caption>`, `aria-label`, `aria-labelledby` ou `title`.

### 5.6–5.7 En-têtes correctement déclarés et associés

- En-têtes de colonnes : `<th scope="col">`
- En-têtes de lignes : `<th scope="row">`
- Tableaux complexes : `<th id="...">` + `<td headers="...">`

### 5.8 Tableau de mise en forme sans éléments de données

**React — Tableau de données accessible :**
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

---

## Thème 6 — Liens (2 critères)

### 6.1 Chaque lien est-il explicite ?

L'intitulé du lien (seul ou avec son contexte) doit permettre de comprendre sa fonction et sa destination.

**Contexte valide :** phrase englobante, paragraphe, élément de liste, titre précédent, cellule d'en-tête de tableau.

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
```

### 6.2 Chaque lien a-t-il un intitulé ?

Tout lien (`<a href>` ou `role="link"`) doit avoir un contenu accessible (texte, alt d'image, aria-label).

```tsx
// ❌ Lien vide
<a href="/page"></a>

// ✅ Lien avec aria-label
<a href="/page" aria-label="Accéder à la page détails">
  <svg aria-hidden="true">...</svg>
</a>
```

---

## Thème 7 — Scripts (5 critères)

### 7.1 Script compatible avec les technologies d'assistance

Tout composant généré par script doit exposer : nom, rôle, valeur, paramétrage et changements d'états via l'API d'accessibilité.

**React — Utiliser les bons rôles ARIA :**
```tsx
// Bouton toggle accessible
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
```

### 7.2 Alternative pertinente au script

Si JavaScript est désactivé, une alternative équivalente doit être disponible (via `<noscript>` ou rendu serveur).

### 7.3 Script contrôlable au clavier

Tout élément interactif créé par script doit être focusable et activable au clavier.

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

### 7.4 Changement de contexte : utilisateur averti ou en contrôle

Ne pas déclencher de changement de contexte (navigation, ouverture fenêtre, changement de focus) sans action explicite de l'utilisateur (clic sur bouton/lien).

### 7.5 Messages de statut restitués

| Type de message | Attribut ARIA |
|---|---|
| Succès, résultat d'action | `role="status"` ou `aria-live="polite" aria-atomic="true"` |
| Erreur, avertissement | `role="alert"` ou `aria-live="assertive" aria-atomic="true"` |
| Progression | `role="progressbar"` ou `role="log"` ou `role="status"` |

```tsx
// Message de succès
<div role="status">Formulaire envoyé avec succès.</div>

// Message d'erreur
<div role="alert">Erreur : le champ email est invalide.</div>

// Barre de progression
<div role="progressbar" aria-valuenow={75} aria-valuemin={0} aria-valuemax={100}>
  75%
</div>
```
