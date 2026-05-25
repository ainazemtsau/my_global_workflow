---
artifact_control:
  namespace: proof_workflow
  artifact_type: migration_validation_checklist
  status: gate_1_initial
  owner: proof_carrying_workflow_os
---

# Migration Validation Checklist

## Gate 1 File Boundary

- [ ] All created files are under `proof_workflow/**` only.
- [ ] No forbidden paths changed.
- [ ] No Direction migration files created.
- [ ] No old workflow files edited.
- [ ] No old project setup files edited.

## File Integrity

- [ ] Every Markdown file has one YAML `artifact_control` header at the top.
- [ ] Every Markdown file has exactly one `END_OF_FILE:` marker.
- [ ] Every `END_OF_FILE:` marker is the last non-whitespace line.
- [ ] Every file is substantive.

## Kernel Validation

- [ ] Tier 0 primitives are limited to Ledger, Obligation, Operator, Receipt, and Invariant.
- [ ] Commit Scope is defined as runtime policy, not semantic primitive.
- [ ] Legacy terms such as `Layer`, `Sub-workflow`, `Entity`, `Stage`, `Phase`, `Goal`, `Direction Map`, and `Active Goal` are not used as semantic primitives.
- [ ] Documents, processes, compatibility layers, and roadmaps do not create truth.

## Transport Validation

- [ ] Launch Card = Operator invocation over Obligation.
- [ ] Receipt Card = Receipt.
- [ ] Context Request Card = missing blocking context.
- [ ] Human Decision Card = human-owned decision request.
- [ ] Commit Packet = commit proposal or result, not automatic truth.

## Gate 2.1 Context Authority Validation

- [ ] Context Authority Policy exists.
- [ ] Project Files are context, not accepted truth.
- [ ] Human Decision Card has decision framing guard.
- [ ] Receipt Card has context authority audit.
- [ ] Operator Launch Card separates accepted/candidate/projection/legacy context.
- [ ] Loaded domain context cannot become root objective without explicit human decision or committed receipt.

## Gate 2.2 Project Setup Persistence Validation

- [ ] Project Instructions source file exists.
- [ ] Project Files manifest exists.
- [ ] Manifest includes `proof_workflow/10_CONTEXT_AUTHORITY_POLICY.md`.
- [ ] Manifest forbids old workflow runtime/stage/project_files default loading.
- [ ] Project Instructions include Context Authority Rule.
- [ ] Project Instructions do not treat old Direction files as accepted state.
- [ ] Project setup files are not semantic primitives.
- [ ] No old project_setup files changed.

## Gate 2.3 Human Input Normalization Validation

- [ ] Human Input Normalization Policy exists.
- [ ] Human Decision Card supports terse/natural-language replies.
- [ ] Receipt Card records normalized input and defaults.
- [ ] Project Instructions include low-friction human input rule.
- [ ] `Decision B` over A/B/C/D can become a satisfied Receipt when option B is clear and defaults are explicit.
- [ ] Workflow still blocks ambiguous or high-risk silent defaults.

## Projection Validation

- [ ] Strategic Path Map = projection from accepted strategic Receipts.
- [ ] Horizon = committed orientation state view backed by accepted Receipts.
- [ ] Active Frontier = computed eligibility view over open Obligations.
- [ ] Projection claims cite accepted Receipt IDs or are marked unsupported/unresolved.

## Migration Validation

- [ ] Migration requires Legacy Import Receipts.
- [ ] Old workflow is legacy evidence only.
- [ ] Old Direction Map is not Strategic Path Map truth.
- [ ] Old Active Goal is not active Obligation.
- [ ] Old Current Phase is not Ledger state.
- [ ] Old Portfolio Queue is not obligation backlog.

## Execution Scope Validation

- [ ] Execution is placeholder/gated only.
- [ ] No product/project execution templates created.
- [ ] No Task Master, wave, or old execution workflow implementation created.

END_OF_FILE: proof_workflow/evals/MIGRATION_VALIDATION_CHECKLIST.md
