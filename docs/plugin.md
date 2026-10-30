# Using the Claude Code plugin

This repository is also a Claude Code plugin. It brings the same pages as this site, a skill that says which page applies when, a skill that adds new conventions, and a short note at the start of each session that the conventions exist.

## Install

In Claude Code:

```
/plugin marketplace add Marceltov/engineering-conventions
/plugin install engineering-conventions@engineering-conventions
```

On claude.ai, add the repository as a plugin marketplace for your account, so cloud sessions get it as well.

## What it does

- **At session start**, and again after `/clear`, compaction and resume, a hook adds a short note to the context: the conventions apply, which skill to load when, the [working rules for Claude sessions](claude/session-rules.md) (small output, narrow reads, no unasked subagents, short replies), and that the repository's own rules win. It replaces the `rules` plugin of Marceltov/claude-marketplace: install one, not both.
- **The skill `engineering-conventions`** maps the task to the pages to read (for example: sign-in work reads [Sign-in](architecture/sign-in.md) and the stack page) and says how to apply them: the repository wins, use the _Rules out_ line, name the page in a review, don't change a repository unasked.
- **The skill `add-convention`** adds, changes or retires a convention: a page in the shape every page has, listed in the menu, the index and the reading skill's table, a version bump and a pull request to this repository. It is used when you decide a rule for every repository ("make this a convention"), or when a convention turns out wrong.
- **The pages** are read from the installed plugin, so they match the version installed.

## In a repository

Add one line to the repository's `CLAUDE.md`:

```markdown
- Follows Marceltov/engineering-conventions; the rules here win where they differ.
```

## Updates

Every change to the pages, the skill or the hook bumps the plugin's version, so installed plugins pick it up.
