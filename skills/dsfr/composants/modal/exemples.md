# Modale : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Modale simple

```html
<button data-fr-opened="false" aria-controls="modal-6110" id="button-modal-6110" type="button" class="fr-btn">Modale simple</button>
<dialog id="modal-6110" class="fr-modal" aria-labelledby="modal-6110-title">
    <div class="fr-container fr-container--fluid fr-container-md">
        <div class="fr-grid-row fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
                <div class="fr-modal__body">
                    <div class="fr-modal__header">
                        <button aria-controls="modal-6110" title="Fermer" type="button" id="button-6111" class="fr-btn--close fr-btn">Fermer</button>
                    </div>
                    <div class="fr-modal__content">
                        <h2 id="modal-6110-title" class="fr-modal__title">
                            <span class="fr-icon-arrow-right-line fr-icon--lg" aria-hidden="true"></span>
                            Titre de la modale
                        </h2>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</dialog>
```

### Modale SM

```html
<button data-fr-opened="false" aria-controls="modal-6115" id="button-modal-6115" type="button" class="fr-btn">Modale SM</button>
<dialog id="modal-6115" class="fr-modal" aria-labelledby="modal-6115-title">
    <div class="fr-container fr-container--fluid fr-container-md">
        <div class="fr-grid-row fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-6 fr-col-lg-4">
                <div class="fr-modal__body">
                    <div class="fr-modal__header">
                        <button aria-controls="modal-6115" title="Fermer" type="button" id="button-6116" class="fr-btn--close fr-btn">Fermer</button>
                    </div>
                    <div class="fr-modal__content">
                        <h2 id="modal-6115-title" class="fr-modal__title">
                            <span class="fr-icon-arrow-right-line fr-icon--lg" aria-hidden="true"></span>
                            Titre de la modale
                        </h2>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</dialog>
```

### Modale LG

```html
<button data-fr-opened="false" aria-controls="modal-6120" id="button-modal-6120" type="button" class="fr-btn">Modale LG</button>
<dialog id="modal-6120" class="fr-modal" aria-labelledby="modal-6120-title">
    <div class="fr-container fr-container--fluid fr-container-md">
        <div class="fr-grid-row fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-10 fr-col-lg-8">
                <div class="fr-modal__body">
                    <div class="fr-modal__header">
                        <button aria-controls="modal-6120" title="Fermer" type="button" id="button-6121" class="fr-btn--close fr-btn">Fermer</button>
                    </div>
                    <div class="fr-modal__content">
                        <h2 id="modal-6120-title" class="fr-modal__title">
                            <span class="fr-icon-arrow-right-line fr-icon--lg" aria-hidden="true"></span>
                            Titre de la modale
                        </h2>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</dialog>
```

### Modale formulaire

Extrait complet : [exemples/modale-formulaire-1.html](exemples/modale-formulaire-1.html) (4 ko)

### Modale avec iframe

```html
<button data-fr-opened="false" aria-controls="modal-6130" id="button-modal-6130" type="button" class="fr-btn">Modale iframe</button>
<dialog id="modal-6130" class="fr-modal" aria-labelledby="modal-6130-title">
    <div class="fr-container fr-container--fluid fr-container-md">
        <div class="fr-grid-row fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
                <div class="fr-modal__body">
                    <div class="fr-modal__header">
                        <button aria-controls="modal-6130" title="Fermer" type="button" id="button-6131" class="fr-btn--close fr-btn">Fermer</button>
                    </div>
                    <div class="fr-modal__content">
                        <h2 id="modal-6130-title" class="fr-modal__title">
                            <span class="fr-icon-arrow-right-line fr-icon--lg" aria-hidden="true"></span>
                            Titre de la modale
                        </h2>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.</p>
                        <iframe title="Titre de l&#39;iframe" class="fr-responsive-vid" src="https://www.youtube.com/embed/HyirpmPL43I" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    </div>
                </div>
            </div>
        </div>
    </div>
</dialog>
```

### Modale avec zone d'action et boutons

Extrait complet : [exemples/modale-avec-zone-d-action-et-boutons-2.html](exemples/modale-avec-zone-d-action-et-boutons-2.html) (5 ko)

### Modale avec zone d'action ancré en haut en mobile

