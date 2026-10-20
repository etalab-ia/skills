#!/usr/bin/env python3
r"""Génère les index.json consommables par la config skills.urls d'OpenCode.

OpenCode lit `<base>/index.json` au format :
    {"skills": [{"name": "rgaa", "version": "…", "files": ["SKILL.md", "…"]}]}

Chaque fichier de `files` est téléchargé depuis `<base>/<name>/<fichier>` ;
`name` ne doit contenir ni `/` ni `\`, et `files` doit contenir `SKILL.md`.

Ce script génère deux fichiers :
  - skills/index.json                  : sous-dossiers de skills/ avec un SKILL.md
  - skills/.experimental/index.json    : idem pour skills/.experimental/

Règles de génération :
  - files   : tous les fichiers réguliers de la skill, récursivement, en chemins
              POSIX relatifs et triés. Sont exclus les fichiers cachés (nom
              commençant par "."), les dossiers __pycache__ et les index.json.
  - version : les 12 premiers caractères hexadécimaux d'un sha256 calculé sur
              (chemin + contenu) de chaque fichier, dans l'ordre trié. Résultat
              identique sur toutes les machines (pas de date ni de commit).
  - skills triées par name. Sortie JSON avec indentation 2, ensure_ascii=False
    et un saut de ligne final.

Option --check : ne rien écrire ; code 1 si un index sur disque diffère de
l'index généré (le nom du fichier concerné est affiché sur stderr).
"""

import argparse
import hashlib
import json
import os
import sys

# Fichiers et dossiers exclus de `files`.
_EXCLUDED_DIRS = {"__pycache__"}


def _is_hidden(relpath: str) -> bool:
    # Un fichier est caché si l'une de ses composantes commence par ".".
    return any(part.startswith(".") for part in relpath.split("/"))


def collect_files(root: str) -> list:
    """Retourne la liste triée des fichiers réguliers de la skill (POSIX)."""
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        # On retire sur place les dossiers à ne pas parcourir.
        dirnames[:] = [
            d for d in dirnames if d not in _EXCLUDED_DIRS and not d.startswith(".")
        ]
        for filename in filenames:
            if filename.startswith("."):
                continue
            if filename == "index.json":
                continue
            full = os.path.join(dirpath, filename)
            if os.path.isfile(full):
                rel = os.path.relpath(full, root)
                # os.walk produit des chemins OS ; on force POSIX.
                files.append(rel.replace(os.sep, "/"))
    return sorted(files)


def compute_version(root: str, files: list) -> str:
    """12 premiers hex d'un sha256 sur (chemin + contenu) de chaque fichier trié."""
    h = hashlib.sha256()
    for rel in files:
        full = os.path.join(root, *rel.split("/"))
        with open(full, "rb") as fh:
            content = fh.read()
        h.update(rel.encode("utf-8"))
        h.update(content)
    return h.hexdigest()[:12]


def build_index(skills_dir: str) -> dict:
    """Construit l'index d'un dossier contenant des sous-dossiers de skills."""
    skills = []
    for entry in sorted(os.listdir(skills_dir)):
        skill_dir = os.path.join(skills_dir, entry)
        if not os.path.isdir(skill_dir):
            continue
        if entry.startswith("."):
            continue
        if not os.path.isfile(os.path.join(skill_dir, "SKILL.md")):
            continue
        files = collect_files(skill_dir)
        skills.append(
            {
                "name": entry,
                "version": compute_version(skill_dir, files),
                "files": files,
            }
        )
    return {"skills": skills}


def dump_index(index: dict) -> str:
    return (
        json.dumps(index, indent=2, ensure_ascii=False)
        + "\n"
    )


def generate_all(repo_root: str):
    """Retourne {chemin_relatif: contenu} pour les deux index."""
    outputs = {
        os.path.join("skills", "index.json"): dump_index(
            build_index(os.path.join(repo_root, "skills"))
        ),
        os.path.join("skills", ".experimental", "index.json"): dump_index(
            build_index(os.path.join(repo_root, "skills", ".experimental"))
        ),
    }
    results = {}
    for rel, content in outputs.items():
        results[rel] = content
    return results


def main(argv=None, repo_root=None) -> int:
    parser = argparse.ArgumentParser(
        description="Génère les index.json pour skills.urls d'OpenCode."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Ne rien écrire ; code 1 si un index sur disque diffère.",
    )
    args = parser.parse_args(argv)

    if repo_root is None:
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    generated = generate_all(repo_root)

    if args.check:
        ok = True
        for rel, content in generated.items():
            path = os.path.join(repo_root, rel)
            if not os.path.exists(path):
                print(f"missing: {rel}", file=sys.stderr)
                ok = False
                continue
            with open(path, "r", encoding="utf-8") as fh:
                if fh.read() != content:
                    print(f"outdated: {rel}", file=sys.stderr)
                    ok = False
        return 0 if ok else 1

    for rel, content in generated.items():
        path = os.path.join(repo_root, rel)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(content)
    return 0


if __name__ == "__main__":
    sys.exit(main())
