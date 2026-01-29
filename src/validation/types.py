from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional


Severity = Literal["LOW", "MEDIUM", "HIGH"]


@dataclass(frozen=True)
class ValidationError:
    rule_id: str
    severity: Severity
    message: str
    row_index: Optional[int] = None
    column: Optional[str] = None
    value: Optional[object] = None


@dataclass(frozen=True)
class ValidationSummary:
    total_rows: int
    errors_count: int
    high_count: int
    medium_count: int
    low_count: int
