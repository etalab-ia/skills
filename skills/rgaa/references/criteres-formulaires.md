# RGAA — Thème 11 : Formulaires (13 critères)

## 11.1 Chaque champ a une étiquette

Chaque champ de formulaire doit avoir une étiquette associée via (ordre de priorité) :
1. `aria-labelledby` référençant un passage de texte
2. `aria-label`
3. `<label for="id">` associé au champ
4. `title`

**Test :** Vérifier que chaque `<input>`, `<select>`, `<textarea>` a un `<label for>` associé, un `aria-label` ou un `aria-labelledby`. Les placeholders seuls ne constituent pas une étiquette valide.
**Non-conformité type :** `<input type="text" placeholder="Votre nom">` sans `<label>`, ni `aria-label`.
**Impact :** sans étiquette programmatique, le lecteur d'écran annonce une zone de saisie sans intitulé : la personne qui l'utilise ne sait pas quelle donnée renseigner. Saisie bloquée.
**Priorité :** 🔴 Bloquant

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
<label class="fr-label" for="user_email">Adresse e-mail</label>
<input class="fr-input" type="email" id="user_email" name="user[email]">

<%# aria-label si pas de label visible %>
<input class="fr-input" type="search" aria-label="Rechercher sur le site">
```

---

## 11.2 Étiquette pertinente

L'étiquette doit permettre de comprendre la fonction exacte du champ. Si un intitulé visible existe, le nom accessible doit le contenir.

**Test :** Lire les labels et vérifier qu'ils décrivent précisément le champ (pas "Saisir", "Champ 1"). Si un `aria-label` est présent, vérifier qu'il contient le texte visible du label.
**Non-conformité type :** `<label>Saisir :</label>` ; `aria-label="field1"` alors que le label visible dit "Adresse email".
**Impact :** un intitulé vague, restitué hors contexte dans la liste des champs du lecteur d'écran, ne permet pas de savoir quelle donnée renseigner.
**Priorité :** 🟠 Majeur

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
<label class="fr-label" for="email">Adresse e-mail professionnelle</label>
<input class="fr-input" type="email" id="email" name="email">
```

---

## 11.3 Étiquettes cohérentes

