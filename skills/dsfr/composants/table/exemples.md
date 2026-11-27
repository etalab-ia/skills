# Tableau : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Tableau MD (défaut)

```html
<div class="fr-table" id="table-md-component">
    <div class="fr-table__wrapper">
        <div class="fr-table__container">
            <div class="fr-table__content">
                <table id="table-md">
                    <caption>
                        Titre du tableau (caption)
                    </caption>
                    <thead>
                        <tr>
                            <th scope="col">
                                th0
                            </th>
                            <th scope="col">
                                th1
                            </th>
                            <th scope="col">
                                th2
                            </th>
                            <th scope="col">
                                th3
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr id="table-md-row-key-1" data-row-key="1">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-md-row-key-2" data-row-key="2">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-md-row-key-3" data-row-key="3">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-md-row-key-4" data-row-key="4">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
```

### Tableau SM

```html
<div class="fr-table fr-table--sm" id="table-sm-component">
    <div class="fr-table__wrapper">
        <div class="fr-table__container">
            <div class="fr-table__content">
                <table id="table-sm">
                    <caption>
                        Titre du tableau (caption)
                    </caption>
                    <thead>
                        <tr>
                            <th scope="col">
                                th0
                            </th>
                            <th scope="col">
                                th1
                            </th>
                            <th scope="col">
                                th2
                            </th>
                            <th scope="col">
                                th3
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr id="table-sm-row-key-1" data-row-key="1">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-sm-row-key-2" data-row-key="2">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-sm-row-key-3" data-row-key="3">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-sm-row-key-4" data-row-key="4">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
```

### Tableau LG

```html
<div class="fr-table fr-table--lg" id="table-lg-component">
    <div class="fr-table__wrapper">
        <div class="fr-table__container">
            <div class="fr-table__content">
                <table id="table-lg">
                    <caption>
                        Titre du tableau (caption)
                    </caption>
                    <thead>
                        <tr>
                            <th scope="col">
                                th0
                            </th>
                            <th scope="col">
                                th1
                            </th>
                            <th scope="col">
                                th2
                            </th>
                            <th scope="col">
                                th3
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr id="table-lg-row-key-1" data-row-key="1">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-lg-row-key-2" data-row-key="2">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-lg-row-key-3" data-row-key="3">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-lg-row-key-4" data-row-key="4">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
```

### Tableau avec bordures verticales

```html
<div class="fr-table fr-table--bordered" id="table-bordered-component">
    <div class="fr-table__wrapper">
        <div class="fr-table__container">
            <div class="fr-table__content">
                <table id="table-bordered">
                    <caption>
                        Titre du tableau (caption)
                    </caption>
                    <thead>
                        <tr>
                            <th scope="col">
                                th0
                            </th>
                            <th scope="col">
                                th1
                            </th>
                            <th scope="col">
                                th2
                            </th>
                            <th scope="col">
                                th3
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr id="table-bordered-row-key-1" data-row-key="1">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-bordered-row-key-2" data-row-key="2">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-bordered-row-key-3" data-row-key="3">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-bordered-row-key-4" data-row-key="4">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
```

### Tableau non scrollable

```html
<div class="fr-table fr-table--no-scroll" id="table-no-scroll-component">
    <div class="fr-table__wrapper">
        <div class="fr-table__container">
            <div class="fr-table__content">
                <table id="table-no-scroll">
                    <caption>
                        Titre du tableau (caption)
                    </caption>
                    <thead>
                        <tr>
                            <th scope="col">
                                th0
                            </th>
                            <th scope="col">
                                th1
                            </th>
                            <th scope="col">
                                th2
                            </th>
                            <th scope="col">
                                th3
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr id="table-no-scroll-row-key-1" data-row-key="1">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-no-scroll-row-key-2" data-row-key="2">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-no-scroll-row-key-3" data-row-key="3">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-no-scroll-row-key-4" data-row-key="4">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
```

### Exemple des colonnes de tailles minimales fixées

```html
<div class="fr-table" id="table-column-sizes-component">
    <div class="fr-table__wrapper">
        <div class="fr-table__container">
            <div class="fr-table__content">
                <table id="table-column-sizes">
                    <caption>
                        Titre du tableau (caption)
                    </caption>
                    <thead>
                        <tr>
                            <th class="fr-col--xs">
                                xs
                            </th>
                            <th class="fr-col--sm">
                                sm
                            </th>
                            <th class="fr-col--md">
                                md
                            </th>
                            <th class="fr-col--lg">
                                lg
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr id="table-column-sizes-row-key-1" data-row-key="1">
                            <td>
                                Lorem
                            </td>
                            <td>
                                Lorem [...
                            </td>
                            <td>
                                Lorem [...] eli
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-column-sizes-row-key-2" data-row-key="2">
                            <td>
                                Lorem
                            </td>
                            <td>
                                Lorem [...
                            </td>
                            <td>
                                Lorem [...] eli
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-column-sizes-row-key-3" data-row-key="3">
                            <td>
                                Lorem
                            </td>
                            <td>
                                Lorem [...
                            </td>
                            <td>
                                Lorem [...] eli
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-column-sizes-row-key-4" data-row-key="4">
                            <td>
                                Lorem
                            </td>
                            <td>
                                Lorem [...
                            </td>
                            <td>
                                Lorem [...] eli
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
```

### Exemple des classes utilitaires d'alignement

Extrait complet : [exemples/exemple-des-classes-utilitaires-d-alignement-1.html](exemples/exemple-des-classes-utilitaires-d-alignement-1.html) (4 ko)

### Exemple de tableau avec retour à la ligne automatique dans les cellules

