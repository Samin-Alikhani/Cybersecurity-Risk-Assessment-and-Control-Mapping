# Cybersecurity Risk Assessment: Anonymized Nonprofit Case Study

**Status:** Anonymized portfolio draft derived from an academic team report. No organization systems were tested. New portfolio analysis is proposed and requires review.

## 1. Executive assessment

The source report describes a nonprofit relying on staff and volunteers. Questionnaire responses indicate several useful practices: backups kept separately from primary systems, account creation and removal, automatic software updates, vendor data-handling agreements, and informal awareness of suspicious activity.

The same report identifies gaps in authentication requirements, assigned security responsibility, written policies, awareness training, incident preparation, and technology inventory. These findings support targeted improvement recommendations. They do not support a numerical maturity score or a conclusion that the organization meets, nearly meets, or fails the entire CIS Implementation Group 1 baseline.

Recommended first steps are to assign accountable contacts, confirm MFA coverage on important services, document access procedures and incident reporting, and establish an inventory. Backup recoverability and update coverage should be verified rather than assumed from their reported existence.

## 2. Scope, method, and limitations

The original academic project addressed security controls, training and awareness, and policies and plans through questionnaires. Technical testing was excluded by the assignment. This portfolio revision uses the supplied team report as its immediate evidence source: original questionnaires, configuration exports, policies, and supporting evidence were not provided for this revision.

All organizational statements below therefore mean **reported in the source report**, rather than directly observed, independently verified, or confirmed current. No follow-up contact, system access, document inspection, or remediation implementation is claimed.

The analysis retains CIS Controls v8 as used by the original report. Selected safeguards organize follow-up questions and recommendations. NIST CSF 2.0 functions provide high-level context. This is not a full safeguard assessment, legal compliance determination, or control effectiveness opinion.

The original project was completed by a team. Samin Alikhani confirmed responsibility for mapping reported gaps to CIS Controls and providing NIST references. The source report explicitly maps authentication gaps to Controls 5 and 6 and awareness gaps to Control 14; its NIST references appear in the strengths analysis. The expanded safeguard-level mappings and portfolio registers are AI-assisted drafts, not additional work completed for the nonprofit. Individual authorship of other original sections is not established.

## 3. Scope inventory and information needs

The report supports the existence of a distributed work environment, user accounts, systems receiving updates, backups, and vendor relationships. Exact platforms, device populations, data classifications, owners, and critical dependencies are unknown.

Email, cloud storage, administrative accounts, and personal devices are areas proposed for follow-up, not a verified asset inventory. Do not assume payment processing, financial records, donor information, regulated data, or particular service providers.

An inventory should record asset or service identifier, purpose, owner, access method, relevant data category, business criticality, and review date. All these values remain to be collected by authorized personnel.

## 4. Evidence classification

Use separate labels for implementation and verification:

- **Reported present:** the report describes a practice; completeness and effectiveness remain unverified.
- **Reported gap:** the report describes an absent or inconsistent practice; current status requires confirmation.
- **Unknown:** the available material does not establish the answer.
- **Verified:** reserve for a later assessment with recorded evidence and an authorized procedure. No organizational item currently has this status.

Missing documentation does not automatically mean a technical safeguard is absent. Conversely, a reported policy or setting does not establish that it works or covers all relevant systems.

## 5. Reported strengths and mapping interpretation

| Reported practice | Potentially relevant CIS v8 safeguards | What remains unverified |
| --- | --- | --- |
| Backups are performed and held separately | 11.1–11.4: recovery planning, backups, protection, isolation | Automation, frequency, scope, permissions, isolation, and actual restoration |
| Accounts are created and removed | 6.1–6.2: access granting and revocation | Defined process, coverage, timeliness, approvals, and evidence |
| Automatic updates are used | 7.3–7.4: operating-system and application patching | Which platforms are covered, successful installation, exceptions, and unsupported software |
| Vendor data-handling agreements exist | 15.4: contractual security expectations | Contract contents, coverage, and review; 15.4 is IG2/IG3, not IG1 |
| Informal awareness exists | Control 14: awareness and training | Formal program, content, completion, reporting process, and refresh cycle |

The source report maps practices at the Control level. Safeguard-level details in the register are portfolio refinements or suggested follow-up criteria, as marked there. Vendor agreements do not establish safeguard 15.1, the IG1 service-provider inventory requirement. Informal caution does not establish a formal training program. A backup's existence does not establish recoverability.

