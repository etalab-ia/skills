# anssi-guides

Skill d'aiguillage vers les guides publiés par l'ANSSI : trouver le bon guide dans le catalogue (126 guides), le consulter à la demande et répondre en citant la source exacte.

## Positionnement

Cette skill **localise et cite, elle ne pré-digère pas**. Elle maintient le catalogue (titres, dates, collections, URLs), pas une synthèse des règles — la consultation du contenu se fait à la demande, sur la page vitrine ou le PDF du guide concerné.

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
└── references/
    └── catalogue.md          # Les 126 guides + méthode de re-scan
```

## Maintenance

Le catalogue est un instantané daté (date de scan en tête de `catalogue.md`). La méthode de re-scan, documentée en fin de fichier, permet de détecter publications et révisions ; toute révision d'un guide ★ doit être signalée pour que `securite-developpement` rejoue son extraction (`references/sources.md`).

Les PDF ne sont pas versionnés dans ce dépôt : la skill cite les guides, elle ne les redistribue pas.

## Installation

Copier le répertoire dans le dossier des skills de votre outil :

```bash
# Claude Code
cp -r skills/anssi-guides ~/.claude/skills/

# OpenCode
cp -r skills/anssi-guides ~/.config/opencode/skills/
```
