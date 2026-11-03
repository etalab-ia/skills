# Fil d'Ariane : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Fil d’Ariane avec liens

```html
<nav role="navigation" class="fr-breadcrumb" aria-label="vous êtes ici :">
    <button type="button" class="fr-breadcrumb__button" aria-expanded="false" aria-controls="breadcrumb-3722">Voir le fil d’Ariane</button>
    <div class="fr-collapse" id="breadcrumb-3722">
        <ol class="fr-breadcrumb__list">
            <li>
                <a class="fr-breadcrumb__link" id="breadcrumb-3714" href="../">Accueil</a>
            </li>
            <li>
                <a class="fr-breadcrumb__link" id="breadcrumb-3715" href="../">Segment 1: lorem ipsum</a>
            </li>
            <li>
                <a class="fr-breadcrumb__link" id="breadcrumb-3716" href="../">Segment 2: lorem ipsum</a>
            </li>
            <li>
                <a class="fr-breadcrumb__link" id="breadcrumb-3717" href="../">Segment 3: lorem ipsum</a>
            </li>
            <li>
                <a class="fr-breadcrumb__link" id="breadcrumb-3718" href="../">Segment 4: lorem ipsum</a>
            </li>
            <li>
                <a class="fr-breadcrumb__link" id="breadcrumb-3719" href="../">Segment 5: lorem ipsum</a>
            </li>
            <li>
                <a class="fr-breadcrumb__link" id="breadcrumb-3720" href="../">Segment 6: lorem ipsum</a>
            </li>
            <li>
                <a class="fr-breadcrumb__link" id="breadcrumb-3721" href="../">Segment 7: lorem ipsum</a>
            </li>
            <li>
                <a class="fr-breadcrumb__link" aria-current="page">Page Actuelle</a>
            </li>
        </ol>
    </div>
</nav>
```
