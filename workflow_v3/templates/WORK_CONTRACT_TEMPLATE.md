# Work Contract Template

status: template

## Core Work Contract

work_contract_id:
target:
parent_graph_node_ref:
parent_front_ref:
parent_work_graph_node_ref:
relation_to_parent:
source_authority:
in_scope:
out_of_scope:
allowed_surfaces:
forbidden_surfaces:
expected_result:
evidence_required:
validation_required:
return_destination:
stop_conditions:

## Optional metadata

procedure_ref:
formation_eval_ref:
related_direction:
related_front:
related_work_graph_node:
adapter_or_human_surface:
context_supplied:
repository_path_boundaries_if_applicable:
finish_packet_required:
limitations:

## Boundary

One Work Contract has one bounded target.

If the target contains multiple independent jobs, return `split_required` instead of widening the contract.

Work Contract carries no route authority, product-meaning authority, scope-expansion authority, or acceptance authority.

Adapter output under this contract remains candidate until verified and accepted.

Repository path boundaries are required only when repository/file mutation or inspection makes paths material.

END_OF_FILE: workflow_v3/templates/WORK_CONTRACT_TEMPLATE.md
