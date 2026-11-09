#!/bin/sh
set -eu

script_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
script="$script_dir/officiel.py"
tmp_dir=$(mktemp -d)
trap 'rm -rf "$tmp_dir"' EXIT HUP INT TERM

fail() {
  echo "$1" >&2
  exit 1
}

output="$tmp_dir/sortie.txt"

setup() {
  rm -rf "$tmp_dir/cas"
  mkdir -p "$tmp_dir/cas/classement" "$tmp_dir/cas/references"
  cat >"$tmp_dir/cas/criteres.json" <<'EOF'
{"wcag": {"version": "2.1"}, "topics": [{"topic": "Images", "number": 1, "criteria": [
  {"criterium": {"number": 1, "title": "Chaque [image porteuse d’information](#image-porteuse-d-information) a-t-elle une alternative ?",
    "tests": {"1": ["Chaque image `<img>` a-t-elle une alternative ?"], "2": ["Chaque `<svg>` vérifie-t-il ces conditions ?", "Il a `role=\"img\"` ;", "Il a une alternative."]},
    "particularCases": ["Le critère est non applicable :", {"ul": ["sans image ;", "image d’un <span lang=\"en\">“captcha”</span>."]}]}},
  {"criterium": {"number": 2, "title": "Chaque alternative est-elle pertinente ?",
    "tests": {"1": ["Le texte est-il pertinent ?"]}}},
  {"criterium": {"number": 3, "title": "Chaque image décorative est-elle ignorée ?",
    "tests": {"1": ["L’image a-t-elle `alt=\"\"` ?"]}, "technicalNote": ["Une note."]}}
]}]}
EOF
  cat >"$tmp_dir/cas/glossaire.json" <<'EOF'
{"glossary": [{"title": "Image porteuse d’information", "body": "<p>Image qui donne une <code>information</code>.</p><ul><li>premier cas ;</li><li>second cas.</li></ul>"}]}
EOF
  cat >"$tmp_dir/cas/classement/criteres-1.md" <<'EOF'
# Classement

- **1.1** Alternative présente — code
- **1.2** Alternative pertinente — jugement humain. Reste : lire l’alternative.
- **1.3** Image décorative — mixte. Le code prouve : NC sur un alt rempli. Reste : voir l’image.
EOF
  cat >"$tmp_dir/cas/references/criteres-images.md" <<'EOF'
# Thème 1

### 1.1 Alternative

**Texte officiel 1.1 :** à générer

**Impact :** texte libre conservé.

### 1.2 Pertinence

**Texte officiel 1.2 :** à générer

### 1.3 Décoration

**Texte officiel 1.3 :** à générer
EOF
}

run() {
  status=0
  python3 "$script" --source "$tmp_dir/cas/criteres.json" --glossary-source "$tmp_dir/cas/glossaire.json" \
    --classement "$tmp_dir/cas/classement" --references "$tmp_dir/cas/references" \
    --glossary "$tmp_dir/cas/references/glossaire.md" "$@" >"$output" 2>&1 || status=$?
}

expect() {
  [ "$status" -eq "$1" ] || { cat "$output" >&2; fail "$2 : code de sortie $status, attendu $1"; }
  if [ -n "${3:-}" ]; then
    grep -qF -- "$3" "$output" || { cat "$output" >&2; fail "$2 : message « $3 » absent"; }
  fi
}

reference="$tmp_dir/cas/references/criteres-images.md"

setup
run
expect 1 "blocs non générés" "texte officiel 1.1 différent de la source"
run --write
expect 0 "génération"
run
expect 0 "contrôle après génération" "3 blocs pour 3 critères de la source ; 0 erreur(s)"
grep -qF '**1.1.2** Chaque `<svg>` vérifie-t-il ces conditions ?' "$reference" || fail "test numéroté absent"
grep -qF '  - Il a `role="img"` ;' "$reference" || fail "condition de test absente"
grep -qF 'Chaque *image porteuse d’information* a-t-elle' "$reference" || fail "terme du glossaire non mis en italique"
grep -qF '    - image d’un “captcha”.' "$reference" || fail "cas particulier imbriqué mal rendu"
grep -qF '  - Une note.' "$reference" || fail "note technique absente"
grep -qF '**Impact :** texte libre conservé.' "$reference" || fail "texte hors bloc modifié"
grep -q '1\.2\.1' "$reference" && fail "un critère « jugement humain » ne porte que son intitulé"
grep -qF '### Image porteuse d’information' "$tmp_dir/cas/references/glossaire.md" || fail "titre du glossaire absent"
grep -qF -- '- second cas.' "$tmp_dir/cas/references/glossaire.md" || fail "liste du glossaire mal rendue"
grep -qF 'une `information`.' "$tmp_dir/cas/references/glossaire.md" || fail "code du glossaire mal rendu"

sed -i.bak 's/Chaque image `<img>` a-t-elle une alternative ?/Chaque image a une alternative./' "$reference"
run
expect 1 "texte officiel retouché à la main" "criteres-images.md:5: texte officiel 1.1 différent de la source"
run --write
expect 0 "réparation par --write"
run
expect 0 "contrôle après réparation"

sed -i.bak '/^\*\*Texte officiel 1\.3 :\*\*/,$d' "$reference"
run
expect 1 "bloc supprimé" "critère 1.3 : aucun bloc « Texte officiel » dans les références"

setup
run --write
printf '\n**Texte officiel 1.2 :** Chaque alternative est-elle pertinente ?\n' >>"$reference"
run
expect 1 "bloc en double" "critère 1.2 déjà présent"

setup
run --write
sed -i.bak 's/- \*\*1\.2\*\* Alternative pertinente — jugement humain\./- **1.2** Alternative pertinente — mixte. Le code prouve : NC./' "$tmp_dir/cas/classement/criteres-1.md"
run
expect 1 "critère reclassé de jugement humain à mixte" "texte officiel 1.2 différent de la source"
run --write
expect 0 "tests ajoutés après reclassement"
grep -qF '**1.2.1** Le texte est-il pertinent ?' "$reference" || fail "tests absents après reclassement"

setup
run --write
sed -i.bak '/1\.3/d' "$tmp_dir/cas/classement/criteres-1.md"
run
expect 1 "critère absent du classement" "critère 1.3 : absent du classement, mode inconnu"

setup
run --write
echo "retouche" >>"$tmp_dir/cas/references/glossaire.md"
run
expect 1 "glossaire retouché" "glossaire.md : différent de la source"

setup
run --write
printf '\n**Texte officiel 9.9 :** inventé\n' >>"$reference"
run
expect 1 "critère inconnu de la source" "critère 9.9 absent de la source"

setup
status=0
python3 "$script" --source "$tmp_dir/absent.json" >"$output" 2>&1 || status=$?
expect 2 "source illisible" "lecture impossible"

echo "Official text tests passed"
