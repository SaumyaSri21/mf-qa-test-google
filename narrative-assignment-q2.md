# Test Strategy Document

## Objective
To ensure accurate, reliable, and timely migration of ERP data from 30 systems to AWS S3, executed incrementally over 10 months.
The QA team will focus on validating data integrity, job performance, and critical system behavior with risk-based prioritization due to limited resources.

---

## QA Scope and Focus Areas

### In Scope
- Validation of initial migration (50 tables, one-time).
- Ongoing daily sync (2950 tables in batches of 300/month).
- Testing CDC methods (CDC1, CDC3, CDC7).
- Partitioning validation, S3 data checks.
- Performance monitoring for a 4-hour job run.

### Out of Scope
- Non-functional testing except performance testing (e.g., UI, UX, accessibility).
- Source system-level testing (assumed stable).

---

## Testing Approach

Due to a limited QA team, a risk-based, phased approach can be used:

### Phase Activity
- **Phase 1 (1st Month):** Focus on initial 50-table migration + framework setup for automation + define baseline data validation scripts.
- **Phase 2–9 (Months 2–10):** Test 300 new tables/month. Automate repetitive validations for ongoing sync jobs. Prioritize based on data sensitivity, volume, and change type. Maintain smoke, regression, and performance tests and verify results. Collaborate with DevOps to monitor job health and logs.

---

## Test Data Requirement

- Test Data should support CDC1, CDC3 and CDC7 system logics (full-load, insert, updates, deletes).
- Should be at the source level and controlled so expected outcomes can be predicted.
- Should cover boundary cases (empty tables, max-size, null values, etc.).
- Reusable for automation scripts.

---

## Test Type Execution Plan

### Smoke Testing
Run daily on job completion. Verify S3 upload success, record count sanity checks. Quickly verify critical path functionality after job deployment.

#### Major Scenarios
- Verify that the data extraction job starts at 2 AM as scheduled.
- Verify job execution completes successfully without errors.
- Verify raw files are uploaded to S3 (correct path and naming conventions).
- Verify the output file for at least 1 table from each CDC type.
- Verify that the S3 bucket is reachable and accessible.

### Functional Testing
Ensure the system behaves as expected for each migration function. CDC Logic Validation and partition checks to confirm 100K record partitions for sampled tables.
Confirm the system responds well to failures (Error handling and recovery)

#### Major Scenarios
- Verify complete data export for initial 50 tables.
- Validate CDC methods:
  - CDC1: All data fetched.
  - CDC3: Only new records.
  - CDC7: Only changed records.
- Verify partitioning logic: each partition contains ~100K records.
- Verify filenames and metadata (e.g., timestamps, versions).
- Verify correct file format (CSV, JSON, etc.) and structure.
- Verify failure in source DB connection and validate error handling (simulate an error)
- Verify upload failure to S3 and check retry logic  (simulate an error)
- Corrupt one source file and verify system response.
- Kill a running job midway; verify logs and retry capability.
- Verify that no partial/incomplete files are pushed to S3.


### Data Validation
Ensure the data is accurately migrated. Data Validation Row count checks for all tables. Deep record-level checks on ~10% of tables per batch.
Validate behavior at volume extremes (boundary levels).

#### Major Scenarios
- Verify row count match between source tables and raw files for sampled tables.
- Verify only expected deltas are present for CDC3 and CDC7.
- Verify checksum of sampled source vs target records.
- Verify no duplicates or missing records in target files.
- Verify key fields (IDs, timestamps) and referential integrity.
- Verify a table with exactly 100K records (1 partition).
- Verify a large table (~60GB) and check for splitting & stability.
- Verify with an empty table (0 records).
- Verify with a table containing special characters or long strings.


### Schema Validation
Ensure source and target schemas match.

#### Major Scenarios
- Verify field names, data types, and field order in exported files.
- Verify that mandatory columns are present in exported files.
- Verify schema changes are handled gracefully across sync cycles.
- Verify column nullability, default values (if applicable).


### Performance Testing
Ensure job SLA compliance (< 4 hrs). Monthly audits and alerts.

#### Major Scenarios
- Validate total job execution time.
- Test on:
  - Smallest table (~100K records)
  - Largest table (~60GB)
  - Peak volume days
  - Under load

### Security Testing
Ensure data security in transit and at rest.

#### Major Scenarios
- Verify that all S3 uploads are encrypted (if applicable).
- Verify job access is via IAM roles with least privilege.
- Verify the test access restrictions to raw data files (role-based S3 policies, if applicable).
- Verify sensitive data is masked (if required).


---

## Test Automation Strategy
- Prioritize repetitive, high-effort tasks (e.g. data validation,file checks)
- Automate early for foundational scripts (row counts, schema, partitioning)


### In Scope
- Smoke tests: Should include verification for job status, presence of expected file in S3 and a basic data sanity
Why: Daily run after sync job helps in identifying broken pipelines


- Regression tests: Automate record counts, schema validations, data comparisons, file format checks and partition size validations. Automate CDC logic verification and S3 upload validations.
Why: High volume tasks, repetitive across batches, easy to verify any schema change, manual comparison is error prone.Critical business logic validation with CDC methods. Saves manual effort across 2950 tables.


- Performance tests: Automate job completion time logs and alerts.
Why: Automate to reduce manual tracking and delays. Detects performance regressions as data volume scales.


### Out of Scope
- Full end to end UI, as the project is BE heavy and there’s no mention of UI.
- Monthly exploratory testing for edge cases.
- Row by row validation for 3000 tables.
- Test data creation at run time is not recommended, instead use production-like staging data to save time.
- Security and IAM tests.


---

## QA Resource Allocation

- Each QA: 100 tables/month (10 per working day).
- Assign per CDC category.
- Rotate lead QA weekly (regression, automation, docs).

### Time Allocation
- 40% Functional/data testing  
- 30% Automation/scripting  
- 20% Reporting/meetings/regression  
- 10% Ad hoc/special tests

---

## Entry and Exit Criteria

### Entry
- Source-to-S3 job deployed.
- Test tables identified and accessible.
- Test data ready.

### Exit
- Data matches for high-volume/critical tables.
- No critical defects open.
- Job completes < 4 hours.

---

## Risk Mitigation Plan

| Risk                 | Plan to Prevent                              |
|----------------------|-----------------------------------------------|
| QA bandwidth         | Automate early, test representative tables.   |
| Growing data size    | Monitor and test largest tables early.        |
| Unclear CDC logic    | Request documentation early from Dev.         |
| Schema changes       | Monitor changes monthly.                      |
| Job failures         | Use log alerts, retry tests, validate recovery.|

---

## Exit Strategy

At the end of 10 months:
- Regression suite in place for all CDC methods.
- Automation covers majority of validations.
- Final QA sign-off documented.
- Knowledge transfer docs prepared.
