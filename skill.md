---
name: autostudy
description: Multi-semester Canvas learning workspace. Check assignments, complete homework, archive materials, review daily course changes and support course learning. Validated on HKUST(GZ).
---

# AutoStudy Learning Workspace

Read [workspace-layout.md](docs/workspace-layout.md) for canonical paths and term/course identity.
Use sibling independent AutoStudy and Canvas CLI repositories in one chosen project;
`sub-skills/` contains focused domain guidance, not a mandatory execution pipeline.

Run from this repository; resolve `.venv/`, `data/`, `scripts/` and
`sub-skills/` relative to its root. Canvas access is provided by the separate
`canvascli` repository. Use its CLI rather than reimplementing the data layer.

## Choose the task

| User request | Read |
|---|---|
| What is due / check or sync Canvas status | `sub-skills/tasks/sync-status.md` |
| Review course changes, maintain a semester overview and daily journal, or set up recurring Canvas review | `sub-skills/tasks/daily-course-review.md` |
| Do, continue, fix, review or package an assignment | `sub-skills/tasks/do-homework.md` |
| Download/archive course materials | `sub-skills/tasks/sync-course.md` |
| Generate course notes | `sub-skills/tasks/write-course-notes.md` |
| First-time setup or expired login | `sub-skills/tools/canvascli-setup.md` |

Load only the relevant task and the tools it needs.

`daily-course-review` handles both one-off reviews and user-requested scheduling.
Its Codex schedule defaults to the current conversation and respects user notification intent;
setup resolves a time (suggested 08:00), timezone, scope and notification preferences.
It maintains the semester overview and daily journal, with brief preparation
notes enabled by default. A one-off review does not create a schedule.

## Homework default

Create or reuse `data/semesters/<TERM>/courses/<COURSE>/homework/<assignment>/`. First investigate the
course comprehensively: assignment/rubric, syllabus, announcements, modules/pages,
course documents and linked resources. Cover sources and inspect their contents
before filtering for task relevance; do not narrow discovery in advance.
Preserve useful sources and a concise investigation summary, then one short
`pipeline.md`. Execute and verify freely without stage documents or phase approvals.

New work, continuation and repairs share this workflow. Reuse verified sources,
check freshness and fill coverage gaps; do not create separate repair plans or
repair pipelines. `sub-skills/tasks/do-homework.md` is authoritative. Old staged
contracts and tool-guide prerequisites do not override it; the old system is
available only on explicit request through `sub-skills/tasks/do-homework-staged.md`.

## Setup and Canvas access

Use the repository virtual environment. On Windows executables are under
`.venv/Scripts/`; on macOS/Linux they are under `.venv/bin/`.

Before using Canvas, run `canvascli version` and `canvascli whoami` from that
environment. `whoami` checks the saved session; `init` is login/refresh, not a
health check. If setup is missing or a request fails with an expired session,
read `sub-skills/tools/canvascli-setup.md` and complete the missing step before
retrying Canvas. A local-only task does not need Canvas login.

For installation, prepare full sibling repositories `autoust-dev/` and `canvascli/`
in the user's chosen learning project. Inspect and reuse existing directories;
never overwrite a nonempty target. Prefer editable installation of the sibling
CLI into the selected local virtual environment. Follow the setup guide.

For other Canvas operations, consult `sub-skills/tools/canvascli-api.md`. Never
print or copy saved authentication state or tokens into work products.

## Status handoff

`sync-status` reports and recommends; it does not start every listed assignment.
When the user selects a numbered item, run:

```bash
.venv/bin/python scripts/select_plan_item.py --term "<actual Canvas term>" --index <N> --pretty
```

Use `.venv/Scripts/python.exe` on Windows. Preserve the returned `course_id`,
`assignment_id` and `suggested_work_dir`; do not re-match by title. Pass the
selection to `do-homework.md`, including older `pipeline_ready` or `draft_ready`
records. Inspect existing work rather than automatically restarting old stages.
Optional legacy status helpers remain readable.

## User interaction and boundaries

- Communicate in Chinese unless the user asks otherwise.
- Ask only when missing information or ambiguity would materially affect the
  result. Continue authorized work; routine implementation and checking do not
  need additional permission.
- Ground requirements in sources. Do not invent user-owned facts, inaccessible
  content or verification results.
- Create useful deliverables and check them appropriately. Link the main result
  and state material gaps without generating paperwork for its own sake.
- Keep private coursework and credentials local. Canvas submission requires
  explicit approval of the exact assignment and file. Drafting is not submission.
- Course-wide downloads and scheduled automation stay within the user's chosen
  scope; they are not implied by finishing one assignment.
