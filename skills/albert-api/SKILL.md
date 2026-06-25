---
name: albert-api
description: >-
  Albert API — API d'inférence et d'IA générative interministérielle de l'État
  (OpenGateLLM, hébergement SecNumCloud). Compatible OpenAI : chat completions,
  embeddings, rerank. Plus transcription audio, OCR, parsing de documents, et un
  pipeline RAG souverain complet (collections, documents, recherche sémantique/
  hybride/lexicale). À utiliser pour appeler Albert, intégrer un LLM souverain
  dans un produit ou un script de l'administration, faire du RAG sur corpus
  interne, transcrire de l'audio ou extraire du texte de PDF/images via Albert,
  ou gérer ses clés et quotas Albert. Déclencheurs : Albert, Albert API,
  OpenGateLLM, LLM de l'État, IA générative souveraine, base_url Albert.
---

# Albert API — Référence consolidée

API d'inférence de l'État français, opérée par le département IAE de la DINUM (commun numérique **OpenGateLLM**). **Largement compatible OpenAI** : pour `chat/completions`, `embeddings` et `rerank`, réutiliser le SDK `openai` (ou tout client OpenAI) en changeant simplement `base_url` et la clé. Les capacités propres à Albert (RAG, audio, OCR, parsing) s'appellent en HTTP direct.

**Base URL :** `https://albert.api.etalab.gouv.fr`
**Spec OpenAPI (fait foi) :** `https://albert.api.etalab.gouv.fr/openapi.json`
**Doc humaine :** https://doc.incubateur.net/alliance/albert-api

---

## Comment utiliser cette skill

- **Consommation d'abord.** L'usage courant = appeler les modèles (chat, embeddings) et le RAG. Les écritures (créer collection, uploader documents, gérer des clés) ne se font que sur intention explicite de l'utilisateur.
- **Compatibilité OpenAI.** Pointer un client OpenAI sur `https://albert.api.etalab.gouv.fr/v1` évite de réécrire du code. Les schémas de requête/réponse de `chat/completions` et `embeddings` suivent OpenAI ; Albert ajoute des paramètres (`search`, `search_args`).
- **Ne jamais logger ni afficher le token.** Le Bearer token est un secret. Ne pas l'écho dans les réponses, les logs, les exemples copiés. Le lire depuis une variable d'environnement (`ALBERT_API_KEY`).
- **L'OpenAPI fait autorité.** En cas de divergence entre ce fichier et la spec récupérée en live, **suivre la spec**. La version peut évoluer (ce fichier décrit v0.4.7).
- **Ne pas inventer d'ID de modèle.** Lister les modèles disponibles via `GET /v1/models` avant d'en coder un en dur.

---

## Authentification & accès

- **Header :** `Authorization: Bearer <token>` sur tous les endpoints `/v1/*`.
- **Public :** réservé aux agents de la fonction publique. Demande d'accès en ligne (voir la doc humaine). L'accès distingue un mode **expérimentation** (quotas réduits) d'un mode **production** (sur dossier).
- **Connaître ses droits :** `GET /v1/me/info` renvoie l'identité, les quotas et limites du compte. `GET /v1/me/usage` renvoie la consommation.
- **Gérer ses clés :** `GET/POST /v1/me/keys`, `DELETE /v1/me/keys/{key}`. Créer une clé dédiée par usage/produit plutôt que réutiliser la clé personnelle.
- **Erreurs :** `401` = token absent/invalide ; `403` = droits ou quota insuffisants ; `404` = ressource/ID inexistant ; `429` = rate limit. Sur 401/403, distinguer *token manquant* de *quota dépassé* avant de réessayer.

---

## Choisir un endpoint (intention → surface)

