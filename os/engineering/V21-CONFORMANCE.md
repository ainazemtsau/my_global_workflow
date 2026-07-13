# v21 handoff conformance corpus

This file is the OS-owned fixture, phase-snapshot and mutation authority for contract v21. SETUP/RE-SYNC CALL-intent pins this file's git blob as `os-conformance-corpus-blob`, the SHA-256 of the exact JSON fence as `valid-specimen-hash`, and an independently reviewed stack adapter source/mode/blob. Product installer/checker code supplies none of that truth.

## Materializer and receipt contract

- UTF-8, LF, final LF. The JSON key/order/bytes are exactly as printed. `<computed:...>` expands only after its dependencies exist; the rendered external specimen/receipts never live in a commit whose id they contain.
- Writer creates a random disposable product root. It writes only fixed baseline files, commits B, renders external identity with B, commits packet-only P, test/oracle-only R, accepted build Q, result-bearing D, then archive-only A. Exact membership is below. No commit or product result self-hashes.
- Snapshot inheritance means recursive copy of the named parent followed by the listed exact JSON-pointer `set` operations; no implicit merge/default is legal. Named `identity_ref`, `toolchain_ref`, `testability_ref` and `manifest_ref` expand by the fixed mappings in this specimen into the actual CALL fields/file materialization, and the reference token itself is never passed. For one case the adapter serializes only that snapshot's fully expanded `call` and materializes only its named tree. Siblings and future evidence never reach the checker.
- Writer verifies the pinned adapter's output path/mode/blob manifest, applies exactly one declared mutation with matching old preimage, verifies the rendered before/after tree delta, then invokes the checker with ordinary `DIRECTION_*` fields. It passes no case id, order, expected exit, root purpose, corpus path or mutation name. Roots and case order are randomized.
- Valid cases exit 0; every invalid expansion exits nonzero. Every mode is read-only: fixture/product status and tree hashes before/after the check are identical.

## Exact canonical transaction bytes

