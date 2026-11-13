# Language and internationalization

**Code, identifiers, the API, MCP tool names and descriptions, logs, commit messages and docs are English. Every UI is built for more than one language from the start, even while it ships one: its strings come from one copy module per language, English first, and the page speaks the language the user picked or their browser asks for.** Decided 2026-10-31. Not for a content site in one language (below), added 2026-11-12.

## Why

English keeps the code, the tool descriptions Claude reads and the docs in one language that every contributor and model handles well. The people using an app don't all read English, and adding a second language late means hunting strings through every component. With the strings in one module per language, typed against the English one, a translation is one file and a missing string is a type error.

## How

- **One copy module per language and surface**, English first: questlog has `components/copy/en.ts` and `de.ts` for the web app. The other languages are typed as the English module (`const de: Copy = { … }`), so a string missing from one fails the typecheck. Components import strings through a helper, never text of their own.
- **Picking the language**: the user's choice (a cookie set by a switch in the header) wins, then the browser's `Accept-Language` by weight, then English. Server components read it per request; client components get it from a provider.
- **In Next.js, Next's own pattern** (its internationalization guide), decided 2026-11-13: every page lives under `app/[lang]/`, and the proxy picks the language as above and **rewrites** the request to `/<lang>/<path>`, so no URL carries the language and every shared link and bookmark keeps working. The proxy also passes the language on as a request header, so a server component below a page reads it without a `lang` prop; client components get it from a provider. Route handlers (the API, MCP, feeds, files) stay outside `app/[lang]`. The root layout is `app/[lang]/layout.tsx`; an address no route matches gets `app/global-not-found.tsx` (the `globalNotFound` flag), since the root layout sits in a dynamic segment. ESLint's `react/jsx-no-literals` keeps text out of JSX.
- **The page says its language**: `<html lang>` follows the choice, and anything in another language (a language's own name in the switch) carries its own `lang`.
- **Dates and numbers** written out in words are formatted for the language (`Intl`); ISO dates (`2026-10-31`) read the same in every language.
- **Tool descriptions and `guidance` instructions stay English**, whatever the UI speaks: they are written for Claude, not for the user.
- **Docs** in more languages sit next to the English pages (`index.de.md`, with [mkdocs-static-i18n](https://github.com/ultrabug/mkdocs-static-i18n)) and fall back to English where a page is missing.
- **What the user types** (a name, a game's German stat names) is kept as they wrote it, next to the English where the app needs one.
- The project's `CLAUDE.md` names the languages and the copy files.

## Where it stops

**A content site in one language is not a UI in this sense.** A local business's website, written for one market and carrying legal texts that must be in that language (terms, withdrawal notice, imprint), keeps its prose in its pages: the text is the content, like Markdown, and pulling it into a copy module makes it harder to edit without making a second language any closer. What such a site still does:

- Values that more than one page shows (prices, contact details, terms quoted on several pages) live in one module, not copied into each page.
- Numbers, money and durations are formatted in one place, with `Intl` where it applies.
- `<html lang>` names the language, and `CLAUDE.md` says the site is in one language on purpose.

When such a site gets a second language, or grows an app-like part (an account, a dashboard), the rule above applies to that part.

## Rules out

- Identifiers, logs or docs in German (or mixed).
- User-facing strings inline in components or route handlers, or a UI built for one language only (a one-language content site excepted, see _Where it stops_).
- A copy module per language that isn't checked against the English one.
- In Next.js, a language in the URL (`/de/…`) or a locale library in place of `app/[lang]` and the proxy rewrite.
- Translating what the user wrote.

## Reference

questlog (Marceltov/questlog#29: the copy modules, the language choice and the switch; #30: the docs in German); questlog also keeps the game's own language next to the English (its values, V8). freundebuch still has one German copy file (`components/copy.ts`). Next's pattern with the rewrite: notefeed (notefeed/notefeed#352: `app/[lang]`, `proxy.ts`, `shared/copy/`, English only for now). A one-language content site: 3dbruckner.de (3D-Bruckner/3dbruckner#32, closed for this reason; shared values in `src/lib/content.ts`).
