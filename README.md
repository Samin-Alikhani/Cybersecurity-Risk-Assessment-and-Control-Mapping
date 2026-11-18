# Cybersecurity Risk Assessment and Control Mapping

## Project overview

This portfolio case study is an anonymized version of a student team report prepared for a Cyber Risk Management final project in collaboration with a real nonprofit organization. The assessment was based on questionnaire responses and did not include technical testing of the organization’s systems. The nonprofit is not named in this repository.

## Contribution

My contribution to the original team report was framework mapping: mapping reported cybersecurity gaps to CIS Controls v8 and incorporating NIST Cybersecurity Framework references. The assessment and its other original analysis were completed collaboratively. This portfolio adds structured evidence, risk, remediation, and control-assessment materials.

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
- [Recorded lab results](lab/backup-recovery/runs/run-20261118T044037Z/results.json)

## Framework approach

CIS Controls v8 is retained to match the source report. The mapping register identifies mappings present in the original report and distinguishes them from additional safeguard-level analysis. Implementation Group 2 and 3 safeguards are labeled. NIST CSF 2.0 functions provide thematic context; they are not presented as official CIS-to-NIST equivalences.

## Scope and limitations

Reported practices were not independently verified. Risk priorities are provisional; likelihood and impact were not rated. No organizational control effectiveness, implementation, or risk reduction is claimed.

A separate recovery lab used three synthetic files. All restored with matching SHA-256 hashes, and a deliberately altered copy was detected. This demonstrates the lab procedure only; it does not test the nonprofit's backups or recovery capability.

## Anonymization

The nonprofit and its personnel are unnamed. Identifying contact, team, and institutional details, the original report, and questionnaires are excluded. Case details have been generalized.
