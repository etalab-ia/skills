# Lien : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Lien seul

```html
<a id="link-4210" href="#" class="fr-link">Libellé lien</a>
```

### Lien icon à gauche

```html
<a id="link-4213" href="#" class="fr-link fr-icon-arrow-left-line fr-link--icon-left">Libellé lien</a>
```

### Lien icon à droite

```html
<a id="link-4216" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien</a>
```

### Lien seul SM

```html
<a id="link-4219" href="#" class="fr-link fr-link--sm">Libellé lien</a>
```

### Lien seul LG

```html
<a id="link-4222" href="#" class="fr-link fr-link--lg">Libellé lien</a>
```

### Lien seul désactivé

```html
<a id="link-4225" aria-disabled="true" role="link" class="fr-link">Libellé lien</a>
```

### Lien externe

```html
<a id="link-4228" href="#" target="_blank" rel="noopener external" class="fr-link">Libellé lien</a>
```

## Groupe de liens

### Groupe de liens

Lorsque que l'on a plus d'un lien, il convient d'utiliser un groupe de liens. La taille de tous les liens peut être définie au niveau du groupe.

```html
<ul class="fr-links-group">
    <li>
        <a id="link-4239" href="#" class="fr-link">Libellé lien 1</a>
    </li>
    <li>
        <a id="link-4240" href="#" class="fr-link fr-icon-arrow-left-line fr-link--icon-left">Libellé lien 2</a>
    </li>
    <li>
        <a id="link-4241" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 3</a>
    </li>
    <li>
        <a id="link-4242" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 4</a>
    </li>
    <li>
        <a id="link-4243" href="#" class="fr-link fr-icon-arrow-left-line fr-link--icon-left">Libellé lien 5</a>
    </li>
    <li>
        <a id="link-4244" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 6</a>
    </li>
    <li>
        <a id="link-4245" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 7</a>
    </li>
    <li>
        <a id="link-4246" href="#" class="fr-link fr-icon-arrow-left-line fr-link--icon-left">Libellé lien 8</a>
    </li>
    <li>
        <a id="link-4247" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 9</a>
    </li>
</ul>
```

### Groupe de liens sm

```html
<ul class="fr-links-group fr-links-group--sm">
    <li>
        <a id="link-4258" href="#" class="fr-link">Libellé lien 1</a>
    </li>
    <li>
        <a id="link-4259" href="#" class="fr-link fr-icon-arrow-left-line fr-link--icon-left">Libellé lien 2</a>
    </li>
    <li>
        <a id="link-4260" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 3</a>
    </li>
    <li>
        <a id="link-4261" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 4</a>
    </li>
    <li>
        <a id="link-4262" href="#" class="fr-link fr-icon-arrow-left-line fr-link--icon-left">Libellé lien 5</a>
    </li>
    <li>
        <a id="link-4263" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 6</a>
    </li>
    <li>
        <a id="link-4264" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 7</a>
    </li>
    <li>
        <a id="link-4265" href="#" class="fr-link fr-icon-arrow-left-line fr-link--icon-left">Libellé lien 8</a>
    </li>
    <li>
        <a id="link-4266" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 9</a>
    </li>
</ul>
```

### Groupe de liens lg

```html
<ul class="fr-links-group fr-links-group--lg">
    <li>
        <a id="link-4277" href="#" class="fr-link">Libellé lien 1</a>
    </li>
    <li>
        <a id="link-4278" href="#" class="fr-link fr-icon-arrow-left-line fr-link--icon-left">Libellé lien 2</a>
    </li>
    <li>
        <a id="link-4279" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 3</a>
    </li>
    <li>
        <a id="link-4280" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 4</a>
    </li>
    <li>
        <a id="link-4281" href="#" class="fr-link fr-icon-arrow-left-line fr-link--icon-left">Libellé lien 5</a>
    </li>
    <li>
        <a id="link-4282" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 6</a>
    </li>
    <li>
        <a id="link-4283" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 7</a>
    </li>
    <li>
        <a id="link-4284" href="#" class="fr-link fr-icon-arrow-left-line fr-link--icon-left">Libellé lien 8</a>
    </li>
    <li>
        <a id="link-4285" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 9</a>
    </li>
</ul>
```

### Groupe de liens en ligne

```html
<ul class="fr-links-group fr-links-group--inline">
    <li>
        <a id="link-4296" href="#" class="fr-link">Libellé lien 1</a>
    </li>
    <li>
        <a id="link-4297" href="#" class="fr-link fr-icon-arrow-left-line fr-link--icon-left">Libellé lien 2</a>
    </li>
    <li>
        <a id="link-4298" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 3</a>
    </li>
    <li>
        <a id="link-4299" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 4</a>
    </li>
    <li>
        <a id="link-4300" href="#" class="fr-link fr-icon-arrow-left-line fr-link--icon-left">Libellé lien 5</a>
    </li>
    <li>
        <a id="link-4301" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 6</a>
    </li>
    <li>
        <a id="link-4302" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 7</a>
    </li>
    <li>
        <a id="link-4303" href="#" class="fr-link fr-icon-arrow-left-line fr-link--icon-left">Libellé lien 8</a>
    </li>
    <li>
        <a id="link-4304" href="#" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Libellé lien 9</a>
    </li>
</ul>
```
