# v21 handoff conformance corpus

This file is the OS-owned fixture, phase-snapshot and mutation authority for contract v21. SETUP/RE-SYNC CALL-intent pins this file's git blob as `os-conformance-corpus-blob`, the SHA-256 of the exact JSON fence as `valid-specimen-hash`, and an independently reviewed stack adapter source/mode/blob. Product installer/checker code supplies none of that truth.

## Materializer and receipt contract

- UTF-8, LF, final LF. The JSON key/order/bytes are exactly as printed. `<computed:...>` expands only after its dependencies exist; the rendered external specimen/receipts never live in a commit whose id they contain.
- Writer creates a random disposable product root. It writes only fixed baseline files, commits B, renders external identity with B, commits packet-only P, test/oracle-only R, accepted build Q, result-bearing D, then archive-only A. Exact membership is below. No commit or product result self-hashes.
- Snapshot inheritance means recursive copy of the named parent, exact listed JSON-pointer `delete` operations, then `set`; no implicit merge/default is legal. `identity_ref` expands all identity keys; `toolchain_ref` expands root rows/manifest/corpus/accepted-adapter fields; `manifest_ref` expands ordered create/overlay rows; `testability_ref` materializes TESTABILITY content and expands exactly `testability|testability-mode|testability-blob|input-manifest-hash|complete-sweep|verdict`. Reference tokens are never passed. Adapter serializes only that snapshot's expanded `call` and materializes only its current checker tree. Install first verifies `entry_tree`, applies only manifest, then runs on `tree`; every other snapshot has no transition. Siblings/future evidence never reach checker.
- Writer verifies the pinned adapter's output path/mode/blob manifest, applies exactly one declared (possibly compound) mutation with matching old preimage, and verifies the rendered before/after tree delta. Product gate modes invoke the checker with ordinary `DIRECTION_*` fields; `writer-*` snapshots exercise the writer transaction guard only. Snapshot handback evidence is never checker input. Neither surface receives case id, order, expected exit, root purpose, corpus path or mutation name. Roots and case order are randomized.
- Valid cases exit 0; every invalid expansion exits nonzero. Every mode is read-only: fixture/product status and tree hashes before/after the check are identical.

## Canonical bytes, salt and dependency order

`H(x)` is lowercase SHA-256 of exact UTF-8/LF bytes. `F(kind, fields...)` is `v21/` + kind + LF, then each field in the listed order as `name<TAB>utf8-byte-count<TAB>value<LF>`; repeated rows use zero-padded ordinal names. Values are never locale-sorted or implicitly trimmed. This framing is the only receipt serialization.

Writer creates a fresh 32-byte random nonce for every corpus run. `S(literal)` is the first 16 hex chars of `H(F("salt", nonce, literal))`. Keys, `<computed|salt:...>` tokens, git modes/hashes, phase/mode/status/visibility/record-kind values, config/result field names, system primitives and structural tool paths `validation.config|AGENTS.md|tools/plan-handoff-*|docs/results/{change-id}.md` are the complete reserved set. Every other JSON string value and graph path/content literal is neutral fixture data and receives suffix `-S(literal)`; identical literals share a value, replacements run longest-first before any blob/hash. Grammar prefixes `literal:|fixture:|slot:|reflection:|internal-friend:` stay fixed while identifier payloads salt; integer fixture literals use `1 + (first nonce byte mod 3)` and all golden bytes update before hashing. Thus repo, branches, change/criterion/obligation/test ids, namespaces/types/members, fixture data and PublicApi/FixtureTests/ADR/oracle/result path segments all vary. `salt-map-hash=H(F("salt-map", ordered canonical->rendered rows))`. Two nonces must yield identical verdicts. A checker switching on neutral canonical/rendered fingerprint is a required failing meta-witness.

Canonical derived values, in dependency order:

