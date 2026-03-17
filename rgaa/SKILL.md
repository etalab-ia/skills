---
name: rgaa
description: Référentiel Général d'Amélioration de l'Accessibilité (RGAA 4.1.2) — les 106 critères d'accessibilité numérique français avec patterns React/HTML. Utiliser cette skill quand l'utilisateur demande de vérifier l'accessibilité, de rendre du code accessible, de respecter le RGAA, quand il mentionne l'accessibilité web, les critères RGAA, la conformité RGAA, le WCAG dans un contexte français, ou quand on crée/modifie des composants HTML/React qui doivent être accessibles. Couvre images, couleurs, formulaires, navigation, structure, liens, scripts, multimédia, tableaux et consultation.
---

# RGAA 4.1.2

Référentiel d'accessibilité numérique français. 106 critères répartis en 13 thématiques. Basé sur WCAG 2.1 niveau AA.

Source : https://accessibilite.numerique.gouv.fr/

## Checklist rapide par type de composant

### Page HTML
- [ ] `<!DOCTYPE html>` présent (8.1)
- [ ] `<html lang="fr">` (8.3)
- [ ] `<title>` pertinent et unique (8.5–8.6)
- [ ] Structure : `<header>`, `<nav>`, `<main>` (unique), `<footer>` (9.2)
- [ ] Hiérarchie des titres h1→h6 sans saut (9.1)
- [ ] Lien d'évitement "Aller au contenu" (12.7)
- [ ] 2 systèmes de navigation minimum (12.1)
- [ ] Focus visible sur tout élément interactif (10.7)
- [ ] Pas de scroll horizontal à 320px de large (10.11)

### Images
- [ ] Image informative : `alt` pertinent et concis ≤80 car (1.1, 1.3)
- [ ] Image décorative : `alt=""` (1.2)
- [ ] SVG informative : `role="img"` + `aria-label` (1.1)
- [ ] SVG décorative : `aria-hidden="true"` (1.2)
- [ ] Image complexe : description détaillée (1.6)
- [ ] Image avec légende : `<figure>` + `<figcaption>` (1.9)

### Liens
- [ ] Intitulé explicite (pas de "cliquez ici") (6.1)
- [ ] Tout lien a un intitulé accessible (6.2)
- [ ] Liens distinguables du texte autrement que par la couleur (10.6)
- [ ] Nouvelle fenêtre signalée (13.2)

### Formulaires
- [ ] Chaque champ a un `<label>` associé (11.1)
- [ ] Champs obligatoires : `required` + indication visible (11.10)
- [ ] Erreurs : `aria-invalid="true"` + message visible avec `aria-describedby` (11.10)
- [ ] Format attendu indiqué avant saisie (11.10)
- [ ] Suggestions de correction (11.11)
- [ ] Champs groupés : `<fieldset>` + `<legend>` (11.5)
- [ ] Boutons avec intitulé pertinent (11.9)
- [ ] `autocomplete` sur les champs utilisateur (11.13)

### Tableaux
- [ ] `<caption>` pour le titre (5.4)
- [ ] `<th scope="col/row">` pour les en-têtes (5.6)
- [ ] Tableau de mise en forme : `role="presentation"` (5.3)

### Couleurs et contraste
- [ ] Texte normal : contraste ≥ 4.5:1 (3.2)
- [ ] Grand texte (≥24px ou ≥18.5px gras) : contraste ≥ 3:1 (3.2)
- [ ] Composants d'interface : contraste ≥ 3:1 (3.3)
- [ ] Information pas uniquement par la couleur (3.1)

### Scripts et composants interactifs
- [ ] Composants accessibles au clavier (7.3)
- [ ] Rôles ARIA corrects (7.1)
- [ ] Messages de statut : `role="status"` ou `role="alert"` (7.5)
- [ ] Pas de piège au clavier (12.9)
- [ ] Ordre de tabulation logique (12.8)

### Multimédia
- [ ] Vidéo : sous-titres `<track kind="captions">` (4.3)
- [ ] Transcription textuelle disponible (4.1)
- [ ] Contrôles accessibles au clavier (4.11)
- [ ] Pas de son automatique (4.10)

## Patterns React essentiels

### Classe sr-only (contenu visible uniquement par les AT)
```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

### Bouton interactif (pas de div cliquable)
```tsx
// ❌ <div onClick={fn}>Action</div>
// ✅
<button onClick={fn}>Action</button>
```

### Message de statut dynamique
```tsx
<div role="status" aria-live="polite">
  {message && <p>{message}</p>}
</div>
```

### Modale accessible
```tsx
<dialog open={isOpen} aria-labelledby="modal-title" aria-modal="true">
  <h2 id="modal-title">Titre</h2>
  <p>Contenu</p>
  <button onClick={close}>Fermer</button>
</dialog>
```

### Navigation avec landmarks
```tsx
<a href="#main-content" className="sr-only focus:not-sr-only">
  Aller au contenu principal
</a>
<header>...</header>
<nav aria-label="Menu principal">...</nav>
<main id="main-content" tabIndex={-1}>...</main>
<footer>...</footer>
```

## Référence détaillée des critères

Consulter les fichiers de référence par thématique :

- **Images, Cadres, Couleurs** (thèmes 1–3, 14 critères) : [references/criteres-images-cadres-couleurs.md](references/criteres-images-cadres-couleurs.md)
- **Multimédia, Tableaux, Liens, Scripts** (thèmes 4–7, 28 critères) : [references/criteres-multimedia-tableaux-liens-scripts.md](references/criteres-multimedia-tableaux-liens-scripts.md)
- **Éléments obligatoires, Structure, Présentation** (thèmes 8–10, 28 critères) : [references/criteres-structure-presentation.md](references/criteres-structure-presentation.md)
- **Formulaires** (thème 11, 13 critères) : [references/criteres-formulaires.md](references/criteres-formulaires.md)
- **Navigation, Consultation** (thèmes 12–13, 23 critères) : [references/criteres-navigation-consultation.md](references/criteres-navigation-consultation.md)

Chaque fichier contient les critères détaillés, les tests associés et des exemples de code React/HTML conformes.
