# Gnova Labs Session Record

> Last updated: Cursor (2026-06-11)
> Workspace: `C:\Users\king0\노바깨비법인`

---

## 2026-06-11

### Summary
- Investigated recent static-site commits for high-severity regressions.
- Confirmed the header `템플릿 판매` CTA redirected to missing `gnova_sales_suite.html`, causing a production 404 for a top-level route.
- Added `gnova_sales_suite.html` as the intended sales destination and `tests/test_static_site_links.py` to catch missing local static references, including JavaScript redirects.

### Validation
- Ran `python3 tests/test_static_site_links.py` successfully.

### Safe Push Notes
- Pushed safe code/test changes to `origin/cursor/critical-bug-investigation-40fa`.
- No secrets, logs, runtime state, or local-only operational artifacts were staged.

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
