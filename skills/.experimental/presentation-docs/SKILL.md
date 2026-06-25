---
name: presentation-docs
description: Transforme une source (note Obsidian, texte/Markdown brut, ou fichier de présentation PPTX/PDF/DOCX) en un fichier Markdown propre respectant la convention "mode présentation" de Docs (La Suite) — une diapo par diviseur `---`. Produit uniquement le fichier .md prêt à coller/importer dans Docs ; ne publie rien. Utiliser quand l'utilisateur dit "/presentation-docs", "transforme cette note en présentation Docs", "convertis X en présentation Docs", "mets ce PPTX en diapos Docs", "formate ce texte en présentation Docs".
---

# Skill : Présentation Docs

Transforme une source en un **fichier Markdown propre**, formaté selon la convention du **mode présentation de Docs (La Suite)**. La sortie est un `.md` prêt à coller ou importer dans Docs. **La skill ne publie rien** : aucun appel réseau, aucune publication — elle produit le fichier, point.

Le mode présentation de Docs ([doc officielle](https://docs.numerique.gouv.fr/docs/f7ca1950-5e0f-48bb-993a-54584e8c060d/)) repose sur une règle unique : **chaque diviseur `---` crée une nouvelle diapo**. C'est un mode lecture. Il supporte alignement, couleurs, types de blocs, colonnes et médias (images/vidéos lisibles en présentant).

## Entrées possibles

1. **Note Obsidian** du vault → lecture directe (`Read`).
2. **Texte / Markdown brut** (collé par l'utilisateur ou pointé par un chemin) → utilisé tel quel comme matière première.
3. **Fichier de présentation externe** (PPTX / PDF / DOCX) → conversion en markdown (cf. § Récupérer texte et médias).

## Sortie

Un seul livrable : un fichier `.md` dans le vault, respectant la convention diapos ci-dessous, avec ses médias dans un dossier d'assets à côté. À la fin, montrer le résultat et rappeler le nombre de diapos (= nombre de `---` + 1). L'utilisateur l'utilise ensuite dans Docs (copier-coller le contenu, ou importer le `.md`) — ce n'est pas du ressort de la skill.

## La convention diapos (à respecter absolument)

- **Séparateur de diapo = `---`** seul sur sa ligne, **avec une ligne vide avant et après**. Sans ces lignes vides, `---` collé à une ligne de texte au-dessus est interprété comme un soulignement de titre (setext H2), pas comme un diviseur — la diapo ne se crée pas.
- **Titres : `#` pour la diapo d'accroche, `##` pour les diapos suivantes** — les modèles officiels de l'équipe Docs utilisent un `# Titre` (souvent avec emoji) comme 1re diapo. Donc `#` = diapo de titre/accroche, `##` = titres des diapos de contenu, `###` = sous-titres. (Seul cas où éviter le `# H1` : quand un titre est déjà poussé séparément par une API de création de document, pour ne pas doublonner.)
- **1 diapo = 1 idée** : titre court (`##`) + contenu concis (puces, lignes courtes). Éviter les pavés : un contenu plus haut que l'écran reste accessible au scroll mais nuit à la lisibilité en présentation.
- **Médias** : `![texte](chemin-ou-url)` → bloc image/vidéo. Liens, **gras**, *italique*, listes, citations `>`, tableaux et blocs de code sont conservés.
- **Ce que le markdown NE transporte PAS** : l'alignement (centrage), les couleurs et les colonnes sont des fonctions de l'éditeur Docs sans équivalent markdown. Le `.md` livre la **structure** (titres, texte, listes, diapos, images, liens) ; le **fignolage visuel se fait à la main dans Docs** après import. Le dire à l'utilisateur, ne pas le simuler.

## Pré-requis

- Aucun pour une note Obsidian ou un texte/Markdown brut.
- Pour un **fichier externe** : skill `rag-parse` (`lit parse`) et/ou `poppler` (`pdftotext`, `pdfimages`, `pdftoppm`, `pdfinfo` — `brew install poppler`). `magick`/`convert` (ImageMagick) utile pour recadrer. Une présentation disponible uniquement en ligne (pas en fichier local) doit d'abord être exportée en **PPTX ou PDF**.

## Workflow

### Étape 1 — Identifier la source

- **Note Obsidian** (chemin `.md`) → `Read`.
- **Texte / Markdown brut** → prendre le contenu fourni tel quel.
- **Fichier PPTX / PDF / DOCX / ODP** → en extraire texte et médias (étape 2). Pour un PDF, `pdftotext`/`pdfimages`/`pdftoppm` ; pour un PPTX, `rag-parse` ou parsing `python-pptx`.

### Étape 2 — Restructurer en diapos

**Distinction de fidélité selon la source :**

- **Source PDF / PPTX / présentation existante** → **respecter à l'identique la mise en forme et le découpage de la source**. Une diapo source = une diapo Docs, dans le même ordre, mêmes titres/puces/médias. Ne pas synthétiser, reformuler, fusionner ni réordonner : on translittère le deck en convention Docs (un `---` entre chaque diapo), transformation **syntaxique** seulement.
- **Source note / texte / Markdown brut** → construire un deck en découpant aux frontières logiques, **1 idée par diapo** :
  1. **Diapo de titre** (avant le 1er `---`) : titre (`#` recommandé, à la manière des modèles Docs), sous-titre, date. Garder court.
  2. `---`
  3. **Diapos de contenu** : chacune = `## Titre court` + 2 à 5 puces concises, ou une citation `>`, ou un média, ou un tableau.
  4. **Diapo de clôture** éventuelle (synthèse, contacts).

  Si la source est déjà du Markdown, **réutiliser sa structure** (titres existants → titres de diapo) plutôt que de tout réécrire ; n'ajouter que les `---` et les ajustements de convention.

Veiller pour chaque `---` à la **ligne vide avant et après**.

#### Texte ET images, pas que des images

Objectif : un deck **texte éditable + images**, jamais un empilement de pages aplaties en images. Le texte d'une diapo (titres, puces, libellés) reste du **texte markdown** — éditable, cherchable, accessible. On n'embarque en image que ce que le markdown ne peut pas reproduire (photos, captures, schémas).

**1. Récupérer le texte de chaque diapo.**
- PDF → `pdftotext -layout -f {page} -l {page} {fichier.pdf} -` (la couche texte d'un export de slides est en général propre, emojis compris).
- PPTX → parser les zones de texte par diapo (`python-pptx` : pour chaque `shape` de `slide.shapes`, vérifier `shape.has_text_frame` avant de lire `shape.text_frame` — toutes les formes n'en ont pas, sinon `AttributeError` ; ou dézipper le `.pptx` et lire `ppt/slides/slideN.xml`). Avantage du PPTX : texte et images sont des éléments **distincts** par diapo.

**2. Récupérer les médias de contenu.**
- Bitmaps embarqués (photos, captures, illustrations) → `pdfimages -all -p {fichier.pdf} {prefixe}` (PDF, `pdfimages -list` pour l'inventaire) ou `ppt/media/` du PPTX. Écarter le **bruit de gabarit** (fonds, logos répétés, emojis décoratifs).

**3. Schémas vectoriels non reproductibles** (diagrammes, pyramides, infographies, flux) → ni texte ni bitmap extractible, et le markdown ne sait pas les recréer. Pour **ceux-là seulement**, rendre la page concernée en image et l'embarquer **en plus** du texte : `pdftoppm -jpeg -r 130 -f {page} -l {page} {fichier.pdf} {prefixe}`. Résultat par diapo : `## titre` + texte markdown + image du schéma.

Décision par diapo : titres/puces/colonnes de texte → **tout en markdown** (pas d'image) ; photo/capture/schéma → **texte markdown + l'image**. Conserver les **liens** en texte (`[libellé](url)`). Récupérer les URL écrites en clair depuis le texte extrait (`pdftotext {fichier.pdf} - | grep -oE 'https?://[^ )<>"]+' | sort -u`) ; pour un lien dont le libellé diffère de la cible (annotation hypertexte), lire les annotations avec un parser PDF — ex. `pypdf` : pour chaque page, `page.annotations` → `/A` → `/URI` (ne pas compter sur `strings`, les flux PDF étant souvent compressés).

Enregistrer les médias dans un **dossier d'assets à côté du `.md`** (ex : `assets/{nom-deck}/slide-04.jpg`) et les référencer en markdown relatif : `![description](assets/{nom-deck}/slide-04.jpg)`.

**Builds d'animation PowerPoint** : un même slide exporté en plusieurs pages quasi identiques produit des doublons. Replier chaque série sur son **état final** et le **signaler** à l'utilisateur (ne pas supprimer silencieusement).

### Étape 3 — Écrire le fichier .md

Proposer un emplacement cohérent dans le vault :
- Note source → à côté, suffixe ` - présentation.md` (ex : `ALLiaNCE/Strat 2026.md` → `ALLiaNCE/Strat 2026 - présentation.md`).
- Fichier externe ou texte brut → dossier thématique pertinent ; demander si ambigu.

Écrire avec `Write`, puis **montrer le résultat** (nombre de diapos) et indiquer où il se trouve. Si des médias locaux sont référencés, signaler qu'à l'import dans Docs ils peuvent devoir être réinsérés à la main (un import markdown ne transporte pas les binaires).

## Contraintes

- **Sortie = fichier .md uniquement** — la skill ne publie pas et ne touche à aucun service Docs ; elle produit seulement le fichier.
- **Fidélité au deck source** — pour un PDF/PPTX, reproduire à l'identique contenu, découpage et ordre (1 diapo source = 1 diapo). Pas de synthèse ni reformulation. La restructuration éditoriale est réservée aux sources texte/Markdown.
- **Médias récupérés, pas perdus** — extraire et réembarquer schémas/photos/captures. Ne jamais remplacer un média par une description textuelle.
- **Diviseur entouré de lignes vides** — sinon la diapo ne se crée pas (interprété comme titre setext).
- **Titres** — `#` pour la diapo d'accroche (comme les modèles officiels de l'équipe Docs), `##` pour les titres des diapos suivantes, `###` pour les sous-titres.
- **Honnêteté visuelle** — le markdown porte la structure et les coupures de diapo, pas l'alignement/couleurs/colonnes (réglages manuels dans Docs).

## Exemple (avant / après)

Source (texte/Markdown brut) :

```
## Bilan T1
- 3 serveurs MCP en prod
- 12 administrations accompagnées
## Cap T2
- Cartographie des données mobilisables
- Guide MCP pour les administrations
```

Sortie `.md` (`---` = nouvelle diapo, lignes vides autour, `#` pour la diapo d'accroche) :

```
# Socle IA interministériel

Point d'étape · juin 2026

---

## Bilan T1

- 3 serveurs MCP en production
- 12 administrations accompagnées

---

## Cap T2

- Cartographie des données mobilisables pour l'IA
- Guide MCP à destination des administrations
```

→ 3 diapos (titre + bilan + cap).
