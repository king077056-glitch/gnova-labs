# Shared Safety Rules

- Every substantial change should leave a short session record before closing the task.
- Do not commit or push secrets, logs, inbox dumps, recovery files, raw exports, runtime state files, or other local-only operational artifacts.
- Prefer small, reviewable commits that separate safe code/docs from local-only files.
- When remote backup is needed, stage only safe files, commit them, and push to the private remote branch.
- If the repo contains mixed safe/unsafe changes, keep unsafe files local and explain that they remain available only on this machine unless later sanitized.

# Gnova Labs Workspace Agent Instructions

**Read and follow this file at the start of each new chat or task.**

## Required Reads

1. `C:\Users\king0\노바깨비법인\\HANDOVER_NEXT.md` — if present, summarize current state before starting.
2. `C:\Users\king0\노바깨비법인\\ANTIGRAVITY_READ_FIRST.md` — if present, read fully.
3. `C:\Users\king0\노바깨비법인\\session_record.md` — review latest section before major edits.
4. `C:\Users\king0\노바깨비법인\\docs\\LOCAL_ONLY_EXCLUSIONS_TRACKER.md` — if present, check excluded local-only items.
5. `WORKSPACE_ROOT\docs\PROJECT_NOTES.md` - add project-specific required reads here if needed.

## Workspace Rules

- Work only inside `C:\Users\king0\노바깨비법인` unless the task explicitly requires a shared HQ file.
- Never push `.env` or local secret files.
- Leave a short session record after substantial work.
- Keep commits small and safe.

## Optional Project Notes

- Telegram prefix: `노바깨비법인`
- Add project-specific startup commands here.
- Add project-specific no-touch files or folders here.
