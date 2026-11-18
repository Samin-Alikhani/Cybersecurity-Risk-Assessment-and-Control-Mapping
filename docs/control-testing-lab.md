# Independent Synthetic Backup Recovery Lab — Procedure and Results

**Execution status:** Performed on 2026-11-18 with synthetic files only. The actual results are recorded in [results.json](../lab/backup-recovery/runs/run-20261118T044037Z/results.json). This does not test the nonprofit's controls or backups.

## Purpose and boundary

Demonstrate a repeatable restore-integrity procedure using synthetic files in a local environment. No nonprofit data, accounts, devices, or services are in scope. This plan relates to CIS v8 Control 11; 11.5 recovery testing is IG2/IG3, and completion does not establish full safeguard implementation.

## Procedure

1. Create a dedicated disposable lab directory containing synthetic text/CSV files. Record file list, sizes, and SHA-256 hashes.
2. Copy the files to a separate backup directory. This models a recovery copy; two directories on one disk do not demonstrate isolated or disaster-resilient backup storage.
3. Retain the source unchanged. Restore the backup into a new empty directory; do not delete or overwrite existing user files.
4. Compare restored filenames, contents, and hashes with the baseline. Record missing files and mismatches.
5. In a separate disposable backup copy, deliberately alter one synthetic file. Repeat verification to show that the test detects corruption.
6. Record actual start/end times if measuring restore duration. Do not claim an organizational recovery objective was met without an independently defined objective.
7. Save sanitized output, a result worksheet, limitations, and any corrective action. Repeat after a fix if a failure occurs.

## Acceptance criteria

- Positive test: all expected files restore with matching hashes.
- Negative test: the deliberately altered file is the only file flagged as a mismatch.
- Results refer only to synthetic files and the test environment.

## Recorded synthetic-lab results

| Field | Actual result |
| --- | --- |
| Execution date | 2026-11-18 UTC |
| Runtime | Python 3.14.6 on macOS 26.6.2 arm64 |
| Expected files | 3 |
| Restored files | 3 |
| Positive restore | PASS; 3/3 files matched baseline SHA-256 hashes, with no missing, unexpected, or mismatched files |
| Negative corruption check | PASS; altered `sample-records.csv` was detected by hash mismatch |
| Overall lab result | PASS for both synthetic-data checks |
| Evidence | [Machine-readable results](../lab/backup-recovery/runs/run-20261118T044037Z/results.json) |
| Nonprofit test status | Not performed |

## Limits

This does not test automated scheduling, encryption, access controls, offsite isolation, ransomware resistance, production applications, retention, or organization-wide recovery. The script and run evidence are stored under `lab/backup-recovery/`. These results do not establish the nonprofit's backup recoverability or implementation of any CIS safeguard.
