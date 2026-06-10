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

## 2026-06-10

### Summary
- Investigated recent static-site commits for critical correctness regressions.
- Found top-level `템플릿 판매` navigation targeting missing `gnova_sales_suite.html`, causing a production 404.
- Restored `gnova_sales_suite.html` and added `tests/test_static_site_links.py` to catch missing local HTML/image/script targets.

### Validation
- `python3 tests/test_static_site_links.py`
- Simulated pre-fix checkout without `gnova_sales_suite.html`; the new test failed on the missing sales target as expected.

### Safe Push Notes
- Only safe static-site code, test, and this session record are intended for commit/push.
