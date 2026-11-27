# Pied de page : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Pied de page minimal

```html
<footer class="fr-footer" role="contentinfo" id="footer-7027">
    <div class="fr-container">
        <div class="fr-footer__body">
            <div class="fr-footer__brand fr-enlarge-link">
                <a id="footer-brand-link-7028" title="Retour à l’accueil du site - Nom de l’entité (ministère, secrétariat d‘état, gouvernement)" href="/">
                    <p class="fr-logo">
                        Intitulé
                        <br>officiel
                    </p>
                </a>
            </div>
            <div class="fr-footer__content">
                <p class="fr-footer__content-desc">Lorem [...] elit ut.</p>
                <ul class="fr-footer__content-list">
                    <li class="fr-footer__content-item">
                        <a title="info.gouv.fr - nouvelle fenêtre" id="footer__content-link-7029" href="https://info.gouv.fr" target="_blank" rel="noopener external" class="fr-footer__content-link">info.gouv.fr</a>
                    </li>
                    <li class="fr-footer__content-item">
                        <a title="service-public.gouv.fr - nouvelle fenêtre" id="footer__content-link-7030" href="https://service-public.gouv.fr" target="_blank" rel="noopener external" class="fr-footer__content-link">service-public.gouv.fr</a>
                    </li>
                    <li class="fr-footer__content-item">
                        <a title="legifrance.gouv.fr - nouvelle fenêtre" id="footer__content-link-7031" href="https://legifrance.gouv.fr" target="_blank" rel="noopener external" class="fr-footer__content-link">legifrance.gouv.fr</a>
                    </li>
                    <li class="fr-footer__content-item">
                        <a title="data.gouv.fr - nouvelle fenêtre" id="footer__content-link-7032" href="https://data.gouv.fr" target="_blank" rel="noopener external" class="fr-footer__content-link">data.gouv.fr</a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="fr-footer__bottom">
            <ul class="fr-footer__bottom-list">
                <li class="fr-footer__bottom-item">
                    <a id="footer__bottom-link-7033" href="[url - à modifier]" class="fr-footer__bottom-link">Plan du site</a>
                </li>
                <li class="fr-footer__bottom-item">
                    <a id="footer__bottom-link-7034" href="[url - à modifier]" class="fr-footer__bottom-link">Accessibilité : non/partiellement/totalement conforme</a>
                </li>
                <li class="fr-footer__bottom-item">
                    <a id="footer__bottom-link-7035" href="[url - à modifier]" class="fr-footer__bottom-link">Mentions légales</a>
                </li>
                <li class="fr-footer__bottom-item">
                    <a id="footer__bottom-link-7036" href="[url - à modifier]" class="fr-footer__bottom-link">Données personnelles</a>
                </li>
                <li class="fr-footer__bottom-item">
                    <a id="footer__bottom-link-7037" href="[url - à modifier]" class="fr-footer__bottom-link">Gestion des cookies</a>
                </li>
            </ul>
            <div class="fr-footer__bottom-copy">
                <p>Sauf mention explicite de propriété intellectuelle détenue par des tiers, les contenus de ce site sont proposés sous <a href="https://github.com/etalab/licence-ouverte/blob/master/LO.md" target="_blank" rel="noopener external" title="Licence etalab - nouvelle fenêtre">licence etalab-2.0</a>
                </p>
            </div>
        </div>
    </div>
</footer>
```

### Pied de page avec navigation

Extrait complet : [exemples/pied-de-page-avec-navigation-1.html](exemples/pied-de-page-avec-navigation-1.html) (11 ko)

### Pied de page avec logo opérateur

