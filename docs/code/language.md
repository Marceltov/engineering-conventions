# Language and internationalization

**Code, identifiers, the API, MCP tool names and descriptions, logs, commit messages and docs are English. Every UI is built for more than one language from the start, even while it ships one: its strings come from one copy module per language, English first, and the page speaks the language the user picked or their browser asks for.** Decided 2026-10-31.

## Why

English keeps the code, the tool descriptions Claude reads and the docs in one language that every contributor and model handles well. The people using an app don't all read English, and adding a second language late means hunting strings through every component. With the strings in one module per language, typed against the English one, a translation is one file and a missing string is a type error.

## How

- **One copy module per language and surface**, English first: questlog has `components/copy/en.ts` and `de.ts` for the web app. The other languages are typed as the English module (`const de: Copy = { … }`), so a string missing from one fails the typecheck. Components import strings through a helper, never text of their own.
- **Picking the language**: the user's choice (a cookie set by a switch in the header) wins, then the browser's `Accept-Language` by weight, then English. Server components read it per request; client components get it from a provider.
- **The page says its language**: `<html lang>` follows the choice, and anything in another language (a language's own name in the switch) carries its own `lang`.
- **Dates and numbers** written out in words are formatted for the language (`Intl`); ISO dates (`2026-10-31`) read the same in every language.
- **Tool descriptions and `next` instructions stay English**, whatever the UI speaks: they are written for Claude, not for the user.
- **Docs** in more languages sit next to the English pages (`index.de.md`, with [mkdocs-static-i18n](https://github.com/ultrabug/mkdocs-static-i18n)) and fall back to English where a page is missing.
- **What the user types** (a name, a game's German stat names) is kept as they wrote it, next to the English where the app needs one.
- The project's `CLAUDE.md` names the languages and the copy files.

## Rules out

- Identifiers, logs or docs in German (or mixed).
- User-facing strings inline in components or route handlers, or a UI built for one language only.
- A copy module per language that isn't checked against the English one.
- Translating what the user wrote.

## Reference

questlog (Marceltov/questlog#29: the copy modules, the language choice and the switch; #30: the docs in German); questlog also keeps the game's own language next to the English (its values, V8). freundebuch still has one German copy file (`components/copy.ts`).
