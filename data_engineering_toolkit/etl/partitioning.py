from datetime import date


def date_partition_path(base_path: str, event_date: date) -> str:
    """Create hive-style year/month/day partitions."""
    return f"{base_path.rstrip('/')}/year={event_date.year}/month={event_date.month:02d}/day={event_date.day:02d}/"
