## ✅ Running DOC 3040 Validations (End-to-End)
This project includes an automated validation engine for a DOC 3040-like dataset, producing a machine-readable summary and a detailed error report.
### 1) Install dependencies

```
pip install -r requirements.txt
```
### 2) Run validation on the sample dataset
A synthetic dataset is provided in data/raw/doc3040_sample.csv.
```
python -m src.validation.run_validate_3040 data/raw/doc3040_sample.csv
```
### 3) Outputs
The command generates the following files under outputs/:
- outputs/validation_errors_3040.csv
  Detailed list of validation issues (rule_id, severity, row_index, column, value)
 - outputs/validation_summary_3040.json
  Validation summary metrics (total_rows, errors_count, counts by severity)
### Validation Rules (current MVP)
- Schema checks: required columns exist
- Mandatory fields: key fields cannot be null/empty
- Uniqueness: no duplicate keys (institution + period + contract)
- Numerical consistency: non-negative exposure values
- Note: Regulatory rules are modeled conceptually from the SCR documentation and will be expanded to include conditional constraints and domain validations based on DOC 3044.






 










