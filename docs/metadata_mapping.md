# 🔗 Metadata Mapping — SCR Regulatory Documents

## 1. Objective
This document describes how SCR regulatory documents relate to each other from a data structure and consistency perspective, supporting validation, reconciliation and analytical use cases.

The focus is on understanding:
- Granularity differences
- Key relationships
- Aggregation logic
- Regulatory consistency risks

---

## 2. Document Roles in the Data Model

### DOC 3040 — Source of Truth (Detailed Layer)
- Primary detailed dataset
- Contains record-level credit information
- Serves as the base for analytics, validations and anomaly detection

### DOC 3044 — Rule and Constraint Layer
- Defines how DOC 3040 must be filled
- Does not contain data itself
- Provides regulatory logic used by validation engines

### DOC 3050 — Control and Aggregation Layer
- Contains aggregated and consolidated metrics
- Used as a control mechanism to verify consistency of detailed data
- Enables monitoring and regulatory oversight

---

## 3. Conceptual Mapping Between Documents

### Mapping Logic
- DOC 3040 records are aggregated according to regulatory dimensions
- Aggregated results are compared against DOC 3050 totals
- DOC 3044 rules define how aggregation and classification must be applied

### Example (Conceptual)
| DOC 3040 (Detailed) | Transformation | DOC 3050 (Aggregated) |
|--------------------|---------------|-----------------------|
| Individual records | Sum / Grouping | Total exposure values |
| Modalities         | Classification | Exposure by modality |
| Reporting period   | Time alignment | Period totals |

---

## 4. Key Dimensions for Reconciliation
Typical dimensions involved in reconciliation include:
- Reporting institution
- Reference period
- Credit modality
- Risk classification
- Currency or unit of measure

Consistency across these dimensions is required to ensure regulatory compliance.

---

## 5. Common Reconciliation Risks
- Aggregation logic mismatch
- Missing or duplicated records
- Incorrect classification codes
- Temporal misalignment between documents
- Rule misinterpretation from DOC 3044

---

## 6. Usage in This Case Study
This metadata mapping supports:
- Automated reconciliation scripts
- Data quality dashboards
- Prioritization of validation rules
- Design of AWS-based data pipelines

---

## 7. Next Steps
Detailed field-level mappings and transformation rules will be implemented in validation and reconciliation modules.
