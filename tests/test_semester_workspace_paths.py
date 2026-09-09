"""Offline scan/selection integration, including colliding semester identities."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def run(script, cwd, *args):
    return subprocess.run([sys.executable, str(ROOT / "scripts" / script), *args],
                          cwd=cwd, text=True, capture_output=True)


def fixture(tmp_path, term, status="draft_ready"):
    semester = tmp_path / "data" / "semesters" / term
    course = semester / "courses" / "AIAA3201--L02"
    write(course / "meta.json", {"course_id": "42", "term": term})
    write(semester / "sync/current/courses.json", [{"id": 42, "course_code": "AIAA3201 (L02)"}])
    write(semester / "sync/current/assignments.json", [
        {"id": 88, "course_id": 42, "name": "Lab 1", "submission_state": "unsubmitted"}])
    write(course / "homework/lab-1/result.json", {
        "course_id": "42", "assignment_id": "88", "status": status,
        "work_dir": "data/homework/old/stale-path"})
    return semester, course


def test_scan_and_select_are_scoped_and_reuse_migrated_folder(tmp_path):
    fixture(tmp_path, "2025-26-Fall", "submitted")
    semester, course = fixture(tmp_path, "2026-27-Fall")
    scan = run("write_scan_plan.py", tmp_path, "--term", "2026-27 Fall", "--date", "2026-09-09")
    assert scan.returncode == 0, scan.stderr
    plan = json.loads((semester / "runs/2026-09-09/plan.json").read_text())
    assert plan["term"] == "2026-27-Fall"
    assert plan["items"][0]["existing_result_status"] == "draft_ready"
    selected = run("select_plan_item.py", tmp_path, "--term", "2026-27-Fall", "--date", "2026-09-09", "--index", "1")
    assert selected.returncode == 0, selected.stderr
    item = json.loads(selected.stdout)
    assert item["term"] == "2026-27-Fall"
    assert item["suggested_work_dir"] == "data/semesters/2026-27-Fall/courses/AIAA3201--L02/homework/lab-1"
    assert (tmp_path / item["existing_result_path"]).is_file()
    assert not (tmp_path / "data/runs").exists()
    assert not (tmp_path / "data/homework").exists()


def test_new_identical_titles_use_ids_and_course_meta(tmp_path):
    semester, course = fixture(tmp_path, "2026-27-Fall")
    write(semester / "sync/current/assignments.json", [
        {"id": aid, "course_id": 42, "name": "New lab"} for aid in (89, 90)])
    (course / "homework/new-lab").mkdir()
    scan = run("write_scan_plan.py", tmp_path, "--term", "2026-27-Fall", "--date", "2026-09-09")
    assert scan.returncode == 0, scan.stderr
    items = json.loads((semester / "runs/2026-09-09/plan.json").read_text())["items"]
    assert {Path(item["suggested_work_dir"]).name for item in items} == {"new-lab--89", "new-lab--90"}
    assert all("AIAA3201--L02/homework/" in item["suggested_work_dir"] for item in items)


def test_existing_unique_folder_without_result_is_reused(tmp_path):
    semester, course = fixture(tmp_path, "2026-27-Fall")
    (course / "homework/lab-1/result.json").unlink()
    result = run("write_scan_plan.py", tmp_path, "--term", "2026-27-Fall", "--date", "2026-09-09")
    assert result.returncode == 0, result.stderr
    item = json.loads((semester / "runs/2026-09-09/plan.json").read_text())["items"][0]
    assert item["suggested_work_dir"].endswith("/homework/lab-1")


def test_snapshot_course_from_other_term_is_filtered(tmp_path):
    semester, _ = fixture(tmp_path, "2026-27-Fall")
    write(semester / "sync/current/courses.json", [{"id": 42, "term": {"name": "2025-26 Fall"}}])
    result = run("write_scan_plan.py", tmp_path, "--term", "2026-27-Fall", "--date", "2026-09-09")
    assert result.returncode == 0, result.stderr
    plan = json.loads((semester / "runs/2026-09-09/plan.json").read_text())
    assert plan["items"] == []
    assert plan["counts"]["filtered"] == {"other_semester": 1}


def test_legacy_result_is_read_but_new_path_is_suggested(tmp_path):
    semester, course = fixture(tmp_path, "2026-27-Fall")
    legacy = tmp_path / "legacy"
    write(legacy / "result.json", {"course_id": "42", "assignment_id": "99", "status": "pipeline_ready"})
    write(semester / "sync/current/assignments.json", [{"id": 99, "course_id": 42, "name": "Legacy"}])
    scan = run("write_scan_plan.py", tmp_path, "--term", "2026-27-Fall", "--homework-dir", str(legacy), "--date", "2026-09-09")
    assert scan.returncode == 0, scan.stderr
    item = json.loads((semester / "runs/2026-09-09/plan.json").read_text())["items"][0]
    assert item["existing_result_status"] == "pipeline_ready"
    assert item["suggested_work_dir"].endswith("/courses/AIAA3201--L02/homework/legacy--99")


def test_missing_term_and_path_traversal_fail_without_writes(tmp_path):
    for script, args in (("write_scan_plan.py", []), ("select_plan_item.py", ["--index", "1"]),
                         ("write_scan_plan.py", ["--term", "../other"])):
        result = run(script, tmp_path, *args)
        assert result.returncode != 0
    assert not (tmp_path / "data").exists()


def test_duplicate_course_identity_fails_before_run_write(tmp_path):
    semester, _ = fixture(tmp_path, "2026-27-Fall")
    write(semester / "courses/duplicate/meta.json", {"course_id": "42"})
    result = run("write_scan_plan.py", tmp_path, "--term", "2026-27-Fall")
    assert result.returncode != 0
    assert "ambiguous course_id" in result.stderr
    assert not (semester / "runs").exists()


def test_explicit_wrong_semester_plan_is_rejected(tmp_path):
    semester, _ = fixture(tmp_path, "2026-27-Fall")
    assert run("write_scan_plan.py", tmp_path, "--term", "2026-27-Fall", "--date", "2026-09-09").returncode == 0
    result = run("select_plan_item.py", tmp_path, "--term", "2025-26-Fall", "--runs-dir", str(semester / "runs"), "--date", "2026-09-09", "--index", "1")
    assert result.returncode != 0
    assert "different semester" in result.stderr


def test_wrong_semester_course_root_override_is_rejected(tmp_path):
    fixture(tmp_path, "2026-27-Fall")
    older, _ = fixture(tmp_path, "2025-26-Fall", "submitted")
    result = run("write_scan_plan.py", tmp_path, "--term", "2026-27-Fall", "--courses-dir", str(older / "courses"))
    assert result.returncode != 0
    assert "different semester" in result.stderr


def test_course_metadata_term_must_match_even_when_receipt_is_terminal(tmp_path):
    semester, course = fixture(tmp_path, "2026-27-Fall", "submitted")
    write(course / "meta.json", {"course_id": "42", "term": "2025-26 Fall"})
    result = run("write_scan_plan.py", tmp_path, "--term", "2026-27-Fall")
    assert result.returncode != 0
    assert "metadata belongs to a different semester" in result.stderr
    assert not (semester / "runs").exists()


def test_unknown_course_snapshot_identity_fails_without_run_write(tmp_path):
    semester, _ = fixture(tmp_path, "2026-27-Fall")
    write(semester / "sync/current/courses.json", [])
    result = run("write_scan_plan.py", tmp_path, "--term", "2026-27-Fall")
    assert result.returncode != 0
    assert "course_id 42 is missing from courses snapshot" in result.stderr
    assert not (semester / "runs").exists()