Les champs de même fonction (ex: "Email" dans formulaire de contact et d'inscription) doivent avoir des étiquettes formulées de manière cohérente.

**Test :** Comparer les étiquettes de champs de même type sur différentes pages ou formulaires du site.
**Non-conformité type :** "Adresse email" sur une page, "Courriel" sur une autre pour le même type de champ.
**Impact :** des intitulés divergents pour une même donnée d'un formulaire à l'autre désorientent, en particulier en cas de troubles cognitifs.
**Priorité :** 🟡 Mineur

> Pas de correction locale : critère trans-pages. Harmoniser les libellés à l'échelle du site (centraliser dans les locales i18n côté Rails, dans un dictionnaire de libellés côté React).

---

## 11.4 Étiquette et champ accolés

- Champs texte/select : étiquette au-dessus ou à gauche
- Checkbox/radio : étiquette en-dessous ou à droite

**Test :** Vérifier visuellement et dans le code la proximité entre chaque label et son champ. Le label et le champ doivent être contigus dans le DOM.
**Non-conformité type :** Label en haut de page référençant un champ en bas de page ; label séparé du champ par un autre élément.
**Impact :** un label éloigné de son champ rompt l'association, notamment en agrandissement (zoom 200 %, loupe) où l'on perd le lien visuel entre les deux.
**Priorité :** 🟠 Majeur

### Correction — React / JSX

```tsx
// ✅ label contigu au champ dans le DOM
<label htmlFor="ville">Ville</label>
<input id="ville" type="text" />
```

### Correction — Rails / ERB

```erb
<%# Label contigu au champ dans le DOM %>
<label class="fr-label" for="ville">Ville</label>
<input class="fr-input" id="ville" name="ville" type="text">
```

---

## 11.5–11.7 Regroupement de champs

Regrouper les champs de même nature avec `<fieldset>` + `<legend>`.

**Test :** Identifier les groupes logiques de champs (cases à cocher, boutons radio, adresse en plusieurs champs). Vérifier qu'ils sont enveloppés dans un `<fieldset>` avec une `<legend>` pertinente, ou un `role="group"` + `aria-label`.
**Non-conformité type :** Groupe de boutons radio sans `<fieldset>` ; groupe de champs d'adresse sans légende de groupe.
**Impact :** sans `fieldset`/`legend`, le groupe est restitué champ par champ sans son intitulé commun : on ne sait pas à quelle question le choix se rapporte.
**Priorité :** 🟠 Majeur

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
      <input class="fr-radio" type="radio" id="civilite_mme" name="civilite" value="mme">
      <label class="fr-label" for="civilite_mme">Madame</label>
    </div>
  </div>
  <div class="fr-fieldset__element">
    <div class="fr-radio-group">
      <input class="fr-radio" type="radio" id="civilite_m" name="civilite" value="m">
      <label class="fr-label" for="civilite_m">Monsieur</label>
    </div>
  </div>
</fieldset>
```

Alternative ARIA : `role="group"` + `aria-label` ou `role="radiogroup"`.

---

## 11.8 Items de liste de choix regroupés

**Test :** Vérifier que les `<select>` avec de nombreuses options utilisent `<optgroup>` pour les regrouper par catégorie logique si nécessaire.
**Non-conformité type :** `<select>` avec 20+ options sans aucun `<optgroup>` alors que les options relèvent de catégories distinctes.
**Impact :** une longue liste sans regroupement allonge la navigation et alourdit la charge cognitive, surtout au clavier ou au lecteur d'écran.
**Priorité :** 🟡 Mineur

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
<select class="fr-select" id="departement" name="departement">
  <optgroup label="Île-de-France">
    <option value="75">Paris</option>
    <option value="92">Hauts-de-Seine</option>
  </optgroup>
  <optgroup label="Auvergne-Rhône-Alpes">
    <option value="69">Rhône</option>
  </optgroup>
</select>
```

---

## 11.9 Intitulé de bouton pertinent

Chaque bouton doit avoir un intitulé décrivant son action.

**Test :** Vérifier que chaque `<button>` et `<input type="submit/reset/button">` a un texte ou `aria-label` décrivant précisément son action dans le contexte du formulaire.
**Non-conformité type :** `<button>OK</button>` ; `<button>Envoyer</button>` quand plusieurs formulaires sont présents sur la page.
**Impact :** un intitulé vague restitué hors contexte (« OK », « Envoyer ») ne dit pas quelle action sera déclenchée.
**Priorité :** 🟠 Majeur

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

---

## 11.10 Contrôle de saisie

### Champs obligatoires

**Test :** Vérifier que les champs obligatoires ont une indication visible (astérisque ou texte) ET `required` ou `aria-required="true"`.
**Non-conformité type :** Champ obligatoire sans `required` ; obligation signalée visuellement (couleur seule) sans attribut ARIA.
**Impact :** une obligation signalée par la seule couleur n'est ni restituée par le lecteur d'écran, ni perçue par une personne ayant un trouble de la vision des couleurs ; l'envoi échoue sans qu'on sache quel champ compléter.
**Priorité :** 🔴 Bloquant

#### Correction — React / JSX

```tsx
<label htmlFor="nom">
  Nom <span aria-hidden="true">*</span>
</label>
<input id="nom" required aria-required="true" />
<p className="sr-only">Les champs marqués d'un * sont obligatoires</p>
```

#### Correction — Rails / ERB

```erb
<%# Mention unique, en tête de formulaire, plutôt que répétée sous chaque champ %>
<p class="fr-hint-text">Les champs marqués d'un * sont obligatoires.</p>

<label class="fr-label" for="nom">Nom <span aria-hidden="true">*</span></label>
<input class="fr-input" id="nom" name="nom" required aria-required="true">
```

### Messages d'erreur

**Test :** Vérifier que les erreurs de validation sont associées au champ via `aria-describedby`, que le champ a `aria-invalid="true"`, et que le message d'erreur est visible et descriptif.
**Non-conformité type :** Message d'erreur visible mais pas lié au champ via `aria-describedby` ; `aria-invalid` absent.
**Impact :** un message d'erreur non rattaché au champ n'est pas restitué au bon endroit par le lecteur d'écran : la personne qui l'utilise ne sait pas quel champ corriger ni pourquoi.
**Priorité :** 🔴 Bloquant

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
  Erreur : veuillez saisir une adresse email valide (ex : jeanne.martin@example.fr)
</p>
```

#### Correction — Rails / ERB

```erb
<label class="fr-label" for="email">Adresse e-mail</label>
<input class="fr-input" type="email" id="email" aria-invalid="true" aria-describedby="error-email">
<p id="error-email" class="fr-error-text" role="alert">
  Erreur : veuillez saisir une adresse e-mail valide (ex : jeanne.martin@example.fr)
</p>
```

```javascript
// Focus sur le premier champ en erreur après soumission
document.querySelector('[aria-invalid="true"]')?.focus()
```

### Indications de format

**Test :** Vérifier que le format attendu est indiqué avant ou au moment de la saisie (pas seulement après erreur), et lié au champ via `aria-describedby`.
**Non-conformité type :** Champ de date sans indication du format attendu (JJ/MM/AAAA).
**Impact :** sans indication de format en amont, la contrainte n'est découverte qu'après l'erreur, ce qui multiplie les tentatives (impact fort en saisie vocale et en cas de troubles cognitifs).
**Priorité :** 🟠 Majeur

#### Correction — React / JSX

```tsx
<label htmlFor="tel">Téléphone</label>
<p id="hint-tel">Format attendu : 01 99 00 12 34</p>
<input id="tel" type="tel" aria-describedby="hint-tel" />
```

#### Correction — Rails / ERB

```erb
<label class="fr-label" for="tel">Téléphone</label>
<span class="fr-hint-text" id="hint-tel">Format attendu : 01 99 00 12 34</span>
<input class="fr-input" id="tel" type="tel" aria-describedby="hint-tel">
```

> **Astuce — numéros de téléphone d'exemple.** Pour illustrer un champ téléphone, utiliser une plage **réservée à la fiction par l'ARCEP** plutôt qu'un numéro inventé : ces numéros ne sont pas attribuables et ne peuvent ni appeler ni être appelés, donc aucun risque de tomber sur un vrai abonné. Fixe : `01 99 00 XX XX`, `02 61 91 XX XX`, `03 53 01 XX XX`, `04 65 71 XX XX`, `05 36 49 XX XX` ; mobile : `06 39 98 XX XX`. Voir le [plan de numérotation en France](https://fr.wikipedia.org/wiki/Plan_de_num%C3%A9rotation_en_France) (numéros réservés aux œuvres audiovisuelles, décision ARCEP n° 2018-0881).

---

## 11.11 Suggestions de correction

En cas d'erreur, suggérer le type de données attendu et donner un exemple.

**Test :** Vérifier que les messages d'erreur contiennent une suggestion de correction concrète (exemple de valeur valide, format attendu).
**Non-conformité type :** Message "Format invalide" sans préciser le format attendu.
**Impact :** une erreur sans piste de correction (« Format invalide ») laisse la personne sans moyen de savoir comment corriger.
**Priorité :** 🟠 Majeur

### Correction — React / JSX

```tsx
<p id="error-date" role="alert">
  Erreur : format de date invalide. Saisissez une date au format JJ/MM/AAAA (ex: 15/03/2024).
</p>
```

### Correction — Rails / ERB

```erb
<p id="error-date" class="fr-error-text" role="alert">
  Format de date invalide. Saisissez une date au format JJ/MM/AAAA (ex : 15/03/2024).
</p>
```

> **Astuce — exemples de valeurs.** Quand un champ porte déjà un exemple dans son indication de format (`hint`), donner dans le message d'erreur une valeur **différente** : deux valeurs distinctes montrent clairement qu'il s'agit d'illustrations et non d'une saisie attendue. Ex. hint `email@example.fr`, message d'erreur `jeanne.martin@example.fr`. Pour les e-mails, utiliser un **domaine réservé à la documentation** (`example.fr`, `example.com`) plutôt qu'un domaine réel — l'équivalent des numéros de téléphone de fiction (cf. critère 11.10).

---

## 11.12 Données modifiables/récupérables (conséquences financières/juridiques)

Pour les formulaires avec conséquences financières, juridiques ou de suppression :
- Permettre de modifier/annuler après validation
- OU étape de vérification/confirmation avant envoi
- OU case à cocher de confirmation explicite

**Test :** Identifier les formulaires à conséquences irréversibles (paiement, suppression de compte, soumission juridique). Vérifier qu'un mécanisme de vérification ou d'annulation est proposé.
**Non-conformité type :** Formulaire de paiement sans étape de confirmation ni possibilité d'annulation.
**Impact :** une action irréversible sans étape de vérification expose à des conséquences lourdes (paiement, suppression) en cas d'erreur de manipulation — tremblements, fatigue, restitution partielle.
**Priorité :** 🔴 Bloquant

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

---

## 11.13 Autocomplete pour les champs utilisateur

Champs concernant l'utilisateur : attribut `autocomplete` avec la bonne valeur.

**Test :** Vérifier que les champs demandant des données personnelles (nom, prénom, email, téléphone, adresse...) ont l'attribut `autocomplete` avec la valeur normalisée correspondante.
**Non-conformité type :** `<input type="email" name="email">` sans `autocomplete="email"`.
**Impact :** sans `autocomplete`, le remplissage automatique ne fonctionne pas — surcoût de saisie pour les personnes à mobilité réduite, en saisie vocale ou en cas de troubles cognitifs.
**Priorité :** 🟡 Mineur

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
