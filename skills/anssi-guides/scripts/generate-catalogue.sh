#!/bin/sh
set -eu

API_URL=${ANSSI_GUIDES_API_URL:-https://messervices.cyber.gouv.fr/api/guides}
SCAN_DATE=${SCAN_DATE:-$(date -u +%Y-%m-%d)}
OUTPUT_PATH=${1:-}
script_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
tracked_ids_file="$script_dir/tracked-guide-ids.json"

json_file=$(mktemp)
catalogue_tmp=
trap 'rm -f "$json_file"; [ -z "$catalogue_tmp" ] || rm -f "$catalogue_tmp"' EXIT HUP INT TERM

curl -fsSL "$API_URL" >"$json_file"

jq -e '
  type == "array" and
  ([.[] | select(.langue == "FR")] | length > 0) and
  ([.[] | select(.langue == "FR") | .id] | length == (unique | length)) and
  all(.[] | select(.langue == "FR");
    (.id | type == "string" and length > 0) and
    (.nom | type == "string" and length > 0) and
    (.dateMiseAJour | type == "string" and length > 0) and
    (.collections | type == "array") and
    (.besoins | type == "array") and
    (.documents | type == "array")
  )
' "$json_file" >/dev/null

render_catalogue() {
  jq -r --arg scan_date "$SCAN_DATE" --slurpfile tracked_ids "$tracked_ids_file" '
  def md:
    gsub("[\\r\\n]+"; " ") | gsub("\\|"; "\\|");
  def values:
    if length == 0 then "—" else map(md) | join(", ") end;
  def need_label:
    {
      "ETRE_SENSIBILISE": "Être sensibilisé",
      "REAGIR": "Réagir",
      "SECURISER": "Sécuriser",
      "SE_FORMER": "Se former"
    }[.] // .;

  [.[] | select(.langue == "FR")] as $guides |
  ($tracked_ids[0] - [$guides[].id]) as $missing_tracked |
  if ($missing_tracked | length) > 0 then
    error("Guides suivis absents de l\u2019API : " + ($missing_tracked | join(", ")))
  else
    [
      "# Catalogue des guides ANSSI — \($guides | length) guides en français",
      "",
      "**Date du scan : \($scan_date).** Source canonique : [API des guides MesServicesCyber](https://messervices.cyber.gouv.fr/api/guides). Le filtre `langue == \"FR\"` est appliqué explicitement ; les traductions anglaises ne figurent pas dans ce tableau.",
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
      | sort_by(.dateMiseAJour, .nom)
      | reverse
      | map(
          . as $guide |
          "| " +
          (if $tracked_ids[0] | index($guide.id) then "★ " else "" end) +
          (.nom | md) + " | " +
          (.dateMiseAJour[0:10]) + " | " +
          ((.collections // []) | values) + " | " +
          ((.besoins // []) | map(need_label) | values) + " | " +
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
      "Le test hors ligne `skills/anssi-guides/scripts/test-generate-catalogue.sh` couvre aussi le filtrage de langue, le rejet des doublons, la disparition d\u2019une fiche suivie et la préservation du catalogue en cas d\u2019échec.",
      "",
      "Pour rechercher sans régénérer le fichier :",
      "",
      "```bash",
      "curl -fsSL https://messervices.cyber.gouv.fr/api/guides | jq --arg q \"tls\" '\''",
      "  .[]",
      "  | select(.langue == \"FR\")",
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
