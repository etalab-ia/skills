#!/bin/sh
set -eu

API_URL=${ANSSI_GUIDES_API_URL:-https://messervices.cyber.gouv.fr/api/guides}
SCAN_DATE=${SCAN_DATE:-$(date -u +%Y-%m-%d)}
OUTPUT_PATH=${1:-}
script_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
tracked_ids_file="$script_dir/tracked-guide-ids.json"
included_english_ids_file="$script_dir/included-english-guide-ids.json"

json_file=$(mktemp)
catalogue_tmp=
trap 'rm -f "$json_file"; [ -z "$catalogue_tmp" ] || rm -f "$catalogue_tmp"' EXIT HUP INT TERM

curl -fsSL "$API_URL" >"$json_file"

jq -e --slurpfile included_english_ids "$included_english_ids_file" '
  type == "array" and
  ($included_english_ids[0] | type == "array" and length == (unique | length)) and
  ([.[] | . as $guide
    | select($guide.langue == "FR" or ($included_english_ids[0] | index($guide.id)))]
  ) as $guides |
  ($guides | map(select(.langue == "FR")) | length > 0) and
  ([$guides[].id] | length == (unique | length)) and
  ([$guides[] | select(.langue == "EN") | .id] | sort
    == ($included_english_ids[0] | sort)) and
  all($guides[];
    (.id | type == "string" and length > 0) and
    (.nom | type == "string" and length > 0) and
    (.dateMiseAJour | type == "string" and length > 0) and
    (.collections | type == "array") and
    (.besoins | type == "array") and
    (.documents | type == "array")
  )
' "$json_file" >/dev/null

render_catalogue() {
  jq -r --arg scan_date "$SCAN_DATE" \
    --slurpfile tracked_ids "$tracked_ids_file" \
    --slurpfile included_english_ids "$included_english_ids_file" '
  def md:
    gsub("[\\r\\n]+"; " ") | gsub("^\\s+|\\s+$"; "") | gsub("\\|"; "\\|");
  def display_values:
    if length == 0 then "—" else map(md) | join(", ") end;
  def need_label:
    {
      "ETRE_SENSIBILISE": "Être sensibilisé",
      "REAGIR": "Réagir",
      "SECURISER": "Sécuriser",
      "SE_FORMER": "Se former"
    }[.] // .;

  [.[] | . as $guide
    | select($guide.langue == "FR" or ($included_english_ids[0] | index($guide.id)))] as $guides |
  ($guides | map(select(.langue == "FR")) | length) as $french_count |
  ($guides | map(select(.langue == "EN")) | length) as $english_count |
  ($tracked_ids[0] - [$guides[].id]) as $missing_tracked |
  if ($missing_tracked | length) > 0 then
    error("Guides suivis absents de l\u2019API : " + ($missing_tracked | join(", ")))
  else
    [
      "# Catalogue des guides ANSSI — \($guides | length) publications",
      "",
      "**Date du scan : \($scan_date).** Source canonique : [API des guides MesServicesCyber](https://messervices.cyber.gouv.fr/api/guides). Le tableau contient \($french_count) guides en français et \($english_count) publication en anglais sans équivalent français ; les traductions anglaises de guides français sont exclues.",
      "",
      "**Légende** : ★ = guide déjà digéré et tracé règle par règle dans la skill [`securite-developpement`](../../securite-developpement/SKILL.md) — pour une question de développement d\u2019application, utiliser cette skill plutôt que le PDF.",
      "",
      "**Limites de ce tableau** :",
      "- `dateMiseAJour` est la date exposée par le catalogue, pas nécessairement celle de la version du document — le numéro de version et la référence ANSSI-PA/PG doivent être vérifiés dans le PDF ;",
      "- une même fiche peut regrouper plusieurs documents (par exemple « Mécanismes cryptographiques ») ; leurs URLs exactes sont disponibles dans le champ `documents` de l\u2019API.",
      "",
      "Trié du plus récent au plus ancien.",
      "",
      "| Guide | Mise à jour API | Collection | Besoin | Thématique | Fiche |",
      "|---|---|---|---|---|---|"
    ] +
    ($guides
      | group_by(.dateMiseAJour)
      | sort_by(.[0].dateMiseAJour)
      | reverse
      | map(sort_by(.nom))
      | add
      | map(
          . as $guide |
          "| " +
          (if $tracked_ids[0] | index($guide.id) then "★ " else "" end) +
          (.nom | md) +
          (if $guide.langue == "EN" then " *(en anglais, sans équivalent français)*" else "" end) + " | " +
          (.dateMiseAJour[0:10]) + " | " +
          ((.collections // []) | display_values) + " | " +
          ((.besoins // []) | map(need_label) | display_values) + " | " +
          ((if (.thematique // "") == "" then "—" else .thematique end) | md) + " | " +
          "[lien](https://messervices.cyber.gouv.fr/guides/" + .id + ") |"
        )) +
    [
      "",
      "---",
      "",
      "## Méthode de re-scan",
      "",
      "Le catalogue est généré depuis l\u2019API JSON, sans analyser la page HTML :",
      "",
      "```bash",
      "skills/anssi-guides/scripts/generate-catalogue.sh skills/anssi-guides/references/catalogue.md",
      "```",
      "",
      "Le générateur vérifie que les identifiants français sont uniques, que les champs structurés nécessaires sont présents et que les 13 fiches suivies par `securite-developpement` existent toujours. Il conserve leur marqueur ★.",
      "Le test hors ligne `skills/anssi-guides/scripts/test-generate-catalogue.sh` couvre aussi le filtrage de langue, l\u2019exception anglaise déclarée, le rejet des doublons, la disparition d\u2019une fiche suivie et la préservation du catalogue en cas d\u2019échec.",
      "",
      "Pour rechercher sans régénérer le fichier :",
      "",
      "```bash",
      "curl -fsSL https://messervices.cyber.gouv.fr/api/guides | jq --arg q \"tls\" --slurpfile included_english skills/anssi-guides/scripts/included-english-guide-ids.json '\''",
      "  .[] | . as $guide",
      "  | select($guide.langue == \"FR\" or ($included_english[0] | index($guide.id)))",
      "  | select(([.nom, .description, .thematique] + .collections + .besoins)",
      "      | map(ascii_downcase) | any(contains($q | ascii_downcase)))",
      "  | {id, nom, dateMiseAJour, collections, besoins, thematique, documents}",
      "'\''",
      "```",
      "",
      "Toute nouvelle fiche apparaît au prochain re-scan. Si la date d\u2019une fiche ★ change, vérifier les documents listés par l\u2019API puis rejouer l\u2019extraction de `securite-developpement` selon sa méthode documentée dans [`sources.md`](../../securite-developpement/references/sources.md)."
    ]
    | .[]
  end
' "$json_file"
}

if [ -z "$OUTPUT_PATH" ]; then
  render_catalogue
else
  output_dir=$(dirname -- "$OUTPUT_PATH")
  catalogue_tmp=$(mktemp "$output_dir/.catalogue.XXXXXX")
  render_catalogue >"$catalogue_tmp"
  chmod 0644 "$catalogue_tmp"
  mv -f "$catalogue_tmp" "$OUTPUT_PATH"
  catalogue_tmp=
fi
