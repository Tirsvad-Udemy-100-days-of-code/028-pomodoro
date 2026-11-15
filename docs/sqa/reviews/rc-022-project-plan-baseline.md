# Review Record: PP-001 against QC-PP-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-022 |
| CrossReference | [PP-001], [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial review record; verdict Go (autonomous, not independent) | pending |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / education
- Language reviewer: none (the stand-in reads English and knows the education domain)
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Planning Assumptions give the start date 2026-10-13, the end date 2026-10-20 of the first five gateways and the start date 2026-11-16 and end date 2026-11-23 of MIL-006, and cite BC-001. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | The Gateway Schedule lists MIL-001 to MIL-005 and MIL-006 once each with document, decision date and owner; every document exists. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Every decision date lies in its window and equals the Target Date of its milestone (2026-11-23 for MIL-006). |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage maps every In Scope item of BC-001 to a gateway; the baseline item maps to MIL-006. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | The chain MIL-001 to MIL-006 is acyclic and in schedule order, as the Dependencies section says. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | Dependencies state that a No-Go holds the later gateways and shifts their windows, and that a No-Go on MIL-006 leaves the program and the earlier gateways as they are; S01 decides the new date. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Owner S01 and reviewer S01 (stand-in for MIL-006) are stakeholder IDs of SA-001; no governance document exists, so there is no RACI to contradict. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Each planning assumption names its source or is a decision of S01; the later end date of the baseline gateway is recorded with its reason (the agreed minimum quality baseline). |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Plan Risks give impact and mitigation for each of the four risks; the CI risk traces to success criterion 8 of BC-001. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open Issues lists three points; the note on the missing QC checklist was replaced because the checklist now exists, and the baseline entry records what the baseline changed in the wiki; none contradicts the rest of the plan. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | The main deliverable of each gateway is the first-named deliverable of its milestone; for MIL-006 it names the same items as its Deliverable section. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | The Stories column says `none` for every gateway; no use case or user story exists in docs/. |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | The Gantt bars use the dates of the schedule table; the dependency line agrees with the order. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | MIL-001 to MIL-004 and MIL-005 link milestones 141 to 144 and 146 of the git host, which exist and are closed there; MIL-006 links its milestone after the sync. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | PP-001 is the only Project Plan; its Version History records each change in its own row and only the latest row is Accepted. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | The Metadata table has `Language | en` and `Domain | education`; neither is a placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code and `education` is a row of the domain list of docs/artifact-registry.md. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | The prose and the table cells are English; only file names, commands and IDs are code. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | The registry gives the register `IT Executive English` for this type; the text is short, plain and written for that reader. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | The dictionary DICT-001 exists; the text uses its terms (work session, break, check mark, countdown, reset) in one meaning each, with no synonym found by reading. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, section headings, IDs and statuses are the framework's English ones. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No file `<name>.<language>.md` exists beside the document. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | The `Domain` row changed from `it` to `education` in this version (the language `en` is unchanged). The Version History row records the change and this review covers it. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The stand-in reads English and knows the education domain and checked the terms; the check is autonomous and not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out where they are first used (SQA, QC, CI, FURPS+) or are established names (README, API). |

## Overall Verdict

Go — every Mandatory criterion of QC-PP-001 and QC-LANG-001 passes after the edits of this change; the document is Accepted. Review of the whole document after the edits of this change.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| No open action | S01 | 2026-11-23 |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
