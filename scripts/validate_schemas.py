#!/usr/bin/env python3
"""Validate that schema files parse as YAML."""

from pathlib import Path
import sys


try:
    import yaml
except ImportError:
    print("PyYAML is required. Install with: pip install -r requirements.txt")
    sys.exit(1)


ROOT = Path(__file__).resolve().parents[1]

SCHEMA_FILES = [
    "schemas/candidate.schema.yml",
    "schemas/verification.schema.yml",
    "schemas/brief.schema.yml",
    "schemas/script.schema.yml",
    "schemas/design_prompt.schema.yml",
    "schemas/performance.schema.yml",
]


def main():
    failures = []

    for schema_file in SCHEMA_FILES:
        path = ROOT / schema_file
        if not path.is_file():
            failures.append((schema_file, "missing file"))
            continue

        try:
            with path.open("r", encoding="utf-8") as handle:
                yaml.safe_load(handle)
        except yaml.YAMLError as error:
            failures.append((schema_file, str(error)))

    if failures:
        print("Schema validation failed.")
        for schema_file, error in failures:
            print(f"\n{schema_file}:")
            print(f"  {error}")
        return 1

    print("Schema validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
