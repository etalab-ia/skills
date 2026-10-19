#!/usr/bin/env python3
"""Vérifie la complétude du classement des critères RGAA par mode d’évaluation.

Le classement (`references/classement/*.md`) donne, ligne par ligne, le mode de
chacun des 106 critères : code, mixte, conditions réelles ou jugement humain.
Ce script contrôle qu’aucun critère ne manque ni n’est en double, que chaque
ligne suit le format attendu, que chaque question de phase 2 citée existe dans
le catalogue du `SKILL.md` et que le bloc des modes est identique dans tous les
fichiers.

Usage :
    python3 scripts/check-classement.py                 # references/classement/*.md
    python3 scripts/check-classement.py fichier.md ...  # fichiers choisis
    python3 scripts/check-classement.py --skill SKILL.md

Codes de sortie : 0 conforme, 1 classement incomplet ou mal formé,
2 erreur d’usage ou de lecture. Aucune dépendance externe.
"""

import argparse
import os
import re
import sys
from collections import Counter
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
CLASSEMENT = SKILL_DIR / "references" / "classement"

CRITERIA_PER_THEME = {1: 9, 2: 2, 3: 3, 4: 13, 5: 8, 6: 2, 7: 5, 8: 10, 9: 4, 10: 14, 11: 13, 12: 11, 13: 12}
MODES = ("code", "mixte", "conditions réelles", "jugement humain")

CRITERION = re.compile(r"^- \*\*(\d+)\.(\d+)\*\* (.*)$")
MODE = re.compile(
    r"^(?P<title>.+?) — (?P<mode>" + "|".join(MODES) + r")"
    r"(?: \(question « (?P<question>[^»]+) »\))?(?P<rest>.*)$"
)
PHASE_2 = re.compile(r"^### Phase 2\b")
QUESTION = re.compile(r"^\|\s*\*\*(?P<name>[^*]+)\*\*\s*\|")


class CheckError(Exception):
    """Erreur de lecture : code de sortie 2."""


def read_file(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8")
    except OSError as error:
        raise CheckError(f"lecture impossible : {path} ({error})") from error


def catalogue(skill: str) -> set[str]:
    """Noms des questions du tableau de la section « Phase 2 » du SKILL.md."""
    names, inside = set(), False
    for line in read_file(skill).splitlines():
        if line.startswith("### "):
            inside = bool(PHASE_2.match(line))
        elif inside and (match := QUESTION.match(line)):
            names.add(match.group("name").strip())
    if not names:
        raise CheckError(f"aucune question de phase 2 trouvée dans {skill}")
    return names


def modes_block(lines: list[str]) -> list[str]:
    """Lignes entre le titre du fichier et la première section."""
    block = []
    for line in lines[1:]:
        if line.startswith("## "):
            break
        block.append(line)
    return [line for line in block if line.strip()]


def line_errors(number: str, text: str, questions: set[str]) -> tuple[str | None, list[str]]:
    match = MODE.match(text)
    if not match:
        return None, [f"critère {number} : mode inconnu (attendu : {', '.join(MODES)})"]
    mode, question, rest = match.group("mode"), match.group("question"), match.group("rest")
    errors = []
    if mode == "code" and (question or rest.strip()):
        errors.append(f"critère {number} : une ligne « code » ne porte rien après le mode")
    if mode != "code" and "Reste : " not in rest:
        errors.append(f"critère {number} : « Reste : » manquant")
    if mode == "mixte" and "Le code prouve : " not in rest:
        errors.append(f"critère {number} : « Le code prouve : » manquant")
    if mode == "conditions réelles" and not question:
        errors.append(f"critère {number} : une ligne « conditions réelles » cite sa question de phase 2")
    if question and question not in questions:
        errors.append(f"critère {number} : question « {question} » absente du catalogue de phase 2")
    return mode, errors


def check(files: list[str], questions: set[str]) -> int:
    errors, seen, reference_block = [], Counter(), None
    per_file = {}
    for path in files:
        lines = read_file(path).splitlines()
        block = modes_block(lines)
        if reference_block is None:
            reference_block = (path, block)
        elif block != reference_block[1]:
            errors.append(f"{path} : bloc des modes différent de celui de {reference_block[0]}")
        modes = Counter()
        for line_number, line in enumerate(lines, start=1):
            match = CRITERION.match(line)
            if not match:
                continue
            theme, index = int(match.group(1)), int(match.group(2))
            number = f"{theme}.{index}"
            seen[(theme, index)] += 1
            if index > CRITERIA_PER_THEME.get(theme, 0) or index < 1:
                errors.append(f"{path}:{line_number}: critère {number} inconnu")
            mode, line_errs = line_errors(number, match.group(3), questions)
            errors.extend(f"{path}:{line_number}: {error}" for error in line_errs)
            if mode:
                modes[mode] += 1
        per_file[path] = modes

    for (theme, index), count in sorted(seen.items()):
        if count > 1:
            errors.append(f"critère {theme}.{index} en double ({count} lignes)")
    for theme, expected in CRITERIA_PER_THEME.items():
        for index in range(1, expected + 1):
            if (theme, index) not in seen:
                errors.append(f"critère {theme}.{index} manquant")
        found = sum(1 for (t, i) in seen if t == theme and 1 <= i <= expected)
        if found != expected:
            errors.append(f"thème {theme} : {found} critères au lieu de {expected}")

    for error in errors:
        print(error)
    total = Counter()
    for path, modes in per_file.items():
        total.update(modes)
        print(f"{path} : {sum(modes.values())} critères — {summary(modes)}")
    print(f"Total : {sum(total.values())} critères — {summary(total)} ; {len(errors)} erreur(s).")
    return 1 if errors else 0


def summary(modes: Counter) -> str:
    return ", ".join(f"{mode} {modes[mode]}" for mode in MODES)


def default_files() -> list[str]:
    return [os.path.relpath(path) for path in sorted(CLASSEMENT.glob("*.md"))]


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("files", nargs="*", help="fichiers de classement (défaut : references/classement/*.md)")
    parser.add_argument("--skill", default=str(SKILL_DIR / "SKILL.md"), help="SKILL.md qui porte le catalogue de phase 2")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        files = args.files or default_files()
        if not files:
            raise CheckError(f"aucun fichier de classement dans {CLASSEMENT}")
        return check(files, catalogue(args.skill))
    except CheckError as error:
        print(f"erreur : {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
