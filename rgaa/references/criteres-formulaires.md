# RGAA — Thème 11 : Formulaires (13 critères)

## 11.1 Chaque champ a une étiquette

Chaque champ de formulaire doit avoir une étiquette associée via (ordre de priorité) :
1. `aria-labelledby` référençant un passage de texte
2. `aria-label`
3. `<label for="id">` associé au champ
4. `title`

```tsx
// ✅ Label explicite avec for/id
<label htmlFor="email">Email</label>
<input id="email" type="email" />

// ✅ aria-label (si pas de label visible)
<input type="search" aria-label="Rechercher sur le site" />

// ✅ aria-labelledby
<span id="label-tel">Téléphone</span>
<span id="hint-tel">Format : 01 23 45 67 89</span>
<input aria-labelledby="label-tel hint-tel" type="tel" />
```

## 11.2 Étiquette pertinente

L'étiquette doit permettre de comprendre la fonction exacte du champ. Si un intitulé visible existe, le nom accessible doit le contenir.

## 11.3 Étiquettes cohérentes

Les champs de même fonction (ex: "Email" dans formulaire de contact et d'inscription) doivent avoir des étiquettes formulées de manière cohérente.

## 11.4 Étiquette et champ accolés

- Champs texte/select : étiquette au-dessus ou à gauche
- Checkbox/radio : étiquette en-dessous ou à droite

## 11.5–11.7 Regroupement de champs

Regrouper les champs de même nature avec `<fieldset>` + `<legend>` :

```tsx
<fieldset>
  <legend>Adresse de livraison</legend>
  <label htmlFor="rue">Rue</label>
  <input id="rue" type="text" />
  <label htmlFor="ville">Ville</label>
  <input id="ville" type="text" />
  <label htmlFor="cp">Code postal</label>
  <input id="cp" type="text" />
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

## 11.8 Items de liste de choix regroupés

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

## 11.9 Intitulé de bouton pertinent

Chaque bouton doit avoir un intitulé décrivant son action :
```tsx
// ❌ Mauvais
<button>OK</button>
<button>Envoyer</button> <!-- si plusieurs formulaires sur la page -->

// ✅ Bon
<button type="submit">Envoyer ma demande de contact</button>
<button type="reset">Réinitialiser le formulaire</button>
```

## 11.10 Contrôle de saisie

### Champs obligatoires
```tsx
// Indication visible + aria
<label htmlFor="nom">
  Nom <span aria-hidden="true">*</span>
</label>
<input id="nom" required aria-required="true" />
<p className="sr-only">Les champs marqués d'un * sont obligatoires</p>
```

### Messages d'erreur
```tsx
// Erreur visible + aria-invalid + aria-describedby
<label htmlFor="email">Email</label>
<input
  id="email"
  type="email"
  aria-invalid="true"
  aria-describedby="error-email"
/>
<p id="error-email" role="alert">
  Erreur : veuillez saisir une adresse email valide (ex: nom@domaine.fr)
</p>
```

### Indications de format
```tsx
<label htmlFor="tel">Téléphone</label>
<p id="hint-tel">Format attendu : 01 23 45 67 89</p>
<input id="tel" type="tel" aria-describedby="hint-tel" />
```

## 11.11 Suggestions de correction

En cas d'erreur, suggérer le type de données attendu et donner un exemple :
```tsx
<p id="error-date" role="alert">
  Erreur : format de date invalide. Saisissez une date au format JJ/MM/AAAA (ex: 15/03/2024).
</p>
```

## 11.12 Données modifiables/récupérables (conséquences financières/juridiques)

Pour les formulaires avec conséquences financières, juridiques ou de suppression :
- Permettre de modifier/annuler après validation
- OU étape de vérification/confirmation avant envoi
- OU case à cocher de confirmation explicite

```tsx
// Étape de confirmation
<h2>Vérifiez vos informations avant envoi</h2>
<dl>
  <dt>Nom</dt><dd>{nom}</dd>
  <dt>Email</dt><dd>{email}</dd>
</dl>
<button onClick={goBack}>Modifier</button>
<button onClick={submit}>Confirmer et envoyer</button>
```

## 11.13 Autocomplete pour les champs utilisateur

Champs concernant l'utilisateur : attribut `autocomplete` avec la bonne valeur.

```tsx
<input type="text" autocomplete="given-name" name="prenom" />
<input type="text" autocomplete="family-name" name="nom" />
<input type="email" autocomplete="email" name="email" />
<input type="tel" autocomplete="tel" name="telephone" />
<input type="text" autocomplete="street-address" name="adresse" />
<input type="text" autocomplete="postal-code" name="cp" />
<input type="text" autocomplete="address-level2" name="ville" />
```

**Valeurs courantes :** `name`, `given-name`, `family-name`, `email`, `tel`, `street-address`, `postal-code`, `address-level2` (ville), `country-name`, `organization`, `username`, `new-password`, `current-password`, `bday`, `cc-number`, `cc-exp`, `cc-name`.
