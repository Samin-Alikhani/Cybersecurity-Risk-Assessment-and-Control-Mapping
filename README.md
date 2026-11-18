# Cybersecurity Risk Assessment and Control Mapping

## Project overview

This portfolio case study is an anonymized version of a student team assessment completed for a Cyber Risk Management final project in collaboration with a real nonprofit organization. The assessment used questionnaire responses; the organization and its personnel are not identified here.

## Contribution

My contribution to the original team report was framework mapping: connecting reported cybersecurity gaps to CIS Controls v8 and incorporating NIST Cybersecurity Framework references. The original assessment and its other analysis were completed collaboratively. This portfolio organizes the mappings and adds evidence, risk, remediation, assessment-procedure, and independent lab materials.

## Findings summary

Questionnaire responses identified reported gaps in authentication requirements, assigned security responsibility, written incident procedures, formal awareness training, and technology inventory. The source report also described backups, account provisioning and removal, automatic updates, vendor agreements, and informal awareness practices. These are reported conditions, not independently verified controls.

The framework mapping preserves the source report's original references and labels portfolio refinements and suggested follow-up criteria separately. The proposed actions are recommendations; this repository does not claim that the nonprofit implemented them.

## Start here

1. [Executive brief](docs/executive-brief.md) — scope, principal reported gaps, and recommended follow-up.
2. [Framework mapping register](registers/framework-mapping.csv) — original CIS and NIST references, mapping rationale, and separately labeled refinements.

## Assessment materials

Continue through the assessment work in this order:

3. [Qualitative risk register](registers/risk-register.csv) — risk scenarios, supporting evidence, and provisional follow-up priorities.
4. [Proposed remediation plan](registers/remediation-plan.csv) — recommended actions and completion criteria.
5. [Control-assessment worksheet](registers/control-assessment.csv) — evidence requests, procedures, acceptance criteria, and execution status.

For the full narrative and evidence context, see the [assessment report](docs/assessment.md) and [evidence register](registers/evidence-register.csv).

## Supporting lab

6. [Lab procedure and results](docs/control-testing-lab.md) — readable procedure, acceptance criteria, and actual synthetic-lab outcome.

The [lab README and script](lab/backup-recovery/README.md) explain how to reproduce the exercise. The timestamped [recorded run](lab/backup-recovery/runs/run-20261118T044037Z/results.json) retains machine-readable evidence.

## Limitations

Organizational findings are questionnaire-based and were not independently verified or technically tested. Risk priorities are provisional; likelihood and impact were not rated. No control implementation or risk reduction is claimed. The separate lab used synthetic files and does not validate the nonprofit's controls or recovery capability.

## Anonymization

The nonprofit and its personnel are unnamed. Identifying contact, team, and institutional details, the original report, and questionnaires are excluded. Case details have been generalized.
