#!/usr/bin/env python3
"""Contrôle et régénère le texte officiel des critères RGAA dans les références.

Chaque critère des fichiers `references/criteres-*.md` porte un bloc
« **Texte officiel N.M :** » généré depuis `sources/criteres.json`, copie du
fichier publié par la DINUM (dépôt DISIC/accessibilite.numerique.gouv.fr).
Le bloc reprend mot pour mot l’intitulé, les tests numérotés, les cas
particuliers et les notes techniques ; pour un critère classé « jugement
humain », l’intitulé seul, car l’assistant n’en tranche pas les tests. Les
termes du glossaire sont en italique ; `references/glossaire.md` est généré
depuis `sources/glossaire.json`.

Usage :
    python3 scripts/officiel.py           # contrôle : aucun écart avec la source
    python3 scripts/officiel.py --write   # réécrit les blocs et le glossaire

Codes de sortie : 0 conforme, 1 écart avec la source, 2 erreur d’usage ou de
lecture. Aucune dépendance externe ; Python 3.8 minimum.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent

MODES = ("code", "mixte", "conditions réelles", "jugement humain")
CLASSEMENT_LINE = re.compile(r"^- \*\*(\d+\.\d+)\*\* .+? — (" + "|".join(MODES) + r")\b")
BLOCK_START = re.compile(r"^\*\*Texte officiel (\d+\.\d+) :\*\*")
LINK = re.compile(r"\[([^\]]+)\]\(#[^)]*\)")
SPAN_LANG = re.compile(r'<span lang="[^"]*">([^<]*)</span>')
GLOSSARY_HEADER = (
    "# Glossaire officiel du RGAA 4.1.2\n\n"
    "Généré par `scripts/officiel.py` depuis `sources/glossaire.json` : ne pas modifier à la main.\n"
    "Chercher le terme en italique d’un texte officiel parmi les titres `###` ci-dessous.\n"
)


class CheckError(Exception):
    """Erreur de lecture : code de sortie 2."""


def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise CheckError(f"lecture impossible : {path} ({error})") from error


def clean(text: str) -> str:
    return SPAN_LANG.sub(r"\1", LINK.sub(r"*\1*", text)).strip()


def items(entries: list, indent: str) -> list[str]:
    lines = []
    for entry in entries:
        if isinstance(entry, str):
            lines.append(f"{indent}- {clean(entry)}")
        elif isinstance(entry, dict) and set(entry) == {"ul"}:
            lines.extend(items(entry["ul"], indent + "  "))
        else:
            raise CheckError(f"structure inattendue dans la source : {entry!r}")
    return lines


def render_block(number: str, criterion: dict, mode: str) -> str:
    lines = [f"**Texte officiel {number} :** {clean(criterion['title'])}"]
    if mode == "jugement humain":
        return "\n".join(lines)
    for index, test in criterion["tests"].items():
        lines.append(f"- **{number}.{index}** {clean(test[0])}")
        lines.extend(f"  - {clean(condition)}" for condition in test[1:])
    if criterion.get("particularCases"):
        lines.append("- *Cas particuliers :*")
        lines.extend(items(criterion["particularCases"], "  "))
    if criterion.get("technicalNote"):
        lines.append("- *Notes techniques :*")
        lines.extend(items(criterion["technicalNote"], "  "))
    return "\n".join(lines)


def html_to_markdown(body: str) -> str:
    text = re.sub(r"<code>(.*?)</code>", r"`\1`", body, flags=re.S)
    text = re.sub(r"<li>\s*", "\n- ", text)
    text = re.sub(r"</p>|<br\s*/?>|</ul>|</ol>", "\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    lines = [re.sub(r"\s+", " ", line).strip() for line in text.splitlines()]
    return "\n".join(line for line in lines if line)


def render_glossary(glossary: dict) -> str:
    parts = [GLOSSARY_HEADER]
    for entry in glossary["glossary"]:
        parts.append(f"### {html.unescape(entry['title']).strip()}\n\n{html_to_markdown(entry['body'])}\n")
    return "\n".join(parts)


def load_modes(classement: Path) -> dict[str, str]:
    modes = {}
    for path in sorted(classement.glob("*.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            match = CLASSEMENT_LINE.match(line)
            if match:
                modes[match.group(1)] = match.group(2)
    return modes


def expected_blocks(criteria: dict, modes: dict[str, str]) -> tuple[dict[str, str], list[str]]:
    blocks, errors = {}, []
    for topic in criteria["topics"]:
        for wrapper in topic["criteria"]:
            criterion = wrapper["criterium"]
            number = f"{topic['number']}.{criterion['number']}"
            if number not in modes:
                errors.append(f"critère {number} : absent du classement, mode inconnu")
                continue
            blocks[number] = render_block(number, criterion, modes[number])
    return blocks, errors


def find_blocks(lines: list[str]) -> list[tuple[str, int, int]]:
    """(numéro, première ligne, ligne après le bloc) : un bloc finit à la première ligne vide."""
    found, index = [], 0
    while index < len(lines):
        match = BLOCK_START.match(lines[index])
        if not match:
            index += 1
            continue
        end = index + 1
        while end < len(lines) and lines[end].strip():
            end += 1
        found.append((match.group(1), index, end))
        index = end
    return found


def run(args) -> int:
    criteria = read_json(Path(args.source))
    glossary = read_json(Path(args.glossary_source))
    references = sorted(Path(args.references).glob("criteres-*.md"))
    if not references:
        raise CheckError(f"aucun fichier criteres-*.md dans {args.references}")
    blocks, errors = expected_blocks(criteria, load_modes(Path(args.classement)))

    seen: dict[str, str] = {}
    for path in references:
        lines = path.read_text(encoding="utf-8").splitlines()
        changed = False
        for number, start, end in reversed(find_blocks(lines)):
            where = f"{path}:{start + 1}"
            if number in seen:
                errors.append(f"{where}: critère {number} déjà présent dans {seen[number]}")
                continue
            seen[number] = where
            if number not in blocks:
                errors.append(f"{where}: critère {number} absent de la source")
                continue
            expected = blocks[number].splitlines()
            if lines[start:end] != expected:
                if args.write:
                    lines[start:end] = expected
                    changed = True
                else:
                    errors.append(f"{where}: texte officiel {number} différent de la source")
        if changed:
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            print(f"réécrit : {path}")

    for number in blocks:
        if number not in seen:
            errors.append(f"critère {number} : aucun bloc « Texte officiel » dans les références")

    glossary_path = Path(args.glossary)
    rendered = render_glossary(glossary)
    current = glossary_path.read_text(encoding="utf-8") if glossary_path.exists() else None
    if current != rendered:
        if args.write:
            glossary_path.write_text(rendered, encoding="utf-8")
            print(f"réécrit : {glossary_path}")
        else:
            errors.append(f"{glossary_path} : différent de la source (relancer avec --write)")

    for error in errors:
        print(error)
    print(f"Texte officiel : {len(seen)} blocs pour {len(blocks)} critères de la source ; {len(errors)} erreur(s).")
    return 1 if errors else 0


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--write", action="store_true", help="réécrire les blocs et le glossaire au lieu de contrôler")
    parser.add_argument("--source", default=str(SKILL_DIR / "sources" / "criteres.json"))
    parser.add_argument("--glossary-source", default=str(SKILL_DIR / "sources" / "glossaire.json"))
    parser.add_argument("--classement", default=str(SKILL_DIR / "references" / "classement"))
    parser.add_argument("--references", default=str(SKILL_DIR / "references"))
    parser.add_argument("--glossary", default=str(SKILL_DIR / "references" / "glossaire.md"))
    return parser.parse_args()


def main() -> int:
    try:
        return run(parse_args())
    except CheckError as error:
        print(f"erreur : {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
