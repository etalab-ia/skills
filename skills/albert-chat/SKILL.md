---
name: albert-chat
description: "Accompagner un FDE (Forward Deployed Engineer) dans la mise en œuvre du widget RAG etalab-ia/albert-chat sur un corpus métier dans l'API Albert : cadrage d'éligibilité, contrat des extraits et citations, vérification préalable check:config, adaptation sûre d'un fork, déploiement Scaleway Serverless Containers et intégration iframe (/embed.js) ou Web Component (albert-chat). À utiliser dès que l'utilisateur déploie albert-chat pour un cas d'usage métier, prépare une collection Albert pour ce widget, personnalise le fork, configure Scaleway/GitHub Actions, intègre le widget dans un intranet (CSP, CORS, postMessage) ou diagnostique un problème de citation, de configuration ou de déploiement. Complémentaire d'albert-api pour les appels généraux à l'API Albert."
---

# Albert Chat — Guide FDE de mise en œuvre

`etalab-ia/albert-chat` est un **runtime de widget RAG en lecture seule** (Next.js App Router + assistant-ui) adossé à l'API Albert. Ce guide cadre le parcours FDE de bout en bout, de l'évaluation initiale jusqu'à l'intégration dans la page hôte.

## Positionnement et frontière entre dépôts

```text
Dépôt du projet métier (FDE)              Fork albert-chat (ce runtime)
  extraction, découpage, OCR      ───▶     Collections Albert
  synchronisation des documents            │
                                           ▼
                                  POST /api/chat (clé serveur)
                                    ├─ /v1/search (hybrid)
                                    ├─ buildContextBlocks + citations [n]
                                    └─ /v1/chat/completions (flux NDJSON)
```

- **Séparation des responsabilités** : `albert-chat` ne contient ni base de données, ni authentification utilisateur, ni gestion de droits par document, ni historique persistant côté serveur. Les scripts d'ingestion vivent dans le dépôt du projet métier (s'appuyer sur [`albert-api`](../albert-api/SKILL.md) pour les appels à l'API Albert).
- **Vérifier l'éligibilité avant de forker** : le corpus configuré est identique pour tous les utilisateurs, toute personne connaissant l'URL peut interroger `/api/chat` dans la limite des plafonds en mémoire (`10 req/min/IP`, `500 req/jour/instance`), et le fil disparaît au rechargement. Si le besoin exige une authentification ou un cloisonnement par utilisateur, placer un mandataire authentifiant devant le service ou choisir une autre architecture avant tout déploiement.

---

## Workflow FDE en 5 étapes

**L'ordre compte** : le corpus et sa validation passent avant le déploiement du conteneur, sinon le widget répond en erreur à chaque question avec deux causes à démêler au lieu d'une.

### 1. Préparer le corpus dans le dépôt métier

Alimenter une ou plusieurs collections Albert en respectant le contrat lu par `lib/rag/citations.ts` :

- **`content` non vide, idéalement `<= 1200` caractères** (`LIMITS.maxChunkCharacters`) : les extraits vides sont ignorés et les extraits plus longs sont tronqués dans le prompt.
- **Métadonnées lues par le widget** : `title` (recommandé, sinon `guide_title`, sinon `Document <id>`), `source_url` (optionnel, URL absolue `http://` ou `https://` uniquement), `page_number` (optionnel, entier strictement positif, sinon `page`).
- **Préserver les numéros de page** : l'upload brut d'un fichier via `POST /v1/documents` (`file=...`) ne conserve pas la pagination. Créer un document sans fichier puis pousser les extraits page par page via `POST /v1/documents/{id}/chunks` (lots de 64 max, 10 champs de métadonnées max par extrait). Un corpus sans pagination fiable doit omettre `page_number` plutôt que fournir un numéro approximatif.

Détail complet du contrat, des limites Albert et de la stratégie de remplacement sans coupure : [`references/contrat-corpus.md`](references/contrat-corpus.md).

### 2. Configurer et valider avant de déployer

