# Gnova Labs Session Record

> Last updated: Cursor (2026-06-05)
> Workspace: `C:\Users\king0\노바깨비법인`

---

## 2026-06-05

### Summary
- Fixed a critical static-site navigation regression where the header `템플릿 판매` CTA pointed to missing `gnova_sales_suite.html`.
- Added `gnova_sales_suite.html` as the shipped Template Sales Suite destination page.
- Added `tests/test_static_site_links.py` to catch missing local HTML/asset/script redirect targets.

### Validation
- Ran `python3 tests/test_static_site_links.py` successfully.
- Served the site locally with `python3 -m http.server 8000`.
- Verified `/gnova_sales_suite.html` returns HTTP 200 and contains the Template Sales Suite headline.
- Manually clicked the `템플릿 판매` CTA in Chrome and confirmed the sales suite page renders instead of a 404.

### Safe Push Notes
- Safe code/test/docs changes were committed and pushed to `origin/cursor/critical-bug-investigation-e6ee`.
- No secrets, logs, inbox dumps, runtime state, or raw exports were staged.

### Local-Only Notes
- Local static server left running for follow-up validation.

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