| Objectif | Endpoint |
|----------|----------|
| Générer du texte, chat, RAG-in-one-call, tool calling | `POST /v1/chat/completions` |
| Vectoriser du texte (embeddings) | `POST /v1/embeddings` |
| Reclasser des documents par pertinence | `POST /v1/rerank` |
| Transcrire de l'audio | `POST /v1/audio/transcriptions` |
| Extraire le texte d'un PDF/image (OCR) | `POST /v1/ocr` |
| Parser un fichier en markdown structuré | `POST /v1/parse-beta` |
| Indexer un corpus puis chercher dedans (RAG) | `/v1/collections` → `/v1/documents` → `POST /v1/search` |
| Lister les modèles et leurs types | `GET /v1/models` |
| Quotas, usage, clés | `/v1/me/info`, `/v1/me/usage`, `/v1/me/keys` |
| Santé du service | `GET /health`, `GET /health/models` |

---

## Modèles

Lister en live : `GET /v1/models` (champ `data[]`, chaque entrée a un `id` et un `type`). `GET /v1/models/{model}` pour le détail d'un modèle.

Instantané du catalogue (juin 2026, **à revérifier via `GET /v1/models`** — il évolue) :

| `type` | Usage | Exemples d'`id` |
|--------|-------|-----------------|
| `text-generation` | Chat / complétion | `mistral-medium-2508`, `openai/gpt-oss-120b`, `Qwen/Qwen3-Coder-30B-A3B-Instruct` |
| `image-text-to-text` | Vision (image + texte) | `mistralai/Mistral-Small-3.2-24B-Instruct-2506`, `mistralai/Ministral-3-8B-Instruct-2512` |
| `text-embeddings-inference` | Embeddings | `BAAI/bge-m3` |
| `text-classification` | Rerank | `BAAI/bge-reranker-v2-m3` |
| `automatic-speech-recognition` | Transcription audio | `openai/whisper-large-v3` |
| `image-to-text` | OCR | `mistral-ocr-2512` |

> ⚠️ **Ne pas coder un ID de modèle en dur sans l'avoir listé** : le catalogue évolue. Récupérer l'`id` exact via `GET /v1/models` et filtrer par `type`.

---

## Endpoints

### Inférence — compatibles OpenAI

| Méthode | Chemin | Notes |
|---------|--------|-------|
| POST | `/v1/chat/completions` | `messages*`, `model*` ; options : `temperature`, `top_p`, `max_completion_tokens`, `stream`, `stop`, `n`, `seed`, `response_format`, `tools`, `tool_choice`. **Spécifique Albert :** `search: true` + `search_args` pour activer le RAG dans l'appel. |
| POST | `/v1/embeddings` | `input*` (string ou array), `model*` ; `dimensions`, `encoding_format` (`float`\|`base64`). |
| GET | `/v1/models` · `/v1/models/{model}` | Catalogue des modèles. |

### Reranking

| Méthode | Chemin | Corps |
|---------|--------|-------|
| POST | `/v1/rerank` | `query*`, `documents*` (array de strings), `model*`, `top_n`. Renvoie les documents triés par score de pertinence. |

### Audio & documents

| Méthode | Chemin | Corps | Notes |
|---------|--------|-------|-------|
| POST | `/v1/audio/transcriptions` | `multipart` : `file*`, `model*` ; `language`, `prompt`, `response_format` (`json`\|`text`\|`verbose_json`\|`diarized_json`\|`srt`\|`vtt`), `temperature` | `diarized_json` = transcription avec séparation des locuteurs. |
| POST | `/v1/ocr` | `json` : `document*` (**objet**, pas une URL nue : `{"type":"document_url","document_url":"…"}` pour un PDF, ou `{"type":"image_url","image_url":"…"}` pour une image), `model`, `pages`, `image_limit`, `include_image_base64` | OCR d'un PDF/image accessible par URL. |
| POST | `/v1/parse-beta` | `multipart` : `file*` ; `page_range`, `force_ocr` | Parsing d'un fichier uploadé en markdown structuré (bêta). |

### RAG — collections, documents, recherche

