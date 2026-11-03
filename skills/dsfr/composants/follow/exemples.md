# Lettre d'information et réseaux sociaux : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Réseaux sociaux seuls

Les icones réseaux sociaux disponibles pour ce composant sont définies dans :

```scss
////
/// Logo Setting
/// @group logo
////

$follow-icons: (
  bluesky: bluesky-fill,
  dailymotion: dailymotion-fill,
  facebook: facebook-circle-fill,
  github: github-fill,
  instagram: instagram-fill,
  linkedin: linkedin-box-fill,
  mastodon: mastodon-fill,
  snapchat: snapchat-fill,
  telegram: telegram-fill,
  threads: threads-fill,
  tiktok: tiktok-fill,
  twitch: twitch-fill,
  twitter: twitter-fill,
  twitter-x: twitter-x-fill,
  vimeo: vimeo-fill,
  youtube: youtube-fill,
);
```

### Suivez-nous sur les réseaux sociaux

Il est aussi possible d'appliquer une classe utilitaire sur un bouton pour utiliser une icone du dsfr (ex: "fr-icon-rss-line")

```html
<div class="fr-follow" id="follow-4088">
    <div class="fr-container">
        <div class="fr-grid-row">
            <div class="fr-col-12">
                <div class="fr-follow__social">
                    <h2 class="fr-h5">Suivez-nous
                        <br> sur les réseaux sociaux
                    </h2>
                    <ul class="fr-btns-group">
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4089" href="[À MODIFIER - Lien vers le facebook de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--facebook fr-btn">Facebook</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4090" href="[À MODIFIER - Lien vers le twitter de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--twitter-x fr-btn">X (anciennement Twitter)</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4091" href="[À MODIFIER - Lien vers le bluesky de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--bluesky fr-btn">Bluesky</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4092" href="[À MODIFIER - Lien vers le linkedin de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--linkedin fr-btn">Linkedin</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4093" href="[À MODIFIER - Lien vers l'instagram de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--instagram fr-btn">Instagram</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4094" href="[À MODIFIER - Lien vers le youtube de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--youtube fr-btn">Youtube</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
```

### Lettre d'info seule

```html
<div class="fr-follow" id="follow-4099">
    <div class="fr-container">
        <div class="fr-grid-row">
            <div class="fr-col-12">
                <div class="fr-follow__newsletter">
                    <div>
                        <h2 class="fr-h5">Abonnez-vous à notre lettre d’information</h2>
                        <p class="fr-text--sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.</p>
                    </div>
                    <div>
                        <ul class="fr-btns-group fr-btns-group--inline-md">
                            <li>
                                <button title="S‘abonner à notre lettre d’information" type="button" id="newsletter-button-4098" class="fr-btn">S'abonner</button>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

### Lettre d'info seule avec formulaire

```html
<div class="fr-follow" id="follow-4107">
    <div class="fr-container">
        <div class="fr-grid-row">
            <div class="fr-col-12">
                <div class="fr-follow__newsletter">
                    <div>
                        <h2 class="fr-h5">Abonnez-vous à notre lettre d’information</h2>
                        <p class="fr-text--sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.</p>
                    </div>
                    <div>
                        <form action="">
                            <div class="fr-input-group" id="input-group-4108">
                                <label class="fr-label" for="newsletter-email-4105">
                                    Votre adresse électronique (ex. : nom@example.com)
                                </label>
                                <div class="fr-input-wrap fr-input-wrap--addon">
                                    <input class="fr-input" title="Votre adresse électronique (ex. : nom@example.com)" autocomplete="email" attributes="[object Object]" aria-describedby="newsletter-email-4105-hint-text newsletter-email-4105-messages" placeholder="Votre adresse électronique (ex. : nom@example.com)" id="newsletter-email-4105" type="email">
                                    <button title="S‘abonner à notre lettre d’information" type="submit" id="newsletter-button-4106" class="fr-btn">S'abonner</button>
                                </div>
                                <div class="fr-messages-group" id="newsletter-email-4105-messages" aria-live="polite">
                                </div>
                            </div>
                            <p id="newsletter-email-4105-hint-text" class="fr-hint-text">En renseignant votre adresse électronique, vous acceptez de recevoir nos actualités par courriel. Vous pouvez vous désinscrire à tout moment à l’aide des liens de désinscription ou en nous contactant.</p>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

### Réseaux sociaux et Lettre d'info mise en avant

```html
<div class="fr-follow" id="follow-4119">
    <div class="fr-container">
        <div class="fr-grid-row">
            <div class="fr-col-12 fr-col-md-8">
                <div class="fr-follow__newsletter">
                    <div>
                        <h2 class="fr-h5">Abonnez-vous à notre lettre d’information</h2>
                        <p class="fr-text--sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.</p>
                    </div>
                    <div>
                        <ul class="fr-btns-group fr-btns-group--inline-md">
                            <li>
                                <button title="S‘abonner à notre lettre d’information" type="button" id="newsletter-button-4118" class="fr-btn">S'abonner</button>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="fr-col-12 fr-col-md-4">
                <div class="fr-follow__social">
                    <h2 class="fr-h5">Suivez-nous
                        <br> sur les réseaux sociaux
                    </h2>
                    <ul class="fr-btns-group">
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4120" href="[À MODIFIER - Lien vers le facebook de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--facebook fr-btn">Facebook</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4121" href="[À MODIFIER - Lien vers le twitter de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--twitter-x fr-btn">X (anciennement Twitter)</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4122" href="[À MODIFIER - Lien vers le bluesky de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--bluesky fr-btn">Bluesky</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4123" href="[À MODIFIER - Lien vers le linkedin de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--linkedin fr-btn">Linkedin</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4124" href="[À MODIFIER - Lien vers l'instagram de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--instagram fr-btn">Instagram</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4125" href="[À MODIFIER - Lien vers le youtube de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--youtube fr-btn">Youtube</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
```

