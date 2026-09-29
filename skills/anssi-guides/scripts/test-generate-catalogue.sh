#!/bin/sh
set -eu

script_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
tmp_dir=$(mktemp -d)
trap 'rm -rf "$tmp_dir"' EXIT HUP INT TERM

fixture="$tmp_dir/guides.json"
output="$tmp_dir/catalogue.md"

jq '
  map({
    id: .,
    nom: ("Guide " + .),
    description: "Description de test",
    langue: "FR",
    collections: ["Collection test"],
    dateMiseAJour: "2026-09-29T00:00:00.000Z",
    thematique: "Thématique test",
    besoins: ["SECURISER"],
    documents: [{libelle: "PDF", url: "https://example.test/guide.pdf"}]
  }) + [{
    id: "ANSSI-views-on-crypto-agility",
    nom: "ANSSI views on crypto agility",
    description: "English-only publication",
    langue: "EN",
    collections: ["Cryptographie"],
    dateMiseAJour: "2026-01-19T00:00:00.000Z",
    thematique: "Cryptographie post-quantique",
    besoins: ["SECURISER"],
    documents: [{libelle: "PDF", url: "https://example.test/crypto-agility.pdf"}]
  }, {
    id: "english-guide",
    nom: "English guide",
    description: "Must be excluded",
    langue: "EN",
    collections: ["Test"],
    dateMiseAJour: "2026-09-29T00:00:00.000Z",
    thematique: "Test",
    besoins: ["SECURISER"],
    documents: []
  }]
' "$script_dir/tracked-guide-ids.json" >"$fixture"

ANSSI_GUIDES_API_URL="file://$fixture" SCAN_DATE=2026-09-29 \
  "$script_dir/generate-catalogue.sh" "$output"

grep -q '^# Catalogue des guides ANSSI — 14 publications$' "$output"
[ "$(grep -c '^| ★' "$output")" -eq 13 ]
grep -q '| Sécuriser |' "$output"
grep -q 'ANSSI views on crypto agility.*en anglais, sans équivalent français' "$output"
if grep -q 'guides/english-guide)' "$output"; then
  echo "Une fiche non française a été incluse" >&2
  exit 1
fi

jq '. + [.[0]]' "$fixture" >"$tmp_dir/duplicate.json"
printf 'catalogue existant\n' >"$output"
if ANSSI_GUIDES_API_URL="file://$tmp_dir/introuvable.json" \
  "$script_dir/generate-catalogue.sh" "$output" >/dev/null 2>&1; then
  echo "Un échec de récupération a été accepté" >&2
  exit 1
fi
grep -qx 'catalogue existant' "$output"

if ANSSI_GUIDES_API_URL="file://$tmp_dir/duplicate.json" \
  "$script_dir/generate-catalogue.sh" "$output" >/dev/null 2>&1; then
  echo "Un identifiant français dupliqué a été accepté" >&2
  exit 1
fi
grep -qx 'catalogue existant' "$output"

jq 'del(.[0])' "$fixture" >"$tmp_dir/missing.json"
if ANSSI_GUIDES_API_URL="file://$tmp_dir/missing.json" \
  "$script_dir/generate-catalogue.sh" "$output" >/dev/null 2>&1; then
  echo "La disparition d’un guide suivi a été acceptée" >&2
  exit 1
fi
grep -qx 'catalogue existant' "$output"

jq 'map(select(.id != "ANSSI-views-on-crypto-agility"))' "$fixture" >"$tmp_dir/missing-english.json"
if ANSSI_GUIDES_API_URL="file://$tmp_dir/missing-english.json" \
  "$script_dir/generate-catalogue.sh" "$output" >/dev/null 2>&1; then
  echo "La disparition de l’exception anglaise a été acceptée" >&2
  exit 1
fi
grep -qx 'catalogue existant' "$output"

echo "Catalogue generator tests passed"
