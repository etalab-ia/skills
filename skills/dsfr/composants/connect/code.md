# Boutons FranceConnect et ProConnect : Code

## HTML

### Structure du composant

Les composants **Bouton FranceConnect et ProConnect** permettent de proposer une connexion en utilisant l’identité numérique d’un fournisseur agréé. Leur structure est la suivante :

- Un élément `<div>` de classe `fr-connect-group` contient le bouton FranceConnect ou ProConnect et un lien d'information.
  - Le bouton FranceConnect ou ProConnect est un élément HTML `<button>` défini par la classe `fr-connect`. Il doit contenir deux éléments `<span>` :
    - Un texte de connexion "S'identifier avec", un `<span>` avec la classe `fr-connect__login`. Ce texte peut être traduit mais ne doit pas être modifié.
    - L'intitulé du service "FranceConnect" ou "ProConnect", un `<span>` avec la classe `fr-connect__brand`.
  - Le bouton doit être accompagné d'un lien d'information. Il s'agit d'un élément `<p>` contenant un lien `<a>` vers le service dédié.
    - Le lien doit être ouvert dans une nouvelle fenêtre.
    - L'intitulé du lien peut être traduit mais ne doit pas être modifié.

Pour plus de clarté, le bouton FranceConnect peut être accompagné de la phrase :
« FranceConnect est la solution proposée par l’État pour sécuriser et simplifier la connexion à vos services en ligne ».

**Structure HTML du bouton FranceConnect**

```html
<div class="fr-connect-group">
    <button class="fr-connect" type="button">
        <span class="fr-connect__login">S’identifier avec</span>
        <span class="fr-connect__brand">FranceConnect</span>
    </button>
    <p>
        <a href="https://franceconnect.gouv.fr/" target="_blank" rel="noopener" title="Qu’est-ce que FranceConnect ? - nouvelle fenêtre">Qu’est-ce que FranceConnect ?</a>
    </p>
</div>
```

**Structure HTML du bouton FranceConnect+**

```html
<div class="fr-connect-group">
    <button class="fr-connect fr-connect--plus" type="button">
        <span class="fr-connect__login">S’identifier avec</span>
        <span class="fr-connect__brand">FranceConnect</span>
    </button>
    <p>
        <a href="https://franceconnect.gouv.fr/france-connect-plus" target="_blank" rel="noopener" title="Qu’est-ce que FranceConnect+ ? - nouvelle fenêtre">Qu’est-ce que FranceConnect+ ?</a>
    </p>
</div>
```

**Structure HTML du bouton ProConnect**

```html
<div class="fr-connect-group">
    <button class="fr-connect fr-connect--pro" type="button">
        <span class="fr-connect__login">S’identifier avec</span>
        <span class="fr-connect__brand">ProConnect</span>
    </button>
    <p>
        <a href="https://proconnect.gouv.fr/" target="_blank" rel="noopener" title="Qu’est-ce que ProConnect ? - nouvelle fenêtre">Qu’est-ce que ProConnect ?</a>
    </p>
</div>
```

---

## CSS

### Installation du CSS

Pour fonctionner correctement le style CSS du composant et de ses dépendances doivent être importés. L'import doit se faire avant le contenu de la page dans la partie `<head>`, et de préférence avec les fichiers minifiés, car plus légers.

Il est possible d'importer les fichiers CSS avec un niveau de granularité adapté à vos besoins. Voir le découpage des fichiers CSS du DSFR dans la [documentation dédiée](../../demarrage.md).

**Dépendances CSS**

| Dépendance | Obligatoire |
|------------|-------------|
| Core       | Oui         |
| Connect    | Oui         |

**Exemple d'imports CSS**

```html
<link href="dist/core/core.min.css" rel="stylesheet">
<link href="dist/component/connect/connect.min.css" rel="stylesheet">
```

Une version <span lang="en">**standalone**</span> du bouton FranceConnect est également disponible, permettant de l'utiliser **en dehors du DSFR**.
Ce fichier CSS comprend le minimum requis du core du DSFR et le style du bouton FranceConnect.

```html
<link href="standalone/component/connect/connect.standalone.min.css" rel="stylesheet">
```

### Variantes de style

Le composant Bouton FranceConnect ou ProConnect est stylisé par les classes CSS suivantes :

- `.fr-connect-group` : Conteneur du bouton et du lien d'information.
- `.fr-connect` : Bouton FranceConnect ou ProConnect.
- `.fr-connect__login` : Texte "S'identifier avec".
- `.fr-connect__brand` : Intitulé du service
- `.fr-connect-group p` : Conteneur du lien d'information.
- `.fr-connect-group a` : Lien d'information.

Une classe supplémentaire peut être ajoutée au bouton pour proposer une connexion via un autre service :
- `.fr-connect--plus` : FranceConnect+.
- `.fr-connect--pro` : ProConnect.

---

## JavaScript

La documentation technique pour la mise en place du service souhaité peut être consultée sur leur site dédié :
- [FranceConnect](https://partenaires.franceconnect.gouv.fr/fcp/fournisseur-service)
- [ProConnect](https://partenaires.proconnect.gouv.fr/)

---

## Note de version

[Voir les évolutions sur github](https://github.com/GouvernementFR/dsfr/pulls?q=is%3Apr+is%3Aclosed+is%3Amerged+connect+)
