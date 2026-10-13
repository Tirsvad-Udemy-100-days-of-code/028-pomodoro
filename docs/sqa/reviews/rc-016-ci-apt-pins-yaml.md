# Review Record: YAML files after pinning the apt packages (re-review of RC-014)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [QC-YML-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | AI for S01 | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [YML-MIL-001] (.gitea/workflows/ci.yml and .yamllint.yml)
- Checklist used: [QC-YML-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the author is the same AI)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file parses with a safe YAML loader and has no duplicate keys in any mapping | Pass | yamllint 1.38.0 parses both files with its safe loader and finds no duplicate key. |
| 2 | Indentation is 2 spaces everywhere, never tabs; lines end with LF; the file ends with one newline and has no trailing spaces | Pass | 2-space indentation, LF endings, one final newline, no trailing spaces (yamllint default rules). |
| 3 | Passes `yamllint` (or the project's YAML linter) with its configuration committed next to the code and no unexplained `disable` comments | Pass | `.yamllint.yml` is committed next to the code; yamllint 1.38.0 passes with no disable comment. |
| 4 | A scalar that YAML would coerce to another type is quoted: `yes`, `no`, `on`, `off`, `null`, `~`, numbers with a leading zero, versions such as `1.10`, and values that contain `: ` or ` #` | Pass | Version strings (`"3.13"`, `"8.6.14-1build1"`, `"2:21.1.12-1ubuntu1.8"`) are quoted; the `on:` key is declared by `truthy.check-keys: false`. |
| 5 | Only safe, plain types are used: no language-specific tags (`!!python/object`, `!ruby/object`) and no `!include`-style extension unless the consuming tool documents it | Pass | No language-specific tags or includes. |
| 6 | No secret is written in the file: no password, token, key or private connection string; a secret is referenced by name and supplied by the consuming tool | Pass | No secret in either file. |
| 7 | Embedded program text (shell, Python, SQL, `jq`, and so on) in a value is at most five lines; a longer one is moved to a file of its own, in its own language, and the YAML calls it | Pass | The longest embedded program text in a value is four lines (the apt-get step). |
| 8 | A block of keys or values repeated in the file or across files is defined once (an anchor, a template, an include or a reusable unit the consumer supports) | Pass | No block is repeated in the file. |
| 9 | Anchors, aliases and merge keys (`&`, `*`, `<<`) are used only where the consuming tool is known to support them | N-A | No anchors, aliases or merge keys are used. |
| 10 | The file validates against the schema of the consuming tool where one exists, and the schema or tool version is stated | Pass | actionlint 1.7.12 validates ci.yml against the workflow schema. |
| 11 | A header comment states what the file is for, which tool reads it, and where its decision or design is recorded | Pass | Header comments state purpose, reader tool and decision record. |
| 12 | Key names follow the convention of the consuming tool; one case style is used within the file (kebab-case or snake_case, never mixed) | Pass | Keys follow the workflow schema (kebab-case `runs-on`, `timeout-minutes`; snake_case `workflow_dispatch` is the tool's own name). |
| 13 | Multi-line strings use a block scalar (`\|` or `>`) and state the chomping indicator (`\|-`, `\|+`) where the trailing newline matters | Pass | Block scalars `run: |` hold commands; the trailing newline does not matter. |
| 14 | The file name is lowercase kebab-case with one extension style (`.yml` or `.yaml`) used throughout the repository | Pass | `ci.yml` and `.yamllint.yml`: lowercase, `.yml` throughout. |
| 15 | A change is exercised by a check that runs without the real target: a parse and schema test, or a dry run of the consuming tool | Pass | actionlint and yamllint run without the target host; a pull request run was also observed. |

## Overall Verdict

Go — every Mandatory criterion of QC-YML-001 passes or is not applicable with the reason stated. 

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Challenge this stand-in review in the pull request if it looks wrong | S01 | at the pull request review |

---

[YML-MIL-001]: ../../../.gitea/workflows/ci.yml
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md
