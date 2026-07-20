# Module conditionnel — Rust

**Charger uniquement si** le projet contient un `Cargo.toml` ou un `Cargo.lock`.

Dérivé de *Règles de programmation pour le développement d'applications sécurisées en Rust* (ANSSI-PA-074 v1.0, 09/06/2020) — voir [`../sources.md`](../sources.md). Le guide compte **51 items R1 à R51**, répartis en deux niveaux imprimés : **RÈGLE** (obligatoire, 34 items) et **RECO** (recommandation, 17 items). Ce module retient les items vérifiables par inspection du code, du `Cargo.toml` ou de la CI, et dont la violation a une conséquence de sécurité directe.

Les règles de style, de nommage et de lisibilité du guide (R5 rustfmt, R9 conventions de nommage, R13 opérateur `?`, R30/R31 traits de comparaison) sont volontairement écartées : elles ne portent pas de risque de sécurité.

> Le guide est maintenu à ciel ouvert sur https://github.com/ANSSI-FR/rust-guide — s'y référer en cas de doute sur une règle.

---

## 1. Chaîne d'outils et profils de compilation

- [ ] Chaîne d'outils **stable** utilisée (pas de nightly en production) — [RUST R1 · RÈGLE]
- [ ] `debug-assertions` et `overflow-checks` **non modifiées** dans `[profile.dev]` et `[profile.test]` du `Cargo.toml` — [RUST R2 · RÈGLE]
- [ ] `RUSTC`, `RUSTC_WRAPPER` et `RUSTFLAGS` laissées à leurs valeurs par défaut — [RUST R3 · RÈGLE]
- [ ] Un *linter* (`clippy`) est exécuté régulièrement, idéalement en CI — [RUST R4 · RÈGLE]
- [ ] Les réparations automatiques de `rustfix` sont **relues par un développeur**, jamais appliquées en aveugle — [RUST R6 · RÈGLE]

> **Point de vigilance signalé par le guide** (encadrés « Attention », non numérotés) : `rustup` ne valide pas les signatures des fichiers téléchargés et `cargo` ne valide pas l'index du registre. Pour un contexte sensible, prévoir une méthode d'installation alternative.

## 2. Dépendances

- [ ] `cargo-outdated` exécuté pour détecter les dépendances obsolètes — [RUST R7 · RÈGLE]
- [ ] `cargo-audit` exécuté pour détecter les vulnérabilités connues des dépendances — [RUST R8 · RÈGLE]

> Le module 6 du socle (Dépendances et composants tiers) s'applique en complément.

## 3. Code `unsafe`

- [ ] `#![forbid(unsafe_code)]` présent dans `main.rs` — [RUST R10 · RÈGLE]
- [ ] Si `unsafe` est présent, il relève de l'un des **trois cas tolérés** par le guide, et il est justifié :
  - FFI vers des fonctions `extern "C"`, encapsulée dans un *wrapper* sûr ;
  - programmation embarquée sur adresses mémoire fixées, avec une abstraction dédiée minimisant le nombre de blocs ;
  - fonction inévitablement non sûre selon ses arguments, alors marquée globalement `unsafe`.
  — [RUST R10 · RÈGLE]

## 4. Arithmétique entière

- [ ] Toute opération susceptible de déborder utilise les fonctions spécialisées `overflowing_<op>`, `checked_<op>`, `wrapping_<op>` ou le type `Wrapping` — [RUST R11 · RÈGLE]

> **Pourquoi c'est critique** : en profil *debug*, un dépassement d'entier provoque un `panic` ; en profil *release*, la valeur est **silencieusement tronquée**. Un calcul de taille ou d'index correct en test peut donc devenir une faille en production.

## 5. Gestion des erreurs et `panic`

- [ ] Pas de fonction pouvant provoquer un `panic` sur une entrée non maîtrisée — [RUST R14 · RÈGLE]
  - motifs cités par le guide : `unwrap`, `expect`, `assert`, accès non vérifié à un tableau, dépassement d'entier (debug), division par zéro, `format!`
- [ ] Indices d'accès aux tableaux testés, ou méthode `get` utilisée — [RUST R15 · RÈGLE]
- [ ] Un type `Error` personnalisé couvre toutes les erreurs possibles, *exception-safe* (RFC 1236), implémentant `Error + Send + Sync + 'static` et `Display` — [RUST R12 · RECO]

