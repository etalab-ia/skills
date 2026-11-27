# Auditer une page DSFR

## 1. Vérification automatique

Sur le HTML rendu (page statique, ou source enregistrée depuis le navigateur pour un template ou une SPA) :

```bash
node <dossier du skill>/scripts/verifier.mjs page.html
```

Le script, sans dépendance, signale :

- erreurs : `id` en double, `aria-controls` / `aria-labelledby` / `aria-describedby` / `for` sans cible, lien d'évitement sans cible, champ sans label, `<img>` sans `alt`, modale sans titre lié, champ en erreur sans message, pictogramme `<use>` chargé depuis un CDN, CDN sans version, `<html>` sans `lang` ;
- avertissements : classe `fr-*` absente du CSS DSFR 1.15.4, icônes ou composants interactifs sans CSS utilitaire ou JS du DSFR visibles (ils peuvent être dans un bundle), icône vide sans `aria-hidden`, lien `target="_blank"` sans mention « nouvelle fenêtre », `<use>` vers une URL absolue (bloqué si ce n'est pas l'origine de la page), plusieurs boutons primaires dans un groupe, CDN dans une autre version, et pour une page complète : nombre de `<h1>`, liens d'évitement, en-tête, `<main>` et pied de page manquants, `data-fr-theme` écrit à la main.

Sur un projet dont le DSFR installé n'est pas en 1.15.4, un écart avec ce skill (classe inconnue, balisage différent, composant déprécié) est d'abord un écart de version : le signaler comme tel, avec la montée de version comme correction, pas comme une faute d'intégration.

Sur un fragment, les références vers des `id` hors du fragment ressortent en erreur : les ignorer. Une classe inconnue peut être un simple point d'accroche JS : vérifier dans le `code.md` du composant avant de la déclarer inventée.

## 2. Vérification manuelle

Pour chaque composant de la page, comparer son balisage à `composants/<nom>/exemples.md` et relire les règles de `index.md` (quand l'utiliser) et `accessibilite.md` (clavier, ARIA). Points que le script ne voit pas :

- hiérarchie des titres sans saut de niveau, titres de composants (accordéon, carte, modale) au bon niveau dans la page ;
- libellés : boutons et liens explicites hors contexte, pas de « cliquez ici », textes d'aide et messages d'erreur qui disent comment corriger ;
- formulaires : groupes de champs liés dans `fr-fieldset` avec `<legend>`, champs obligatoires signalés, `autocomplete` sur les données personnelles (voir [modeles/blocs](modeles/blocs/)) ;
- couleurs : uniquement les tokens et classes utilitaires ([fondamentaux/color](fondamentaux/color/index.md)), contraste vérifié pour toute personnalisation (4,5:1 pour le texte) ;
- rendu en thème sombre (`data-fr-scheme`) et en mobile (grille, menu de l'en-tête) ;
- composants marqués *(sans code)* dans `SKILL.md` : ne doivent pas apparaître avec des classes inventées ;
- pied de page : liens obligatoires et mention réelle de conformité d'accessibilité.

## 3. Restitution

Lister les problèmes du plus grave au moins grave, chacun avec l'emplacement (`fichier:ligne`), la règle enfreinte et le fichier du skill qui la documente, puis la correction en HTML. Distinguer ce qui est vérifié de ce qui est supposé.
