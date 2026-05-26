# Gnova Labs Session Record

> Last updated: Cursor (2026-05-26)
> Workspace: `C:\Users\king0\노바깨비법인`

---

## 2026-05-26

### Summary
- Fixed a production 404 regression where the main header's template-sales button routed to missing `gnova_sales_suite.html`.
- Added `gnova_sales_suite.html` as a small static sales target using the existing G-NOVA visual language and local assets.
- Added `tests/test_static_site_links.py` to validate local `href`, `src`, and `window.location.href` references resolve.

### Safe Push Notes
- Stage and push only safe code and documentation.
- Keep secrets, logs, inbox dumps, runtime state, and raw operational artifacts local-only unless sanitized.
- Changed files are safe static HTML, a Python validation script, and this session record.

### Local-Only Notes
- No local-only artifacts were added.
