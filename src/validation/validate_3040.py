from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import pandas as pd


@dataclass(frozen=True)
class ValidationError:
    rule_id: str
    severity: str  # HIGH | MEDIUM | LOW
    message: str
    row_index: Optional[int] = None
    column: Optional[str] = None
    value: Optional[object] = None


REQUIRED_COLUMNS = ["instituicao_id", "referencia", "contrato_id", "valor_exposicao"]
KEY_COLUMNS = ["instituicao_id", "referencia", "contrato_id"]


def validate_3040(df: pd.DataFrame) -> list[ValidationError]:
    errors: list[ValidationError] = []

    # 1) Schema: colunas obrigatórias
    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            errors.append(
                ValidationError(
                    rule_id="R3040_SCHEMA_REQUIRED_COLUMN",
                    severity="HIGH",
                    message=f"Missing required column: {col}",
                    column=col,
                )
            )

    # Se faltou coluna-chave, não dá pra validar o resto com segurança
    if any(c not in df.columns for c in KEY_COLUMNS):
        return errors

    # 2) Not null (campos chave)
    for col in KEY_COLUMNS:
        null_mask = df[col].isna() | (df[col].astype(str).str.strip() == "")
        for idx in df[null_mask].index.tolist():
            errors.append(
                ValidationError(
                    rule_id="R3040_NOT_NULL",
                    severity="HIGH",
                    message=f"Null/empty in mandatory field: {col}",
                    row_index=int(idx),
                    column=col,
                )
            )

    # 3) Duplicidade de chave
    dup_mask = df.duplicated(subset=KEY_COLUMNS, keep=False)
    for idx in df[dup_mask].index.tolist():
        errors.append(
            ValidationError(
                rule_id="R3040_DUPLICATE_KEY",
                severity="HIGH",
                message=f"Duplicate key for: {', '.join(KEY_COLUMNS)}",
                row_index=int(idx),
                column=",".join(KEY_COLUMNS),
                value={c: df.loc[idx, c] for c in KEY_COLUMNS},
            )
        )

    # 4) Valor exposição não-negativo (se existir a coluna)
    if "valor_exposicao" in df.columns:
        s = pd.to_numeric(df["valor_exposicao"], errors="coerce")
        neg_mask = s.notna() & (s < 0)
        for idx in df[neg_mask].index.tolist():
            errors.append(
                ValidationError(
                    rule_id="R3040_NON_NEGATIVE",
                    severity="MEDIUM",
                    message="Negative valor_exposicao is not allowed",
                    row_index=int(idx),
                    column="valor_exposicao",
                    value=df.loc[idx, "valor_exposicao"],
                )
            )

    return errors
