# Page de connexion : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

## Variante 1-default

Extrait complet : [exemples/1-default-titre-editorialise-1.html](exemples/1-default-titre-editorialise-1.html) (8 ko)

## Variante 2-error

Extrait complet : [exemples/2-error-titre-editorialise-2.html](exemples/2-error-titre-editorialise-2.html) (9 ko)

## Variante 3a-form

```html
<main role="main" id="content">
    <div class="fr-container fr-mt-8v fr-mt-md-14v fr-mb-2v fr-mb-md-8v">
        <div class="fr-grid-row fr-grid-row--gutters fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-10 fr-col-lg-8">
                <h1 class="fr-h2">Récupération de mot de passe sur [Nom du service-site]</h1>
                <p class="fr-text--lead">Chapô — Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.</p>
            </div>
        </div>
    </div>
    <div class="fr-container fr-container--fluid fr-mb-md-14v">
        <div class="fr-grid-row fr-grid-row--gutters fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-10 fr-col-lg-8">
                <div class="fr-container fr-background-alt--grey fr-px-md-0 fr-pt-10v fr-pt-md-14v fr-pb-6v fr-pb-md-10v">
                    <div class="fr-grid-row fr-grid-row--gutters fr-grid-row--center">
                        <div class="fr-col-12 fr-col-md-10 fr-col-lg-9">
                            <div>
                                <form class="fr-mb-0 fr-fieldset" id="recover">
                                    <fieldset class="fr-mb-0 fr-fieldset fr-fieldset" id="recover-fieldset" aria-labelledby="recover-fieldset-legend recover-fieldset-messages">
                                        <legend class="fr-fieldset__legend" id="recover-fieldset-legend">
                                            <h2 class="fr-h5">Récupérer le mot de passe de votre compte</h2>
                                        </legend>
                                        <div class="fr-fieldset__element">
                                            <p class="fr-text--sm">Description — Veuillez saisir l’adresse électronique associée à votre compte. Nous vous enverrons plus d’informations sur pour réinitialiser votre mot de passe</p>
                                        </div>
                                        <div class="fr-fieldset__element">
                                            <div class="fr-input-group" id="input-group-8529">
                                                <label class="fr-label" for="username-8527">
                                                    Identifiant
                                                    <span class="fr-hint-text">Format attendu : nom@example.com</span>
                                                </label>
                                                <input class="fr-input" aria-describedby="username-8527-messages" name="username" id="username-8527" type="text">
                                                <div class="fr-messages-group" id="username-8527-messages" aria-live="polite">
                                                </div>
                                            </div>
                                        </div>
                                        <div class="fr-fieldset__element">
                                            <ul class="fr-btns-group--right fr-mt-2v fr-btns-group fr-btns-group--inline fr-btns-group fr-btns-group--inline">
                                                <li>
                                                    <button type="submit" class="fr-btn">Valider</button>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="fr-messages-group" id="recover-fieldset-messages" aria-live="polite">
                                        </div>
                                    </fieldset>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</main>
```

## Variante 3b-confirmation

```html
<main role="main" id="content">
    <div class="fr-container fr-mt-8v fr-mt-md-14v fr-mb-2v fr-mb-md-8v">
        <div class="fr-grid-row fr-grid-row--gutters fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-10 fr-col-lg-8">
                <h1 class="fr-h2">Récupération de mot de passe sur [Nom du service-site]</h1>
                <p class="fr-text--lead">Chapô — Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.</p>
            </div>
        </div>
    </div>
    <div class="fr-container fr-container--fluid fr-mb-md-14v">
        <div class="fr-grid-row fr-grid-row--gutters fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-10 fr-col-lg-8">
                <div class="fr-container fr-background-alt--grey fr-px-md-0 fr-pt-10v fr-pt-md-14v fr-pb-6v fr-pb-md-10v">
                    <div class="fr-grid-row fr-grid-row--gutters fr-grid-row--center">
                        <div class="fr-col-12 fr-col-md-10 fr-col-lg-9">
                            <div>
                                <div id="alert-8699" class="fr-mb-6v fr-alert fr-alert--success fr-alert--sm">
                                    <p>Votre demande de récupération de mot de passe a été transmise. Vous recevrez un courriel dans quelques instants.</p>
                                </div>
                                <p class="fr-hint-text">Détail — Si vous n’avez pas reçu de courriel (n’hésitez pas à vérifier dans les indérisables), vous pouvez re saisir votre adresse électronique.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</main>
```
