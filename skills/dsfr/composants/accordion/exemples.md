# Accordéon : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Accordéon

```html
<section class="fr-accordion">
    <h3 class="fr-accordion__title">
        <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-529">Libellé accordéon</button>
    </h3>
    <div class="fr-collapse" id="accordion-529">
        <!-- données de test -->
    </div>
</section>
```

### Groupe d‘accordéons

```html
<div class="fr-accordions-group">
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-537">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse" id="accordion-537">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-538">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse" id="accordion-538">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-539">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse" id="accordion-539">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-540">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse" id="accordion-540">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-541">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse" id="accordion-541">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-542">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse" id="accordion-542">
            <!-- données de test -->
        </div>
    </section>
</div>
```

### Groupe d‘accordéons ouvert au chargement

```html
<div class="fr-accordions-group">
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="true" aria-controls="accordion-550">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse fr-collapse--expanded" id="accordion-550">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-551">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse" id="accordion-551">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-552">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse" id="accordion-552">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-553">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse" id="accordion-553">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-554">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse" id="accordion-554">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-555">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse" id="accordion-555">
            <!-- données de test -->
        </div>
    </section>
</div>
```

### Groupe d‘accordéons dissociés

```html
<div data-fr-group="false" class="fr-accordions-group">
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-563">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse" id="accordion-563">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-564">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse" id="accordion-564">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-565">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse" id="accordion-565">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-566">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse" id="accordion-566">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-567">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse" id="accordion-567">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-568">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse" id="accordion-568">
            <!-- données de test -->
        </div>
    </section>
</div>
```

### Groupe d‘accordéons dissociés ouvert au chargement

```html
<div data-fr-group="false" class="fr-accordions-group">
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="true" aria-controls="accordion-576">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse fr-collapse--expanded" id="accordion-576">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="true" aria-controls="accordion-577">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse fr-collapse--expanded" id="accordion-577">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="true" aria-controls="accordion-578">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse fr-collapse--expanded" id="accordion-578">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="true" aria-controls="accordion-579">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse fr-collapse--expanded" id="accordion-579">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="true" aria-controls="accordion-580">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse fr-collapse--expanded" id="accordion-580">
            <!-- données de test -->
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button type="button" class="fr-accordion__btn" aria-expanded="true" aria-controls="accordion-581">Libellé accordéon</button>
        </h3>
        <div class="fr-collapse fr-collapse--expanded" id="accordion-581">
            <!-- données de test -->
        </div>
    </section>
</div>
```
