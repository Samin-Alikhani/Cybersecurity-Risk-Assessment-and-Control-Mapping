#!/usr/bin/env python3
"""Run a safe backup/restore integrity demonstration on synthetic data only."""

from __future__ import annotations

import hashlib
import json
import platform
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


def sha256_files(directory: Path) -> dict[str, str]:
    """Return relative file paths and SHA-256 hashes for regular files."""
    result: dict[str, str] = {}
    for path in sorted(p for p in directory.rglob("*") if p.is_file()):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        result[path.relative_to(directory).as_posix()] = digest
    return result


def make_run_directory(runs_root: Path, run_id: str) -> tuple[Path, str]:
    """Create a new run directory without overwriting any prior evidence."""
    candidate = run_id
    suffix = 1
    while True:
        run_dir = runs_root / candidate
        try:
            run_dir.mkdir(parents=True, exist_ok=False)
            return run_dir, candidate
        except FileExistsError:
            candidate = f"{run_id}-{suffix:02d}"
            suffix += 1


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    runs_root = script_dir / "runs"
    start = datetime.now(timezone.utc)
    run_id = start.strftime("run-%Y%m%dT%H%M%SZ")
    run_dir, actual_run_id = make_run_directory(runs_root, run_id)

    baseline = run_dir / "baseline"
    backup = run_dir / "backup"
    restored = run_dir / "restored"
    altered_backup = run_dir / "altered-backup-copy"
    altered_restore = run_dir / "altered-restore"
    baseline.mkdir()

    synthetic_files = {
        "sample-notes.txt": (
            "Synthetic recovery lab data. No organizational information.\n"
        ),
        "sample-records.csv": (
            "record_id,status\nSYN-001,example\nSYN-002,example\n"
        ),
        "sample-config.txt": (
            "setting=demo\nmode=synthetic\n"
        ),
    }
    for name, content in synthetic_files.items():
        (baseline / name).write_text(content, encoding="utf-8", newline="")

    expected_hashes = sha256_files(baseline)
    shutil.copytree(baseline, backup)
    shutil.copytree(backup, restored)
    restored_hashes = sha256_files(restored)
    positive_missing = sorted(set(expected_hashes) - set(restored_hashes))
    positive_unexpected = sorted(set(restored_hashes) - set(expected_hashes))
    positive_mismatches = sorted(
        name for name in set(expected_hashes) & set(restored_hashes)
        if expected_hashes[name] != restored_hashes[name]
    )
    positive_pass = not (positive_missing or positive_unexpected or positive_mismatches)

    shutil.copytree(backup, altered_backup)
    altered_file = altered_backup / "sample-records.csv"
    with altered_file.open("a", encoding="utf-8", newline="") as stream:
        stream.write("SYN-003,deliberately-altered-copy\n")
    shutil.copytree(altered_backup, altered_restore)
    altered_hashes = sha256_files(altered_restore)
    negative_mismatches = sorted(
        name for name in set(expected_hashes) & set(altered_hashes)
        if expected_hashes[name] != altered_hashes[name]
    )
    expected_negative_mismatches = ["sample-records.csv"]
    negative_pass = (
        set(expected_hashes) == set(altered_hashes)
        and negative_mismatches == expected_negative_mismatches
    )

    end = datetime.now(timezone.utc)
    results = {
        "lab": "Synthetic backup recovery integrity demonstration",
        "scope": "Synthetic files only; no nonprofit data, systems, or controls tested.",
        "run_id": actual_run_id,
        "started_utc": start.isoformat(),
        "finished_utc": end.isoformat(),
        "python_version": sys.version.split()[0],
        "platform": platform.platform(),
        "expected_file_count": len(expected_hashes),
        "restored_file_count": len(restored_hashes),
        "expected_sha256": expected_hashes,
        "positive_restore": {
            "status": "PASS" if positive_pass else "FAIL",
            "missing_files": positive_missing,
            "unexpected_files": positive_unexpected,
            "hash_mismatches": positive_mismatches,
        },
        "negative_corruption_detection": {
            "status": "PASS" if negative_pass else "FAIL",
            "deliberately_altered_file": "sample-records.csv",
            "expected_hash_mismatches": expected_negative_mismatches,
            "detected_hash_mismatches": negative_mismatches,
        },
        "overall_status": "PASS" if positive_pass and negative_pass else "FAIL",
        "limitations": [
            "Does not test automated scheduling, encryption, access control, offsite isolation, ransomware resistance, production applications, retention, or organizational recovery.",
            "A copy on the same machine is not an isolated or disaster-resilient backup.",
            "Results apply only to the synthetic files and this execution.",
        ],
    }
    results_path = run_dir / "results.json"
    results_path.write_text(
        json.dumps(results, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="",
    )
    print(json.dumps(results, indent=2, sort_keys=True))
    print(f"Evidence written to: {results_path}")
    return 0 if results["overall_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
