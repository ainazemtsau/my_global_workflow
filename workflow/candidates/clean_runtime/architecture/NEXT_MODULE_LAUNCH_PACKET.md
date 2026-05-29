---
artifact:
  id: CWR-NEXT-MODULE-LAUNCH-PACKET-001
  title: Clean Workflow Runtime Next Module Launch Packet
  type: module_launch_packet
  status: candidate
  owner_module: architecture_canon
  scope: module_1_runtime_kernel_launch
  version: 0.1
---

# Next Module Launch Packet

## Ready-To-Copy Launch Prompt

```text
TASK: Design Module 1 — Runtime Kernel for Clean Workflow Runtime.

STATUS:
Clean Workflow Runtime is candidate architecture only. It is not active runtime authority and does not replace the current Workflow OS.

ACCEPTED MODULE 0 BASELINE:
- Use the Module 0 candidate architecture docs as the baseline for this design chat:
  - workflow/candidates/clean_runtime/README.md
  - workflow/candidates/clean_runtime/CONCEPT_SOURCE.md
  - workflow/candidates/clean_runtime/architecture/ARCHITECTURE_CANON.md
  - workflow/candidates/clean_runtime/architecture/MODULE_MAP.md
  - workflow/candidates/clean_runtime/architecture/ROLE_TAXONOMY.md
  - workflow/candidates/clean_runtime/architecture/MODULE_CHAT_PROTOCOL.md
  - workflow/candidates/clean_runtime/architecture/OPEN_ARCHITECTURE_DECISIONS.md
- Preserve the Module 0 rule that ChatGPT, Codex, Claude Code, Deep Research, GitHub, and future agents are adapters / role implementations, not core primitives.
- Preserve one mutable state surface / one owner.
- Preserve no hidden state changes.

CANONICAL SEMANTIC PRIMITIVES:
- Accepted State
- Work Contract
- Run
- Evidence
- Acceptance Decision
- Invariant

LEGACY MAPPING:
- Ledger -> Accepted State
- Obligation -> Work Contract
- Operator -> Run
- Receipt -> Evidence / Acceptance Candidate
- Verify + Commit -> Acceptance Decision / Accepted Transition
- Invariant -> Invariant

TASK SCOPE:
Design only the Runtime Kernel: how candidate work becomes Accepted State through Work Contract, Run, Evidence, validation, Acceptance Decision, and Invariant checks.

DELIVERABLES:
1. STATE_TRANSITION_KERNEL.md draft
2. WORK_CONTRACT_MODEL.md draft
3. EVIDENCE_AND_RESULT_MODEL.md draft
4. ACCEPTANCE_DECISION_PROTOCOL.md draft
5. KERNEL_INVARIANTS.md draft
6. Unresolved kernel decisions
7. Integration risks against Module 0
8. Acceptance criteria for moving to Direction Control / Active Front

FORBIDDEN SCOPE:
- Do not design Direction Control.
- Do not design Active Front.
- Do not design Work Graph in detail.
- Do not design Memory System.
- Do not design Event System.
- Do not design Review/Patch.
- Do not design Execution Gateway.
- Do not design storage layout in detail.
- Do not mutate repo.

RETURN FORMAT:
Return a module result packet with draft summaries, unresolved decisions, integration risks, and acceptance criteria. Do not claim repository acceptance.
```

END_OF_FILE: workflow/candidates/clean_runtime/architecture/NEXT_MODULE_LAUNCH_PACKET.md
