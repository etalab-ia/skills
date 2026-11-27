# Onglet : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Onglets 4 éléments

```html
<div class="fr-tabs">
    <ul class="fr-tabs__list" role="tablist" aria-label="[A modifier | nom du système d'onglet]">
        <li role="presentation">
            <button type="button" id="tab-6488" class="fr-tabs__tab fr-icon-checkbox-circle-line fr-tabs__tab--icon-left" tabindex="0" role="tab" aria-selected="true" aria-controls="tab-6488-panel">Libellé onglet 1</button>
        </li>
        <li role="presentation">
            <button type="button" id="tab-6489" class="fr-tabs__tab fr-icon-checkbox-circle-line fr-tabs__tab--icon-left" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6489-panel">Libellé onglet 2</button>
        </li>
        <li role="presentation">
            <button type="button" id="tab-6490" class="fr-tabs__tab fr-icon-checkbox-circle-line fr-tabs__tab--icon-left" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6490-panel">Libellé onglet 3</button>
        </li>
        <li role="presentation">
            <button type="button" id="tab-6491" class="fr-tabs__tab fr-icon-checkbox-circle-line fr-tabs__tab--icon-left" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6491-panel">Libellé onglet 4</button>
        </li>
    </ul>
    <div id="tab-6488-panel" class="fr-tabs__panel fr-tabs__panel--selected" role="tabpanel" aria-labelledby="tab-6488" tabindex="0">
        <!-- données de test -->
    </div>
    <div id="tab-6489-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6489" tabindex="0">
        <!-- données de test -->
    </div>
    <div id="tab-6490-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6490" tabindex="0">
        <!-- données de test -->
    </div>
    <div id="tab-6491-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6491" tabindex="0">
        <!-- données de test -->
    </div>
</div>
```

### Onglets 2 éléments

```html
<div class="fr-tabs">
    <ul class="fr-tabs__list" role="tablist" aria-label="[A modifier | nom du système d'onglet]">
        <li role="presentation">
            <button type="button" id="tab-6495" class="fr-tabs__tab" tabindex="0" role="tab" aria-selected="true" aria-controls="tab-6495-panel">Libellé onglet 1</button>
        </li>
        <li role="presentation">
            <button type="button" id="tab-6496" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6496-panel">Libellé onglet 2</button>
        </li>
    </ul>
    <div id="tab-6495-panel" class="fr-tabs__panel fr-tabs__panel--selected" role="tabpanel" aria-labelledby="tab-6495" tabindex="0">
        <!-- données de test -->
    </div>
    <div id="tab-6496-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6496" tabindex="0">
        <!-- données de test -->
    </div>
</div>
```

### Onglets dans onglets

Extrait complet : [exemples/onglets-dans-onglets-1.html](exemples/onglets-dans-onglets-1.html) (11 ko)

### Accordéon dans onglets

```html
<div class="fr-tabs">
    <ul class="fr-tabs__list" role="tablist" aria-label="[A modifier | nom du système d'onglet]">
        <li role="presentation">
            <button type="button" id="tab-accordion-6555" class="fr-tabs__tab" tabindex="0" role="tab" aria-selected="true" aria-controls="tab-accordion-6555-panel">Libellé onglet 1</button>
        </li>
        <li role="presentation">
            <button type="button" id="tab-accordion-6557" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-accordion-6557-panel">Libellé onglet 2</button>
        </li>
    </ul>
    <div id="tab-accordion-6555-panel" class="fr-tabs__panel fr-tabs__panel--selected" role="tabpanel" aria-labelledby="tab-accordion-6555" tabindex="0">
        <section class="fr-accordion">
            <h3 class="fr-accordion__title">
                <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-6556">Libellé accordéon</button>
            </h3>
            <div class="fr-collapse" id="accordion-6556">
                <!-- données de test -->
            </div>
        </section>
    </div>
    <div id="tab-accordion-6557-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-accordion-6557" tabindex="0">
        <section class="fr-accordion">
            <h3 class="fr-accordion__title">
                <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-6558">Libellé accordéon</button>
            </h3>
            <div class="fr-collapse" id="accordion-6558">
                <!-- données de test -->
            </div>
        </section>
    </div>
</div>
```

### Onglets 100% largeur du viewport en mobile

```html
<div class="fr-tabs fr-tabs--viewport-width">
    <ul class="fr-tabs__list" role="tablist" aria-label="[A modifier | nom du système d'onglet]">
        <li role="presentation">
            <button type="button" id="tab-6562" class="fr-tabs__tab" tabindex="0" role="tab" aria-selected="true" aria-controls="tab-6562-panel">Libellé onglet 1</button>
        </li>
        <li role="presentation">
            <button type="button" id="tab-6563" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6563-panel">Libellé onglet 2</button>
        </li>
    </ul>
    <div id="tab-6562-panel" class="fr-tabs__panel fr-tabs__panel--selected" role="tabpanel" aria-labelledby="tab-6562" tabindex="0">
        <!-- données de test -->
    </div>
    <div id="tab-6563-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6563" tabindex="0">
        <!-- données de test -->
    </div>
</div>
```