Dans le fork `albert-chat`, copier `.env.example` vers `.env.local` (ou un fichier dédié), renseigner une **clé `ALBERT_API_KEY` dédiée au projet** et la liste `ALBERT_COLLECTION_IDS` (entiers positifs séparés par des virgules), puis lancer :

```bash
pnpm install
pnpm check:config -- --env-file .env.local
```

> **Point de vigilance critique** : `pnpm check:config` vérifie le câblage (schéma de config, authentification Albert, existence des collections, extraits non vides via `buildContextBlocks`), **pas l'adéquation métier du corpus**. La recherche hybride d'Albert retourne des résultats sans seuil de score (`score_threshold` non défini) : même une collection hors sujet passe `check:config`. Valider ensuite la pertinence et les liens `#page=N` avec de vraies questions sur `/api/chat`.

### 3. Adapter le fork sans casser les contrats

**Personnalisation attendue pour un projet métier :**
- Libellés visibles dans `components/widget/assistant-modal.tsx` (`"Assistant ANSSI"`, `aria-label` du lanceur et du bouton de fermeture) et dans `components/widget/thread.tsx` (texte d'accueil dans `EmptyState` et tableau `SUGGESTIONS`).
- Page de démonstration `app/(site)/page.tsx` (ou suppression/adaptation selon l'usage) et modèle via `ALBERT_CHAT_MODEL` (défaut `gpt-oss-120b`).
- Neutraliser `release-please.yml` sur un fork mono-déploiement s'il n'y a pas de cycle de versions ; `anssi-sync.yml` est déjà bloqué hors propriétaire `etalab-ia`.

**Contrats à ne pas casser :**
- Conserver le nom d'élément `<albert-chat>` (`WIDGET_TAG` dans `widget/element.tsx`) et les identifiants internes du pont (`anssi-widget`, `__anssiWidget`, `data-anssi-widget`, `data-anssi-auto-mount`) si les pages hôtes ou les tests Playwright s'appuient dessus.
- Ne jamais importer `@codegouvfr/react-dsfr` dans `app/(embed)/` : les règles CSS non-layered du DSFR écrasent les classes utilitaires Tailwind v4 et réinitialisent les boutons et marges de `<p>`. Les deux groupes de routes `app/(site)/` et `app/(embed)/` doivent rester isolés.
- Si `SYSTEM_PROMPT` (`lib/rag/prompt.ts`) est modifié, préserver la consigne d'absence de Markdown (`*`, `#`, `|`) et le format de citation `[1]`, attendus par `lib/render-answer.ts`.

### 4. Déployer sur Scaleway depuis le fork

Dans les paramètres GitHub du fork (`Settings → Secrets and variables → Actions`), renseigner :
- **4 secrets** : `SCW_ACCESS_KEY`, `SCW_SECRET_KEY`, `SCW_ORGANIZATION_ID`, `SCW_PROJECT_ID` (plus `ALBERT_API_KEY` uniquement côté environnement du conteneur Scaleway, pas nécessaire au build).
- **5 variables de dépôt obligatoires** : `SCW_CONTAINER_ID`, `SCW_NAMESPACE_ID`, `SCW_IMAGE_BASE`, `SCW_REGISTRY_HOST`, `SCW_REGION`.

> **Piège de fork fréquent** : `.github/workflows/ci-cd.yml` contient des valeurs de repli pointant vers les ressources du démonstrateur ANSSI. Si les 5 variables ne sont pas renseignées dans le fork, le déploiement échoue à l'étape *« Verify the Scaleway project and container »* avec un message évoquant les droits/identifiants alors que la cause est l'identifiant du conteneur cible.

Sur le conteneur Scaleway (`fr-par`, port `8080`) : définir `HOSTNAME=0.0.0.0` (obligatoire pour Next.js standalone) et ne jamais définir `PORT` en variable d'environnement (nom réservé Scaleway). Avec `min_scale: 0`, poser une question de chauffe avant toute démonstration en direct pour absorber le démarrage à froid.

Procédure détaillée, variables d'environnement et pièges Scaleway : [`references/integration-et-deploiement.md`](references/integration-et-deploiement.md).

### 5. Intégrer dans la page hôte et vérifier

- **Privilégier l'iframe (`/embed.js`) par défaut** : isole DOM, CSS, stockage d'origine, applique `sandbox` et `Permissions-Policy`. Renseigner `EMBED_ALLOWED_PARENTS` (redéploiement requis après modification).
- **Réserver le Web Component (`<albert-chat>`)** aux intégrations sans cadre ou auto-hébergées (`widget.js` + `widget.css` + `widget.js.LEGAL.txt`). Le Shadow DOM n'isole que le CSS, pas les privilèges JavaScript. Renseigner `WIDGET_ALLOWED_ORIGINS` (redémarrage suffit).
- **Avant toute mise en production ou PR**, exécuter la chaîne complète dans le fork :

```bash
pnpm lint && pnpm typecheck && pnpm test && pnpm build && pnpm test:browser
```

Note : `pnpm test:browser` exécute Playwright sur le bundle de production généré (`pnpm build` préalable requis) avec des réponses simulées, sans appeler Albert.

---

## Diagnostic rapide des pièges connus

| Symptôme | Cause vérifiée | Correction |
|---|---|---|
| `check:config` passe mais le widget répond hors sujet | Albert hybride répond à toute requête (aucun `score_threshold`) | Tester des questions métier réelles sur `/api/chat` et contrôler la qualité du découpage |
| Échec CI *« Verify the Scaleway project and container »* sur un fork | Variables GitHub `SCW_*` absentes → repli sur l'ID du démonstrateur ANSSI | Renseigner les 5 variables (`SCW_CONTAINER_ID`, `SCW_NAMESPACE_ID`, `SCW_IMAGE_BASE`, `SCW_REGISTRY_HOST`, `SCW_REGION`) |
| Conteneur écrit `Ready` puis Scaleway signale le port 8080 injoignable | Next standalone écoute sur `HOSTNAME` (ID de conteneur non résolu) | Ajouter `HOSTNAME=0.0.0.0` dans l'env Scaleway (localement Podman masque le bug) |
| Iframe bloquée alors que `EMBED_ALLOWED_PARENTS` a été modifié | Variable lue au chargement/build (`next.config.ts`), ou joker `*.gouv.fr` / chemin présent | Lister chaque origine nue (`https://host.gouv.fr`) et **redéployer** (build + image) |
| Web Component bloqué en CORS | `WIDGET_ALLOWED_ORIGINS` manquant, joker `*`, ou `Origin: null` | Lister les origines nues autorisées et redémarrer le conteneur (pas de rebuild requis) |
| Citations non cliquables ou absentes de page | `source_url` absente/non `http(s)` ou upload fichier brut à Albert | Passer à l'ingestion par chunks avec `title`, `source_url`, `page_number` |
| Boutons du widget cassés ou marges `<p>` décalées sur `/embed` | Import DSFR ayant fuité dans le groupe `app/(embed)/` | Maintenir l'isolation stricte entre `app/(site)/` (DSFR) et `app/(embed)/` (Tailwind seul) |

---

## Références et skills complémentaires

- [`references/contrat-corpus.md`](references/contrat-corpus.md) — contrat de métadonnées, ingestion par chunks sans perte de page, limites Albert et vérification.
- [`references/integration-et-deploiement.md`](references/integration-et-deploiement.md) — iframe vs Web Component, matrice CSP/CORS, variables d'environnement, fork Scaleway et zone sûre de personnalisation.
- [`albert-api`](../albert-api/SKILL.md) — référence OpenGateLLM (authentification, collections, documents, chunks, OCR, recherche, modèles).
- [`react-dsfr`](../react-dsfr/SKILL.md) — si la page hôte ou la page vitrine `(site)` est modifiée avec `@codegouvfr/react-dsfr`.
- [`securite-developpement`](../securite-developpement/SKILL.md) — durcissement applicatif, secrets, en-têtes HTTP et conformité ANSSI.
