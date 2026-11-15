# Review Record: DICT-001 against QC-DICT-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-023 |
| CrossReference | [DICT-001], [QC-DICT-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial review record; verdict Go (autonomous, not independent) | [3da20f5] |

---

## Artifact Under Review

- Instance reviewed: [DICT-001]
- Checklist used: [QC-DICT-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / education
- Language reviewer: none (the stand-in reads English and knows the education domain)
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Every row has a PO term, its language, an IT term and a definition | Pass | Every row has a PO term, its language, an IT term and a definition. |
| 2 | Each PO term maps to exactly one IT term and the reverse (no synonyms) | Pass | Five PO terms map to five distinct IT terms. |
| 3 | Every Domain Model concept has a row, and the Domain Model uses its PO term | Pass | No Domain Model exists in this project (single-screen exercise, PP-001 Planning Assumptions). |
| 4 | The Operation Contracts, Sequence Diagrams, Design Class Diagrams and ERD use the IT term, not the PO term | Pass | No Operation Contract, Sequence Diagram, Design Class Diagram or ERD exists. |
| 5 | Definitions are written in the PO language and are one sentence | Pass | Each definition is one English sentence. |
| 6 | "Used as PO term in" and "Used as IT term in" name artifact types that exist in the project | Pass | Rows name only BC, SA, PP, MIL and PY, types that exist or are planned. |
| 7 | The dictionary's `Language` and `Domain` rows, and the language of every row, match the PO language and domain in the project registry | Pass | Language en and Domain education match the registry; every row is English. |
| 8 | The dictionary rows are in ascending order of the PO term (case-insensitive, by the alphabet of the PO language) | Pass | The five rows are in ascending order of the PO term (break, check mark, countdown, reset, work session); the rows were re-ordered in this change. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | The Metadata table has `Language | en` and `Domain | education`; neither is a placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code and `education` is a row of the domain list of docs/artifact-registry.md. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | The prose and the table cells are English; only file names, commands and IDs are code. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | The registry gives the register `IT Professional English` for this type; the text is short, plain and written for that reader. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | The dictionary DICT-001 exists; the text uses its terms (work session, break, check mark, countdown, reset) in one meaning each, with no synonym found by reading. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, section headings, IDs and statuses are the framework's English ones. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No file `<name>.<language>.md` exists beside the document. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | The `Domain` row changed from `it` to `education` in this version (the language `en` is unchanged). The Version History row records the change and this review covers it. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The stand-in reads English and knows the education domain and checked the terms; the check is autonomous and not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out where they are first used (SQA, QC, CI, FURPS+) or are established names (README, API). |

## Overall Verdict

Go — every Mandatory criterion of QC-DICT-001 and QC-LANG-001 passes after the edits of this change (domain, row order); the document is Accepted. Review of the whole document after the edits of this change.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| No open action | S01 | 2026-11-23 |

---

[DICT-001]: ../../dictionary.md
[QC-DICT-001]: ../../../framework/qc/artifacts/qc-dictionary.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[3da20f5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/commit/3da20f512ebb3297bac84d8e9146b55bd1a30098
