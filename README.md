# Data Engineering Toolkit

A lightweight, production-minded Python toolkit for building reliable metadata-driven data pipelines.

The project focuses on reusable patterns commonly needed in batch and near-real-time data platforms: configuration-driven ingestion, schema validation, data-quality checks, incremental processing, partition management, retries, and PySpark helpers.

> This is an open-source engineering project designed for practical reuse and experimentation.

## What it provides

- **Metadata-driven pipelines** using YAML configuration.
- **Schema validation** with clear type/missing-column errors.
- **Data-quality checks** for nulls and uniqueness, with an extensible quality-report model.
- **Incremental ingestion** using a watermark/checkpoint abstraction.
- **Retry utilities** with bounded exponential backoff.
- **Partition helpers** for date-based data layouts.
- **PySpark utilities** that keep Spark-specific logic isolated.
- **Unit tests** and GitHub Actions CI.

## Architecture

```text
Source
  |
  v
Metadata / Config --> Validation --> Ingestion --> Transform
                                      |              |
                                      v              v
                                  Checkpoint      Quality Checks
                                      |              |
                                      +-------> Storage
                                                     |
                                                     v
                                               Monitoring / Logs
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
```

Run the example:

```bash
python examples/run_pipeline.py
```

## Configuration example

```yaml
pipeline:
  name: orders_daily
  source: s3://example/raw/orders/
  target: s3://example/curated/orders/
  watermark_column: updated_at
  partition_columns:
    - event_date

quality:
  not_null:
    - order_id
    - updated_at
  unique:
    - order_id
```

## Design principles

1. **Configuration over hard-coded pipeline logic.**
2. **Fail fast on invalid schemas and critical quality failures.**
3. **Keep state explicit through watermarks/checkpoints.**
4. **Make storage and compute adapters replaceable.**
5. **Keep the core library cloud-agnostic while allowing AWS/Spark integration.**

## Roadmap

- Add object-store adapters for S3/GCS/Azure Blob.
- Add Great Expectations/Deequ-compatible quality adapters.
- Add Kafka/Kinesis ingestion examples.
- Add Delta Lake helpers.
- Add OpenTelemetry metrics and tracing.

## License

Apache-2.0. See [LICENSE](LICENSE).
