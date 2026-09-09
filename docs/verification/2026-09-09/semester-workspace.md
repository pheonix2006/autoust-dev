# Semester learning workspace validation

The current layout is defined in [workspace-layout.md](../../workspace-layout.md). Semester roots contain courses, reports, runs and sync/current; homework belongs to its course. Existing course folders and material categories retain their names.

## Validation performed

- `C:/Python313/python.exe -m pytest tests -q`: 57 passed. Includes semester isolation, course metadata mismatch, missing course identity, same-name assignments, legacy result compatibility, existing directory reuse and selection handoff.
- An offline scan using an existing local Canvas snapshot followed by numbered selection resolved the relocated existing homework directory.
- Local migration inventory and user-file hashes were checked before text-path updates; teacher originals and binary deliverables remained unchanged. Local relative links and helper Python syntax were checked after updates.
- Existing coursework tests passed in the relocated environment. Windows console entry points were regenerated for the new environment location.
- The existing scheduled task was updated using the scheduling tool and read back with its time, status and conversation binding preserved.
- `git diff --check` passed in the workspace and both repositories.

Private filenames, course contents, identifiers and recovery inventories are retained only under ignored `data/migrations/`. Historical design documents preserve their original facts with a status notice; the old introductory PDF is under `docs/history/`.

This validates local migration and offline behavior. It does not claim a fresh live Canvas scan, a homework submission, a new recurring-task run or a fresh-machine installation. Publishing to the personal fork main branch is authorized separately from this validation.
