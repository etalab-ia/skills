# Corrections RGAA — Thème 11 : Formulaires (13 critères)

Blocs de correction par stack, à lire seulement pour rédiger la correction d’une NC. Le texte officiel et le reste de chaque critère sont dans `../criteres-formulaires.md`.

## 11.1 Chaque champ a une étiquette

### Correction — React / JSX

```tsx
// ✅ Label explicite avec for/id
<label htmlFor="email">Email</label>
<input id="email" type="email" />

// ✅ aria-label (si pas de label visible)
<input type="search" aria-label="Rechercher sur le site" />

// ✅ aria-labelledby
<span id="label-tel">Téléphone</span>
<span id="hint-tel">Format : 01 99 00 12 34</span>
<input aria-labelledby="label-tel hint-tel" type="tel" />
```

### Correction — Rails / ERB

```erb
<%# Label explicite for/id — classes fr-* du DSFR %>
<div class="fr-input-group">
  <label class="fr-label" for="user_email">Adresse e-mail</label>
  <input class="fr-input" type="email" id="user_email" name="user[email]">
</div>

<%# aria-label si pas de label visible %>
<input class="fr-input" type="search" name="q" aria-label="Rechercher sur le site">
```

## 11.2 Étiquette pertinente

### Correction — React / JSX

```tsx
// ❌ <label>Saisir :</label>
// ✅ intitulé explicite ; si aria-label, il contient le texte visible
<label htmlFor="email">Adresse e-mail professionnelle</label>
<input id="email" type="email" />
```

### Correction — Rails / ERB

```erb
<%# ❌ <label class="fr-label" for="email">Saisir :</label> %>
<%# ✅ intitulé explicite %>
<div class="fr-input-group">
  <label class="fr-label" for="email">Adresse e-mail professionnelle</label>
  <input class="fr-input" type="email" id="email" name="email">
</div>
```

## 11.4 Étiquette et champ accolés

### Correction — React / JSX

```tsx
// ✅ label contigu au champ dans le DOM
<label htmlFor="ville">Ville</label>
<input id="ville" type="text" />
```

### Correction — Rails / ERB

```erb
<%# Label contigu au champ dans le DOM %>
<div class="fr-input-group">
  <label class="fr-label" for="ville">Ville</label>
  <input class="fr-input" id="ville" name="ville" type="text">
</div>
```

## 11.5–11.7 Regroupement de champs

### Correction — React / JSX

```tsx
<fieldset>
  <legend>Adresse de livraison</legend>
  <label htmlFor="rue">Rue</label>
  <input id="rue" type="text" />
  <label htmlFor="ville">Ville</label>
  <input id="ville" type="text" />
</fieldset>

// Radio buttons obligatoirement groupés
<fieldset>
  <legend>Civilité</legend>
  <input type="radio" id="mme" name="civilite" value="mme" />
  <label htmlFor="mme">Madame</label>
  <input type="radio" id="m" name="civilite" value="m" />
  <label htmlFor="m">Monsieur</label>
</fieldset>
```

Alternative ARIA : `role="group"` + `aria-label` ou `role="radiogroup"`.

### Correction — Rails / ERB

```erb
<%# Groupe radio — fieldset DSFR %>
<fieldset class="fr-fieldset">
  <legend class="fr-fieldset__legend">Civilité</legend>
  <div class="fr-fieldset__element">
    <div class="fr-radio-group">
      <input type="radio" id="civilite_mme" name="civilite" value="mme">
      <label class="fr-label" for="civilite_mme">Madame</label>
    </div>
  </div>
  <div class="fr-fieldset__element">
    <div class="fr-radio-group">
      <input type="radio" id="civilite_m" name="civilite" value="m">
      <label class="fr-label" for="civilite_m">Monsieur</label>
    </div>
  </div>
</fieldset>
```

Alternative ARIA : `role="group"` + `aria-label` ou `role="radiogroup"`.

## 11.8 Items de liste de choix regroupés

### Correction — React / JSX

