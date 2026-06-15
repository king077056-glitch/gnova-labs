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

---

## 2026-06-15

### Summary
- Investigated recent static-site changes for high-severity regressions.
- Fixed the `템플릿 판매` header button so it no longer navigates to missing `gnova_sales_suite.html`; it now opens an in-app template sales category.
- Added `tests/test_static_site_links.py` to catch missing same-site static targets in HTML attributes and JavaScript navigation.

### Validation
- `python3 tests/test_static_site_links.py`
- `node --check /tmp/gnova_inline_script.js`

### Safe Push Notes
- Safe code/test changes were committed and pushed to `cursor/critical-bug-investigation-881b`.
- No secrets, logs, runtime state, or local-only operational artifacts were staged.
