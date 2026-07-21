# Valeurs chiffrées de référence

Les valeurs que l'assistant doit **citer, jamais réinventer**, en mode conseil comme en mode audit. Chacune est tracée jusqu'à sa recommandation ANSSI (voir [`sources.md`](sources.md)).

**Versions utilisées — extraction du 2026-07-20 :** TLS v1.2 (2020) · Crypto PA-079 v1.0 (2021) et **PG-083 v3.00 (20/03/2026)** · MFA PG-078 v2.0 (2021) · Site web PA-009 v2.0 (2021) · Journalisation PA-012 v2.0 (2022).

> **Règle de préséance.** En cryptographie, **PG-083 v3.00 (2026) prévaut** sur tout autre guide : il est le plus récent et intègre la menace quantique. Le guide TLS date de 2020, le guide de sélection d'algorithmes de 2021.

---

## 1. TLS

### Versions de protocole — `[TLS R3, R4]`

| Version | Statut |
|---------|--------|
| **TLS 1.3** | Doit être prise en charge et **privilégiée** |
| **TLS 1.2** | Acceptée, sous condition de suivre le guide |
| TLS 1.1, TLS 1.0, SSLv3, SSLv2 | **À proscrire** — privilégier des composants qui ne les compilent même pas |

### Suites cryptographiques recommandées — `[TLS R9, R10, R12]`

**TLS 1.3**
```
TLS_AES_256_GCM_SHA384          (0x1302)
TLS_AES_128_GCM_SHA256          (0x1301)
TLS_AES_128_CCM_SHA256          (0x1304)
TLS_CHACHA20_POLY1305_SHA256    (0x1303)
```

**TLS 1.2 — certificat ECDSA**
```
TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384        (0xC02C)
TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256        (0xC02B)
TLS_ECDHE_ECDSA_WITH_AES_256_CCM               (0xC0AD)
TLS_ECDHE_ECDSA_WITH_AES_128_CCM               (0xC0AC)
TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256  (0xCCA9)
```

**TLS 1.2 — certificat RSA**
```
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384          (0xC030)
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256          (0xC02F)
TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256    (0xCCA8)
```

Toute suite en mode CBC n'est tolérée qu'**en conjonction avec l'extension `encrypt_then_mac`** — `[TLS R10-]`.

### Échange de clés — `[TLS R6, R7, R7-]`

- **Confidentialité persistante (PFS) obligatoire** : ECDHE, ou à défaut DHE.
- Courbes privilégiées : `secp256r1`, `secp384r1`, `secp521r1`. Acceptables : `x25519`, `x448`, `brainpoolP256r1`, `brainpoolP384r1`, `brainpoolP512r1`.
- DHE (dégradé) : groupes **≥ 2048 bits**, **≥ 3072 bits** si la protection doit dépasser 2030.

### Certificats — `[TLS R24 à R33]`

| Paramètre | Valeur |
|-----------|--------|
| Signature | Famille **SHA-2** obligatoire |
| Durée de validité | **≤ 3 ans**, et **≤ 825 jours** pour tout certificat émis après le 01/03/2018 |
| Clé RSA | **≥ 2048 bits** (guide TLS) — mais voir §2, PG-083 impose 3072 à partir de 2031 |
| Exposant public RSA | **≥ 2¹⁶ + 1** (65537) |
| Clé ECDSA | **≥ 256 bits** |
| Numéro de série | Entier positif, **≤ 20 octets**, non prédictible |
| `KeyUsage` | Présent et **critique**. Serveur : `digitalSignature` et/ou `keyEncipherment`. Client : `digitalSignature`. Rien d'autre |
| `ExtendedKeyUsage` | Présent et **non-critique**. Serveur : `id-kp-serverAuth` seul. Client : `id-kp-clientAuth` seul |
| `SubjectAlternativeName` | Présent, non-critique, au moins un `dNSName` = FQDN du service |
| Révocation | Au moins une extension parmi **CRLDP** et **AIA**. Agrafage OCSP préféré aux CRL. Comportement **hard-fail** `[TLS R37]` |

### Divers TLS

