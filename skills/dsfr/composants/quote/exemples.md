# Citation : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Citation par défaut (texte taille xl)

« Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut. »

```html
<figure class="fr-quote">
    <blockquote cite="[À MODIFIER - https://lien-vers-la-source.fr]">
        <p>«&nbsp;Lorem [...] elit ut.&nbsp;»</p>
    </blockquote>
    <figcaption>
        <p class="fr-quote__author">Auteur</p>
        <ul class="fr-quote__source">
            <li>
                <cite>Ouvrage</cite>
            </li>
            <li>Détail 1</li>
            <li>Détail 2</li>
            <li>Détail 3</li>
            <li>
                <a target="_blank" rel="noopener external" title="Détail 4 - nouvelle fenêtre" href="[À MODIFIER - Lien vers la sources ou des infos complémentaires]">Détail 4</a>
            </li>
        </ul>
    </figcaption>
</figure>
```

### Citation taille lg

```html
<figure class="fr-quote">
    <blockquote cite="[À MODIFIER - https://lien-vers-la-source.fr]">
        <p class="fr-text--lg">«&nbsp;Lorem [...] elit ut.&nbsp;»</p>
    </blockquote>
    <figcaption>
        <p class="fr-quote__author">Auteur</p>
        <div class="fr-quote__source">
            <a target="_blank" href="[À MODIFIER - Lien vers la sources ou des infos complémentaires]">Un seul détail</a>
        </div>
    </figcaption>
</figure>
```

### Citation avec image

« Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut. »

```html
<figure class="fr-quote fr-quote--column">
    <blockquote cite="[À MODIFIER - https://lien-vers-la-source.fr]">
        <p>«&nbsp;Lorem [...] elit ut.&nbsp;»</p>
    </blockquote>
    <figcaption>
        <p class="fr-quote__author">Auteur</p>
        <ul class="fr-quote__source">
            <li>
                <cite>Ouvrage</cite>
            </li>
            <li>Détail 1</li>
            <li>Détail 2</li>
            <li>Détail 3</li>
            <li>
                <a href="">Détail 4</a>
            </li>
        </ul>
        <div class="fr-quote__image">
            <img class="fr-responsive-img" src="../../../example/img/placeholder.1x1.png" alt="" />
            <!-- L’alternative de l’image (attribut alt) doit rester vide car l’image est illustrative et ne doit pas être restituée aux technologies d’assistance -->
        </div>
    </figcaption>
</figure>
```

### Citation accentuée

« Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut. »

```html
<figure class="fr-quote fr-quote--green-emeraude">
    <blockquote cite="[À MODIFIER - https://lien-vers-la-source.fr]">
        <p>«&nbsp;Lorem [...] elit ut.&nbsp;»</p>
    </blockquote>
    <figcaption>
        <p class="fr-quote__author">Auteur</p>
        <ul class="fr-quote__source">
            <li>
                <cite>Ouvrage</cite>
            </li>
            <li>Détail 1</li>
            <li>Détail 2</li>
            <li>Détail 3</li>
            <li>
                <a target="_blank" rel="noopener external" title="Détail 4 - nouvelle fenêtre" href="[À MODIFIER - Lien vers la sources ou des infos complémentaires]">Détail 4</a>
            </li>
        </ul>
    </figcaption>
</figure>
```