### Réseaux sociaux et Lettre d'info avec formulaire

Extrait complet : [exemples/reseaux-sociaux-et-lettre-d-info-avec-formulaire-1.html](exemples/reseaux-sociaux-et-lettre-d-info-avec-formulaire-1.html) (4 ko)

### Réseaux sociaux et Lettre d'info avec formulaire - succès

```html
<div class="fr-follow" id="follow-4157">
    <div class="fr-container">
        <div class="fr-grid-row">
            <div class="fr-col-12 fr-col-md-8">
                <div class="fr-follow__newsletter">
                    <div>
                        <h2 class="fr-h5">Abonnez-vous à notre lettre d’information</h2>
                        <p class="fr-text--sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.</p>
                    </div>
                    <div>
                        <div id="newsletter-alert-4156" class="fr-alert fr-alert--success">
                            <p>Votre inscription a bien été prise en compte.</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="fr-col-12 fr-col-md-4">
                <div class="fr-follow__social">
                    <h2 class="fr-h5">Suivez-nous
                        <br> sur les réseaux sociaux
                    </h2>
                    <ul class="fr-btns-group">
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4158" href="[À MODIFIER - Lien vers le facebook de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--facebook fr-btn">Facebook</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4159" href="[À MODIFIER - Lien vers le twitter de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--twitter-x fr-btn">X (anciennement Twitter)</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4160" href="[À MODIFIER - Lien vers le bluesky de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--bluesky fr-btn">Bluesky</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4161" href="[À MODIFIER - Lien vers le linkedin de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--linkedin fr-btn">Linkedin</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4162" href="[À MODIFIER - Lien vers l'instagram de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--instagram fr-btn">Instagram</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4163" href="[À MODIFIER - Lien vers le youtube de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--youtube fr-btn">Youtube</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
```

### Réseaux sociaux et Lettre d'info avec formulaire - erreur

Extrait complet : [exemples/reseaux-sociaux-et-lettre-d-info-avec-formulaire-e-2.html](exemples/reseaux-sociaux-et-lettre-d-info-avec-formulaire-e-2.html) (5 ko)

## Dépréciation

### Réseaux sociaux seuls

Les exemples suivants sont dépréciés, ne pas utiliser comme référence Pour support des versions précédentes

```html
<div class="fr-follow">
    <div class="fr-container">
        <div class="fr-grid-row">
            <div class="fr-col-12">
                <div class="fr-follow__social">
                    <p class="fr-h5">Suivez-nous
                        <br> sur les réseaux sociaux
                    </p>
                    <ul class="fr-links-group">
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4191" href="[À MODIFIER - Lien vers le facebook de l'organisation]" target="_blank" rel="noopener external" class="fr-link--facebook fr-link">facebook</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4192" href="[À MODIFIER - Lien vers le twitter de l'organisation]" target="_blank" rel="noopener external" class="fr-link--twitter-x fr-link">twitter-x</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4193" href="[À MODIFIER - Lien vers l'instagram de l'organisation]" target="_blank" rel="noopener external" class="fr-link--instagram fr-link">instagram</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4194" href="[À MODIFIER - Lien vers le linkedin de l'organisation]" target="_blank" rel="noopener external" class="fr-link--linkedin fr-link">linkedin</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4195" href="[À MODIFIER - Lien vers le youtube de l'organisation]" target="_blank" rel="noopener external" class="fr-link--youtube fr-link">youtube</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
```

### Réseaux sociaux et Lettre d'info mise en avant

```html
<div class="fr-follow">
    <div class="fr-container">
        <div class="fr-grid-row">
            <div class="fr-col-12 fr-col-md-8">
                <div class="fr-follow__newsletter">
                    <div>
                        <p class="fr-h5">Abonnez-vous à notre lettre d’information</p>
                        <p class="fr-text--sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.</p>
                    </div>
                    <div>
                        <button title="S‘abonner à notre lettre d’information" type="button" class="fr-btn">S'abonner</button>
                    </div>
                </div>
            </div>
            <div class="fr-col-12 fr-col-md-4">
                <div class="fr-follow__social">
                    <p class="fr-h5">Suivez-nous
                        <br> sur les réseaux sociaux
                    </p>
                    <ul class="fr-links-group">
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4202" href="[À MODIFIER - Lien vers le facebook de l'organisation]" target="_blank" rel="noopener external" class="fr-link--facebook fr-link">facebook</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4203" href="[À MODIFIER - Lien vers le twitter de l'organisation]" target="_blank" rel="noopener external" class="fr-link--twitter-x fr-link">twitter-x</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4204" href="[À MODIFIER - Lien vers l'instagram de l'organisation]" target="_blank" rel="noopener external" class="fr-link--instagram fr-link">instagram</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4205" href="[À MODIFIER - Lien vers le linkedin de l'organisation]" target="_blank" rel="noopener external" class="fr-link--linkedin fr-link">linkedin</a>
                        </li>
                        <li>
                            <a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4206" href="[À MODIFIER - Lien vers le youtube de l'organisation]" target="_blank" rel="noopener external" class="fr-link--youtube fr-link">youtube</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
```
