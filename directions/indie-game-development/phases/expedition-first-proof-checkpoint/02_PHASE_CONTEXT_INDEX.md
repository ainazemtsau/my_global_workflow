# 02 Phase Context Index

## Load rules

```
phase_context_loading:
  default_when_triggered:
    - "00 Phase Brief"
  request_only:
    - "01 Phase Working Context"
    - "04 Phase Execution Log"
    - "05 Phase Review"
    - "Game Documentation / Expedition Skeleton Document"
    - "Game Documentation / Expedition Proof Handoff"
    - "Game Documentation / Expedition Experience Model"
    - "Game Documentation / Technical Foundation - Gas and Grid Contract"
  pointer_only:
    - "Active Goal child history: Sessions, Wave Cards, Decisions, Goal Brief, Execution Pack"
  archive:
    - "archived/historical material"

```

## Stop rules

Stop and request context if Game Documentation is missing, GitHub project files conflict with each other, active Goal state is unclear, or Codex execution requires unverified project/tool bindings.
