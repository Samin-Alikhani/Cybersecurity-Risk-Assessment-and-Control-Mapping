# Cybersecurity Risk Assessment and Control Mapping

## Project overview

This anonymized case study develops a questionnaire-based cybersecurity assessment into a structured portfolio project. It connects reported practices and gaps to CIS Controls v8, organizes supporting evidence, and outlines practical risk treatment and control validation steps.

## Contribution

I mapped reported cybersecurity gaps to CIS Controls v8 and incorporated NIST Cybersecurity Framework references in the assessment. The original assessment was a collaborative team project; this repository distinguishes the source report's mappings from subsequent portfolio analysis.

## Deliverables

- [Assessment report](docs/assessment.md)
- [Executive brief](docs/executive-brief.md)
- [Framework mapping register](registers/framework-mapping.csv)
- [Evidence register](registers/evidence-register.csv)
- [Qualitative risk register](registers/risk-register.csv)
- [Proposed remediation plan](registers/remediation-plan.csv)
- [Control-assessment worksheet](templates/control-assessment.csv)
- [Synthetic backup recovery lab plan](docs/control-testing-lab.md)
- [Lab instructions and script](lab/backup-recovery/README.md)
- [Recorded lab results](lab/backup-recovery/runs/run-20261118T042351Z/results.json)

## Framework approach

CIS Controls v8 is retained to match the source assessment. The mapping register identifies source-report mappings and separates them from additional safeguard-level analysis. Implementation Group 2 and 3 safeguards are labeled. NIST CSF 2.0 functions provide thematic context; they are not presented as official CIS-to-NIST equivalences.

## Scope and limitations

The original assessment relied on questionnaire responses. Organizational systems were not technically tested, and reported practices were not independently verified. Risk priorities are provisional; likelihood and impact were not rated.

A separate recovery lab used three synthetic files. All restored with matching SHA-256 hashes, and a deliberately altered copy was detected. This demonstrates the lab procedure only; it does not test the organization's backups or recovery capability.

## Anonymization

The organization and its personnel are anonymized. Identifying contact and institutional details, the source report, and questionnaires are excluded. Case details have been generalized.