## 6. Mémoire et secrets

- [ ] `std::mem::forget` / `core::mem::forget` non utilisée — [RUST R17 · RÈGLE]
- [ ] Lint `#![deny(clippy::mem_forget)]` activé — [RUST R18 · RECO]
- [ ] Pas de fuite mémoire ou de ressource via `Box::leak` — [RUST R19 · RÈGLE]
- [ ] Valeurs encapsulées dans `ManuallyDrop` correctement libérées (`ManuallyDrop::into_inner` ou `unsafe ManuallyDrop::drop`) — [RUST R20 · RÈGLE]
- [ ] Tout `into_raw` a son `from_raw` correspondant (`Box`, `Rc`, `rc::Weak`, `Arc`, `sync::Weak`, `CString`, `OsString`) — [RUST R21 · RÈGLE]
- [ ] `std::mem::uninitialized` et `std::mem::MaybeUninit` non utilisés, ou explicitement justifiés — [RUST R22 · RÈGLE]
- [ ] **Données sensibles mises à zéro après usage**, avec des primitives que le compilateur n'élimine pas à l'optimisation : `std::ptr::write_volatile` ou la crate `zeroize` — [RUST R23 · RÈGLE]

## 7. Traits critiques et concurrence

- [ ] Toute implémentation de `Drop` est justifiée, documentée et relue par des pairs — [RUST R24 · RECO]
- [ ] Aucun `panic` dans une implémentation de `Drop` — [RUST R25 · RÈGLE]
- [ ] Pas de cycle de références à compteurs (`Rc`/`Arc`) incluant des valeurs implémentant `Drop` — [RUST R26 · RÈGLE]
- [ ] L'effacement des secrets cryptographiques **ne repose pas uniquement sur `Drop`** — [RUST R27 · RECO]
- [ ] Implémentation manuelle de `Send` / `Sync` évitée ; si nécessaire, justifiée, documentée et relue — [RUST R28 · RECO]

> `Send` et `Sync` sont des traits `unsafe` que le compilateur ne vérifie pas : une implémentation manuelle incorrecte produit un comportement indéfini.

## 8. Interfaçage avec du code externe (FFI)

À évaluer uniquement si le projet expose ou consomme une FFI.

- [ ] Types compatibles C exclusivement dans les FFI — [RUST R32 · RÈGLE]
- [ ] Types cohérents entre les deux côtés de l'interface — [RUST R33 · RÈGLE]
- [ ] Alias portables `c_*` utilisés pour les types dépendants de la plateforme — [RUST R35 · RÈGLE]
- [ ] Valeurs de types non-robustes traitées conformément au guide — [RUST R36 · RÈGLE]
- [ ] Références provenant d'un langage externe vérifiées — [RUST R38 · RÈGLE]
- [ ] Pointeurs externes vérifiés — [RUST R40 · RÈGLE]
- [ ] Pointeurs de fonction dans les FFI marqués `extern` et `unsafe` — [RUST R41 · RÈGLE]
- [ ] Pointeurs de fonction provenant d'une FFI vérifiés — [RUST R42 · RÈGLE]
- [ ] Aucun type implémentant `Drop` traversant une FFI — [RUST R46 · RÈGLE]
- [ ] Responsabilité de libération des données explicitement identifiée entre les deux langages — [RUST R47 · RÈGLE]
- [ ] `panic` correctement contenus aux frontières FFI (`catch_unwind` / `std::panic`) — [RUST R16, R49 · RÈGLE]

---

## Ce que ce module ne couvre pas

- **`miri`, `cargo-fuzz`** : absents du guide v1.0. Ne pas les présenter comme une exigence ANSSI — ce sont des bonnes pratiques utiles, à qualifier `[DINUM]` si on les recommande.
- **Concurrence** : le guide n'a pas de chapitre dédié. Seules R28 (`Send`/`Sync`) et R26 (cycles `Rc`/`Arc`) l'abordent.
- Le libellé imprimé de **R36** est « Non-vérification des valeurs de types non-robustes » — formulation contre-intuitive du guide, conservée telle quelle pour rester citable.
