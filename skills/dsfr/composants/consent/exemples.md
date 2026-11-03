# Gestionnaire de consentement : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Gestionnaire de consentement

```html
<div class="fr-consent-banner">
    <h2 class="fr-h6">À propos des cookies sur nomdusite.gouv.fr</h2>
    <div class="fr-consent-banner__content">
        <p class="fr-text--sm">Bienvenue ! Nous utilisons des cookies pour améliorer votre expérience et les services disponibles sur ce site. Pour en savoir plus, visitez la page <a href="">Données personnelles et cookies</a>. Vous pouvez, à tout moment, avoir le contrôle sur les cookies que vous souhaitez activer.</p>
    </div>
    <ul class="fr-consent-banner__buttons fr-btns-group fr-btns-group--right fr-btns-group--inline-reverse fr-btns-group--inline-sm">
        <li>
            <button title="Autoriser tous les cookies" type="button" class="fr-btn">Tout accepter</button>
        </li>
        <li>
            <button title="Refuser tous les cookies" type="button" class="fr-btn">Tout refuser</button>
        </li>
        <li>
            <button data-fr-opened="false" aria-controls="fr-consent-modal" title="Personnaliser les cookies" type="button" class="fr-btn fr-btn--secondary">Personnaliser</button>
        </li>
    </ul>
</div>
```

### Panneau de gestion des cookies

Extrait complet : [exemples/panneau-de-gestion-des-cookies-1.html](exemples/panneau-de-gestion-des-cookies-1.html) (20 ko)

### Placeholder cookies désactivés standard

```html
<div class="fr-consent-placeholder">
    <h4 class="fr-h6">**Nom du service** est désactivé</h4>
    <p>Autorisez le dépôt de cookies pour accéder à cette fonctionnalité.</p>
    <button title="Autorisez le dépôt de cookies pour accéder au service **Nom du service**" type="button" class="fr-btn">Autoriser</button>
</div>
```

### Placeholder dans un bloc vidéo responsive grande taille

```html
<figure role="group" class="fr-content-media fr-content-media--lg" id="media-3826">
    <div class="fr-responsive-vid">
        <div class="fr-consent-placeholder">
            <h4 class="fr-h6">**Nom du service** est désactivé</h4>
            <p>Autorisez le dépôt de cookies pour accèder à cette fonctionnalité.</p>
            <button type="button" class="fr-btn">Autoriser</button>
        </div>
    </div>
    <figcaption class="fr-content-media__caption">
        Description / Source
        <a id="link-3828" href="#" class="fr-link">Libellé lien</a>
    </figcaption>
</figure>
<div class="fr-transcription" id="transcription-3827">
    <button type="button" class="fr-transcription__btn" aria-expanded="false" aria-controls="fr-transcription-collapse-transcription-3827">Transcription</button>
    <div class="fr-collapse" id="fr-transcription-collapse-transcription-3827">
        <div class="fr-transcription__footer">
            <div class="fr-transcription__actions-group">
                <button aria-controls="fr-transcription-modal-transcription-3827" aria-label="Agrandir la transcription" data-fr-opened="false" type="button" class="fr-btn--fullscreen fr-btn">Agrandir</button>
            </div>
        </div>
        <div id="fr-transcription-modal-transcription-3827" class="fr-modal" aria-labelledby="fr-transcription-modal-transcription-3827-title">
            <div class="fr-container fr-container--fluid fr-container-md">
                <div class="fr-grid-row fr-grid-row--center">
                    <div class="fr-col-12 fr-col-md-10 fr-col-lg-8">
                        <div class="fr-modal__body">
                            <div class="fr-modal__header">
                                <button aria-controls="fr-transcription-modal-transcription-3827" title="Fermer" type="button" id="button-3830" class="fr-btn--close fr-btn">Fermer</button>
                            </div>
                            <div class="fr-modal__content">
                                <h2 id="fr-transcription-modal-transcription-3827-title" class="fr-modal__title">
                                    Titre de la transcription
                                </h2>
                                <!-- données de test -->
                                <div>
                                    <ul>
                                        <li>list item</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```
