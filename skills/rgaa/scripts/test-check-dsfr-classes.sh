#!/bin/sh
set -eu

script_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
script="$script_dir/check-dsfr-classes.py"
tmp_dir=$(mktemp -d)
trap 'rm -rf "$tmp_dir"' EXIT HUP INT TERM

http_proxy=http://127.0.0.1:9
https_proxy=http://127.0.0.1:9
export http_proxy https_proxy

fail() {
  echo "$1" >&2
  exit 1
}

css="$tmp_dir/dsfr-minimal.css"
clean="$tmp_dir/formulaires-propre.md"
faulty="$tmp_dir/formulaires-fautif.md"
malformed="$tmp_dir/formulaires-malformes.md"
quoted="$tmp_dir/valeurs-commentaires.md"
rails="$tmp_dir/rails.md"
react="$tmp_dir/react.md"
not_classes="$tmp_dir/hors-classes.md"
comments="$tmp_dir/commentaires.md"
output="$tmp_dir/sortie.txt"

cat >"$css" <<'EOF'
/* .fr-radio */
.fr-input-group,.fr-input-group--error,.fr-label{margin:0}.fr-input{display:block}
@media (min-width:48em){.fr-fieldset__element--inline\@md{display:inline}}
.fr-radio-group input[type=radio]:not(.fr-fieldset){opacity:0}
.fr-fieldset__element{background:url(a.fr-radio.svg)}
.fr-btn{color:#000091}
EOF

cat >"$clean" <<'EOF'
# Formulaires

La classe fr-radio n’existe pas dans le DSFR.

```erb
<%# Classes fr-* du DSFR %>
<div class="fr-input-group" lang="fr-FR" data-fr-js-input="true">
  <label class="fr-label" for="fr-radio">Adresse e-mail</label>
  <input class="fr-input" id="fr-radio" name="fr-radio" aria-describedby="fr-radio-hint">
</div>
<fieldset class="fr-fieldset" style="color: var(--fr-radio)">
  <div class="fr-fieldset__element fr-fieldset__element--inline@md">
    <div class="fr-radio-group"></div>
  </div>
</fieldset>
```

Après le bloc, fr-radio reste de la prose.
EOF

cp "$clean" "$faulty"
cat >>"$faulty" <<'EOF'

```erb
<input class="fr-radio" type="radio" id="civilite_mme" name="civilite">
```
EOF

cat >"$malformed" <<'EOF'
```erb
<input class="fr-input fr-radio-" type="radio" id="civilite_mme">
<button class="fr-btn--" type="submit">Envoyer</button>
<span class="fr-Radio">Civilité</span>
```
EOF

cat >"$quoted" <<'EOF'
```erb
<input title="Étape # 1" class="fr-radio">
<span title="Aide // assistance" className="fr-radio" />
<input title="a \" b" class="fr-radio">
```
EOF

cat >"$rails" <<'EOF'
```ruby
<%= f.radio_button :civilite, :mme, class: %w[fr-btn fr-radio] %>
```
EOF

cat >"$react" <<'EOF'
```tsx
<div className={cx("fr-input-group", { "fr-input-group--error": hasError })}>
  <label className="fr-label" htmlFor={"fr-radio"}>Adresse e-mail</label>
  <input className={`fr-input ${extra}`} id={'fr-radio'} aria-describedby={`fr-radio-hint`} />
  <Button className={fr.cx("fr-btn")} nativeButtonProps={{ id: "fr-radio" }}>Valider</Button>
  <span className={clsx("fr-radio")} />
</div>
```
EOF

cat >"$not_classes" <<'EOF'
```tsx
// fr-radio n’est pas une classe du DSFR
const route = "/fr-aide"
const page = `/aide/fr-radio`
const motif = "les classes fr-* du DSFR"
<%# classes fr-* du DSFR %>
<%# ne pas écrire "fr-radio" %>
{/* "fr-radio" */}
<html lang="fr-fr">
<html lang={"fr-fr"}>
<a hrefLang="fr-fr" href="/aide">Aide</a>
{/* fr-radio */}
<!-- fr-radio -->
<%# fr-radio %>
# fr-radio
/* fr-radio */
<a href="https://exemple.gouv.fr/fr-aide" class="fr-btn">Aide</a>
```
EOF

cat >"$comments" <<'EOF'
```erb
<input class="fr-radio"> // fr-inconnue
<%# commentaire %><input class="fr-radio">
<!-- commentaire --><input class="fr-radio">
<a href="https://exemple.gouv.fr/aide" class="fr-radio">Aide</a>
<input class="fr-radio"> # commentaire
<img src="assets/*.png" class="fr-radio">
<div style="color: #fff" class="fr-radio"></div>
```
EOF

status=0
python3 "$script" --css "$css" "$not_classes" >"$output" 2>&1 || status=$?
[ "$status" -eq 0 ] || fail "Un commentaire, une langue ou une route a été pris pour une classe (code $status) : $(cat "$output")"

status=0
python3 "$script" --css "$css" "$comments" >"$output" 2>&1 || status=$?
[ "$status" -eq 1 ] || fail "Une classe voisine d’un commentaire n’a pas été vérifiée (code $status) : $(cat "$output")"
for line in 2 3 4 5 6 7 8; do
  grep -q "commentaires.md:$line: classe inconnue « fr-radio »" "$output" ||
    fail "La classe fr-radio de la ligne $line a été masquée : $(cat "$output")"
done
[ "$(grep -c 'classe inconnue' "$output")" -eq 7 ] ||
  fail "Une classe dans un commentaire a été vérifiée : $(cat "$output")"

status=0
python3 "$script" --css "$css" "$clean" >"$output" 2>&1 || status=$?
[ "$status" -eq 0 ] || fail "Le fichier propre a été refusé (code $status) : $(cat "$output")"

status=0
python3 "$script" --css "$css" "$faulty" >"$output" 2>&1 || status=$?
[ "$status" -eq 1 ] || fail "La classe fr-radio n’a pas été refusée (code $status) : $(cat "$output")"
faulty_line=$(grep -n 'class="fr-radio"' "$faulty" | cut -d: -f1)
grep -q "formulaires-fautif.md:$faulty_line: classe inconnue « fr-radio »" "$output" ||
  fail "La classe fr-radio n’est pas signalée avec fichier et ligne : $(cat "$output")"
[ "$(grep -c 'classe inconnue' "$output")" -eq 1 ] ||
  fail "Une classe hors bloc de code ou un identifiant a été signalé : $(cat "$output")"

status=0
python3 "$script" --css "$css" "$malformed" >"$output" 2>&1 || status=$?
[ "$status" -eq 1 ] || fail "Une classe fr-* mal formée a été acceptée (code $status) : $(cat "$output")"
for name in 'fr-radio-' 'fr-btn--' 'fr-Radio'; do
  grep -q "classe inconnue « $name »" "$output" ||
    fail "La classe mal formée $name n’est pas signalée : $(cat "$output")"
done
[ "$(grep -c 'classe inconnue' "$output")" -eq 3 ] ||
  fail "Le fichier aux classes mal formées n’a pas donné trois signalements : $(cat "$output")"

status=0
python3 "$script" --css "$css" "$quoted" >"$output" 2>&1 || status=$?
[ "$status" -eq 1 ] || fail "Une valeur contenant un marqueur de commentaire a masqué la classe suivante (code $status) : $(cat "$output")"
for line in 2 3 4; do
  grep -q "valeurs-commentaires.md:$line: classe inconnue « fr-radio »" "$output" ||
    fail "La classe de la ligne $line a été masquée par un marqueur dans une chaîne : $(cat "$output")"
done
[ "$(grep -c 'classe inconnue' "$output")" -eq 3 ] ||
  fail "Les valeurs entre guillemets n’ont pas donné trois signalements : $(cat "$output")"

status=0
python3 "$script" --css "$css" "$rails" >"$output" 2>&1 || status=$?
[ "$status" -eq 1 ] || fail "La classe d’un helper Rails n’a pas été vérifiée (code $status)"
grep -q 'rails.md:2: classe inconnue « fr-radio »' "$output" ||
  fail "La classe fr-radio du helper Rails n’est pas signalée : $(cat "$output")"
[ "$(grep -c 'classe inconnue' "$output")" -eq 1 ] ||
  fail "La classe fr-btn du helper Rails a été refusée : $(cat "$output")"

status=0
python3 "$script" --css "$css" "$react" >"$output" 2>&1 || status=$?
[ "$status" -eq 1 ] || fail "La classe d’un composant React n’a pas été vérifiée (code $status)"
grep -q 'react.md:6: classe inconnue « fr-radio »' "$output" ||
  fail "La classe fr-radio du composant React n’est pas signalée : $(cat "$output")"
[ "$(grep -c 'classe inconnue' "$output")" -eq 1 ] ||
  fail "Un identifiant JSX entre accolades a été pris pour une classe : $(cat "$output")"

status=0
python3 "$script" --css "$tmp_dir/introuvable.css" "$clean" >"$output" 2>&1 || status=$?
[ "$status" -eq 2 ] || fail "Un CSS introuvable n’a pas renvoyé le code 2 (code $status)"

status=0
python3 "$script" --css "$css" --dsfr-version 1.15.4 "$clean" >"$output" 2>&1 || status=$?
[ "$status" -eq 2 ] || fail "--css et --dsfr-version ont été acceptés ensemble (code $status)"

status=0
python3 - "$script_dir" "$tmp_dir" >"$output" 2>&1 <<'PY' || status=$?
import importlib.util
import pathlib
import sys

script_dir, tmp_dir = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location(
    "check_dsfr_classes", pathlib.Path(script_dir) / "check-dsfr-classes.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

references = pathlib.Path(tmp_dir) / "references"
(references / "corrections").mkdir(parents=True, exist_ok=True)
(references / "themes.md").write_text("x", encoding="utf-8")
(references / "corrections" / "formulaires.md").write_text("x", encoding="utf-8")
module.REFERENCES = references
names = sorted(pathlib.Path(path).name for path in module.default_files())
assert names == ["formulaires.md", "themes.md"], names
PY
[ "$status" -eq 0 ] || fail "Les sous-dossiers de references/ échappent au contrôle par défaut : $(cat "$output")"

echo "DSFR class checker tests passed"
