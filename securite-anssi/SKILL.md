---
name: securite-anssi
description: "Règles essentielles de sécurité ANSSI pour le développement d'applications de l'État. 12 règles couvrant TLS, secrets, authentification, headers, dépendances, entrées, logs et durcissement. Utiliser cette skill quand l'utilisateur développe une application web, une API, ou tout service exposé, quand il mentionne la sécurité, l'ANSSI, le durcissement, ou quand on configure un serveur, un reverse proxy ou un pipeline CI/CD."
---

# Sécurité ANSSI — Règles essentielles

Règles de sécurité pour le développement d'applications de l'État, issues du [guide d'hygiène informatique ANSSI](https://cyber.gouv.fr/publications/guide-dhygiene-informatique) et des [recommandations TLS](https://cyber.gouv.fr/publications/recommandations-de-securite-relatives-tls).

Source : https://cyber.gouv.fr/reglementation/cybersecurite-systemes-dinformation/

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
