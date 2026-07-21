# Module conditionnel — Langage C

**Charger uniquement si** le projet contient des fichiers `*.c` / `*.h`, un `Makefile` ou un `CMakeLists.txt`.

Dérivé de *Règles de programmation pour le développement sécurisé de logiciels en langage C* (ANSSI-PA-073 v1.2, 21/07/2020) — voir [`../sources.md`](../sources.md).

## Comment citer ce guide

Le guide **ne numérote pas par chapitre** : chaque énoncé porte un numéro global **1 à 181** et un type imprimé dans son encadré — `RÈGLE` (120), `RECOMMANDATION` (52) ou `BONNE PRATIQUE` (9). La citation correcte est donc `[C RÈGLE 168]`, pas `[C R168]`.

**Ce module retient 38 énoncés sur 181.** Critère : violation produisant directement une vulnérabilité mémoire, arithmétique ou de contrôle de flux, **et** détectable sur le code source ou la ligne de commande de build. Les ~143 énoncés écartés portent sur la mise en page, le nommage, la documentation, la portabilité, la lisibilité et la structuration — utiles, mais hors portée d'un audit de sécurité outillé. Pour un projet C critique, se référer au guide complet.

> Chaque section du guide est croisée avec **MISRA C:2012, CERT C et CWE** : ces correspondances permettent de mapper les règles vers `clang-tidy` (`cert-*`), `cppcheck --addon=misra` et les analyseurs statiques du marché.

---

## 1. Compilation et durcissement

- [ ] Options de compilation définies précisément et explicitement — [C RÈGLE 4]
- [ ] **Options de durcissement activées** (obligatoire) : exécutables relocalisables, ASLR efficace, protection contre le dépassement de pile — [C RÈGLE 5]
- [ ] Code compilé **sans erreur ni avertissement**, options exigeantes activées — [C RÈGLE 7]
- [ ] Tout code mis en production compilé en **mode release** — [C RÈGLE 9]
- [ ] `-Wformat=2` et `-Wformat-security` dès qu'une fonction variadique est utilisée — [C BONNE PRATIQUE 137]
- [ ] Si les options de durcissement sont indisponibles, mécanismes « canari » implémentés manuellement — [C RÈGLE 178]

**Jeu de flags de l'annexe B.2 du guide :**

```make
CFLAGS  = -Wall -Wextra -Wformat=2 -Wformat-security -Wwrite-strings -Wstack-protector
CFLAGS += -pie -fPIE                  # exécutable relocalisable → ASLR
CFLAGS += -fstack-protector=strong    # canaris de pile
CFLAGS += -D_FORTIFY_SOURCE=2         # sans effet si niveau d'optimisation < 1
LDFLAGS = -Wl,-z,relro -Wl,-z,now     # RELRO complet
```

**Options à proscrire** (§4.1, encadré « Attention » du guide) — elles masquent des comportements indéfinis au lieu de les corriger :

```
-fno-strict-overflow   -fwrapv   -fno-delete-null-pointer-checks   -fno-strict-aliasing
```

## 2. Comportements indéfinis et arithmétique entière

- [ ] Seul du code C **conforme au standard** est utilisé — [C RÈGLE 2]
- [ ] Tous les débordements possibles d'entiers **signés** supprimés — [C RÈGLE 92]
- [ ] Tous les `wrap` possibles d'entiers **non signés** détectés — [C RECOMMANDATION 93]
- [ ] Toute division par zéro potentielle détectée et supprimée — [C RÈGLE 94]
- [ ] Opérateurs logiques non appliqués à des opérandes signés — [C RECOMMANDATION 96]

## 3. Types et conversions

- [ ] Seuls `signed char` et `unsigned char` utilisés (jamais `char` nu pour une valeur numérique) — [C RÈGLE 65]
- [ ] Règles de conversion maîtrisées et comprises — [C RÈGLE 67]
- [ ] Conversions entre types signés et non signés **explicites** — [C RÈGLE 68]
- [ ] Type d'une expression constante suffisamment large pour la contenir — [C RÈGLE 47]

## 4. Initialisation

