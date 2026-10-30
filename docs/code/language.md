# Language

**Code, identifiers, the API, MCP tool names and descriptions, logs, commit messages and docs are English. The UI speaks the language its users speak, and every UI string comes from one copy file per surface.**

## Why

English keeps the code, the tool descriptions Claude reads and the docs in one language that every contributor and model handles well. A UI for German-speaking users is German, but strings scattered through components can't be reviewed, reworded or translated together.

## How

- One copy module per surface: freundebuch has `components/copy.ts` for the web app and `backend/notify/copy.ts` for notifications. Components import strings from it; they don't contain user-facing text.
- Tool descriptions and `next` instructions are English, even in an app whose UI is German: they are written for Claude, not for the user.
- The project's `CLAUDE.md` names the UI language and the copy files.
- What the user types (a name, a game's German stat names) is kept as they wrote it, next to the English where the app needs one.

## Rules out

- Identifiers, logs or docs in German (or mixed).
- User-facing strings inline in components or route handlers.
- Translating what the user wrote.

## Reference

freundebuch (`components/copy.ts`, `backend/notify/copy.ts`, its `CLAUDE.md`); questlog keeps the game's own language next to the English (values V8).
