# anssi-guides

Skill d'aiguillage vers les guides publiés par l'ANSSI : interroger le catalogue français via l'API MesServicesCyber, consulter le bon document et répondre en citant la source exacte.

## Positionnement

Cette skill **localise et cite, elle ne pré-digère pas**. Elle interroge les métadonnées structurées de l'API (`collections`, `besoins`, `thematique`, `documents`), pas une synthèse des règles — la consultation du contenu se fait à la demande dans les documents indiqués par l'API.

Elle est complémentaire de [`securite-developpement`](../securite-developpement/) :

| Question | Skill |
|---|---|
| « Comment stocker les mots de passe ? », « Audite mon API », « Configure nginx en TLS » | `securite-developpement` — 13 guides ANSSI digérés règle par règle, avec traçabilité et valeurs chiffrées |
| « Existe-t-il un guide ANSSI sur les pare-feux ? », « Que recommande l'ANSSI sur la remédiation Active Directory ? », « Que dit l'ANSSI sur l'IA générative ? » | `anssi-guides` — recherche dans tout le catalogue, consultation et citation |

Les 13 guides couverts par `securite-developpement` sont marqués ★ dans le catalogue : pour ces sujets en contexte de développement, la skill aiguille vers le référentiel existant plutôt que de relire les PDF.

## Contenu

```
anssi-guides/
├── SKILL.md                  # Workflow : chercher, aiguiller, consulter, citer
├── scripts/
│   ├── generate-catalogue.sh # Génération et validation depuis l'API
│   ├── test-generate-catalogue.sh
│   └── tracked-guide-ids.json
└── references/
    └── catalogue.md          # Instantané des guides français + méthode de re-scan
```

## Maintenance

Le catalogue est un instantané daté (date de scan en tête de `catalogue.md`) généré depuis `https://messervices.cyber.gouv.fr/api/guides` :

```bash
skills/anssi-guides/scripts/generate-catalogue.sh > skills/anssi-guides/references/catalogue.md
skills/anssi-guides/scripts/test-generate-catalogue.sh
```

Le générateur filtre les fiches françaises, valide les champs attendus et conserve le marquage ★ des 13 fiches suivies par `securite-developpement`. Toute révision d'une fiche ★ doit être signalée pour que cette skill rejoue son extraction (`references/sources.md`).

Les PDF ne sont pas versionnés dans ce dépôt : la skill cite les guides, elle ne les redistribue pas.

## Installation

Copier le répertoire dans le dossier des skills de votre outil :

```bash
# Claude Code
cp -r skills/anssi-guides ~/.claude/skills/

# OpenCode
cp -r skills/anssi-guides ~/.config/opencode/skills/
```
