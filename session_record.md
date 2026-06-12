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

## 2026-06-12

### Summary
- Investigated recent static-site commits for critical correctness regressions.
- Found that the production header action `템플릿 판매` navigated to missing local page `gnova_sales_suite.html`, producing a user-facing 404.
- Added `gnova_sales_suite.html` as the sales suite landing page target.
- Added `tests/test_static_site_links.py` to validate local `href`, `src`, and `window.location.href` references.

### Validation
- Ran `python3 tests/test_static_site_links.py` successfully.

### Safe Push Notes
- Only static HTML, test code, and this session record were changed.
