# 11 Direction Execution Log - Workflow Governance

## Entries

```yaml
execution_log_entry:
  timestamp: "2026-05-13"
  stage_or_process: "WORKFLOW_STEWARD_AUDIT"
  patch_id: WFG_PATCH_2026_05_13_GITHUB_LONG_FILE_READ_GUARD
  summary: "Approved patch plan for GitHub long-file truncation guard, Project Files runtime cache manifest, and prompt-read completeness rule."
  files_changed:
    - "workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md"
    - "workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md"
    - "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md"
    - "workflow/stage_registry/STAGE_REGISTRY.md"
    - "WORKFLOW_SOURCE_OF_TRUTH.md"
    - "directions/workflow-governance/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md"
    - "directions/workflow-governance/project_files/06_CONTEXT_LIBRARY_INDEX.md"
    - "directions/workflow-governance/evals/TRANSPORT_CONTRACT_CHECKLIST.md"
    - "directions/workflow-governance/findings/FINDING_REGISTER.md"
    - "directions/workflow-governance/findings/OPEN_FINDINGS.md"
    - "directions/workflow-governance/execution_logs/11_DIRECTION_EXECUTION_LOG.md"
  validation:
    - "Patch must be applied by repository maintenance, then verified by file read-back, diff verification, and commit verification."
    - "Project Files runtime cache must be manually refreshed after repository patch is applied."
  next_route: "Codex repository maintenance apply/read-back"
```

```yaml
execution_log_entry:
  timestamp: "2026-05-13"
  stage_or_process: "repository_maintenance_amendment"
  summary: "Added mandatory Codex reporting rule for ChatGPT Project Files cache refresh after repository maintenance."
  files_changed:
    - "workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md"
    - "workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md"
    - "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md"
    - "directions/workflow-governance/execution_logs/11_DIRECTION_EXECUTION_LOG.md"
  validation:
    - "Read-back anchors must confirm cache refresh reporting rule exists in manifest, guard, and runtime core."
    - "Codex return must include project_files_cache_refresh_required section."
  next_route: "Refresh Workflow Governance Project Files if any cached file changed."
```

```yaml
execution_log_entry:
  timestamp: "2026-05-13"
  stage_or_process: "repository_maintenance_rollout"
  patch_id: WFG_PATCH_2026_05_13_ALL_DIRECTIONS_RUNTIME_CACHE_ROLLOUT
  summary: "Rolled out Project Files runtime cache, GitHub long-file read guard, and dedicated Project Instructions model to all active Direction Projects."
  files_changed:
    - "workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md"
    - "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md"
    - "docs/CHATGPT_PROJECT_SETUP.md"
    - "directions/workflow-governance/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md"
    - "directions/workflow-governance/project_files/03_FOCUS_REGISTER.md"
    - "directions/workflow-governance/project_files/06_CONTEXT_LIBRARY_INDEX.md"
    - "directions/workflow-governance/evals/TRANSPORT_CONTRACT_CHECKLIST.md"
    - "directions/solo-max-productive/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md"
    - "directions/indie-game-development/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md"
    - "directions/health-and-beauty/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md"
    - "directions/workflow-governance/project_files/00_DIRECTION_START_HERE.md"
    - "directions/solo-max-productive/project_files/00_DIRECTION_START_HERE.md"
    - "directions/indie-game-development/project_files/00_DIRECTION_START_HERE.md"
    - "directions/health-and-beauty/project_files/00_DIRECTION_START_HERE.md"
    - "directions/solo-max-productive/project_files/06_CONTEXT_LIBRARY_INDEX.md"
    - "directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md"
    - "directions/health-and-beauty/project_files/06_CONTEXT_LIBRARY_INDEX.md"
    - "directions/workflow-governance/execution_logs/11_DIRECTION_EXECUTION_LOG.md"
  validation:
    - "Read-back anchors must confirm all active Directions have dedicated Project Instructions or updated setup references."
    - "Read-back anchors must confirm all active Direction context indexes include shared runtime cache files."
    - "Codex return must include project_files_cache_refresh_required for all affected ChatGPT Projects."
  next_route: "Refresh all active ChatGPT Project Instructions and Project Files runtime caches."
```

```yaml
execution_log_entry:
  timestamp: "2026-05-13"
  stage_or_process: "repository_maintenance_correction"
  patch_id: WFG_PATCH_2026_05_13_REMOVE_ROLLOUT_RULE_FROM_RUNTIME_CORE
  summary: "Moved the hard all-Direction rollout rule out of shared runtime core and kept it in Workflow Governance-specific governance/setup surfaces."
  files_changed:
    - "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md"
    - "directions/workflow-governance/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md"
    - "directions/workflow-governance/project_files/03_FOCUS_REGISTER.md"
    - "directions/workflow-governance/project_files/06_CONTEXT_LIBRARY_INDEX.md"
    - "directions/workflow-governance/evals/TRANSPORT_CONTRACT_CHECKLIST.md"
    - "directions/workflow-governance/execution_logs/11_DIRECTION_EXECUTION_LOG.md"
  validation:
    - "Runtime core must not contain `## 18.1 Shared Workflow All-Direction Rollout Rule`."
    - "Workflow Governance Project Instructions must contain `## Hard Cross-Direction Rollout Rule`."
  next_route: "Refresh Workflow Governance Project Instructions and affected Project Files if changed."
```

```yaml
execution_log_entry:
  timestamp: "2026-05-18"
  stage_or_process: "workflow_governance_maintenance_direct"
  patch_id: WFG_PATCH_2026_05_18_U1_USER_GUIDED_EXECUTION
  summary: "Approved shared runtime patch to add U1_USER_GUIDED_EXECUTION for step-by-step human operation of external apps, websites, local programs, ChatGPT Project UI, Unity/Blender/editor surfaces, and setup workflows without verified tool bindings."
  files_changed:
    - "workflow/stage_registry/STAGE_REGISTRY.md"
    - "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md"
    - "workflow/runtime/AD_WF_RT_001_SINGLE_RUNTIME_AUTHORITY_MODEL.md"
    - "workflow/stage_prompts/E1_EXECUTION_BRIEF.md"
    - "workflow/stage_prompts/F0_FAST_DIRECT.md"
    - "workflow/stage_prompts/U1_USER_GUIDED_EXECUTION.md"
    - "workflow/transport/USER_GUIDED_STEP_CARD.md"
    - "docs/CHATGPT_PROJECT_SETUP.md"
    - "directions/workflow-governance/execution_logs/11_DIRECTION_EXECUTION_LOG.md"
  validation:
    - "Read-back anchors must confirm U1 is listed in canonical stage IDs and runtime registry."
    - "Read-back anchors must confirm E1 and F0 can route to U1 according to registry."
    - "Read-back anchors must confirm U1 prompt contains AD-WF-RT-001 boundary and EOF marker."
    - "Read-back anchors must confirm USER_GUIDED_STEP_CARD.md exists with schema user_guided_step_card.v1."
    - "Runtime static checks must pass or return exact failures."
    - "Project Files runtime cache must be manually refreshed after shared runtime files are changed."
  next_route: "Codex repository maintenance apply/read-back"
```

## Entry shape

```yaml
execution_log_entry:
  timestamp:
  stage_or_process:
  summary:
  files_changed:
  validation:
  next_route:
```
