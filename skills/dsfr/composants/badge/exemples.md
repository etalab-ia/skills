# Badge : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Badge seul

```html
<p id="badge-719" class="fr-badge">Libellé badge</p>
```

### Badge sur une seule ligne - ellipsis

Il est conseillé d'ajouter une balise span avec la classe fr-ellipsis à l'interieur du badge pour que celui ci reste sur une seule ligne, avec le texte coupé par des points de suspensions.

```html
<p class="fr-badge">
    <span class="fr-ellipsis">Libellé badge très long, coupé par des points de suspensions lorsque le Libellé dépasse la largeur du conteneur</span>
</p>
```

### Badge - succès

```html
<p id="badge-722" class="fr-badge fr-badge--success">Libellé badge</p>
```

### Badge - succès sans icone

```html
<p id="badge-724" class="fr-badge fr-badge--success fr-badge--no-icon">Libellé badge</p>
```

### Badge - erreur

```html
<p id="badge-726" class="fr-badge fr-badge--error">Libellé badge</p>
```

### Badge - erreur sans icone

```html
<p id="badge-728" class="fr-badge fr-badge--error fr-badge--no-icon">Libellé badge</p>
```

### Badge - information

```html
<p id="badge-730" class="fr-badge fr-badge--info">Libellé badge</p>
```

### Badge - information sans icone

```html
<p id="badge-732" class="fr-badge fr-badge--info fr-badge--no-icon">Libellé badge</p>
```

### Badge - avertissement

```html
<p id="badge-734" class="fr-badge fr-badge--warning">Libellé badge</p>
```

### Badge - avertissement sans icone

```html
<p id="badge-736" class="fr-badge fr-badge--warning fr-badge--no-icon">Libellé badge</p>
```

### Badge - nouveauté

```html
<p id="badge-738" class="fr-badge fr-badge--new">Libellé badge</p>
```

### Badge - nouveauté sans icone

```html
<p id="badge-740" class="fr-badge fr-badge--new fr-badge--no-icon">Libellé badge</p>
```

### Badge - personnalisé green-menthe

```html
<p id="badge-742" class="fr-badge fr-badge--green-menthe">Libellé badge</p>
```

### Badge - personnalisé orange-terre-battue

```html
<p id="badge-744" class="fr-badge fr-badge--orange-terre-battue">Libellé badge</p>
```

### Badge - personnalisé purple-glycine

```html
<p id="badge-746" class="fr-badge fr-badge--purple-glycine">Libellé badge</p>
```

### Badge taille SM

```html
<p id="badge-749" class="fr-badge fr-badge--sm">Libellé badge</p>
```

### Badge SM - succès

```html
<p id="badge-751" class="fr-badge fr-badge--sm fr-badge--success">Libellé badge</p>
```

### Badge SM - erreur

```html
<p id="badge-753" class="fr-badge fr-badge--sm fr-badge--error">Libellé badge</p>
```

### Badge SM - information

```html
<p id="badge-755" class="fr-badge fr-badge--sm fr-badge--info">Libellé badge</p>
```

### Badge SM - avertissement

```html
<p id="badge-757" class="fr-badge fr-badge--sm fr-badge--warning">Libellé badge</p>
```

### Badge SM - nouveauté

```html
<p id="badge-759" class="fr-badge fr-badge--sm fr-badge--new">Libellé badge</p>
```

### Badge SM - personnalisé purple-glycine

```html
<p id="badge-761" class="fr-badge fr-badge--sm fr-badge--purple-glycine">Libellé badge</p>
```

## Groupe de badges

### Groupe de badges

Lorsque que l'on a plus d'un badge, il convient d'utiliser un groupe de badges. La taille de tous les badges peut être définie au niveau du groupe.

```html
<ul class="fr-badges-group">
    <li>
        <span id="badge-763" class="fr-badge">Libellé badge 1</span>
    </li>
    <li>
        <span id="badge-764" class="fr-badge">Libellé badge 2</span>
    </li>
    <li>
        <span id="badge-765" class="fr-badge">Libellé badge 3</span>
    </li>
    <li>
        <span id="badge-766" class="fr-badge">Libellé badge 4</span>
    </li>
    <li>
        <span id="badge-767" class="fr-badge">Libellé badge 5</span>
    </li>
    <li>
        <span id="badge-768" class="fr-badge">Libellé badge 6</span>
    </li>
    <li>
        <span id="badge-769" class="fr-badge">Libellé badge 7</span>
    </li>
    <li>
        <span id="badge-770" class="fr-badge">Libellé badge 8</span>
    </li>
    <li>
        <span id="badge-771" class="fr-badge">Libellé badge 9</span>
    </li>
</ul>
```

### Groupe de badges SM

```html
<ul class="fr-badges-group fr-badges-group--sm">
    <li>
        <span id="badge-773" class="fr-badge">Libellé badge 1</span>
    </li>
    <li>
        <span id="badge-774" class="fr-badge">Libellé badge 2</span>
    </li>
    <li>
        <span id="badge-775" class="fr-badge">Libellé badge 3</span>
    </li>
    <li>
        <span id="badge-776" class="fr-badge">Libellé badge 4</span>
    </li>
    <li>
        <span id="badge-777" class="fr-badge">Libellé badge 5</span>
    </li>
    <li>
        <span id="badge-778" class="fr-badge">Libellé badge 6</span>
    </li>
    <li>
        <span id="badge-779" class="fr-badge">Libellé badge 7</span>
    </li>
    <li>
        <span id="badge-780" class="fr-badge">Libellé badge 8</span>
    </li>
    <li>
        <span id="badge-781" class="fr-badge">Libellé badge 9</span>
    </li>
</ul>
```
