# 🧬 Data Lineage — Central de Riscos (SCR)

## 1. Overview
This document describes the high-level data lineage for the Central de Riscos (SCR) case study, outlining how regulatory data flows from source to analytics and monitoring.

The lineage is designed to support transparency, auditability and risk control.

---

## 2. Source Layer
### Regulatory Inputs
- SCR regulatory documents (DOC 3040, DOC 3044, DOC 3050)
- Public metadata and layout definitions provided by Bacen

### Characteristics
- Strict regulatory definitions
- Periodic submissions
- High sensitivity to data quality and consistency

---

## 3. Ingestion Layer
### Purpose
- Load raw SCR-compatible datasets into the platform
- Preserve original structure for traceability

### Typical Storage (Conceptual)
- Raw data stored in object storage (e.g., AWS S3 – raw zone)

---

## 4. Validation and Quality Layer
### Activities
- Structural validation (mandatory fields, formats)
- Regulatory rule enforcement (DOC 3044)
- Domain and consistency checks
- Detection of duplicates and missing data

### Outputs
- Validation flags
- Error metrics
- Data quality indicators

---

## 5. Reconciliation Layer
### Purpose
- Aggregate detailed data from DOC 3040
- Compare results against DOC 3050 consolidated figures

### Key Controls
- Totals consistency
- Dimensional alignment
- Temporal consistency

---

## 6. Analytics and ML Layer
### Use Cases
- Exploratory data analysis
- Anomaly detection
- Pattern identification and clustering
- Risk-oriented insights

### Role
This layer complements regulatory validation by identifying non-explicit risks and unusual behaviors.

---

## 7. Monitoring and Reporting
### Outputs
- Data quality dashboards
- Reconciliation reports
- Alerts for critical deviations

### Stakeholders
- Finance
- Risk management
- Compliance
- Data and analytics teams

---

## 8. Governance Notes
- Regulatory rules are sourced from Bacen documentation
- Validation logic is versioned and auditable
- Analytical models do not override regulatory rules
