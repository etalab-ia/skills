---
name: rgaa
description: >-
  Outil d'audit de conformité RGAA 4.1.2 pour sites web et composants HTML, React/JSX et Rails/ERB.
  Utiliser cette skill pour auditer la conformité RGAA d'un site ou d'un composant :
  quand l'utilisateur demande un audit d'accessibilité, un rapport de conformité RGAA,
  quand il veut savoir si son code/site respecte le RGAA, quand il mentionne "audit RGAA",
  "conformité RGAA", "non-conformités", "déclaration d'accessibilité", ou quand il partage
  du code HTML, React ou ERB pour vérification a posteriori.
---

# RGAA 4.1.2 — Outil d'audit de conformité

Référentiel d'accessibilité numérique français. 106 critères répartis en 13 thématiques. Basé sur WCAG 2.1 niveau AA.

Source : https://accessibilite.numerique.gouv.fr/

## Stack du code audité

Les critères et leurs tests sont communs à toutes les stacks ; seules les corrections changent. Avant l’analyse, déterminer la stack, sans poser de question :

1. **Extension du fichier audité** : `.erb` → Rails / ERB ; `.jsx`, `.tsx` → React / JSX ; `.html` → HTML.
2. **Code collé sans fichier** : d’après la syntaxe. `<%= … %>`, `<%# … %>` → Rails / ERB ; `className`, `htmlFor`, expressions `{…}` dans les attributs → React / JSX ; sinon HTML.
3. **En dernier recours, le projet** : `Gemfile` qui déclare `rails` → Rails / ERB ; `package.json` qui déclare `react` → React / JSX. Un `Gemfile` seul ne suffit pas : une application Rails peut avoir un front React.

Indiquer dans l’en-tête du rapport la stack retenue et ce qui l’a déterminée : la personne qui lit le rapport peut la corriger.

**Choisir la correction :**

- Quand le critère a des blocs « Correction — React / JSX » et « Correction — Rails / ERB » dans sa référence, reprendre le bloc de la stack retenue. Si le bloc manque pour ce critère, rédiger la correction dans la stack retenue.
- Quand la référence n’a qu’un exemple, sans bloc par stack : en React / JSX, le reprendre ; en Rails / ERB, le transposer (`className` → `class`, `htmlFor` → `for`, expressions JSX → ERB) et le signaler par « exemple transposé depuis React » ; en HTML ou pour une autre stack, en donner la version HTML.
- Ne jamais inventer de classe `fr-*` du DSFR : n’utiliser que celles déjà présentes dans les références ou dans le code audité.

## Workflow d’audit en trois phases

### Phase 1 — Analyse statique silencieuse

Lire le code et établir les verdicts sans poser de question :

1. Déterminer la stack (section précédente) et le mode page ou composant (ci-dessous).
2. Lire aussi les fichiers liés au code audité quand ils existent (script, styles, classe du composant) : ils portent souvent les comportements à vérifier.
3. Parcourir les thèmes à évaluer en consultant les fichiers de référence.
4. Attribuer à chaque critère un statut, en appliquant la règle de tri par impact :
   - **C** — Conforme : critère respecté
   - **NC** — Non conforme : critère violé (identifier l’élément et le problème)
   - **NA** — Non applicable : critère sans objet pour ce contenu (justifier)
   - **NT** — Non testé : le verdict dépend du rendu ou d’une aide technique et ne peut pas être établi à la lecture du code (contrastes non calculables, zoom 200 %, focus visible, restitution par un lecteur d’écran), ou d’une vérification hors du fragment audité (critère qui compare plusieurs pages, comme 11.3 en mode composant). Ne jamais conclure C par défaut sur ces points.

**Mode page ou composant :**

- **Page** : document complet (`<html>`, `<head>`), layout ou gabarit de route (`app/views/layouts/`, `pages/`, `app/**/page.tsx`, `index.html`).
- **Composant** : tout le reste (composant, partial, fragment de page).

