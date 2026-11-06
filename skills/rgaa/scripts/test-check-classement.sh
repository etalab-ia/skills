#!/bin/sh
set -eu

script_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
script="$script_dir/check-classement.py"
tmp_dir=$(mktemp -d)
trap 'rm -rf "$tmp_dir"' EXIT HUP INT TERM

fail() {
  echo "$1" >&2
  exit 1
}

skill="$tmp_dir/SKILL.md"
clean="$tmp_dir/propre"
output="$tmp_dir/sortie.txt"

cat >"$skill" <<'EOF'
# Skill

### Phase 2 — Vérifications en conditions réelles

| Question | Priorité | Libellé |
|---|---|---|
| **Clavier** | 🔴 | Test au clavier effectué ? |
| **Orientation** | 🟡 | Portrait et paysage testés ? |

### Phase 3 — Format de sortie

| 🔴 **Bloquant** | Exemple hors catalogue |
EOF

header() {
  cat <<EOF
# Classement des critères — $1

Classement provisoire, en attente de l’avis du pôle accessibilité numérique.

- **code** : le verdict se tranche à la lecture du code.
- **mixte** : le code peut prouver une NC, jamais une conformité.

EOF
}

criteria() {
  for pair in $1; do
    theme=${pair%%:*}
    count=${pair##*:}
    echo "## Thème $theme"
    echo
    number=1
    while [ "$number" -le "$count" ]; do
      echo "- **$theme.$number** Intitulé du critère $theme.$number — code"
      number=$((number + 1))
    done
    echo
  done
}

make_clean() {
  mkdir -p "$1"
  { header "thèmes 1 à 6"; criteria "1:9 2:2 3:3 4:13 5:8 6:2"; } >"$1/criteres-1-6.md"
  { header "thèmes 7 à 13"; criteria "7:5 8:10 9:4 10:14 11:13 12:11 13:12"; } >"$1/criteres-7-13.md"
  sed -i.bak \
    -e 's/^- \*\*1\.2\*\* Intitulé du critère 1\.2 — code$/- **1.2** Images de décoration — mixte. Le code prouve : NC sur un `<svg>` sans `aria-hidden`. Reste : voir l’image./' \
    -e 's/^- \*\*1\.5\*\* Intitulé du critère 1\.5 — code$/- **1.5** CAPTCHA — conditions réelles (question « Clavier »). Reste : tester./' \
    "$1/criteres-1-6.md"
  sed -i.bak \
    -e 's/^- \*\*13\.9\*\* Intitulé du critère 13\.9 — code$/- **13.9** Orientation — conditions réelles (question « Orientation »). Reste : tourner l’écran./' \
    -e 's/^- \*\*11\.3\*\* Intitulé du critère 11\.3 — code$/- **11.3** Étiquettes cohérentes — jugement humain. Reste : comparer les pages./' \
    "$1/criteres-7-13.md"
  rm -f "$1"/*.bak
}

run() {
  status=0
  python3 "$script" --skill "$skill" "$@" >"$output" 2>&1 || status=$?
}

variant() {
  rm -rf "$tmp_dir/$1"
  make_clean "$tmp_dir/$1"
}

make_clean "$clean"
run "$clean"/*.md
[ "$status" -eq 0 ] || fail "Le classement propre a été refusé (code $status) : $(cat "$output")"
grep -q '106 critères' "$output" || fail "Le total des critères n’est pas affiché : $(cat "$output")"
grep -q 'code 102, mixte 1, conditions réelles 2, jugement humain 1' "$output" ||
  fail "La répartition par mode est fausse : $(cat "$output")"

variant doublon
printf '%s\n' '- **2.1** Doublon — code' >>"$tmp_dir/doublon/criteres-1-6.md"
run "$tmp_dir/doublon"/criteres-*.md
[ "$status" -eq 1 ] || fail "Un doublon a été accepté (code $status)"
grep -q 'critère 2.1 en double' "$output" || fail "Le doublon n’est pas signalé : $(cat "$output")"

variant manquant
sed -i.bak '/^- \*\*12\.7\*\* /d' "$tmp_dir/manquant/criteres-7-13.md"
run "$tmp_dir/manquant"/criteres-*.md
[ "$status" -eq 1 ] || fail "Un critère manquant a été accepté (code $status)"
grep -q 'critère 12.7 manquant' "$output" || fail "Le critère manquant n’est pas signalé : $(cat "$output")"
grep -q 'thème 12 : 10 critères au lieu de 11' "$output" ||
  fail "Le compte du thème 12 n’est pas signalé : $(cat "$output")"

variant inattendu
printf '%s\n' '- **1.10** Critère inventé — code' >>"$tmp_dir/inattendu/criteres-1-6.md"
run "$tmp_dir/inattendu"/criteres-*.md
[ "$status" -eq 1 ] || fail "Un critère inexistant a été accepté (code $status)"
grep -q 'critère 1.10 inconnu' "$output" || fail "Le critère inexistant n’est pas signalé : $(cat "$output")"

variant mode
sed -i.bak 's/^\(- \*\*6\.1\*\* Intitulé du critère 6\.1\) — code$/\1 — analyse/' "$tmp_dir/mode/criteres-1-6.md"
run "$tmp_dir/mode"/criteres-*.md
[ "$status" -eq 1 ] || fail "Un mode inconnu a été accepté (code $status)"
grep -q 'criteres-1-6.md:[0-9]*: critère 6.1 : mode inconnu' "$output" ||
  fail "Le mode inconnu n’est pas signalé avec fichier et ligne : $(cat "$output")"

variant reste
sed -i.bak 's/ Reste : voir l’image\.//' "$tmp_dir/reste/criteres-1-6.md"
run "$tmp_dir/reste"/criteres-*.md
[ "$status" -eq 1 ] || fail "Une ligne mixte sans « Reste » a été acceptée (code $status)"
grep -q 'critère 1.2 : « Reste : » manquant' "$output" || fail "Le « Reste » manquant n’est pas signalé : $(cat "$output")"

variant prouve
sed -i.bak 's/ Le code prouve : NC sur un `<svg>` sans `aria-hidden`\.//' "$tmp_dir/prouve/criteres-1-6.md"
run "$tmp_dir/prouve"/criteres-*.md
[ "$status" -eq 1 ] || fail "Une ligne mixte sans « Le code prouve » a été acceptée (code $status)"
grep -q 'critère 1.2 : « Le code prouve : » manquant' "$output" ||
  fail "Le « Le code prouve » manquant n’est pas signalé : $(cat "$output")"

variant code
sed -i.bak 's/^\(- \*\*6\.2\*\* Intitulé du critère 6\.2 — code\)$/\1. Reste : rien./' "$tmp_dir/code/criteres-1-6.md"
run "$tmp_dir/code"/criteres-*.md
[ "$status" -eq 1 ] || fail "Une ligne code avec une raison a été acceptée (code $status)"
grep -q 'critère 6.2 : une ligne « code » ne porte rien après le mode' "$output" ||
  fail "La ligne code avec une raison n’est pas signalée : $(cat "$output")"

variant question
sed -i.bak 's/question « Orientation »/question « Gyroscope »/' "$tmp_dir/question/criteres-7-13.md"
run "$tmp_dir/question"/criteres-*.md
[ "$status" -eq 1 ] || fail "Une question absente du catalogue a été acceptée (code $status)"
grep -q 'critère 13.9 : question « Gyroscope » absente du catalogue de phase 2' "$output" ||
  fail "La question inconnue n’est pas signalée : $(cat "$output")"

variant sansquestion
sed -i.bak 's/ (question « Orientation »)//' "$tmp_dir/sansquestion/criteres-7-13.md"
run "$tmp_dir/sansquestion"/criteres-*.md
[ "$status" -eq 1 ] || fail "Une ligne conditions réelles sans question a été acceptée (code $status)"
grep -q 'critère 13.9 : une ligne « conditions réelles » cite sa question' "$output" ||
  fail "La question manquante n’est pas signalée : $(cat "$output")"

variant entete
sed -i.bak 's/jamais une conformité\./jamais une conformité, sauf exception./' "$tmp_dir/entete/criteres-7-13.md"
run "$tmp_dir/entete"/criteres-*.md
[ "$status" -eq 1 ] || fail "Des en-têtes divergents ont été acceptés (code $status)"
grep -q 'criteres-7-13.md : bloc des modes différent de celui de' "$output" ||
  fail "Les en-têtes divergents ne sont pas signalés : $(cat "$output")"

run "$clean/introuvable.md"
[ "$status" -eq 2 ] || fail "Un fichier introuvable n’a pas renvoyé le code 2 (code $status)"

status=0
python3 "$script" --skill "$tmp_dir/absent.md" "$clean"/*.md >"$output" 2>&1 || status=$?
[ "$status" -eq 2 ] || fail "Un SKILL.md introuvable n’a pas renvoyé le code 2 (code $status)"

echo "Classement checker tests passed"
