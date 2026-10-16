# Format du rapport, grille de priorités et export

Produit à la fin du [workflow d'audit](../SKILL.md) une fois les 14 domaines de [`checklist.md`](checklist.md) parcourus, les modules conditionnels applicables évalués et les non-conformités validées.

---

## Format du rapport d'audit

```markdown
## Audit Sécurité — Rapport de conformité

**Date :** AAAA-MM-JJ
**Périmètre audité :** [description du projet / service / composant]
**Résultat global :** X/Y règles conformes (Z% conforme)
(X conformes, X non conformes, X partielles, X non applicables)

---

### Tableau de synthèse

| # | Domaine | Statut | Détail |
|---|---------|--------|--------|
| 1 | TLS / HTTPS | OK / KO / Partiel / NA | résumé en une ligne |
| 2 | Cryptographie | OK / KO / Partiel / NA | résumé en une ligne |
| 3 | Gestion des secrets | OK / KO / Partiel / NA | résumé en une ligne |
| 4 | Authentification, MFA et mots de passe | OK / KO / Partiel / NA | résumé en une ligne |
| 5 | Validation des entrées et bases de données | OK / KO / Partiel / NA | résumé en une ligne |
| 6 | Dépendances et composants tiers | OK / KO / Partiel / NA | résumé en une ligne |
| 7 | Journalisation | OK / KO / Partiel / NA | résumé en une ligne |
| 8 | Sécurité navigateur et API | OK / KO / Partiel / NA | résumé en une ligne |
| 9 | Cloisonnement système | OK / KO / Partiel / NA | résumé en une ligne |
| 10 | Conteneurs et déploiement | OK / KO / Partiel / NA | résumé en une ligne |
| 11 | Chaîne de développement (CI/CD) | OK / KO / Partiel / NA | résumé en une ligne |
| 12 | Poste de développement | OK / KO / Partiel / NA | résumé en une ligne |
| 13 | Sauvegarde et continuité | OK / KO / Partiel / NA | résumé en une ligne |
| 14 | Gestion des incidents | OK / KO / Partiel / NA | résumé en une ligne |

### Modules conditionnels évalués

À n'inclure que si le module a été chargé (voir la sélection des modules dans [`../SKILL.md`](../SKILL.md)). Ne pas lister les modules non applicables et ne pas les compter dans le résultat global.

| Module | Déclencheur constaté | Statut | Détail |
|--------|----------------------|--------|--------|
| Langage C | ex. présence de `*.c` / `Makefile` | OK / KO / Partiel | résumé en une ligne |
| Rust | ex. présence de `Cargo.toml` | OK / KO / Partiel | résumé en une ligne |
| CMS | ex. WordPress, Drupal détecté | OK / KO / Partiel | résumé en une ligne |

---

### Non-conformités détectées

**[KO] Domaine {#} — {Nom du domaine}**
- **Règle concernée :** description de la règle non respectée
- **Source :** identifiant(s) de recommandation ANSSI, ex. `[MFA R29]` — ou `[DINUM]` si la règle est une bonne pratique sans équivalent dans les guides (voir [`sources.md`](sources.md))
- **Constat :** ce qui a été observé dans le code / la configuration
- **Exploitabilité :** Exploitable (faille activable en l'état) / Bonne pratique manquante (défense en profondeur)
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

La priorité combine **exploitabilité** (la faille est-elle activable en l'état ?) et **impact** (gravité si exploitée), dans l'esprit *sévérité = vraisemblance × impact*. Une bonne pratique manquante qui ne crée pas de chemin d'attaque direct reste 🟡, même si le principe est important.

| Priorité | Définition | Exemples |
|----------|------------|---------|
| 🔴 **Critique** | Vulnérabilité exploitable, risque immédiat de compromission | Secret dans le code source, pas de TLS, injection SQL possible |
| 🟠 **Élevée** | Faiblesse significative, exploitation possible sous conditions | Headers de sécurité manquants, pas de rate limiting, pas de MFA admin |
| 🟡 **Modérée** | Bonne pratique non respectée, risque limité / défense en profondeur | Logs non centralisés, pas de scan d'images Docker, rotation des secrets non planifiée |

> **Qualifier chaque KO.** Un constat *exploitable* tire la priorité vers 🔴/🟠 ; une *bonne pratique manquante* (sans chemin d'attaque direct) reste généralement 🟡. Cette qualification, issue de l'étape de validation du workflow, doit apparaître dans le champ « Exploitabilité » de chaque non-conformité.

## Export du rapport

Après avoir produit le rapport, **toujours** :

1. Créer le dossier `audits/` à la racine du projet s'il n'existe pas
2. Écrire le rapport complet dans `audits/securite-developpement-AAAA-MM-JJ.md` (date du jour, format ISO)
3. Afficher également le rapport dans la conversation

Si un fichier du même nom existe déjà, ajouter un suffixe incrémental : `securite-developpement-2026-03-26-2.md`.

> Exemple : `audits/securite-developpement-2026-03-26.md`

## Sortie structurée optionnelle (`securite-developpement-AAAA-MM-JJ.json`)

En **complément** du rapport Markdown (et seulement si l'utilisateur le demande, ou pour outiller/agréger des audits sur plusieurs projets), produire un fichier `audits/securite-developpement-AAAA-MM-JJ.json` conforme au schéma [`findings-schema.json`](findings-schema.json).

Le JSON ne remplace jamais le Markdown : il en est la version machine-lisible. Champs clés par finding : `domaine` (1–14) **ou** `module` (`langage-c`/`langage-rust`/`cms`, exclusifs l'un de l'autre), `regle`, `references_anssi`, `statut` (`OK`/`KO`/`NA`/`Partiel`), `constat`, `exploitable` (booléen), `risque`, `correction`, `priorite` (`critique`/`elevee`/`moderee`).

Exemple minimal :

```json
{
  "date": "2026-03-26",
  "perimetre": "API Express du service X",
  "synthese": { "total": 14, "conformes": 9, "non_conformes": 2, "partiels": 2, "non_applicables": 1 },
  "findings": [
    {
      "domaine": 3,
      "nom_domaine": "Gestion des secrets",
      "regle": "Jamais de secret dans le code source",
      "references_anssi": ["ESS-DEVSECOPS"],
      "statut": "KO",
      "constat": "Clé API Stripe en dur dans src/config.ts:12",
      "exploitable": true,
      "risque": "Compromission du compte de paiement si le dépôt fuite",
      "correction": "Déplacer la clé en variable d'environnement, révoquer et régénérer la clé exposée",
      "priorite": "critique"
    },
    {
      "domaine": 4,
      "nom_domaine": "Authentification, MFA et mots de passe",
      "regle": "Utiliser une fonction de dérivation memory-hard pour conserver les mots de passe",
      "references_anssi": ["MFA R29", "MFA R28"],
      "statut": "KO",
      "constat": "Mots de passe hachés en SHA-256 sans sel dans src/auth/user.ts:47",
      "exploitable": true,
      "risque": "Récupération des mots de passe en clair par tables précalculées si la base fuite",
      "correction": "Migrer vers Argon2id avec un sel aléatoire d'au moins 128 bits par compte, re-hacher à la prochaine connexion",
      "priorite": "critique"
    }
  ]
}
```
