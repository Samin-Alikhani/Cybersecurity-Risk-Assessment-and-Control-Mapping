# Cybersecurity Risk Assessment and Control Mapping

An anonymized questionnaire-based academic team assessment, developed into a portfolio case study focused on evidence traceability, framework-informed gap analysis, and practical control follow-up.

## Contribution and portfolio scope

- **Original team project:** assessed reported cybersecurity practices and gaps using questionnaire responses. No organizational systems were technically tested.
- **My contribution:** mapped reported gaps to CIS Controls v8 and provided NIST CSF references.
- **Portfolio extension:** adds an evidence register, safeguard-level mapping refinements, a provisional risk register, proposed remediation actions, and a control-assessment worksheet. These additions include AI-assisted drafting and are proposals, not work validated with or performed for the organization.

## Project files

- [Assessment](docs/assessment.md)
- [Executive brief](docs/executive-brief.md)
- [Framework mapping register](registers/framework-mapping.csv)
- [Evidence register](registers/evidence-register.csv)
- [Risk register](registers/risk-register.csv)
- [Proposed remediation plan](registers/remediation-plan.csv)
- [Control-assessment worksheet](templates/control-assessment.csv)
- [Synthetic backup recovery lab plan](docs/control-testing-lab.md)
- [Lab instructions and script](lab/backup-recovery/README.md)
- [Recorded synthetic-lab results](lab/backup-recovery/runs/run-20261118T042351Z/results.json)

## Method and limitations

The portfolio uses the team report as its immediate evidence source; the original questionnaires and supporting organizational evidence were not reviewed for this case study. Evidence is labeled as reported, a reported gap, or unknown. No organizational control effectiveness, implementation, or risk reduction is claimed. Risk priorities are provisional, and likelihood and impact are not rated.

The independent recovery lab used three synthetic files. All three restored with matching SHA-256 hashes, and a deliberately altered copy was detected. This result demonstrates only the lab procedure; it does not test the organization's backups or recovery capability.

## Framework interpretation

CIS Controls v8 is retained to match the source report. The mapping register distinguishes source-report mappings from suggested safeguard-level refinements and new portfolio mappings, and identifies safeguards outside IG1. NIST CSF 2.0 functions are used as thematic references, not as official CIS-to-NIST equivalences.

## Privacy

The organization and its personnel are anonymized. The original report, questionnaires, contact details, and team member identities are not included. Context has been generalized, though anonymization cannot guarantee that the source organization is unrecognizable.
