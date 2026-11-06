# RGAA — Thèmes 4 à 7 : Multimédia, Tableaux, Liens, Scripts

## Thème 4 — Multimédia (13 critères)

### 4.1–4.2 Transcription textuelle ou audiodescription présente et pertinente

4.1 : l’alternative existe, si le média en a besoin. 4.2 : elle restitue le contenu du média.

**Test :** Vérifier que chaque média temporel pré-enregistré qui le nécessite a une transcription textuelle adjacente, ou accessible par un lien ou un bouton adjacent. Une vidéo seule peut aussi avoir une version audio ou une audiodescription. Comparer ensuite cette alternative au contenu du média.
**Non-conformité type :** `<audio>` sans transcription ; transcription absente ou accessible uniquement après téléchargement.
**Impact :** sans transcription, la personne sourde ou malentendante, ou qui utilise une plage braille, n’accède pas au contenu parlé du média.
**Priorité :** 🔴 Bloquant

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

---

### 4.3–4.4 Sous-titres synchronisés présents et pertinents

4.3 : les sous-titres existent, si le média en a besoin. 4.4 : ils restituent les dialogues et les sons porteurs d’information.

**Test :** Vérifier que chaque `<video>` pré-enregistrée qui le nécessite a des sous-titres synchronisés : une `<track kind="captions">`, des sous-titres incrustés dans l’image ou fournis par le lecteur, ou une version alternative sous-titrée accessible par un lien ou un bouton adjacent. Une vidéo sans `<track>` n’est pas une NC en soi : regarder la vidéo pour vérifier qu’elle n’a pas de sous-titres incrustés. Quand les sous-titres passent par une `<track>`, `kind="captions"`, et non `subtitles`, désigne les sous-titres d’accessibilité. Comparer ensuite les sous-titres au média.
**Non-conformité type :** vidéo parlée sans aucun sous-titre, ni piste, ni incrustation, ni version alternative ; `<track kind="subtitles">` utilisée pour les sous-titres d’accessibilité.
**Impact :** sans sous-titres, la personne sourde ou malentendante perd le contenu parlé et les sons porteurs d’information.
**Priorité :** 🔴 Bloquant

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

---

### 4.5–4.6 Audiodescription synchronisée présente et pertinente

4.5 : l’audiodescription existe, si l’image porte une information absente de la bande-son. 4.6 : elle restitue cette information.

**Test :** Vérifier que chaque média vidéo pré-enregistré qui le nécessite a une audiodescription synchronisée, c’est-à-dire une narration sonore : piste audio intégrée à la vidéo, piste fournie par un lecteur qui la restitue, ou version audiodécrite reliée. Une `<track kind="descriptions">` ne suffit pas : c’est un texte que les navigateurs ne vocalisent pas d’eux-mêmes ; elle ne compte que si le lecteur utilisé la restitue, à vérifier en lecture. Comparer ensuite l’audiodescription à l’image.
**Non-conformité type :** Vidéo sans parole qui présente une démarche à l’écran, sans audiodescription ni version audiodécrite.
**Impact :** sans audiodescription, la personne aveugle ou malvoyante n’accède pas à ce qui n’est transmis que par l’image.
**Priorité :** 🟠 Majeur

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

---

### 4.7 Média clairement identifiable

**Test :** Vérifier qu’un texte adjacent (titre, légende) identifie clairement chaque média temporel.
**Non-conformité type :** `<video>` seule dans la page, sans titre ni légende.
**Impact :** sans texte adjacent, la personne qui utilise un lecteur d’écran ne sait pas quel média elle s’apprête à lancer.
**Priorité :** 🟡 Mineur

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

---

### 4.8–4.9 Média non temporel : alternative présente et pertinente

4.8 : l’alternative existe, si le média en a besoin. 4.9 : elle donne accès au même contenu et à des fonctionnalités similaires.

**Test :** Repérer les médias non temporels (`<canvas>`, `<object>`, `<embed>`, `<svg>` interactif). Vérifier qu’un lien ou un bouton adjacent, clairement identifiable, mène à une alternative, dans la page ou sur une autre page.
**Non-conformité type :** Carte interactive en `<canvas>` sans lien vers une liste équivalente.
**Impact :** sans alternative, la personne qui ne peut pas utiliser le média (lecteur d’écran, clavier seul) n’a aucun accès à son contenu.
**Priorité :** 🟠 Majeur

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

---