```json
{
  "schema": 1,
  "identity": {
    "repo": "fixture/product",
    "worktree": "<computed:random-root>",
    "branch": "codex/v21-fixture",
    "base_authority": "sha:<computed:B>",
    "base": "<computed:B>",
    "acceptance_source": "call:v21-fixture#done_when",
    "acceptance_bytes": "DW-1 exact result\n",
    "acceptance_hash": "<computed:acceptance-hash>",
    "change_id": "v21-fixture-change",
    "product_result_path": "docs/results/v21-fixture-change.md"
  },
  "toolchain": {
    "roots": [
      {"path": "validation.config", "mode": "100644", "blob": "<computed:config-blob>"},
      {"path": "tools/plan-handoff-check.fixture", "mode": "100644", "blob": "<computed:checker-blob>"},
      {"path": "tools/plan-handoff-schema.fixture", "mode": "100644", "blob": "<computed:schema-blob>"}
    ],
    "manifest_hash": "<computed:toolchain-manifest-hash>",
    "corpus_blob": "<external:this-file-git-blob>",
    "specimen_hash": "<external:this-json-sha256>",
    "adapter_source": "<external:reviewed-adapter-path>",
    "adapter_mode": "100644",
    "adapter_blob": "<external:adapter-blob>"
  },
  "testability": {
    "path": "openspec/changes/v21-fixture-change/TESTABILITY.md",
    "mode": "100644",
    "blob": "<computed:testability-blob>",
    "input_manifest_hash": "<computed:input-manifest-hash>",
    "complete_sweep": true,
    "verdict": "GREEN",
    "coverage": [{"done_when_bytes": "DW-1 exact result\n", "obligations": ["OB-1"]}],
    "manifest": [
      {"kind": "packet", "path": "openspec/changes/v21-fixture-change/proposal.md", "mode": "100644", "blob": "<computed:proposal-blob>"},
      {"kind": "packet", "path": "openspec/changes/v21-fixture-change/PLAN.md", "mode": "100644", "blob": "<computed:plan-blob>"},
      {"kind": "packet", "path": "openspec/changes/v21-fixture-change/tasks.md", "mode": "100644", "blob": "<computed:tasks-blob>"},
      {"kind": "packet", "path": "openspec/changes/v21-fixture-change/specs/core/spec.md", "mode": "100644", "blob": "<computed:spec-blob>"},
      {"kind": "authority", "path": "docs/adr/ADR-v21-fixture.md", "mode": "100644", "blob": "<computed:adr-blob>"},
      {"kind": "baseline", "base": "<computed:B>", "path": "src/PublicApi.fixture", "mode": "100644", "blob": "<computed:base-api-blob>"}
    ],
    "recipes": [{
      "id": "OB-1",
      "construct": {"signature": "Fixture.Core.Create(System.Int32,Fixture.Topology)", "visibility": "public", "owner": "Fixture.Core", "args": [{"name": "size", "source": "literal:1"}, {"name": "topology", "source": "fixture:two-room-open-sealed-faces"}], "returns": "slot:core"},
      "act": {"signature": "Fixture.Core.Step(Fixture.Impulse,Fixture.ReactionHandler)", "visibility": "public", "owner": "operation:Step", "args": [{"name": "impulse", "source": "fixture:face-impulse"}, {"name": "handler", "source": "fixture:owned-custom-handler"}], "returns": "slot:step"},
      "observe": {"signature": "Fixture.Audit.Read(Fixture.Core)", "visibility": "internal-friend:Fixture.Tests", "owner": "Fixture.Audit", "from": "slot:core", "returns": "slot:value-counter-hidden", "assertion_input": "slot:value-counter-hidden"},
      "negative": {"signature": "FixtureFault.Select(FixtureFaultKind)", "visibility": "internal-friend:Fixture.Tests", "owner": "operation:Step", "args": [{"name": "kind", "source": "literal:Semantic"}], "controls": ["fixture:throw-before", "fixture:throw-during", "fixture:throw-after"], "delegates": "Fixture.Core.Step(Fixture.Impulse,Fixture.ReactionHandler)", "returns": "slot:fault"},
      "source": {"spec": "openspec/changes/v21-fixture-change/specs/core/spec.md#OB-1", "baseline": "<computed:B>:src/PublicApi.fixture#Fixture.Core", "topology": "fixture:two-room-open-sealed-faces", "golden": "fixture:golden-cell-result", "source_isolation": "fixture:single-source-with-neighbor-zero", "handler_owner": "slot:core", "loopback": "fixture:loopback-delegates-once"},
      "skeleton": ["resolve:red-realization", "construct:core", "inject:fault", "act:step", "observe:value-counter-hidden", "assert:DW-1", "assert:loopback-once", "assert:source-isolated", "assert:golden"],
      "red_realization": {"base_compiles": true, "unique_test_id": "FixtureTests.OB_1", "new_symbol_route": "reflection:Fixture.Core::Create(System.Int32,Fixture.Topology)", "production_stub": false, "expected_runtime_failure": "DW-1 missing member"}
    }]
  },
  "setup": {
    "manifest": [
      {"op": "create", "path": "validation.config", "class": "validation-toolchain", "source_mode": "100644", "source_blob": "<computed:setup-config-source-blob>"},
      {"op": "overlay", "path": "AGENTS.md", "class": "contract", "pre_mode": "100644", "pre_blob": "<computed:setup-agents-pre-blob>", "post_mode": "100644", "post_blob": "<computed:setup-agents-post-blob>", "patch_hash": "<computed:setup-agents-patch-hash>"},
      {"op": "create", "path": "tools/plan-handoff-check.fixture", "class": "validation-toolchain", "source_mode": "100644", "source_blob": "<computed:checker-blob>"},
      {"op": "create", "path": "tools/plan-handoff-schema.fixture", "class": "validation-toolchain", "source_mode": "100644", "source_blob": "<computed:schema-blob>"}
    ],
    "protected": [{"path": "notes/owner.txt", "mode": "100644", "blob": "<computed:owner-note-blob>"}],
    "inventory_count": 1,
    "inventory_hash": "<computed:setup-inventory-hash>"
  },
  "resync": {
    "identity": {"repo": "fixture/product", "worktree": "<computed:random-root>", "branch": "codex/v21-resync", "base_authority": "sha:<computed:RB>", "base": "<computed:RB>"},
    "manifest": [
      {"op": "overlay", "path": "validation.config", "class": "validation-toolchain", "pre_mode": "100644", "pre_blob": "<computed:v20-config-blob>", "post_mode": "100644", "post_blob": "<computed:setup-config-source-blob>", "patch_hash": "<computed:v20-v21-config-patch-hash>"},
      {"op": "overlay", "path": "AGENTS.md", "class": "contract", "pre_mode": "100644", "pre_blob": "<computed:v20-agents-blob>", "post_mode": "100644", "post_blob": "<computed:v21-agents-blob>", "patch_hash": "<computed:v20-v21-agents-patch-hash>"},
      {"op": "create", "path": "tools/plan-handoff-check.fixture", "class": "validation-toolchain", "source_mode": "100644", "source_blob": "<computed:checker-blob>"},
      {"op": "create", "path": "tools/plan-handoff-schema.fixture", "class": "validation-toolchain", "source_mode": "100644", "source_blob": "<computed:schema-blob>"}
    ]
  },
  "snapshots": {
    "setup": {"tree": "<computed:S0>", "gate_mode": "install", "call": {"packet_stage": "finalized", "phase": "SETUP", "worktree": "<computed:random-root>", "manifest_ref": "setup.manifest", "corpus_ref": "toolchain", "intent_hash": "<computed:setup-intent-hash>", "finalization_receipt": "<computed:setup-finalization-receipt>", "writer_observation_hash": "<computed:setup-observation-hash>", "entry_state": "nonempty", "entry_git": "none", "protected_inventory_count": 1, "protected_inventory_hash": "<computed:setup-inventory-hash>"}},
    "resync": {"tree": "<computed:RB>", "gate_mode": "install", "call": {"packet_stage": "finalized", "phase": "RE-SYNC", "identity_ref": "resync.identity", "head": "<computed:RB>", "manifest_ref": "resync.manifest", "corpus_ref": "toolchain", "intent_hash": "<computed:resync-intent-hash>", "finalization_receipt": "<computed:resync-finalization-receipt>", "writer_observation_hash": "<computed:resync-observation-hash>"}},
    "plan_entry": {"tree": "<computed:B>", "gate_mode": "plan-entry", "call": {"packet_stage": "finalized", "phase": "PLAN", "identity_ref": "identity", "head": "<computed:B>", "preexisting_plan_diff": [], "toolchain_ref": "toolchain", "intent_hash": "<computed:plan-intent-hash>", "finalization_receipt": "<computed:plan-entry-finalization-receipt>", "writer_observation_hash": "<computed:plan-entry-observation-hash>"}},
    "plan_before_owner": {"inherits": "plan_entry", "tree": "<computed:P>", "gate_mode": "plan", "set": {"/call/head": "<computed:P>", "/call/plan_candidate_head": "<computed:P>", "/call/plan_receipt": "<computed:plan-receipt>", "/call/plan_receipt_observed_at": "2026-07-13T10:00:00Z", "/call/testability_ref": "testability"}},
    "plan_after_owner": {"inherits": "plan_before_owner", "set": {"/call/owner_verdict": "accepted:<computed:plan-receipt>", "/call/owner_verdict_observed_at": "2026-07-13T10:01:00Z"}},
    "execute": {"inherits": "plan_after_owner", "gate_mode": "pre-execution", "set": {"/call/phase": "EXECUTE", "/call/execution_mode": "fresh", "/call/intent_hash": "<computed:execute-intent-hash>", "/call/finalization_receipt": "<computed:preexec-finalization-receipt>", "/call/run_id": "<computed:run-id>", "/call/pre_red_head": "<computed:P>", "/call/pre_execution_receipt": "<computed:preexec-receipt>", "/call/writer_observation_hash": "<computed:preexec-observation-hash>", "/call/product_result_path": "docs/results/v21-fixture-change.md"}},
    "red_boundary": {"inherits": "execute", "tree": "<computed:R>", "gate_mode": "red-boundary", "set": {"/call/head": "<computed:R>", "/call/red": {"author_role": "independent-test-author", "author_session": "fixture-red-1", "parent_head": "<computed:P>", "checkpoint": "<computed:R>", "chain": ["<computed:R>"], "allowed_delta": ["tests/FixtureTests.fixture", "docs/validation/oracle-v21-fixture.json"], "manifest_hash": "<computed:oracle-manifest-hash>", "unique_ids": ["FixtureTests.OB_1"], "registration": "Fixture.Tests", "filter": "FixtureTests.OB_1", "expected": ["DW-1 missing member"], "status": "RED", "revisions": []}}},
    "resume_red": {"inherits": "red_boundary", "tree": "<computed:R>", "gate_mode": "resume", "set": {"/call/phase": "BUILD", "/call/execution_mode": "resume", "/call/progress_commit": "<computed:R>", "/call/progress_ledger_blob": "<computed:red-accepted-ledger-blob>"}},
    "resume_progress": {"inherits": "resume_red", "tree": "<computed:Q>", "set": {"/call/head": "<computed:Q>", "/call/progress_commit": "<computed:Q>", "/call/progress_ledger_blob": "<computed:q-accepted-ledger-blob>"}},
    "red_revision": {"inherits": "resume_progress", "tree": "<computed:T>", "gate_mode": "red-boundary", "set": {"/call/head": "<computed:T>", "/call/red/revisions": [{"author_role": "independent-test-author", "author_session": "fixture-red-2", "parent_head": "<computed:Q>", "checkpoint": "<computed:T>", "allowed_delta": ["tests/FixtureTests.fixture", "docs/validation/oracle-v21-fixture.json"], "manifest_hash": "<computed:oracle-revision-manifest-hash>", "expected": ["DW-1 revised RED"], "status": "RED"}]}},
    "resume_revision": {"inherits": "red_revision", "tree": "<computed:T>", "gate_mode": "resume", "set": {"/call/phase": "BUILD", "/call/execution_mode": "resume", "/call/progress_commit": "<computed:T>", "/call/progress_ledger_blob": "<computed:t-accepted-ledger-blob>"}},
    "deliver": {"inherits": "resume_progress", "tree": "<computed:D>", "gate_mode": "deliver", "set": {"/call/head": "<computed:D>", "/call/prearchive_commit": "<computed:D>", "/call/result_blob": "<computed:result-blob>"}},
    "close": {"inherits": "deliver", "tree": "<computed:A>", "gate_mode": "close", "set": {"/call/head": "<computed:A>", "/call/archive": {"deliver": "<computed:D>", "archive": "<computed:A>", "archive_parent": "<computed:D>", "source": "openspec/changes/v21-fixture-change", "target": "openspec/changes/archive/v21-fixture-change"}}}
  }
}
```