```html
<div class="fr-table fr-table--multiline" id="table-multiline-component">
    <div class="fr-table__wrapper">
        <div class="fr-table__container">
            <div class="fr-table__content">
                <table id="table-multiline">
                    <caption>
                        Titre du tableau (caption)
                    </caption>
                    <thead>
                        <tr>
                            <th scope="col">
                                th0
                            </th>
                            <th scope="col">
                                th1
                            </th>
                            <th scope="col">
                                th2
                            </th>
                            <th scope="col">
                                th3
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr id="table-multiline-row-key-1" data-row-key="1">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-multiline-row-key-2" data-row-key="2">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-multiline-row-key-3" data-row-key="3">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-multiline-row-key-4" data-row-key="4">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
```

### Exemple de tableau avec retour à la ligne automatique dans une cellule

```html
<div class="fr-table" id="table-multiline-component">
    <div class="fr-table__wrapper">
        <div class="fr-table__container">
            <div class="fr-table__content">
                <table id="table-multiline">
                    <caption>
                        Titre du tableau (caption)
                    </caption>
                    <thead>
                        <tr>
                            <th>
                                th0
                            </th>
                            <th>
                                th1
                            </th>
                            <th>
                                th2
                            </th>
                            <th>
                                th3
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr id="table-multiline-row-key-1" data-row-key="1">
                            <td>
                                Lorem ipsum dolor sit ame
                            </td>
                            <td>
                                Lorem ipsum dolor sit ame
                            </td>
                            <td>
                                Lorem ipsum dolor sit ame
                            </td>
                            <td>
                                Lorem ipsum dolor sit ame
                            </td>
                        </tr>
                        <tr id="table-multiline-row-key-2" data-row-key="2">
                            <td>
                                Lorem ipsum dolor sit ame
                            </td>
                            <td class="fr-cell--multiline">
                                <b>Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan la</b>
                            </td>
                            <td>
                                Lorem ipsum dolor sit ame
                            </td>
                            <td>
                                Lorem ipsum dolor sit ame
                            </td>
                        </tr>
                        <tr id="table-multiline-row-key-3" data-row-key="3">
                            <td>
                                Lorem ipsum dolor sit ame
                            </td>
                            <td>
                                Lorem ipsum dolor sit ame
                            </td>
                            <td>
                                Lorem ipsum dolor sit ame
                            </td>
                            <td>
                                Lorem ipsum dolor sit ame
                            </td>
                        </tr>
                        <tr id="table-multiline-row-key-4" data-row-key="4">
                            <td>
                                Lorem ipsum dolor sit ame
                            </td>
                            <td>
                                Lorem ipsum dolor sit ame
                            </td>
                            <td>
                                Lorem ipsum dolor sit ame
                            </td>
                            <td>
                                Lorem ipsum dolor sit ame
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
```

### Tableau avec titre invisible

```html
<div class="fr-table fr-table--no-caption" id="table-noCaption-component">
    <div class="fr-table__wrapper">
        <div class="fr-table__container">
            <div class="fr-table__content">
                <table id="table-noCaption">
                    <caption>
                        Titre du tableau (caption)
                    </caption>
                    <thead>
                        <tr>
                            <th scope="col">
                                th0
                            </th>
                            <th scope="col">
                                th1
                            </th>
                            <th scope="col">
                                th2
                            </th>
                            <th scope="col">
                                th3
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr id="table-noCaption-row-key-1" data-row-key="1">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-noCaption-row-key-2" data-row-key="2">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-noCaption-row-key-3" data-row-key="3">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-noCaption-row-key-4" data-row-key="4">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
```

### Tableau avec titre en bas

```html
<div class="fr-table fr-table--caption-bottom" id="table-captionBottom-component">
    <div class="fr-table__wrapper">
        <div class="fr-table__container">
            <div class="fr-table__content">
                <table id="table-captionBottom">
                    <caption>
                        Titre du tableau (caption)
                    </caption>
                    <thead>
                        <tr>
                            <th scope="col">
                                th0
                            </th>
                            <th scope="col">
                                th1
                            </th>
                            <th scope="col">
                                th2
                            </th>
                            <th scope="col">
                                th3
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr id="table-captionBottom-row-key-1" data-row-key="1">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-captionBottom-row-key-2" data-row-key="2">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-captionBottom-row-key-3" data-row-key="3">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="table-captionBottom-row-key-4" data-row-key="4">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
```

### Tableau avec lignes sélectionnables

Extrait complet : [exemples/tableau-avec-lignes-selectionnables-2.html](exemples/tableau-avec-lignes-selectionnables-2.html) (6 ko)

### Tableau avec première colonne fixée à partir du breakpoint MD (existe en SM, MD et LG)

Extrait complet : [exemples/tableau-avec-premiere-colonne-fixee-a-partir-du-br-3.html](exemples/tableau-avec-premiere-colonne-fixee-a-partir-du-br-3.html) (6 ko)

### Tableau à double entrée

Extrait complet : [exemples/tableau-a-double-entree-4.html](exemples/tableau-a-double-entree-4.html) (4 ko)

### Tableau complexe (comportant des cellules fusionnées)

Extrait complet : [exemples/tableau-complexe-comportant-des-cellules-fusionnee-5.html](exemples/tableau-complexe-comportant-des-cellules-fusionnee-5.html) (9 ko)

### Tableau avec recherche

Extrait complet : [exemples/tableau-avec-recherche-6.html](exemples/tableau-avec-recherche-6.html) (7 ko)

### Tableau avec filtre et navigation comportant différents types de données

Extrait complet : [exemples/tableau-avec-filtre-et-navigation-comportant-diffe-7.html](exemples/tableau-avec-filtre-et-navigation-comportant-diffe-7.html) (32 ko)
