# AutoStudy

> Local Canvas LMS study-assistant skill, validated on HKUST(GZ)'s Canvas instance.
> Sync Canvas, plan deadlines, investigate assignments, draft reviewable
> artifacts, archive course materials, and generate course notes.

Other versions:

- [Default Chinese README](./README.md)
- [Quick Chinese README](./README.quick.md)

This fork is maintained at [pheonix2006/autoust-dev](https://github.com/pheonix2006/autoust-dev),
based on [Aurorra1123/autoust-dev](https://github.com/Aurorra1123/autoust-dev).

AutoStudy is a **local Canvas LMS skill package** for Claude Code /
Codex-style agentic coding environments, validated on HKUST(GZ)'s Canvas
instance. You ask in natural language; the agent reads `skill.md`, calls the
local `canvascli` data layer, writes evidence and artifacts into this
repository, and asks before key actions.

It gathers Canvas context, explains findings, and produces local artifacts you
can inspect, edit, and decide whether to submit. You can also schedule course
reviews in the current Codex conversation, with visible start, progress and
completion messages in that same conversation.

---

## What You Can Ask

```text
"看看这周有什么作业"
"同步课程状态"
"Review my courses daily and maintain the semester overview and daily journal"
"帮我完成 DSAA2011 Project，先生成本地草稿，不提交"
"继续改上次那个 report，让实验讨论更深入"
"同步 DSAA2011 的课件"
"把 DSAA2011 的 lecture notes 写出来"
```

Current user-facing tasks:

| Task | What It Does | Output |
|---|---|---|
| `sync-status` | Refreshes Canvas courses, assignments, announcements, and creates an assistant plan. It does **not** execute assignments. | `data/runs/<date>/REPORT.md`, `plan.json`, `pending_assignments.json` |
| `daily-course-review` | Reviews course changes once or on a schedule, maintains the semester overview/daily journal, and prepares brief notes for new lectures by default. | `data/reports/<term>/`, reusing existing reports and course archives |
| `do-homework` | Creates or reuses an assignment folder and completes/verifies local work according to the actual task. | `data/homework/<COURSE>/<HWID>/` |
| `sync-course` | Archives course files, announcements, and module structure for reuse. | `data/courses/<COURSE>/` |
| `write-course-notes` | Generates Obsidian-style Markdown notes from synced lecture PDFs. | `data/courses/<COURSE>/notes/` |

The older M3 proof-of-concept scenarios, paper / slides / math / lab, have all
been validated on real HKUST(GZ) Canvas assignments. The current main line is
Default homework is task-driven: complete investigation, a short plan, then autonomous execution.
The former M3.5 staged workflow is explicit opt-in only.

---

## Daily Course Review

Ask for a daily course review to use [daily-course-review](sub-skills/tasks/daily-course-review.md).
Setup asks for a time, defaults to **08:00**, and displays the timezone, semester,
course scope and preparation-note setting. Codex uses a schedule in the **current
conversation**, showing start, quick-scan and final messages there, including
unchanged days. Keep the computer and desktop app running. If this scheduling
capability is unavailable, the task explains the limitation and supports manual
review. Matching existing schedules are updated rather than duplicated.

Reviews check syllabus, announcements, assignments and linked attachments,
Files, Modules/Pages and other course entrances. The first review builds a
baseline; later reviews inspect changes and unresolved sources, maintaining the
current semester overview and daily journal. New lectures get brief preparation
notes by default; this is configurable and preserves handwritten annotations.
Failed reads are reported as gaps, never as evidence of no changes.

A request to review now runs once. Changing a scheduled review reuses its saved
settings. All course content, reports, notes and personal settings remain local
under ignored paths. Publishing this task does not create a schedule or migrate
an existing personal automation.

## Quick Start

### 1. Load The Skill

AutoStudy is a full local repository, not a standalone `skill.md` file. On a
first run, the safest flow is to open an empty project folder in Claude Code /
Codex, then ask the agent to clone AutoStudy into the current directory:

```text
Clone https://github.com/pheonix2006/autoust-dev into the current empty folder,
then read skill.md and help me initialize it.
```

The agent should confirm the current directory is empty, then run the equivalent
of:

```bash
git clone https://github.com/pheonix2006/autoust-dev.git .
```

If the current directory is not empty, or if no clear project folder is open,
the agent should ask where to place the repository instead of silently choosing
`~/workspace`, Desktop, Downloads, or another implicit location.

You can also provide an explicit folder:

```text
Clone https://github.com/pheonix2006/autoust-dev into ~/workspace/autoust-dev,
then enter that folder, read skill.md, and help me initialize it.
```

If you prefer to clone it yourself:

```bash
mkdir -p ~/workspace
git clone https://github.com/pheonix2006/autoust-dev.git ~/workspace/autoust-dev
cd ~/workspace/autoust-dev
```

Then tell the agent from that directory:

```text
Use the AutoStudy skill in the current directory. Read skill.md and help me initialize it.
```

`~/workspace/autoust-dev` is only an example location, not a default. Any local folder is fine.
The important part is that AutoStudy stays as its own repository folder because
`.venv/`, `data/`, `scripts/`, and `sub-skills/` are all used relative to it. The
agent should read `skill.md`, check the environment, and install missing
dependencies into the local `.venv/`.

### 2. Complete Canvas Login Once

AutoStudy uses the separate [`canvascli`](https://github.com/Aurorra1123/canvascli)
data layer. On the first run, the agent confirms your Canvas school/domain or
login page, then opens a browser for that Canvas SSO:

```bash
.venv/bin/canvascli init --canvas-url "https://canvas.example.edu"
```

The saved Canvas session is stored locally:

```text
~/Library/Application Support/canvascli/state.json
```

That file is a credential. Agents must not print it, copy it into chat, or
commit it. To check whether the saved session still works, run:

```bash
.venv/bin/canvascli whoami
```

`canvascli init` is a login/refresh command, not a health check.

### 3. Start With Status

The safest first request is:

```text
看看这周有什么作业
```

AutoStudy will:

1. fetch Canvas courses, assignments, and announcements;
2. save current sync snapshots under `data/sync/current/`;
3. write a dated run under `data/runs/<date>/`;
4. show numbered next-step recommendations;
5. wait for you to choose whether to start an assignment.

If you choose a numbered item, AutoStudy uses `scripts/select_plan_item.py` to
resolve exact Canvas IDs and the suggested workbench. After a numbered selection,
the agent should not re-match by title.

---

## How Homework Works Now

Create or reuse `data/homework/<COURSE>/<assignment>/`. Investigate the course
comprehensively before filtering relevance: assignment/rubric, full syllabus,
term-wide announcement bodies, front page, modules/pages, complete course file
inventory and local materials, plus discovered task-bearing links. Inspect
contents rather than discarding sources by title. Record coverage and access gaps.

Preserve useful sources and a concise investigation summary. Keep one short
`pipeline.md` covering goal, deliverables, approach and verification. Then execute,
check and revise freely, without stage briefs/reviews, ledgers or phase approvals.
Continuation and repairs use the same investigation and plan: check freshness and
fill gaps, without separate repair plans/pipelines. A current investigation can be
reused for an in-session edit. Legacy staged mode requires an explicit request.

Canvas submission requires explicit authorization. Optional `result.json` records
remain readable by scanning; inspect the folder when local progress is unrecorded.
Existing assignment files are not automatically cleaned up. Legacy `pipeline_ready`
and `draft_ready` records remain readable; they do not activate staged execution.

---

## Course Materials And Notes

To sync reusable course context:

```text
同步 DSAA2011 的资料
```

This routes to `sync-course`, confirms scope, then archives files and Canvas
structure under:

```text
data/courses/<COURSE>/
├── materials/
├── canvas_sync/
├── notes/
├── meta.json
└── index.md
```

Then:

```text
写 DSAA2011 的课程笔记
```

routes to `write-course-notes`, which reads lecture PDFs from the course archive
and writes structured Markdown notes under `notes/`.

---

## Repository Map

```text
AutoStudy/
├── skill.md                         # User-facing skill entry and routing
├── README.md                        # Default Chinese README
├── README.en.md                     # English full README
├── README.quick.md                  # Chinese quick README
├── scripts/
│   ├── write_scan_plan.py           # Canvas snapshot -> plan/report
│   ├── select_plan_item.py          # Numbered plan item -> exact handoff
│   └── write_homework_result.py     # Stable result.json writer
├── sub-skills/
│   ├── tasks/
│   │   ├── sync-status.md
│   │   ├── do-homework.md             # investigate, plan, execute freely
│   │   ├── do-homework-staged.md      # legacy opt-in router
│   │   ├── background-recon.md        # legacy mode
│   │   ├── existing-work-recon.md     # legacy mode
│   │   ├── alignment-planning.md      # legacy mode
│   │   ├── task-orchestrator.md
│   │   ├── sync-course.md
│   │   ├── daily-course-review.md
│   │   └── write-course-notes.md
│   └── tools/
│       ├── canvascli-setup.md
│       ├── canvascli-api.md
│       ├── assignment-recon.md
│       ├── code-writer.md
│       ├── writing-helper.md
│       ├── pdf-renderer.md
│       ├── slide-maker.md
│       └── ...
├── docs/
│   ├── DEVELOPMENT.md
│   ├── ROADMAP.md
│   ├── COLLABORATION.md
│   ├── runtime-agent-protocol.md
│   ├── skills-architecture-spec.md
│   ├── PITFALLS.md
│   ├── plans/feature-list.json
│   └── progress/agent-progress.md
└── data/                            # Local Canvas snapshots and artifacts
```

`data/` is a local workspace and is gitignored. It may contain course files,
assignment drafts, verification logs, and result receipts.
Current Canvas sync snapshots live under `data/sync/current/`, while each
scan-plan run keeps its own copied evidence under `data/runs/<date>/raw/`.

---

## Current Status

Passing and usable:

- Canvas data layer via `canvascli`.
- `sync-status` scan-plan flow.
- `do-homework`: one assignment folder with task-driven implementation and verification.
- Legacy `task-orchestrator` execution only when explicitly requested.
- M3 tools: prose, code, figures, tests, slides, PDF rendering, humanizer.
- Course material sync and course-note generation.
- Optional legacy `result.json` records for scan/status integration.

Still being hardened:

- Clean process validation for the unified executor/reviewer runtime.
- Retained-artifact repair and multi-turn iteration ergonomics.
- Course-level and user-level preference memory.
- Real Canvas submission E2E on a safe, unexpired sandbox assignment.
- Multi-runtime support beyond the current Claude Code-oriented skill surface.

Detailed status:

- [docs/ROADMAP.md](./docs/ROADMAP.md)
- [docs/plans/feature-list.json](./docs/plans/feature-list.json)

---

## Safety And Academic Integrity

- AutoStudy never auto-submits to Canvas.
- `sync-status` proposes a plan but never auto-executes plan items.
- Broad downloads, homework drafting, and file submission should have user
  confirmation points.
- AutoStudy should not fabricate group details, datasets, personal experience,
  partner names, instructor oral instructions, or inaccessible source material.
- Drafts are local artifacts for you to inspect, revise, and own.
- The intended use is to reduce repetitive work and improve traceability, not to
  hide responsibility from the student.

When unsure, AutoStudy should stop and explain uncertainty instead of guessing.

---

## Contributing

For development work, start with [docs/DEVELOPMENT.md](./docs/DEVELOPMENT.md).
It explains the boundary between AutoStudy and `canvascli`, the Canvas Copilot
reference, branch policy, progress/backlog updates, and verification rules.
