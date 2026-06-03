# Gnova Labs Session Record

> Last updated: Cursor (2026-06-03)
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

## 2026-06-03

### Summary
- Investigated recent static-site changes for critical correctness regressions.
- Restored the missing `gnova_sales_suite.html` page targeted by the homepage `템플릿 판매` CTA.
- Added `tests/test_static_site_links.py` to fail on missing local static references, including JavaScript `window.location.href` redirects.

### Validation
- Verified before the fix that `gnova_metal_console.html` referenced `gnova_sales_suite.html` while the target file did not exist.
- Planned validation: run `python3 tests/test_static_site_links.py` and perform a browser walkthrough of the CTA.

### Local-Only Notes
- No local-only operational artifacts were staged for this change.