### 4.10 Son automatique contrôlable

Son automatique interdit sauf durée de 3 secondes au plus, ou possibilité de l’arrêter ou d’en régler le volume indépendamment du système.

**Test :** Vérifier qu'aucun son ne se déclenche automatiquement au chargement de la page, ou que sa durée est ≤ 3 secondes, ou qu'un mécanisme de contrôle est accessible dès le début de la page.
**Non-conformité type :** Vidéo ou audio en autoplay sans contrôle de volume/pause accessible.
**Impact :** un son lancé tout seul couvre la voix du lecteur d’écran : la personne qui l’utilise n’entend plus rien et ne trouve plus comment l’arrêter.
**Priorité :** 🟠 Majeur

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

---

### 4.11 Média temporel contrôlable au clavier et au pointeur

Au minimum lecture et pause ou stop ; activation et désactivation du son si le média en a ; des sous-titres et de l’audiodescription s’il en a.

**Test :** Vérifier que tous les contrôles du lecteur (lecture, pause, volume, sous-titres) sont accessibles au clavier et au pointeur.
**Non-conformité type :** Lecteur vidéo custom dont les boutons ne sont pas focusables au clavier.
**Impact :** sans commande utilisable au clavier, la personne qui ne se sert pas de la souris ne peut ni lancer ni arrêter le média.
**Priorité :** 🔴 Bloquant

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

---

### 4.12 Média non temporel contrôlable au clavier et au pointeur

**Test :** Vérifier que chaque fonctionnalité du média est accessible au clavier et au pointeur, ou qu’une fonctionnalité équivalente l’est dans la page.
**Non-conformité type :** Carte en `<canvas>` qui ne se déplace qu’à la souris, sans commande ni alternative.
**Impact :** une fonctionnalité réservée à la souris reste hors d’atteinte pour la personne qui navigue au clavier.
**Priorité :** 🔴 Bloquant

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

---

### 4.13 Média compatible avec les technologies d’assistance

**Test :** Vérifier que le nom, le rôle et l’état de chaque commande du média sont exposés aux technologies d’assistance, ou qu’une alternative compatible donne accès aux mêmes fonctionnalités.
**Non-conformité type :** Lecteur personnalisé dont les commandes sont des `<div>` cliquables ou des icônes sans nom accessible.
**Impact :** une commande sans nom ni rôle est annoncée au lecteur d’écran, au mieux, comme un simple élément : la personne qui l’utilise ne sait pas à quoi elle sert.
**Priorité :** 🟠 Majeur

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

---

## Thème 5 — Tableaux (8 critères)

### 5.1–5.2 Tableau complexe : résumé présent et pertinent

Un tableau complexe (en-têtes multi-niveaux) nécessite un résumé expliquant sa structure. 5.1 : le résumé existe. 5.2 : il explique la structure du tableau.

**Test :** Identifier les tableaux avec en-têtes sur plusieurs lignes/colonnes. Vérifier qu'un résumé de structure est fourni via `aria-describedby` ou un passage de texte adjacent.
**Non-conformité type :** Tableau avec en-têtes croisés sans aucun résumé de lecture.
**Impact :** sans résumé, la personne qui utilise un lecteur d’écran découvre la structure cellule par cellule et peine à comprendre comment lire le tableau.
**Priorité :** 🟠 Majeur

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

---

### 5.3 Tableau de mise en forme : contenu linéarisé compréhensible

Tableau de mise en forme : `role="presentation"` obligatoire, pas de `<th>`, `<caption>`, `<thead>`, `<tfoot>`.

**Test :** Identifier les `<table>` utilisés pour la mise en page (non pour des données). Vérifier qu'ils ont `role="presentation"` et ne contiennent pas de `<th>`, `<caption>`, `<thead>` ou `<tfoot>`.
**Non-conformité type :** `<table>` de mise en page sans `role="presentation"` ; utilisation de `<th>` dans un tableau de présentation.
**Impact :** sans `role="presentation"`, le lecteur d’écran annonce un tableau de données qui n’en est pas un, et fait perdre le fil du contenu.
**Priorité :** 🟠 Majeur

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

---

### 5.4–5.5 Titre de tableau correctement associé et pertinent

Via `<caption>`, `aria-label`, `aria-labelledby` ou `title`. 5.4 : le titre est associé au tableau. 5.5 : il identifie son contenu. Ces deux critères ne visent que les tableaux qui ont un titre : un tableau sans titre est NA ici, le RGAA n’en impose pas.

