# Contrat de corpus et ingestion

## Sommaire

- [Ce que lit le widget dans chaque extrait](#ce-que-lit-le-widget-dans-chaque-extrait)
- [Regroupement et construction des liens de citation](#regroupement-et-construction-des-liens-de-citation)
- [Ingérer dans Albert sans perdre les numéros de page](#ingérer-dans-albert-sans-perdre-les-numéros-de-page)
- [Vérifier la configuration et le corpus](#vérifier-la-configuration-et-le-corpus)

---

## Ce que lit le widget dans chaque extrait

Le fichier `lib/rag/citations.ts` (`buildContextBlocks`) transforme les résultats de `POST /v1/search` avant de construire le contexte transmis au modèle :

| Champ | Emplacement | Statut | Comportement exact |
|-------|-------------|--------|--------------------|
| `content` | `hit.chunk.content` | **obligatoire** | `trim()` appliqué. Tout extrait vide est ignoré ; le contenu est tronqué à `LIMITS.maxChunkCharacters` (`1200` caractères). |
| `title` | `hit.chunk.metadata.title` | recommandé | Titre affiché dans la source et dans le contexte du modèle. Repli sur `guide_title`, puis sur `Document <document_id>`. |
| `source_url` | `hit.chunk.metadata.source_url` | optionnel | Retenu uniquement si c'est une URL absolue `http://` ou `https://`. Toute autre valeur (`javascript:`, chemin relatif, vide) est écartée : l'extrait reste utilisable mais s'affiche comme badge non cliquable. |
| `page_number` | `hit.chunk.metadata.page_number` | optionnel | Entier strictement positif (ou chaîne numérique positive). Repli sur `page` (héritage ANSSI). |

**Conséquence directe pour le découpage (chunking)** : viser des extraits d'au plus `1200` caractères dans le dépôt d'ingestion. Un extrait de `2000` caractères perd sa fin au moment où `buildContextBlocks` le coupe à `1200`.

---

## Regroupement et construction des liens de citation

- **Lien dynamique** : l'URL finale n'est jamais stockée dans les métadonnées. `buildCitationUrl(sourceUrl, page)` ajoute `#page=N` (ou `&page=N` s'il existe déjà un fragment sans `page=`). Un fragment existant contenant déjà `page=` est conservé tel quel.
- **Regroupement avec pagination** : deux extraits partageant la même URL finale (ou le même `(collection_id, document_id, page)` sans URL) sont fusionnés dans un seul bloc de contexte (plafonné à `1200` caractères) afin d'éviter des citations répétitives.
- **Absence de pagination** : si `page === null`, les extraits ne sont **jamais** regroupés (`sourceKey` inclut `chunk.id`). Un corpus HTML ou Markdown sans pagination doit omettre `page_number` plutôt qu'inventer `1` : inventer un numéro fusionnerait des extraits sans rapport et pointerait vers la mauvaise page.

---

## Ingérer dans Albert sans perdre les numéros de page

Le dépôt `albert-chat` ne réalise pas l'ingestion des projets métier ; ces règles s'appliquent aux scripts d'ingestion du dépôt métier (voir aussi [`albert-api`](../../albert-api/SKILL.md)) :

1. **Pourquoi éviter `POST /v1/documents` avec un fichier brut pour les PDF paginés** : le découpage automatique côté serveur Albert ne rattache pas le numéro de page à chaque extrait.
2. **Patron validé pour conserver les pages** (repris de `lib/albert/client.ts` et `scripts/lib/ingest.ts`) :
   - Extraire le texte page par page (`pdftotext` sur sauts de page ``, avec repli sur `POST /v1/ocr` modèle `mistral-ocr-2512` pour les pages sans couche texte).
   - Créer un document vide en `multipart/form-data` sur `POST /v1/documents` avec les champs `collection_id` et `name`, **sans champ `file`**.
   - Envoyer les extraits via `POST /v1/documents/{document_id}/chunks` par **lots de 64 maximum** (`BATCH = 64`), chaque extrait portant `{ content, metadata }`.
   - En cas d'échec en cours d'envoi par lots, supprimer immédiatement le document partiel (`DELETE /v1/documents/{document_id}`) pour ne pas laisser un demi-document interrogeable.
3. **Contraintes API Albert à intégrer dès la conception** :
   - **Plafond de 10 champs** dans `metadata` par extrait : garder des clés sobres (`title`, `source_url`, `page_number`, et éventuellement `source_sha256` et `sync_complete` pour une synchronisation incrémentale).
   - **Pagination des listings** : `GET /v1/collections` et `GET /v1/documents` paginent par défaut (`limit=100` max utile pour tout parcourir).
   - **Ordre des extraits non garanti** : `GET /v1/documents/{id}/chunks` ne restitue pas forcément le dernier extrait inséré en dernier. Pour une reprise après interruption, poser `sync_complete: true` sur le dernier extrait envoyé et rechercher ce marqueur dans les pages de chunks.

---

## Vérifier la configuration et le corpus

Avant de créer ou mettre à jour le conteneur `albert-chat` :

```bash
# Sur variables d'environnement déjà exportées
pnpm check:config

# Depuis un fichier .env sans exposer ALBERT_API_KEY dans l'historique shell
pnpm check:config -- --env-file .env.production
```

**Ce que fait exactement `scripts/check-config.ts` :**
- Lit `ALBERT_API_KEY`, `ALBERT_BASE_URL`, `ALBERT_CHAT_MODEL`, `ALBERT_COLLECTION_IDS` (et `ALBERT_COLLECTION_FR`/`EN` si `ALBERT_COLLECTION_IDS` est absente) sans masquer une variable définie à vide (`ALBERT_BASE_URL=""` échoue comme dans `/api/chat`).
- Appelle `POST /v1/search` (`method: "hybrid"`, `limit: 5`) sur **chaque collection** avec trois requêtes fixes (`"procédure"`, `"comment faire une demande"`, `"responsabilité"`).
- Passe les résultats dans `buildContextBlocks()` : si tous les extraits sont vides ou ignorés, la vérification échoue.

**Ce que `pnpm check:config` ne vérifie pas :**
- Comme `/api/chat` ne passe pas de `score_threshold`, la recherche hybride Albert renvoie des extraits même pour une requête hors sujet. Une sortie `OK` garantit **le câblage et la lisibilité des extraits**, jamais la pertinence du corpus.
- Toujours enchaîner par un test manuel en local (`pnpm dev` puis questions représentatives du métier) en vérifiant le texte des réponses, la présence des marqueurs `[n]` et l'ouverture effective des liens `#page=N`.
