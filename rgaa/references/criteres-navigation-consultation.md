# RGAA — Thèmes 12–13 : Navigation, Consultation

## Thème 12 — Navigation (11 critères)

### 12.1 Deux systèmes de navigation minimum

Chaque ensemble de pages doit proposer au moins deux parmi :
- Menu de navigation
- Plan du site
- Moteur de recherche

### 12.2 Menu et barres de navigation à la même place

Le menu doit être à la même position visuelle et dans le même ordre dans le code source sur toutes les pages.

### 12.3–12.5 Plan du site et moteur de recherche

- Plan du site pertinent et représentatif de l'architecture
- Liens fonctionnels et cohérents
- Accessibles depuis une fonctionnalité identique sur toutes les pages

### 12.6 Zones de regroupement identifiables

Chaque zone principale doit être identifiable via landmark ARIA ou titre :

```tsx
<header role="banner">...</header>          {/* En-tête */}
<nav role="navigation" aria-label="Menu principal">...</nav>
<main role="main">...</main>                {/* Contenu principal */}
<footer role="contentinfo">...</footer>     {/* Pied de page */}
<form role="search" aria-label="Recherche">...</form>
```

**Plusieurs `<nav>` :** différencier avec `aria-label` :
```tsx
<nav aria-label="Menu principal">...</nav>
<nav aria-label="Menu secondaire">...</nav>
<nav aria-label="Fil d'Ariane">...</nav>
```

### 12.7 Lien d'évitement vers le contenu principal

Doit être le premier lien de la page (visible ou visible au focus) :

```tsx
<body>
  <a href="#contenu" className="skip-link">Aller au contenu principal</a>
  <header>...</header>
  <nav>...</nav>
  <main id="contenu">...</main>
</body>
```

```css
.skip-link {
  position: absolute;
  left: -9999px;
}
.skip-link:focus {
  position: static;
  /* ou position visible */
}
```

### 12.8 Ordre de tabulation cohérent

L'ordre du focus (Tab) doit suivre l'ordre logique de lecture. Ne pas utiliser `tabindex > 0`.

### 12.9 Pas de piège au clavier

Tout élément focusable doit permettre d'atteindre l'élément suivant/précédent via Tab/Shift+Tab.

**Attention aux modales :** le focus doit être piégé dans la modale tant qu'elle est ouverte, mais libéré à sa fermeture.

### 12.10 Raccourcis clavier mono-touche contrôlables

Si un raccourci utilise une seule touche (lettre, chiffre, ponctuation), l'utilisateur doit pouvoir :
- Le désactiver
- Le reconfigurer avec une touche modificatrice (Ctrl, Alt, Maj)
- Ou le limiter au focus sur le composant concerné

### 12.11 Contenus additionnels atteignables au clavier

Les contenus apparaissant au survol/focus/activation doivent être atteignables au clavier.

---

## Thème 13 — Consultation (12 critères)

### 13.1 Limites de temps contrôlables

L'utilisateur doit pouvoir :
- Arrêter/relancer un rafraîchissement automatique
- Augmenter la limite de temps (×10 minimum)
- Être averti 20s avant l'expiration

Redirection `<meta>` : doit être immédiate (pas de délai).

### 13.2 Pas d'ouverture de fenêtre sans action utilisateur

Ne pas ouvrir de popup/nouvelle fenêtre automatiquement au chargement.

Pour les liens ouvrant une nouvelle fenêtre :
```tsx
// Indiquer l'ouverture dans une nouvelle fenêtre
<a href="/doc.pdf" target="_blank" title="Télécharger le rapport (nouvelle fenêtre)">
  Rapport annuel (PDF, 2 Mo)
  <span className="sr-only"> - nouvelle fenêtre</span>
</a>
```

### 13.3–13.4 Documents bureautiques accessibles

Tout document en téléchargement (PDF, DOCX, ODS...) doit être accessible ou avoir une version alternative accessible (HTML ou autre format).

### 13.5–13.6 Contenus cryptiques avec alternative pertinente

Art ASCII, émoticônes, syntaxe cryptique : fournir une alternative via `title` ou contexte adjacent.

```tsx
<span title="Content">:-)</span>
// ou
<span role="img" aria-label="Content">:-)</span>
```

### 13.7 Pas de flash dangereux

Pas d'effet flash > 3 fois/seconde ou > 21824 pixels cumulés.

### 13.8 Contenus en mouvement contrôlables

Animation/clignotement automatique :
- Durée ≤ 5 secondes, ou
- Contrôle utilisateur (pause/stop)

```tsx
// Respecter prefers-reduced-motion
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}
```

### 13.9 Contenu consultable en portrait et paysage

Le contenu doit fonctionner dans les deux orientations (sauf nécessité essentielle : piano, chèque).

### 13.10 Gestes complexes doublés par gestes simples

Toute fonctionnalité via geste complexe (multipoint, trajectoire) doit être aussi disponible via geste simple (tap, clic).

### 13.11 Actions annulables

Actions via pointeur sur un point unique :
- Déclenchées au relâchement (mouseup/touchend), pas à la pression
- Ou annulables après déclenchement
- Ou mécanisme d'abandon disponible

### 13.12 Fonctionnalités basées sur le mouvement de l'appareil

Si une fonctionnalité utilise le mouvement (secouer, incliner) :
- Une alternative via composant d'interface doit exister
- L'utilisateur doit pouvoir désactiver la détection de mouvement
