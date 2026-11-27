# Tag : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

## Tag non cliquable

### Tag non cliquable sans icône

```html
<p class="fr-tag">Libellé tag</p>
```

### Tag non cliquable icône à gauche

```html
<p class="fr-tag fr-icon-arrow-left-line fr-tag--icon-left">Libellé tag</p>
```

### Tag non cliquable taille SM

```html
<p class="fr-tag fr-tag--sm">Libellé tag</p>
```

## Tag cliquable

### Tag cliquable

La balise utilisée pour le tag cliquable est un "a" s'il s'agit d'un lien (href), si pas de href utiliser "button".

```html
<a class="fr-tag" href="#">Libellé tag</a>
```

### Tag cliquable avec icône

```html
<a class="fr-tag fr-icon-arrow-left-line fr-tag--icon-left" href="#">Libellé tag</a>
```

### Tag cliquable SM

```html
<a class="fr-tag fr-tag--sm" href="#">Libellé tag</a>
```

### Tag cliquable accentué

```html
<a class="fr-tag fr-tag--green-emeraude" href="#">Libellé tag</a>
```

### Tag cliquable désactivé

```html
<a class="fr-tag" aria-disabled="true" role="link">Libellé tag</a>
```

### Tag bouton cliquable désactivé

```html
<a class="fr-tag" aria-disabled="true" role="link">Libellé tag</a>
```

### Tag cliquable désactivé SM

```html
<a class="fr-tag fr-tag--sm" aria-disabled="true" role="link">Libellé tag</a>
```

## Tag sélectionnable

### Tag sélectionnable

Le tag sélectionnable n'autorise pas l'accentuation.

```html
<button class="fr-tag" aria-pressed="false" type="button">Libellé tag</button>
```

### Tag sélectionnable avec icone

```html
<button class="fr-tag fr-icon-information-line fr-tag--icon-left" aria-pressed="false" type="button">Libellé tag</button>
```

### Tag sélectionnable taille sm

```html
<button class="fr-tag fr-tag--sm" aria-pressed="false" type="button">Libellé tag</button>
```

### Tag sélectionnable désactivé

```html
<button class="fr-tag" aria-pressed="false" type="button" disabled>Libellé tag</button>
```

## Tag supprimable

### Tag supprimable

Le tag supprimable n'autorise ni accentuation ni icône personnalisée. Le javascript présent dans l’attribut onclick est donné à titre d’exemple, à vous de l’implémenter dans votre contexte technique.

```html
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag]">Libellé tag</button>
```

### Tag supprimable taille sm

```html
<button class="fr-tag fr-tag--sm fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag]">Libellé tag</button>
```

### Tag supprimable désactivé

```html
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag]" disabled>Libellé tag</button>
```

## Groupe de tags

### Groupe de tags non cliquables

Lorsque que l'on a plus d'un tag, il convient d'utiliser un groupe de tags. La taille de tous les tags peut être définie au niveau du groupe.

```html
<ul class="fr-tags-group">
    <li>
        <span class="fr-tag">Libellé tag 1</span>
    </li>
    <li>
        <span class="fr-tag">Libellé tag 2</span>
    </li>
    <li>
        <span class="fr-tag">Libellé tag 3</span>
    </li>
    <li>
        <span class="fr-tag">Libellé tag 4</span>
    </li>
    <li>
        <span class="fr-tag">Libellé tag 5</span>
    </li>
    <li>
        <span class="fr-tag">Libellé tag 6</span>
    </li>
    <li>
        <span class="fr-tag">Libellé tag 7</span>
    </li>
    <li>
        <span class="fr-tag">Libellé tag 8</span>
    </li>
    <li>
        <span class="fr-tag">Libellé tag 9</span>
    </li>
</ul>
```

### Groupe de tags non cliquables SM

```html
<ul class="fr-tags-group fr-tags-group--sm">
    <li>
        <span class="fr-tag">Libellé tag 1</span>
    </li>
    <li>
        <span class="fr-tag">Libellé tag 2</span>
    </li>
    <li>
        <span class="fr-tag">Libellé tag 3</span>
    </li>
    <li>
        <span class="fr-tag">Libellé tag 4</span>
    </li>
    <li>
        <span class="fr-tag">Libellé tag 5</span>
    </li>
    <li>
        <span class="fr-tag">Libellé tag 6</span>
    </li>
    <li>
        <span class="fr-tag">Libellé tag 7</span>
    </li>
    <li>
        <span class="fr-tag">Libellé tag 8</span>
    </li>
    <li>
        <span class="fr-tag">Libellé tag 9</span>
    </li>
</ul>
```

### Groupe de tags cliquables

```html
<ul class="fr-tags-group">
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 1</a>
    </li>
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 2</a>
    </li>
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 3</a>
    </li>
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 4</a>
    </li>
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 5</a>
    </li>
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 6</a>
    </li>
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 7</a>
    </li>
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 8</a>
    </li>
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 9</a>
    </li>
</ul>
```

### Groupe de tags cliquables SM

```html
<ul class="fr-tags-group fr-tags-group--sm">
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 1</a>
    </li>
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 2</a>
    </li>
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 3</a>
    </li>
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 4</a>
    </li>
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 5</a>
    </li>
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 6</a>
    </li>
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 7</a>
    </li>
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 8</a>
    </li>
    <li>
        <a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 9</a>
    </li>
</ul>
```

### Groupe de tags sélectionnables

```html
<ul class="fr-tags-group">
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 1</button>
    </li>
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 2</button>
    </li>
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 3</button>
    </li>
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 4</button>
    </li>
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 5</button>
    </li>
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 6</button>
    </li>
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 7</button>
    </li>
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 8</button>
    </li>
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 9</button>
    </li>
</ul>
```

### Groupe de tags sélectionnables SM

```html
<ul class="fr-tags-group fr-tags-group--sm">
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 1</button>
    </li>
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 2</button>
    </li>
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 3</button>
    </li>
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 4</button>
    </li>
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 5</button>
    </li>
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 6</button>
    </li>
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 7</button>
    </li>
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 8</button>
    </li>
    <li>
        <button class="fr-tag" type="button" aria-pressed="false">Libellé tag 9</button>
    </li>
</ul>
```

### Groupe de tags supprimables

```html
<ul class="fr-tags-group">
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 1]">Libellé tag 1</button>
    </li>
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 2]">Libellé tag 2</button>
    </li>
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 3]">Libellé tag 3</button>
    </li>
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 4]">Libellé tag 4</button>
    </li>
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 5]">Libellé tag 5</button>
    </li>
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 6]">Libellé tag 6</button>
    </li>
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 7]">Libellé tag 7</button>
    </li>
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 8]">Libellé tag 8</button>
    </li>
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 9]">Libellé tag 9</button>
    </li>
</ul>
```

### Groupe de tags supprimables SM

```html
<ul class="fr-tags-group fr-tags-group--sm">
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 1]">Libellé tag 1</button>
    </li>
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 2]">Libellé tag 2</button>
    </li>
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 3]">Libellé tag 3</button>
    </li>
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 4]">Libellé tag 4</button>
    </li>
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 5]">Libellé tag 5</button>
    </li>
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 6]">Libellé tag 6</button>
    </li>
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 7]">Libellé tag 7</button>
    </li>
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 8]">Libellé tag 8</button>
    </li>
    <li>
        <button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 9]">Libellé tag 9</button>
    </li>
</ul>
```
