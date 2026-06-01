# Gnova Labs Session Record

> Last updated: Cursor (2026-06-01)
> Workspace: `C:\Users\king0\노바깨비법인`

---

## 2026-06-01

### Summary
- Investigated recent branch state for critical correctness regressions.
- Fixed a production 404 path where the main page sales CTA navigated to missing `gnova_sales_suite.html`.
- Added `tests/test_static_site_links.py` to validate local HTML asset links and JavaScript `location.href` targets.

### Validation
- Ran `python3 tests/test_static_site_links.py`.

### Safe Push Notes
- Safe code/docs changes committed and pushed to `cursor/critical-bug-investigation-de7e`.
- No secrets, logs, inbox dumps, runtime state, or raw local artifacts were staged.

### Local-Only Notes
- No new local-only items.

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
