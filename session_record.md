# Gnova Labs Session Record

> Last updated: Cursor (2026-05-27)
> Workspace: `C:\Users\king0\노바깨비법인`

---

## 2026-05-27

### Summary
- Investigated recent static-site navigation changes for critical correctness regressions.
- Restored `gnova_sales_suite.html`, the missing target for the main console "템플릿 판매" button.
- Added `tests/test_static_site_links.py` to catch missing local `href`, `src`, and `window.location.href` targets.

### Safe Push Notes
- Pushed safe site and test changes to `origin/cursor/critical-bug-investigation-4890`.
- Validation: `python3 tests/test_static_site_links.py`.

### Local-Only Notes
- No local-only files were intentionally created or changed.

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
