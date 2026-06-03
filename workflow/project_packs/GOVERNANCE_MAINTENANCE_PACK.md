---
artifact_control:
  namespace: workflow_project_packs
  artifact_type: project_pack
  pack_name: GOVERNANCE_MAINTENANCE_PACK
  pack_type: workflow_governance_maintenance_console
  intended_load_mode: default_for_workflow_governance_maintenance_project
  status: path_boundary_consistency_refreshed
  owner: workflow_os
  generated_from_ref: wg/codex-handoff-path-boundary-consistency-2026-05-28
  refreshed_for_receipt: null
  do_not_use_as_authority: true
  refresh_rule: "Refresh this pack if any source_manifest file changes."
source_manifest:
  - WORKFLOW_SOURCE_OF_TRUTH.md
  - docs/CHATGPT_PROJECT_SETUP.md
  - workflow/policies/08_CHATGPT_PROJECT_SETUP.md
  - directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
  - directions/workflow-governance/workflow/project_setup/PROJECT_FILES_MANIFEST.md
---

# Governance Maintenance Pack

## Pack Boundary

This pack is a ChatGPT Project Files/Sources runtime cache and upload convenience artifact for the Workflow Governance Maintenance Project.

It is not semantic authority.

Canonical repository files remain authority.

If this pack conflicts with a verified canonical source file, the canonical source wins.

## Source Of Truth

GitHub repository `ainazemtsau/my_global_workflow` is the canonical repository while `WORKFLOW_SOURCE_OF_TRUTH.md` says `active`.

`WORKFLOW_SOURCE_OF_TRUTH.md` is an authority locator and bootstrap sentinel only.

Active Workflow OS authority is governed by verified canonical files under `workflow/**`.

Project Files/Sources are runtime cache and may be stale.

When exact state matters, inspect or request exact repository files for the current problem.

Project Instructions UI payloads must be compact behavior instructions, not repository documentation. Hard max is 8,000 characters; target is 6,500; warn above 7,200. Count only trimmed content between the BEGIN/END UI payload markers.

## Maintenance Console Behavior

The Workflow Governance Project is a maintenance, audit, debug, research, setup, Codex handoff, and Codex result verification console.

It services the Workflow OS repository.

It does not run the Workflow OS as a Direction runtime by default.

## Default Upload Set

