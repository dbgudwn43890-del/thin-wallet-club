#!/usr/bin/env python3
"""Run all structure lock validations."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]

VALIDATORS = [
    "scripts/validate_structure.py",
    "scripts/validate_empty_production_dirs.py",
    "scripts/validate_schemas.py",
]


def main():
    for validator in VALIDATORS:
        print(f"\nRunning {validator}...", flush=True)
        result = subprocess.run([sys.executable, str(ROOT / validator)], cwd=ROOT)
        if result.returncode != 0:
            print(f"\nValidation failed: {validator}", flush=True)
            return result.returncode

    print("\nAll validations passed. Structure is ready for Git baseline locking.", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
