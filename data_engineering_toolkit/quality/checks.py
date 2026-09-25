from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Any


@dataclass
class QualityReport:
    passed: bool
    checks: dict[str, bool] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)


def check_not_null(
    rows: Iterable[Mapping[str, Any]], columns: list[str]
) -> tuple[bool, list[str]]:
    rows = list(rows)
    errors = [
        f"null values found in {column}"
        for column in columns
        if any(row.get(column) is None for row in rows)
    ]
    return not errors, errors


def check_unique(rows: Iterable[Mapping[str, Any]], columns: list[str]) -> tuple[bool, list[str]]:
    rows = list(rows)
    errors: list[str] = []
    for column in columns:
        seen: set[Any] = set()
        for row in rows:
            value = row.get(column)
            if value in seen:
                errors.append(f"duplicate value found in {column}: {value!r}")
                break
            seen.add(value)
    return not errors, errors


def run_quality_suite(rows: Iterable[Mapping[str, Any]], config: dict[str, Any]) -> QualityReport:
    rows = list(rows)
    checks = config.get("quality", {})
    result = QualityReport(passed=True)
    if checks.get("not_null"):
        passed, errors = check_not_null(rows, list(checks["not_null"]))
        result.checks["not_null"] = passed
        result.errors.extend(errors)
    if checks.get("unique"):
        passed, errors = check_unique(rows, list(checks["unique"]))
        result.checks["unique"] = passed
        result.errors.extend(errors)
    result.passed = not result.errors
    return result
