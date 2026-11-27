# Bouton : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

## Bouton primaire

### Bouton simple

```html
<button type="button" class="fr-btn">Libellé bouton</button>
```

### Bouton simple SM

```html
<button type="button" class="fr-btn fr-btn--sm">Libellé bouton SM</button>
```

### Bouton simple LG

```html
<button type="button" class="fr-btn fr-btn--lg">Libellé bouton LG</button>
```

### Bouton désactivé

```html
<button type="button" disabled class="fr-btn">Libellé bouton</button>
```

### Bouton icon à gauche

```html
<button type="button" class="fr-btn fr-icon-checkbox-circle-line fr-btn--icon-left">Libellé bouton</button>
```

### Bouton icon à droite

```html
<button type="button" class="fr-btn fr-icon-checkbox-circle-line fr-btn--icon-right">Libellé bouton</button>
```

### Bouton icon seule

```html
<button title="[À MODIFIER - Libellé bouton]" type="button" class="fr-btn fr-icon-checkbox-circle-line">Libellé bouton</button>
```

### Bouton markup a href

L’exemple ci-dessous montre la possibilité d'appliquer le style du bouton secondaire sur un élément de type "lien" <a>. A n'appliquer qu'en cas exceptionnel d'impossibilité technique d'utiliser un <button>.

```html
<a href="[url - à modifier]" class="fr-btn">Libellé bouton</a>
```

### Bouton secondaire

```html
<button type="button" class="fr-btn fr-btn--secondary">Libellé bouton</button>
```

### Bouton secondaire désactivé

```html
<button type="button" disabled class="fr-btn fr-btn--secondary">Libellé bouton</button>
```

### Bouton secondaire icon à gauche

```html
<button type="button" class="fr-btn fr-icon-checkbox-circle-line fr-btn--icon-left fr-btn--secondary">Libellé bouton</button>
```

### Bouton secondaire icon à droite

```html
<button type="button" class="fr-btn fr-icon-checkbox-circle-line fr-btn--icon-right fr-btn--secondary">Libellé bouton</button>
```

### Bouton secondaire icon seule

```html
<button title="[À MODIFIER - Libellé bouton]" type="button" class="fr-btn fr-icon-checkbox-circle-line fr-btn--secondary">Libellé bouton</button>
```

### Bouton secondaire markup a href

L’exemple ci-dessous montre la possibilité d'appliquer le style du bouton secondaire sur un élément de type "lien" <a>. A n'appliquer qu'en cas exceptionnel d'impossibilité technique d'utiliser un <button>.

```html
<a href="[url - à modifier]" class="fr-btn fr-btn--secondary">Libellé bouton</a>
```

## Bouton tertiaire

### Bouton tertiaire

```html
<button type="button" class="fr-btn fr-btn--tertiary">Libellé bouton</button>
```

### Bouton tertiaire désactivé

```html
<button type="button" disabled class="fr-btn fr-btn--tertiary">Libellé bouton</button>
```

### Bouton tertiaire icon à gauche

```html
<button type="button" class="fr-btn fr-icon-checkbox-circle-line fr-btn--icon-left fr-btn--tertiary">Libellé bouton</button>
```

### Bouton tertiaire icon à droite

```html
<button type="button" class="fr-btn fr-icon-checkbox-circle-line fr-btn--icon-right fr-btn--tertiary">Libellé bouton</button>
```

### Bouton tertiaire icon seule

```html
<button title="[À MODIFIER - Libellé bouton]" type="button" class="fr-btn fr-icon-checkbox-circle-line fr-btn--tertiary">Libellé bouton</button>
```

### Bouton tertiaire markup a href

L’exemple ci-dessous montre la possibilité d'appliquer le style du bouton secondaire sur un élément de type "lien" <a>. A n'appliquer qu'en cas exceptionnel d'impossibilité technique d'utiliser un <button>.

```html
<a href="[url - à modifier]" class="fr-btn fr-btn--tertiary">Libellé bouton</a>
```

## Bouton tertiaire sans contour

### Bouton tertiaire sans contour

```html
<button type="button" class="fr-btn fr-btn--tertiary-no-outline">Libellé bouton</button>
```

### Bouton tertiaire sans contour désactivé

```html
<button type="button" disabled class="fr-btn fr-btn--tertiary-no-outline">Libellé bouton</button>
```

### Bouton tertiaire sans contour icon à gauche

```html
<button type="button" class="fr-btn fr-icon-checkbox-circle-line fr-btn--icon-left fr-btn--tertiary-no-outline">Libellé bouton</button>
```

### Bouton tertiaire sans contour icon à droite

```html
<button type="button" class="fr-btn fr-icon-checkbox-circle-line fr-btn--icon-right fr-btn--tertiary-no-outline">Libellé bouton</button>
```

### Bouton tertiaire sans contour icon seule

```html
<button title="[À MODIFIER - Libellé bouton]" type="button" class="fr-btn fr-icon-checkbox-circle-line fr-btn--tertiary-no-outline">Libellé bouton</button>
```

