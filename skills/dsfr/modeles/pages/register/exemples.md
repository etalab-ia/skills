# Page de création de compte : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

## Variante 1-single

Extrait complet : [exemples/1-single-titre-editorialise-1.html](exemples/1-single-titre-editorialise-1.html) (9 ko)

## Variante 2a-login

Extrait complet : [exemples/2a-login-titre-editorialise-2.html](exemples/2a-login-titre-editorialise-2.html) (10 ko)

## Variante 2b-identity

Extrait complet : [exemples/2b-identity-titre-editorialise-3.html](exemples/2b-identity-titre-editorialise-3.html) (10 ko)

## Variante 2c-address

Extrait complet : [exemples/2c-address-titre-editorialise-4.html](exemples/2c-address-titre-editorialise-4.html) (9 ko)

## Variante 3a-create

```html
<main role="main" id="content">
    <div class="fr-container fr-mt-8v fr-mt-md-14v fr-mb-2v fr-mb-md-8v">
        <div class="fr-grid-row fr-grid-row--gutters fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-10 fr-col-lg-8">
                <h1 class="fr-h2">Création de compte sur [Nom de service-site]</h1>
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
                                <div id="alert-9594" class="fr-mb-6v fr-alert fr-alert--success fr-alert--sm">
                                    <p>Votre compte a bien été créé. Vous recevrez un courriel dans quelques instants contenant un lien de confirmation.</p>
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

## Variante 3b-activate

```html
<main role="main" id="content">
    <div class="fr-container fr-mt-8v fr-mt-md-14v fr-mb-2v fr-mb-md-8v">
        <div class="fr-grid-row fr-grid-row--gutters fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-10 fr-col-lg-8">
                <h1 class="fr-h2">Création de compte sur [Nom de service-site]</h1>
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
                                <div id="alert-9764" class="fr-mb-6v fr-alert fr-alert--success fr-alert--sm">
                                    <p>Votre compte a bien été activé. Vous pouvez dès maintenant commencer à l’utiliser.</p>
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
