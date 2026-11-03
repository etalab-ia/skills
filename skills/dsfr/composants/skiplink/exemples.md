# Liens d'évitement : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Titre éditorialisé

Les liens d’évitement permettent aux utilisateurs naviguant au clavier, ou équipés de lecteurs d'écran, d’accéder plus rapidement à des zones précises de la page.

```html
<div class="fr-skiplinks">
    <nav role="navigation" aria-label="Accès rapide" class="fr-container">
        <ul class="fr-skiplinks__list">
            <li>
                <a class="fr-link" href="#content">Contenu</a>
            </li>
            <li>
                <a class="fr-link" href="#header-navigation">Menu</a>
            </li>
            <li>
                <a class="fr-link" href="#header-search">Recherche</a>
            </li>
            <li>
                <a class="fr-link" href="#footer">Pied de page</a>
            </li>
        </ul>
    </nav>
</div>
```
