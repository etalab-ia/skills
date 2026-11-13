# Ajout de fichier : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Bouton upload 1 seul fichier

```html
<div class="fr-upload-group">
    <label class="fr-label" for="file-upload">
        Ajouter un fichier
        <span class="fr-hint-text">Indication : taille maximale : 500 Mo. Formats supportés : jpg, png, pdf. Plusieurs fichiers possibles. Lorem ipsum dolor sit amet, consectetur adipiscing.</span>
    </label>
    <input class="fr-upload" aria-describedby="file-upload-messages" type="file" id="file-upload" name="file-upload">
    <div class="fr-messages-group" id="file-upload-messages" aria-live="polite">
    </div>
</div>
```

### Bouton upload avec erreur

```html
<div class="fr-upload-group fr-upload-group--error">
    <label class="fr-label" for="file-upload-with-error">
        Ajouter un fichier
        <span class="fr-hint-text">Indication : taille maximale : 500 Mo. Formats supportés : jpg, png, pdf. Plusieurs fichiers possibles. Lorem ipsum dolor sit amet, consectetur adipiscing.</span>
    </label>
    <input class="fr-upload" aria-describedby="file-upload-with-error-messages" type="file" id="file-upload-with-error" name="file-upload-with-error">
    <div class="fr-messages-group" id="file-upload-with-error-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="file-upload-with-error-message-error">Format de fichier non supporté</p>
    </div>
</div>
```

### Bouton upload fichiers multiples

```html
<div class="fr-upload-group">
    <label class="fr-label" for="file-upload-multiple">
        Ajouter des fichiers
        <span class="fr-hint-text">Indication : taille maximale : 500 Mo. Formats supportés : jpg, png, pdf. Plusieurs fichiers possibles. Lorem ipsum dolor sit amet, consectetur adipiscing.</span>
    </label>
    <input class="fr-upload" aria-describedby="file-upload-multiple-messages" multiple type="file" id="file-upload-multiple" name="file-upload-multiple">
    <div class="fr-messages-group" id="file-upload-multiple-messages" aria-live="polite">
    </div>
</div>
```

### Bouton upload désactivé

```html
<div class="fr-upload-group fr-upload-group--disabled">
    <label class="fr-label" for="file-upload-disabled">
        Ajouter un fichier
        <span class="fr-hint-text">Indication : taille maximale : 500 Mo. Formats supportés : jpg, png, pdf. Plusieurs fichiers possibles. Lorem ipsum dolor sit amet, consectetur adipiscing.</span>
    </label>
    <input class="fr-upload" disabled aria-describedby="file-upload-disabled-messages" type="file" id="file-upload-disabled" name="file-upload-disabled">
    <div class="fr-messages-group" id="file-upload-disabled-messages" aria-live="polite">
    </div>
</div>
```
