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

- Les corrections sont dans `references/corrections/`, sous le même nom de fichier que la référence du thème. Ne les lire que pour rédiger la correction d’une NC.
- Quand le critère a des blocs « Correction — React / JSX » et « Correction — Rails / ERB », reprendre le bloc de la stack retenue. Si le bloc manque pour ce critère, rédiger la correction dans la stack retenue. Si le bloc ne convient pas au défaut, ou si le projet a déjà son propre mécanisme, adapter la correction et le signaler.
- Quand la référence n’a qu’un exemple, sans bloc par stack : en React / JSX, le reprendre ; en Rails / ERB, le transposer (`className` → `class`, `htmlFor` → `for`, expressions JSX → ERB) et le signaler par « exemple transposé depuis React » ; en HTML ou pour une autre stack, en donner la version HTML.
- Ne jamais inventer de classe `fr-*` du DSFR : n’utiliser que celles déjà présentes dans les références ou dans le code audité.
- Même règle pour le balisage d’un composant DSFR : si aucun bloc de la référence ni le code audité ne le montre, ne pas écrire sa structure de mémoire ; renvoyer à la documentation du composant sur [le site du DSFR](https://www.systeme-de-design.gouv.fr/).

## Workflow d’audit en trois phases

### Phase 1 — Analyse statique silencieuse

Lire le code et établir les verdicts sans poser de question :

1. Déterminer la stack (section précédente) et le mode page ou composant (ci-dessous).
2. Lire aussi les fichiers liés au code audité quand ils existent (script, styles, classe du composant) : ils portent souvent les comportements à vérifier.
3. Lire les cinq fichiers de classement (`references/classement/`, voir « Référence détaillée des critères ») : ils donnent le mode d’évaluation de chaque critère. Puis parcourir les thèmes à évaluer en consultant les fichiers de référence. Pour chaque critère, lire son bloc « Texte officiel » : l’intitulé, les tests numérotés, les cas particuliers et les notes techniques, copiés mot pour mot de la méthodologie officielle. Le verdict se juge contre ces tests ; les cas particuliers disent souvent quand le critère est NA. Un terme en italique est défini dans le glossaire officiel ([references/glossaire.md](references/glossaire.md)) : quand le verdict dépend de sa définition, chercher le terme parmi les titres `###` du glossaire, sans lire le fichier en entier.
4. Attribuer à chaque critère un statut, en appliquant la règle de tri par impact et le mode du critère :
   - **C** — Conforme : critère respecté
   - **NC** — Non conforme : critère violé (identifier l’élément et le problème)
   - **NA** — Non applicable : critère sans objet pour ce contenu (justifier)
   - **NT** — Non testé : le mode du critère ne permet pas de conclure à la lecture du code, et aucune réponse de phase 2 ne l’a tranché. Chaque NT renvoie à la ligne de son classement. Ne jamais conclure C par défaut.

**Mode d’évaluation de chaque critère** (classement provisoire, en attente de l’avis du pôle accessibilité numérique) :

- **code** : le verdict (C, NC ou NA) se tranche à la lecture du code.
- **mixte** : le code prouve une NC, ou une conformité quand la ligne le prévoit (critères « si nécessaire », contrastes entièrement déterminés dans le code) ; chaque ligne dit laquelle. Sans preuve dans le code, NT.
- **conditions réelles** : une vérification posée en phase 2 suffit ; sans réponse, NT.
- **jugement humain** : toujours NT, jamais C.

Dans tous les modes, NA reste possible quand le code montre que le critère est sans objet (aucune image → 1.3 et 1.8 NA). Si une valeur dynamique de ce code (prop, variable, texte traduit) peut apporter l’objet du critère, le code ne le montre pas : NT. Le contenu injecté par un gabarit (`yield`, `children`) n’entre pas dans cette règle : il se vérifie sur les vues qui le fournissent.

Les cas listés après « Le code prouve : NC… » sont des exemples, pas une liste fermée : tout défaut visible dans le code et dont l’impact est nommé reste une NC, même absent de la ligne.

**Mode page ou composant :**

- **Page** : document complet (`<html>`, `<head>`), layout ou gabarit de route (`app/views/layouts/`, `pages/`, `app/**/page.tsx`, `index.html`).
- **Composant** : tout le reste (composant, partial, fragment de page).

En mode composant, 13 critères ne sont pas évalués, car ils dépendent de la page complète ou de l’ensemble de pages : 8.1, 8.3 à 8.6, 9.2 et 12.1 à 12.7. Les compter à part, en « non évalués — mode composant », jamais en NA. Les autres critères de ces thèmes s’évaluent sur le fragment audité. Indiquer le mode dans l’en-tête du rapport.

**Règle de tri par impact (avant tout verdict) :**

Le RGAA vérifie un défaut restitué à la personne qui consulte la page. Raisonner par impact, pas par récitation de règle :

1. **Avant de conclure NC** : nommer l’impact concret, c’est-à-dire le blocage et l’outil concerné (voir [references/impacts.md](references/impacts.md)). Sans impact réel (élément purement décoratif, règle sans objet dans ce cas), ce n’est pas une NC : classer C ou NA.
2. **Avant de conclure C** : vérifier que le mode du critère le permet. C n’est possible qu’en mode code, quand la ligne « mixte » prévoit un C (« Le code prouve : C… »), ou après une réponse de phase 2 à la question que cite le critère. Avoir parcouru le critère et vérifié qu’aucun motif à risque n’est présent. L’absence de défaut visible ne suffit pas : en mode mixte, elle donne NT.
3. **Avant de conclure NA** : vérifier que le critère ne s’applique vraiment pas à ce contenu, pas seulement qu’aucun défaut n’a été trouvé. NA quand l’élément visé par les tests officiels est absent, même si cette absence est la NC d’un autre critère : la justification renvoie à cette NC (aucun `<th>` → 5.7 NA, « en-têtes absents : NC en 5.6 »). Sauf si la ligne de classement en dispose autrement.
4. **Un élément, plusieurs critères** : un élément qui échoue aux tests de plusieurs critères est NC dans chacun, sans dédoublonnage. La correction groupée les résout en une modification.

**Critère officiel :** avant de conclure NC, désigner le test officiel que le code ne satisfait pas (« test 1.1.5 ») et citer la condition en cause. Sans test officiel en défaut, pas de NC : reprendre l’analyse ou classer NT. Chaque NC renvoie au critère officiel, par un lien de la forme `https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.1`, et propose une correction. Les « non-conformités types » des fichiers de référence sont des exemples : la règle reste le texte officiel. Un critère classé « jugement humain » n’a que son intitulé officiel : il suffit à décider NA, ses tests restent à l’auditeur.

### Phase 2 — Vérifications en conditions réelles

Après l’analyse, poser en un seul message les vérifications que le code seul ne permet pas, prises dans ce catalogue fermé : aucune autre question. Une question rattache les critères dont la ligne de classement la cite (« question « Clavier » »). Ne la poser que si au moins un de ces critères est applicable et encore NT après la phase 1. En mode composant, les critères non évalués ne déclenchent aucune question.

| Question | Priorité | Libellé posé |
|---|---|---|
| **Clavier** | 🔴 | Test au clavier et au pointeur effectué ? (Tab, Maj+Tab, Entrée, Espace, Échap, flèches sur chaque élément interactif ; on sort de chaque composant au clavier ; chaque commande s’utilise au pointeur ; un contenu additionnel reste visible quand le pointeur passe dessus) |
| **Focus visible** | 🔴 | Focus visible sur tous les éléments interactifs ? |
| **CAPTCHA** | 🔴 | Le CAPTCHA propose-t-il une autre forme d’accès (audio, question) ? |
| **Titre de la page** | 🔴 | Le titre de la page est-il pertinent et spécifique ? |
| **Zoom et reflow** | 🟠 | Zoom à 200 %, fenêtre de 320 px de large, fenêtre de 256 px de haut et espacement du texte augmenté testés ? (aucun texte coupé, pas de défilement horizontal à 320 px, pas de défilement vertical à 256 px pour un contenu en écriture verticale, conçu pour défiler horizontalement : une page en français n’est pas concernée) |
| **Contrastes** | 🟠 | Contrastes vérifiés ? (texte, composants d’interface, liens dans un texte) |
| **Sans feuille de style** | 🟠 | Contenu consulté sans feuille de style ? (information toujours présente, ordre de lecture compréhensible) |
| **Orientation** | 🟡 | Contenu consulté en portrait puis en paysage ? |

Exemple de message, quand seuls les critères des questions « Clavier » et « Contrastes » restent NT :

```
Avant de finaliser le rapport, quelques vérifications que le code seul ne permet pas. Pour chacune, indique le résultat et les défauts observés (élément, touche ou écran concerné), pas seulement si le test a été fait :

🔴 Test au clavier et au pointeur effectué ? (Tab, Maj+Tab, Entrée, Espace, Échap, flèches sur chaque élément interactif ; on sort de chaque composant au clavier ; chaque commande s’utilise au pointeur ; un contenu additionnel reste visible quand le pointeur passe dessus)
🟠 Contrastes vérifiés ? (texte, composants d’interface, liens dans un texte)
```

Chaque réponse confirme ou corrige les verdicts des critères qui citent la question. Un « oui » ou « fait » dit que le test a eu lieu, pas qu’il a réussi : sans résultat, redemander le résultat et les défauts observés avant de lever NT. Puis, critère par critère :

- **NC** : la réponse rapporte un défaut qui relève du critère. Le décrire avec l’élément concerné.
- **C** : la réponse couvre ce que le critère vérifie (sa ligne « Reste : ») et ne rapporte aucun défaut.
- **NT** : pas de réponse, réponse sans résultat, ou réponse qui ne couvre pas ce que vérifie le critère.

### Phase 3 — Format de sortie

Demander le format attendu, sauf s’il a déjà été précisé :

```
Audit terminé. Quel résultat souhaites-tu ?

1. Rapport complet enregistré dans audits/
2. Corrections directes dans les fichiers
3. Les deux
```

Sans réponse, ou en exécution non interactive (agent, script) : sauter les phases 2 et 3, laisser en NT les critères « conditions réelles » et les critères « mixte » dont le code ne prouve rien, produire le rapport et l’exporter.

## Format du rapport

```markdown
## Rapport d’auto-évaluation RGAA assistée par IA

> Produit par une IA à partir du code : ce n’est pas un audit de conformité RGAA, et une partie des critères reste à vérifier par une personne.

- **Référentiel :** RGAA 4.1.2
- **Date :** JJ/MM/AAAA
- **Périmètre :** [description du code / page / composant]
- **Stack :** [HTML | React / JSX | Rails / ERB] (déduite de [l’extension du fichier | la syntaxe du code | le projet])
- **Mode :** [page | composant]
- **Bilan :** X conformes, X non conformes, X non testés, X non applicables[, X non évalués (mode composant)] (106 critères)
- **À vérifier par une personne :** les X critères non testés, listés dans « Critères non testés »
- **Taux sur les critères tranchés :** X % (X C sur X C + NC), indicatif, ne vaut pas déclaration de conformité

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

En mode composant, les lignes 8, 9 et 12 ne comptent que les critères évalués sur le fragment et précisent le reste : « 8. Éléments obligatoires (5 non évalués) », « 9. Structuration (1 non évalué) », « 12. Navigation (7 non évalués) ».

---

### Non-conformités détectées

**[NC] {ID} — {Intitulé du critère}** ([critère officiel](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#{ID}))
- **Élément concerné :** `<code>` ou description de l’endroit dans la page
- **Test officiel en défaut :** {ID}.{n} — condition non satisfaite, citée du texte officiel
- **Problème :** description précise de la violation
- **Impact utilisateur :** mécanisme du blocage et outil concerné
- **Correction :** action concrète à mener, dans la stack retenue
- **Priorité :** 🔴 Bloquant / 🟠 Majeur / 🟡 Mineur

---

### Correction groupée _(si plusieurs NC portent sur le même extrait de code)_

**NC {ID1} + {ID2} — résolues en une modification**

Avant / après, dans la stack retenue.

Priorité : celle de la NC la plus grave (un même champ en 🔴 au 11.10 et en 🟠 au 3.1 → 🔴).

---

### Critères conformes

{ID1}, {ID2}, {ID3}... (liste compacte)

### Critères non applicables

- **{ID}** — {justification courte}

### Critères non testés

- **{ID}** — {« Reste » de la ligne du classement, adapté à l’élément audité}

### Limites du mode composant _(si applicable)_

Ces critères nécessitent la page complète pour être évalués, entre autres :
- 8.1, 8.3 à 8.6 Type de document, langue par défaut et titre de la page
- 8.2 Code source valide (évalué sur le fragment, à revérifier sur la page complète)
- 9.1 Hiérarchie de titres sur l’ensemble de la page (évaluée sur le fragment, à revérifier sur la page complète)
- 9.2 Structure du document
- 12.1 à 12.7 Systèmes de navigation, plan du site, moteur de recherche, zones de regroupement et lien d’évitement
```

**Impact utilisateur :** reprendre la ligne **Impact** du critère dans sa référence si elle correspond au défaut constaté. Sinon, décrire le mécanisme du blocage et l’outil concerné en s’appuyant sur [references/impacts.md](references/impacts.md), par exemple : « Pour une personne qui utilise un lecteur d’écran, le lien est restitué caractère par caractère : la destination est inintelligible. » Ne jamais désigner une catégorie de handicap.

## Export du rapport

Quand le rapport est demandé en phase 3, ou par défaut sans réponse :

Si la personne a demandé un autre emplacement, il prime sur `audits/`.

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
| 🟡 **Mineur** | Gêne légère, dégradation de l’expérience sans blocage | `autocomplete` manquant, `caption` de tableau absent, nouvelle fenêtre ouverte au chargement |

Chaque NC reprend la ligne **Priorité** de sa référence. Ne s’en écarter que si l’impact du défaut constaté diffère de la ligne **Impact** de la référence, et l’écrire : « 🟡 Mineur (référence : 🔴 ; motif) ».

## Référence détaillée des critères

Chaque fichier de référence liste les critères avec leur texte officiel (bloc « Texte officiel », généré depuis la méthodologie officielle : ne jamais le reformuler), leur non-conformité type, leur impact et leur priorité. Les corrections par stack sont dans `references/corrections/`, sous le même nom de fichier. Chaque fichier de classement donne, en une ligne par critère, son mode d’évaluation, ce que le code prouve et ce qui reste à vérifier. Lire les cinq fichiers de classement en phase 1, avant les références : chaque audit attribue un statut aux 106 critères.

- **Images, Cadres, Couleurs** (thèmes 1–3, 14 critères) : [references/criteres-images-cadres-couleurs.md](references/criteres-images-cadres-couleurs.md) ; classement : [references/classement/criteres-1-3.md](references/classement/criteres-1-3.md)
- **Multimédia, Tableaux, Liens, Scripts** (thèmes 4–7, 28 critères) : [references/criteres-multimedia-tableaux-liens-scripts.md](references/criteres-multimedia-tableaux-liens-scripts.md) ; classement : [references/classement/criteres-4-7.md](references/classement/criteres-4-7.md)
- **Éléments obligatoires, Structure, Présentation** (thèmes 8–10, 28 critères) : [references/criteres-structure-presentation.md](references/criteres-structure-presentation.md) ; classement : [references/classement/criteres-8-10.md](references/classement/criteres-8-10.md)
- **Formulaires** (thème 11, 13 critères) : [references/criteres-formulaires.md](references/criteres-formulaires.md) ; classement : [references/classement/criteres-11.md](references/classement/criteres-11.md)
- **Navigation, Consultation** (thèmes 12–13, 23 critères) : [references/criteres-navigation-consultation.md](references/criteres-navigation-consultation.md) ; classement : [references/classement/criteres-12-13.md](references/classement/criteres-12-13.md)
- **Impacts par mécanisme de blocage** (tous thèmes, pour la ligne « Impact utilisateur ») : [references/impacts.md](references/impacts.md)
- **Glossaire officiel** (à consulter terme par terme, jamais en entier) : [references/glossaire.md](references/glossaire.md)
