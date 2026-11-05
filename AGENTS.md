# Working on skillshi

This repository holds personal, platform-neutral agent skill adaptations. Keep the canonical source in `skills/<name>/`; installed copies outside this repository are separate snapshots. Use the shared Agent Skills format with `name` and `description` frontmatter. Keep tool-specific metadata and invocation syntax out of the shared instructions.

Use skill-creator when available for additions or substantial revisions, and skill-installer when available for requested upstream installations. Otherwise follow the shared format and repository checks directly. Read upstream instructions before adapting them. Preserve useful local decisions and keep descriptions precise enough to distinguish related skills.

Keep each skill independently usable. Companion skills may improve a workflow, but document a fallback when they are optional. Add scripts, references, assets, or dependencies only for a demonstrated need. Preserve source attribution and applicable license notices in each distributable skill folder.

Do not import every skill mentioned as inspiration or copy a tool's built-in creator and installer skills into this collection. A new capability should serve an actual recurring task. Avoid mandatory tool brands, model rosters, delegation, or output formats unless that workflow requires them.

For skill changes, run skill-creator's `quick_validate.py` when available and the repository checks documented in README.md. Inspect realistic requests for routing, scope expansion, missing dependencies, and premature completion. Structural validation does not establish behavioral quality.

When creating a Git branch, use a descriptive name without the `codex/` prefix unless the user supplies an exact name. Local edits do not authorize pushing, publishing, or changing globally installed skills.
