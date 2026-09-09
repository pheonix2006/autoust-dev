"""Explicit semester-scoped paths shared by local workspace commands."""
from pathlib import Path
import json
import re


def semester_dir(data_dir: Path, term: str) -> Path:
    term = re.sub(r"\s+", "-", term.strip())
    if not term or term in {".", ".."} or term.endswith(".") or re.search(r'[<>:"/\\|?*\s]', term):
        raise ValueError("--term must be a single directory name, e.g. 2026-27-Fall")
    return data_dir / "semesters" / term


def course_directory(courses_dir: Path, cid: str, code: str, expected_term: str) -> Path:
    normalized_term = semester_dir(Path("data"), expected_term).name
    resolved = courses_dir.resolve()
    if resolved.parent.parent.name == "semesters" and resolved.parent.name != normalized_term:
        raise ValueError(f"course root belongs to a different semester: {courses_dir}")
    matches = []
    for meta_path in courses_dir.glob("*/meta.json"):
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        if str(meta.get("course_id", meta.get("id"))) == cid:
            matches.append((meta_path.parent, meta))
    if len(matches) > 1:
        raise ValueError(f"ambiguous course_id {cid}: multiple course directories")
    if matches:
        directory, meta = matches[0]
        declared_term = meta.get("term")
        if isinstance(declared_term, dict):
            declared_term = declared_term.get("name")
        if not isinstance(declared_term, str) or not declared_term.strip():
            raise ValueError(f"missing term in course metadata: {directory / 'meta.json'}")
        if semester_dir(Path("data"), declared_term).name != normalized_term:
            raise ValueError(f"course metadata belongs to a different semester: {directory / 'meta.json'}")
        return directory
    safe_code = re.sub(r"[^A-Za-z0-9_-]+", "-", code).strip("-") or "COURSE"
    safe_id = re.sub(r"[^A-Za-z0-9_-]+", "-", cid).strip("-")
    if not safe_id or safe_id != cid:
        raise ValueError(f"invalid course_id: {cid}")
    return courses_dir / f"{safe_code}--{safe_id}"
