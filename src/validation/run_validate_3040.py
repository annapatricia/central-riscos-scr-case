from __future__ import annotations

import json
from pathlib import Path
import sys

import pandas as pd

from src.validation.validate_3040 import validate_3040


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python -m src.validation.run_validate_3040 <input_csv> [out_dir]")
        return 2

    input_csv = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) >= 3 else "outputs"

    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(input_csv)
    errors = validate_3040(df)

    errors_rows = [
        {
            "rule_id": e.rule_id,
            "severity": e.severity,
            "message": e.message,
            "row_index": e.row_index,
            "column": e.column,
            "value": e.value,
        }
        for e in errors
    ]

    pd.DataFrame(errors_rows).to_csv(
        out_path / "validation_errors_3040.csv", index=False
    )

    summary = {
        "total_rows": int(len(df)),
        "errors_count": int(len(errors)),
        "high_count": int(sum(1 for e in errors if e.severity == "HIGH")),
        "medium_count": int(sum(1 for e in errors if e.severity == "MEDIUM")),
        "low_count": int(sum(1 for e in errors if e.severity == "LOW")),
    }

    with open(out_path / "validation_summary_3040.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print("Arquivos gerados:")
    print(f"- {out_path / 'validation_errors_3040.csv'}")
    print(f"- {out_path / 'validation_summary_3040.json'}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
