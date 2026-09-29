---
name: anssi-guides
description: "Catalogue français des guides et recommandations publiés par l'ANSSI, interrogé via l'API MesServicesCyber pour trouver le bon guide et répondre à une question de sécurité en citant sa source. Utiliser cette skill quand l'utilisateur cherche un guide ou une publication de l'ANSSI, demande « que dit / que recommande l'ANSSI sur… », « existe-t-il un guide sur… », ou pose une question de sécurité hors du développement d'application : architecture réseau, pare-feu, DNS, Active Directory, Wi-Fi, virtualisation, nomadisme, systèmes industriels, gestion de crise cyber, remédiation, homologation, EBIOS, IA générative, cryptographie post-quantique. Pour la sécurité du développement d'une application (code, serveur, base de données, CI/CD), utiliser plutôt la skill securite-developpement."
---

# Guides ANSSI — trouver et consulter la bonne source

Cette skill aiguille vers les guides publiés par l'ANSSI et les consulte à la demande. Elle **localise et cite, elle ne pré-digère pas** : le référentiel de règles applicables au développement, lui, est la skill [`securite-developpement`](../securite-developpement/SKILL.md).

## Workflow

1. **Interroger l'API canonique** — `https://messervices.cyber.gouv.fr/api/guides`. Filtrer impérativement `.langue == "FR"`, puis chercher les mots-clés et synonymes du sujet dans `nom`, `description`, `thematique`, `collections` et `besoins` (ex. « SSO » → OpenID Connect ; « conteneurs » → Docker, cloisonnement, virtualisation). Les champs `collections` et `besoins` permettent aussi de restreindre la recherche par public ou objectif (`ETRE_SENSIBILISE`, `REAGIR`, `SECURISER`, `SE_FORMER`). Utiliser [`references/catalogue.md`](references/catalogue.md) comme instantané hors ligne, pas comme source plus fraîche que l'API.

2. **Aiguiller vers `securite-developpement` si la question relève du développement.** Les guides marqués ★ dans le catalogue y sont déjà digérés règle par règle, avec leur traçabilité (`[TLS R3]`, `[ESS-BDD]`…) et les valeurs chiffrées exactes. Ne pas refaire ce travail depuis les PDF. Aiguiller uniquement sur les guides ★ : un sujet pertinent pour le développement mais hors ★ (ex. OpenID Connect, conteneurs Docker) reste traité par le workflow ci-dessous (catalogue → consultation → citation), même si `securite-developpement` couvre partiellement le domaine avec une règle `[DINUM]`.

3. **Présenter le ou les guides pertinents** : titre exact (`nom`), date de mise à jour du catalogue (`dateMiseAJour`), collections, besoins, thématique et URL de la fiche (`https://messervices.cyber.gouv.fr/guides/<id>`). S'il existe plusieurs guides sur le sujet, les donner du plus récent au plus ancien et signaler les recouvrements (ex. TLS 2020 et Transition post-quantique de TLS 1.3 2026).

4. **Consulter le contenu si la question le demande** :
   - Pour une vue d'ensemble : utiliser `description` dans la réponse de l'API (le champ contient du HTML, à convertir en texte avant citation).
   - Pour une question précise : prendre les URLs exactes dans `documents[].url`, télécharger le ou les PDF pertinents, puis `pdftotext -layout guide.pdf guide.txt` et aller à la liste récapitulative des recommandations, généralement en fin de document. Ne pas reconstruire une URL de document ni parser la page HTML de la fiche.
   - **Toujours citer** : nom du guide, version si connue, identifiant de la recommandation (`R12`, `M5`…) quand le guide en a. Ne jamais attribuer à l'ANSSI une recommandation qui ne figure pas dans le texte consulté.

5. **Signaler la fraîcheur** : distinguer `dateMiseAJour` (métadonnée de la fiche) de la version imprimée dans le document. Si la réponse doit être garantie à jour, interroger l'API pendant la tâche et vérifier la version dans le PDF ; la date de scan de l'instantané figure en tête de [`references/catalogue.md`](references/catalogue.md).

## Pièges connus

- La date affichée au catalogue est celle de **mise en ligne**, pas celle de la version du document. Version et référence (ANSSI-PA/PG) ne figurent que dans le PDF.
- Certains sujets ont plusieurs guides d'époques très différentes (DDoS : 2015 et 2024 ; Active Directory : 2014, 2022, 2023-24 ; virtualisation : 2012, 2016, 2017, 2024) — toujours vérifier la date avant de citer.
- Une même page vitrine peut recouvrir plusieurs documents (« Mécanismes cryptographiques » : deux guides distincts, 2021 et 2026).
- Les « Essentiels » et « Fondamentaux » sont des fiches de sensibilisation de 1-2 pages, pas des guides prescriptifs : le dire quand on les cite.

## Références

| Fichier | Contenu |
|---------|---------|
| [`references/catalogue.md`](references/catalogue.md) | Instantané généré des guides français : titre, date, collection, besoin, thématique et URL — plus la méthode de re-scan |
| [`scripts/generate-catalogue.sh`](scripts/generate-catalogue.sh) | Génération et validation du catalogue depuis l'API JSON |
