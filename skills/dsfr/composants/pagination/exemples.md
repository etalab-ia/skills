# Pagination : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Élément de navigation icône seule (par défaut)

```html
<nav role="navigation" class="fr-pagination" aria-label="Pagination">
    <ul class="fr-pagination__list">
        <li>
            <a class="fr-pagination__link fr-pagination__link--prev" href="#">
                Page précédente
            </a>
        </li>
    </ul>
</nav>
```

### Élément de navigation avec libellés

```html
<nav role="navigation" class="fr-pagination" aria-label="Pagination">
    <ul class="fr-pagination__list">
        <li>
            <a class="fr-pagination__link fr-pagination__link--prev fr-pagination__link--label" href="#">
                Page précédente
            </a>
        </li>
    </ul>
</nav>
```

### Élément de navigation avec libellés à partir du breakpoint LG

```html
<nav role="navigation" class="fr-pagination" aria-label="Pagination">
    <ul class="fr-pagination__list">
        <li>
            <a class="fr-pagination__link fr-pagination__link--prev fr-pagination__link--lg-label" href="#">
                Page précédente
            </a>
        </li>
    </ul>
</nav>
```

### Pagination première page

```html
<nav role="navigation" class="fr-pagination" aria-label="Pagination" data-fr-analytics-page-total="132">
    <ul class="fr-pagination__list">
        <li>
            <a class="fr-pagination__link fr-pagination__link--first" id="pagination-6587" title="Première page" aria-disabled="true" role="link">
                Première page
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-pagination__link--prev fr-pagination__link--lg-label" id="pagination-6588" title="Page précédente" aria-disabled="true" role="link">
                Page précédente
            </a>
        </li>
        <li>
            <a class="fr-pagination__link" id="pagination-6580" aria-current="page" title="Page 1">
                1
            </a>
        </li>
        <li>
            <a class="fr-pagination__link" id="pagination-6581" href="#" title="Page 2">
                2
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6582" href="#" title="Page 3">
                3
            </a>
        </li>
        <li>
            <span class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6583">
                …
            </span>
        </li>
        <li>
            <a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6584" href="#" title="Page 130">
                130
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6585" href="#" title="Page 131">
                131
            </a>
        </li>
        <li>
            <a class="fr-pagination__link" id="pagination-6586" href="#" title="Page 132">
                132
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-pagination__link--next fr-pagination__link--lg-label" id="pagination-6589" href="#" title="Page suivante">
                Page suivante
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-pagination__link--last" id="pagination-6590" href="#" title="Dernière page">
                Dernière page
            </a>
        </li>
    </ul>
</nav>
```

### Pagination deuxième page

```html
<nav role="navigation" class="fr-pagination" aria-label="Pagination" data-fr-analytics-page-total="132">
    <ul class="fr-pagination__list">
        <li>
            <a class="fr-pagination__link fr-pagination__link--first" id="pagination-6610" href="#" title="Première page">
                Première page
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-pagination__link--prev fr-pagination__link--lg-label" id="pagination-6611" href="#" title="Page précédente">
                Page précédente
            </a>
        </li>
        <li>
            <a class="fr-pagination__link" id="pagination-6603" href="#" title="Page 1">
                1
            </a>
        </li>
        <li>
            <a class="fr-pagination__link" id="pagination-6604" aria-current="page" title="Page 2">
                2
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6605" href="#" title="Page 3">
                3
            </a>
        </li>
        <li>
            <span class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6606">
                …
            </span>
        </li>
        <li>
            <a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6607" href="#" title="Page 130">
                130
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6608" href="#" title="Page 131">
                131
            </a>
        </li>
        <li>
            <a class="fr-pagination__link" id="pagination-6609" href="#" title="Page 132">
                132
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-pagination__link--next fr-pagination__link--lg-label" id="pagination-6612" href="#" title="Page suivante">
                Page suivante
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-pagination__link--last" id="pagination-6613" href="#" title="Dernière page">
                Dernière page
            </a>
        </li>
    </ul>
</nav>
```

### Pagination dernière page

```html
<nav role="navigation" class="fr-pagination" aria-label="Pagination" data-fr-analytics-page-total="132">
    <ul class="fr-pagination__list">
        <li>
            <a class="fr-pagination__link fr-pagination__link--first" id="pagination-6633" href="#" title="Première page">
                Première page
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-pagination__link--prev fr-pagination__link--lg-label" id="pagination-6634" href="#" title="Page précédente">
                Page précédente
            </a>
        </li>
        <li>
            <a class="fr-pagination__link" id="pagination-6626" href="#" title="Page 1">
                1
            </a>
        </li>
        <li>
            <a class="fr-pagination__link" id="pagination-6627" href="#" title="Page 2">
                2
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6628" href="#" title="Page 3">
                3
            </a>
        </li>
        <li>
            <span class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6629">
                …
            </span>
        </li>
        <li>
            <a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6630" href="#" title="Page 130">
                130
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6631" href="#" title="Page 131">
                131
            </a>
        </li>
        <li>
            <a class="fr-pagination__link" id="pagination-6632" aria-current="page" title="Page 132">
                132
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-pagination__link--next fr-pagination__link--lg-label" id="pagination-6635" title="Page suivante" aria-disabled="true" role="link">
                Page suivante
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-pagination__link--last" id="pagination-6636" title="Dernière page" aria-disabled="true" role="link">
                Dernière page
            </a>
        </li>
    </ul>
</nav>
```