**Test :** Pour chaque tableau de données qui a un titre, vérifier qu’il est associé au tableau par `<caption>`, `title`, `aria-label` ou `aria-labelledby`, et qu’il décrit clairement son contenu.
**Non-conformité type :** Titre visible dans un `<p>` au-dessus du tableau, sans lien avec lui ; `<caption>Tableau 1</caption>` non descriptif.
**Impact :** un titre non associé n’est pas annoncé avec le tableau : la personne qui parcourt les tableaux au lecteur d’écran ne sait pas ce que chacun contient.
**Priorité :** 🟡 Mineur

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

---

### 5.6–5.7 En-têtes correctement déclarés et associés

- En-têtes de colonnes : `<th scope="col">`
- En-têtes de lignes : `<th scope="row">`
- Tableaux complexes : `<th id="...">` + `<td headers="...">`

5.6 : les en-têtes sont des `<th>` (ou portent le rôle correspondant). 5.7 : les cellules sont reliées à leurs en-têtes.

**Test :** Vérifier que chaque cellule d'en-tête utilise `<th>` avec `scope="col"` ou `scope="row"`. Pour les tableaux complexes, vérifier les attributs `id`/`headers`.
**Non-conformité type :** En-têtes de colonnes en `<td>` stylés en gras au lieu de `<th scope="col">` ; absence de `scope` sur les `<th>`.
**Impact :** sans en-têtes associés, le lecteur d’écran annonce les cellules sans leur en-tête de ligne ou de colonne : les données n’ont plus de sens.
**Priorité :** 🟠 Majeur

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

---

### 5.8 Tableau de mise en forme sans éléments de données

**Test :** Vérifier l'absence de `<th>`, `<caption>`, `<thead>`, `<tfoot>`, `summary` dans les tableaux de présentation.
**Non-conformité type :** `<table>` de mise en page contenant des `<th>`.
**Impact :** des éléments de tableau de données dans une mise en page font annoncer des en-têtes et un titre sans objet au lecteur d’écran.
**Priorité :** 🟠 Majeur

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

---

## Thème 6 — Liens (2 critères)

### 6.1 Chaque lien est-il explicite ?

L'intitulé du lien (seul ou avec son contexte) doit permettre de comprendre sa fonction et sa destination.

**Contexte valide :** phrase englobante, paragraphe, élément de liste, titre précédent, cellule d'en-tête de tableau.

**Test :** Identifier tous les `<a href>`. Lire leur texte seul (hors contexte). Si ambigu ("cliquez ici", "en savoir plus", "lire la suite"), vérifier que le contexte immédiat (phrase, `aria-label`, `aria-labelledby`) lève l'ambiguïté.
**Non-conformité type :** `<a href="/rapport">En savoir plus</a>` sans contexte permettant de comprendre de quel rapport il s'agit.
**Impact :** dans la liste des liens du lecteur d’écran, des intitulés comme « Cliquez ici » se ressemblent tous : la destination reste inconnue tant que le texte autour n’a pas été lu.
**Priorité :** 🟠 Majeur

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

---

### 6.2 Chaque lien a-t-il un intitulé ?

Tout lien (`<a href>` ou `role="link"`) doit contenir un intitulé : du texte, éventuellement masqué visuellement, ou l’alternative d’une image.

**Test :** Vérifier que chaque `<a>` contient du texte ou un `alt` si l'enfant est une image. Repérer les liens contenant uniquement une icône SVG sans texte.
**Non-conformité type :** `<a href="/page"><svg>...</svg></a>` sans `aria-label` ni texte.
**Impact :** un lien sans intitulé est annoncé par son adresse, ou sans rien : la personne qui utilise un lecteur d’écran ne sait pas où il mène.
**Priorité :** 🔴 Bloquant

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

---

## Thème 7 — Scripts (5 critères)

### 7.1 Script compatible avec les technologies d'assistance

Tout composant généré par script doit exposer : nom, rôle, valeur, paramétrage et changements d'états via l'API d'accessibilité.

**Test :** Vérifier que les composants interactifs custom (accordéon, onglets, menu déroulant, combobox, carrousel) ont les rôles ARIA appropriés (`role`, `aria-expanded`, `aria-selected`, `aria-controls`...).
**Non-conformité type :** Accordéon custom sans `aria-expanded` sur le bouton ; menu déroulant sans `aria-haspopup` ; liste `role="listbox"` sans nom accessible.
**Impact :** un composant sans rôle, sans nom ou sans état annoncé ne dit rien au lecteur d’écran : la personne qui l’utilise ne sait ni ce qu’il fait, ni s’il est ouvert.
**Priorité :** 🟠 Majeur

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