| Méthode | Chemin | Corps / notes |
|---------|--------|---------------|
| GET/POST | `/v1/collections` | POST : `name*`, `description`, `visibility` (`private`\|`public`). |
| GET/PATCH/DELETE | `/v1/collections/{collection_id}` | Lire / modifier / supprimer une collection. |
| GET/POST | `/v1/documents` | POST `multipart` : `file` (le fichier à indexer ; ou `name` pour un document sans fichier), `collection_id` (collection cible) ; chunking paramétrable (`chunk_size`, `chunk_overlap`, `separators`, `preset_separators`, `disable_chunking`). |
| GET/DELETE | `/v1/documents/{document_id}` | Métadonnées / suppression d'un document. |
| GET/POST | `/v1/documents/{document_id}/chunks` | Lister / ajouter des chunks. |
| GET/DELETE | `/v1/documents/{document_id}/chunks/{chunk_id}` | Lire / supprimer un chunk. |
| GET | `/v1/chunks/{document}` · `/v1/chunks/{document}/{chunk}` | Accès direct aux chunks. |
| POST | `/v1/search` | `query`, `collection_ids`, `document_ids`, `method` (`hybrid`\|`semantic`\|`lexical`), `limit`, `score_threshold`, `metadata_filters`. Renvoie les chunks les plus pertinents. |

### Compte & supervision

| Méthode | Chemin |
|---------|--------|
| GET/PATCH | `/v1/me/info` |
| GET | `/v1/me/usage` |
| GET/POST · DELETE | `/v1/me/keys` · `/v1/me/keys/{key}` |
| GET | `/health` · `/health/models` · `/metrics` |

---

## Workflow RAG (la valeur cœur d'Albert)

Deux approches :

**A. RAG explicite** (contrôle total) :
1. Créer une collection — `POST /v1/collections`.
2. Uploader les documents dedans — `POST /v1/documents` (chunking automatique).
3. Chercher les passages pertinents — `POST /v1/search` (`method: hybrid` par défaut conseillé).
4. Injecter les chunks récupérés dans le `messages` d'un `POST /v1/chat/completions`.

**B. RAG intégré** (une seule requête) : passer `search: true` + `search_args` (collections, méthode, limite) directement à `POST /v1/chat/completions` — Albert fait la recherche et la génération en un appel.

---

## Exemples

> Lire `ALBERT_API_KEY` depuis l'environnement ; ne jamais coller le token en clair. Vérifier les `id` de modèle via `GET /v1/models`.

### Chat (SDK OpenAI)

```python
from openai import OpenAI
import os

client = OpenAI(
    base_url="https://albert.api.etalab.gouv.fr/v1",
    api_key=os.environ["ALBERT_API_KEY"],
)

resp = client.chat.completions.create(
    model="mistral-medium-2508",  # un id de type text-generation (cf. GET /v1/models)
    messages=[{"role": "user", "content": "Explique le RGPD en une phrase."}],
    temperature=0.2,
)
print(resp.choices[0].message.content)
```

### Lister les modèles / chat (curl)

```bash
curl -s https://albert.api.etalab.gouv.fr/v1/models \
  -H "Authorization: Bearer $ALBERT_API_KEY" | jq '.data[] | {id, type}'

curl -s https://albert.api.etalab.gouv.fr/v1/chat/completions \
  -H "Authorization: Bearer $ALBERT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"mistral-medium-2508","messages":[{"role":"user","content":"Bonjour"}]}'
```

### Embeddings

```python
emb = client.embeddings.create(model="BAAI/bge-m3", input=["texte à vectoriser"])
vector = emb.data[0].embedding
```

### Transcription audio

```bash
curl -s https://albert.api.etalab.gouv.fr/v1/audio/transcriptions \
  -H "Authorization: Bearer $ALBERT_API_KEY" \
  -F "file=@reunion.mp3" \
  -F "model=openai/whisper-large-v3" \
  -F "response_format=text"
```

### RAG explicite (requests)

