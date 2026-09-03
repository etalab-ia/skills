#!/usr/bin/env python3
"""Détecte les écarts entre la skill albert-api et la spec OpenAPI live d'Albert.

L'OpenAPI fait autorité (cf. SKILL.md). Ce script télécharge la spec, en extrait
un résumé normalisé (version, endpoints, enums) et le compare au snapshot committé
`openapi.snapshot.json`. En cas d'écart, il liste les différences et sort en code 1
— signal qu'il faut relire/mettre à jour SKILL.md.

Usage :
    python3 bin/check_drift.py            # compare au snapshot, exit 1 si drift
    python3 bin/check_drift.py --update   # régénère le snapshot depuis la spec live
    python3 bin/check_drift.py --spec /chemin/openapi.json   # source locale

Aucune dépendance externe (urllib + json de la stdlib).
"""

import argparse
import json
import sys
import urllib.request
from pathlib import Path

OPENAPI_URL = "https://albert.api.etalab.gouv.fr/openapi.json"
SNAPSHOT = Path(__file__).resolve().parent.parent / "openapi.snapshot.json"

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}


def load_spec(source: str) -> dict:
    """Charge la spec depuis une URL (http/https) ou un fichier local."""
    if source.startswith(("http://", "https://")):
        with urllib.request.urlopen(source, timeout=30) as r:  # noqa: S310
            return json.load(r)
    return json.loads(Path(source).read_text(encoding="utf-8"))


def summarize(spec: dict) -> dict:
    """Réduit la spec à ce qui doit déclencher une revue si ça change."""
    endpoints = {}
    for path, item in spec.get("paths", {}).items():
        for method, op in item.items():
            if method.lower() in HTTP_METHODS:
                key = f"{method.upper()} {path}"
                endpoints[key] = (op or {}).get("operationId", "")

    # Enums nommés dans components.schemas : capte p.ex. les valeurs de
    # `method` (search), `response_format` (audio), `visibility` (collections).
    enums = {}
    for name, schema in spec.get("components", {}).get("schemas", {}).items():
        if isinstance(schema, dict) and isinstance(schema.get("enum"), list):
            enums[name] = sorted(str(v) for v in schema["enum"])

    return {
        "version": spec.get("info", {}).get("version", ""),
        "endpoints": dict(sorted(endpoints.items())),
        "enums": dict(sorted(enums.items())),
    }


def diff(old: dict, new: dict) -> list[str]:
    """Liste lisible des écarts entre deux résumés."""
    out = []

    if old.get("version") != new.get("version"):
        out.append(f"version : {old.get('version')} → {new.get('version')}")

    old_ep, new_ep = old.get("endpoints", {}), new.get("endpoints", {})
    for ep in sorted(set(new_ep) - set(old_ep)):
        out.append(f"+ endpoint : {ep}")
    for ep in sorted(set(old_ep) - set(new_ep)):
        out.append(f"- endpoint : {ep}")
    for ep in sorted(set(old_ep) & set(new_ep)):
        if old_ep[ep] != new_ep[ep]:
            out.append(f"~ operationId [{ep}] : {old_ep[ep]} → {new_ep[ep]}")

    old_en, new_en = old.get("enums", {}), new.get("enums", {})
    for name in sorted(set(new_en) - set(old_en)):
        out.append(f"+ enum : {name} = {new_en[name]}")
    for name in sorted(set(old_en) - set(new_en)):
        out.append(f"- enum : {name}")
    for name in sorted(set(old_en) & set(new_en)):
        if old_en[name] != new_en[name]:
            out.append(f"~ enum [{name}] : {old_en[name]} → {new_en[name]}")

    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--spec", default=OPENAPI_URL, help="URL ou fichier OpenAPI")
    ap.add_argument("--update", action="store_true", help="régénère le snapshot")
    args = ap.parse_args()

    try:
        spec = load_spec(args.spec)
    except Exception as e:  # noqa: BLE001
        print(f"Erreur : impossible de charger la spec ({args.spec}) : {e}", file=sys.stderr)
        return 2

    summary = summarize(spec)

    if args.update:
        SNAPSHOT.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Snapshot mis à jour ({SNAPSHOT.name}) : version {summary['version']}, "
              f"{len(summary['endpoints'])} endpoints.")
        return 0

    if not SNAPSHOT.exists():
        print(f"Pas de snapshot ({SNAPSHOT.name}). Lancer --update pour l'initialiser.", file=sys.stderr)
        return 2

    old = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    changes = diff(old, summary)

    if not changes:
        print(f"✅ Aucun écart. Spec v{summary['version']}, {len(summary['endpoints'])} endpoints, "
              f"alignée sur le snapshot.")
        return 0

    print(f"⚠️  Écart(s) détecté(s) entre la spec live et le snapshot ({len(changes)}) :\n")
    for c in changes:
        print(f"  {c}")
    print("\n→ Relire SKILL.md, corriger si besoin, puis : python3 bin/check_drift.py --update")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
