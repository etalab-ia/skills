---
name: anssi-guides
description: "Catalogue des 126 guides et recommandations publiés par l'ANSSI, pour trouver le bon guide et répondre à une question de sécurité en citant sa source. Utiliser cette skill quand l'utilisateur cherche un guide ou une publication de l'ANSSI, demande « que dit / que recommande l'ANSSI sur… », « existe-t-il un guide sur… », ou pose une question de sécurité hors du développement d'application : architecture réseau, pare-feu, DNS, Active Directory, Wi-Fi, virtualisation, nomadisme, systèmes industriels, gestion de crise cyber, remédiation, homologation, EBIOS, IA générative, cryptographie post-quantique. Pour la sécurité du développement d'une application (code, serveur, base de données, CI/CD), utiliser plutôt la skill securite-developpement."
---

# Guides ANSSI — trouver et consulter la bonne source

Cette skill aiguille vers les guides publiés par l'ANSSI et les consulte à la demande. Elle **localise et cite, elle ne pré-digère pas** : le référentiel de règles applicables au développement, lui, est la skill [`securite-developpement`](../securite-developpement/SKILL.md).

## Workflow

1. **Chercher dans le catalogue** — [`references/catalogue.md`](references/catalogue.md) : 126 guides — 125 en français, 1 disponible uniquement en anglais — (titre, date, collection, thématique, URL). Chercher par mots-clés du sujet, y compris les synonymes (ex. « SSO » → OpenID Connect ; « conteneurs » → Docker, cloisonnement, virtualisation).

2. **Aiguiller vers `securite-developpement` si la question relève du développement.** Les guides marqués ★ dans le catalogue y sont déjà digérés règle par règle, avec leur traçabilité (`[TLS R3]`, `[ESS-BDD]`…) et les valeurs chiffrées exactes. Ne pas refaire ce travail depuis les PDF.

3. **Présenter le ou les guides pertinents** : titre exact, date de publication, collection, URL. S'il existe plusieurs guides sur le sujet, les donner du plus récent au plus ancien et signaler les recouvrements (ex. TLS 2020 et Transition post-quantique de TLS 1.3 2026).

4. **Consulter le contenu si la question le demande** :
   - Pour une vue d'ensemble : récupérer la page vitrine (WebFetch de l'URL du catalogue).
   - Pour une question précise : télécharger le PDF depuis la page vitrine, puis `pdftotext -layout guide.pdf guide.txt` et aller à la liste récapitulative des recommandations, généralement en fin de document.
   - **Toujours citer** : nom du guide, version si connue, identifiant de la recommandation (`R12`, `M5`…) quand le guide en a. Ne jamais attribuer à l'ANSSI une recommandation qui ne figure pas dans le texte consulté.

5. **Signaler la fraîcheur** : le catalogue a une date de scan (en tête de [`references/catalogue.md`](references/catalogue.md)). Si la réponse doit être garantie à jour, ou si le guide semble ancien, rejouer le re-scan (méthode en fin de catalogue) ou vérifier la page vitrine.

## Pièges connus

- La date affichée au catalogue est celle de **mise en ligne**, pas celle de la version du document. Version et référence (ANSSI-PA/PG) ne figurent que dans le PDF.
- Certains sujets ont plusieurs guides d'époques très différentes (DDoS : 2015 et 2024 ; Active Directory : 2014, 2022, 2023-24 ; virtualisation : 2012, 2016, 2017, 2024) — toujours vérifier la date avant de citer.
- Une même page vitrine peut recouvrir plusieurs documents (« Mécanismes cryptographiques » : deux guides distincts, 2021 et 2026).
- Les « Essentiels » et « Fondamentaux » sont des fiches de sensibilisation de 1-2 pages, pas des guides prescriptifs : le dire quand on les cite.

## Références

| Fichier | Contenu |
|---------|---------|
| [`references/catalogue.md`](references/catalogue.md) | Les 126 guides : titre, date, collection, thématique, URL — plus la méthode de re-scan |
