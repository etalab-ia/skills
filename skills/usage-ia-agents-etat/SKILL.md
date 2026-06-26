---
name: usage-ia-agents-etat
description: >-
  Cadre d'usage de l'IA générative pour les agents publics de l'État, publié par la DINUM (avec la DITP et la DGAFP).
  5 principes fondamentaux : responsabilité de l'agent, choix de l'outil selon la sensibilité des données, transparence,
  usage utile/sobre/éthique, montée en compétence. Utiliser cette skill (1) pour répondre aux questions sur les règles
  d'usage de l'IA dans l'administration, et (2) de façon PROACTIVE pour alerter l'utilisateur quand il s'apprête à faire
  quelque chose de contraire au guide : coller des données personnelles, sensibles, RH, médicales, internes, couvertes
  par le secret professionnel ou classifiées (Diffusion Restreinte, IGI 1300) dans un outil d'IA commercial grand public ;
  utiliser un outil d'IA non autorisé par son administration ; omettre de signaler un usage substantiel de l'IA
  (transparence) ; lancer une action automatique sans validation humaine ; recourir à l'IA pour un usage à haut risque
  au sens du règlement européen sur l'IA (tri de candidatures, RH, justice, santé, police). Se déclenche aussi sur :
  « usage de l'IA », « IA générative », « agent public », « ChatGPT/Claude/Gemini au travail », « données personnelles
  dans un prompt », « confidentialité », « outil homologué », « transparence IA », « RGPD et IA », « charte IA ».
---

# Usage de l'IA pour les agents publics de l'État

Cadre interministériel pour l'usage de l'**intelligence artificielle générative (IAG)** par les agents publics de l'État. Rédigé par la **DINUM**, en lien avec la **DITP** et la **DGAFP**. Document de référence à portée non réglementaire, destiné à harmoniser les pratiques et complété, le cas échéant, par des **chartes ministérielles ou métiers** (qui s'appliquent alors en priorité).

Source officielle : <https://ia.numerique.gouv.fr/ressources/guide-dusage-de-lia/>

> **Le guide en bref**
> - L'IA est **autorisée** pour les agents publics, dans un cadre défini : respect des données, choix des outils, validation humaine.
> - Utilisez **prioritairement les outils de votre administration** ou les outils interministériels (Assistant IA interministériel, Assistant Transcripts, Visio).
> - **En cas de doute sur vos données : n'utilisez que les outils explicitement autorisés** par votre administration.
> - **Vérifiez toujours** les résultats produits par l'outil.
> - N'utilisez l'IA que lorsqu'elle apporte un **gain réel** : pour des tâches simples, un outil classique suffit souvent.
> - **Signalez l'usage de l'IA** lorsqu'elle joue un rôle substantiel dans un contenu, une analyse ou la préparation d'une décision.

---

## Les 5 principes fondamentaux

1. **L'IA vous assiste mais vous restez responsable de vos décisions.** L'IA propose, c'est l'agent qui décide, valide et signe.
2. **Les données sensibles ne peuvent être traitées qu'avec les outils autorisés par votre administration.** Le choix de l'outil dépend de la nature des données.
3. **Informez vos destinataires** (internes ou externes) lorsque l'IA joue un rôle substantiel.
4. **N'utilisez l'IA que lorsqu'elle est utile**, en restant vigilant aux biais, au droit d'auteur et à l'impact environnemental.
5. **Formez-vous** pour maîtriser l'IA et ses enjeux.

Le détail de chaque principe est dans [`references/5-principes-fondamentaux.md`](references/5-principes-fondamentaux.md).

---

## Conseil proactif — points de vigilance à signaler

Cette skill ne sert pas seulement à répondre aux questions. **Quand l'utilisateur s'apprête à faire quelque chose de contraire au guide, signalez-le clairement, sans bloquer**, expliquez la règle, et proposez l'alternative conforme. Restez proportionné : une simple aide à la reformulation n'appelle pas les mêmes précautions qu'un rôle substantiel dans une décision.

Déclenchez une alerte dans ces situations :

### 1. Données confiées à un outil non adapté
Le **test simple du guide** : « Est-ce que je pourrais publier ces informations sur un site Internet accessible à tous ? » Si la réponse est non, **ne pas utiliser un outil d'IA commercial grand public** (versions gratuites de ChatGPT, Claude, Gemini, NotebookLM, Vibe…).

