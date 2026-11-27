# Transcription : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Transcription avec zone d’action

```html
<div class="fr-transcription" id="transcription-7512">
    <button type="button" class="fr-transcription__btn" aria-expanded="false" aria-controls="fr-transcription-collapse-transcription-7512">Transcription</button>
    <div class="fr-collapse" id="fr-transcription-collapse-transcription-7512">
        <div class="fr-transcription__footer">
            <div class="fr-transcription__actions-group">
                <button aria-controls="fr-transcription-modal-transcription-7512" aria-label="Agrandir la transcription" data-fr-opened="false" type="button" class="fr-btn--fullscreen fr-btn">Agrandir</button>
            </div>
        </div>
        <div id="fr-transcription-modal-transcription-7512" class="fr-modal" aria-labelledby="fr-transcription-modal-transcription-7512-title">
            <div class="fr-container fr-container--fluid fr-container-md">
                <div class="fr-grid-row fr-grid-row--center">
                    <div class="fr-col-12 fr-col-md-10 fr-col-lg-8">
                        <div class="fr-modal__body">
                            <div class="fr-modal__header">
                                <button aria-controls="fr-transcription-modal-transcription-7512" title="Fermer" type="button" id="button-7514" class="fr-btn--close fr-btn">Fermer</button>
                            </div>
                            <div class="fr-modal__content">
                                <h2 id="fr-transcription-modal-transcription-7512-title" class="fr-modal__title">
                                    Titre de la transcription
                                </h2>
                                <!-- données de test -->
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```