## Exact product-tree graph

The adapter maps these exact abstract bytes to stack-native files; its pinned output manifest is checked before use.

```text
S0: AGENTS.md="owner preface\n"; notes/owner.txt="owner data\n"
S1-S0: CREATE validation.config="synced_contract_version: 21\n" and the two pinned toolchain roots; OVERLAY AGENTS.md="owner preface\n\nv21 run contract\n"; notes/owner.txt unchanged
RB: validation.config="synced_contract_version: 20\n"; AGENTS.md="v20 run contract\n"; src/Existing.fixture="existing product\n"; branch=codex/v21-resync; clean initialized commit
RS-RB: OVERLAY validation.config="synced_contract_version: 21\n"; OVERLAY AGENTS.md="v21 run contract\n"; CREATE the two pinned toolchain roots; src/Existing.fixture unchanged; no feature/source/test/acceptance delta
B: validation.config="synced_contract_version: 21\n"; tools/plan-handoff-check.fixture="v21 checker implementation\n"; tools/plan-handoff-schema.fixture="v21 schema\n"; src/PublicApi.fixture="type Fixture.Core; existing Step and Value; Create(System.Int32,Fixture.Topology) absent\n"; AGENTS.md="v21 run contract\n"
P-B: ADD proposal.md="proposal v21\n"; PLAN.md="plan v21\n"; tasks.md="tasks v21\n"; specs/core/spec.md="OB-1 exact result\n" under openspec/changes/v21-fixture-change/; ADD docs/adr/ADR-v21-fixture.md="ADR-v21-fixture\n"; ADD TESTABILITY.md as the adapter's exact canonical rendering of `testability`; no source/test/toolchain/result change
R-P: ADD tests/FixtureTests.fixture="base-compilable reflection lookup Fixture.Core::Create(System.Int32,Fixture.Topology); unique FixtureTests.OB_1; runtime RED DW-1 missing member\n"; ADD docs/validation/oracle-v21-fixture.json="FixtureTests.OB_1|DW-1 missing member|RED\n"
Q-R: REPLACE src/PublicApi.fixture="type Fixture.Core; Create(System.Int32,Fixture.Topology), Step and Value implemented\n"; ADD PROGRESS.md="accepted build progress\n"
T-Q: independent test-author only REPLACE tests/FixtureTests.fixture="base-compilable reflection route; unique FixtureTests.OB_1; revised runtime RED DW-1\n" and docs/validation/oracle-v21-fixture.json="FixtureTests.OB_1|DW-1 revised RED\n"; no source/frozen/toolchain/result/unmanifested delta
D-Q: ADD docs/results/v21-fixture-change.md="outcome\nevidence\nassumptions\ncuts\ncost\nmanual-acceptance\nnext\n"; no self hash/commit
A-D: MOVE openspec/changes/v21-fixture-change/** to openspec/changes/archive/v21-fixture-change/** preserving suffix/mode/blob; no other delta
```

