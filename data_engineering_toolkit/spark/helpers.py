def require_pyspark():
    """Import PySpark lazily so the core package remains lightweight."""
    try:
        from pyspark.sql import DataFrame
    except ImportError as exc:
        raise RuntimeError("Install the optional 'spark' dependency to use Spark helpers") from exc
    return DataFrame
