from collections.abc import Mapping
from typing import Any

TYPE_MAP = {"string": str, "int": int, "float": (int, float), "bool": bool}


def validate_schema(rows: list[Mapping[str, Any]], schema: dict[str, str]) -> list[str]:
    """Validate required columns and basic Python types."""
    if not rows:
        return []
    errors: list[str] = []
    for column, expected_type in schema.items():
        if expected_type not in TYPE_MAP:
            errors.append(f"unsupported type '{expected_type}' for column '{column}'")
            continue
        expected = TYPE_MAP[expected_type]
        if column not in rows[0]:
            errors.append(f"missing required column: {column}")
            continue
        for index, row in enumerate(rows):
            value = row.get(column)
            if value is not None and not isinstance(value, expected):
                errors.append(
                    f"invalid type for '{column}' at row {index}: "
                    f"expected {expected_type}, got {type(value).__name__}"
                )
                break
    return errors
