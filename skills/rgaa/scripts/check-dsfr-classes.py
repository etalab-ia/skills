#!/usr/bin/env python3
"""Vérifie que les classes fr-* des exemples de code existent dans le DSFR publié.

Les exemples des fichiers de référence sont recopiés tels quels : une classe
inventée (ex. `fr-radio`) s'y propage dans les projets. Ce script extrait les
classes `fr-*` des blocs de code Markdown et les cherche dans le CSS de la
dernière version publiée de `@gouvfr/dsfr` (résolue à chaque lancement).

Usage :
    python3 scripts/check-dsfr-classes.py                    # references/*.md
    python3 scripts/check-dsfr-classes.py fichier.md         # fichiers choisis
    python3 scripts/check-dsfr-classes.py --dsfr-version 1.15.4
    python3 scripts/check-dsfr-classes.py --css dsfr.min.css # CSS local

Codes de sortie : 0 conforme, 1 classe inconnue, 2 erreur d'usage ou de lecture.
Aucune dépendance externe (urllib + re de la stdlib).
"""

import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

REGISTRY_URL = "https://registry.npmjs.org/@gouvfr/dsfr/latest"
CDN_URL = "https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@{version}/dist/{path}"
CSS_PATHS = ("dsfr.min.css", "utility/utility.min.css")
REFERENCES = Path(__file__).resolve().parent.parent / "references"

VERSION = re.compile(r"^\d+\.\d+\.\d+$")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
CSS_COMMENT = re.compile(r"/\*.*?\*/", re.DOTALL)
CSS_BLOCK = re.compile(r"([^{}]*)([{}])")
CSS_CLASS = re.compile(r"\.((?:[\w-]|\\.)+)")
CSS_ESCAPE = re.compile(r"\\(.)")
IDENTIFIER_VALUE = re.compile(
    r"""\b(?:id|for|htmlFor|name|href|aria-[\w-]+|data-[\w-]+)\s*[=:]\s*\{?\s*(["'`])(.*?)\1"""
)
FR_CLASS = re.compile(r"(?<![\w-])fr-[a-z0-9]+(?:(?:--|__|-)[a-z0-9]+)*(?:@[a-z]+)?(?![\w-])")


class CheckError(Exception):
    """Erreur de lecture ou de téléchargement : code de sortie 2."""


def read_url(url: str) -> str:
    try:
        with urllib.request.urlopen(url, timeout=30) as response:  # noqa: S310
            return response.read().decode("utf-8")
    except OSError as error:
        raise CheckError(f"téléchargement impossible : {url} ({error})") from error


def read_file(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8")
    except OSError as error:
        raise CheckError(f"lecture impossible : {path} ({error})") from error


def resolve_version() -> str:
    version = json.loads(read_url(REGISTRY_URL)).get("version", "")
    if not VERSION.match(version):
        raise CheckError(f"version DSFR inattendue dans le registre npm : {version!r}")
    return version


def css_classes(css: str) -> set[str]:
    """Classes déclarées dans les sélecteurs, hors commentaires et valeurs."""
    classes = set()
    for prelude, delimiter in CSS_BLOCK.findall(CSS_COMMENT.sub("", css)):
        if delimiter == "{" and not prelude.lstrip().startswith("@"):
            for name in CSS_CLASS.findall(prelude):
                classes.add(CSS_ESCAPE.sub(r"\1", name))
    return classes


def code_lines(markdown: str):
    """(numéro, ligne) de chaque ligne située dans un bloc de code délimité."""
    fence = None
    for number, line in enumerate(markdown.splitlines(), start=1):
        match = FENCE.match(line)
        if fence is None:
            if match:
                fence = match.group(1)
        elif match and match.group(1)[0] == fence[0] and len(match.group(1)) >= len(fence) \
                and not line.strip().strip(fence[0]):
            fence = None
        else:
            yield number, line


def class_tokens(line: str) -> list[str]:
    """Classes fr-* d'une ligne, hors valeurs d'identifiants (id, for, aria-*…)."""
    masked = IDENTIFIER_VALUE.sub(lambda m: " " * len(m.group(0)), line)
    return FR_CLASS.findall(masked)


def load_classes(args) -> tuple[set[str], str]:
    if args.css:
        css = "\n".join(read_file(path) for path in args.css)
        return css_classes(css), "CSS local : " + ", ".join(args.css)
    version = args.dsfr_version or resolve_version()
    if not VERSION.match(version):
        raise CheckError(f"version DSFR invalide : {version!r}")
    css = "\n".join(read_url(CDN_URL.format(version=version, path=p)) for p in CSS_PATHS)
    return css_classes(css), f"DSFR {version}"


def check(files: list[str], known: set[str], source: str) -> int:
    checked, unknown = set(), 0
    for path in files:
        for number, line in code_lines(read_file(path)):
            for name in class_tokens(line):
                checked.add(name)
                if name not in known:
                    unknown += 1
                    print(f"{path}:{number}: classe inconnue « {name} » ({source})")
    print(f"{unknown} classe(s) inconnue(s), {len(checked)} classe(s) distincte(s) vérifiée(s) ({source}).")
    return 1 if unknown else 0


def default_files() -> list[str]:
    return [os.path.relpath(path) for path in sorted(REFERENCES.glob("*.md"))]


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("files", nargs="*", help="fichiers Markdown (défaut : references/*.md)")
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--css", action="append", help="fichier CSS local (répétable)")
    source.add_argument("--dsfr-version", help="version précise du DSFR (défaut : la dernière)")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        known, source = load_classes(args)
        return check(args.files or default_files(), known, source)
    except CheckError as error:
        print(f"erreur : {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