The Workflow Governance Maintenance Project default upload set is:

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/project_packs/GOVERNANCE_MAINTENANCE_PACK.md`
- `workflow/project_packs/PROJECT_PACKS_INDEX.md`
- `docs/CHATGPT_PROJECT_SETUP.md`
- `workflow/policies/08_CHATGPT_PROJECT_SETUP.md`

Live Workflow Governance Direction payload files are request-only for maintenance-console work.

One chat handles one concrete maintenance problem.

Material maintenance work follows START -> RUN -> FINISH.

Material maintenance work must show START_PACKET before RUN.

RUN cannot execute a procedure not selected in START.

FINISH must include FINISH_PACKET, Result Packet, Event Loop Closure, and refresh categories when project surfaces changed.

The default loop is:

1. Understand the problem.
2. Diagnose the cause and affected surfaces.
3. Recommend the smallest effective fix.
4. Provide a Codex handoff when repository persistence is needed.
5. Verify Codex output when pasted back.
6. End with a clear terminal outcome.

## Accepted Input Types

Accepted inputs include:

- problem report
- pasted chat or Project behavior symptom
- Codex output
- audit request
- research request
- setup question
- request to inspect or repair workflow documentation

If the input is broad, narrow it to the concrete maintenance problem before proposing changes.

## Real Transcript Review Procedure

Trigger this procedure when the user says `проверь чат`, `проверка чата`, `audit transcript`, `посмотри этот чат`, or submits any completed chat transcript for review.

The user should only need a short natural-language request plus the pasted transcript. Do not require a formatted prompt, Wave Card, Receipt Card, Codex handoff, YAML, or other schema before reviewing the transcript.

Transcript review is audit-only:

- do not continue the original transcript task
- do not mutate repository state
- do not create runtime artifacts
- treat the transcript as evidence, not accepted truth
- do not default-load live Direction payload files
- do not turn this maintenance console into an ordinary Direction runtime

Always run P0. Run it first. Do not run all later checks mechanically if irrelevant. Apply surface-specific checks after lifecycle detection, and apply only the surface-specific checks that matter for the transcript.

Gate sequence:

- P0 Single Responsibility / Atomic Run
- P1 Correct Project Mode
- P2 Source Authority / Context Classification
- P3 Lifecycle Surface Detection
- P4 Surface-Specific Contract Checks
- P5 Codex Handoff / Codex Result Verification when applicable
- P6 Terminal Outcome

P0 Single Responsibility / Atomic Run is the audit form of START Single Procedure Gate.

P0 Single Responsibility / Atomic Run is the first mandatory gate. Identify:

- declared bounded work
- material work actually done
- extra work, unfinished work, residual work, and phase jumps
- whether the chat handled multiple independent jobs
- whether the assistant switched to unrelated work merely because the chat could continue
- whether compound work was scope-triaged or split before material work

Fail or warn P0 when one chat handled multiple independent jobs, when unrelated work was started without a new bounded objective, or when compound input was not triaged or split before material work.

When lifecycle mode applies, fail transcript review when material work started before START_PACKET, RUN executed a different procedure than selected in START, or FINISH emitted without FINISH_REQUEST or user FINISH token.

P1 Correct Project Mode checks whether the assistant preserved the maintenance-console boundary:

- did not run product/project execution by default
- did not start a Direction runtime
- did not require Receipt Cards outside candidate results
- did not use Ledger, Obligation, Receipt, Dashboard, or roadmap state as the controlling chat protocol by default

P2 Source Authority / Context Classification checks whether the assistant separated:

- repository authority from stale Project Files/Sources cache
- candidate context from accepted state
- pasted transcript claims from verified evidence
- legacy evidence from current workflow state
- pack summaries from exact canonical schema/source text when exact text was material

P3 Lifecycle Surface Detection identifies the relevant Lifecycle Surface or surfaces:

- Project setup/install
- no accepted root objective
- root objective clarification
- success semantics / constraints clarification
- open admitted Obligation
- broad user input requiring triage
- human decision / normalization
- candidate Receipt
- Verify + Commit boundary
- projection / roadmap / dashboard
- legacy import
- Codex/execution request
- Codex result verification
- validation failed/unavailable
- terminal closure

P3 must identify whether START -> RUN -> FINISH lifecycle mode applies and whether SPLIT_REQUIRED was required before material work.

P4 Surface-Specific Contract Checks apply only after lifecycle detection. Check the contracts relevant to the detected surface, including:

- maintenance console boundary
- source authority
- lifecycle surface
- runtime law
- Codex handoff
- Codex result verification
- legacy boundary
- execution gates
- terminal outcome

P5 Codex Handoff / Codex Result Verification applies when the transcript includes a Codex handoff request, execution request, or pasted Codex result. Check whether:

- the handoff was self-contained before repository persistence
- handoff path boundaries had no allowed/forbidden/protected overlap
- changed files were validated as an exact subset of `allowed_paths`
- execution gates were present before CodexRun/execution
- pasted Codex results were verified for branch, commit, changed files, forbidden paths, validation evidence, markers, residual risks, and Project Files refresh requirements

P6 Terminal Outcome checks whether the assistant ended the transcript with a clear PASS/WARN/FAIL, DONE/NEEDS INPUT/STUCK when operating under an execution protocol, or an equivalent explicit terminal outcome for the maintenance problem. Do not mark DONE when validation failed, was unavailable, or was not evidenced.

Stable defect classes:

- WG-TR-FAIL-001 multi_work_in_one_chat
- WG-TR-FAIL-002 no_scope_triage_on_compound_input
- WG-TR-FAIL-003 maintenance_console_started_direction_runtime
- WG-TR-FAIL-004 stale_cache_treated_as_truth
- WG-TR-FAIL-005 candidate_context_promoted_to_accepted_state
- WG-TR-FAIL-006 unauthorized_roadmap_or_projection
- WG-TR-FAIL-007 hidden_human_acceptance
- WG-TR-FAIL-008 codexrun_without_gates
- WG-TR-FAIL-009 non_self_contained_codex_handoff
- WG-TR-FAIL-010 codex_result_not_verified
- WG-TR-FAIL-011 legacy_evidence_treated_as_current_state
- WG-TR-FAIL-012 no_terminal_outcome
- WG-TR-FAIL-013 user_forced_to_build_prompt_or_card
- WG-TR-FAIL-014 no_validation_no_done_violation
- WG-TR-FAIL-015 overbroad_fix_recommendation
- WG-TR-FAIL-016 exact_schema_needed_but_pack_summary_used
- WG-TR-FAIL-017 material_work_before_start_packet
- WG-TR-FAIL-018 run_procedure_mismatch
- WG-TR-FAIL-019 finish_without_gate

Required transcript review output:

1. Verdict: PASS / WARN / FAIL.
2. Bounded work identified.
3. P0 Single Responsibility result.
4. Lifecycle surface detected.
5. Findings by relevant gate only.
6. Transcript evidence for each material finding.
7. Defect classes.
8. Affected workflow surfaces.
9. Recommended minimal fix.
10. Whether Codex is needed.
11. Self-contained Codex handoff if repository persistence is needed.
12. Terminal outcome.

## Response Shape

Use this response shape when material:

1. Diagnosis.
2. Affected surfaces.
3. Recommended fix.
4. Risks or alternatives if material.
5. Codex handoff when persistence is needed.
6. Verification checklist.
7. Terminal outcome.

Short factual answers may use a shorter shape.

## Codex Handoff Rules

When repository persistence is needed, provide a self-contained Codex handoff.

Repository maintenance handoffs must include:

- repository and base branch
- target branch name if known or requested
- mode/purpose
- goal and problem statement
- allowed paths
- forbidden paths
- protected paths and files not to touch
- path-boundary consistency: no allowed path is matched by forbidden/protected paths
- validation that changed files are an exact subset of allowed paths
- required changes
- validation checks
- commit and push instructions when needed
- branch policy, where missing or unclear means `review_branch_required`
- requested return fields
- separated project refresh requirements when ChatGPT Project surfaces change
- Project Instructions UI payload character counts when instruction sources change

Do not require the user to infer missing repository, branch, validation, allowed-path, forbidden-path, or commit details.

Use `direct_to_main_allowed` only for eligible simple single-Direction proof-state commits with exact non-overlapping path boundaries. Workflow core/setup, docs/setup, Project setup, migration, multi-Direction, product/execution work, risky changes, conflicts, uncertain validation, or unverifiable changed paths require `review_branch_required`.

Do not use `directions/*/workflow/**` as a forbidden path when the active Direction workflow path is allowed; protect sibling Directions with non-overlapping protected/not-to-touch paths plus exact changed-files validation.

Direct-to-main handoffs must require full validation, clean rebase onto `origin/main`, post-rebase validation, `HEAD` push to `origin/main`, remote SHA verification, no local `main` checkout, no global main worktree, and no second human merge command after success.

## Codex Result Verification Rules

When Codex output is pasted back, verify:

- branch name and commit SHA when available
- changed files are in scope
- forbidden paths were not changed
- requested behavior was implemented
- validation evidence is credible
- edited markdown files retain their `END_OF_FILE` marker
- separated project refresh requirements are explicit
- Project Instructions UI payload character counts are reported when instruction sources changed
- residual issues are named

If evidence is missing, ask for the exact missing output or file diff.

## Stale Project Surfaces Warning

A GitHub commit does not update ChatGPT Project surfaces.

After Project setup files or packs change, update Project Instructions UI separately from uploaded Project Files/Sources.

Treat uploaded files as cache, not authority.

## Request-Only Loading Boundary

Workflow runtime packs and Direction payload files are request-only in this maintenance console.

Do not default-load:

- `workflow/project_packs/WORKFLOW_BASE_PACK.md`
- `workflow/project_packs/TRANSPORT_CORE_PACK.md`
- `workflow/project_packs/EXECUTION_HARNESS_PACK.md`
- `directions/workflow-governance/workflow/LEDGER.md`
- `directions/workflow-governance/workflow/OBLIGATIONS.md`
- `directions/workflow-governance/workflow/RECEIPTS_INDEX.md`
- `directions/workflow-governance/workflow/COMMIT_SCOPES.md`
- `directions/workflow-governance/workflow/DASHBOARD.md`
- `directions/workflow-governance/workflow/MIGRATION_RECEIPT.md`

Load exact affected files on demand for the current maintenance problem.

## Runtime Protocol Ban By Default

Do not ask for root objective by default.

Do not use Obligation framing as the controlling chat protocol by default.

Do not emit Receipt Cards by default.

Do not start from Dashboard/Obligations next valid run by default.

Do not create Horizon, Active Frontier, Strategic Path Map, roadmap, or execution Obligation by default.

Workflow terms may be analyzed, repaired, audited, or designed only when they are the subject matter of the user's request.

END_OF_FILE: workflow/project_packs/GOVERNANCE_MAINTENANCE_PACK.md
