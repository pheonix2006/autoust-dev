---
name: tools-index
description: Capability menu for AutoStudy tools. Read this to discover what tools exist and what each can do. Sub-skills and appendices are discovered by reading the parent skill file, not listed here.
---

# Tools Index

For ordinary homework, these are optional domain guides. Their historical
spec/pipeline prerequisites and fixed document/output contracts do not apply;
`sub-skills/tasks/do-homework.md` governs. Load only a guide that improves the
actual deliverable, without adding process paperwork.

This is the **capability menu** for AutoStudy. Read this file to discover
available tools and their contracts. Each tool's full guidance lives in
`sub-skills/tools/<name>.md`.

Use the guides that improve the current artifact; no stage plan is required.

## Tool registry

| Tool | File | One-line capability | Inputs | Outputs |
|---|---|---|---|---|
| **pdf-renderer** | [pdf-renderer.md](./pdf-renderer.md) | Markdown → PDF (Chinese, LaTeX math, code, callouts) | markdown file, options | PDF file |
| **writing-helper** | [writing-helper.md](./writing-helper.md) | Structured academic prose (essay/report/reflection) | investigation.md, execution plan, rubric, references | draft.md |
| **paper-search** | [paper-search.md](./paper-search.md) | Literature search via arxiv → bib + json | keywords, max_results | references.bib, references.json |
| **figure-maker** | [figure-maker.md](./figure-maker.md) | Charts/plots via matplotlib | figure_spec dict | fig_N.pdf/png |
| **code-writer** | [code-writer.md](./code-writer.md) | Source code from spec (Python/C++/etc.) | investigation.md, execution plan, references | src/*.py + tests |
| **test-runner** | [test-runner.md](./test-runner.md) | pytest execution + report | actual project | verified results |
| **slide-maker** | [slide-maker.md](./slide-maker.md) | Presentation slides (guizang HTML or beamer) | investigation.md, execution plan | slides.pdf |
| **humanizer** | [humanizer.md](./humanizer.md) | Post-processing: reduce AI-detectable patterns | draft text | revised text |

Read a relevant parent guide, then its needed appendices. Existing runtime
tools may be used directly. Start homework with `do-homework.md`.

## Task registry

| Task | File | One-line capability | Trigger |
|---|---|---|---|
| **sync-course** | [../tasks/sync-course.md](../tasks/sync-course.md) | Persistent course material sync (files, announcements, modules) | "同步课程资料", "下载课件" |
| **write-course-notes** | [../tasks/write-course-notes.md](../tasks/write-course-notes.md) | Parallel Agent notes from lecture PDFs (Obsidian style) | "写笔记", "课程笔记" |

## Capability vocabulary

| Verb | Meaning |
|---|---|
| `render_pdf` | Markdown → PDF |
| `render_slides` | Slides (HTML/PDF) |
| `search_papers` | Literature search → bib |
| `make_figure` | Charts/plots |
| `write_essay` | Structured academic prose |
| `write_code` | Source code + tests |
| `run_tests` | Execute tests + report |
| `humanize` | Reduce AI patterns in text |

## What is NOT a tool

- ❌ Anything that talks to Canvas — that's `canvascli`
- ❌ One-off shell snippets the orchestrator can write inline
- ❌ Things that depend on services without a stable API
- ✅ Anything that produces a tangible artifact
- ✅ Anything reused across multiple task types

## Adding a new tool

1. Create `sub-skills/tools/<name>.md` with its scope, actual inputs, useful domain advice and appropriate checks
2. Add a row to the registry table above
3. If the tool has language/type-specific variants, create `<name>-<variant>.md` as an appendix file and list it in the parent skill's Appendices section
4. Do NOT list appendix files in this registry — they are discovered through the parent skill
