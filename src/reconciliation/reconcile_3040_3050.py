from __future__ import annotations

import json
from pathlib import Path
import sys

import pandas as pd


def reconcile(doc3040_csv: str, doc3050_csv: str) -> pd.DataFrame:
    d3040 = pd.read_csv(doc3040_csv)
    d3050 = pd.read_csv(doc3050_csv)

    # Agrega o DOC 3040 por instituicao + referencia
    agg_3040 = (
        d3040.groupby(["instituicao_id", "referencia"], dropna=False)["valor_exposicao"]
        .sum()
        .reset_index()
        .rename(columns={"valor_exposicao": "total_3040"})
    )

    # Junta com DOC 3050 (totais esperados)
    merged = agg_3040.merge(
        d3050[["instituicao_id", "referencia", "total_exposicao"]],
        on=["instituicao_id", "referencia"],
        how="outer",
    ).rename(columns={"total_exposicao": "total_3050"})

    # Diferença
    merged["diff"] = (pd.to_numeric(merged["total_3040"], errors="coerce") - pd.to_numeric(merged["total_3050"], errors="coerce"))

    # Status simples
    merged["status"] = merged["diff"].apply(lambda x: "OK" if pd.notna(x) and abs(x) < 1e-9 else "MISMATCH")

    return merged


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: python -m src.reconciliation.reconcile_3040_3050 <doc3040_csv> <doc3050_csv> [out_dir]")
        return 2

    doc3040_csv = sys.argv[1]
    doc3050_csv = sys.argv[2]
    out_dir = sys.argv[3] if len(sys.argv) >= 4 else "outputs"

    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    result = reconcile(doc3040_csv, doc3050_csv)

    # Salvar CSV
    result.to_csv(out_path / "reconciliation_3040_3050.csv", index=False)

    # Salvar summary JSON
    summary = {
        "rows": int(len(result)),
        "ok": int((result["status"] == "OK").sum()),
        "mismatch": int((result["status"] != "OK").sum()),
    }
    with open(out_path / "reconciliation_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print("Arquivos gerados:")
    print(f"- {out_path / 'reconciliation_3040_3050.csv'}")
    print(f"- {out_path / 'reconciliation_summary.json'}")

    return 0

    


if __name__ == "__main__":
    raise SystemExit(main())