- [ ] Variables initialisées à la déclaration ou immédiatement après — [C RECOMMANDATION 57]
- [ ] Variables structurées initialisées champ par champ, valeur explicitée — [C RÈGLE 59]

## 5. Tableaux, pointeurs et débordements de tampon

- [ ] Pas de VLA (tableaux de taille variable) — [C RÈGLE 72]
- [ ] Entiers **non signés** pour les tailles de tableaux — [C RÈGLE 74]
- [ ] Validité de l'indice vérifiée avant tout accès à un élément de tableau — [C RÈGLE 75]
- [ ] Aucun déréférencement de pointeur `NULL` — [C RÈGLE 76]
- [ ] Pointeur affecté à `NULL` après désallocation (prévention de l'*use-after-free*) — [C RÈGLE 77]
- [ ] Aucune arithmétique sur des pointeurs `void*` — [C RÈGLE 82]
- [ ] Soustraction et comparaison de pointeurs limitées à un même tableau — [C RÈGLE 84]
- [ ] Pas de FAM (*flexible array members*) — [C RÈGLE 90]

## 6. Gestion de la mémoire

- [ ] Taille allouée dynamiquement suffisante pour l'objet — [C RÈGLE 145]
- [ ] Mémoire allouée dynamiquement libérée au plus tôt — [C RÈGLE 146]
- [ ] **Zones mémoire sensibles mises à zéro avant libération** — [C RÈGLE 147]
- [ ] Aucune libération de mémoire non allouée dynamiquement — [C RÈGLE 148]
- [ ] Allocation dynamique non modifiée via `realloc` — [C RÈGLE 149]
- [ ] `sizeof` correctement utilisé (jamais sur un pointeur pour obtenir la taille d'un tampon) — [C RÈGLE 150]
- [ ] **Succès de toute allocation mémoire vérifié** — [C RÈGLE 151]
- [ ] Isolement des données sensibles effectué — [C RÈGLE 152]

## 7. Fonctions, erreurs et valeurs de retour

- [ ] Validité de **tous** les paramètres de fonction systématiquement remise en cause — [C RÈGLE 128]
- [ ] **Valeur de retour de toute fonction testée** — [C RÈGLE 132]
- [ ] Aucun retour implicite pour une fonction de type non `void` — [C RÈGLE 133]
- [ ] Aucun appel de fonction variadique avec `NULL` en argument — [C RÈGLE 138]
- [ ] `errno` initialisée avant et consultée après tout appel de la bibliothèque standard qui la modifie — [C RÈGLE 153]
- [ ] Gestion systématique des erreurs retournées par la bibliothèque standard — [C RÈGLE 154]
- [ ] `setjmp()` et `longjmp()` non utilisées — [C RÈGLE 161]

## 8. Bibliothèque standard et fonctions dangereuses

- [ ] Bibliothèques `setjmp.h` et `stdarg.h` non utilisées — [C RÈGLE 162]
- [ ] `atoi()`, `atol()`, `atof()`, `atoll()` remplacées par les équivalents `strto*()` — [C RÈGLE 164]
- [ ] `rand()` non utilisée (jamais pour un usage cryptographique) — [C RÈGLE 165]
- [ ] Versions bornées préférées : `strxx` → `strnxx` quand le nombre de caractères peut être borné — [C RÈGLE 166]
- [ ] Aucune fonction obsolescente ou devenue obsolète dans une norme ultérieure — ex. `gets()` — [C RÈGLE 167]
- [ ] **Aucune fonction manipulant un tampon sans prendre sa taille en argument** — [C RÈGLE 168]

> **Nuances à ne pas perdre.** Le guide **ne nomme pas** `strcpy`, `sprintf` ou `gets` dans des règles dédiées : la proscription passe par les RÈGLES 166, 167 et 168, formulées génériquement, `gets()` n'étant qu'un exemple cité au §16.4. Le guide avertit aussi que les variantes `strn*` peuvent **encore** produire un comportement indéfini (troncature sans terminaison nulle) ; seule `strcpy_s()` du C11 est présentée comme réellement plus sûre.

## 9. Données sensibles

- [ ] **Aucune donnée sensible codée en dur** — [C RÈGLE 63]

> Recoupe le domaine 3 du socle (Gestion des secrets), qui s'applique en complément.
