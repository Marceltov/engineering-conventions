# What engineering-conventions stands for

engineering-conventions holds the standing rules for how Marcel Bruckner builds software, read by people and loaded by Claude. This page says what it will stay, whoever reads it and whatever it grows into.

It is for anyone deciding whether to follow these conventions, or a repository that does, and it is the yardstick for every change to them: a contribution, from a person or an AI, is judged against these points, and a review names the one it touches ("this breaks V3").

## Lines never crossed

When a convention would be easier to write, or would sound better, by bending one of these, it changes or is not written.

### V1. Every rule has a reason and a limit

A convention says why it exists and what it rules out. A rule without a reason can't be weighed when it doesn't fit; a rule without a _Rules out_ line can't be used in a review.

**Rules out:** rules stated as taste ("prefer X") without the problem they solve; pages without a **Rules out:** line; "we will / we won't" lists in place of reasons.

**ADRs:** none yet.

### V2. The repository wins

A repository's own `CLAUDE.md`, values page and ADRs override these conventions. The conventions are the default for what a repository hasn't decided, not a law over it.

**Rules out:** a convention that tells a repository to drop its own decision; a plugin or skill that applies a convention against what the repository says; changing a repository to match a convention without the user asking.

**ADRs:** none yet.

### V3. Public, so nothing private

This repository is public, so that every session and every contributor can read it without access to anything else. It holds only what may be read by anyone.

**Rules out:** hostnames, internal URLs, IP addresses, secrets or account details; personal notes; homelab specifics that only matter on Marcel's network (those stay in his private wiki).

**ADRs:** none yet.

## What you can rely on

### V4. Each rule is done somewhere

Every convention names a repository where it is applied, so it can be checked against working code rather than read as theory.

**Rules out:** a convention nobody has applied yet, presented as settled; a reference that no longer follows the rule.

**ADRs:** none yet.

### V5. Changes are visible

Conventions change through pull requests that say why. People read the change on the site; Claude gets it through the plugin's next version.

**Rules out:** changing a rule without saying why in its pull request; a docs change without a plugin version bump.

**ADRs:** none yet.

## Principles that follow

### V6. Versions only where the pin is the rule

Conventions outlive releases. A page names a version only when pinning it is the point (`mkdocs<2`, because MkDocs 2 breaks Material), and says why.

**Rules out:** "use Next.js 16"-style pages that are stale with the next release; version numbers as decoration.

**ADRs:** none yet.

## Changing this page

Points keep their numbers, so that reviews and issues citing them stay right. A change needs the maintainer's approval and says why in its pull request. Weakening a line never crossed is a change to what this repository is.
