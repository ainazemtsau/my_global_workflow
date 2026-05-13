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
