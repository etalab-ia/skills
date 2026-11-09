#!/bin/sh
set -eu

script_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
script="$script_dir/check-form-names.py"
tmp_dir=$(mktemp -d)
trap 'rm -rf "$tmp_dir"' EXIT HUP INT TERM

fail() {
  echo "$1" >&2
  exit 1
}

clean="$tmp_dir/propre.md"
faulty="$tmp_dir/fautif.md"
exception="$tmp_dir/exception.md"
ignored="$tmp_dir/ignore.md"
limits="$tmp_dir/limites.md"
output="$tmp_dir/sortie.txt"

cat >"$clean" <<'EOF'
# Formulaires

Un `<input>` cité dans la prose n’est pas vérifié.

```erb
<div class="fr-input-group">
  <label class="fr-label" for="email_<%= index %>">Adresse e-mail</label>
  <input class="fr-input" id="email_<%= index %>" name="contacts[][email]" type="email">
</div>
<input
  class="fr-input"
  id="tel"
  name="telephone"
  type="tel">
<select class="fr-select" id="departement" name="departement"></select>
<textarea class="fr-input" id="message" name="message"></textarea>
<input type="submit" value="Envoyer">
<input type="button" value="Ajouter">
<input type="reset" value="Effacer">
<input type="image" src="envoyer.svg" alt="Envoyer">
<input TYPE="Submit" value="Valider">
<input type=submit value="Envoyer sans guillemets">
<input class="fr-input" id="dynamique" name="<%= champ %>">
<button class="fr-btn" type="submit">Envoyer</button>
```

```html
<input class="fr-input" id="q" name="q" type="search">
```
EOF

cat >"$faulty" <<'EOF'
```erb
<input class="fr-input" id="tel" type="tel" aria-describedby="hint-tel">
<select class="fr-select" id="departement"></select>
<textarea class="fr-input" id="message"></textarea>
<input class="fr-input" id="nom" data-name="nom" aria-label="name=nom">
<input
  class="fr-input"
  id="ville">
```

```html
<input type="checkbox" id="cgu">
<input type="hidden" id="jeton" value="abc">
<input class="fr-input" id="vide" name="">
<input class="fr-input" id="vide-simple" name=' '>
<input class="fr-input" id="sans-valeur" name>
<input aria-label="type=button" type="text" id="faux-bouton">
<input type="text" type="submit" id="doublon">
```
EOF

cat >"$exception" <<'EOF'
```erb
<!-- sans name : piloté en JavaScript -->
<input type="checkbox" class="fr-toggle__input" id="raccourcis-actifs">
<input type="checkbox" class="fr-toggle__input" id="secousse-active">
<%# sans name : piloté en JavaScript %>
<input type="checkbox" class="fr-toggle__input" id="contraste-renforce">
<!-- sans name : piloté en JavaScript --><input type="checkbox" id="theme-sombre">
```
EOF

cat >"$ignored" <<'EOF'
<input id="hors-bloc">

```tsx
<input id="tel" type="tel" aria-describedby="hint-tel" />
<select id="departement"></select>
```

```
<input id="sans-langage">
```

```css
input[type="tel"] { color: #000; }
```

```erb
<!-- <input id="commente"> -->
<%# <input id="commente-erb"> %>
<%= f.text_field :email, class: "fr-input" %>
```
EOF

cat >"$limits" <<'EOF'
```erb
<input class="fr-input" <%= "required" if obligatoire %> name="nom">
<input id="a" placeholder="type=submit">
<input-group class="x"></input-group>
<!-- sans name : piloté en JavaScript -->
<p>Texte</p>
<input id="loin">
<input value="<%= "name=nom" %>">
<input value="<%= "type=submit" %>" id="faux-bouton-erb">
```

```html+erb
<input id="variante">
```

```erb
<input id="non-ferme">
EOF

status=0
python3 "$script" "$clean" >"$output" 2>&1 || status=$?
[ "$status" -eq 0 ] || fail "Le fichier propre a été refusé (code $status) : $(cat "$output")"

status=0
python3 "$script" "$faulty" >"$output" 2>&1 || status=$?
[ "$status" -eq 1 ] || fail "Les champs sans name n’ont pas été refusés (code $status) : $(cat "$output")"
for line in 2 3 4 5 6 12 13 14 15 16 17 18; do
  grep -q "fautif.md:$line: champ sans name" "$output" ||
    fail "Le champ de la ligne $line n’est pas signalé : $(cat "$output")"
done
[ "$(grep -c 'champ sans name' "$output")" -eq 12 ] ||
  fail "Le fichier fautif n’a pas donné douze signalements : $(cat "$output")"

status=0
python3 "$script" "$exception" >"$output" 2>&1 || status=$?
[ "$status" -eq 1 ] || fail "Une exception a dispensé plus d’un champ (code $status) : $(cat "$output")"
grep -q "exception.md:4: champ sans name" "$output" ||
  fail "Le champ qui suit un champ dispensé n’est pas signalé : $(cat "$output")"
[ "$(grep -c 'champ sans name' "$output")" -eq 1 ] ||
  fail "Une exception déclarée n’a pas dispensé le champ suivant : $(cat "$output")"

status=0
python3 "$script" "$ignored" >"$output" 2>&1 || status=$?
[ "$status" -eq 0 ] || fail "Un champ hors bloc HTML ou ERB, en commentaire ou généré par un helper a été vérifié (code $status) : $(cat "$output")"

status=0
python3 "$script" "$limits" >"$output" 2>&1 || status=$?
[ "$status" -eq 1 ] || fail "Les cas limites n’ont pas été refusés (code $status) : $(cat "$output")"
for line in 3 7 8 9 13 17; do
  grep -q "limites.md:$line: champ sans name" "$output" ||
    fail "Le champ de la ligne $line des cas limites n’est pas signalé : $(cat "$output")"
done
[ "$(grep -c 'champ sans name' "$output")" -eq 6 ] ||
  fail "Une balise ERB entre attributs ou un élément personnalisé a été signalé : $(cat "$output")"
grep -q "6 champ(s) sans name, 7 champ(s) vérifié(s)" "$output" ||
  fail "Le décompte des cas limites est faux : $(cat "$output")"

status=0
python3 "$script" "$exception" >"$output" 2>&1 || status=$?
grep -q "1 champ(s) sans name, 1 champ(s) vérifié(s)" "$output" ||
  fail "Des champs dispensés ont été comptés comme vérifiés : $(cat "$output")"

status=0
python3 "$script" "$tmp_dir/introuvable.md" >"$output" 2>&1 || status=$?
[ "$status" -eq 2 ] || fail "Un fichier introuvable n’a pas renvoyé le code 2 (code $status)"

status=0
python3 - "$script_dir" "$tmp_dir" >"$output" 2>&1 <<'PY' || status=$?
import importlib.util
import pathlib
import sys

script_dir, tmp_dir = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location(
    "check_form_names", pathlib.Path(script_dir) / "check-form-names.py"
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

echo "Form name checker tests passed"
