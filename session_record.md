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

## 2026-06-06

### Summary
- Investigated recent static-site commits for critical breakage.
- Restored `gnova_sales_suite.html` so the main page's template-sales CTA no longer routes to a missing local page.
- Added `tests/test_static_site_links.py` to catch missing local HTML, image, script, and `location.href` targets.

### Safe Push Notes
- Only safe static-site code, tests, and this session record were changed.

### Local-Only Notes
- No local-only files were added.
