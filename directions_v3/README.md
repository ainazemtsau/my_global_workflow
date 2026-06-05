# Workflow v3 Direction Namespace

Status: active_namespace_marker

`directions_v3/**` is the clean-start Workflow v3 Direction namespace.

Future adopted Directions use:

```text
directions_v3/<direction-id>/runtime/**
```

No Direction is adopted by this correction package.

No `directions_v3/<direction-id>/runtime/**` root is created by this correction package.

No concrete `directions_v3/<direction-id>/runtime/**` root exists after this cleanup unless a future accepted package creates one.

Future clean-start adoption and setup packages must use canonical Workflow v3 sources such as:

- `workflow_v3/adoption/**`;
- `workflow_v3/project_setup/DIRECTION_ROOT_BOOTSTRAP_LAUNCH_PACKET_TEMPLATE.md`;
- `workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md`;
- `workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md`;
- `workflow_v3/evals/DIRECTION_RUNTIME_BOOTSTRAP_EVAL.md`.

`directions/**` remains `legacy_evidence` for Workflow v3 and may be used only through explicit bridge, import, or adoption policy.

END_OF_FILE: directions_v3/README.md
