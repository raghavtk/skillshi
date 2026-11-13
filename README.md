# skillshi

My personal collection of skills for coding agents: things I like to use, adaptations I've made, and ideas I've picked up from other people's workflows.

I wanted one place to keep them instead of leaving them scattered across my local setup. This repo gives me a history of what I've changed and somewhere to add the next useful skill I come across.

Most of these started with someone else's work. I've adapted them to fit how I like to work, and the original sources are credited below and in each skill. I want to keep the same instructions usable in Claude Code, Cursor, Codex, or another agent that supports the format.

## What's here

### Understanding code

- [how](skills/how/SKILL.md) follows the code to explain what happens, who owns the state, and where a change belongs.
- [why](skills/why/SKILL.md) looks through history and supporting records to explain a design decision, keeping evidence separate from inference.
- [teach](skills/teach/SKILL.md) brings the mechanics and rationale together in a plain explanation.
- [tutor](skills/tutor/SKILL.md) builds deeper understanding through guided questions, practical exercises, review, and assessment. It also works for topics beyond code.

### Designing and reviewing changes

- [frontend-design](skills/frontend-design/SKILL.md) builds distinctive interfaces with a focused Quickdraw tier and a deeper Art Director tier, including interaction and motion guidance.
- [landing-page-design](skills/landing-page-design/SKILL.md) plans, builds, and critiques marketing pages and portfolios around what visitors need to see and do.
- [ui-ux-helpers](skills/ui-ux-helpers/SKILL.md) helps choose and review patterns for forms, navigation, accessibility, responsive layouts, and data displays.
- [architect](skills/architect/SKILL.md) works through callers, interfaces, ownership, and migration before a substantial change.
- [improve-codebase-architecture](skills/improve-codebase-architecture/SKILL.md) finds places where a refactor could make the code easier to understand, change, or test.
- [code-review](skills/code-review/SKILL.md) checks a change against its requirements and the repository's standards.
- [blast-radius](skills/blast-radius/SKILL.md) follows a change beyond the diff and tests the assumptions its safety depends on.
- [principle-foundational-thinking](skills/principle-foundational-thinking/SKILL.md) focuses on data structures, ownership, and invariants before adding logic.

### Testing and measurements

- [testing-conventions](skills/testing-conventions/SKILL.md) covers reliable fixtures, subprocesses, cleanup, and integration tests.
- [principle-test-behavior-not-implementation](skills/principle-test-behavior-not-implementation/SKILL.md) keeps tests focused on what a consumer can observe.
- [principle-explain-the-number](skills/principle-explain-the-number/SKILL.md) checks what a benchmark or evaluation actually measured before drawing conclusions.

### Writing

- [prose-writing](skills/prose-writing/SKILL.md) helps draft and revise technical explanations and documentation.
- [unslop](skills/unslop/SKILL.md) edits out formulaic writing while preserving the meaning, voice, and useful caveats.

## Using a skill

Each folder in [skills](skills/) contains a `SKILL.md` and its upstream license notice. The instructions use the shared [Agent Skills format](https://agentskills.io/specification), with no required vendor metadata, model names, or tool-specific orchestration.

Copy a whole skill folder into the location your tool reads. For example, installing `blast-radius` means placing its `SKILL.md` and `LICENSE` inside a folder named `blast-radius`:

- **Claude Code:** `.claude/skills/` in a project, or `~/.claude/skills/` for personal use. See the [Claude Code skills docs](https://code.claude.com/docs/en/skills).
- **Cursor:** `.cursor/skills/` in a project, or `~/.cursor/skills/` for personal use. Cursor also reads `.agents/skills/` and `~/.agents/skills/`. See the [Cursor skills docs](https://cursor.com/docs/skills).
- **Codex:** `.agents/skills/` in a project, or `~/.agents/skills/` for personal use. See the [Codex skills docs](https://learn.chatgpt.com/docs/build-skills).

Here, `~` means your home directory, including on Windows. Compare existing copies before replacing them. Keep the source in this repo and install only the skills you want; there's no need to maintain a separate version of each skill for every tool.

Invocation syntax belongs to the tool: Claude Code and Cursor use `/skill-name`, while Codex supports `$skill-name`. For example:

```text
/how Explain how this request reaches the database.
/blast-radius Check what this change could break downstream.
/tutor Help me understand this subsystem well enough to debug it independently.

Use $prose-writing to clean up this README.  (Codex)
```

The repo and installed copies are separate. Editing a skill here doesn't update the copy your agent uses. Portability covers the instructions and file format; each agent still needs the tools, repository access, and permissions required by the task. The directory examples above are for local coding tools, not every chat or cloud interface.

## Credits

Much of what I like about these skills came from:

- **Anthropic** and **Emil Kowalski** contributed the visual and interaction design guidance adapted in frontend-design. [Anthropic's skill](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) · [Emil's skill](https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md)
- **Leonxlnx**, **Paul Bakaus**, **Adam Wathan**, and **Steve Schoger** informed landing-page-design. [Design Taste](https://github.com/Leonxlnx/taste-skill) · [Impeccable](https://github.com/pbakaus/impeccable) · [Refactoring UI](https://refactoringui.com/)
- **Next Level Builder** provided the prioritized UX guidance adapted in ui-ux-helpers. [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

- **Lauren Tan (poteto)** and [pstack](https://github.com/cursor/plugins/tree/main/pstack): architect, blast-radius, how, why, teach, prose-writing, unslop, and the three principle skills. Prose-writing draws on pstack's technical-writing and unslop skills. The design and ownership guidance in improve-codebase-architecture also draws on pstack's architect and foundational thinking skills.
- **Matt Pocock** and his [skills collection](https://github.com/mattpocock/skills): code-review and improve-codebase-architecture. I also looked at his teach skill; the version here keeps the narrower focus on explaining code rather than creating a learning workspace.
- **Kun Chen** and [no-mistakes](https://github.com/kunchenguid/no-mistakes): testing-conventions, adapted from that project's testing guidance.
- **Jane Street** and [socratic-tutor](https://github.com/janestreet/agent_skills/tree/master/socratic-tutor): tutor, combining its interactive learning workflow with code-grounded explanation practices from Lauren Tan's pstack teach skill.

These are personal adaptations. Some instructions are shorter, optional dependencies have fallbacks, and workflows that relied on a particular tool's models or orchestration have been rewritten to work with the agent's available tools.

Each skill links its specific sources and includes the relevant upstream license notices. [Third-party notices](THIRD_PARTY_NOTICES.md) lists which notices apply to which skills.

## Keeping the collection useful

I expect this collection to grow as I find things worth keeping. The source of truth is `skills/<name>/`. Upstream changes get reviewed manually so they don't overwrite the adaptations here.

For additions or substantial revisions, use skill-creator when available, or follow the same shared format directly. Keep each skill focused on a recurring task, with extra scripts or references only when they help. Tool-specific creators and installers aren't required dependencies or copied into this repo.

To check the collection, use Python 3.10 or newer:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_skills.py
python -m unittest discover -s tests
```

When available, also run skill-creator's `scripts/quick_validate.py` against changed skills. CI runs the repository validator and tests on pushes and pull requests.

The checks catch packaging mistakes such as invalid frontmatter, missing local links, or missing license notices. They don't prove that an instruction works well in practice. That takes trying it on real tasks and adjusting it when something falls short.