- **Tickets de session : durée de vie ≤ 24 heures** — `[TLS R20]`
- **Compression TLS : proscrite** — `[TLS R19]`
- **0-RTT / `early_data`** : ne pas émettre côté client, refuser côté serveur (`max_early_data_size` à 0) — `[TLS R23]`
- HSTS : `Strict-Transport-Security: max-age=31536000; includeSubDomains;` — `[WEB R2]`

### Proscrits

RC4, MD5, SHA-1, DES, Triple-DES, échange de clé RSA (`RSAES-PKCS1-v1_5`), Diffie–Hellman statique, eTLS, certificats à clé publique brute (RFC 7250), compression Deflate.

---

## 2. Cryptographie

### Niveaux de sécurité et horizon

- Mécanisme **recommandé (R)** : niveau de sécurité **≥ 128 bits** contre les attaques hors ligne.
- Mécanisme **obsolescent (O)** : ≥ 100 bits, toléré à court terme, à abandonner.
- **`CRYPTO-DIM RecoSécuLongTerme`** : « En cas d'utilisation prévue **au-delà du 1er janvier 2030**, ou de risque d'attaque rétroactive, il est recommandé de viser une **sécurité post-quantique**. »

### Symétrique — `[CRYPTO R1, R2]`, `[CRYPTO-DIM RègleTailleCléSym]`

| Élément | Valeur |
|---------|--------|
| Algorithme par bloc | **AES** — clés 128 / 192 / 256 bits |
| Algorithme par flot | **ChaCha20** |
| Taille de clé minimale | **≥ 128 bits** — **≥ 192 bits** en visée post-quantique |
| Taille de bloc minimale | **≥ 128 bits** (exclut Triple-DES, bloc 64 bits) |
| Volume par clé AES | jusqu'à **2⁵⁹ blocs** |

### Chiffrement authentifié — `[CRYPTO R4, R12]`

**Recommandés** : `Encrypt-then-MAC`, **GCM**, **CCM**, **EAX**, **ChaCha20-Poly1305**.
**Obsolescents** : `MAC-then-Encrypt`, `Encrypt-and-MAC`.

Les modes de chiffrement **seul** (CTR, OFB, CBC, CFB, CBC-CS) **ne doivent pas être utilisés seuls** — uniquement comme brique d'un mode authentifié — `[CRYPTO R4, R5]`.

**Contraintes GCM, souvent manquées** :
- L'IV doit faire **exactement 96 bits**, construit selon la méthode déterministe de SP800-38D §8.2.1 — `[CRYPTO note 4.5.d]`
- Réutiliser un IV avec GCM **casse aussi l'intégrité**, pas seulement la confidentialité — `[CRYPTO note 4.5.c]`
- Clair limité à **2³² − 2 blocs** par couple (clé, IV) — `[CRYPTO note 4.5.e]`
- **MAC d'au moins 128 bits, aucune troncature possible** — `[CRYPTO note 4.5.f]`

Chiffrement de disque : **XTS** recommandé ; CBC-ESSIV obsolescent — `[CRYPTO R6]`.

### Hachage — `[CRYPTO R3]`

**Recommandés** : SHA-2 et SHA-3 avec **sortie ≥ 256 bits** — SHA-256, SHA-384, SHA-512, SHA-512/256, SHA3-256/384/512.

**SHA-1 est explicitement « proscrite pour une utilisation générale »**. Seule tolérance : HMAC-SHA-1 avec clé ≥ 100 bits, statut obsolescent. MD5 et toute sortie < 256 bits sont hors périmètre.

En visée post-quantique, **SHA3-384** est conforme ; SHA-256 et SHA3-256 ne le sont pas — `[CRYPTO-DIM RecoPQHachage]`.

### MAC — `[CRYPTO R7 à R10]`

| Mécanisme | Statut |
|-----------|--------|
| **CMAC** (sur bloc recommandé) | R |
| **HMAC**, clé ≥ 128 bits | R |
| **GMAC** | R |
| CBC-MAC | R **uniquement à taille de message constante** — proscrit à taille variable |

**Troncature** : ne pas descendre sous **96 bits** ; tolérance à 64 bits si ≤ 2²⁰ vérifications par clé. **Exception GCM/GMAC : 128 bits minimum, pas de troncature.**

