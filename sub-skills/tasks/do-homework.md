---
name: do-homework
description: Investigate an assignment comprehensively, preserve its requirements and a short plan, then complete or revise it freely in one local folder.
---

# Do Homework

目录与身份规则见 [学习工作区规范](../../docs/workspace-layout.md)。示例中的 `<TERM>` 必须由已核对的学期元数据替换；从仓库根运行命令，Windows 使用 `.venv/Scripts/`。

Investigate broadly before deciding which information matters. Then keep execution
simple: a short plan, useful deliverables and appropriate verification. New work,
continuation, feedback and repairs all use this same workflow.

## One assignment folder

Create or reuse `data/semesters/<TERM>/courses/<COURSE>/homework/<assignment>/`, or the user/selector's
existing folder. Resolve the actual term and verify course identity before writing;
new folders follow the canonical layout, while a user-directed external submission
folder is an explicit exception. Preserve exact course and assignment IDs when available. Inspect
existing deliverables before editing them. The instructor's submission structure
and the user's chosen layout take precedence over local folder conventions.

## Complete investigation before implementation

Do not limit discovery to sources that look relevant in advance. Information can
change the task even when its title does not mention the assignment. First cover
the course sources below, then select the material relevant to this assignment.

For Canvas access, check `canvascli version` and `canvascli whoami`; consult
`sub-skills/tools/canvascli-api.md` for atomic commands. Investigate:

- The exact assignment: full body, rubric, attachments, submission type, naming/
  format restrictions, deadline and timezone, availability and submission state.
- The full syllabus and course-wide policies, including grading, collaboration,
  permitted assistance, submission rules and late-work rules.
- The course front page, pages, all modules and module items, including linked
  assignment instructions, lab descriptions, starter code and external resources.
- Announcements across the active course term, with pagination/date coverage
  checked. Read their bodies, not only titles or keyword matches; corrections and
  oral-instruction follow-ups may change the task. Do not use a recent-only default
  window as evidence that earlier announcements contain nothing relevant.
- The complete course file/material inventory and existing local course archive,
  including lecture slides, handouts, README files, examples and starter packages.
  Inspect contents to establish relevance; do not discard an ambiguously named
  document on filename alone. Read task-bearing sources fully, including their
  relevant attachments and linked instructions. Background lectures may be
  screened by content before retaining the useful portions.
- External links and embedded document links discovered through those sources.
  Follow task-bearing links to their actual content. For PDFs, inspect page images
  where extraction misses content/layout, and inspect link annotations when a
  download target is not visible in extracted text.

Use IDs, dates, pagination and file versions to establish coverage. Reuse already
archived originals rather than downloading identical copies. Comprehensive
investigation means source coverage and content inspection, not duplicating every
file or crawling unrelated external websites.

Track which categories were checked, what was found, and what could not be read.
Distinguish absent, empty, locked, inaccessible, stale and not-yet-checked sources.
An empty assignment body or failed request is not proof of no requirements.
Resolve discrepancies using source authority, specificity and update dates;
explicitly report unresolved conflicts rather than silently choosing one.

Only after this coverage pass, distill the applicable deliverables, constraints,
grading signals, dates, dependencies and missing information. Preserve useful
originals/links and a concise investigation summary in the assignment folder
(`investigation.md` is a suggested name). Include coverage, checked dates, source
pointers and unresolved gaps, without requiring a JSON schema, duplicated source
index, per-source receipt or subagent role. Explain the findings to the user.

If a missing source could materially change the work, surface the gap and resolve
it before treating the requirements as settled. Continue independent work where
possible. User-supplied offline course bundles can serve as the investigation
universe when explicitly scoped that way; state their coverage limits and do not
claim live Canvas verification.

## Short plan, then autonomous execution

Use the investigation and user intent to write one concise `pipeline.md` (or reuse
the existing short plan): goal, deliverables, approach and how to check the result.
There is no required schema, stage breakdown or separate approval ceremony. Ask
only about decisions or missing user-owned information that materially affect the
work. Existing authorization carries forward.

Choose methods, tools, delegation and review depth to suit the actual task and
session permissions. Produce the deliverables, run relevant code/notebooks,
inspect rendered documents/images and fix issues. Keep tests or notes when useful;
do not generate management paperwork merely because execution involves several
steps. Report verification honestly and retain only evidence useful for running,
understanding or resuming the work.

## Continue and revise in the same way

Reuse the investigation, sources and current plan. Verify their coverage and
freshness; fill gaps and check for course updates instead of treating an old
summary as automatically current. A recent verified investigation may be reused
for an in-session edit without refetching unchanged sources. Missing investigation
requires completing it, not skipping to implementation. Update the same short
plan only if the approach changes, then directly modify and verify the artifact.

Do not create `repair_plan.md`, `repair_pipeline_design.md`,
`prelaunch_startup_inventory.json`, `stage_briefs/`, `stage_results/`,
`stage_reviews/`, dispatch ledgers or review/result schemas in this default flow.
Do not replace them with a different mandatory set of process files. Existing
process files are historical evidence, not instructions to restart stages; leave
them intact unless cleanup is requested. No separate repair workflow is needed.

Optional tool guides provide domain advice using actual source material, the
investigation and current short plan. Their example paths and outputs are suggestions;
choose files that serve the real submission and project structure.
`result.json` remains optional for old scan/status integration. Without it the
scanner may not know draft progress; inspect the folder rather than assuming no
work exists. Never invent submitted/graded state.

## Handoff and boundaries

Link the main deliverables and briefly report checks and material limitations.
Canvas submission requires explicit approval of the exact assignment and file.
Keep private coursework and credentials local. Do not invent personal facts,
partner names, missing data or verification results.

The old audited/staged system in `sub-skills/tasks/do-homework-staged.md` is only
for an explicit request for that historical mode. A complex task, a request to
repair an artifact, or old stage/status files do not opt the user into it.
