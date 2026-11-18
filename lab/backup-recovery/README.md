# Synthetic Backup Recovery Lab

This independent lab demonstrates a small, repeatable recovery check using synthetic files created by the script. It is separate from the nonprofit assessment and does not test the nonprofit's backups, systems, controls, or recovery objectives.

## Run

From this directory, run:

```bash
python3 run_lab.py
```

Requires Python 3.10 or later and uses only the standard library. Each run creates a new timestamped directory under `runs/`; existing runs are preserved, and no files outside the new run directory are modified.

## What it checks

1. Creates three synthetic text/CSV files and records their SHA-256 hashes.
2. Copies them into a backup directory, restores them into a new directory, and compares the restored names and hashes with the baseline.
3. Creates a separate copy of the backup, alters one synthetic file, restores that copy, and confirms that hash comparison detects the change.
4. Writes the actual run details and results to `runs/<run-id>/results.json`.

The positive check passes only when all expected files are restored with matching hashes. The negative check passes only when `sample-records.csv` is the sole hash mismatch. A pass demonstrates only this script's behavior on these synthetic files. It does not demonstrate scheduled, encrypted, isolated, offsite, ransomware-resistant, or production backups.

## Evidence

The [recorded run](runs/run-20261118T044037Z/results.json) is the actual result from this execution. Local runs retain the baseline, backup, restored files, altered-copy fixtures, and `results.json`. The repository publishes the timestamped result records; synthetic file fixtures remain local. Results record runtime, file counts, hashes, mismatches, and outcomes, with subsequent result records retained separately.