### Asymétrique — `[CRYPTO R16 à R22]`, `[CRYPTO-DIM]`

| Famille | Règle (PG-083 v3.00) | Recommandé |
|---------|---------------------|-----------|
| **RSA** | ≥ 2048 bits jusqu'à fin 2030, **≥ 3072 bits à partir de 2031** ; exposant public > 2¹⁶ et ≤ 256 bits | **≥ 3072 bits dès maintenant** |
| **DLOG sur GF(p)** | ≥ 2048 bits jusqu'à fin 2030, **≥ 3072 à partir de 2031** ; sous-groupe d'ordre premier ≥ 250 bits | ≥ 3072 dès maintenant |
| **Courbes elliptiques** | sous-groupe d'ordre multiple d'un premier **≥ 250 bits** | ordre premier |

**Courbes recommandées** : `BrainpoolP256r1/P384r1/P512r1`, `P-256`, `P-384`, `P-521`, `Curve25519`, `Curve448` — corps premier uniquement.

**Mécanismes** : chiffrement `RSA-OAEP`, `ECIES-KEM`, `DLIES-KEM` · signature `RSA-PSS`, `EC-DSA`, `EC-KCDSA` · établissement de clé `DH`, `EC-DH`.

**`RSA PKCS#1 v1.5` est obsolescent**, en chiffrement comme en signature (oracles de padding Bleichenbacher).

### Post-quantique — `[CRYPTO R19]`, `[CRYPTO-DIM]`

**Ne jamais utiliser un mécanisme post-quantique seul** : l'hybrider avec un schéma classique éprouvé.

- `ML-KEM-512` (FIPS 203) : conforme **uniquement hybridé** — préférer **ML-KEM-768**
- `ML-DSA` (FIPS 204) : **non conforme sans hybridation**, quels que soient les paramètres
- **`SLH-DSA` (FIPS 205)** : conforme aux règles classique **et** post-quantique — seul mécanisme asymétrique utilisable tel quel après 2030

### Génération d'aléa — `[CRYPTO R23, R24]`

- DRBG recommandés : **HMAC-DRBG, Hash-DRBG, CTR-DRBG**. L'usage direct d'une source d'aléa brute ne respecte pas le RGS.
- **Germe (seed) : entropie ≥ 128 bits** ; état interne ≥ 192 bits en v3.00.
- Tirer un entier modulo q : **par rejet** ou par aléa additionnel. La **réduction modulaire directe introduit un biais** et est à proscrire.

### Principes structurants

- **« Une clé, un usage »** — clés distinctes entre intégrité et authentification d'entité, entre signature et authentification, entre chiffrement et MAC dans une composition.
- **« La créativité n'est pas recommandée ! »** — utiliser des bibliothèques éprouvées, jamais une construction maison.
- Une primitive asymétrique nue, sans padding, **n'est pas un schéma valide**.

---

## 3. Mots de passe et authentification

### Longueur minimale — `[MFA R21]`, table 3 du guide

Valeurs pour un **alphabet de 90 caractères** (minuscules, majuscules, chiffres, caractères spéciaux) :

| Sensibilité | Longueur minimale | Équivalent en bits |
|-------------|-------------------|--------------------|
| Faible à moyen | **9 à 11** caractères | ≈ 65 |
| Moyen à fort | **12 à 14** caractères | ≈ 85 |
| Fort à très fort | **≥ 15** caractères | ≥ 100 |

- En sensibilité forte à très forte, **l'ANSSI recommande le MFA** plutôt que d'allonger le mot de passe — `[MFA R1]`.
- Mot de passe **non mémorisé** (géré en coffre-fort) : viser **> 20 caractères**.
- **Pas de longueur maximale** imposée — `[MFA R22]`. Fixer tout de même une borne haute (plusieurs centaines de caractères) contre le déni de service par hachage de charges massives.