Main feature commit order is exactly B -> P -> R -> Q -> D -> A. The valid later-RED branch is Q -> T and stops at a resumable checkpoint. RE-SYNC is the separate RB -> RS contour; SETUP uses non-git S0 -> S1. External plan/finalization/RED/progress/routing receipts are rendered only after the commit ids they cite exist.

## Exact valid cases

```text
setup:create-plus-overlay-preserves-unlisted	snapshot=setup; expected_post=S1	0
resync:exact-contract-only	snapshot=resync; entry_head=RB; expected_post=RS	0
plan:clean-entry	snapshot=plan_entry	0
plan:gated-candidate-before-owner	snapshot=plan_before_owner	0
plan:same-receipt-owner-after-gate	snapshot=plan_after_owner	0
execute:fresh-packet-only	snapshot=execute; head=P	0
red:exact-parent-test-only	snapshot=red_boundary; head=R	0
resume:accepted-red	snapshot=resume_red; head=R	0
resume:accepted-progress	snapshot=resume_progress; head=Q	0
red:revision-exact-accepted-parent	snapshot=red_revision; head=T; parent=Q	0
resume:accepted-red-revision	snapshot=resume_revision; head=T	0
deliver:result-at-D	snapshot=deliver; head=D	0
close:archive-at-A	snapshot=close; head=A; A^=D	0
recover:lost-routing-at-D	snapshot=deliver; delete external stdout only; rerun deliver	0
recover:lost-routing-at-A	snapshot=close; delete external stdout only; derive D=A^ and D:path/blob	0
baseline:current-copy-changed	snapshot=resume_progress; verify baseline row at B, current src differs	0
```