```tsx
<select>
  <optgroup label="Île-de-France">
    <option value="75">Paris</option>
    <option value="92">Hauts-de-Seine</option>
  </optgroup>
  <optgroup label="Auvergne-Rhône-Alpes">
    <option value="69">Rhône</option>
  </optgroup>
</select>
```

### Correction — Rails / ERB

```erb
<div class="fr-select-group">
  <label class="fr-label" for="departement">Département</label>
  <select class="fr-select" id="departement" name="departement">
    <optgroup label="Île-de-France">
      <option value="75">Paris</option>
      <option value="92">Hauts-de-Seine</option>
    </optgroup>
    <optgroup label="Auvergne-Rhône-Alpes">
      <option value="69">Rhône</option>
    </optgroup>
  </select>
</div>
```

## 11.9 Intitulé de bouton pertinent

### Correction — React / JSX

```tsx
// ❌ Mauvais
<button>OK</button>

// ✅ Bon
<button type="submit">Envoyer ma demande de contact</button>
<button type="reset">Réinitialiser le formulaire</button>
```

### Correction — Rails / ERB

```erb
<%# Intitulé d'action explicite %>
<button type="submit" class="fr-btn">Envoyer ma demande de contact</button>
<button type="reset" class="fr-btn fr-btn--secondary">Réinitialiser le formulaire</button>
```

## 11.10 Contrôle de saisie

### Champs obligatoires

#### Correction — React / JSX

```tsx
{/* Mention unique, visible et en tête de formulaire, avant le premier astérisque */}
<p className="fr-hint-text">Les champs marqués d'un * sont obligatoires.</p>

<div className="fr-input-group">
  <label className="fr-label" htmlFor="nom">
    Nom <span aria-hidden="true">*</span>
  </label>
  <input className="fr-input" id="nom" name="nom" required aria-required="true" />
</div>
```

#### Correction — Rails / ERB

```erb
<%# Mention unique, en tête de formulaire, plutôt que répétée sous chaque champ %>
<p class="fr-hint-text">Les champs marqués d'un * sont obligatoires.</p>

<div class="fr-input-group">
  <label class="fr-label" for="nom">Nom <span aria-hidden="true">*</span></label>
  <input class="fr-input" id="nom" name="nom" required aria-required="true">
</div>
```

### Messages d'erreur

#### Correction — React / JSX

```tsx
<label htmlFor="email">Email</label>
<input
  id="email"
  type="email"
  aria-invalid="true"
  aria-describedby="error-email"
/>
<p id="error-email" role="alert">
  Erreur : veuillez saisir une adresse email valide (ex : jeanne.martin@example.com)
</p>
```

#### Correction — Rails / ERB

```erb
<div class="fr-input-group fr-input-group--error">
  <label class="fr-label" for="email">Adresse e-mail</label>
  <input class="fr-input" type="email" id="email" name="email" aria-invalid="true" aria-describedby="email-messages">
  <div class="fr-messages-group" id="email-messages" aria-live="polite">
    <p class="fr-message fr-message--error" id="error-email">
      Erreur : veuillez saisir une adresse e-mail valide (ex : jeanne.martin@example.com)
    </p>
  </div>
</div>
```

```javascript
// Focus sur le premier champ en erreur après soumission
document.querySelector('[aria-invalid="true"]')?.focus()
```

### Indications de format

#### Correction — React / JSX

```tsx
<label htmlFor="tel">Téléphone</label>
<p id="hint-tel">Format attendu : 01 99 00 12 34</p>
<input id="tel" type="tel" aria-describedby="hint-tel" />
```

#### Correction — Rails / ERB

```erb
<div class="fr-input-group">
  <label class="fr-label" for="tel">Téléphone</label>
  <span class="fr-hint-text" id="hint-tel">Format attendu : 01 99 00 12 34</span>
  <input class="fr-input" id="tel" name="telephone" type="tel" aria-describedby="hint-tel">
</div>
```

