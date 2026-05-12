# 06_CONTEXT_LIBRARY_INDEX.md

```yaml
project_file_projection: 1
schema: direction_project_file_projection.v1
source_file: "directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md"
canonical_source: GitHub repository file
projection_status: fresh
activated_at: "2026-05-12"
```

## Canon rule

This file is an active GitHub Direction runtime file. If it conflicts with another current GitHub Direction file, return Context Request; do not invent state.

## Default context

Load the Direction Project Files default set only. Do not bulk-load `Game Documentation`, old sessions, Wave Cards, archives, or execution logs by default.

## Shared runtime and stage prompts

```yaml
shared_runtime_file: "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md"
stage_prompt_source_root: "workflow/stage_prompts/"
stage_prompt_load_rule: "request exact stage prompt by stage ID; do not bulk-load all prompts"
local_runtime_core_copy_required: false
```

Stage prompts are request-only runtime inputs. Do not copy stage prompt files into Direction Project Files.

## Request-only context

### Active domain documentation

* `directions/indie-game-development/domain_docs/game_documentation/game-documentation.md`
* `directions/indie-game-development/domain_docs/game_documentation/game-foundation.md`
* `directions/indie-game-development/domain_docs/game_documentation/technical-foundation-gas-and-grid-contract.md`
* `directions/indie-game-development/domain_docs/game_documentation/clean-start-transfer-boundary.md`
* `directions/indie-game-development/domain_docs/game_documentation/foundation-docs-index.md`
* `directions/indie-game-development/domain_docs/game_documentation/documentation-index.md`
* `directions/indie-game-development/domain_docs/game_documentation/expedition-proof-handoff.md`
* `directions/indie-game-development/domain_docs/game_documentation/primary-product-bet-expedition.md`
* `directions/indie-game-development/domain_docs/game_documentation/expedition-experience-model.md`
* `directions/indie-game-development/domain_docs/game_documentation/expedition-skeleton-document.md`

### Accepted Goal artifacts

* `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md`
  * Status: `accepted_by_R1`
  * Use when shaping the next proof-related Goal.
  * Do not treat as a prototype design, implementation plan, Game Documentation promotion, or Codex execution brief.

### Preserved Goal context

* Active Goal preserved children: `Sessions`, `Wave Cards`, `Decisions`, `Goal Brief`, `Execution Pack`.
* Phase/Goal working context and execution logs when a stage asks for them.

## Archive boundary

Archived or historical material is pointer-only and must not be default-loaded.

## Tool boundary

Concrete project setup for Gas Coop Game must be verified before Codex product/project execution. Do not infer AGENTS.md, `.codex/config.toml`, Task Master, Serena, Basic Memory, or validators from governance notes.

## Game Documentation promotion boundary

The accepted minimum proof-core artifact may become a candidate input for future Game Documentation maintenance, but it is not promoted automatically.

A future documentation stage must load the exact target Game Documentation files before writing domain docs.
