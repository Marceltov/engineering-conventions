# One gate for every read

**When some rows must not reach some readers (another user's private items, another player's log, a spoiler the player hasn't reached), that rule is one function in the query layer, and every read goes through it: lists, single items, counts, summaries, hints and notifications.**

## Why

A rule applied in each read path is missed in one of them, and the one that is missed is usually a count or a summary, where nobody looks: "3 private notes" already tells the other user something. One function can be tested once, with a seed that has both kinds of rows, and a new read path either uses it or is visibly wrong in review.

## How

- **One function per rule**, named for what it guards: freundebuch's `visible()` in `backend/visibility.ts`; questlog's spoiler check and its per-player scope sit in the same query layer.
- **Every query on a guarded table goes through it**, including aggregates. Derived output (a briefing, a tool's `next`, a notification) is built only from rows that came through it.
- **The tests use a fixture seed** with rows on both sides of the rule (two users, shared and private items) and assert, per read path, that the hidden rows don't appear in any form, counts included.
- **The values page names the rule** as a line never crossed, so a review can cite it.

## Rules out

- Filtering hidden rows in a route handler, a component or a tool instead of in the query.
- A count, a total, a "you might also" hint or a summary computed from unguarded rows.
- A new read path on a guarded table without a test against the seed.
- An admin view or a debug endpoint that skips the gate.

## Reference

freundebuch: `backend/visibility.ts`, `backend/testing/fixtures.ts`, ADR 0002 (privacy model). questlog applies the same pattern to spoilers and to one log per player (values V1, V2).
