# 06\_CONTEXT\_LIBRARY\_INDEX.md

```yaml
project_file_projection: 1
schema: direction_project_file_projection.v1
source_file: "directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md"
canonical_source: GitHub repository file
projection_status: fresh
activated_at: "2026-05-11"

```

## Canon rule

This file is an active GitHub Direction runtime file. If it conflicts with another current GitHub Direction file, return Context Request; do not invent state.

## Default context

Load the Direction Project Files default set only. Do not bulk-load `Game Documentation`, old sessions, Wave Cards, archives, or execution logs by default.

## Request-only context

*   `domain_docs/game_documentation` by topic.
*   Active Goal preserved children: `Sessions`, `Wave Cards`, `Decisions`, `Goal Brief`, `Execution Pack`.
*   Phase/Goal working context and execution logs when a stage asks for them.

## Archive boundary

`90 Archive / Historical` is archive/pointer-only and must not be default-loaded.

## Tool boundary

Concrete project setup for Gas Coop Game must be verified before Codex execution. Do not infer AGENTS.md, `.codex/config.toml`, Task Master, Serena, Basic Memory, or validators from governance notes.