En mode composant, les thèmes 8 (Éléments obligatoires) et 12 (Navigation) ne sont pas évalués : leurs 21 critères dépendent de la page complète. Les compter à part, en « non évalués — mode composant », jamais en NA. Indiquer le mode dans l’en-tête du rapport.

**Règle de tri par impact (avant tout verdict) :**

Le RGAA vérifie un défaut restitué à la personne qui consulte la page. Raisonner par impact, pas par récitation de règle :

1. **Avant de conclure NC** : nommer l’impact concret, c’est-à-dire le blocage et l’outil concerné (voir [references/impacts.md](references/impacts.md)). Sans impact réel (élément purement décoratif, règle sans objet dans ce cas), ce n’est pas une NC : classer C ou NA.
2. **Avant de conclure C** : avoir parcouru le critère et vérifié qu’aucun motif à risque n’est présent. L’absence de défaut visible ne suffit pas.
3. **Avant de conclure NA** : vérifier que le critère ne s’applique vraiment pas à ce contenu, pas seulement qu’aucun défaut n’a été trouvé.

**Critère officiel :** chaque NC renvoie au critère officiel, par un lien de la forme `https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.1`. Les « non-conformités types » des fichiers de référence sont des exemples : la règle reste le critère officiel et ses tests. Ne pas citer de numéro de test, les fichiers de référence n’en contiennent pas encore.

### Phase 2 — Vérifications en conditions réelles

Après l’analyse, poser en un seul message les vérifications que le code seul ne permet pas :

```
Avant de finaliser le rapport, quelques vérifications que le code seul ne permet pas :

🔴 Test au clavier effectué ? (Tab, Maj+Tab, Entrée, Échap sur les éléments interactifs)
🟠 Zoom à 200 % testé ? (aucun texte coupé, pas de défilement horizontal)
🔴 Focus visible sur tous les éléments interactifs ?
🟠 Contrastes vérifiés ? (seulement si les couleurs ne sont pas calculables depuis le code)
🔴 En mode page : le titre de la page est-il pertinent et spécifique ?
```

Chaque réponse confirme ou corrige les verdicts concernés : un critère NT passe en C ou NC. Sans réponse, il reste NT.

### Phase 3 — Format de sortie

Demander le format attendu, sauf s’il a déjà été précisé :

```
Audit terminé. Quel résultat souhaites-tu ?

1. Rapport complet enregistré dans audits/
2. Corrections directes dans les fichiers
3. Les deux
```

Sans réponse, ou en exécution non interactive (agent, script) : sauter les phases 2 et 3, laisser en NT les critères qui dépendent du rendu dans le navigateur, produire le rapport et l’exporter.

## Format du rapport de conformité

```markdown
## Audit RGAA 4.1.2 — Rapport de conformité

**Date :** JJ/MM/AAAA
**Périmètre audité :** [description du code / page / composant]
**Stack :** [HTML | React / JSX | Rails / ERB] (déduite de [l’extension du fichier | la syntaxe du code | le projet])
**Mode :** [page | composant]
**Résultat global :** X% conforme
(X critères applicables — X conformes, X non conformes, X non applicables ; X non testés et X non évalués en mode composant, exclus du taux)

---

### Tableau de synthèse

| Thème | C | NC | NA | NT |
|-------|---|----|----|----|
| 1. Images | | | | |
| 2. Cadres | | | | |
| 3. Couleurs | | | | |
| 4. Multimédia | | | | |
| 5. Tableaux | | | | |
| 6. Liens | | | | |
| 7. Scripts | | | | |
| 8. Éléments obligatoires | | | | |
| 9. Structuration | | | | |
| 10. Présentation | | | | |
| 11. Formulaires | | | | |
| 12. Navigation | | | | |
| 13. Consultation | | | | |
| **Total** | | | | |

En mode composant, les lignes 8 et 12 portent « non évalués — mode composant ».

---

### Non-conformités détectées

**[NC] {ID} — {Intitulé du critère}** ([critère officiel](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#{ID}))
- **Élément concerné :** `<code>` ou description de l’endroit dans la page
- **Problème :** description précise de la violation
- **Impact utilisateur :** mécanisme du blocage et outil concerné
- **Correction :** action concrète à mener, dans la stack retenue
- **Priorité :** 🔴 Bloquant / 🟠 Majeur / 🟡 Mineur

---

### Correction groupée _(si plusieurs NC portent sur le même extrait de code)_

**NC {ID1} + {ID2} — résolues en une modification**

Avant / après, dans la stack retenue.

---

### Critères conformes

{ID1}, {ID2}, {ID3}... (liste compacte)

### Critères non applicables

- **{ID}** — {justification courte}

### Critères non testés

- **{ID}** — {vérification à mener en conditions réelles}

### Limites du mode composant _(si applicable)_

Ces critères nécessitent la page complète pour être évalués, entre autres :
- 8.3 Langue par défaut de la page
- 8.5 Titre de la page
- 9.1 Hiérarchie de titres sur l’ensemble de la page (évaluée sur le fragment, à revérifier sur la page complète)
- 12.1 Systèmes de navigation
- 12.7 Lien d’évitement
```