Extrait complet : [exemples/modale-avec-zone-d-action-ancre-en-haut-en-mobile-3.html](exemples/modale-avec-zone-d-action-ancre-en-haut-en-mobile-3.html) (5 ko)

### Modale avec zone d'action, tableau et tooltip

Extrait complet : [exemples/modale-avec-zone-d-action-tableau-et-tooltip-4.html](exemples/modale-avec-zone-d-action-tableau-et-tooltip-4.html) (13 ko)

### Modale avec titre sans niveau d'en-tête

```html
<button data-fr-opened="false" aria-controls="modal-6150" id="button-modal-6150" type="button" class="fr-btn">Modale avec titre en p</button>
<dialog id="modal-6150" class="fr-modal" aria-labelledby="modal-6150-title">
    <div class="fr-container fr-container--fluid fr-container-md">
        <div class="fr-grid-row fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
                <div class="fr-modal__body">
                    <div class="fr-modal__header">
                        <button aria-controls="modal-6150" title="Fermer" type="button" id="button-6151" class="fr-btn--close fr-btn">Fermer</button>
                    </div>
                    <div class="fr-modal__content">
                        <p id="modal-6150-title" class="fr-modal__title">
                            <span class="fr-icon-arrow-right-line fr-icon--lg" aria-hidden="true"></span>
                            Titre de la modale
                        </p>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</dialog>
```

### Modale simple non refermable au click sur le fond

```html
<button data-fr-opened="false" aria-controls="modal-6155" id="button-modal-6155" type="button" class="fr-btn">Modale simple</button>
<dialog id="modal-6155" class="fr-modal" aria-labelledby="modal-6155-title" data-fr-concealing-backdrop="false">
    <div class="fr-container fr-container--fluid fr-container-md">
        <div class="fr-grid-row fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
                <div class="fr-modal__body">
                    <div class="fr-modal__header">
                        <button aria-controls="modal-6155" title="Fermer" type="button" id="button-6156" class="fr-btn--close fr-btn">Fermer</button>
                    </div>
                    <div class="fr-modal__content">
                        <h2 id="modal-6155-title" class="fr-modal__title">
                            <span class="fr-icon-arrow-right-line fr-icon--lg" aria-hidden="true"></span>
                            Titre de la modale
                        </h2>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</dialog>
```

### Modale sans bouton lié

```html
<button onclick="window.dsfr(this.nextElementSibling).modal.disclose()" type="button" class="fr-btn">Ouverture programmatique</button>
<dialog id="modal-6160" class="fr-modal" aria-labelledby="modal-6160-title">
    <div class="fr-container fr-container--fluid fr-container-md">
        <div class="fr-grid-row fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
                <div class="fr-modal__body">
                    <div class="fr-modal__header">
                        <button aria-controls="modal-6160" title="Fermer" type="button" id="button-6161" class="fr-btn--close fr-btn">Fermer</button>
                    </div>
                    <div class="fr-modal__content">
                        <h2 id="modal-6160-title" class="fr-modal__title">
                            <span class="fr-icon-arrow-right-line fr-icon--lg" aria-hidden="true"></span>
                            Titre de la modale
                        </h2>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</dialog>
```

### Modale avec plusieurs boutons liés

```html
<button aria-controls="modal-multi-button" data-fr-opened="false" type="button" class="fr-btn">Ouvrir la modale (bouton 1)</button>
<button aria-controls="modal-multi-button" data-fr-opened="false" type="button" class="fr-btn">Ouvrir la modale (bouton 2)</button>
<dialog id="modal-multi-button" class="fr-modal" aria-labelledby="modal-multi-button-title">
    <div class="fr-container fr-container--fluid fr-container-md">
        <div class="fr-grid-row fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
                <div class="fr-modal__body">
                    <div class="fr-modal__header">
                        <button aria-controls="modal-multi-button" title="Fermer" type="button" id="button-6164" class="fr-btn--close fr-btn">Fermer</button>
                    </div>
                    <div class="fr-modal__content">
                        <h2 id="modal-multi-button-title" class="fr-modal__title">
                            <span class="fr-icon-arrow-right-line fr-icon--lg" aria-hidden="true"></span>
                            Titre de la modale
                        </h2>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</dialog>
```