1. Pin corpus template git blob, exact unexpanded JSON-fence hash, stack profile blob and writer-accepted adapter event/path/mode/blob.
2. Generate nonce/salt map and random root. Materialize fixed S0/RB/B bytes only. Product B never contains a specimen/receipt that cites B.
3. Git blobs use the repository's observed object format. Trees are built from sorted path/mode/blob rows. Commits use `git commit-tree`, author/committer `Direction OS <direction-os@invalid>`, timestamps `2001-01-01T00:00:00Z` plus graph ordinal seconds, and exact message `v21 <node>`. This deterministically yields RB/RS/SB/B/P/R/Q/T/D/A.
4. `acceptance-hash=H(exact salted done_when bytes)`. Typed manifest/toolchain hashes are `H(F(kind, ordered ordinal rows))`. `exact-patch-hash=H(F("overlay", path, pre-mode, pre-blob, post-mode, post-blob))`; no patch tool output is hashed. TESTABILITY blob is computed only from its in-file content; its external pin is added afterward.
5. `intent-hash=H(exact LF intent packet bytes)`. `finalization-receipt=H(F("finalize", intent-hash, worktree, phase, plan-stage-or-empty, branch-or-empty, base-authority-or-empty, observed-head-or-empty, applicable ordered identity hashes, pre-status-hash))`; it excludes itself and checker result. `writer-observation-hash=H(F("observe", mode, exact-command, decimal-exit, status-before-hash, status-after-hash))`.
6. `plan-receipt=H(F("plan", candidate-head, base-authority, acceptance-hash, toolchain-manifest-hash, validation-conformance-receipt, testability-mode, testability-blob, input-manifest-hash, plan-observation-hash))`. Writer history event stores those fields plus product paths/blobs; its workflow commit is computed only after the event file exists. `run-id=H(F("run", plan-receipt-event, candidate-head, base-authority, acceptance-hash))`; `pre-execution-receipt=H(F("preexec", run-id, pre-red-head, plan-receipt, all immutable pins, preexec-observation-hash))`.
7. Oracle/progress/result/archive fields are external git path/mode/blob/commit observations. Ledger blobs are git blob ids of exact ledger bytes and never contain their own blob/commit. Product result contains no D/result-blob/A.
8. Install pass uses random challenge `H(F("challenge", nonce, target-root))`. `bootstrap-receipt=H(F("bootstrap", challenge, corpus-blob, specimen-hash, salt-map-hash, adapter-event, adapter-blob, ordered install rows))`. In non-install corpus cases the projected CALL carries that value while writer separately supplies the same value from Stage-A rows as `DIRECTION_CONFORMANCE_AUTHORITY_RECEIPT`; checker must compare them. `validation-conformance-receipt=H(F("conformance", bootstrap-receipt, ordered non-install rows))`. Writer persists final value/path/blob in Direction history. Real calls name that event; writer resolves it independently into the authority environment. A final per-mode binding smoke uses the final receipt/event but is excluded from receipt preimage and stored beside it.

Token registry is closed: node tokens `S0|SB|RB|RS|B|P|R|Q|T|D|A|W-plan-receipt` come only from graph/tree/commit rules; file `*-blob` tokens come only from exact graph/config/packet/ledger/result bytes via git blob hashing; `*-intent-hash|*-observation-hash|*-finalization-receipt|plan-receipt|run-id|preexec-receipt|bootstrap-*|final-conformance-receipt|input-manifest-hash|toolchain-manifest-hash|*-patch-hash` come only from numbered `H/F` formulas. `random-root|outside-root|runtime-path|*-result-path` are nonce-named paths. `RB-parent|foreign-Q|foreign-writer-commit|verdict-result-commit|changed-adapter-blob|nonzero-plan-*` are negative-only disposable objects and never equal/ancestor valid counterparts. `stack-id|adapter-author-session|adapter-review-session|installer-session|adapter event/blob` are exact observations from the already committed separate adapter transaction/profile and are never generated by installer. No other computed token is legal.

