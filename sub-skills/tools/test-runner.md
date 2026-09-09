---
name: test-runner
description: Verify assignment code and runnable artifacts with task-appropriate behavioral checks.
---

# Test Runner

Follow [do-homework](../tasks/do-homework.md) and the [workspace layout](../../docs/workspace-layout.md). Use the actual assignment requirements, current short plan and existing project structure. No fixed `src/`, stage contract or JSON report is required.

Choose checks that establish required behavior: instructor examples, meaningful edge cases, executable entry points and notebooks, plus relevant existing tests. Do not fabricate outputs or equate a zero exit code with correct results. Verify packaging in a fresh environment when reproducibility is part of the requested deliverable.

Locate the virtual environment from the known AutoStudy root before changing directories. Run its Python by explicit path; do not expect `.venv/` inside a nested assignment. On Windows it is `.venv/Scripts/python.exe`, on Unix `.venv/bin/python`.

Example from the repository root, after replacing placeholders:

```text
<venv-python> -m pytest "<assignment-directory>" -q
```

Run only applicable tests; pytest exit 5 means no tests were collected, not a pass. Also execute the documented entry point with its expected working directory and inputs. Preserve exit codes and inspect relevant outputs, figures and numerical results. Install missing dependencies into the selected environment only when needed.

Fix discovered problems and rerun affected checks. Report the actual commands, results and material limits concisely in the handoff or an existing verification note. Machine-readable reports are optional legacy integration artifacts. Passing local checks does not authorize Canvas submission.