## 6. Findings and risk scenarios

**R-01: Inconsistent authentication requirements.** The report describes missing formal password requirements and inconsistent MFA enforcement. A plausible scenario is unauthorized access following credential theft or reuse. Actual exposure depends on service configuration and account privilege. Prioritize discovering important services and documenting supported MFA enforcement, exceptions, and responsible owners.

**R-02: Incompletely documented access processes.** Provisioning and removal are reported, but repeatable approvals and access reviews are not established. Access could remain unnecessary or excessive following role changes or departures. Review a defined sample of authorized records before determining whether the process operates effectively.

**R-03: Unassigned coordination and undocumented incident procedures.** The report identifies no formal security responsibility or incident plan. Delayed reporting and unclear decisions could prolong disruption. Propose a primary and backup incident contact, reporting instructions, and a short response procedure. Formal response-plan development is relevant beyond the minimum IG1 safeguards.

**R-04: No formal awareness program.** Informal awareness may vary across staff and volunteers. A phishing attempt could succeed or go unreported. Propose role-appropriate training and clear reporting instructions; do not infer a measured susceptibility rate.

**R-05: Incomplete technology visibility.** The report does not establish a centralized inventory. Unknown assets or services could miss access removal, updates, or recovery coverage. First confirm inventory status, then reconcile a scoped inventory against available authorized records.

**R-06: Backup recoverability is unknown.** Separate backups are reported, but restore evidence is unavailable. A disruption could reveal incomplete or unusable recovery copies. This is an assurance gap, not evidence that backups have failed.

**R-07: Vendor assurance is incomplete.** Agreements are reported, but an inventory and systematic review are not established. Dependencies or data-handling responsibilities may remain unclear. Request an inventory before judging contract or oversight coverage.

## 7. Qualitative prioritization

The accompanying risk register uses provisional High/Medium priorities to sequence follow-up. They are portfolio analyst judgments, not measured organizational risk or management-approved ratings. Likelihood and impact remain **Not rated** until platform scope, data sensitivity, exposure, and operational dependencies are established.

For a future assessment, define the time horizon and rating criteria first. Likelihood should consider exposure, attacker opportunity, and existing safeguards. Impact should consider confidentiality, integrity, availability, and mission disruption. Record the rationale and uncertainty for each rating. Residual risk should be reassessed only after supported treatment evidence exists; no reduction is claimed here.

## 8. Proposed action plan

Sequence proposed activities by dependencies rather than invented deadlines:

1. Leadership designates a coordinator and incident backup; confirm report findings and asset scope.
2. Inventory important services/accounts; identify MFA capabilities, enforce supported requirements through authorized administrators, and document exceptions.
3. Document granting/revocation and incident reporting; create usable contact and response guidance.
4. Establish awareness training, inventory maintenance, and vendor ownership.
5. Collect evidence for update and backup coverage; arrange authorized recovery testing and review outstanding gaps.

Owners are proposed roles, not assigned people. Dates, budgets, acceptance decisions, and implementation status require organizational approval. The remediation register supplies completion criteria without claiming execution.

## 9. Assessment procedures and independent lab

The control worksheet defines evidence requests and procedures for a future authorized assessment. Every procedure is **Not performed**. The original project must not be represented as a technical control test.

A separate synthetic-data backup recovery lab is proposed to demonstrate test design, evidence recording, and result analysis. Any completed lab results apply only to that lab, not to the nonprofit. It will not establish full CIS compliance.

## 10. Conclusion

The source report provides a useful starting point for a scoped, evidence-aware assessment. Its strongest portfolio value is the traceable connection between reported practices, relevant framework guidance, information gaps, and practical next steps. Further evidence is necessary before asserting control effectiveness, full IG1 alignment, or reduced residual risk.

## References and interpretation

- CIS Controls v8 Navigator: https://www.cisecurity.org/controls/cis-controls-navigator/v8
- CIS v8 assessment specifications: https://cas8.docs.cisecurity.org/en/latest/
- NIST CSF 2.0: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf

Safeguard and CSF descriptions are concise interpretive labels. Consult the official sources for full requirements, applicability, and assessment procedures. Framework mappings are thematic, not official crosswalk equivalences.