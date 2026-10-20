#!/usr/bin/env python3
"""Tests de scripts/build_index.py sur une arborescence temporaire.

Cas couverts :
  - les fichiers cachés et __pycache__ sont exclus de `files`, et
    `skills/.experimental` n'est pas listé dans l'index officiel ;
  - `version` est stable d'une exécution à l'autre et change si un octet
    d'un fichier change ;
  - `--check` sort en 1 sur un index périmé et en 0 sur un index à jour.
"""

import os
import shutil
import sys
import tempfile
import unittest

# Rend le module build_index importable et appelle main() avec une racine
# arbitraire pour les tests d'intégration.
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPTS_DIR)

import build_index  # noqa: E402


def make_skill(skills_dir, name, extra="contenu"):
    """Crée une skill basique avec un SKILL.md et un fichier dans references/."""
    root = os.path.join(skills_dir, name)
    os.makedirs(os.path.join(root, "references"))
    with open(os.path.join(root, "SKILL.md"), "w", encoding="utf-8") as fh:
        fh.write(f"# {name}\n")
    with open(os.path.join(root, "references", "r.md"), "w", encoding="utf-8") as fh:
        fh.write(extra + "\n")


class CollectFilesTest(unittest.TestCase):
    def test_excludes_hidden_and_pycache(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = os.path.join(tmp, "skill")
            os.makedirs(os.path.join(root, "__pycache__"))
            os.makedirs(os.path.join(root, ".hidden_dir"))
            for rel in (
                "SKILL.md",
                ".dotfile",
                "__pycache__/cache.pyc",
                ".hidden_dir/nope.md",
                "ok.txt",
                "index.json",
            ):
                path = os.path.join(root, rel)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write("x\n")

            files = build_index.collect_files(root)
            self.assertEqual(files, ["SKILL.md", "ok.txt"])


class BuildIndexTest(unittest.TestCase):
    def test_experimental_not_in_official_index(self):
        with tempfile.TemporaryDirectory() as tmp:
            make_skill(os.path.join(tmp, "skills"), "alpha")
            make_skill(os.path.join(tmp, "skills", ".experimental"), "beta")
            official = build_index.build_index(os.path.join(tmp, "skills"))
            exp = build_index.build_index(
                os.path.join(tmp, "skills", ".experimental")
            )
            names = [s["name"] for s in official["skills"]]
            self.assertNotIn(".experimental", names)
            self.assertEqual(names, ["alpha"])
            self.assertEqual([s["name"] for s in exp["skills"]], ["beta"])

    def test_version_stable_and_changes_with_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            make_skill(os.path.join(tmp, "skills"), "a")
            idx1 = build_index.build_index(os.path.join(tmp, "skills"))
            idx2 = build_index.build_index(os.path.join(tmp, "skills"))
            self.assertEqual(idx1["skills"][0]["version"], idx2["skills"][0]["version"])

            # On modifie un octet d'un fichier.
            target = os.path.join(tmp, "skills", "a", "references", "r.md")
            with open(target, "a", encoding="utf-8") as fh:
                fh.write("y")
            idx3 = build_index.build_index(os.path.join(tmp, "skills"))
            self.assertNotEqual(
                idx1["skills"][0]["version"], idx3["skills"][0]["version"]
            )


class CheckTest(unittest.TestCase):
    def build_tree(self):
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        make_skill(os.path.join(tmp, "skills"), "alpha")
        make_skill(os.path.join(tmp, "skills", ".experimental"), "beta")
        return tmp

    def run_check(self, repo_root):
        return build_index.main(["--check"], repo_root=repo_root)

    def test_check_up_to_date_returns_0(self):
        repo_root = self.build_tree()
        self.assertEqual(build_index.main([], repo_root=repo_root), 0)
        self.assertEqual(self.run_check(repo_root), 0)

    def test_check_outdated_returns_1(self):
        repo_root = self.build_tree()
        build_index.main([], repo_root=repo_root)
        # On rend un index obsolète puis on vérifie qu'il est détecté.
        index_path = os.path.join(repo_root, "skills", "index.json")
        with open(index_path, "w", encoding="utf-8") as fh:
            fh.write("{}")
        self.assertEqual(self.run_check(repo_root), 1)


if __name__ == "__main__":
    unittest.main()
