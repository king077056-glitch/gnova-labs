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

## 2026-06-13

### Summary
- Investigated recent static-site changes for high-severity regressions.
- Fixed the header `템플릿 판매` button so it no longer navigates to missing `gnova_sales_suite.html`; it opens the existing in-page `무료 프롬프트` category instead.
- Added `tests/test_static_site_links.py` to validate local `href`, `src`, and script `location` targets.

### Safe Push Notes
- Safe code/test/docs changes only.

### Local-Only Notes
- No local-only artifacts were intentionally left behind.
