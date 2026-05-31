# Workflow v3 Direction Namespace

Status: active_namespace_marker

`directions_v3/**` is the clean-start Workflow v3 Direction namespace.

Future adopted Directions use:

```text
directions_v3/<direction-id>/runtime/**
```

No Direction is adopted by this correction package.

No `directions_v3/<direction-id>/runtime/**` root is created by this correction package.

Future clean-start adoption packages must use `workflow_v3/adoption/**`, `workflow_v3/runbooks/DIRECTION_BOOTSTRAP_RUNBOOK.md`, and `workflow_v3/evals/DIRECTION_RUNTIME_BOOTSTRAP_EVAL.md` before creating any runtime root.

`directions/**` remains `legacy_evidence` for Workflow v3 and may be used only through explicit bridge, import, or adoption policy.

END_OF_FILE: directions_v3/README.md
