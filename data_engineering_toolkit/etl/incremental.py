from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class Watermark:
    column: str
    value: Any | None = None

    def should_process(self, record: dict[str, Any]) -> bool:
        """Return True when the record is newer than the current watermark."""
        if self.value is None:
            return True
        current = record.get(self.column)
        return current is not None and current > self.value

    def advance(self, records: list[dict[str, Any]]) -> None:
        values = [r[self.column] for r in records if r.get(self.column) is not None]
        if values:
            self.value = max(values)

    @staticmethod
    def now() -> datetime:
        return datetime.now(timezone.utc)
