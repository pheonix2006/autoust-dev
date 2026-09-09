# Daily review: source coverage and change handling

Read from `daily-course-review.md` when running a course review. This is its
coverage appendix, not a separate user-facing task or scheduled job.

## Course-source coverage

Follow pagination to completion and retain per-entrance outcomes: `ok`, `empty`,
`locked`, `disabled_or_404`, or `failed`. A 404 does not prove the course contains
no pages or quizzes. Distinguish the endpoint result from linked objects that
remain readable. Avoid a recent-only announcement window: use the selected
term's actual coverage, with an explicit gap if historical coverage is unavailable.

| Entrance | Read and compare | Follow-up |
|---|---|---|
| Syllabus | HTML/text, attachments, source IDs, meaningful body changes | Read linked syllabus files even when the page only contains a link; compare rules with announcements and assignment details |
| Announcements | Complete bodies, titles, posted/delayed times, attachments and links, by announcement ID | Prioritize class changes, locations, exams, deadlines, grading and group requirements; queue body/attachment file IDs |
| Files and Folders | All file metadata, folder hierarchy, IDs, names, size, updated time, access/lock state | Establish file candidates and provenance; the Files listing is not the full resource universe |
| Assignments | Full detail per assignment, body, rubric, attachments, submission types, allowed extensions, unlock/due/lock times and submission state | Use supported `assignment` and `assignment-files` operations; queue body and attachment file IDs without submitting |
| Modules | All modules and each module's complete items, item IDs, order, type, target and title | Follow File targets and Page bodies; compare additions, removals and target changes |
| Pages and Front Page | Enumerate available pages and refresh the front page; read new/changed bodies | Resolve page links from modules even if the page index returns 404; queue file IDs and relevant course links |
| Discussions | Ordinary topic bodies and attachments, separate from announcements | Queue linked files; retain unavailable/locked outcomes |
| Quizzes | Available Quiz/New Quiz metadata and instructions, with assignment associations | Record unsupported/404 entrances; use assignment evidence where available; do not start attempts or request quiz answers |
| Calendar and Tabs | Course events for the chosen term; visible navigation/tool entrances | Catch events absent from assignments; record external/LTI entrances and coverage limits |

For external links, follow clearly accessible read-only course sources within
the chosen scope. Do not launch LTI sessions, log into another service, fill
forms or recursively crawl unrelated sites. Record the source and unresolved
access when a linked source cannot be inspected. Inspect PDF link annotations
when extracted text omits a task-bearing link.

## File discovery and archive

Union file IDs from Files, Syllabus, Announcements, Assignment bodies/attachments,
Module items, Pages/Front Page and Discussions. Preserve every source chain, such
as `assignment:<id> -> description -> file:<id>`. Deduplicate by course identity
and file ID, not display name. Resolve file metadata even for IDs absent from
Files. `hidden=true` alone is not a lock: archive an explicitly linked file when
the authenticated API permits it; never bypass a locked/unpublished resource.

Use `sync-course.md` in daily-review mode for archive conventions. Its old
Files-only snippets are not a complete implementation of this checklist.

- Compare file ID, size and `updated_at`. Reuse a local file only if prior
  metadata matches and its local hash agrees with the last verified receipt;
  retry missing/corrupt files and previous failures even when metadata matches.
- For candidates, download to a temporary file, verify the request and calculate
  SHA-256 before replacing a destination. Preserve a content-different old
  version in `_versions/`. Failed downloads leave the verified old copy intact.
- Identical remote content with different metadata is `metadata_only`, not a
  new version. Same content from multiple sources can reuse an archived copy;
  preserve all source records. Different file IDs with the same filename and
  different content need distinct destinations; never overwrite by name alone.
- Do not repeatedly download or generate notes for a verified duplicate. Record
  reuse. If the archive copy disappears, download again rather than trusting an
  old successful receipt.
- Metadata is a candidate filter, not proof of remote byte equality. If the
  server changes bytes without changing metadata, routine incremental checks
  may miss it; re-download on evidence of inconsistency or an explicit refresh.

## Changes, access and counts

Compare meaningful structured fields or normalized content, not only timestamp
or title. In particular, new body links, rubric changes, allowed extensions,
unlock/lock dates and submission states can matter without a file-list change.
Retain raw source bodies and evidence pointers for any derived summary.

Use separate dimensions instead of one ambiguous status list:

- Entrance coverage: `ok`, `empty`, `locked`, `disabled_or_404`, `failed`.
- Per discovered file, one primary outcome: `downloaded_new`,
  `downloaded_updated`, `metadata_only`, `unchanged`, `duplicate_content`,
  `locked_or_unpublished`, `read_failed`, or `download_failed`.
- Object transitions: added, changed, newly unlocked/locked, reappeared, or
  removed/no longer visible. These may accompany a primary file outcome and
  must not be added again to the file-outcome total.

The primary file-outcome counts must sum to the unique discovered-file count,
including metadata failures and duplicates. List previously known objects now
absent separately: they are not in today's discovered-file denominator.
When discovery is partial, label this denominator as the known discovered set,
not the total files in the course; unresolved old IDs remain visible separately.
Infer disappearance only from a successful complete comparable enumeration;
an API error, changed filter or incomplete page is not evidence of deletion.
Never delete archived teacher material merely because it is no longer visible.

## Evidence and completion

For each selected course, retain which entrances were checked, their results,
source objects/links, and whether changed content was actually read. For each
discovered file, retain metadata/access outcome, origins, local path and hash
when archived, or an explicit failure/lock reason. Redact authentication values
and signed download-URL secrets from human-facing reports.

Before claiming completion, check that all courses and entrances have outcomes,
every discovered file has an outcome, all accessible files were downloaded or
reused, and counts/links agree. Unresolved failed, unsupported or inaccessible
entrances are disclosed as coverage limits; state partial completion when a
required source cannot be checked. A fully reviewed but locked object is a
known limit, not evidence that its contents are empty.
