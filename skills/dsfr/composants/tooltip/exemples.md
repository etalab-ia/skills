# Infobulle : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Information contextuelle

```html
<a aria-describedby="tooltip-3838" id="link-3839" href="#" class="fr-link">Exemple</a>
<span class="fr-tooltip fr-placement" id="tooltip-3838" role="tooltip">Lorem [...] elit ut.</span>
```

### Infobulle

```html
<button aria-describedby="tooltip-3842" type="button" class="fr-btn--tooltip fr-btn">Information contextuelle</button>
<span class="fr-tooltip fr-placement" id="tooltip-3842" role="tooltip">Lorem [...] elit ut.</span>
```

### Information contextuelle dans une grille à gauche

```html
<div class="fr-grid-row fr-grid-row--gutters">
    <div class="fr-col-4 fr-col-sm-2">
        <a class="fr-link" href="#" aria-describedby="tooltip-3845">Exemple</a>
        <span class="fr-tooltip fr-placement" id="tooltip-3845" role="tooltip">Lorem [...] elit ut.</span>
    </div>
    <div class="fr-col-8 fr-col-sm-10">
        <p>Lorem [...] elit ut.</p>
    </div>
</div>
```

### Information contextuelle dans une grille à droite

```html
<div class="fr-grid-row fr-grid-row--gutters">
    <div class="fr-col-8 fr-col-sm-10">
        <p>Lorem [...] elit ut.</p>
    </div>
    <div class="fr-col-4 fr-col-sm-2">
        <a class="fr-link" href="#" aria-describedby="tooltip-3848">Exemple</a>
        <span class="fr-tooltip fr-placement" id="tooltip-3848" role="tooltip">Lorem [...] elit ut.</span>
    </div>
</div>
```

### Information contextuelle dans une liste

```html
<div class="fr-share" id="share-3859">
    <p class="fr-share__title">Partager la page</p>
    <ul class="fr-btns-group">
        <li>
            <a onclick="window.open(this.href,'Partager sur Facebook','toolbar=no,location=yes,status=no,menubar=no,scrollbars=yes,resizable=yes,width=600,height=450'); event.preventDefault();" aria-describedby="tooltip-3858" id="share-3860" href="https://www.facebook.com/sharer.php?u=[À MODIFIER - url de la page]" target="_blank" rel="noopener external" class="fr-btn--facebook fr-btn">Partager sur Facebook</a>
            <span class="fr-tooltip fr-placement" id="tooltip-3858" role="tooltip">Lorem [...] elit ut.</span>
        </li>
        <li>
            <!-- Les paramètres de la reqûete doivent être URI-encodés (ex: encodeURIComponent() en js) -->
            <a onclick="window.open(this.href,'Partager sur X (anciennement Twitter)','toolbar=no,location=yes,status=no,menubar=no,scrollbars=yes,resizable=yes,width=600,height=420'); event.preventDefault();" id="share-3861" href="https://twitter.com/intent/tweet?url=[À MODIFIER - url de la page]&text=[À MODIFIER - titre ou texte descriptif de la page]&via=[À MODIFIER - via]&hashtags=[À MODIFIER - hashtags]" target="_blank" rel="noopener external" class="fr-btn--twitter-x fr-btn">Partager sur X (anciennement Twitter)</a>
        </li>
        <li>
            <!-- Les paramètres de la reqûete doivent être URI-encodés (ex: encodeURIComponent() en js) -->
            <a onclick="window.open(this.href,'Partager sur Bluesky','toolbar=no,location=yes,status=no,menubar=no,scrollbars=yes,resizable=yes,width=600,height=430'); event.preventDefault();" id="share-3862" href="https://bsky.app/intent/compose?text=[À MODIFIER - titre ou texte descriptif de la page]+[À MODIFIER - url de la page]" target="_blank" rel="noopener external" class="fr-btn--bluesky fr-btn">Partager sur Bluesky</a>
        </li>
        <li>
            <a onclick="window.open(this.href,'Partager sur LinkedIn','toolbar=no,location=yes,status=no,menubar=no,scrollbars=yes,resizable=yes,width=550,height=550'); event.preventDefault();" id="share-3863" href="https://www.linkedin.com/shareArticle?url=[À MODIFIER - url de la page]&title=[À MODIFIER - titre ou texte descriptif de la page]" target="_blank" rel="noopener external" class="fr-btn--linkedin fr-btn">Partager sur LinkedIn</a>
        </li>
        <li>
            <a id="share-3864" href="mailto:?subject=[À MODIFIER - objet du mail]&body=[À MODIFIER - titre ou texte descriptif de la page] [À MODIFIER - url de la page]" target="_blank" rel="noopener external" class="fr-btn--mail fr-btn">Partager par email</a>
        </li>
        <li>
            <button onclick="navigator.clipboard.writeText(window.location).then(function() {alert('Adresse copiée dans le presse papier.')});" type="button" id="share-3865" class="fr-btn--copy fr-btn">Copier dans le presse-papier</button>
        </li>
    </ul>
</div>
```

### Infobulle dans un tableau

```html
<div class="fr-table" id="tootltip-table-component">
    <div class="fr-table__wrapper">
        <div class="fr-table__container">
            <div class="fr-table__content">
                <table id="tootltip-table">
                    <thead>
                        <tr>
                            <th scope="col">
                                th0
                            </th>
                            <th scope="col">
                                th1
                            </th>
                            <th scope="col">
                                th2
                            </th>
                            <th scope="col">
                                th3
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr id="tootltip-table-row-key-1" data-row-key="1">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="tootltip-table-row-key-2" data-row-key="2">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                <button aria-describedby="tooltip-3868" type="button" class="fr-btn--tooltip fr-btn">Information contextuelle</button>
                                <span class="fr-tooltip fr-placement" id="tooltip-3868" role="tooltip">Lorem [...] elit ut.</span>
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="tootltip-table-row-key-3" data-row-key="3">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                        <tr id="tootltip-table-row-key-4" data-row-key="4">
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                            <td>
                                Lorem [...] elit ut.
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
```
