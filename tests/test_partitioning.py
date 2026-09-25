from datetime import date
from data_engineering_toolkit.etl.partitioning import date_partition_path

def test_date_partition_path():
    assert date_partition_path("s3://bucket/data", date(2026, 9, 25)) == "s3://bucket/data/year=2026/month=09/day=25/"
