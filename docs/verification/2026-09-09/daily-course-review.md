# Daily course review validation

This change adds an agent task and a source-coverage appendix, not a standalone
scanner. Runtime settings and course artifacts remain under ignored `data/`.

## Checks

- Existing repository regression suite: `uv run --no-project --with pytest
  --with pyyaml python -m pytest -q tests` — 46 passed.
- The skill-creator validator accepted the root skill and the new task's YAML
  frontmatter (the task was copied to a temporary `SKILL.md` for validation).
- Independent read-only review covered routing, scheduling, source coverage,
  archive/note integration and privacy boundaries. It identified ambiguity in
  the first-time time question; this was corrected and independently rechecked.
  General setup authorization cannot skip the time question, and silence is not
  acceptance of the 08:00 default.

## Independent offline review exercise

A separate agent used the task to produce an overview, daily journal and a
downloaded text attachment in an isolated temporary directory from synthetic API
records. The maintainer inspected the actual outputs and verified the attachment
SHA-256. No real course data was used.

The scenario combined a fixed course scope, an extra accessible course, a Files
pagination failure, a linked Page readable despite a Pages-index 404, and a new
Assignment-body attachment with `hidden=true` but `locked_for_user=false`.

Observed behavior:

- Kept the fixed scope and performed a one-off review without scheduling.
- Archived the accessible body-linked attachment missing from the Files list.
- Reported partial coverage, retained the old baseline, and did not infer that
  an unseen old file was deleted after a failed page request.
- Counted the two known discovered files once each: one unchanged and one new.
- Preserved the existing same-day attempt and handwritten overview annotation.
- Converted the supplied UTC deadline to the configured local timezone.
- Did not generate notes when the saved preference disabled them.

The source appendix additionally clarifies that counts from partial discovery
describe the known discovered set, not the course's total file count.

A second offline exercise enabled preparation notes and provided a three-page
lecture text fixture plus an existing detailed note with a handwritten question.
The agent produced a separate brief Chinese preview with page references and
self-check questions, retained the old note, and preserved an unrelated handwritten
index entry while linking the new preview. It explicitly labeled the source as
an offline fixture and did not claim a real PDF download or rendering check.

## Scope of evidence

No real Canvas account was scanned and no live schedule was created, moved or
edited during development. These checks do not demonstrate a future timed
trigger or real SSO availability. On first use, the task must verify the host's
scheduling capability and read back the actual schedule and conversation binding.
The user's existing personal automation is not migrated by publishing this task.