**Impact utilisateur :** reprendre la ligne **Impact** du critère dans sa référence si elle correspond au défaut constaté. Sinon, décrire le mécanisme du blocage et l’outil concerné en s’appuyant sur [references/impacts.md](references/impacts.md), par exemple : « Pour une personne qui utilise un lecteur d’écran, le lien est restitué caractère par caractère : la destination est inintelligible. » Ne jamais désigner une catégorie de handicap.

## Export du rapport

Quand le rapport est demandé en phase 3, ou par défaut sans réponse :

1. Créer le dossier `audits/` à la racine du projet s'il n'existe pas
2. Écrire le rapport complet dans `audits/rgaa-AAAA-MM-JJ.md` (date du jour, format ISO)
3. Afficher également le rapport dans la conversation

Si un fichier du même nom existe déjà, ajouter un suffixe incrémental : `rgaa-2026-03-26-2.md`.

> Exemple : `audits/rgaa-2026-03-26.md`

## Grille de priorités

| Priorité | Définition | Exemples |
|----------|------------|---------|
| 🔴 **Bloquant** | Bloque l'accès au contenu ou à la fonctionnalité pour une personne qui utilise une aide technique | Image sans `alt`, champ sans label, lien vide, piège au clavier, focus non visible |
| 🟠 **Majeur** | Impact fort sur l'expérience mais contournable selon l’aide technique utilisée | Contraste insuffisant, hiérarchie de titres cassée, lien non explicite |
| 🟡 **Mineur** | Gêne légère, dégradation de l'expérience sans blocage | `autocomplete` manquant, `caption` de tableau absent, nouvelle fenêtre non signalée |

## Référence détaillée des critères

Chaque fichier de référence liste les critères avec leur condition, test de code, non-conformité type et priorité, ainsi que leur impact et leurs corrections par stack quand ils existent.

- **Images, Cadres, Couleurs** (thèmes 1–3, 14 critères) : [references/criteres-images-cadres-couleurs.md](references/criteres-images-cadres-couleurs.md)
- **Multimédia, Tableaux, Liens, Scripts** (thèmes 4–7, 28 critères) : [references/criteres-multimedia-tableaux-liens-scripts.md](references/criteres-multimedia-tableaux-liens-scripts.md)
- **Éléments obligatoires, Structure, Présentation** (thèmes 8–10, 28 critères) : [references/criteres-structure-presentation.md](references/criteres-structure-presentation.md)
- **Formulaires** (thème 11, 13 critères) : [references/criteres-formulaires.md](references/criteres-formulaires.md)
- **Navigation, Consultation** (thèmes 12–13, 23 critères) : [references/criteres-navigation-consultation.md](references/criteres-navigation-consultation.md)
- **Impacts par mécanisme de blocage** (tous thèmes, pour la ligne « Impact utilisateur ») : [references/impacts.md](references/impacts.md)
