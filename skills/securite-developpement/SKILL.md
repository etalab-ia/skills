---
name: securite-developpement
description: "Règles essentielles de sécurité pour le développement d'applications de l'État, générées par la DINUM en s'appuyant sur les guides produits par l'ANSSI. 12 règles couvrant TLS, secrets, authentification, headers, dépendances, entrées, logs et durcissement. Utiliser cette skill quand l'utilisateur développe une application web, une API, ou tout service exposé, quand il mentionne la sécurité, l'ANSSI, le durcissement, ou quand on configure un serveur, un reverse proxy ou un pipeline CI/CD."
---

# Sécurité — Règles essentielles pour le développement

Règles de sécurité pour le développement d'applications de l'État, générées par la DINUM en s'appuyant sur le [guide d'hygiène informatique ANSSI](https://cyber.gouv.fr/publications/guide-dhygiene-informatique) et des [recommandations TLS](https://cyber.gouv.fr/publications/recommandations-de-securite-relatives-tls).

Source : https://cyber.gouv.fr/reglementation/cybersecurite-systemes-dinformation/

---

## Workflow d'audit

1. **Analyser le projet** (code source, configuration, infrastructure, CI/CD)
2. **Parcourir les 12 domaines** de la checklist détaillée dans [`references/checklist.md`](references/checklist.md)
3. **Pour chaque règle**, attribuer un statut :
   - **OK** — Règle respectée
   - **KO** — Règle non respectée (identifier le problème et le risque)
   - **NA** — Non applicable (justifier)
   - **Partiel** — Partiellement respectée (préciser ce qui manque)
4. **Qualifier l'exploitabilité de chaque KO** : distinguer une faille **exploitable** (activable en l'état → chemin d'attaque réel) d'une **bonne pratique manquante** (défense en profondeur, sans exploitation directe). Cette qualification alimente la priorité.
5. **Valider les non-conformités** : avant de finaliser, re-vérifier chaque KO contre le code et la configuration réels. Écarter les faux positifs, ou requalifier le statut/l'exploitabilité si le constat ne tient pas. Ne conserver que les constats étayés par une preuve concrète (fichier, ligne, réglage).
6. **Produire le rapport structuré** selon le format défini dans [`references/rapport.md`](references/rapport.md)
7. **Exporter le rapport** : écrire le rapport dans un fichier Markdown ET l'afficher dans la conversation (règles d'export dans [`references/rapport.md`](references/rapport.md)). Une sortie structurée JSON optionnelle est disponible au format `securite-developpement-AAAA-MM-JJ.json` (schéma : [`references/findings-schema.json`](references/findings-schema.json)).

---

## Références

| Fichier | Contenu |
|---------|---------|
| [`references/checklist.md`](references/checklist.md) | Les 12 domaines de sécurité détaillés (règles à vérifier) |
| [`references/rapport.md`](references/rapport.md) | Format du rapport, grille de priorités, export, sortie JSON optionnelle |
| [`references/findings-schema.json`](references/findings-schema.json) | JSON Schema de la sortie structurée optionnelle (`securite-developpement-AAAA-MM-JJ.json`) |
