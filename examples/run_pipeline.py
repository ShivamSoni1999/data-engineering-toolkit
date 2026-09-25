from data_engineering_toolkit.config.loader import load_yaml
from data_engineering_toolkit.quality.checks import run_quality_suite
from data_engineering_toolkit.quality.schema import validate_schema

rows = [
    {"order_id": "1001", "updated_at": "2026-01-01T10:00:00Z"},
    {"order_id": "1002", "updated_at": "2026-01-01T10:05:00Z"},
]
config = load_yaml("examples/pipeline.yaml")
report = run_quality_suite(rows, config)
schema_errors = validate_schema(rows, {"order_id": "string", "updated_at": "string"})
print("pipeline=" + config["pipeline"]["name"])
print("schema_passed=" + str(not schema_errors))
print("quality_passed=" + str(report.passed))
