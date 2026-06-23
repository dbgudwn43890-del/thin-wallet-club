#!/usr/bin/env python3
"""Ensure production directories are empty before content production starts."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]

PRODUCTION_DIRS = [
    "data/candidates",
    "data/verified",
    "data/rejected",
    "data/archive",
    "data/performance",
    "reviews/human_review_queue",
    "reviews/approved",
    "reviews/revision_needed",
    "drafts/briefs",
    "drafts/scripts",
    "drafts/design_prompts",
    "drafts/captions",
    "outputs/reviewed",
    "outputs/published",
]

ALLOWED_FILENAMES = {".gitkeep", ".DS_Store"}


def find_unexpected_files(directory):
    path = ROOT / directory
    if not path.is_dir():
        return [f"{directory} (missing directory)"]

    unexpected = []
    for item in sorted(path.rglob("*")):
        if item.is_file() and item.name not in ALLOWED_FILENAMES:
            unexpected.append(str(item.relative_to(ROOT)))
    return unexpected


def main():
    failures = {}

    for directory in PRODUCTION_DIRS:
        unexpected = find_unexpected_files(directory)
        if unexpected:
            failures[directory] = unexpected

    if failures:
        print("Empty production directory validation failed.")
        print("Only .gitkeep and .DS_Store are allowed before content production starts.")
        for directory, files in failures.items():
            print(f"\n{directory}:")
            for file_path in files:
                print(f"  - {file_path}")
        return 1

    print("Empty production directory validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
