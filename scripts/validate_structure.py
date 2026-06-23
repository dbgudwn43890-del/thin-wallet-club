#!/usr/bin/env python3
"""Validate the locked project structure for thin_wallet_club."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_ROOT_FILES = [
    "CLAUDE.md",
    "AGENTS.md",
    "README.md",
    ".gitignore",
]

REQUIRED_DIRS = [
    ".claude/agents",
    ".claude/commands",
    ".claude/skills",
    "brand",
    "content",
    "sources",
    "templates",
    "workflows",
    "ops",
    "schemas",
    "docs",
    "data",
    "reviews",
    "drafts",
    "outputs",
]

REQUIRED_AGENTS = [
    ".claude/agents/trend-scout.md",
    ".claude/agents/policy-scout.md",
    ".claude/agents/verifier.md",
    ".claude/agents/curator.md",
    ".claude/agents/editor.md",
    ".claude/agents/design-director.md",
    ".claude/agents/growth-analyst.md",
]

REQUIRED_COMMANDS = [
    ".claude/commands/research-candidates.md",
    ".claude/commands/verify-candidate.md",
    ".claude/commands/curate-candidates.md",
    ".claude/commands/plan-cardnews.md",
    ".claude/commands/write-script.md",
    ".claude/commands/create-design-prompt.md",
    ".claude/commands/review-before-upload.md",
]

REQUIRED_SKILLS = [
    ".claude/skills/cardnews-planning/SKILL.md",
    ".claude/skills/fact-verification/SKILL.md",
    ".claude/skills/magazine-design/SKILL.md",
]

REQUIRED_OPS = [
    "ops/operating_principles.md",
    "ops/status_rules.md",
    "ops/naming_rules.md",
    "ops/source_rules.md",
    "ops/human_review_rules.md",
    "ops/quality_rules.md",
    "ops/change_log_rules.md",
    "ops/upload_rules.md",
]

REQUIRED_SCHEMAS = [
    "schemas/candidate.schema.yml",
    "schemas/verification.schema.yml",
    "schemas/brief.schema.yml",
    "schemas/script.schema.yml",
    "schemas/design_prompt.schema.yml",
    "schemas/performance.schema.yml",
]

REQUIRED_DOCS = [
    "docs/system_overview.md",
    "docs/agent_handoff_protocol.md",
    "docs/content_lifecycle.md",
]

FORBIDDEN_PATHS = [
    ".agents",
    "engine",
]


def missing_files(paths):
    return [path for path in paths if not (ROOT / path).is_file()]


def missing_dirs(paths):
    return [path for path in paths if not (ROOT / path).is_dir()]


def existing_forbidden_paths(paths):
    return [path for path in paths if (ROOT / path).exists()]


def main():
    failures = []

    for label, paths in [
        ("root files", REQUIRED_ROOT_FILES),
        ("agents", REQUIRED_AGENTS),
        ("commands", REQUIRED_COMMANDS),
        ("skills", REQUIRED_SKILLS),
        ("ops files", REQUIRED_OPS),
        ("schema files", REQUIRED_SCHEMAS),
        ("docs files", REQUIRED_DOCS),
    ]:
        missing = missing_files(paths)
        if missing:
            failures.append((label, missing))

    missing_required_dirs = missing_dirs(REQUIRED_DIRS)
    if missing_required_dirs:
        failures.append(("directories", missing_required_dirs))

    forbidden = existing_forbidden_paths(FORBIDDEN_PATHS)
    if forbidden:
        failures.append(("forbidden paths", forbidden))

    if failures:
        print("Structure validation failed.")
        for label, paths in failures:
            print(f"\nMissing or invalid {label}:")
            for path in paths:
                print(f"  - {path}")
        return 1

    print("Structure validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
