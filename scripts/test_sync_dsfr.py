#!/usr/bin/env python3
"""Tests de scripts/sync_dsfr.py sur une arborescence temporaire.

Cas couverts :
  - la skill copiée s'appelle `dsfr`, le reste de SKILL.md est intact ;
  - README.md et LICENSE.md propres à ce dépôt survivent à la sync, et
    un fichier supprimé côté source disparaît de la copie ;
  - un README.md upstream ne remplace pas celui de ce dépôt ;
  - un `name` source inattendu fait échouer la sync sans toucher la copie ;
  - une copie qui échoue en cours de route laisse la skill précédente intacte ;
  - des dossiers source et cible imbriqués, ou un lien symbolique dans la
    source, font échouer la sync sans rien supprimer ni copier.
"""

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sync_dsfr  # noqa: E402

SKILL_MD = "---\nname: {name}\ndescription: DSFR en HTML\n---\n\n# DSFR\n"


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


class SyncDsfrTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.source = os.path.join(self.tmp.name, "source")
        self.target = os.path.join(self.tmp.name, "skills", "dsfr")
        write(os.path.join(self.source, "SKILL.md"), SKILL_MD.format(name="dsfr-skill"))
        write(os.path.join(self.source, "composants", "bouton", "index.md"), "bouton\n")

    def tearDown(self):
        self.tmp.cleanup()

    def test_published_skill_is_named_dsfr(self):
        self.assertEqual(sync_dsfr.main([self.source, self.target]), 0)
        self.assertEqual(
            read(os.path.join(self.target, "SKILL.md")), SKILL_MD.format(name="dsfr")
        )
        self.assertEqual(
            read(os.path.join(self.target, "composants", "bouton", "index.md")),
            "bouton\n",
        )

    def test_keeps_local_readme_and_license_and_drops_removed_files(self):
        write(os.path.join(self.target, "README.md"), "readme DINUM\n")
        write(os.path.join(self.target, "LICENSE.md"), "licence\n")
        write(os.path.join(self.target, "composants", "retire", "index.md"), "x\n")

        self.assertEqual(sync_dsfr.main([self.source, self.target]), 0)

        self.assertEqual(read(os.path.join(self.target, "README.md")), "readme DINUM\n")
        self.assertEqual(read(os.path.join(self.target, "LICENSE.md")), "licence\n")
        self.assertFalse(os.path.exists(os.path.join(self.target, "composants", "retire")))

    def test_unexpected_source_name_fails_without_touching_target(self):
        write(os.path.join(self.source, "SKILL.md"), SKILL_MD.format(name="dsfr-v2"))
        write(os.path.join(self.target, "SKILL.md"), SKILL_MD.format(name="dsfr"))

        self.assertEqual(sync_dsfr.main([self.source, self.target]), 1)

        self.assertEqual(
            read(os.path.join(self.target, "SKILL.md")), SKILL_MD.format(name="dsfr")
        )
        self.assertFalse(os.path.exists(os.path.join(self.target, "composants")))

    def test_upstream_readme_does_not_replace_local_one(self):
        write(os.path.join(self.source, "README.md"), "readme upstream\n")
        write(os.path.join(self.target, "README.md"), "readme DINUM\n")

        self.assertEqual(sync_dsfr.main([self.source, self.target]), 0)

        self.assertEqual(read(os.path.join(self.target, "README.md")), "readme DINUM\n")

    def test_failed_copy_leaves_previous_skill_intact(self):
        write(os.path.join(self.target, "SKILL.md"), SKILL_MD.format(name="dsfr"))
        write(os.path.join(self.target, "composants", "ancien", "index.md"), "x\n")
        unreadable = os.path.join(self.source, "composants", "bouton", "index.md")
        os.chmod(unreadable, 0)
        try:
            with self.assertRaises(OSError):
                sync_dsfr.sync(self.source, self.target)
        finally:
            os.chmod(unreadable, 0o644)

        self.assertTrue(os.path.exists(os.path.join(self.target, "composants", "ancien")))
        self.assertEqual(os.listdir(os.path.dirname(self.target)), ["dsfr"])

    def test_refuses_nested_source_and_target(self):
        self.assertEqual(sync_dsfr.main([self.source, self.source]), 1)
        self.assertEqual(
            sync_dsfr.main([self.source, os.path.join(self.source, "copie")]), 1
        )
        self.assertTrue(
            os.path.exists(os.path.join(self.source, "composants", "bouton", "index.md"))
        )

    def test_refuses_symlink_in_source(self):
        outside = os.path.join(self.tmp.name, "ailleurs.md")
        write(outside, "hors skill\n")
        os.symlink(outside, os.path.join(self.source, "lien.md"))

        self.assertEqual(sync_dsfr.main([self.source, self.target]), 1)
        self.assertFalse(os.path.exists(self.target))


if __name__ == "__main__":
    unittest.main()
