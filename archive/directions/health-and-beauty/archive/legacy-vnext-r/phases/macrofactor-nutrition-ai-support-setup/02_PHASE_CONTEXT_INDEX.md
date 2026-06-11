# 02 Phase Context Index

```
phase_context_loading:
  default_when_triggered:
    - "00 Phase Brief"
  request_only:
    - "01 Phase Working Context"
    - "04 Phase Execution Log"
    - "05 Phase Review"
    - "Health Domain Documentation"
    - "Legacy Direction Docs - review before canonizing"
  pointer_only:
    - "Active Goal child history: Sessions, Wave Cards, Goal Brief, Execution Pack"
  archive:
    - "archived/historical material"

```

Stop before execution if project/tool bindings, active Goal acceptance, or domain documentation freshness is unclear.
