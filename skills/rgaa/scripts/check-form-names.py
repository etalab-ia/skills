#!/usr/bin/env python3
"""Vérifie que les champs de formulaire des exemples HTML et ERB portent un attribut name.

Les exemples des fichiers de référence sont recopiés tels quels : un champ sans
`name` ne transmet pas sa valeur à l’envoi du formulaire. Ce script lit les
blocs de code Markdown marqués `html`, `erb` ou `html+erb` et signale chaque
`<input>`, `<select>` ou `<textarea>` sans `name` non vide, sauf les boutons
(`type` `submit`, `button`, `reset`, `image`).

Les blocs `tsx`, `jsx` et sans langage ne sont pas lus : les exemples React ne
portent que les attributs d’accessibilité. Les helpers Rails (`f.text_field`)
génèrent le `name` eux-mêmes et ne sont pas vérifiés. Un champ en commentaire
(`<!-- -->`, `<%# %>`) est ignoré.

Exception : un commentaire `<!-- sans name : raison -->` ou `<%# sans name :
raison %>` placé juste avant un champ, sans rien d’autre entre eux que des
espaces ou des sauts de ligne, dispense ce seul champ (interrupteur piloté en
JavaScript, par exemple).

Usage :
    python3 scripts/check-form-names.py                 # references/**/*.md
    python3 scripts/check-form-names.py fichier.md      # fichiers choisis

Codes de sortie : 0 conforme, 1 champ sans name, 2 erreur d’usage ou de lecture.
Aucune dépendance externe.
"""

import argparse
import os
import re
import sys
from pathlib import Path

REFERENCES = Path(__file__).resolve().parent.parent / "references"

LANGUAGES = {"html", "erb", "html+erb"}
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})\s*([^\s`]*)")
# Une balise de champ, lue sur le bloc où commentaires et expressions ERB sont
# déjà neutralisés : une valeur entre guillemets peut contenir `>`.
FIELD = re.compile(r"""<(input|select|textarea)(?=[\s/>])(?:"[^"]*"|'[^']*'|[^>"'])*>""", re.IGNORECASE)
COMMENT = re.compile(r"<!--.*?-->|<%#.*?%>", re.DOTALL)
EXCEPTION = re.compile(r"^(?:<!--|<%#)\s*sans name\s*:", re.IGNORECASE)
# Une expression ERB est opaque, même entre guillemets : ses chaînes Ruby
# (`<%= "name=nom" %>`) ne sont ni des attributs ni des fins de valeur.
ERB = re.compile(r"<%.*?%>", re.DOTALL)
# Un attribut : son nom, puis une valeur facultative, entre guillemets ou non.
ATTRIBUTE = re.compile(r"""([^\s"'=<>/]+)(?:\s*=\s*("[^"]*"|'[^']*'|[^\s"'=<>`]+))?""")
BUTTON_TYPES = {"submit", "button", "reset", "image"}


class CheckError(Exception):
    """Erreur de lecture : code de sortie 2."""


def read_file(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8")
    except OSError as error:
        raise CheckError(f"lecture impossible : {path} ({error})") from error


def code_blocks(markdown: str):
    """(numéro de la première ligne, texte) de chaque bloc `html`, `erb` ou `html+erb`.

    Un bloc resté ouvert en fin de fichier est lu jusqu’à la dernière ligne,
    comme le fait `check-dsfr-classes.py`.
    """
    fence, language, start, lines = None, "", 0, []
    for number, line in enumerate(markdown.splitlines(), start=1):
        match = FENCE.match(line)
        if fence is None:
            if match:
                fence, language, start, lines = match.group(1), match.group(2).lower(), number + 1, []
        elif match and match.group(1)[0] == fence[0] and len(match.group(1)) >= len(fence) \
                and not line.strip().strip(fence[0]):
            if language in LANGUAGES:
                yield start, "\n".join(lines)
            fence = None
        else:
            lines.append(line)
    if fence is not None and language in LANGUAGES:
        yield start, "\n".join(lines)


def attributes(element: str, tag: str) -> dict[str, str]:
    """Attributs de la balise, noms en minuscules, valeurs sans guillemets.

    Comme en HTML, la première occurrence d’un attribut l’emporte, et un
    attribut sans valeur vaut la chaîne vide.
    """
    found = {}
    for match in ATTRIBUTE.finditer(tag[len(element) + 1:-1]):
        value = match.group(2) or ""
        if value[:1] in "\"'":
            value = value[1:-1]
        found.setdefault(match.group(1).lower(), value)
    return found


def needs_name(element: str, tag: str) -> bool:
    """Vrai si la balise est un champ qui doit porter un name non vide et n’en a pas."""
    found = attributes(element, tag)
    if found.get("name", "").strip():
        return False
    is_button = element.lower() == "input" and found.get("type", "").strip().lower() in BUTTON_TYPES
    return not is_button


def fields(block: str):
    """(décalage, balise, manquant) de chaque champ vérifié, hors commentaires et exceptions.

    Les commentaires deviennent des espaces. Une expression ERB devient une
    suite de `_` : dans une valeur, elle la laisse non vide (`name="<%= champ %>"`) ;
    entre deux attributs, elle n’en forme aucun qui compte. Le masquage garde
    la longueur du texte : les décalages renvoient au bloc d’origine.
    """
    exceptions = [c.end() for c in COMMENT.finditer(block) if EXCEPTION.match(c.group(0))]
    masked = COMMENT.sub(lambda m: " " * len(m.group(0)), block)
    masked = ERB.sub(lambda m: "_" * len(m.group(0)), masked)
    for field in FIELD.finditer(masked):
        # Une exception ne dispense que le champ qui la suit immédiatement.
        if any(end <= field.start() and not masked[end:field.start()].strip() for end in exceptions):
            continue
        tag = " ".join(block[field.start():field.end()].split())
        yield field.start(), tag, needs_name(field.group(1), field.group(0))


def check(files: list[str]) -> int:
    missing = checked = 0
    for path in files:
        for start, block in code_blocks(read_file(path)):
            for offset, tag, is_missing in fields(block):
                checked += 1
                if is_missing:
                    missing += 1
                    line = start + block.count("\n", 0, offset)
                    print(f"{path}:{line}: champ sans name « {tag} »")
    print(f"{missing} champ(s) sans name, {checked} champ(s) vérifié(s).")
    return 1 if missing else 0


def default_files() -> list[str]:
    return [os.path.relpath(path) for path in sorted(REFERENCES.rglob("*.md"))]


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("files", nargs="*", help="fichiers Markdown (défaut : references/**/*.md)")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        return check(args.files or default_files())
    except CheckError as error:
        print(f"erreur : {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