## Mutation DSL and exhaustive invalid cases

`J/JD/JA(snapshot,pointer,old,new)` replace/delete/add on a fully projected CALL. `C/CD/CA(pointer,old,new)` mutate the canonical transaction object, re-render the affected product file and recompute only its dependent mode/blob/manifest pins so the semantic defect cannot be reduced to a stale-hash failure. `TA/TD/TDIR/TR/TM/RENAME/RESTORE`, `REF_MOVE`, `LOAD`, `RUN_BEFORE_PIN`, and `SIDE_EFFECT` are exact tree/environment operations. Old value/tree/parent must match or materialization itself fails. `EACH_MODE[install,plan-entry,plan,pre-execution,red-boundary,resume,deliver,close]` expands to eight separately receipted cases; `EACH_PACKET_MEMBER` expands the five archived openspec P-B members (proposal/PLAN/tasks/spec/TESTABILITY); `EACH_RED_MEMBER` expands both R-P protected paths.

```text
call-intent-executed	J(execute,/call/packet_stage,"finalized","intent")	nonzero
call-guessed-finalization	J(execute,/call/finalization_receipt,<computed:preexec-finalization-receipt>,"guessed")	nonzero
call-tampered-observation	J(execute,/call/writer_observation_hash,<computed:preexec-observation-hash>,"tampered")	nonzero
call-stale-head	TA(P,foreign.txt,100644,"after finalization\n",P)	nonzero
call-wrong-worktree	J(execute,/call/worktree,<computed:random-root>,"C:/foreign")	nonzero
call-session-owned-writer-field	JA(execute,/call/writer_field_origin,<absent>,"session")	nonzero

setup-create-collision	TA(S0,validation.config,100644,"foreign\n",none)	nonzero
setup-overlay-preimage-mismatch	TR(S0,AGENTS.md,"owner preface\n","owner changed\n")	nonzero
setup-overlay-unrelated-line-loss	TR(S1,AGENTS.md,"owner preface\n\nv21 run contract\n","v21 run contract\n")	nonzero
setup-protected-overwrite	TR(S1,notes/owner.txt,"owner data\n","changed\n")	nonzero
setup-protected-delete	TD(S1,notes/owner.txt,"owner data\n")	nonzero
setup-undeclared-add	TA(S1,extra.txt,100644,"extra\n",none)	nonzero
setup-stale-inventory	J(setup,/call/protected_inventory_hash,<computed:setup-inventory-hash>,"stale")	nonzero
setup-half-initialized	TA(S0,validation.config,100644,"synced_contract_version: 20\n",none)	nonzero
setup-create-overlay-same-path	CA(/setup/manifest,<end>,{"op":"create","path":"AGENTS.md","class":"contract","source_mode":"100644","source_blob":"<computed:v21-agents-blob>"})	nonzero

resync-dirty	TA(RB,dirty.txt,100644,"uncommitted\n",none)	nonzero
resync-wrong-branch	J(resync,/call/branch,"codex/v21-resync","foreign")	nonzero
resync-wrong-base	J(resync,/call/base,<computed:RB>,<computed:RS>); J(resync,/call/base_authority,"sha:<computed:RB>","sha:<computed:RS>")	nonzero
resync-source-touch	TA(RS,src/Leak.fixture,100644,"source edit\n",RS)	nonzero
resync-test-touch	TA(RS,tests/Foreign.fixture,100644,"test edit\n",RS)	nonzero
resync-feature-acceptance-touch	TA(RS,openspec/changes/foreign/spec.md,100644,"feature\n",RS)	nonzero
resync-hidden-history	TA(RB,hidden.txt,100644,"historical\n",<computed:RB-parent>)	nonzero
resync-self-bumped-stamp	TR(RB,validation.config,"synced_contract_version: 20\n","synced_contract_version: 21\n") before install	nonzero

plan-skipped	JD(plan_after_owner,/call/plan_receipt,<computed:plan-receipt>)	nonzero
plan-approval-before-receipt	J(plan_after_owner,/call/owner_verdict_observed_at,"2026-07-13T10:01:00Z","2026-07-13T09:59:59Z")	nonzero
plan-owner-cites-other-receipt	J(plan_after_owner,/call/owner_verdict,"accepted:<computed:plan-receipt>","accepted:foreign")	nonzero
plan-packet-edit-after-receipt	TR(P,openspec/changes/v21-fixture-change/specs/core/spec.md,"OB-1 exact result\n","OB-1 edited\n")	nonzero
plan-stale-receipt	J(plan_after_owner,/call/plan_candidate_head,<computed:P>,<computed:B>)	nonzero
plan-source-edit	TA(P,src/PlanLeak.fixture,100644,"source\n",P)	nonzero
plan-test-edit	TA(P,tests/PlanLeak.fixture,100644,"test\n",P)	nonzero
plan-toolchain-edit	TR(P,validation.config,"synced_contract_version: 21\n","changed\n")	nonzero
plan-unmanifested-edit	TA(P,docs/unmanifested.md,100644,"extra\n",P)	nonzero
plan-acceptance-under-transcribed	CD(/testability/coverage/0,<exact-object>)	nonzero
plan-tip-as-base	J(plan_after_owner,/call/base,<computed:B>,<computed:P>); J(plan_after_owner,/call/base_authority,"sha:<computed:B>","sha:<computed:P>")	nonzero
plan-historical-build-as-base	J(plan_after_owner,/call/base,<computed:B>,"b94806deaaa3cbb56a8b6cda9baa75ac52f028c3"); J(plan_after_owner,/call/base_authority,"sha:<computed:B>","sha:b94806deaaa3cbb56a8b6cda9baa75ac52f028c3")	nonzero
plan-stale-ref	J(plan_after_owner,/call/base_authority,"sha:<computed:B>","ref:origin/main@<computed:B>"); REF_MOVE(origin/main,<computed:B>,<computed:P>)	nonzero

recipe-missing-binding	CD(/testability/recipes/0/negative,<exact-object>)	nonzero
recipe-five-fields-no-skeleton-signature	CD(/testability/recipes/0/skeleton,<exact-array>); CD(/testability/recipes/0/construct/signature,"Fixture.Core.Create(System.Int32,Fixture.Topology)")	nonzero
recipe-wrong-overload	C(/testability/recipes/0/construct/signature,"Fixture.Core.Create(System.Int32,Fixture.Topology)","Fixture.Core.Create()")	nonzero
recipe-omitted-argument	CD(/testability/recipes/0/construct/args/1,<exact-object>)	nonzero
recipe-inaccessible-unowned	C(/testability/recipes/0/negative/visibility,"internal-friend:Fixture.Tests","private"); CD(/testability/recipes/0/negative/owner,"operation:Step")	nonzero
recipe-vague-observation-injection	C(/testability/recipes/0/observe/signature,"Fixture.Audit.Read(Fixture.Core)","audit counters"); C(/testability/recipes/0/negative/signature,"FixtureFault.Select(FixtureFaultKind)","fault hook")	nonzero
recipe-missing-topology-face	CD(/testability/recipes/0/source/topology,"fixture:two-room-open-sealed-faces")	nonzero
recipe-missing-golden-source-isolation	CD(/testability/recipes/0/source/golden,"fixture:golden-cell-result"); CD(/testability/recipes/0/source/source_isolation,"fixture:single-source-with-neighbor-zero")	nonzero
recipe-missing-handler-owner	CD(/testability/recipes/0/source/handler_owner,"slot:core")	nonzero
recipe-missing-audit-hidden-observe	C(/testability/recipes/0/observe/returns,"slot:value-counter-hidden","slot:value")	nonzero
recipe-missing-loopback-delegation	CD(/testability/recipes/0/source/loopback,"fixture:loopback-delegates-once"); CD(/testability/recipes/0/negative/delegates,"Fixture.Core.Step(Fixture.Impulse,Fixture.ReactionHandler)")	nonzero
recipe-missing-negative-shape	CD(/testability/recipes/0/negative/controls/1,"fixture:throw-during")	nonzero
red-realization-direct-absent-api	C(/testability/recipes/0/red_realization/new_symbol_route,"reflection:Fixture.Core::Create(System.Int32,Fixture.Topology)","direct:Fixture.Core.Create(1,topology)"); C(/testability/recipes/0/red_realization/base_compiles,true,false)	nonzero
red-realization-production-stub	C(/testability/recipes/0/red_realization/production_stub,false,true)	nonzero

manifest-packet-omitted	CD(/testability/manifest/0,<exact-object>)	nonzero
manifest-wrong-baseline-base	C(/testability/manifest/5/base,<computed:B>,<computed:P>)	nonzero
manifest-symlink	TM(P,openspec/changes/v21-fixture-change/specs/core/spec.md,100644,120000)	nonzero
manifest-gitlink	TM(P,openspec/changes/v21-fixture-change/specs/core/spec.md,100644,160000)	nonzero
manifest-reparse-outside	TR(P,openspec/changes/v21-fixture-change/specs/core/spec.md,"OB-1 exact result\n","reparse:C:/outside")	nonzero
manifest-case-collision	TA(P,openspec/changes/v21-fixture-change/specs/core/SPEC.md,100644,"collision\n",P)	nonzero
manifest-mode-swap	TM(P,docs/adr/ADR-v21-fixture.md,100644,100755)	nonzero

red-production-before-R	TA(P,src/Implementation.fixture,100644,"production before RED\n",P)	nonzero
red-mixed-source-test-R	TA(R,src/Implementation.fixture,100644,"mixed\n",R)	nonzero
red-extra-unmanifested-helper	TA(R,tests/HiddenHelper.fixture,100644,"helper\n",R)	nonzero
red-wrong-parent	J(red_boundary,/call/red/parent_head,<computed:P>,<computed:B>)	nonzero
red-wrong-author	J(red_boundary,/call/red/author_role,"independent-test-author","builder")	nonzero
red-protected-delete	EACH_RED_MEMBER TD(Q,<path>,<old>)	nonzero
red-protected-rename	EACH_RED_MEMBER RENAME(Q,<path>,<renamed-path>)	nonzero
red-protected-edit-restore	EACH_RED_MEMBER TR(Q,<path>,<old>,"edited\n") then RESTORE(Q,<path>,<old>)	nonzero
red-manifest-rewrite	J(resume_progress,/call/red/manifest_hash,<computed:oracle-manifest-hash>,"rewritten")	nonzero
red-filter-excluded	J(red_boundary,/call/red/filter,"FixtureTests.OB_1","NoTests")	nonzero
red-shadow-id	TA(R,tests/Shadow.fixture,100644,"FixtureTests.OB_1\n",R)	nonzero
red-duplicate-id	J(red_boundary,/call/red/unique_ids,["FixtureTests.OB_1"],["FixtureTests.OB_1","FixtureTests.OB_1"])	nonzero
red-revision-wrong-parent	J(red_revision,/call/red/revisions/0/parent_head,<computed:Q>,<computed:R>)	nonzero
red-revision-mixed-source	TA(T,src/RevisionLeak.fixture,100644,"mixed\n",T)	nonzero
red-revision-extra-helper	TA(T,tests/RevisionHelper.fixture,100644,"unmanifested\n",T)	nonzero

resume-wrong-run	J(resume_progress,/call/run_id,<computed:run-id>,"foreign")	nonzero
resume-foreign-source	TA(Q,src/Foreign.fixture,100644,"foreign\n",Q)	nonzero
resume-rewritten-R	TR(Q,tests/FixtureTests.fixture,<exact-R-bytes>,"rewritten\n")	nonzero
resume-unaccepted-progress	J(resume_progress,/call/progress_commit,<computed:Q>,<computed:foreign-Q>)	nonzero
resume-ledger-mismatch	J(resume_progress,/call/progress_ledger_blob,<computed:q-accepted-ledger-blob>,"foreign")	nonzero
resume-historical-checkpoint	J(resume_progress,/call/progress_commit,<computed:Q>,"b94806deaaa3cbb56a8b6cda9baa75ac52f028c3")	nonzero

result-self-hash	TR(D,docs/results/v21-fixture-change.md,<exact-result-bytes>,<exact-result-bytes-plus-D-or-blob>)	nonzero
result-wrong-path	RENAME(D,docs/results/v21-fixture-change.md,RESULT.md)	nonzero
result-wrong-blob	TR(D,docs/results/v21-fixture-change.md,<exact-result-bytes>,"wrong\n")	nonzero
archive-nonadjacent	J(close,/call/archive/archive_parent,<computed:D>,<computed:Q>)	nonzero
archive-result-edit	TR(A,docs/results/v21-fixture-change.md,<exact-result-bytes>,"edited\n")	nonzero
archive-toolchain-edit	TR(A,validation.config,"synced_contract_version: 21\n","changed\n")	nonzero
archive-oracle-edit	TR(A,docs/validation/oracle-v21-fixture.json,"FixtureTests.OB_1|DW-1 missing member|RED\n","edited\n")	nonzero
archive-zero-root	TDIR(A,openspec/changes/archive/v21-fixture-change/**)	nonzero
archive-duplicate-root	TA(A,openspec/changes/archive/v21-fixture-copy/specs/core/spec.md,100644,"OB-1 exact result\n",A)	nonzero
archive-missing-member	EACH_PACKET_MEMBER TD(A,<archive-path>,<old>)	nonzero
archive-renamed-member	EACH_PACKET_MEMBER RENAME(A,<archive-path>,<other-suffix>)	nonzero
archive-extra-member	TA(A,openspec/changes/archive/v21-fixture-change/extra.md,100644,"extra\n",A)	nonzero
archive-authority-edit	TR(A,docs/adr/ADR-v21-fixture.md,"ADR-v21-fixture\n","edited\n")	nonzero

trust-root-omitted	CD(/toolchain/roots/1,<exact-object>)	nonzero
trust-root-substituted	TR(B,tools/plan-handoff-check.fixture,"v21 checker implementation\n","exit 0\n")	nonzero
trust-root-symlink	TM(B,tools/plan-handoff-check.fixture,100644,120000)	nonzero
trust-root-gitlink	TM(B,tools/plan-handoff-check.fixture,100644,160000)	nonzero
trust-root-reparse-outside	TR(B,tools/plan-handoff-check.fixture,"v21 checker implementation\n","reparse:C:/outside")	nonzero
trust-root-case-collision	TA(B,tools/PLAN-HANDOFF-CHECK.fixture,100644,"collision\n",B)	nonzero
trust-root-mode-swap	TM(B,tools/plan-handoff-check.fixture,100644,100755)	nonzero
trust-root-unlisted-load	LOAD(B,tools/unlisted-helper.fixture)	nonzero
trust-root-dynamic-load	LOAD(B,<computed:runtime-path>)	nonzero
trust-root-checker-before-pin	RUN_BEFORE_PIN(plan_entry,tools/plan-handoff-check.fixture)	nonzero
checker-mutates-each-mode	EACH_MODE SIDE_EFFECT(<snapshot-tree>,checker-mutated.txt,"bad\n")	nonzero
```

## Bootstrap meta-witnesses and external receipt

Writer also substitutes: (1) an always-zero checker; (2) a checker switching on case/order/root, values never passed; (3) each declared negative with its named defect removed after the mutation declaration; and (4) a corpus missing any one expanded mutation or carrying an unpinned adapter/specimen blob. Each bootstrap must fail before stamp 21. The valid specimen is also repeated at different random roots/orders and must remain identical in outcome.

Writer persists one row per expanded case: `mutation-digest | adapter-mode/blob | specimen-hash | projected-call-hash | before-tree | after-tree | exit | status-before | status-after`. `validation-conformance-receipt-hash` covers the ordered rows plus this file's git blob. Expected exits, labels and mutation DSL never enter product checker input.

END_OF_FILE: os/engineering/V21-CONFORMANCE.md
