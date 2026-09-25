from data_engineering_toolkit.quality.checks import run_quality_suite


def test_quality_passes_for_valid_rows():
    rows = [{"id": 1, "value": 10}, {"id": 2, "value": 20}]
    config = {"quality": {"not_null": ["id"], "unique": ["id"]}}
    assert run_quality_suite(rows, config).passed is True


def test_quality_fails_on_duplicate():
    rows = [{"id": 1}, {"id": 1}]
    config = {"quality": {"unique": ["id"]}}
    assert run_quality_suite(rows, config).passed is False