> **Astuce — numéros de téléphone d'exemple.** Pour illustrer un champ téléphone, utiliser une plage **réservée à la fiction par l'ARCEP** plutôt qu'un numéro inventé : ces numéros ne sont pas attribuables et ne peuvent ni appeler ni être appelés, donc aucun risque de tomber sur un vrai abonné. Fixe : `01 99 00 XX XX`, `02 61 91 XX XX`, `03 53 01 XX XX`, `04 65 71 XX XX`, `05 36 49 XX XX` ; mobile : `06 39 98 XX XX`. Voir le [plan de numérotation en France](https://fr.wikipedia.org/wiki/Plan_de_num%C3%A9rotation_en_France) (numéros réservés aux œuvres audiovisuelles, décision ARCEP n° 2018-0881).

## 11.11 Suggestions de correction

### Correction — React / JSX

```tsx
<p id="error-date" role="alert">
  Erreur : format de date invalide. Saisissez une date au format JJ/MM/AAAA (ex: 15/03/2024).
</p>
```

### Correction — Rails / ERB

```erb
<div class="fr-messages-group" id="date-messages" aria-live="polite">
  <p class="fr-message fr-message--error" id="error-date">
    Format de date invalide. Saisissez une date au format JJ/MM/AAAA (ex : 15/03/2024).
  </p>
</div>
```

> **Astuce — exemples de valeurs.** Quand un champ porte déjà un exemple dans son indication de format (`hint`), donner dans le message d'erreur une valeur **différente** : deux valeurs distinctes montrent clairement qu'il s'agit d'illustrations et non d'une saisie attendue. Ex. hint `email@example.com`, message d'erreur `jeanne.martin@example.com`. Pour les e-mails, utiliser un **domaine réservé à la documentation** (RFC 2606 : `example.com`, `example.net`, `example.org`, TLD `.example`) plutôt qu'un domaine réel — `example.fr` n'est pas réservé. C'est l'équivalent des numéros de téléphone de fiction (cf. critère 11.10).

## 11.12 Données modifiables/récupérables (conséquences financières/juridiques)

### Correction — React / JSX

```tsx
<h2>Vérifiez vos informations avant envoi</h2>
<dl>
  <dt>Nom</dt><dd>{nom}</dd>
  <dt>Email</dt><dd>{email}</dd>
</dl>
<button onClick={goBack}>Modifier</button>
<button onClick={submit}>Confirmer et envoyer</button>
```

### Correction — Rails / ERB

```erb
<h2>Vérifiez vos informations avant envoi</h2>
<dl>
  <dt>Nom</dt><dd><%= @demande.nom %></dd>
  <dt>E-mail</dt><dd><%= @demande.email %></dd>
</dl>
<a class="fr-btn fr-btn--secondary" href="<%= edit_demande_path(@demande) %>">Modifier</a>
<button type="submit" class="fr-btn">Confirmer et envoyer</button>
```

## 11.13 Autocomplete pour les champs utilisateur

### Correction — React / JSX

```tsx
<input type="text" autoComplete="given-name" name="prenom" />
<input type="text" autoComplete="family-name" name="nom" />
<input type="email" autoComplete="email" name="email" />
<input type="tel" autoComplete="tel" name="telephone" />
<input type="text" autoComplete="street-address" name="adresse" />
<input type="text" autoComplete="postal-code" name="cp" />
<input type="text" autoComplete="address-level2" name="ville" />
```

### Correction — Rails / ERB

```erb
<input class="fr-input" type="text" autocomplete="given-name" name="prenom">
<input class="fr-input" type="text" autocomplete="family-name" name="nom">
<input class="fr-input" type="email" autocomplete="email" name="email">
<input class="fr-input" type="tel" autocomplete="tel" name="telephone">
<input class="fr-input" type="text" autocomplete="street-address" name="adresse">
<input class="fr-input" type="text" autocomplete="postal-code" name="cp">
<input class="fr-input" type="text" autocomplete="address-level2" name="ville">
```

**Valeurs courantes :** `name`, `given-name`, `family-name`, `email`, `tel`, `street-address`, `postal-code`, `address-level2` (ville), `country-name`, `organization`, `username`, `new-password`, `current-password`, `bday`, `cc-number`, `cc-exp`, `cc-name`.

**Liste complète des valeurs :** voir la spécification HTML de l'attribut `autocomplete` — https://developer.mozilla.org/fr/docs/Web/HTML/Reference/Attributes/autocomplete