```python
import os, requests

BASE = "https://albert.api.etalab.gouv.fr/v1"
H = {"Authorization": f"Bearer {os.environ['ALBERT_API_KEY']}"}

# 1) collection
col = requests.post(f"{BASE}/collections", headers=H,
                    json={"name": "ma-doc", "visibility": "private"}).json()

# 2) document
with open("guide.pdf", "rb") as f:
    requests.post(f"{BASE}/documents", headers=H,
                  data={"collection_id": col["id"]},
                  files={"file": f})

# 3) recherche
hits = requests.post(f"{BASE}/search", headers=H, json={
    "query": "Quelles sont les obligations de publication ?",
    "collection_ids": [col["id"]],
    "method": "hybrid",
    "limit": 5,
}).json()

# 4) injecter les chunks dans un chat completion (cf. exemple chat)
```

---

## Albert en ligne de commande (CLI)

Albert n'a **pas de CLI dédiée** — et n'en a pas besoin pour l'usage courant : étant compatible OpenAI, **n'importe quel client CLI OpenAI fonctionne** en pointant la base URL sur Albert et la clé sur `ALBERT_API_KEY`. Deux options éprouvées :

### `llm` (Simon Willison) — recommandé pour le terminal

Enregistrer Albert comme modèle OpenAI-compatible dans `~/.config/io.datasette.llm/extra-openai-models.yaml` :

```yaml
- model_id: albert-mistral
  model_name: mistral-medium-2508   # un id renvoyé par GET /v1/models
  api_base: https://albert.api.etalab.gouv.fr/v1
  api_key_name: albert
```

Puis :

```bash
llm keys set albert            # colle le token (stocké hors du shell, jamais en clair dans l'historique)
llm -m albert-mistral "Résume le RGPD en une phrase."
cat rapport.txt | llm -m albert-mistral "Fais-en une synthèse en 3 points."
```

### CLI `openai` officielle

```bash
export OPENAI_BASE_URL="https://albert.api.etalab.gouv.fr/v1"
export OPENAI_API_KEY="$ALBERT_API_KEY"   # déjà exporté côté env, pas en dur

openai api models.list
openai api chat.completions.create -m mistral-medium-2508 -g user "Bonjour"
```

> Pour les capacités propres à Albert (RAG, OCR, parsing, gestion des collections/clés), il n'y a pas de sous-commande CLI standard : utiliser `curl` (cf. exemples ci-dessus) ou le SDK. Ne jamais passer le token en argument de commande (visible dans `ps` et l'historique) : le lire depuis l'environnement ou un gestionnaire de clés (`llm keys`).

---

## Garanties & doctrine

- **Hébergement SecNumCloud** (Outscale) : qualification ANSSI.
- **Pas de rétention des conversations**, pas d'envoi de données sur Internet ouvert.
- Adapté aux usages avec données internes de l'administration, dans le respect du cadre RGPD applicable.

---

## Maintenance de cette skill

La source d'autorité est l'OpenAPI live (`/openapi.json`). Pour vérifier que cette skill n'a pas dérivé de la spec :

```bash
python3 bin/check_drift.py            # compare la spec live au snapshot committé
python3 bin/check_drift.py --update   # régénère le snapshot après mise à jour de SKILL.md
```

Le script (sans dépendance) compare version, endpoints et enums au fichier `openapi.snapshot.json`. En cas d'écart il sort en code 1 et liste les différences — signal qu'il faut relire et corriger ce fichier. À lancer périodiquement ou avant toute revue ; idéalement adossé à une GitHub Action qui ouvre une issue quand la version d'Albert bouge.

---

## Références

- **Doc Albert API :** https://doc.incubateur.net/alliance/albert-api
- **OpenAPI (autoritatif) :** https://albert.api.etalab.gouv.fr/openapi.json
- **OpenGateLLM (commun numérique sous-jacent) :** notebooks et tutoriels RAG/OCR.
- **Assistant IA** (interface chat grand public adossée à Albert) : https://assistant.numerique.gouv.fr/