### Bouton tertiaire sans contour markup a href

L’exemple ci-dessous montre la possibilité d'appliquer le style du bouton secondaire sur un élément de type "lien" <a>. A n'appliquer qu'en cas exceptionnel d'impossibilité technique d'utiliser un <button>.

```html
<a href="[url - à modifier]" class="fr-btn fr-btn--tertiary-no-outline">Libellé bouton</a>
```

## Groupe de bouton

### Groupe de boutons MD

```html
<ul class="fr-btns-group">
    <li>
        <button type="button" id="button-1008" class="fr-btn fr-btn--secondary">Libellé bouton</button>
    </li>
    <li>
        <button type="button" id="button-1009" class="fr-btn fr-btn--secondary">Libellé bouton</button>
    </li>
    <li>
        <button type="button" id="button-1010" class="fr-btn fr-btn--secondary">Libellé bouton</button>
    </li>
</ul>
```

### Groupe de boutons SM

```html
<ul class="fr-btns-group fr-btns-group--sm">
    <li>
        <button type="button" id="button-1012" class="fr-btn fr-btn--secondary">Libellé bouton SM</button>
    </li>
    <li>
        <button type="button" id="button-1013" class="fr-btn fr-btn--secondary">Libellé bouton SM</button>
    </li>
    <li>
        <button type="button" id="button-1014" class="fr-btn fr-btn--secondary">Libellé bouton SM</button>
    </li>
</ul>
```

### Groupe de boutons LG

```html
<ul class="fr-btns-group fr-btns-group--lg">
    <li>
        <button type="button" id="button-1016" class="fr-btn fr-btn--secondary">Libellé bouton LG</button>
    </li>
    <li>
        <button type="button" id="button-1017" class="fr-btn fr-btn--secondary">Libellé bouton LG</button>
    </li>
    <li>
        <button type="button" id="button-1018" class="fr-btn fr-btn--secondary">Libellé bouton LG</button>
    </li>
</ul>
```

### Groupe de boutons verticaux hiérarchisés avec icones

```html
<ul class="fr-btns-group fr-btns-group--icon-left">
    <li>
        <button type="button" id="button-1020" class="fr-btn fr-icon-checkbox-circle-line fr-btn--icon-left">Libellé bouton</button>
    </li>
    <li>
        <button type="button" id="button-1021" class="fr-btn fr-icon-checkbox-circle-line fr-btn--icon-left fr-btn--secondary">Libellé bouton</button>
    </li>
    <li>
        <button type="button" id="button-1022" class="fr-btn fr-icon-checkbox-circle-line fr-btn--icon-left fr-btn--secondary">Libellé bouton</button>
    </li>
</ul>
```

### Groupe de boutons inline

```html
<ul class="fr-btns-group fr-btns-group--inline">
    <li>
        <button type="button" id="button-1024" class="fr-btn">Libellé bouton</button>
    </li>
    <li>
        <button type="button" id="button-1025" class="fr-btn fr-btn--secondary">Libellé bouton</button>
    </li>
</ul>
```

### Groupe de boutons inline non hiérarchisés

```html
<ul class="fr-btns-group fr-btns-group--inline">
    <li>
        <button type="button" id="button-1027" class="fr-btn fr-btn--secondary">Libellé bouton</button>
    </li>
    <li>
        <button type="button" id="button-1028" class="fr-btn fr-btn--secondary">Libellé bouton</button>
    </li>
</ul>
```

### Groupe de boutons inline à partir du breakpoint SM

```html
<ul class="fr-btns-group fr-btns-group--inline-sm">
    <li>
        <button type="button" id="button-1030" class="fr-btn">Libellé bouton</button>
    </li>
    <li>
        <button type="button" id="button-1031" class="fr-btn fr-btn--secondary">Libellé bouton</button>
    </li>
</ul>
```

### Groupe de boutons inline à partir du breakpoint MD

```html
<ul class="fr-btns-group fr-btns-group--inline-md">
    <li>
        <button type="button" id="button-1033" class="fr-btn">Libellé bouton</button>
    </li>
    <li>
        <button type="button" id="button-1034" class="fr-btn fr-btn--secondary">Libellé bouton</button>
    </li>
</ul>
```

### Groupe de boutons inline à partir du breakpoint LG

```html
<ul class="fr-btns-group fr-btns-group--inline-lg">
    <li>
        <button type="button" id="button-1036" class="fr-btn">Libellé bouton</button>
    </li>
    <li>
        <button type="button" id="button-1037" class="fr-btn fr-btn--secondary">Libellé bouton</button>
    </li>
</ul>
```

### Groupe de boutons inversés en inline à partir du breakpoint SM

```html
<ul class="fr-btns-group fr-btns-group--right fr-btns-group--inline-reverse fr-btns-group--inline-sm">
    <li>
        <button type="button" id="button-1039" class="fr-btn">Libellé bouton</button>
    </li>
    <li>
        <button type="button" id="button-1040" class="fr-btn fr-btn--secondary">Libellé bouton</button>
    </li>
</ul>
```

