# 02\_CURRENT\_PHASE.md

```yaml
project_file_control:
  file: 02_CURRENT_PHASE.md
  schema: project_file_projection.v1
  direction: directions/health-and-beauty
  source_files:
    - "directions/health-and-beauty/project_files/02_CURRENT_PHASE.md"
  activated_at: "2026-05-11"
  source_freshness: active_git_file
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes

```

```yaml
current_phase:
  state: active
  phase_name: MacroFactor Nutrition AI Support Setup
  phase_path: "directions/health-and-beauty/phases/macrofactor-nutrition-ai-support-setup"
  critical_constraint: "Preserve active MacroFactor work while normalizing vNext-R structure."
  minimum_outcome: "Active Phase exists, active Goal is preserved under it, root state agrees."

```

## Guard state

*   Active Goal unresolved: `yes, active Goal should be shaped/reviewed before execution`
*   Phase can close now: `no`
*   Blocker: `Goal Contract/tool binding needs verification before execution`