> ⚠️ Le guide **ne fournit pas** de table « avec MFA / sans MFA ». La seule modulation est celle du niveau de sensibilité, du caractère mémorisable, et des mesures compensatoires (ex. un code PIN court reste acceptable s'il est adossé à une désactivation définitive après **3 échecs**).

### Stockage côté serveur — `[MFA R28, R29, R29-]`

- **Stockage en clair : absolument proscrit.**
- **Sel aléatoire par compte, d'au moins 128 bits** — `[MFA R28]` (confirmé par `[CRYPTO note 4.8.b]`).
- **Fonction de dérivation *memory-hard* : `scrypt` ou `Argon2`** — `[MFA R29]`.
- Repli si le memory-hard est hors d'atteinte : **PBKDF2 avec le plus grand nombre d'itérations possible** — `[MFA R29-]`.

> ⚠️ **Divergence entre guides ANSSI.** `CRYPTO R15` ne recommande **que PBKDF2** et ne mentionne nulle part Argon2, scrypt ou bcrypt — vérification faite sur le texte intégral de PA-079 et de PG-083 v3.00. **Retenir `MFA R29`** : c'est le guide spécialisé sur le sujet et il est aligné sur l'état de l'art. Ne pas invoquer le guide cryptographique pour justifier PBKDF2 comme choix nominal.
> ⚠️ **Aucun guide ANSSI ne donne de paramètres chiffrés** pour Argon2 (`m=`, `t=`, `p=`) ni de nombre d'itérations PBKDF2. La formule constante est « le plus grand possible tant que cela n'affecte pas un usage légitime ». Tout paramètre concret proposé est donc `[DINUM]`.

### Expiration — `[MFA R24, R25, R26]`

| Cas | Règle |
|-----|-------|
| Comptes **non sensibles** | **Pas d'expiration par défaut** si la robustesse est garantie. Une rotation tous les 3 à 6 mois est jugée **contre-productive** |
| Si la robustesse ne peut être garantie | Expiration de l'ordre **d'une année** |
| Comptes **à privilèges** | Expiration imposée, **entre 1 et 3 ans** |
| **Compromission** suspectée ou avérée | Renouvellement **de l'ordre de la journée**, puis désactivation du compte au-delà |

### Tentatives et sessions — `[MFA R10, R12, R14]`

- Limiter le nombre de tentatives sur une période donnée : blocage de **quelques secondes à quelques minutes**, **linéaire ou exponentiel**. Aucun seuil générique n'est fixé par l'ANSSI.
- **Ne pas indiquer quel facteur a échoué** ; ne notifier le résultat qu'une fois tous les facteurs demandés — `[MFA R14]`.
- Durée de session : accès à des informations sensibles → **quelques minutes tout au plus** ; réseau interne → plusieurs heures.

### Facteurs d'authentification — `[MFA R8, R40, R41]`

Trois catégories : **connaissance** (ce que je sais) · **possession** (ce que je possède) · **inhérent** (ce que je suis).

- Une authentification multifacteur exige des facteurs de **catégories différentes**. Code PIN + mot de passe = deux facteurs de connaissance → **ce n'est pas du multifacteur**, c'est de la double authentification.
- **Le SMS est à proscrire** comme canal de réception d'un facteur — `[MFA R8]` : vulnérabilités du protocole SS7, *SIM swapping*, réutilisation des numéros.
- **La biométrie ne peut pas être un facteur unique** — `[MFA R40]` ; elle doit être associée à un facteur fort — `[MFA R41]`.
- Le facteur « où je suis » (IP, GPS) est écarté : contournable et peu mature.
- **Multifacteur ≠ authentification forte** : mot de passe + code SMS est multifacteur mais faible. L'authentification forte repose sur un mécanisme cryptographique robuste — FIDO2, FIDO U2F, certificats sur carte à puce, HOTP/TOTP/OCRA, Kerberos, PAKE (SPAKE2, OPAQUE).

---

## 4. Sécurité côté navigateur

### Content Security Policy — `[WEB R13 à R20]`

- Déclarer la CSP **par en-tête HTTP** ; la balise `<meta>` est un repli qui ne supporte ni `frame-ancestors`, ni `sandbox`, ni `report-uri` — `[WEB R14, R14-]`.
- **`default-src` obligatoire**, et jamais positionnée à `*` — `[WEB R16]`. En l'absence de `default-src`, ne pas définir une directive équivaut à `*`.
- **Interdits : `'unsafe-inline'`, `'unsafe-eval'` et `data:`** — `[WEB R15]`.
- Besoin élevé : partir de `default-src 'none'` puis autoriser explicitement chaque type de ressource.
- Déploiement progressif via `Content-Security-Policy-Report-Only`.

```
Content-Security-Policy: default-src 'self'; frame-ancestors 'none';
```

### Cookies — `[WEB R26 à R33]`

| Attribut | Règle |
|----------|-------|
| `HttpOnly` | Dès qu'un cookie n'a pas à être lu en JavaScript ; **nécessaire pour un cookie de session** |
| `Secure` | Dès lors que le site n'est accessible qu'en HTTPS |
| `SameSite` | `Strict` par défaut ; `Lax` si le cookie n'autorise pas d'action privilégiée via GET. Pour un cookie de session, **doit être défini et ne doit pas valoir `None`** |
| `Path` | Ajusté au découpage hiérarchique (ex. `/admin` pour l'administration) |
| `Domain` | **Ne pas le spécifier** en général : le navigateur le limite alors au sous-domaine émetteur |

```
Set-Cookie: sessionId=...; Secure; HttpOnly; SameSite=Lax
```

**Ne pas stocker d'informations sensibles** dans `localStorage`/`sessionStorage` `[WEB R23]`, dans `IndexedDB` `[WEB R24]`, ni dans les cookies hors jetons de session `[WEB R26]`. L'API **Web SQL Database est proscrite** `[WEB R25]`.

### Anti-clickjacking — `[WEB R17, R18]`

| `X-Frame-Options` | Équivalent CSP |
|-------------------|----------------|
| `deny` | `frame-ancestors 'none';` |
| `sameorigin` | `frame-ancestors 'self';` |
| `allow-from https://site.fr` | `frame-ancestors https://site.fr;` |

`frame-ancestors` est la mesure principale ; `X-Frame-Options` (non standard, rendu obsolète par CSP) vient en défense en profondeur.

### Referrer-Policy — `[WEB R21]`

La stratégie par défaut **ne doit pas être conservée**, et `unsafe-url` **ne doit pas être utilisée**. Valeurs sûres : `no-referrer`, `same-origin`, `strict-origin`, `strict-origin-when-cross-origin`.

### CORS et requêtes — `[WEB R38 à R44]`

- **Vérifier l'en-tête `Origin`** côté serveur contre une liste d'origines autorisées — `[WEB R40]`. `Access-Control-Allow-Origin: *` est qualifié de dangereux et est incompatible avec `Access-Control-Allow-Credentials: true`.
- **Jeton anti-CSRF : entropie minimale de 128 bits**, issue d'un générateur d'aléa cryptographique (ex. 22 caractères ASCII imprimables) — `[WEB R38]`.
- Préférer l'**API Fetch** à `XMLHttpRequest` — `[WEB R44]`.
- **JSON-P est à proscrire** — `[WEB R58]`.

### Intégrité des ressources — `[WEB R11, R12]`

SRI via `integrity` + `crossorigin`, sur transport HTTPS :

```html
<script src="https://cdn.example/lib.js"
        integrity="sha384-xBuQ/xzmIsLoJpyjoggmTEz8OWUFM0/RC5BsqQBDX2v5cMvDHcMakNTNrHIW2I5f"
        crossorigin="anonymous"></script>
```

Limites : ne couvre que CSS et JavaScript, ne vérifie pas les dépendances transitives, **impossible dans un Web Worker** (`importScripts`).

### JavaScript — `[WEB R4, R9, R10, R45, R47, R57]`

- **`eval()` proscrit** `[WEB R9]` ; proscrire aussi `setTimeout`/`setInterval` avec une chaîne, `Function('code')`, `.constructor('code')` `[WEB R10]`.
- Préférer `textContent`, `createTextNode()`, `setAttribute()` à `innerHTML`, `outerHTML`, `document.write()`, `insertAdjacentHTML()` `[WEB R4]`.
- **`target="_blank"` exige `rel="noopener"`** `[WEB R45]`.
- **`postMessage` : jamais `"*"`** comme origine destinatrice ; contrôler origine et format en réception `[WEB R54, R55]`.
- **Écriture de `document.domain` proscrite** `[WEB R57]`.
- Mode strict `"use strict";` en tête de chaque fonction `[WEB R47]`.

> ⚠️ **`X-XSS-Protection` n'est plus préconisé** : poser `X-XSS-Protection: 0`. `X-Content-Type-Options: nosniff` **n'apparaît pas dans le guide** — c'est une bonne pratique `[DINUM]` ; l'ANSSI traite le typage par un `Content-Type` explicite `[WEB R6]`.

---

## 5. Journalisation

### Horodatage — `[LOG R3, R4, R5]`

- Horodatage **obligatoire sur tous les événements**.
- Paramètres **homogènes** sur tout le parc, **précision minimale à la seconde**.
- Format : **ISO 8601** recommandé. **UTC** explicitement conseillé quand la gestion des changements d'heure n'est pas certaine.
- Synchronisation sur **plusieurs sources internes cohérentes**, elles-mêmes calées sur plusieurs sources externes fiables — sauf réseau physiquement isolé.

### Rétention — `[LOG R24, R25]`

| Cas | Durée |
|-----|-------|
| **Cas général (CNIL, délibération n° 2021-122)** | **6 mois à 1 an** ; jusqu'à **3 ans** dans des cas particuliers dûment motivés |
| OIV / OSE / FSN | **≥ 6 mois**, centralisés et archivés |
| Rétention locale avant export | Supérieure à l'écart entre deux sauvegardes ou deux envois |

La détection d'une **attaque avérée ou suspectée** justifie une conservation au-delà. La suppression au-delà de la durée doit être **automatisée**, et le mécanisme prévu **dès la conception** — particulièrement pour les applications métier, plus susceptibles de générer des données personnelles.

### Contenu d'un événement — `[LOG R3, section 2.1]`

Format **interprétable** : lisible par un humain **et** analysable automatiquement, composé de **champs fixes à la grammaire définie**, avec une **source identifiable** et un identifiant **intelligible** (`SRV-MSG-001` plutôt que `47834456678`). Prévoir un champ `version` incrémenté à chaque changement de syntaxe.

### Socle minimal à journaliser — `[LOG annexe A]`

| Domaine | Événements |
|---------|-----------|
| **Authentification** | ouvertures de session, réussites et **échecs** d'authentification, utilisation de privilèges |
| **Gestion des comptes** | création de comptes/groupes/rôles, désactivations et verrouillages, octroi de privilèges, ajouts de membres, **modification des secrets d'authentification** |
| **Stratégies de sécurité** | modification des paramètres de sécurité, modification des stratégies d'audit, **effacement de journaux** |
| **Accès aux ressources sensibles** | accès et tentatives d'accès (lecture, écriture, exécution, suppression) — attention à la volumétrie |
| **Activité des processus** | démarrages/arrêts, dysfonctionnements, chargements de modules, exécution de scripts |
| **Activité des systèmes** | démarrages, dysfonctionnements et surcharges, modules noyau, activité matérielle |

### Ce qui ne doit jamais y figurer — `[LOG section 2.1]`

- **Minimiser les données à caractère personnel**, et prévoir leur suppression automatique. La CNIL considère régulièrement une **adresse e-mail, une URL ou une adresse IP** comme des données personnelles ; le nom de machine ou l'identifiant de processus ne le sont pas.
- **Secrets** : attention aux modes `debug` / `verbose`, « potentiellement révélateurs d'informations sensibles (typiquement des secrets) » — et non recommandés en fonctionnement nominal.

### Transport et protection — `[LOG R16, R17, R26, R27]`

- Protocoles reposant sur **TCP** (jamais UDP seul, pertes définitives), complétés de cache et d'acquittement applicatifs.
- **Confidentialité, intégrité et authentification** du serveur de collecte via **TLS** (ou SSH/IPsec à défaut), idéalement avec **authentification mutuelle par certificats**.
- Moindre privilège en **écriture** `[LOG R26]`, en **suppression** `[LOG R26+]` et en **lecture** `[LOG R27]` — sur les équipements générateurs comme sur les collecteurs.
- Transfert en **temps réel** `[LOG R14]` ; à défaut, **au plus tard quelques heures** après génération `[LOG R14-]`.