### Groupe de boutons inline même taille (equisized)

```html
<ul class="fr-btns-group fr-btns-group--equisized fr-btns-group--inline">
    <li>
        <button type="button" id="button-1042" class="fr-btn">Libellé bouton</button>
    </li>
    <li>
        <button type="button" id="button-1043" class="fr-btn fr-btn--secondary">Libellé bouton long</button>
    </li>
    <li>
        <button type="button" id="button-1044" class="fr-btn fr-btn--secondary">Libellé bouton plus long</button>
    </li>
</ul>
```

### Groupe de boutons inline alignés a droite (equisized)

```html
<ul class="fr-btns-group fr-btns-group--right fr-btns-group--equisized fr-btns-group--inline">
    <li>
        <button type="button" id="button-1046" class="fr-btn">Libellé bouton</button>
    </li>
    <li>
        <button type="button" id="button-1047" class="fr-btn fr-btn--secondary">Libellé bouton long</button>
    </li>
    <li>
        <button type="button" id="button-1048" class="fr-btn fr-btn--secondary">Libellé bouton plus long</button>
    </li>
</ul>
```

### Groupe de boutons inline alignés au centre (equisized)

```html
<ul class="fr-btns-group fr-btns-group--center fr-btns-group--equisized fr-btns-group--inline">
    <li>
        <button type="button" id="button-1050" class="fr-btn">Libellé bouton</button>
    </li>
    <li>
        <button type="button" id="button-1051" class="fr-btn fr-btn--secondary">Libellé bouton long</button>
    </li>
    <li>
        <button type="button" id="button-1052" class="fr-btn fr-btn--secondary">Libellé bouton plus long</button>
    </li>
</ul>
```

### Groupe de boutons verticaux même taille (equisized)

```html
<ul class="fr-btns-group fr-btns-group--equisized">
    <li>
        <button type="button" id="button-1054" class="fr-btn">Libellé bouton</button>
    </li>
    <li>
        <button type="button" id="button-1055" class="fr-btn fr-btn--secondary">Libellé bouton long</button>
    </li>
    <li>
        <button type="button" id="button-1056" class="fr-btn fr-btn--secondary">Libellé bouton plus long</button>
    </li>
</ul>
```

### Groupe de boutons verticaux alignés a droite (equisized)

```html
<ul class="fr-btns-group fr-btns-group--right fr-btns-group--equisized">
    <li>
        <button type="button" id="button-1058" class="fr-btn">Libellé bouton</button>
    </li>
    <li>
        <button type="button" id="button-1059" class="fr-btn fr-btn--secondary">Libellé bouton long</button>
    </li>
    <li>
        <button type="button" id="button-1060" class="fr-btn fr-btn--secondary">Libellé bouton plus long</button>
    </li>
</ul>
```

### Groupe de boutons verticaux alignés au centre (equisized)

```html
<ul class="fr-btns-group fr-btns-group--center fr-btns-group--equisized">
    <li>
        <button type="button" id="button-1062" class="fr-btn">Libellé bouton</button>
    </li>
    <li>
        <button type="button" id="button-1063" class="fr-btn fr-btn--secondary">Libellé bouton long</button>
    </li>
    <li>
        <button type="button" id="button-1064" class="fr-btn fr-btn--secondary">Libellé bouton plus long</button>
    </li>
</ul>
```

### Groupe de boutons d'icones

```html
<ul class="fr-btns-group">
    <li>
        <button title="[À MODIFIER - Libellé bouton]" type="button" id="button-1066" class="fr-btn fr-icon-checkbox-circle-line">Libellé bouton</button>
    </li>
    <li>
        <button title="[À MODIFIER - Libellé bouton]" type="button" id="button-1067" class="fr-btn fr-icon-checkbox-circle-line fr-btn--secondary">Libellé bouton</button>
    </li>
    <li>
        <button title="[À MODIFIER - Libellé bouton]" type="button" id="button-1068" class="fr-btn fr-icon-checkbox-circle-line fr-btn--secondary">Libellé bouton</button>
    </li>
</ul>
```

### Groupe de boutons d'icones inline

```html
<ul class="fr-btns-group fr-btns-group--inline">
    <li>
        <button title="[À MODIFIER - Libellé bouton]" type="button" id="button-1070" class="fr-btn fr-icon-checkbox-circle-line">Libellé bouton</button>
    </li>
    <li>
        <button title="[À MODIFIER - Libellé bouton]" type="button" id="button-1071" class="fr-btn fr-icon-checkbox-circle-line fr-btn--secondary">Libellé bouton</button>
    </li>
    <li>
        <button title="[À MODIFIER - Libellé bouton]" type="button" id="button-1072" class="fr-btn fr-icon-checkbox-circle-line fr-btn--secondary">Libellé bouton</button>
    </li>
</ul>
```
