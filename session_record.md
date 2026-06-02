# Gnova Labs Session Record

> Last updated: Cursor (2026-05-26)
> Workspace: `C:\Users\king0\노바깨비법인`

---

## 2026-05-26

### Summary
- Record the substantial work completed in this session.
- Note which files or areas changed.
- Note whether the work was pushed to a private remote.

### Safe Push Notes
- Stage and push only safe code and documentation.
- Keep secrets, logs, inbox dumps, runtime state, and raw operational artifacts local-only unless sanitized.

### Local-Only Notes
- Record any files intentionally left local.
- If needed, point to `docs/LOCAL_ONLY_EXCLUSIONS_TRACKER.md`.

## 2026-06-02

### Summary
- Fixed the header `템플릿 판매` CTA so it routes to the existing in-page `무료 프롬프트` category instead of the missing `gnova_sales_suite.html` page.
- Added `tests/test_static_site_links.py` to catch future local `.html` navigation targets that point at absent files.

### Validation
- Ran `python3 tests/test_static_site_links.py` successfully.

### Local-Only Notes
- No local-only operational artifacts were staged for this change.
