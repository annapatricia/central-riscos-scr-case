# 📘 Data Dictionary — Central de Riscos (SCR)

## 1. Overview
The Central de Riscos (SCR) is a regulatory system maintained by the Brazilian Central Bank (Bacen) to collect, validate and consolidate credit risk information reported by financial institutions.

This data dictionary documents the high-level structure, purpose and critical attributes of the SCR regulatory documents used in this case study:
- DOC 3040
- DOC 3044
- DOC 3050

The goal is to support data quality validation, reconciliation, analytics and monitoring.

---

## 2. DOC 3040 — Detailed Credit Information

### Purpose
DOC 3040 contains detailed credit-related records reported by financial institutions. It represents the most granular layer of the SCR and serves as the primary source for validation and reconciliation.

### Granularity
- Record-level (detailed reporting)
- Typically segmented by institution, reporting period and credit attributes

### Data Characteristics
- High number of fields
- Strong dependency on regulatory codes
- Multiple mandatory fields
- Sensitive to data quality issues

### Examples of Critical Fields
| Category | Description |
|--------|------------|
| Identifiers | Institution ID, reporting period |
| Classification | Credit modality, risk codes |
| Financial Values | Exposure amounts, balances |
| Temporal | Reference date, maturity date |

### Main Risks
- Missing mandatory fields
- Invalid regulatory codes
- Inconsistent values or dates
- Duplicate records

---

## 3. DOC 3044 — Filling Instructions and Business Rules

### Purpose
DOC 3044 defines the business rules, constraints and conditional logic that govern how DOC 3040 data must be filled.

### Role in the Data Pipeline
- Source of regulatory validation rules
- Reference for mandatory vs conditional fields
- Definition of accepted domains and exceptions

### Types of Rules
- Mandatory field rules
- Conditional dependencies (if/then)
- Domain and code validations
- Applicability constraints by modality

### Usage in This Case
Rules from DOC 3044 are translated into automated validation checks and monitoring metrics.

---

## 4. DOC 3050 — Aggregated and Consolidated Information

### Purpose
DOC 3050 provides aggregated views of credit exposure and related indicators derived from detailed SCR data.

### Granularity
- Aggregated by dimensions such as modality, period or institution
- Used for monitoring and regulatory oversight

### Role in Reconciliation
- Acts as a control layer for consistency checks
- Enables reconciliation between detailed (DOC 3040) and aggregated data

### Main Risks
- Aggregation mismatches
- Inconsistent totals
- Temporal misalignment

---

## 5. Relationship Between Documents

| Document | Level | Primary Use |
|--------|------|------------|
| DOC 3040 | Detailed | Validation, analytics, anomaly detection |
| DOC 3044 | Rules | Regulatory compliance and data quality |
| DOC 3050 | Aggregated | Reconciliation and monitoring |

---

## 6. Notes
This dictionary focuses on structural understanding rather than exhaustive field-level definitions. Detailed field mappings and rules are documented separately.