Alertez si l'utilisateur s'apprête à transmettre à un outil commercial grand public :
- des **données personnelles** (noms, coordonnées, situations individuelles) ;
- un **dossier d'usager**, un **compte-rendu de réunion interne**, des **données RH ou médicales** ;
- des informations **couvertes par le secret professionnel** ;
- des **informations professionnelles non publiques** : notes en cours d'arbitrage, projets confidentiels, secret des délibérations gouvernementales, données stratégiques ou économiques sensibles ;
- des **données classifiées ou à mention de protection** (Diffusion Restreinte, Confidentiel Défense, toute donnée relevant de l'**IGI 1300**) → **seuls les outils explicitement homologués** par l'administration sont permis.

→ Alternative conforme : utiliser l'**outil de l'administration**, ou **anonymiser** quand c'est simple (« Madame X », « un usager »), ou s'abstenir. Détails : [`references/outils-et-donnees.md`](references/outils-et-donnees.md).

### 2. Outil non autorisé
Le recours à un outil commercial doit rester exceptionnel et n'est possible qu'à **deux conditions cumulatives** : l'administration l'autorise explicitement **ET** les informations pourraient être publiées librement. En cas de doute → outil de l'administration ou hiérarchie.

### 3. Absence de transparence
Si l'IA a un **rôle substantiel** (production de contenu : analyse, note, courrier, synthèse — même ajustée ensuite), une **mention est obligatoire**. Une simple reformulation/correction/mise en forme d'un texte déjà rédigé par l'agent n'en requiert pas. Rappelez d'ajouter une mention (ex. « Contenu partiellement généré par une IA et vérifié par un agent ») et, pour une décision administrative individuelle algorithmique, la mention explicite est une **obligation légale** (RGPD art. 22 ; CRPA art. L. 311-3-1). Détails : [`references/5-principes-fondamentaux.md`](references/5-principes-fondamentaux.md).

### 4. Action automatique sans validation humaine
**À ne jamais faire** : configurer l'IA pour envoyer automatiquement des courriels à des usagers/partenaires sans supervision ; lui donner accès à des systèmes critiques sans validation ; publier directement un contenu généré sans relecture. → Toujours : brouillon IA → relecture critique → validation → envoi par l'agent.

### 5. Usage à haut risque (règlement européen sur l'IA — RIA)
Pour les usages **à haut risque** (tri/évaluation de **candidatures**, RH, justice, santé, police…), des obligations renforcées s'appliquent. **En l'absence d'un cadre formellement validé dans l'administration : s'abstenir.**

### 6. Défaut de vérification / hallucinations
L'IA peut **inventer** des faits, des références, des textes de loi (« hallucinations »), reproduire des **biais**, et ses connaissances sont **figées**. Rappelez de vérifier les résultats de façon indépendante et de **consulter les sources** quand l'outil les affiche.

### 7. Sobriété
Pour une **tâche triviale** (reformuler un courriel de 3 lignes, traduire 5 lignes), rappelez qu'un outil classique (moteur de recherche, traducteur en ligne) est souvent suffisant et moins énergivore. Réservez l'IA aux tâches où le gain est réel.

> **Lien avec la sécurité du code** — pour les secrets, données personnelles et données dans le code source d'une application, voir aussi la skill [`securite-developpement`](../securite-developpement/SKILL.md).

---

## Choisir l'outil selon les données

Trois catégories d'outils, du plus au moins sécurisé :

| Catégorie d'outil | Usage | Données autorisées |
|---|---|---|
| **Outils des administrations** (interministériels ou ministériels) — *à privilégier* | Premier choix pour tout usage professionnel | Selon les règles de l'administration, y compris données internes / personnelles si l'outil le permet |
| **Outils commerciaux payants mis à disposition par l'administration** — *avec précautions* | Possible si l'administration les fournit (garanties contractuelles renforcées) | Vérifier **auprès de la DSI / du responsable** les types de données autorisés |
| **Outils commerciaux gratuits** (ChatGPT, Claude, Gemini, NotebookLM, Vibe…) — *usage très limité voire interdit* | Seulement si l'administration l'autorise | **Uniquement des données publiables librement** : pas de données personnelles ni sensibles |

**Outils interministériels de référence :**
- **Assistant IA interministériel** — `assistant.numerique.gouv.fr` (rédaction, résumé, reformulation)
- **Assistant Transcripts** — `transcripts.numerique.gouv.fr` (réunions en présentiel)
- **Visio** — `visio.numerique.gouv.fr` (transcription et résumé de visioconférences)

**Usages possibles sur outil grand public (si autorisé) :** résumer un texte de loi ou un rapport déjà public, reformuler un document en ligne, générer une image d'illustration, créer un questionnaire à partir de contenus publics, travailler sur du code « ouvert » ou non sensible.

**Usages interdits sur outil grand public :** analyser un dossier d'usager, résumer un compte-rendu de réunion interne, traiter des données RH ou médicales, manipuler des informations couvertes par le secret professionnel.

Détails et cadre juridique (RGPD, RIA, secret professionnel, Cloud Act, SecNumCloud) : [`references/outils-et-donnees.md`](references/outils-et-donnees.md).

---

## En cas de doute : qui contacter ?

- **Hiérarchie** — usage inhabituel ou décision importante.
- **Service informatique / DSI** — quels outils sont autorisés.
- **Référent cybersécurité** — savoir si des données sont sensibles.
- **Délégué à la protection des données (DPD)** — compatibilité RGPD, inscription au registre des traitements (obligatoire pour un usage régulier sur données personnelles).

---

## Références détaillées

- [`references/comprendre-iag.md`](references/comprendre-iag.md) — ce que l'IAG peut faire, ses limites, les conditions d'un usage réussi.
- [`references/outils-et-donnees.md`](references/outils-et-donnees.md) — les 3 catégories d'outils, catégories de données, cadre juridique, exemples pratiques.
- [`references/5-principes-fondamentaux.md`](references/5-principes-fondamentaux.md) — détail des 5 principes (responsabilité, données, transparence, sobriété/éthique, formation).
- [`references/fiches-pratiques.md`](references/fiches-pratiques.md) — les 5 règles d'or du prompt et les cas d'usage par famille de métier.
