# AutoStudy Learning Workspace

A multi-semester, multi-course learning workspace for Codex / Claude Code and similar agents. Canvas CLI provides Canvas access; AutoStudy supplies file organization, source investigation guidance and focused task instructions. It has been used with HKUST(GZ) Canvas; verify capabilities and permissions on other instances.

[中文](README.md) · [Canonical layout](docs/workspace-layout.md) · [Setup](sub-skills/tools/canvascli-setup.md)

This fork is [pheonix2006/autoust-dev](https://github.com/pheonix2006/autoust-dev), based on [Aurorra1123/autoust-dev](https://github.com/Aurorra1123/autoust-dev). The matching CLI is [pheonix2006/canvascli](https://github.com/pheonix2006/canvascli).

## Start in one learning project

Open your chosen learning project and ask the agent:

```text
Prepare https://github.com/pheonix2006/autoust-dev and
https://github.com/pheonix2006/canvascli as sibling, independent repositories.
Inspect and reuse existing directories without overwriting them. Read
 autoust-dev/skill.md, follow setup, verify my Canvas term and courses,
and initialize the learning workspace.
```

Clone the complete repositories, not just a skill file. Prefer installing the sibling Canvas CLI checkout in editable mode into AutoStudy's `.venv/`. Windows uses `.venv/Scripts/`; macOS/Linux use `.venv/bin/`. Both Git histories remain independent and can be used from one parent project.

First-time setup requires browser SSO. Check with `canvascli version` and `canvascli whoami`. Supported GET requests in this fork attempt automatic renewal using saved SSO state; interactive login is needed only when renewal is unavailable or fails. Keep credentials private.

## Organize and work

The [layout specification](docs/workspace-layout.md) is authoritative. Data lives in `data/semesters/<TERM>/`, with courses, reports, runs and `sync/current/`. Each course retains `meta.json`, `index.md`, `canvas_sync/`, `materials/{lectures,readings,other}` and `notes/`, and contains `homework/<assignment>/`. `data/workflows/` and `data/setup/` remain global.

Resolve the actual Canvas term first: for example, `2026-27 Fall` maps to directory `2026-27-Fall`. Preserve readable course slugs and validate course/assignment IDs. Canvas `assignments.json` is a source snapshot; `homework/` holds deliverables. Link shared course originals rather than copying them unnecessarily.

Ask for deadlines, course downloads, notes, homework creation/revision, or a daily course review. Status scans suggest actions without executing the whole list. Homework investigates the complete course context before filtering relevance, preserves a concise investigation summary and one short `pipeline.md`, then executes and verifies autonomously. Continuing or repairing work uses the same flow. No mandatory stage paperwork or separate repair pipeline; legacy staged mode requires an explicit request.

A one-off course review creates no schedule. Recurring reviews follow the user's time, timezone, scope and notification preferences, reuse existing schedules, maintain semester reports and daily records, and preserve human notes. Scheduling requires a capable environment and available host/application. Installation does not create personal automations.

Private coursework and credentials stay local. Canvas submission requires explicit authorization. Do not invent inaccessible source content, personal facts or validation results.

## Development

Read [DEVELOPMENT.md](docs/DEVELOPMENT.md). `skill.md` is a lightweight task router; `sub-skills/` adds domain advice and does not replace general tools already available in the runtime. Historical designs and validation records retain their original facts and do not govern ordinary work. Migration must update links, scripts and automation paths as well as moving files.
