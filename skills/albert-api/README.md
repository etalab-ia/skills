# albert-api

Skill pour assistants de code IA — référence consolidée d'[Albert API](https://albert.api.etalab.gouv.fr), l'API d'inférence et d'IA générative interministérielle de l'État (commun numérique [OpenGateLLM](https://doc.incubateur.net/alliance/albert-api), hébergement SecNumCloud).

## Ce que fait cette skill

Quand elle est activée, l'assistant IA sait :

- **Inférence compatible OpenAI** — Appeler `chat/completions` et `embeddings` en réutilisant le SDK `openai` (changement de `base_url`), faire du reranking
- **Audio & documents** — Transcrire de l'audio (avec diarisation), faire de l'OCR sur PDF/images, parser des fichiers en markdown
- **RAG souverain** — Créer des collections, indexer des documents, chercher (sémantique / hybride / lexical) et brancher le résultat sur un chat completion
- **Compte & quotas** — Connaître ses droits, gérer ses clés API, suivre sa consommation

Le tout fondé sur la spec OpenAPI de l'API (qui fait autorité), avec les bonnes pratiques de sécurité (ne jamais exposer le token).

## Contenu

| Fichier | Description |
|---------|-------------|
| [`SKILL.md`](SKILL.md) | Référence consolidée de l'API (auth, endpoints, workflow RAG, exemples) |

## Installation

```bash
# Avec Vercel Skills CLI (recommandé)
npx skills add etalab-ia/skills --skill albert-api

# Claude Code
npx skills add etalab-ia/skills --skill albert-api -a claude-code

# OpenCode
npx skills add etalab-ia/skills --skill albert-api -a opencode
```

## Exemples d'utilisation

Une fois la skill installée, l'assistant IA peut répondre à des demandes comme :

- *"Appelle Albert pour résumer ce texte"*
- *"Crée un script Python qui utilise les embeddings d'Albert"*
- *"Indexe ces PDF dans une collection Albert et fais une recherche dessus"*
- *"Transcris ce fichier audio avec Albert"*
- *"Quels modèles sont disponibles sur Albert API ?"*

## Prérequis

Un token Albert API (`Authorization: Bearer …`), réservé aux agents de la fonction publique. Demande d'accès via la [documentation Albert API](https://doc.incubateur.net/alliance/albert-api).

## Liens utiles

- [Documentation Albert API](https://doc.incubateur.net/alliance/albert-api)
- [Spec OpenAPI](https://albert.api.etalab.gouv.fr/openapi.json)
- [Assistant IA](https://assistant.numerique.gouv.fr/) — interface chat adossée à Albert

## Licence

MIT
