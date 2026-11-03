#!/usr/bin/env python3
"""Copie la skill DSFR de numerique-gouv/dsfr-skill dans skills/dsfr/.

Usage : sync_dsfr.py <dossier skills/dsfr-skill du dépôt source> <dossier cible>

Le dépôt source reste la source de vérité : son contenu est généré depuis
@gouvfr/dsfr par son propre script. Ce script :
  - remplace tout le contenu du dossier cible par celui du dossier source,
    sauf les fichiers propres à ce dépôt (KEPT_FILES), écrits par la DINUM ;
  - renomme la skill (`name: dsfr-skill` -> `name: dsfr`) dans le
    frontmatter de SKILL.md, pour suivre le nommage de ce dépôt.

Il échoue sans rien modifier si le frontmatter source ne contient pas
exactement `name: dsfr-skill` (un renommage côté source doit être
répercuté ici à la main, pas publié tel quel), si la source contient un
lien symbolique, ou si les deux dossiers sont imbriqués. La copie est
préparée à côté de la cible et ne la remplace qu'une fois complète.
"""

import os
import shutil
import sys
import tempfile

SOURCE_NAME = "dsfr-skill"
TARGET_NAME = "dsfr"
KEPT_FILES = {"README.md", "LICENSE.md"}


class SyncError(Exception):
    pass


def renamed_skill_md(content: str) -> str:
    lines = content.split("\n")
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        raise SyncError("SKILL.md source sans frontmatter")
    frontmatter_end = lines.index("---", 1)
    name_lines = [
        i for i in range(1, frontmatter_end) if lines[i].startswith("name:")
    ]
    if len(name_lines) != 1 or lines[name_lines[0]] != f"name: {SOURCE_NAME}":
        raise SyncError(
            f"frontmatter source : `name: {SOURCE_NAME}` attendu, "
            "renommage à répercuter dans scripts/sync_dsfr.py"
        )
    lines[name_lines[0]] = f"name: {TARGET_NAME}"
    return "\n".join(lines)


def check_paths(source: str, target: str) -> None:
    real_source = os.path.realpath(source)
    real_target = os.path.realpath(target)
    if os.path.islink(target):
        raise SyncError(f"dossier cible en lien symbolique : {target}")
    if os.path.commonpath([real_source, real_target]) in (real_source, real_target):
        raise SyncError("dossiers source et cible imbriqués")
    for dirpath, dirnames, filenames in os.walk(source):
        for entry in dirnames + filenames:
            if os.path.islink(os.path.join(dirpath, entry)):
                raise SyncError(
                    f"lien symbolique non pris en charge : {os.path.join(dirpath, entry)}"
                )


def sync(source: str, target: str) -> None:
    check_paths(source, target)
    with open(os.path.join(source, "SKILL.md"), encoding="utf-8") as fh:
        skill_md = renamed_skill_md(fh.read())

    parent = os.path.dirname(os.path.abspath(target))
    os.makedirs(parent, exist_ok=True)
    staging = tempfile.mkdtemp(prefix=".sync-dsfr-", dir=parent)
    previous = os.path.join(staging, "previous")
    try:
        replacement = os.path.join(staging, "skill")
        shutil.copytree(
            source, replacement, ignore=lambda d, names: KEPT_FILES & set(names)
            if d == source else set()
        )
        with open(
            os.path.join(replacement, "SKILL.md"), "w", encoding="utf-8", newline="\n"
        ) as fh:
            fh.write(skill_md)
        for kept in KEPT_FILES:
            if os.path.isfile(os.path.join(target, kept)):
                shutil.copy2(os.path.join(target, kept), os.path.join(replacement, kept))

        if os.path.exists(target):
            os.rename(target, previous)
        try:
            os.rename(replacement, target)
        except BaseException:
            if os.path.exists(previous):
                os.rename(previous, target)
            raise
    finally:
        if os.path.exists(previous) and not os.path.exists(target):
            print(f"sync_dsfr: skill précédente conservée dans {previous}", file=sys.stderr)
        else:
            shutil.rmtree(staging)


def main(argv=None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 2:
        print(__doc__.strip().split("\n")[2], file=sys.stderr)
        return 2
    try:
        sync(*args)
    except SyncError as error:
        print(f"sync_dsfr: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
