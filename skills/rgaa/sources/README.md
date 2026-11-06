# Sources officielles du RGAA 4.1.2

`criteres.json` et `glossaire.json` sont des copies non modifiées des fichiers publiés par la DINUM dans le dépôt [DISIC/accessibilite.numerique.gouv.fr](https://github.com/DISIC/accessibilite.numerique.gouv.fr/tree/main/RGAA), sous [Licence Ouverte 2.0](https://www.etalab.gouv.fr/licence-ouverte-open-licence/).

- Version copiée : commit [`95d5ef3`](https://github.com/DISIC/accessibilite.numerique.gouv.fr/commit/95d5ef33df9efe7c862da02ea98c6b8c02909007) du 7 janvier 2026, dernier commit à modifier `RGAA/criteres.json` à la date de copie (5 novembre 2026).
- L’assistant ne lit pas ces fichiers : `scripts/officiel.py` en tire les blocs « Texte officiel » de `references/criteres-*.md` et `references/glossaire.md`.

Pour suivre une révision officielle : remplacer les deux fichiers, mettre à jour le commit ci-dessus, lancer `python3 scripts/officiel.py --write`, puis relire le diff des références.