```html
<footer class="fr-footer" role="contentinfo" id="footer-7073">
    <div class="fr-container">
        <div class="fr-footer__body">
            <div class="fr-footer__brand fr-enlarge-link">
                <p class="fr-logo">
                    République
                    <br>Française
                </p>
                <a id="footer-brand-link-7074" title="Retour à l’accueil du site - [À MODIFIER - texte alternatif de l’image : nom de l'opérateur ou du site serviciel] - République Française" href="/" class="fr-footer__brand-link">
                    <img class="fr-footer__logo" style="max-width:10rem;" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - texte alternatif de l’image]" />
                    <!-- L’alternative de l’image (attribut alt) doit impérativement être renseignée et reprendre le texte visible dans l’image -->
                </a>
            </div>
            <div class="fr-footer__content">
                <p class="fr-footer__content-desc">Lorem [...] elit ut.</p>
                <ul class="fr-footer__content-list">
                    <li class="fr-footer__content-item">
                        <a title="info.gouv.fr - nouvelle fenêtre" id="footer__content-link-7075" href="https://info.gouv.fr" target="_blank" rel="noopener external" class="fr-footer__content-link">info.gouv.fr</a>
                    </li>
                    <li class="fr-footer__content-item">
                        <a title="service-public.gouv.fr - nouvelle fenêtre" id="footer__content-link-7076" href="https://service-public.gouv.fr" target="_blank" rel="noopener external" class="fr-footer__content-link">service-public.gouv.fr</a>
                    </li>
                    <li class="fr-footer__content-item">
                        <a title="legifrance.gouv.fr - nouvelle fenêtre" id="footer__content-link-7077" href="https://legifrance.gouv.fr" target="_blank" rel="noopener external" class="fr-footer__content-link">legifrance.gouv.fr</a>
                    </li>
                    <li class="fr-footer__content-item">
                        <a title="data.gouv.fr - nouvelle fenêtre" id="footer__content-link-7078" href="https://data.gouv.fr" target="_blank" rel="noopener external" class="fr-footer__content-link">data.gouv.fr</a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="fr-footer__bottom">
            <ul class="fr-footer__bottom-list">
                <li class="fr-footer__bottom-item">
                    <a id="footer__bottom-link-7079" href="[url - à modifier]" class="fr-footer__bottom-link">Plan du site</a>
                </li>
                <li class="fr-footer__bottom-item">
                    <a id="footer__bottom-link-7080" href="[url - à modifier]" class="fr-footer__bottom-link">Accessibilité : non/partiellement/totalement conforme</a>
                </li>
                <li class="fr-footer__bottom-item">
                    <a id="footer__bottom-link-7081" href="[url - à modifier]" class="fr-footer__bottom-link">Mentions légales</a>
                </li>
                <li class="fr-footer__bottom-item">
                    <a id="footer__bottom-link-7082" href="[url - à modifier]" class="fr-footer__bottom-link">Données personnelles</a>
                </li>
                <li class="fr-footer__bottom-item">
                    <a id="footer__bottom-link-7083" href="[url - à modifier]" class="fr-footer__bottom-link">Gestion des cookies</a>
                </li>
            </ul>
            <div class="fr-footer__bottom-copy">
                <p>Sauf mention explicite de propriété intellectuelle détenue par des tiers, les contenus de ce site sont proposés sous <a href="https://github.com/etalab/licence-ouverte/blob/master/LO.md" target="_blank" rel="noopener external" title="Licence etalab - nouvelle fenêtre">licence etalab-2.0</a>
                </p>
            </div>
        </div>
    </div>
</footer>
```

### Pied de page avec logos partenaires

Extrait complet : [exemples/pied-de-page-avec-logos-partenaires-2.html](exemples/pied-de-page-avec-logos-partenaires-2.html) (6 ko)

### Pied de page avec logo partenaire primaire uniquement

Extrait complet : [exemples/pied-de-page-avec-logo-partenaire-primaire-uniquem-3.html](exemples/pied-de-page-avec-logo-partenaire-primaire-uniquem-3.html) (4 ko)

### Pied de page avec logos partenaires secondaires uniquement

Extrait complet : [exemples/pied-de-page-avec-logos-partenaires-secondaires-un-4.html](exemples/pied-de-page-avec-logos-partenaires-secondaires-un-4.html) (5 ko)

### Pied de page complet

Extrait complet : [exemples/pied-de-page-complet-5.html](exemples/pied-de-page-complet-5.html) (14 ko)
