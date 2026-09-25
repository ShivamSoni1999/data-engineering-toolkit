from data_engineering_toolkit.quality.schema import validate_schema


def test_schema_validation_passes():
    assert validate_schema(
        [{"id": 1, "name": "a"}], {"id": "int", "name": "string"}
    ) == []


def test_schema_validation_reports_bad_type():
    errors = validate_schema([{"id": "1"}], {"id": "int"})
    assert "invalid type" in errors[0]