Any undeclared `<computed:...>` token, dependency read before its row, different byte framing, implicit timestamp, or adapter-specific default is materialization failure before checker invocation.

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
    "done_when": "DW-1 exact result\n",
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
    "adapter_event": "history/<computed:adapter-review-result-path>@<computed:adapter-accept-writer-commit>",
    "adapter_source": "work/validation-adapters/<computed:stack-id>-v21.fixture",
    "adapter_mode": "100644",
    "adapter_blob": "<computed:accepted-adapter-blob>",
    "adapter_author_session": "<computed:adapter-author-session>",
    "adapter_review_session": "<computed:adapter-review-session>",
    "adapter_review_verdict": "GREEN",
    "installer_session": "<computed:installer-session>"
  },
  "testability_pin": {
    "path": "openspec/changes/v21-fixture-change/TESTABILITY.md",
    "mode": "100644",
    "blob": "<computed:testability-blob>",
    "input_manifest_hash": "<computed:input-manifest-hash>"
  },
  "testability": {
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
    "setup": {"entry_tree": "<computed:S0>", "tree": "<computed:SB>", "gate_mode": "install", "call": {"packet_stage": "finalized", "phase": "SETUP", "worktree": "<computed:random-root>", "manifest_ref": "setup.manifest", "corpus_ref": "toolchain", "conformance_bootstrap_challenge": "<computed:bootstrap-challenge>", "intent_hash": "<computed:setup-intent-hash>", "finalization_receipt": "<computed:setup-finalization-receipt>", "writer_observation_hash": "<computed:setup-observation-hash>", "entry_state": "nonempty", "entry_git": "none", "protected_inventory_count": 1, "protected_inventory_hash": "<computed:setup-inventory-hash>"}},
    "resync": {"entry_tree": "<computed:RB>", "tree": "<computed:RS>", "gate_mode": "install", "call": {"packet_stage": "finalized", "phase": "RE-SYNC", "identity_ref": "resync.identity", "head": "<computed:RB>", "manifest_ref": "resync.manifest", "corpus_ref": "toolchain", "conformance_bootstrap_challenge": "<computed:bootstrap-challenge>", "intent_hash": "<computed:resync-intent-hash>", "finalization_receipt": "<computed:resync-finalization-receipt>", "writer_observation_hash": "<computed:resync-observation-hash>"}},
    "plan_entry": {"tree": "<computed:B>", "gate_mode": "plan-entry", "writer_authority": {"conformance_receipt": "<computed:bootstrap-receipt>", "source": "bootstrap-stage-A-observed-rows"}, "call": {"packet_stage": "finalized", "phase": "PLAN", "plan_stage": "author", "identity_ref": "identity", "head": "<computed:B>", "preexisting_plan_diff": [], "toolchain_ref": "toolchain", "validation_conformance_receipt": "<computed:bootstrap-receipt>", "intent_hash": "<computed:plan-intent-hash>", "finalization_receipt": "<computed:plan-entry-finalization-receipt>", "writer_observation_hash": "<computed:plan-entry-observation-hash>"}},
    "plan_gated": {"inherits": "plan_entry", "tree": "<computed:P>", "gate_mode": "plan", "plan_observation": {"mode": "plan", "command": "tools/plan-handoff-check.fixture plan", "exit": 0, "status_before": "clean:<computed:P>", "status_after": "clean:<computed:P>", "hash": "<computed:plan-observation-hash>"}, "result_evidence": {"checkpoint": "PLAN-GATED", "owner_verdict": "<absent>"}, "set": {"/call/head": "<computed:P>", "/call/plan_candidate_head": "<computed:P>", "/call/plan_observation_hash": "<computed:plan-observation-hash>", "/call/plan_receipt": "<computed:plan-receipt>", "/call/testability_ref": "testability_pin+testability"}},
    "verdict_call": {"inherits": "plan_gated", "gate_mode": "writer-verdict-entry", "writer_event": {"path": "history/<computed:plan-gated-result-path>", "blob": "<computed:plan-gated-result-blob>", "commit": "<computed:W-plan-receipt>"}, "set": {"/call/plan_stage": "verdict", "/call/plan_receipt_event": "history/<computed:plan-gated-result-path>@<computed:W-plan-receipt>", "/call/intent_hash": "<computed:verdict-intent-hash>", "/call/finalization_receipt": "<computed:verdict-finalization-receipt>", "/call/writer_observation_hash": "<computed:verdict-entry-observation-hash>"}},
    "plan_after_owner": {"inherits": "verdict_call", "gate_mode": "writer-verdict-return", "result_evidence": {"owner_words": "ACCEPT exact candidate <computed:P> receipt <computed:plan-receipt>", "plan_receipt_event": "history/<computed:plan-gated-result-path>@<computed:W-plan-receipt>"}},
    "execute": {"inherits": "plan_after_owner", "gate_mode": "pre-execution", "delete": ["/call/plan_stage"], "set": {"/call/phase": "EXECUTE", "/call/execution_mode": "fresh", "/call/owner_verdict": "accepted:<computed:plan-receipt>", "/call/intent_hash": "<computed:execute-intent-hash>", "/call/finalization_receipt": "<computed:preexec-finalization-receipt>", "/call/run_id": "<computed:run-id>", "/call/pre_red_head": "<computed:P>", "/call/pre_execution_receipt": "<computed:preexec-receipt>", "/call/writer_observation_hash": "<computed:preexec-observation-hash>", "/call/product_result_path": "docs/results/v21-fixture-change.md"}},
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
CONFIG_V21="synced_contract_version: 21\nplan_handoff_check: tools/plan-handoff-check.fixture\nplan_handoff_modes: install,plan-entry,plan,pre-execution,red-boundary,resume,deliver,close\nplan_handoff_trust_roots: validation.config@100644,tools/plan-handoff-check.fixture@100644,tools/plan-handoff-schema.fixture@100644\nproduct_result_template: docs/results/{change-id}.md\nproduct_result_required_fields: change-id,base-authority,acceptance-hash,run-id,location,archive-source,archive-target,outcome,evidence,assumptions,cuts,cost,manual-acceptance,next\n"
CONFIG_V20="synced_contract_version: 20\nproduct_result_template: docs/results/{change-id}.md\n"
RESULT_BYTES="change-id: v21-fixture-change\nbase-authority: sha:<computed:B>\nacceptance-hash: <computed:acceptance-hash>\nrun-id: <computed:run-id>\nlocation: docs/results/v21-fixture-change.md\narchive-source: openspec/changes/v21-fixture-change\narchive-target: openspec/changes/archive/v21-fixture-change\noutcome: exact result\nevidence: fixture evidence\nassumptions: none\ncuts: none\ncost: fixture\nmanual-acceptance: none\nnext: return-to-direction\n"
S0: AGENTS.md="owner preface\n"; notes/owner.txt="owner data\n"
SB-S0: CREATE validation.config=CONFIG_V21 and the two pinned toolchain roots; OVERLAY AGENTS.md="owner preface\n\nv21 run contract\n"; notes/owner.txt unchanged; initialize and commit clean installed SB only after exact postimage verification
RB: validation.config=CONFIG_V20; AGENTS.md="owner preface\nv20 run contract\n"; src/Existing.fixture="existing product\n"; branch=codex/v21-resync; clean initialized commit
RS-RB: OVERLAY validation.config=CONFIG_V21; OVERLAY AGENTS.md="owner preface\nv21 run contract\n"; CREATE the two pinned toolchain roots; src/Existing.fixture unchanged; no feature/source/test/acceptance delta
B: validation.config=CONFIG_V21; tools/plan-handoff-check.fixture="v21 checker implementation\n"; tools/plan-handoff-schema.fixture="v21 schema\n"; src/PublicApi.fixture="type Fixture.Core; existing Step and Value; Create(System.Int32,Fixture.Topology) absent\n"; AGENTS.md="v21 run contract\n"
P-B: ADD proposal.md="proposal v21\n"; PLAN.md="plan v21\n"; tasks.md="tasks v21\n"; specs/core/spec.md="OB-1 exact result\n" under openspec/changes/v21-fixture-change/; ADD docs/adr/ADR-v21-fixture.md="ADR-v21-fixture\n"; ADD TESTABILITY.md as the adapter's exact canonical rendering of `testability`; no source/test/toolchain/result change
R-P: ADD tests/FixtureTests.fixture="base-compilable reflection lookup Fixture.Core::Create(System.Int32,Fixture.Topology); unique FixtureTests.OB_1; runtime RED DW-1 missing member\n"; ADD docs/validation/oracle-v21-fixture.json="FixtureTests.OB_1|DW-1 missing member|RED\n"
Q-R: REPLACE src/PublicApi.fixture="type Fixture.Core; Create(System.Int32,Fixture.Topology), Step and Value implemented\n"; ADD PROGRESS.md="accepted build progress\n"
T-Q: independent test-author only REPLACE tests/FixtureTests.fixture="base-compilable reflection route; unique FixtureTests.OB_1; revised runtime RED DW-1\n" and docs/validation/oracle-v21-fixture.json="FixtureTests.OB_1|DW-1 revised RED\n"; no source/frozen/toolchain/result/unmanifested delta
D-Q: ADD docs/results/v21-fixture-change.md=RESULT_BYTES; no self hash/commit
A-D: MOVE openspec/changes/v21-fixture-change/** to openspec/changes/archive/v21-fixture-change/** preserving suffix/mode/blob; no other delta
```

Main feature commit order is exactly B -> P -> R -> Q -> D -> A. The valid later-RED branch is Q -> T and stops at a resumable checkpoint. RE-SYNC is the separate RB -> RS contour; SETUP begins at non-git S0 and ends at clean initial commit SB. External plan/finalization/RED/progress/routing receipts are rendered only after the commit ids they cite exist.

## Exact valid cases

```text
adapter:separate-author-review-writer-event	adapter event ancestor; author!=reviewer!=installer; reviewed blob exact	0
setup:create-plus-overlay-preserves-unlisted	snapshot=setup; entry=S0; expected_post=SB	0
resync:exact-contract-only	snapshot=resync; entry_head=RB; expected_post=RS	0
bootstrap:install-challenge	snapshots=setup,resync; no final conformance receipt	0
bootstrap:noninstall-opaque-receipt	snapshots=plan_entry,plan_gated,execute,red_boundary,resume_red,resume_progress,deliver,close; receipt=<computed:bootstrap-receipt>	0
bootstrap:final-receipt-binding-smoke	EACH_NONINSTALL_MODE replace bootstrap receipt+writer authority with <computed:final-conformance-receipt>, bind persisted event, recompute dependent H/F receipts; rows excluded from conformance preimage	0
plan:clean-entry	snapshot=plan_entry	0
plan:gated-author-checkpoint-no-verdict	snapshot=plan_gated	0
plan:writer-event-precedes-verdict-call	snapshot=verdict_call; workflow event W exists before open_call	0
plan:owner-words-from-separate-verdict	snapshot=plan_after_owner; W ancestor of verdict CALL/RESULT	0
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

`J/JD/JA(snapshot,pointer,old,new)` replace/delete/add on a fully projected snapshot, including its CALL or handback evidence. `C/CD/CA(pointer,old,new)` mutate the canonical transaction object before the relevant phase, re-render the affected product file, then recompute every mechanically dependent mode/blob/manifest/finalization/phase receipt but never the expected outcome or mutated semantic field; `C@mode` schedules that mutation immediately before the named mode. Thus a semantic miss cannot be reduced to a stale-hash failure. `TA/TD/TDIR/TR/TM/RENAME/RESTORE/TEXT_DELETE_EXACT`, `HC(parent,child,operation)` for an exact committed history edge, `REF_MOVE`, `REPARSE`, `LOAD`, `RUN_BEFORE_PIN`, and `SIDE_EFFECT` are exact tree/environment operations. Old value/tree/parent must match or materialization itself fails. `EACH_MODE[install,plan-entry,plan,pre-execution,red-boundary,resume,deliver,close]`, `EACH_NONINSTALL_MODE[plan-entry,plan,pre-execution,red-boundary,resume,deliver,close]`, `EACH_REAL_ID_MODE[plan,pre-execution,red-boundary,resume,deliver,close]` and `EACH_DESCENDANT_MODE[pre-execution,red-boundary,resume,deliver,close]` expand to separately receipted cases; `EACH_RESULT_FIELD[change-id,base-authority,acceptance-hash,run-id,location,archive-source,archive-target,outcome,evidence,assumptions,cuts,cost,manual-acceptance,next]`; `EACH_PACKET_MEMBER` expands five openspec members; `EACH_RED_MEMBER` expands both R-P protected paths.

Operation semantics are fixed: `TA(tree,path,mode,bytes,parent)` hashes exact bytes and adds that index row. `parent=none` leaves the named snapshot dirty; otherwise parent must equal `tree` and adapter commits deterministic child `M(case-label)` with the graph identity rules, then checks that child. `TD` requires current mode/blob then removes; `TDIR` expands sorted tracked descendants; `TR` requires old bytes and replaces only content; `TEXT_DELETE_EXACT` requires exactly one matching LF record and removes it; absent commit syntax means a dirty mutation. `TM` uses `git update-index --cacheinfo <mode>,<blob>,<path>`; mode 120000 stores exact link-target bytes and mode 160000 uses an existing disposable commit id. `REPARSE(tree,path,outside)` creates a real Windows junction/symlink to a nonce-named sibling outside the root and verifies `ReparsePoint` plus resolved escape before running; sentinel text is invalid. `RENAME` is delete+add with identical mode/blob, `RESTORE` requires prior `HC`, `LOAD` records the actually opened canonical path from OS file tracing, and `RUN_BEFORE_PIN` records process start preceding root verification. Tree/status hashes are recomputed after every operation.

Case prefix fixes the execution surface when the operation itself is not snapshot-qualified: `setup|adapter|bootstrap -> install`, `resync -> resync/install`, `plan|recipe|manifest|red-realization -> plan_gated/plan`, first-RED -> red_boundary, RED-history/resume -> resume or deliver as written, result -> deliver, archive|close -> close, trust-root/checker -> the explicit EACH mode. A `C/CD/CA` row without either `@mode` or one of these exact prefixes is corpus-invalid.

```text
call-intent-executed	J(execute,/call/packet_stage,"finalized","intent")	nonzero
call-guessed-finalization	J(execute,/call/finalization_receipt,<computed:preexec-finalization-receipt>,"guessed")	nonzero
call-tampered-observation	J(execute,/call/writer_observation_hash,<computed:preexec-observation-hash>,"tampered")	nonzero
call-stale-head	TA(P,foreign.txt,100644,"after finalization\n",P)	nonzero
call-wrong-worktree	J(execute,/call/worktree,<computed:random-root>,"C:/foreign")	nonzero
call-session-owned-writer-field	JA(execute,/call/writer_field_origin,<absent>,"session")	nonzero
bootstrap-install-missing-challenge	JD(setup,/call/conformance_bootstrap_challenge,<computed:bootstrap-challenge>)	nonzero
bootstrap-install-guessed-final-receipt	JA(setup,/call/validation_conformance_receipt,<absent>,"guessed-final")	nonzero
bootstrap-noninstall-missing-receipt	EACH_NONINSTALL_MODE JD(<snapshot>,/call/validation_conformance_receipt,<computed:bootstrap-receipt>)	nonzero
bootstrap-noninstall-wrong-receipt	EACH_NONINSTALL_MODE J(<snapshot>,/call/validation_conformance_receipt,<computed:bootstrap-receipt>,"wrong")	nonzero
bootstrap-writer-authority-missing	EACH_NONINSTALL_MODE JD(<snapshot>,/writer_authority/conformance_receipt,<computed:bootstrap-receipt>)	nonzero
bootstrap-writer-authority-wrong	EACH_NONINSTALL_MODE J(<snapshot>,/writer_authority/conformance_receipt,<computed:bootstrap-receipt>,"wrong-authority")	nonzero
bootstrap-receipt-changed-between-phases	J(resume_progress,/call/validation_conformance_receipt,<computed:bootstrap-receipt>,"other-phase")	nonzero
bootstrap-final-binding-wrong	EACH_NONINSTALL_MODE final-binding-smoke with "wrong-final" instead of <computed:final-conformance-receipt>	nonzero
bootstrap-final-event-missing	EACH_NONINSTALL_MODE final-binding-smoke without persisted validation-conformance-event	nonzero
bootstrap-final-event-not-ancestral	EACH_NONINSTALL_MODE final-binding-smoke with history/foreign@<computed:foreign-writer-commit>	nonzero
adapter-event-missing	CD@install(/toolchain/adapter_event,"history/<computed:adapter-review-result-path>@<computed:adapter-accept-writer-commit>")	nonzero
adapter-event-not-ancestral	C@install(/toolchain/adapter_event,<exact-event>,"history/foreign@<computed:foreign-writer-commit>")	nonzero
adapter-self-reviewed	C@install(/toolchain/adapter_review_session,<computed:adapter-review-session>,<computed:adapter-author-session>)	nonzero
adapter-installer-is-author	C@install(/toolchain/installer_session,<computed:installer-session>,<computed:adapter-author-session>)	nonzero
adapter-blob-changed-after-review	C@install(/toolchain/adapter_blob,<computed:accepted-adapter-blob>,<computed:changed-adapter-blob>)	nonzero

setup-create-collision	TA(S0,validation.config,100644,"foreign\n",none)	nonzero
setup-overlay-preimage-mismatch	TR(S0,AGENTS.md,"owner preface\n","owner changed\n")	nonzero
setup-overlay-unrelated-line-loss	TR(SB,AGENTS.md,"owner preface\n\nv21 run contract\n","v21 run contract\n")	nonzero
setup-protected-overwrite	TR(SB,notes/owner.txt,"owner data\n","changed\n")	nonzero
setup-protected-delete	TD(SB,notes/owner.txt,"owner data\n")	nonzero
setup-undeclared-add	TA(SB,extra.txt,100644,"extra\n",none)	nonzero
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
resync-self-bumped-stamp	TR(RB,validation.config,CONFIG_V20,CONFIG_V21) before install	nonzero
resync-create-collision	TA(RB,tools/plan-handoff-check.fixture,100644,"foreign\n",RB)	nonzero
resync-overlay-unrelated-line-loss	TR(RS,AGENTS.md,"owner preface\nv21 run contract\n","v21 run contract\n")	nonzero
resync-overlay-wrong-postimage	TR(RS,validation.config,CONFIG_V21,"synced_contract_version: 21\n")	nonzero

plan-skipped	JD(plan_after_owner,/call/plan_receipt,<computed:plan-receipt>)	nonzero
plan-nonzero-observation	J(plan_gated,/plan_observation/exit,0,1); J(plan_gated,/plan_observation/hash,<computed:plan-observation-hash>,<computed:nonzero-plan-observation-hash>); J(plan_gated,/call/plan_observation_hash,<computed:plan-observation-hash>,<computed:nonzero-plan-observation-hash>); J(plan_gated,/call/plan_receipt,<computed:plan-receipt>,<computed:nonzero-plan-receipt>)	nonzero
plan-tampered-observation	J(plan_gated,/call/plan_observation_hash,<computed:plan-observation-hash>,"tampered")	nonzero
plan-author-illegal-owner-verdict	JA(plan_gated,/result_evidence/owner_words,<absent>,"ACCEPT")	nonzero
plan-receipt-first-in-verdict-result	JD(verdict_call,/call/plan_receipt_event,"history/<computed:plan-gated-result-path>@<computed:W-plan-receipt>"); J(plan_after_owner,/result_evidence/plan_receipt_event,"history/<computed:plan-gated-result-path>@<computed:W-plan-receipt>","history/late@<computed:verdict-result-commit>")	nonzero
plan-event-not-ancestral	J(verdict_call,/writer_event/commit,<computed:W-plan-receipt>,<computed:foreign-writer-commit>)	nonzero
plan-owner-cites-other-receipt	J(plan_after_owner,/result_evidence/owner_words,"ACCEPT exact candidate <computed:P> receipt <computed:plan-receipt>","ACCEPT foreign")	nonzero
plan-verdict-candidate-mismatch	J(verdict_call,/call/plan_candidate_head,<computed:P>,<computed:B>)	nonzero
plan-packet-edit-after-receipt	TR(P,openspec/changes/v21-fixture-change/specs/core/spec.md,"OB-1 exact result\n","OB-1 edited\n")	nonzero
plan-stale-receipt	J(plan_after_owner,/call/plan_candidate_head,<computed:P>,<computed:B>)	nonzero
plan-source-edit	TA(P,src/PlanLeak.fixture,100644,"source\n",P)	nonzero
plan-test-edit	TA(P,tests/PlanLeak.fixture,100644,"test\n",P)	nonzero
plan-toolchain-edit	TR(P,validation.config,CONFIG_V21,"changed\n")	nonzero
plan-unmanifested-edit	TA(P,docs/unmanifested.md,100644,"extra\n",P)	nonzero
plan-acceptance-under-transcribed	CD(/testability/coverage/0,<exact-object>)	nonzero
plan-tip-as-base	J(plan_after_owner,/call/base,<computed:B>,<computed:P>); J(plan_after_owner,/call/base_authority,"sha:<computed:B>","sha:<computed:P>")	nonzero
plan-historical-build-as-base	J(plan_after_owner,/call/base,<computed:B>,"b94806deaaa3cbb56a8b6cda9baa75ac52f028c3"); J(plan_after_owner,/call/base_authority,"sha:<computed:B>","sha:b94806deaaa3cbb56a8b6cda9baa75ac52f028c3")	nonzero
plan-stale-ref	J(plan_after_owner,/call/base_authority,"sha:<computed:B>","ref:origin/main@<computed:B>"); REF_MOVE(origin/main,<computed:B>,<computed:P>)	nonzero
execute-next-done-when-shrink	J(execute,/call/done_when,"DW-1 exact result\n","DW-1\n")	nonzero
execute-acceptance-source-rewrite	EACH_DESCENDANT_MODE J(<snapshot>,/call/acceptance_source,"call:v21-fixture#done_when","call:foreign#done_when")	nonzero
execute-acceptance-hash-rewrite	EACH_DESCENDANT_MODE J(<snapshot>,/call/acceptance_hash,<computed:acceptance-hash>,"foreign")	nonzero
testability-path-missing	EACH_REAL_ID_MODE JD(<snapshot>,/call/testability,"openspec/changes/v21-fixture-change/TESTABILITY.md")	nonzero
testability-mode-wrong	EACH_REAL_ID_MODE J(<snapshot>,/call/testability-mode,"100644","100755")	nonzero
testability-blob-wrong	EACH_REAL_ID_MODE J(<snapshot>,/call/testability-blob,<computed:testability-blob>,"foreign")	nonzero
testability-input-manifest-wrong	EACH_REAL_ID_MODE J(<snapshot>,/call/input-manifest-hash,<computed:input-manifest-hash>,"foreign")	nonzero

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
manifest-reparse-outside	REPARSE(P,openspec/changes/v21-fixture-change/specs/core/spec.md,<computed:outside-root>)	nonzero
manifest-case-collision	TA(P,openspec/changes/v21-fixture-change/specs/core/SPEC.md,100644,"collision\n",P)	nonzero
manifest-mode-swap	TM(P,docs/adr/ADR-v21-fixture.md,100644,100755)	nonzero

red-production-before-R	TA(P,src/Implementation.fixture,100644,"production before RED\n",P)	nonzero
red-mixed-source-test-R	TA(R,src/Implementation.fixture,100644,"mixed\n",R)	nonzero
red-extra-unmanifested-helper	TA(R,tests/HiddenHelper.fixture,100644,"helper\n",R)	nonzero
red-wrong-parent	J(red_boundary,/call/red/parent_head,<computed:P>,<computed:B>)	nonzero
red-wrong-author	J(red_boundary,/call/red/author_role,"independent-test-author","builder")	nonzero
red-protected-delete	EACH_RED_MEMBER HC(Q,<X-delete>,TD(Q,<path>,<old>)); deliver from <X-delete>	nonzero
red-protected-rename	EACH_RED_MEMBER HC(Q,<X-rename>,RENAME(Q,<path>,<renamed-path>)); deliver from <X-rename>	nonzero
red-protected-edit-restore	EACH_RED_MEMBER HC(Q,<X-edit>,TR(Q,<path>,<old>,"edited\n")); HC(<X-edit>,<Y-restore>,RESTORE(<X-edit>,<path>,<old>)); deliver from <Y-restore> with final bytes equal R	nonzero
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
result-missing-required-field	EACH_RESULT_FIELD TEXT_DELETE_EXACT(D,docs/results/v21-fixture-change.md,"<field>: <exact-value>\n")	nonzero
result-identity-mismatch	TR(D,docs/results/v21-fixture-change.md,RESULT_BYTES,RESULT_BYTES with "change-id: foreign\n")	nonzero
result-location-mismatch	TR(D,docs/results/v21-fixture-change.md,RESULT_BYTES,RESULT_BYTES with "location: RESULT.md\n")	nonzero
result-archive-source-mismatch	TR(D,docs/results/v21-fixture-change.md,RESULT_BYTES,RESULT_BYTES with "archive-source: openspec/changes/foreign\n")	nonzero
result-archive-target-mismatch	TR(D,docs/results/v21-fixture-change.md,RESULT_BYTES,RESULT_BYTES with "archive-target: openspec/changes/archive/foreign\n")	nonzero
result-call-path-substitution	J(deliver,/call/product_result_path,"docs/results/v21-fixture-change.md","RESULT.md")	nonzero
result-wrong-path	RENAME(D,docs/results/v21-fixture-change.md,RESULT.md)	nonzero
result-wrong-blob	TR(D,docs/results/v21-fixture-change.md,<exact-result-bytes>,"wrong\n")	nonzero
archive-nonadjacent	J(close,/call/archive/archive_parent,<computed:D>,<computed:Q>)	nonzero
archive-result-edit	TR(A,docs/results/v21-fixture-change.md,<exact-result-bytes>,"edited\n")	nonzero
archive-toolchain-edit	TR(A,validation.config,CONFIG_V21,"changed\n")	nonzero
archive-oracle-edit	TR(A,docs/validation/oracle-v21-fixture.json,"FixtureTests.OB_1|DW-1 missing member|RED\n","edited\n")	nonzero
archive-zero-root	TDIR(A,openspec/changes/archive/v21-fixture-change/**)	nonzero
archive-duplicate-root	TA(A,openspec/changes/archive/v21-fixture-copy/specs/core/spec.md,100644,"OB-1 exact result\n",A)	nonzero
archive-source-left-beside-target	EACH_PACKET_MEMBER TA(A,<original-source-path>,<mode>,<blob-bytes>,A)	nonzero
archive-missing-member	EACH_PACKET_MEMBER TD(A,<archive-path>,<old>)	nonzero
archive-renamed-member	EACH_PACKET_MEMBER RENAME(A,<archive-path>,<other-suffix>)	nonzero
archive-edited-member	EACH_PACKET_MEMBER TR(A,<archive-path>,<old>,"edited\n")	nonzero
archive-mode-swapped-member	EACH_PACKET_MEMBER TM(A,<archive-path>,100644,100755)	nonzero
archive-extra-member	TA(A,openspec/changes/archive/v21-fixture-change/extra.md,100644,"extra\n",A)	nonzero
archive-undeclared-output	TA(A,docs/undeclared-after-D.md,100644,"extra\n",A)	nonzero
archive-authority-edit	TR(A,docs/adr/ADR-v21-fixture.md,"ADR-v21-fixture\n","edited\n")	nonzero
close-wrong-baseline-base	C@close(/testability/manifest/5/base,<computed:B>,<computed:P>)	nonzero

trust-root-omitted-each-mode	EACH_MODE CD(/toolchain/roots/1,<exact-object>)	nonzero
trust-root-substituted-each-mode	EACH_MODE TR(<snapshot-tree>,tools/plan-handoff-check.fixture,"v21 checker implementation\n","exit 0\n")	nonzero
trust-root-symlink-each-mode	EACH_MODE TM(<snapshot-tree>,tools/plan-handoff-check.fixture,100644,120000)	nonzero
trust-root-gitlink-each-mode	EACH_MODE TM(<snapshot-tree>,tools/plan-handoff-check.fixture,100644,160000)	nonzero
trust-root-reparse-outside-each-mode	EACH_MODE REPARSE(<snapshot-tree>,tools/plan-handoff-check.fixture,<computed:outside-root>)	nonzero
trust-root-case-collision-each-mode	EACH_MODE TA(<snapshot-tree>,tools/PLAN-HANDOFF-CHECK.fixture,100644,"collision\n",<snapshot-head>)	nonzero
trust-root-mode-swap-each-mode	EACH_MODE TM(<snapshot-tree>,tools/plan-handoff-check.fixture,100644,100755)	nonzero
trust-root-unlisted-load-each-mode	EACH_MODE LOAD(<snapshot-tree>,tools/unlisted-helper.fixture)	nonzero
trust-root-dynamic-load-each-mode	EACH_MODE LOAD(<snapshot-tree>,<computed:runtime-path>)	nonzero
trust-root-checker-before-pin-each-mode	EACH_MODE RUN_BEFORE_PIN(<snapshot>,tools/plan-handoff-check.fixture)	nonzero
checker-mutates-each-mode	EACH_MODE SIDE_EFFECT(<snapshot-tree>,checker-mutated.txt,"bad\n")	nonzero
```

## Bootstrap meta-witnesses and external receipt

Writer also substitutes: (1) an always-zero checker; (2) a checker switching on case/order/root, values never passed; (3) a checker switching on any canonical fixture literal or the first nonce's rendered repo/branch/change/path/type/member/test/criterion fingerprint, then repeats with a second nonce; (4) each declared negative with its named defect removed after declaration; and (5) a corpus missing any expanded mutation or carrying an unaccepted adapter/specimen blob. Each bootstrap must fail before stamp 21. The same semantic specimens at different nonce/root/order must remain identical in outcome.

Writer persists one row per expanded case: `salt-map-hash | mutation-digest | adapter-event/mode/blob | specimen-hash | projected-call-hash | before-tree | after-tree | exit | status-before | status-after`. Receipt construction follows the explicit bootstrap/final/binding order above. Expected exits, labels, canonical unsalted fingerprints and mutation DSL never enter product checker input.

END_OF_FILE: os/engineering/V21-CONFORMANCE.md
