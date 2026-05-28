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

## 2026-05-28

### Summary
- Investigated recent static-site changes for critical correctness bugs.
- Restored the missing `gnova_sales_suite.html` target for the main header "템플릿 판매" navigation.
- Added `tests/test_static_site_links.py` to catch missing local HTML, image, and redirect references.

### Validation
- Ran `python3 tests/test_static_site_links.py` successfully.

### Safe Push Notes
- Pushed only safe site code, tests, and this session record to `cursor/critical-bug-investigation-1403`.

### Local-Only Notes
- No local-only artifacts were intentionally created or retained.
