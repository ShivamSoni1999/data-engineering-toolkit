from data_engineering_toolkit.quality.schema import validate_schema


def test_schema_validation_passes():
    rows = [{"id": 1, "name": "a"}]
    assert validate_schema(rows, {"id": "int", "name": "string"}) == []


def test_schema_validation_reports_bad_type():
    rows = [{"id": "1"}]
    errors = validate_schema(rows, {"id": "int"})
    assert "invalid type" in errors[0]
