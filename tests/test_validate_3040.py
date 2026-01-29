import pandas as pd

from src.validation.validate_3040 import validate_3040


def test_missing_required_columns():
    df = pd.DataFrame({"x": [1]})
    errors = validate_3040(df)
    assert any(e.rule_id == "R3040_SCHEMA_REQUIRED_COLUMN" for e in errors)


def test_duplicate_key_and_negative_value():
    df = pd.DataFrame(
        {
            "instituicao_id": ["001", "001"],
            "referencia": ["2026-01-01", "2026-01-01"],
            "contrato_id": ["A1", "A1"],  # duplicado
            "valor_exposicao": [100, -5],  # negativo
        }
    )
    errors = validate_3040(df)
    assert any(e.rule_id == "R3040_DUPLICATE_KEY" for e in errors)
    assert any(e.rule_id == "R3040_NON_NEGATIVE" for e in errors)
