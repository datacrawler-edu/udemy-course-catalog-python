#!/usr/bin/env python3
"""Validate that public input examples stay synchronized with the documented contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


MARKER = "<!-- apify-input-example:complete -->"


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read JSON from {path}: {exc}") from exc


def _keys(value: Any, label: str) -> set[str]:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be a JSON object")
    return set(value)


def _fenced_json_after_marker(markdown: str, path: Path) -> dict[str, Any]:
    pattern = re.compile(
        re.escape(MARKER) + r"\s*```json\s*(?P<body>\{.*?\})\s*```",
        flags=re.IGNORECASE | re.DOTALL,
    )
    match = pattern.search(markdown)
    if not match:
        raise ValueError(f"{path} is missing a JSON block after {MARKER}")
    try:
        value = json.loads(match.group("body"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid complete input JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"complete input example in {path} must be a JSON object")
    return value


def _documented_fields(reference: str) -> set[str]:
    return {
        field
        for field in re.findall(r"^\|\s*`([^`]+)`\s*\|", reference, flags=re.MULTILINE)
    }


def _difference(expected: set[str], actual: set[str]) -> str:
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    parts: list[str] = []
    if missing:
        parts.append(f"missing={missing}")
    if extra:
        parts.append(f"extra={extra}")
    return ", ".join(parts) or "no differences"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--actor-schema", type=Path, help="Optional current Actor input_schema.json for local cross-repo validation")
    args = parser.parse_args()

    repo = args.repo.resolve()
    sample_path = repo / "data" / "sample-input.json"
    readme_path = repo / "README.md"
    reference_path = repo / "docs" / "input-reference.md"

    try:
        sample_keys = _keys(_load_json(sample_path), str(sample_path))
        readme_input = _fenced_json_after_marker(readme_path.read_text(encoding="utf-8"), readme_path)
        readme_keys = _keys(readme_input, str(readme_path))
        reference_fields = _documented_fields(reference_path.read_text(encoding="utf-8"))

        if args.actor_schema:
            schema = _load_json(args.actor_schema.resolve())
            properties = schema.get("properties") if isinstance(schema, dict) else None
            if not isinstance(properties, dict):
                raise ValueError(f"{args.actor_schema} has no object 'properties' section")
            expected = set(properties)
        else:
            expected = reference_fields

        problems: list[str] = []
        for label, actual in (
            ("data/sample-input.json", sample_keys),
            ("README complete input", readme_keys),
            ("docs/input-reference.md", reference_fields),
        ):
            if actual != expected:
                problems.append(f"{label}: {_difference(expected, actual)}")

        if problems:
            raise ValueError("input contract mismatch: " + "; ".join(problems))
    except ValueError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print(f"PASS: {len(expected)} public input fields are present in the sample, README and input reference")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
