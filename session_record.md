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

## 2026-06-07

### Summary
- Investigated recent static-site UI commits for high-severity correctness regressions.
- Fixed the header template/sales button so it no longer navigates to missing `gnova_sales_suite.html`; it now opens the existing in-page prompt/template category.
- Added `tests/test_static_site_links.py` to catch shipped HTML references and script navigations to missing local files.

### Validation
- Ran `python3 tests/test_static_site_links.py`.
- Served the app locally and recorded a browser walkthrough confirming the header button stays on the shipped page and renders the prompt category instead of a 404.

### Safe Push Notes
- Code, regression test, and this session record are safe to commit and push.

### Local-Only Notes
- No local-only artifacts intentionally left in the repo.
