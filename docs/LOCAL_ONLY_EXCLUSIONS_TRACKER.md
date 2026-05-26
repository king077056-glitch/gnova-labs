# Local-Only Exclusions Tracker

Last updated: 2026-05-26
Scope: `Gnova Labs`

## Purpose

Track files that remain only on the local machine and are intentionally excluded from safe private pushes.

## Rules

- Secrets, logs, inbox dumps, raw notes, recovery memos, and runtime state files are local-only by default.
- Local-only files are not deleted; they remain on this machine unless explicitly cleaned up.
- Before pushing any excluded item later, sanitize and review it first.

## Current Local-Only Items

| Area | Local path example | Why excluded | What is needed before push |
|---|---|---|---|
| Secrets / env | `.env`, `.env.local` | May include tokens, keys, or machine-specific values | Replace with sanitized template |
| Logs / inbox | `logs/`, `telegram_inbox/`, `discord_inbox/` | May include personal or operational history | Extract sanitized samples only |
| Runtime state | `runtime_state.json` | Environment-specific live state | Generalize into docs if needed |
| Raw notes | `raw/`, `drafts/` | Unreviewed or sensitive working material | Review and reduce scope first |

## Review Notes

- Add repo-specific local-only files here.
- Update this tracker before or after selective private pushes.
