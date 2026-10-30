<EXTREMELY_IMPORTANT>

# Engineering conventions and working rules

Marcel Bruckner's engineering conventions apply to this session's software work (plugin engineering-conventions). Before designing, building, setting up, reviewing or choosing a stack for code in one of his repositories, load the `engineering-conventions` skill and read the pages that apply. When the user decides a rule for every repository, or a convention is wrong, load the `add-convention` skill and change the conventions themselves.

These working rules apply in every repository. Where a repository's CLAUDE.md or ADRs say otherwise, they win.

- Keep tool output small: quiet flags (`pytest -q`, `vitest --reporter=dot`), long output through `tail -n 40` or a targeted `grep`. While iterating, run only the tests that cover the change; run the full suite once before shipping.
- Read files by range when you know where to look. Don't re-read a file you've read or just edited.
- Search from the most likely path outward; don't sweep unrelated directories.
- No subagents unless asked. For search-only agents pass `model: haiku`.
- Skip brainstorming for small, clearly specified changes.
- Keep CLAUDE.md small: commands and non-obvious rules only. Put task-specific detail (recipes, style guides, background) in a project skill under `.claude/skills/<name>/SKILL.md` and leave a one-line pointer. When a CLAUDE.md you work in has grown such sections, offer to split them out.
- When a task is done (shipped, merged, or answered) and the next request is unrelated, tell me to `/clear` first.
- Replies: what changed and what's left. No preamble, no recap of the diff.
  </EXTREMELY_IMPORTANT>