---

### 7.2 Alternative pertinente au script

Le critère ne porte que sur les scripts qui ont une alternative : elle doit donner accès à des contenus et à des fonctionnalités similaires. Un script sans alternative relève des autres critères du thème (NA ici) : le RGAA n’exige pas de fonctionnement sans JavaScript.

**Test :** Repérer les alternatives aux fonctionnalités JavaScript (`<noscript>`, page alternative, rendu serveur, composant équivalent dans la page). Vérifier que chacune donne accès aux mêmes contenus et à des fonctionnalités similaires.
**Non-conformité type :** `<noscript>` vide ; alternative qui ne donne accès qu’à une partie de la fonctionnalité.
**Impact :** une alternative vide ou partielle laisse sans solution la personne qui en dépend, parce que le script ne fonctionne pas dans son environnement.
**Priorité :** 🟠 Majeur

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

---

### 7.3 Script contrôlable au clavier et au pointeur

Tout élément interactif créé par script doit être focusable et activable au clavier et au pointeur, à moins qu’un autre élément accessible de ces deux façons réalise la même action dans la page.

**Test :** Parcourir la page au clavier (Tab, Entrée, Espace, flèches). Vérifier que tous les éléments interactifs sont atteignables et utilisables sans souris. Repérer les `<div onClick>` ou `<span onClick>` non focusables. Une option de combobox en `<li onClick>` reste conforme si le champ permet de la choisir au clavier (flèches, puis Entrée).
**Non-conformité type :** `<div onClick={handleClick}>Action</div>` non focusable ; composant React custom non opérable au clavier.
**Impact :** une action réservée à la souris est inaccessible à la personne qui navigue au clavier, avec une commande vocale ou un contacteur.
**Priorité :** 🔴 Bloquant

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

---

### 7.4 Changement de contexte : utilisateur averti ou en contrôle

Un script qui initie un changement de contexte doit être déclenché par un bouton ou un lien explicite, ou annoncé avant par un texte qui décrit l’action et le type de changement.

Un changement de contexte modifie l’agent utilisateur, la zone de restitution, le focus, ou un contenu qui change la signification de la page. Un changement de contenu n’en est pas toujours un : déployer un menu ou une arborescence n’en est pas un.

**Test :** Repérer les scripts qui ouvrent une page, déplacent le focus, ou mettent à jour une partie essentielle de la page. Vérifier qu’un bouton ou un lien explicite les déclenche, ou qu’un texte les annonce avant.
**Non-conformité type :** Navigation ou soumission automatique au changement de valeur d'un `<select>`, sans bouton de validation ni texte qui l’annonce. La simple mise à jour d’un détail secondaire de la page n’en est pas une.
**Impact :** un changement sans avertissement désoriente la personne qui ne voit pas toute la page, au lecteur d’écran ou en fort zoom : elle ne comprend pas ce qui vient de changer.
**Priorité :** 🟠 Majeur

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

---

### 7.5 Messages de statut restitués

| Type de message | Attribut ARIA |
|---|---|
| Succès, résultat d'action | `role="status"` ou `aria-live="polite" aria-atomic="true"` |
| Erreur, avertissement | `role="alert"` ou `aria-live="assertive" aria-atomic="true"` |
| Progression | `role="progressbar"` ou `role="log"` ou `role="status"` |

**Test :** Identifier les messages dynamiques (confirmation d'envoi, erreurs, résultats de recherche chargés dynamiquement). Vérifier qu'ils ont `role="status"` ou `role="alert"` pour être annoncés par les lecteurs d'écran. La zone doit exister dans la page avant l’arrivée du message et rester hors de la partie remplacée (`turbo-frame`, composant recréé), sinon l’annonce n’est pas fiable.
**Non-conformité type :** Message de confirmation "Formulaire envoyé" apparaissant visuellement mais sans `role="status"` ni `aria-live`.
**Impact :** une confirmation, une erreur ou un résultat de recherche apparaît à l’écran sans être annoncé : la personne qui utilise un lecteur d’écran ne sait pas que quelque chose a changé.
**Priorité :** 🟠 Majeur

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
