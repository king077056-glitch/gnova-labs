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

## 2026-06-09

### Summary
- Investigated recent static-site commits for high-severity regressions.
- Fixed the top-level `템플릿 판매` CTA 404 by adding `gnova_sales_suite.html`.
- Added `tests/test_static_site_links.py` to catch missing local HTML/asset targets.

### Safe Push Notes
- Changes are limited to static HTML, a lightweight Python validation script, and this session record.
- No secrets, logs, runtime state, or local-only artifacts were staged.

### Validation Notes
- Run `python3 tests/test_static_site_links.py`.
