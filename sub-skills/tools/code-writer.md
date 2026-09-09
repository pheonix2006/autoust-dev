---
name: code-writer
description: Write source code from assignment spec. Provides domain guidance for code quality — language-specific conventions are in appendix files loaded on demand.
---

# code-writer

> Follow [do-homework](../tasks/do-homework.md) and the [workspace layout](../../docs/workspace-layout.md).
> This is optional domain guidance. Use the actual investigation, short plan and
> deliverables; paths and output examples below are suggestions, not required schemas.

Code generation workhorse. Reads the assignment workbench and writes source
files into `<work_dir>/src/`. This file provides cross-language guidance;
language-specific conventions (project structure, testing, toolchain) are
in appendix files loaded according to the task language.

**Skills provide reference guidance, not hard constraints.** If the task spec
explicitly requires a different approach, follow the spec.

## Inputs and outputs

Read the actual source requirements, rubric, concise investigation summary and
current `pipeline.md`, plus relevant originals and existing deliverables. Reuse
verified evidence; no standardized spec file or stage declaration is required.
Write to the assignment folder using its real submission/project structure.
Suggested filenames below may be adapted to that structure.

## Guidance

### Parse the spec from the workbench

Read `investigation.md`, `pipeline.md`, rubric, and references end-to-end.
Identify:

- **Language**: Python is default. Record in pipeline.md if not already there.
- **Required functions / classes / entry points**: look for "implement", "complete",
  function signatures. Use those exact names — auto-graders match by name.
- **I/O contract**: input format, expected output, datasets.
- **Algorithm constraints**: complexity bounds, allowed libraries, "implement from scratch".
- **Test cases**: translate spec-provided input/output pairs into tests.

If spec names a specific dataset, paper, function, or algorithm — implement that,
not a generic equivalent. If ambiguous on a specific point, write
`[CLARIFICATION NEEDED: <question>]` as a comment and continue with a defensible default.

### Write the code

Style rules (defaults — spec overrides if it says otherwise):

- Implement what spec actually asks. Not a generic representative project.
- One responsibility per file. Don't dump everything into `solution.py`.
- Top of every file: 1-line docstring. No multi-paragraph docstrings.
- No comments unless the WHY is non-obvious.
- Type hints on public functions.
- Use stdlib where possible.
- **No `[TODO: align with actual project spec]` or equivalent placeholders.**
  Use `[CLARIFICATION NEEDED: <question>]` instead.
- `if __name__ == "__main__":` is mandatory for runnable entry points.
- Don't shadow stdlib names (no `os.py`, `json.py`, etc.).
- Use `pathlib.Path(__file__).parent` for relative paths, never hard-code absolute paths.
- No `print()` debug statements in submitted code. Wrap in `if __debug__:` or remove.
- Seed `random`/`numpy.random` with `seed=42` if spec requires reproducibility.

### Write the tests

Test meaningful behavior, required examples and edge cases appropriate to the change.
Avoid implementation-mirroring tests and do not add tests for trivial reversible edits.
Use the project's existing test organization where available.

### Write the README

`src/README.md` — 5-10 lines: how to run, expected output, assumptions made.

## Appendices (loaded on demand)

| Appendix | When to load |
|---|---|
| [code-writer-python.md](./code-writer-python.md) | When `lang: python`, or when the spec/starter files indicate Python |
| `code-writer-cpp.md` (future) | When `lang: cpp` |

Read this parent file first, then load the matching language appendix for
toolchain-specific conventions (project structure, dependency management, testing).

## Post-processing

- Hand off to `test-runner.md` to verify code passes its own tests
- If the assignment also asks for a report, `writing-helper.md` drafts prose next
- If `pipeline.md` declares `post-process: humanize` for code comments,
  load `humanizer.md`

## Self-check

- [ ] `investigation.md` and `pipeline.md` were read completely (not just title)
- [ ] Code implements what the spec asks, not a generic equivalent
- [ ] All required functions/classes from spec are implemented with exact names
- [ ] Code can run in a clean environment without errors
- [ ] Notebooks were actually executed — output cells are not fabricated estimates
- [ ] Report data metrics come from actual execution results
- [ ] No `[TODO]` / `[PROBLEM N]` / `[此处填入...]` placeholders
- [ ] Only `[CITATION NEEDED]` and `[CLARIFICATION NEEDED]` markers used
- [ ] Relevant behavioral checks pass and cover required cases
- [ ] README explains how to run and expected output
