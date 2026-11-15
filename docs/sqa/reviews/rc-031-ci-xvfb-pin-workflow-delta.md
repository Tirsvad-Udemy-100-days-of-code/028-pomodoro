# Review Record: CI workflow, delta re-review of criteria 17 and 22

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-031 |
| CrossReference | [WF-CI], [QC-WF-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [f528e5f] |

---

## Artifact Under Review

- Instance reviewed: [WF-CI] (.gitea/workflows/ci.yml)
- Checklist used: [QC-WF-001]
- Scope: delta re-review of criteria 17 and 22 only. Reason: the apt archive dropped `xvfb=2:21.1.12-1ubuntu1.8` (the install step failed with "Version ... was not found" on the pull request of MIL-006), so `XVFB_VERSION` was changed to `2:21.1.12-1ubuntu1.9`, the version in noble-updates, as the header of the workflow prescribes. Earlier records: RC-015 and RC-019 (all other rows still hold).
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the author is the same AI)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place | Pass | `libtk8.6=8.6.14-1build1` and `xvfb=2:21.1.12-1ubuntu1.9` are still pinned, with the values in the one `env` block; only the value of `XVFB_VERSION` changed. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header | Pass | The pull_request run of MIL-006 after the change succeeded on the Gitea instance (log: `Setting up xvfb (2:21.1.12-1ubuntu1.9)`, 93 tests passed); the header records the date of this run. |

## Overall Verdict

Go — both criteria pass and the other rows of RC-015 and RC-019 are unchanged. Not independent: author and reviewer are the same AI.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Challenge this stand-in review in the pull request if it looks wrong | S01 | at the pull request review |

---

[WF-CI]: ../../../.gitea/workflows/ci.yml
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md
[f528e5f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/commit/f528e5fdd2d95ccd05fd66c17834113ccc278f91
