# SQLite

**A self-hosted app keeps its data in one SQLite file in `DATA_DIR`, through `better-sqlite3` and `kysely`. Migrations live in code, in order, and a migration that has shipped is never edited.**

## Why

One file on one volume is the simplest thing to run, back up and move, and it is enough for an app used by one household or a few people. `kysely` gives typed queries without an ORM's hidden behaviour; the [one gate for every read](../architecture/one-gate-for-every-read.md) sits in that query layer.

## How

- **One file per concern** in `DATA_DIR`: the app's data (`<app>.sqlite`), and the sign-in's own file (`auth.sqlite`, or [mcp-login-oauth](mcp-login-oauth.md)'s `oauth.sqlite`), so that backups and exports of the data hold no sessions or tokens.
- **Migrations** in `backend/db/migrations.ts`, applied at start-up in order. A change to the schema is a new migration; a shipped one is never edited, because databases out there already ran it.
- **Typed queries** with `kysely` over `better-sqlite3`. Every read of a guarded table goes through the gate function.
- **Tests** run against a fresh database with a fixture seed.
- **When an app must scale to several instances**, it moves to Postgres through the same `kysely` layer. That is a decision with its own ADR, not a default.

## Rules out

- Editing a migration that has shipped.
- Schema changes outside migrations.
- Tokens or sessions in the app's own data file.
- Raw SQL strings scattered through the code where `kysely` can express the query.

## Reference

freundebuch (`backend/db/migrations.ts`, `kysely`, `better-sqlite3`).
