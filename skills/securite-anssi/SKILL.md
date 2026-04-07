---
name: securite-anssi
description: "Règles essentielles de sécurité ANSSI pour le développement d'applications de l'État. 12 règles couvrant TLS, secrets, authentification, headers, dépendances, entrées, logs et durcissement. Utiliser cette skill quand l'utilisateur développe une application web, une API, ou tout service exposé, quand il mentionne la sécurité, l'ANSSI, le durcissement, ou quand on configure un serveur, un reverse proxy ou un pipeline CI/CD."
---

# Sécurité ANSSI — Règles essentielles

Règles de sécurité pour le développement d'applications de l'État, issues du [guide d'hygiène informatique ANSSI](https://cyber.gouv.fr/publications/guide-dhygiene-informatique) et des [recommandations TLS](https://cyber.gouv.fr/publications/recommandations-de-securite-relatives-tls).

Source : https://cyber.gouv.fr/reglementation/cybersecurite-systemes-dinformation/

---

## Workflow d'audit

1. **Analyser le projet** (code source, configuration, infrastructure, CI/CD)
2. **Parcourir les 12 domaines** de la checklist ci-dessous
3. **Pour chaque règle**, attribuer un statut :
   - **OK** — Règle respectée
   - **KO** — Règle non respectée (identifier le problème et le risque)
   - **NA** — Non applicable (justifier)
   - **Partiel** — Partiellement respectée (préciser ce qui manque)
4. **Produire le rapport structuré** selon le format défini en fin de document
5. **Exporter le rapport** : écrire le rapport dans un fichier Markdown ET l'afficher dans la conversation

---

## Checklist par domaine

### 1. TLS / HTTPS

- [ ] HTTPS obligatoire sur tous les échanges (pas de HTTP en production)
- [ ] TLS 1.2 minimum, TLS 1.3 recommandé
- [ ] Certificats valides et renouvelés avant expiration
- [ ] Désactiver les suites de chiffrement faibles (RC4, DES, 3DES, MD5)
- [ ] Header `Strict-Transport-Security` (HSTS) avec `max-age` ≥ 1 an

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

### 2. Gestion des secrets

- [ ] **Jamais** de secret dans le code source (clés API, mots de passe, tokens)
- [ ] Utiliser des variables d'environnement ou un gestionnaire de secrets (Vault, AWS Secrets Manager)
- [ ] Fichiers `.env` dans `.gitignore`
- [ ] Rotation régulière des secrets (tous les 90 jours minimum)
- [ ] Révoquer immédiatement tout secret exposé accidentellement

### 3. Authentification et contrôle d'accès

- [ ] Authentification multi-facteurs (MFA) pour les accès administrateurs
- [ ] Mots de passe : 12 caractères minimum, pas de contrainte de complexité artificielle
- [ ] Verrouillage temporaire après 5 tentatives échouées
- [ ] Sessions : durée limitée, invalidation côté serveur à la déconnexion
- [ ] Principe du moindre privilège : chaque composant n'a accès qu'à ce dont il a besoin

### 4. Headers de sécurité HTTP

- [ ] `Content-Security-Policy` : restreindre les sources de scripts, styles, images
- [ ] `X-Content-Type-Options: nosniff`
- [ ] `X-Frame-Options: DENY` (ou `SAMEORIGIN` si iframe nécessaire)
- [ ] `Referrer-Policy: strict-origin-when-cross-origin`
- [ ] `Permissions-Policy` : désactiver les API non utilisées (camera, microphone, geolocation)

```
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: strict-origin-when-cross-origin
```

### 5. Validation des entrées

- [ ] Valider **toutes** les entrées côté serveur (ne jamais faire confiance au client)
- [ ] Utiliser des schémas de validation (Zod, Joi, Pydantic)
- [ ] Échapper les sorties HTML pour prévenir les XSS
- [ ] Requêtes SQL paramétrées (pas de concaténation de chaînes)
- [ ] Limiter la taille des requêtes (body, upload, query strings)

### 6. Gestion des dépendances

- [ ] Auditer les dépendances régulièrement (`npm audit`, `pip audit`, `trivy`)
- [ ] Mettre à jour les dépendances avec des vulnérabilités connues (CVE)
- [ ] Utiliser un fichier de lock (package-lock.json, poetry.lock)
- [ ] Minimiser le nombre de dépendances directes
- [ ] Scanner les images Docker (`trivy image`)

### 7. Journalisation et monitoring

- [ ] Logger les événements de sécurité : authentifications, erreurs d'accès, modifications critiques
- [ ] **Jamais** de données sensibles dans les logs (mots de passe, tokens, données personnelles)
- [ ] Horodatage UTC sur tous les logs
- [ ] Centraliser les logs (ELK, Loki, CloudWatch)
- [ ] Alertes sur les événements anormaux (pics d'erreurs 401/403, tentatives brute force)

### 8. Protection des API

- [ ] Authentification sur tous les endpoints (sauf santé/métadonnées publiques)
- [ ] Rate limiting pour prévenir les abus
- [ ] Pagination obligatoire sur les endpoints de liste
- [ ] Ne pas exposer de détails techniques dans les messages d'erreur en production
- [ ] Versionner les API (`/v1/`, `/v2/`)

### 9. Sécurité des conteneurs et du déploiement

- [ ] Images Docker basées sur des images minimales (Alpine, distroless)
- [ ] Ne pas exécuter les processus en root dans les conteneurs
- [ ] Scanner les images avant déploiement
- [ ] Séparer les environnements (dev, staging, prod) avec des accès distincts
- [ ] Health checks et readiness probes configurés

### 10. Sécurité du poste de développement

- [ ] Chiffrement du disque dur activé (FileVault, LUKS)
- [ ] Verrouillage automatique après 5 minutes d'inactivité
- [ ] VPN pour les accès aux ressources internes
- [ ] Pas de compte administrateur pour l'usage quotidien

### 11. Sauvegarde et continuité

- [ ] Sauvegardes régulières des données et configurations critiques
- [ ] Tester la restauration des sauvegardes périodiquement
- [ ] Documenter la procédure de reprise d'activité

### 12. Gestion des incidents

- [ ] Procédure de signalement des incidents de sécurité documentée
- [ ] Contact CERT ministériel identifié
- [ ] Capacité à révoquer des accès et rotater des secrets en urgence

---

## Format du rapport d'audit

```markdown
## Audit Sécurité ANSSI — Rapport de conformité

**Date :** AAAA-MM-JJ
**Périmètre audité :** [description du projet / service / composant]
**Résultat global :** X/Y règles conformes (Z% conforme)
(X conformes, X non conformes, X partielles, X non applicables)

---

### Tableau de synthèse

| # | Domaine | Statut | Détail |
|---|---------|--------|--------|
| 1 | TLS / HTTPS | OK / KO / Partiel / NA | résumé en une ligne |
| 2 | Gestion des secrets | OK / KO / Partiel / NA | résumé en une ligne |
| 3 | Authentification et contrôle d'accès | OK / KO / Partiel / NA | résumé en une ligne |
| 4 | Headers de sécurité HTTP | OK / KO / Partiel / NA | résumé en une ligne |
| 5 | Validation des entrées | OK / KO / Partiel / NA | résumé en une ligne |
| 6 | Gestion des dépendances | OK / KO / Partiel / NA | résumé en une ligne |
| 7 | Journalisation et monitoring | OK / KO / Partiel / NA | résumé en une ligne |
| 8 | Protection des API | OK / KO / Partiel / NA | résumé en une ligne |
| 9 | Sécurité des conteneurs et du déploiement | OK / KO / Partiel / NA | résumé en une ligne |
| 10 | Sécurité du poste de développement | OK / KO / Partiel / NA | résumé en une ligne |
| 11 | Sauvegarde et continuité | OK / KO / Partiel / NA | résumé en une ligne |
| 12 | Gestion des incidents | OK / KO / Partiel / NA | résumé en une ligne |

---

### Non-conformités détectées

**[KO] Domaine {#} — {Nom du domaine}**
- **Règle concernée :** description de la règle non respectée
- **Constat :** ce qui a été observé dans le code / la configuration
- **Risque :** impact sécurité si non corrigé (ex : fuite de données, compromission)
- **Correction :** action concrète à mener
- **Priorité :** 🔴 Critique / 🟠 Élevée / 🟡 Modérée

### Conformités partielles

**[Partiel] Domaine {#} — {Nom du domaine}**
- **Règles respectées :** liste des points OK
- **Règles manquantes :** liste des points restants à traiter
- **Correction :** actions à mener pour atteindre la conformité complète

---

### Domaines conformes

{liste compacte des domaines OK}

### Domaines non applicables

- **Domaine {#}** — {justification courte}
```

## Grille de priorités

| Priorité | Définition | Exemples |
|----------|------------|---------|
| 🔴 **Critique** | Vulnérabilité exploitable, risque immédiat de compromission | Secret dans le code source, pas de TLS, injection SQL possible |
| 🟠 **Élevée** | Faiblesse significative, exploitation possible sous conditions | Headers de sécurité manquants, pas de rate limiting, pas de MFA admin |
| 🟡 **Modérée** | Bonne pratique non respectée, risque limité | Logs non centralisés, pas de scan d'images Docker, rotation des secrets non planifiée |

## Export du rapport

Après avoir produit le rapport, **toujours** :

1. Créer le dossier `audits/` à la racine du projet s'il n'existe pas
2. Écrire le rapport complet dans `audits/securite-anssi-AAAA-MM-JJ.md` (date du jour, format ISO)
3. Afficher également le rapport dans la conversation

Si un fichier du même nom existe déjà, ajouter un suffixe incrémental : `securite-anssi-2026-03-26-2.md`.

> Exemple : `audits/securite-anssi-2026-03-26.md`
