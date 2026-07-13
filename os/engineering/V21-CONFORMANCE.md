# v21 handoff conformance corpus

This file is the OS-owned fixture, phase-snapshot and mutation authority for contract v21. SETUP/RE-SYNC CALL-intent pins this file's git blob as `os-conformance-corpus-blob`, the SHA-256 of the exact JSON fence as `valid-specimen-hash`, and an independently reviewed stack adapter source/mode/blob. Product installer/checker code supplies none of that truth.

## Materializer and receipt contract

- UTF-8, LF, final LF. The JSON key/order/bytes are exactly as printed. `<computed:...>` expands only after its dependencies exist; the rendered external specimen/receipts never live in a commit whose id they contain.
- Writer creates a random disposable product root. It writes only fixed baseline files, commits B, renders external identity with B, commits packet-only P, test/oracle-only R, accepted build Q, result-bearing D, then archive-only A. Exact membership is below. No commit or product result self-hashes.
- For any canonical object, `inherits` means recursive copy of the named object, exact listed JSON-pointer `delete`, then `set`; no implicit merge/default is legal. `identity_ref` expands all identity keys; `toolchain_ref` expands root rows/manifest/corpus/profile/adapter/adapter-manifest fields; each `compiler_identity_ref|discover_identity_ref|runner_identity_ref` deep-copies the exact path/mode/blob/runtime/version/dependency-manifest-hash object at that toolchain pointer; `manifest_ref` expands ordered create/overlay rows; `testability_ref` materializes content and exact external pins; `light_ref` expands the complete light sentinel/conformance evidence. Every runnable snapshot names `call_intent_ref` and `writer_finalization_ref` directly or inherits them. Snapshot inheritance never carries a CALL object: after ordinary snapshot expansion, materializer injects `/call` exactly once as `FINALIZE(EXPAND(call_intent_ref), EXPAND(writer_finalization_ref))`. A canonical snapshot containing a literal `call` member or a `/call/**` `set` is invalid, so no second copy can supply, default or override a field. `FINALIZE` requires the finalization's `intent_ref` to equal the snapshot intent ref, copies the complete intent, replaces only `packet_stage`, and adds exactly the printed `writer_set` leaves; overlap other than `packet_stage`, omission, extra writer leaf or unresolved reference fails. Reference tokens are never passed. Adapter serializes the full finalized CALL and only the snapshot's declared handback projection into the canonical packet file and independently renders its authority file. Install verifies entry, applies only manifest, then runs on post-tree; siblings/future evidence never reach checker.
- Writer verifies adapter output, applies exactly one declared atomic semantic mutation plus mechanically dependent hash/receipt changes, and verifies before/after delta. Adapter writes one complete canonical packet file and one independent event-authority file, both writer-owned regular path/mode/blob. Closed environment is exactly `DIRECTION_PACKET_PATH|DIRECTION_PACKET_MODE|DIRECTION_PACKET_BLOB|DIRECTION_AUTHORITY_PATH|DIRECTION_AUTHORITY_MODE|DIRECTION_AUTHORITY_BLOB`, plus install-only `DIRECTION_CONFORMANCE_BOOTSTRAP_CHALLENGE`; no non-install receipt or authority value is copied into an environment variable, and no other variable exists. Product modes read all CALL/handback fields from packet bytes and all independently resolved Direction evidence from authority bytes. Writer snapshots exercise Direction transaction guard. Neither receives case/order/expected/root-purpose/corpus/mutation label. Roots, nonces and case order are randomized.
- Valid cases exit 0; every invalid expansion exits nonzero. Every mode is read-only: fixture/product status and tree hashes before/after the check are identical.

## Canonical bytes, salt and dependency order

`H(x)` is lowercase SHA-256 of exact UTF-8/LF bytes. `F(kind, fields...)` is `v21/` + kind + LF, then each field in the listed order as `name<TAB>utf8-byte-count<TAB>value<LF>`; repeated rows use zero-padded ordinal names. Values are never locale-sorted or implicitly trimmed. This framing is the only receipt serialization.

Writer creates a fresh 32-byte random nonce for every corpus run. `S(literal)` is the first 16 hex chars of `H(F("salt", nonce, literal))`. Keys, `<computed|external|salt:...>` tokens, git modes/hashes, phase/mode/status/visibility/record-kind values, config/result field names, system primitives, `stack_profile_authority` path/mode/bytes/blob/sha256, every adapter-output-manifest structural row/byte, and structural trust-root paths `validation.config|AGENTS.md|tools/plan-handoff-*|tools/fixture-*|tests/FixtureRunner.fixture|docs/results/{change-id}.md` are the complete reserved set. Every other JSON string value and graph path/content literal is neutral fixture data and receives suffix `-S(literal)`; identical literals share a value, replacements run longest-first before any blob/hash. Grammar prefixes `literal:|fixture:|slot:|reflection:|internal-friend:` stay fixed while identifier payloads salt. Numeric semantics are exact and preserve inequality: `k=1+(nonce[0] mod 3)`, `k2=k+1`, `n=k+7`; literal zero and face zero remain zero, while `literal:size-one`, `literal:unit-impulse`, `literal:source-two`, `literal:neighbor-seven` and all golden bytes expand from k/k2/n before blobs hash. Thus `k!=k2`, `n!=0`, and the three source-isolation cases cannot collapse under salting. Repo, branches, change/criterion/obligation/test ids, namespaces/types/members, fixture data and PublicApi/FixtureTests/ADR/oracle/result path segments also vary. `salt-map-hash=H(F("salt-map", ordered canonical->rendered rows))`. Two nonces must yield identical verdicts. A checker switching on neutral canonical/rendered fingerprint is a required failing meta-witness.

Canonical derived values, in dependency order:

1. Pin corpus blob, exact JSON-fence hash and `stack_profile_authority.path|mode|bytes|external blob|sha256`; `stack-profile-blob` is that exact external blob, not a nickname. Pin accepted interview/adapter event/path/mode/blob. The accepted adapter RESULT also pins `adapter_output_manifest.path|mode|bytes|blob|hash`; its printed rows must round-trip byte-for-byte, `adapter-output-manifest-hash=H(adapter_output_manifest.bytes)`, and those rows must equal the ordered projection of `toolchain.roots + toolchain.runtime_identity` with no extra/default row. Writer verifies every emitted byte against those rows before install or execution. Generate nonce, salt map and random roots. Materialize only exact named bytes below; B contains no receipt that cites B.
2. Git blobs use the repository object format; trees sort ordinal UTF-8 path/mode/blob rows. Every product commit in both valid graphs and invalid alternatives uses the same author/committer identity `Direction OS <direction-os@invalid>`, the same timestamp `2001-01-02T00:00:00Z`, and the same message `v21 specimen`; only exact parent list and tree determine its id. Node, phase, graph/mutation class, label, order and expected result never reach product git metadata or refs. Direction commits use the exact state bytes/parents/messages in the separate Direction graph below. The checker receives only the canonical event commit/path/mode/blob/payload rows in `AUTHORITY_BYTES`; Direction repo location, refs, config, commit message/timestamp and working tree never enter its cwd, args, environment or files.
3. `acceptance-hash=H(exact salted done_when bytes)`. Every `*-blob` is the repository blob id of exact named bytes; every `*-stdout-hash` is `H(exact named stdout bytes)`. Every binding source, runtime resource, generated test source, ABI packet/authority file and compiler output path printed in `testability` is a nonce-local scratch path `random-root + "/.v21/" + S(canonical-name)`; every `*-result-path` is instead the exact repo-relative filename printed after `history/` by its `direction_transactions.instances.event_path`, and it never enters the nonce namespace. Typed hashes are `H(F(kind, zero-padded ordinal exact rows))`; specifically `toolchain-manifest-hash` covers all root plus checker/schema/compiler/discover/runner path/mode/blob/runtime/version/dependency rows and the adapter-output-manifest path/mode/blob/hash; `binding-registry-hash` uses fully expanded registry nodes in printed order; and `expanded-source-set-hash` uses each recipe id/source path/mode/blob, every ordered compile-only `binding_sources` node/path/mode/blob, every separate runtime-resource node/path/mode/blob, expanded compiler/discover/runner identities, compile command/exit/stdout/output, discovery command/exit/count/ids/stdout and filtered run command/exit/status/criterion/stdout in recipe order, then the union source/compile-source/runtime-resource orders and full union compile/discovery/per-filter run observations. Patch hash is `H(F("overlay", path, pre-mode, pre-blob, post-mode, post-blob))`. TESTABILITY content excludes its external pin; pin is added only to CALL.
4. Intent bytes are canonical LF bytes of the exact complete schema-valid Markdown CALL for that phase before writer fields, with no writer-owned field; `intent-hash=H(those bytes)`. `FINALIZATION_IDENTITY_ROWS` is exact, never a grouped alias: SETUP/interview = `repo,worktree,profile-path,profile-mode,profile-blob,profile-sha256,requested-inventory`; SETUP/adapter-author = prior rows plus `interview-event-path,payload,adapter-path,adapter-mode,required-manifest-schema,corpus-blob,specimen-hash`; SETUP/adapter-review = prior profile/corpus rows plus full interview event, pending author path/payload, adapter path/mode/blob and manifest path/mode/blob/hash; SETUP/install = full interview+author events, pending review path/payload, full profile/adapter/manifest authority, every install row and inventory; RE-SYNC = branch/base-authority/base, full interview+author events, pending review path/payload, full profile/adapter/manifest authority and every install row; PLAN/author = branch/base/acceptance/change/result, full toolchain+TESTABILITY and pending conformance path/payload/receipt; PLAN/verdict = the immutable PLAN rows plus full conformance event, candidate/plan receipt and pending plan-event path/payload; EXECUTE/frozen = the immutable PLAN rows plus full conformance+plan events and pending owner-event path/payload; EXECUTE/coordinated-light = branch/base/acceptance/change/result, full toolchain, exact light scan/config and pending light-conformance path/payload/receipt; BUILD/resume/frozen = all frozen EXECUTE identities with full owner event, run/pre-RED/pre-exec, original RED event+manifest, every accepted revision event+manifest, and pending progress path/payload/commit/ledger; BUILD/resume/coordinated-light = every light EXECUTE identity plus full light-conformance event, light run/pre-exec and pending progress path/payload/commit/ledger. Deliver and close are terminal read-only `gate_mode` observations and handback projections inside the same immutable finalized BUILD CALL: `/call/phase` remains `BUILD`, `execution_mode` remains `resume`, CALL observed HEAD remains its entry progress commit, and D/A/current result/archive observations exist only under handback. No new phase receipt is invented. `finalization-receipt=H(F("finalize", intent-hash, worktree, phase, exact substage-or-literal-n/a, each scalar row from this exact phase/substage list in printed order, pre-status-hash))`.
5. Observation rows are exact: install=`tools/plan-handoff-check.fixture install`, plan-entry=`... plan-entry`, plan=`... plan`, pre-execution=`... pre-execution`, red-boundary=`... red-boundary`, resume=`... resume`, deliver=`... deliver`, close=`... close`; status is `clean:<HEAD>` except SETUP pre-status=`inventory:<inventory-hash>`. `writer-observation-hash=H(F("observe", exact-command, decimal-exit, status-before-hash, status-after-hash))`. No command, status, identity or order is inferred.
6. Scalar aliases are exact JSON paths after reference expansion: `toolchain-manifest-hash=/toolchain/manifest_hash`; `testability-mode=/testability_pin/mode`; `testability-blob=/testability_pin/blob`; `input-manifest-hash=/testability_pin/input_manifest_hash`; `plan-receipt-event=/call/plan_receipt_event`; `plan-receipt=/call/plan_receipt`; `owner-verdict-event=/call/owner_verdict_event`; `red-event=/call/red_event`; `progress-event=/call/progress_event`; `progress-ledger-path|mode|blob=/call/progress_ledger_path|mode|blob`. No slash-joined logical alias is a scalar. `plan-receipt=H(F("plan", candidate-head, base-authority, acceptance-hash, toolchain-manifest-hash, validation-conformance-receipt, testability-mode, testability-blob, input-manifest-hash, binding-registry-hash, expanded-source-set-hash, plan-observation-hash))`. `run-id=H(F("run", plan-receipt-event, candidate-head, base-authority, acceptance-hash))`. `preexec-receipt=H(F("preexec", run-id, pre-red-head, plan-receipt-event, plan-receipt, owner-verdict-event, toolchain-manifest-hash, testability-mode, testability-blob, input-manifest-hash, acceptance-hash, preexec-observation-hash))`. `progress-receipt` has two exact variants: frozen=`H(F("progress",run-id,progress-commit,progress-ledger-path,progress-ledger-mode,progress-ledger-blob,red-event,writer-observation-hash))`; coordinated-light=`H(F("progress",light-run-id,progress-commit,progress-ledger-path,progress-ledger-mode,progress-ledger-blob,literal:n/a,writer-observation-hash))`. Routing recovery bytes are exactly `<deliver-commit>|<product-result-path>|<result-blob><LF>` and `routing-output-hash=H(those bytes)`; D rerun and A derivation must return identical bytes/hash.
7. Install challenge is `H(F("challenge", nonce, target-root))`. Bootstrap receipt hashes challenge, corpus/specimen/salt/adapter identities and the exact ordered install result rows. Final conformance receipt hashes bootstrap receipt and exact ordered non-install rows. Row order is the literal expanded valid/invalid-case order below; an `EACH` expansion is in its declared ordinal list. Each row is `F("case", salt-map-hash, mutation-digest, adapter-event, adapter-mode, adapter-blob, specimen-hash, packet-blob, authority-blob, before-tree, after-tree, decimal-exit, status-before, status-after)`. Final binding smoke uses final receipt/event and is excluded from its own preimage.
8. Computed-token grammar is closed. Token scanning applies only to JSON string leaves and the right-hand sides of the two exact `text` fences after macro expansion; prose and this grammar sentence are not scanner input. A computed token is legal only when its name is: a product or Direction graph node explicitly named below; one of `random-root|packet-path|authority-path|stack-id|adapter-author-session|adapter-review-session|installer-session|run-id|light-run-id|k|k2|n`; `*-blob`/`*-stdout-hash` for exact named/canonical bytes; a binding/source/resource/output scratch path printed in `testability`; a `*-result-path` equal to one printed instance history basename, plus the declared disposable `bootstrap-conformance-result-path`; a named scalar ending `-receipt|-hash|-run-id|-challenge`; or a negative disposable node/object explicitly named in one mutation row (`RB-parent|Q-unaccepted|foreign-Q|foreign-writer-commit|changed-adapter-blob|outside-root|outside-link-target-bytes|disposable-gitlink-commit|runtime-path|result-self`). Angle variables such as `<snapshot>`, `<ordinal>` and `<path>` exist only inside declared expansion/formula macros and are replaced before token scanning and hashing. Any other token, read-before-dependency, grouped slash alias, implicit timestamp, unknown path class or adapter default is materialization failure.

For every non-Direction-only snapshot, `PACKET_BYTES(snapshot)=F("packet-v21", schema=1, snapshot, gate-mode, transaction-stage from the disjoint `abi_contract.entry_snapshots|gate_snapshots|return_snapshots`, exact `FINALIZED_ENGINEERING_CALL_BYTES(EXPAND(snapshot.call_intent_ref),snapshot.writer_finalization_ref)`, product-observation, exact handback projection named by that snapshot, result-presence=`n/a|required`, and `n/a|exact FULL_RESULT_HISTORY_BYTES`)`. Entry and internal gate have result-presence/result-history `n/a`; only return requires the exact `abi_contract.return_result_ref[snapshot]` full RESULT history with trailer. Deliver is an internal gate at D and close is the terminal return at A (or the same LD tree for light); a crash before terminal RESULT leaves the same open BUILD CALL recoverable. A gate/return never rewrites the entry CALL: PLAN candidate, RED/revision, D/result and A/archive facts are handback only. No inherited snapshot field outside its printed projection enters the wrapper. `AUTHORITY_BYTES(snapshot)=F("authority-v21", each of the eight fixed `abi_contract.authority_slot_order` rows)`, where every row is exactly `slot<TAB>path|mode|history-blob|strict-ancestor-commit|semantic-payload-hash` when listed in that snapshot's `authority_required`, otherwise literal `slot<TAB>n/a`; omission, defaulting, a required `n/a`, or a populated N/A slot fails. Writer creates packet/authority ABI scratch paths inside the declared nonce-local ABI scratch class, mode 100644, hashes both files before and after, and passes their exact blob ids in the six ABI variables. The checker compares CALL/handback claims to independently rendered authority rows and never treats a packet claim as authority. Packet or authority bytes never live in product git.

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
    "done_when": "DW-1 absent Create exact result\nDW-2 existing Step loopback once\nDW-3 source-isolated golden audit\n",
    "acceptance_hash": "<computed:acceptance-hash>",
    "change_id": "v21-fixture-change",
    "product_result_path": "docs/results/v21-fixture-change.md"
  },
  "identity_stable_ref": {
    "inherits": "identity",
    "set": {
      "base_authority": "ref:origin/main@<computed:B>"
    },
    "external_ref_map": {
      "origin/main": "<computed:B>"
    }
  },
  "stack_profile_authority": {
    "path": "os/engineering/profiles/fixture.md",
    "mode": "100644",
    "bytes": "stack: fixture\ncompiler: fixture-compiler version 1\ndiscovery: fixture-discover version 1\nrunner: fixture-runner version 1\n",
    "blob": "<external:stack-profile-blob>",
    "sha256": "<external:stack-profile-sha256>"
  },
  "adapter_output_manifest": {
    "path": "work/validation-adapters/<computed:stack-id>-v21.manifest",
    "mode": "100644",
    "rows": [
      {
        "path": "validation.config",
        "mode": "100644",
        "blob": "<computed:config-blob>",
        "runtime": "data",
        "version": "1",
        "dependency_manifest_hash": "<computed:config-dependency-manifest-hash>"
      },
      {
        "path": "tools/plan-handoff-check.fixture",
        "mode": "100644",
        "blob": "<computed:checker-blob>",
        "runtime": "fixture-checker",
        "version": "21",
        "dependency_manifest_hash": "<computed:checker-dependency-manifest-hash>"
      },
      {
        "path": "tools/plan-handoff-schema.fixture",
        "mode": "100644",
        "blob": "<computed:schema-blob>",
        "runtime": "fixture-schema",
        "version": "21",
        "dependency_manifest_hash": "<computed:schema-dependency-manifest-hash>"
      },
      {
        "path": "tools/fixture-compiler.fixture",
        "mode": "100755",
        "blob": "<computed:fixture-compiler-blob>",
        "runtime": "fixture-compiler",
        "version": "1",
        "dependency_manifest_hash": "<computed:compiler-dependency-manifest-hash>"
      },
      {
        "path": "tools/fixture-discover.fixture",
        "mode": "100755",
        "blob": "<computed:fixture-discover-blob>",
        "runtime": "fixture-discover",
        "version": "1",
        "dependency_manifest_hash": "<computed:discover-dependency-manifest-hash>"
      },
      {
        "path": "tests/FixtureRunner.fixture",
        "mode": "100755",
        "blob": "<computed:test-runner-blob>",
        "runtime": "fixture-runner",
        "version": "1",
        "dependency_manifest_hash": "<computed:runner-dependency-manifest-hash>"
      }
    ],
    "bytes_ref": "ADAPTER_OUTPUT_MANIFEST_BYTES",
    "blob": "<computed:adapter-output-manifest-blob>",
    "hash": "<computed:adapter-output-manifest-hash>"
  },
  "toolchain": {
    "roots": [
      {
        "path": "validation.config",
        "mode": "100644",
        "blob": "<computed:config-blob>"
      },
      {
        "path": "tools/plan-handoff-check.fixture",
        "mode": "100644",
        "blob": "<computed:checker-blob>"
      },
      {
        "path": "tools/plan-handoff-schema.fixture",
        "mode": "100644",
        "blob": "<computed:schema-blob>"
      },
      {
        "path": "tools/fixture-compiler.fixture",
        "mode": "100755",
        "blob": "<computed:fixture-compiler-blob>"
      },
      {
        "path": "tools/fixture-discover.fixture",
        "mode": "100755",
        "blob": "<computed:fixture-discover-blob>"
      },
      {
        "path": "tests/FixtureRunner.fixture",
        "mode": "100755",
        "blob": "<computed:test-runner-blob>"
      }
    ],
    "manifest_hash": "<computed:toolchain-manifest-hash>",
    "adapter_output_manifest_hash": "<computed:adapter-output-manifest-hash>",
    "runtime_identity": {
      "checker": {
        "path": "tools/plan-handoff-check.fixture",
        "mode": "100644",
        "blob": "<computed:checker-blob>",
        "runtime": "fixture-checker",
        "version": "21",
        "dependency_manifest_hash": "<computed:checker-dependency-manifest-hash>"
      },
      "schema": {
        "path": "tools/plan-handoff-schema.fixture",
        "mode": "100644",
        "blob": "<computed:schema-blob>",
        "runtime": "fixture-schema",
        "version": "21",
        "dependency_manifest_hash": "<computed:schema-dependency-manifest-hash>"
      },
      "compiler": {
        "path": "tools/fixture-compiler.fixture",
        "mode": "100755",
        "blob": "<computed:fixture-compiler-blob>",
        "runtime": "fixture-compiler",
        "version": "1",
        "dependency_manifest_hash": "<computed:compiler-dependency-manifest-hash>"
      },
      "discover": {
        "path": "tools/fixture-discover.fixture",
        "mode": "100755",
        "blob": "<computed:fixture-discover-blob>",
        "runtime": "fixture-discover",
        "version": "1",
        "dependency_manifest_hash": "<computed:discover-dependency-manifest-hash>"
      },
      "runner": {
        "path": "tests/FixtureRunner.fixture",
        "mode": "100755",
        "blob": "<computed:test-runner-blob>",
        "runtime": "fixture-runner",
        "version": "1",
        "dependency_manifest_hash": "<computed:runner-dependency-manifest-hash>"
      }
    },
    "corpus_blob": "<external:this-file-git-blob>",
    "specimen_hash": "<external:this-json-sha256>",
    "stack_profile_path": "os/engineering/profiles/fixture.md",
    "stack_profile_mode": "100644",
    "stack_profile_blob": "<external:stack-profile-blob>",
    "stack_profile_sha256": "<external:stack-profile-sha256>",
    "adapter_author_event": "history/adapter-author-result.md@<computed:I-adapter-author-result>",
    "adapter_event": "history/<computed:adapter-review-result-path>@<computed:I-adapter-accept>",
    "adapter_source": "work/validation-adapters/<computed:stack-id>-v21.fixture",
    "adapter_mode": "100644",
    "adapter_blob": "<computed:accepted-adapter-blob>",
    "adapter_output_manifest_path": "work/validation-adapters/<computed:stack-id>-v21.manifest",
    "adapter_output_manifest_mode": "100644",
    "adapter_output_manifest_blob": "<computed:adapter-output-manifest-blob>",
    "adapter_author_session": "<computed:adapter-author-session>",
    "adapter_review_session": "<computed:adapter-review-session>",
    "adapter_review_verdict": "GREEN",
    "installer_session": "<computed:installer-session>"
  },
  "toolchain_resync": {
    "inherits": "toolchain",
    "set": {
      "adapter_event": "history/<computed:adapter-review-resync-result-path>@<computed:I-resync-adapter-accept>"
    }
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
    "binding_registry_hash": "<computed:binding-registry-hash>",
    "expanded_source_set_hash": "<computed:expanded-source-set-hash>",
    "coverage": [
      {
        "ordinal": 0,
        "done_when_bytes": "DW-1 absent Create exact result\n",
        "obligations": [
          "OB-1"
        ]
      },
      {
        "ordinal": 1,
        "done_when_bytes": "DW-2 existing Step loopback once\n",
        "obligations": [
          "OB-2"
        ]
      },
      {
        "ordinal": 2,
        "done_when_bytes": "DW-3 source-isolated golden audit\n",
        "obligations": [
          "OB-3"
        ]
      }
    ],
    "manifest": [
      {
        "kind": "packet",
        "path": "openspec/changes/v21-fixture-change/proposal.md",
        "mode": "100644",
        "blob": "<computed:proposal-blob>"
      },
      {
        "kind": "packet",
        "path": "openspec/changes/v21-fixture-change/PLAN.md",
        "mode": "100644",
        "blob": "<computed:plan-blob>"
      },
      {
        "kind": "packet",
        "path": "openspec/changes/v21-fixture-change/tasks.md",
        "mode": "100644",
        "blob": "<computed:tasks-blob>"
      },
      {
        "kind": "packet",
        "path": "openspec/changes/v21-fixture-change/specs/core/spec.md",
        "mode": "100644",
        "blob": "<computed:spec-blob>"
      },
      {
        "kind": "authority",
        "path": "docs/adr/ADR-v21-fixture.md",
        "mode": "100644",
        "blob": "<computed:adr-blob>"
      },
      {
        "kind": "baseline",
        "base": "<computed:B>",
        "path": "src/PublicApi.fixture",
        "mode": "100644",
        "blob": "<computed:base-api-blob>"
      },
      {
        "kind": "baseline",
        "base": "<computed:B>",
        "path": "tests/Fixture.Tests.project",
        "mode": "100644",
        "blob": "<computed:test-project-blob>"
      },
      {
        "kind": "baseline",
        "base": "<computed:B>",
        "path": "tests/FixtureFriendAssembly.fixture",
        "mode": "100644",
        "blob": "<computed:friend-assembly-blob>"
      },
      {
        "kind": "baseline",
        "base": "<computed:B>",
        "path": "tests/FixtureRunner.fixture",
        "mode": "100755",
        "blob": "<computed:test-runner-blob>"
      }
    ],
    "binding_registry": [
      {
        "id": "literal:size-one",
        "kind": "literal",
        "type": "System.Int32",
        "encoding": "utf8-decimal",
        "bytes": "<computed:k>",
        "depends_on": []
      },
      {
        "id": "literal:zero",
        "kind": "literal",
        "type": "System.Int32",
        "encoding": "utf8-decimal",
        "bytes": "0",
        "depends_on": []
      },
      {
        "id": "literal:open-face",
        "kind": "literal",
        "type": "Fixture.FaceKind",
        "encoding": "fq-enum",
        "bytes": "Fixture.FaceKind.Open",
        "depends_on": []
      },
      {
        "id": "literal:sealed-face",
        "kind": "literal",
        "type": "Fixture.FaceKind",
        "encoding": "fq-enum",
        "bytes": "Fixture.FaceKind.Sealed",
        "depends_on": []
      },
      {
        "id": "literal:face-zero",
        "kind": "literal",
        "type": "Fixture.FaceId",
        "encoding": "fq-constructor",
        "bytes": "Fixture.FaceId(0)",
        "depends_on": []
      },
      {
        "id": "literal:unit-impulse",
        "kind": "literal",
        "type": "System.Int32",
        "encoding": "utf8-decimal",
        "bytes": "<computed:k>",
        "depends_on": []
      },
      {
        "id": "literal:semantic-fault",
        "kind": "literal",
        "type": "FixtureFaultKind",
        "encoding": "fq-enum",
        "bytes": "FixtureFaultKind.Semantic",
        "depends_on": []
      },
      {
        "id": "fixture:two-room-open-sealed-faces",
        "kind": "producer",
        "type": "Fixture.Topology",
        "signature": "Fixture.Topology.TwoRoom(Fixture.FaceKind,Fixture.FaceKind)",
        "visibility": "public",
        "owner": "Fixture.Topology",
        "args": [
          {
            "name": "left",
            "type": "Fixture.FaceKind",
            "source": "literal:open-face"
          },
          {
            "name": "right",
            "type": "Fixture.FaceKind",
            "source": "literal:sealed-face"
          }
        ],
        "depends_on": [
          "literal:open-face",
          "literal:sealed-face"
        ]
      },
      {
        "id": "fixture:single-cell-topology",
        "kind": "producer",
        "type": "Fixture.Topology",
        "signature": "Fixture.Topology.SingleCell()",
        "visibility": "public",
        "owner": "Fixture.Topology",
        "args": [],
        "depends_on": []
      },
      {
        "id": "fixture:face-impulse",
        "kind": "producer",
        "type": "Fixture.Impulse",
        "signature": "Fixture.Impulse.AtFace(Fixture.FaceId,System.Int32)",
        "visibility": "public",
        "owner": "Fixture.Impulse",
        "args": [
          {
            "name": "face",
            "type": "Fixture.FaceId",
            "source": "literal:face-zero"
          },
          {
            "name": "amount",
            "type": "System.Int32",
            "source": "literal:unit-impulse"
          }
        ],
        "depends_on": [
          "literal:face-zero",
          "literal:unit-impulse"
        ]
      },
      {
        "id": "fixture:source-isolated-input",
        "kind": "producer",
        "type": "Fixture.SourceInput",
        "signature": "Fixture.SourceInput.Single(Fixture.FaceId,System.Int32,System.Int32)",
        "visibility": "public",
        "owner": "Fixture.SourceInput",
        "args": [
          {
            "name": "face",
            "type": "Fixture.FaceId",
            "source": "literal:face-zero"
          },
          {
            "name": "source",
            "type": "System.Int32",
            "source": "literal:unit-impulse"
          },
          {
            "name": "neighbor",
            "type": "System.Int32",
            "source": "literal:zero"
          }
        ],
        "depends_on": [
          "literal:face-zero",
          "literal:unit-impulse",
          "literal:zero"
        ]
      },
      {"id":"fixture:golden-cell-result","kind":"runtime-resource","type":"Fixture.CellResult","path":"<computed:golden-cell-path>","mode":"100644","bytes":"cell=<computed:k>;counter=1;hidden=0\n","blob":"<computed:golden-cell-blob>","depends_on":[]},
      {"id":"fixture:fault-probe-contract-source","kind":"test-local-source","declares":["Fixture.Tests.NegativePhase","Fixture.Tests.FaultProbe"],"path":"<computed:fault-probe-contract-path>","mode":"100644","bytes":"enum Fixture.Tests.NegativePhase { None, Before, During, After }\ninterface Fixture.Tests.FaultProbe implements Fixture.ReactionHandler { ExpectedPhase():Fixture.Tests.NegativePhase; ObservedPhase():Fixture.Tests.NegativePhase; }\n","blob":"<computed:fault-probe-contract-blob>","depends_on":[]},
      {"id":"fixture:owned-handler-source","kind":"test-local-source","declares":["Fixture.Tests.OwnedHandler"],"path":"<computed:owned-handler-path>","mode":"100644","bytes":"sealed Fixture.Tests.OwnedHandler implements Fixture.ReactionHandler; ctor(Fixture.Core owner){this.owner=owner;} field owner:Fixture.Core; field calls:System.Int32=0; Owner():Fixture.Core{return owner;} CallCount():System.Int32{return calls;} OnReaction(Fixture.Core owner,Fixture.Impulse impulse){require ReferenceEquals(owner,this.owner); calls+=1;}\n","blob":"<computed:owned-handler-blob>","depends_on":[]},
      {"id":"fixture:loopback-source","kind":"test-local-source","declares":["Fixture.Tests.LoopbackOnce"],"path":"<computed:loopback-handler-path>","mode":"100644","bytes":"sealed Fixture.Tests.LoopbackOnce implements Fixture.ReactionHandler; ctor(); field calls:System.Int32=0; field delegations:System.Int32=0; CallCount():System.Int32{return calls;} DelegationCount():System.Int32{return delegations;} OnReaction(Fixture.Core owner,Fixture.Impulse impulse){calls+=1; if delegations==0 {delegations+=1; owner.Step(impulse,this);}}\n","blob":"<computed:loopback-handler-blob>","depends_on":[]},
      {"id":"fixture:throw-before-source","kind":"test-local-source","declares":["Fixture.Tests.ThrowBefore"],"path":"<computed:throw-before-path>","mode":"100644","bytes":"sealed Fixture.Tests.ThrowBefore implements Fixture.Tests.FaultProbe; ctor(); field observed:Fixture.Tests.NegativePhase=Fixture.Tests.NegativePhase.None; ExpectedPhase():Fixture.Tests.NegativePhase{return Fixture.Tests.NegativePhase.Before;} ObservedPhase():Fixture.Tests.NegativePhase{return observed;} OnReaction(Fixture.Core owner,Fixture.Impulse impulse){observed=Fixture.Tests.NegativePhase.Before; throw before-delegate;}\n","blob":"<computed:throw-before-blob>","depends_on":["fixture:fault-probe-contract-source"]},
      {"id":"fixture:throw-during-source","kind":"test-local-source","declares":["Fixture.Tests.ThrowDuring"],"path":"<computed:throw-during-path>","mode":"100644","bytes":"sealed Fixture.Tests.ThrowDuring implements Fixture.Tests.FaultProbe; ctor(); field delegations:System.Int32=0; field observed:Fixture.Tests.NegativePhase=Fixture.Tests.NegativePhase.None; ExpectedPhase():Fixture.Tests.NegativePhase{return Fixture.Tests.NegativePhase.During;} ObservedPhase():Fixture.Tests.NegativePhase{return observed;} OnReaction(Fixture.Core owner,Fixture.Impulse impulse){if delegations>0 {observed=Fixture.Tests.NegativePhase.During; throw during-delegate;} delegations+=1; owner.Step(impulse,this);}\n","blob":"<computed:throw-during-blob>","depends_on":["fixture:fault-probe-contract-source"]},
      {"id":"fixture:throw-after-source","kind":"test-local-source","declares":["Fixture.Tests.ThrowAfter"],"path":"<computed:throw-after-path>","mode":"100644","bytes":"sealed Fixture.Tests.ThrowAfter implements Fixture.Tests.FaultProbe; ctor(); field delegations:System.Int32=0; field observed:Fixture.Tests.NegativePhase=Fixture.Tests.NegativePhase.None; ExpectedPhase():Fixture.Tests.NegativePhase{return Fixture.Tests.NegativePhase.After;} ObservedPhase():Fixture.Tests.NegativePhase{return observed;} OnReaction(Fixture.Core owner,Fixture.Impulse impulse){if delegations>0 {return;} delegations+=1; owner.Step(impulse,this); observed=Fixture.Tests.NegativePhase.After; throw after-delegate;}\n","blob":"<computed:throw-after-blob>","depends_on":["fixture:fault-probe-contract-source"]},
      {"id":"fixture:golden-comparator-source","kind":"test-local-source","declares":["Fixture.Tests.Golden"],"path":"<computed:golden-comparator-path>","mode":"100644","bytes":"sealed Fixture.Tests.Golden; ctor(); Compare(Fixture.AuditResult actual,Fixture.CellResult expected):System.Boolean{return actual.cell==expected.cell and actual.counter==expected.counter and actual.hidden==expected.hidden;} AuditEqual(Fixture.AuditResult left,Fixture.AuditResult right):System.Boolean{return left.cell==right.cell and left.counter==right.counter and left.hidden==right.hidden;} ReferenceEqual(System.Object left,System.Object right):System.Boolean{return ReferenceEquals(left,right);}\n","blob":"<computed:golden-comparator-blob>","depends_on":[]},
      {"id":"fixture:owned-custom-handler","kind":"instance","type":"Fixture.Tests.OwnedHandler","constructor":"Fixture.Tests.OwnedHandler(Fixture.Core)","args":[{"name":"owner","type":"Fixture.Core","source":"slot:ob1-core"}],"depends_on":["fixture:owned-handler-source","slot:ob1-core"]},
      {"id":"fixture:owned-handler-owner","kind":"callable","signature":"Fixture.Tests.OwnedHandler.Owner()","receiver":"fixture:owned-custom-handler","visibility":"test-local","owner":"Fixture.Tests.OwnedHandler","args":[],"returns":"Fixture.Core","depends_on":["fixture:owned-custom-handler"]},
      {"id":"fixture:owned-handler-call-count","kind":"callable","signature":"Fixture.Tests.OwnedHandler.CallCount()","receiver":"fixture:owned-custom-handler","visibility":"test-local","owner":"Fixture.Tests.OwnedHandler","args":[],"returns":"System.Int32","depends_on":["fixture:owned-custom-handler"]},
      {"id":"fixture:loopback-delegates-once","kind":"instance","type":"Fixture.Tests.LoopbackOnce","constructor":"Fixture.Tests.LoopbackOnce()","args":[],"depends_on":["fixture:loopback-source"]},
      {"id":"fixture:loopback-call-count","kind":"callable","signature":"Fixture.Tests.LoopbackOnce.CallCount()","receiver":"fixture:loopback-delegates-once","visibility":"test-local","owner":"Fixture.Tests.LoopbackOnce","args":[],"returns":"System.Int32","depends_on":["fixture:loopback-delegates-once"]},
      {"id":"fixture:loopback-delegation-count","kind":"callable","signature":"Fixture.Tests.LoopbackOnce.DelegationCount()","receiver":"fixture:loopback-delegates-once","visibility":"test-local","owner":"Fixture.Tests.LoopbackOnce","args":[],"returns":"System.Int32","depends_on":["fixture:loopback-delegates-once"]},
      {"id":"fixture:throw-before","kind":"instance","type":"Fixture.Tests.ThrowBefore","constructor":"Fixture.Tests.ThrowBefore()","args":[],"depends_on":["fixture:throw-before-source"]},
      {"id":"fixture:throw-during","kind":"instance","type":"Fixture.Tests.ThrowDuring","constructor":"Fixture.Tests.ThrowDuring()","args":[],"depends_on":["fixture:throw-during-source"]},
      {"id":"fixture:throw-after","kind":"instance","type":"Fixture.Tests.ThrowAfter","constructor":"Fixture.Tests.ThrowAfter()","args":[],"depends_on":["fixture:throw-after-source"]},
      {"id":"fixture:throw-before-expected","kind":"callable","signature":"Fixture.Tests.ThrowBefore.ExpectedPhase()","receiver":"fixture:throw-before","visibility":"test-local","owner":"Fixture.Tests.ThrowBefore","args":[],"returns":"Fixture.Tests.NegativePhase","depends_on":["fixture:throw-before"]},
      {"id":"fixture:throw-before-observed","kind":"callable","signature":"Fixture.Tests.ThrowBefore.ObservedPhase()","receiver":"fixture:throw-before","visibility":"test-local","owner":"Fixture.Tests.ThrowBefore","args":[],"returns":"Fixture.Tests.NegativePhase","depends_on":["fixture:throw-before"]},
      {"id":"fixture:throw-during-expected","kind":"callable","signature":"Fixture.Tests.ThrowDuring.ExpectedPhase()","receiver":"fixture:throw-during","visibility":"test-local","owner":"Fixture.Tests.ThrowDuring","args":[],"returns":"Fixture.Tests.NegativePhase","depends_on":["fixture:throw-during"]},
      {"id":"fixture:throw-during-observed","kind":"callable","signature":"Fixture.Tests.ThrowDuring.ObservedPhase()","receiver":"fixture:throw-during","visibility":"test-local","owner":"Fixture.Tests.ThrowDuring","args":[],"returns":"Fixture.Tests.NegativePhase","depends_on":["fixture:throw-during"]},
      {"id":"fixture:throw-after-expected","kind":"callable","signature":"Fixture.Tests.ThrowAfter.ExpectedPhase()","receiver":"fixture:throw-after","visibility":"test-local","owner":"Fixture.Tests.ThrowAfter","args":[],"returns":"Fixture.Tests.NegativePhase","depends_on":["fixture:throw-after"]},
      {"id":"fixture:throw-after-observed","kind":"callable","signature":"Fixture.Tests.ThrowAfter.ObservedPhase()","receiver":"fixture:throw-after","visibility":"test-local","owner":"Fixture.Tests.ThrowAfter","args":[],"returns":"Fixture.Tests.NegativePhase","depends_on":["fixture:throw-after"]},
      {"id":"fixture:golden-comparator","kind":"instance","type":"Fixture.Tests.Golden","constructor":"Fixture.Tests.Golden()","args":[],"depends_on":["fixture:golden-comparator-source"]},
      {"id":"fixture:golden-compare","kind":"callable","signature":"Fixture.Tests.Golden.Compare(Fixture.AuditResult,Fixture.CellResult)","receiver":"fixture:golden-comparator","visibility":"test-local","owner":"Fixture.Tests.Golden","args":[{"name":"actual","type":"Fixture.AuditResult"},{"name":"expected","type":"Fixture.CellResult"}],"returns":"System.Boolean","depends_on":["fixture:golden-comparator"]},
      {"id":"fixture:golden-audit-equal","kind":"callable","signature":"Fixture.Tests.Golden.AuditEqual(Fixture.AuditResult,Fixture.AuditResult)","receiver":"fixture:golden-comparator","visibility":"test-local","owner":"Fixture.Tests.Golden","args":[{"name":"left","type":"Fixture.AuditResult"},{"name":"right","type":"Fixture.AuditResult"}],"returns":"System.Boolean","depends_on":["fixture:golden-comparator"]},
      {"id":"fixture:golden-reference-equal","kind":"callable","signature":"Fixture.Tests.Golden.ReferenceEqual(System.Object,System.Object)","receiver":"fixture:golden-comparator","visibility":"test-local","owner":"Fixture.Tests.Golden","args":[{"name":"left","type":"System.Object"},{"name":"right","type":"System.Object"}],"returns":"System.Boolean","depends_on":["fixture:golden-comparator"]},
      {"id":"fixture:fault-selector","kind":"callable","signature":"FixtureFault.Select(FixtureFaultKind)","visibility":"internal-friend:Fixture.Tests","owner":"operation:Step","args":[{"name":"kind","type":"FixtureFaultKind","source":"literal:semantic-fault"}],"returns":"FixtureFault","depends_on":["literal:semantic-fault"]},
      {
        "id": "fixture:audit-reader",
        "kind": "producer",
        "type": "Fixture.Audit",
        "signature": "Fixture.Audit.For(Fixture.Core)",
        "visibility": "internal-friend:Fixture.Tests",
        "owner": "Fixture.Audit",
        "args": [
          {
            "name": "core",
            "type": "Fixture.Core",
            "source": "slot:ob1-core"
          }
        ],
        "depends_on": [
          "slot:ob1-core"
        ]
      },
      {
        "id": "fixture:existing-core",
        "kind": "producer",
        "type": "Fixture.Core",
        "signature": "Fixture.Core.Existing(Fixture.Topology)",
        "visibility": "public",
        "owner": "Fixture.Core",
        "args": [
          {
            "name": "topology",
            "type": "Fixture.Topology",
            "source": "fixture:single-cell-topology"
          }
        ],
        "depends_on": [
          "fixture:single-cell-topology"
        ]
      },
      {
        "id": "slot:ob1-core",
        "kind": "slot",
        "type": "Fixture.Core",
        "producer": "OB-1.construct",
        "lifetime": "test",
        "owner": "OB-1",
        "depends_on": [
          "fixture:two-room-open-sealed-faces"
        ]
      },
      {
        "id": "slot:ob1-step",
        "kind": "slot",
        "type": "Fixture.StepResult",
        "producer": "OB-1.act",
        "lifetime": "test",
        "owner": "OB-1",
        "depends_on": [
          "slot:ob1-core",
          "fixture:face-impulse",
          "fixture:owned-custom-handler"
        ]
      },
      {
        "id": "slot:ob1-audit",
        "kind": "slot",
        "type": "Fixture.AuditResult",
        "producer": "OB-1.observe",
        "lifetime": "assertion",
        "owner": "OB-1",
        "depends_on": [
          "fixture:audit-reader"
        ]
      },
      {
        "id": "slot:ob1-fault",
        "kind": "slot",
        "type": "FixtureFault",
        "producer": "OB-1.negative",
        "lifetime": "operation",
        "owner": "OB-1",
        "depends_on": [
          "literal:semantic-fault"
        ]
      },
      {
        "id": "slot:ob2-core",
        "kind": "slot",
        "type": "Fixture.Core",
        "producer": "OB-2.construct",
        "lifetime": "test",
        "owner": "OB-2",
        "depends_on": [
          "fixture:existing-core"
        ]
      },
      {
        "id": "slot:ob2-step",
        "kind": "slot",
        "type": "Fixture.StepResult",
        "producer": "OB-2.act",
        "lifetime": "test",
        "owner": "OB-2",
        "depends_on": [
          "slot:ob2-core",
          "fixture:loopback-delegates-once"
        ]
      },
      {
        "id": "slot:ob2-value",
        "kind": "slot",
        "type": "System.Int32",
        "producer": "OB-2.observe",
        "lifetime": "assertion",
        "owner": "OB-2",
        "depends_on": [
          "slot:ob2-core"
        ]
      },
      {"id":"slot:ob3-core-zero","kind":"slot","type":"Fixture.Core","producer":"OB-3.construct-zero","lifetime":"test","owner":"OB-3","depends_on":["fixture:existing-core"]},
      {"id":"slot:ob3-core-neighbor","kind":"slot","type":"Fixture.Core","producer":"OB-3.construct-neighbor","lifetime":"test","owner":"OB-3","depends_on":["fixture:existing-core"]},
      {"id":"slot:ob3-core-source-two","kind":"slot","type":"Fixture.Core","producer":"OB-3.construct-source-two","lifetime":"test","owner":"OB-3","depends_on":["fixture:existing-core"]},
      {"id":"slot:ob3-step-zero","kind":"slot","type":"Fixture.StepResult","producer":"OB-3.act-zero","lifetime":"test","owner":"OB-3","depends_on":["slot:ob3-core-zero","fixture:source-isolated-input"]},
      {"id":"slot:ob3-step-neighbor","kind":"slot","type":"Fixture.StepResult","producer":"OB-3.act-neighbor","lifetime":"test","owner":"OB-3","depends_on":["slot:ob3-core-neighbor","fixture:source-same-neighbor-seven"]},
      {"id":"slot:ob3-step-source-two","kind":"slot","type":"Fixture.StepResult","producer":"OB-3.act-source-two","lifetime":"test","owner":"OB-3","depends_on":["slot:ob3-core-source-two","fixture:source-two-neighbor-zero"]},
      {"id":"slot:ob3-audit-zero","kind":"slot","type":"Fixture.AuditResult","producer":"OB-3.observe-zero","lifetime":"assertion","owner":"OB-3","depends_on":["slot:ob3-core-zero"]},
      {"id":"slot:ob3-audit-neighbor","kind":"slot","type":"Fixture.AuditResult","producer":"OB-3.observe-neighbor","lifetime":"assertion","owner":"OB-3","depends_on":["slot:ob3-core-neighbor"]},
      {"id":"slot:ob3-audit-source-two","kind":"slot","type":"Fixture.AuditResult","producer":"OB-3.observe-source-two","lifetime":"assertion","owner":"OB-3","depends_on":["slot:ob3-core-source-two"]},
      {"id":"fixture:audit-reader-ob3-zero","kind":"callable","type":"Fixture.AuditResult","signature":"Fixture.Audit.Read(Fixture.Core)","visibility":"internal-friend:Fixture.Tests","owner":"Fixture.Audit","args":[{"name":"core","type":"Fixture.Core","source":"slot:ob3-core-zero"}],"returns":"slot:ob3-audit-zero","depends_on":["slot:ob3-core-zero"]},
      {"id":"fixture:audit-reader-ob3-neighbor","kind":"callable","type":"Fixture.AuditResult","signature":"Fixture.Audit.Read(Fixture.Core)","visibility":"internal-friend:Fixture.Tests","owner":"Fixture.Audit","args":[{"name":"core","type":"Fixture.Core","source":"slot:ob3-core-neighbor"}],"returns":"slot:ob3-audit-neighbor","depends_on":["slot:ob3-core-neighbor"]},
      {"id":"fixture:audit-reader-ob3-source-two","kind":"callable","type":"Fixture.AuditResult","signature":"Fixture.Audit.Read(Fixture.Core)","visibility":"internal-friend:Fixture.Tests","owner":"Fixture.Audit","args":[{"name":"core","type":"Fixture.Core","source":"slot:ob3-core-source-two"}],"returns":"slot:ob3-audit-source-two","depends_on":["slot:ob3-core-source-two"]},
      {
        "id": "slot:ob2-delegations",
        "kind": "slot",
        "type": "System.Int32",
        "producer": "OB-2.negative",
        "lifetime": "assertion",
        "owner": "OB-2",
        "depends_on": [
          "fixture:loopback-delegates-once"
        ]
      },
      {"id":"slot:ob3-comparison","kind":"slot","type":"System.Boolean","producer":"OB-3.negative","lifetime":"assertion","owner":"OB-3","depends_on":["slot:ob3-audit-zero","slot:ob3-audit-neighbor","slot:ob3-audit-source-two","fixture:golden-cell-result","fixture:golden-source-two","fixture:golden-comparator"]},
      {
        "id": "fixture:golden-hidden-flipped",
        "kind": "runtime-resource",
        "type": "Fixture.CellResult",
        "path": "<computed:golden-hidden-flipped-path>",
        "mode": "100644",
        "bytes": "cell=<computed:k>;counter=1;hidden=1\n",
        "blob": "<computed:golden-hidden-flipped-blob>",
        "depends_on": []
      },
      {
        "id": "literal:source-two",
        "kind": "literal",
        "type": "System.Int32",
        "encoding": "utf8-decimal",
        "bytes": "<computed:k2>",
        "depends_on": []
      },
      {
        "id": "literal:neighbor-seven",
        "kind": "literal",
        "type": "System.Int32",
        "encoding": "utf8-decimal",
        "bytes": "<computed:n>",
        "depends_on": []
      },
      {
        "id": "fixture:source-same-neighbor-seven",
        "kind": "producer",
        "type": "Fixture.SourceInput",
        "signature": "Fixture.SourceInput.Single(Fixture.FaceId,System.Int32,System.Int32)",
        "visibility": "public",
        "owner": "Fixture.SourceInput",
        "args": [
          {
            "name": "face",
            "type": "Fixture.FaceId",
            "source": "literal:face-zero"
          },
          {
            "name": "source",
            "type": "System.Int32",
            "source": "literal:unit-impulse"
          },
          {
            "name": "neighbor",
            "type": "System.Int32",
            "source": "literal:neighbor-seven"
          }
        ],
        "depends_on": [
          "literal:face-zero",
          "literal:unit-impulse",
          "literal:neighbor-seven"
        ]
      },
      {
        "id": "fixture:source-two-neighbor-zero",
        "kind": "producer",
        "type": "Fixture.SourceInput",
        "signature": "Fixture.SourceInput.Single(Fixture.FaceId,System.Int32,System.Int32)",
        "visibility": "public",
        "owner": "Fixture.SourceInput",
        "args": [
          {
            "name": "face",
            "type": "Fixture.FaceId",
            "source": "literal:face-zero"
          },
          {
            "name": "source",
            "type": "System.Int32",
            "source": "literal:source-two"
          },
          {
            "name": "neighbor",
            "type": "System.Int32",
            "source": "literal:zero"
          }
        ],
        "depends_on": [
          "literal:face-zero",
          "literal:source-two",
          "literal:zero"
        ]
      },
      {
        "id": "fixture:golden-source-two",
        "kind": "runtime-resource",
        "type": "Fixture.CellResult",
        "path": "<computed:golden-source-two-path>",
        "mode": "100644",
        "bytes": "cell=<computed:k2>;counter=1;hidden=0\n",
        "blob": "<computed:golden-source-two-blob>",
        "depends_on": []
      }
    ],
    "union_red_realization": {
      "source_order": [
        "<computed:ob1-test-source-path>",
        "<computed:ob2-test-source-path>",
        "<computed:ob3-test-source-path>"
      ],
      "binding_source_order": [
        "<computed:fault-probe-contract-path>",
        "<computed:owned-handler-path>",
        "<computed:loopback-handler-path>",
        "<computed:throw-before-path>",
        "<computed:throw-during-path>",
        "<computed:throw-after-path>",
        "<computed:golden-comparator-path>"
      ],
      "compile_binding_source_order": [
        "<computed:fault-probe-contract-path>",
        "<computed:owned-handler-path>",
        "<computed:loopback-handler-path>",
        "<computed:throw-before-path>",
        "<computed:throw-during-path>",
        "<computed:throw-after-path>",
        "<computed:golden-comparator-path>"
      ],
      "runtime_resource_order": [
        {"path":"<computed:golden-cell-path>","mode":"100644","blob":"<computed:golden-cell-blob>"},
        {"path":"<computed:golden-hidden-flipped-path>","mode":"100644","blob":"<computed:golden-hidden-flipped-blob>"},
        {"path":"<computed:golden-source-two-path>","mode":"100644","blob":"<computed:golden-source-two-blob>"}
      ],
      "compile": {
        "compiler_identity_ref": "toolchain.runtime_identity.compiler",
        "command": "tools/fixture-compiler.fixture --base <computed:B> --sources <computed:ob1-test-source-path> <computed:ob2-test-source-path> <computed:ob3-test-source-path> --binding-sources <computed:fault-probe-contract-path> <computed:owned-handler-path> <computed:loopback-handler-path> <computed:throw-before-path> <computed:throw-during-path> <computed:throw-after-path> <computed:golden-comparator-path>",
        "exit": 0,
        "stdout_hash": "<computed:union-compile-stdout-hash>",
        "output_path": "<computed:union-assembly-path>",
        "output_mode": "100644",
        "output_blob": "<computed:union-assembly-blob>"
      },
      "discover": {
        "discover_identity_ref": "toolchain.runtime_identity.discover",
        "command": "tools/fixture-discover.fixture --assembly <computed:union-assembly-path> --filter FixtureTests.OB_*",
        "exit": 0,
        "count": 3,
        "ids": [
          "FixtureTests.OB_1",
          "FixtureTests.OB_2",
          "FixtureTests.OB_3"
        ],
        "stdout_hash": "<computed:union-discover-stdout-hash>"
      },
      "runs": [
        {"id":"FixtureTests.OB_1","runner_identity_ref":"toolchain.runtime_identity.runner","command":"tests/FixtureRunner.fixture --assembly <computed:union-assembly-path> --filter FixtureTests.OB_1 --runtime-resources <computed:golden-cell-path>@100644@<computed:golden-cell-blob>","exit":1,"status":"RED","criterion":"DW-1 missing member","stdout_hash":"<computed:union-ob1-red-stdout-hash>"},
        {"id":"FixtureTests.OB_2","runner_identity_ref":"toolchain.runtime_identity.runner","command":"tests/FixtureRunner.fixture --assembly <computed:union-assembly-path> --filter FixtureTests.OB_2 --runtime-resources none","exit":1,"status":"RED","criterion":"DW-2 loopback count","stdout_hash":"<computed:union-ob2-red-stdout-hash>"},
        {"id":"FixtureTests.OB_3","runner_identity_ref":"toolchain.runtime_identity.runner","command":"tests/FixtureRunner.fixture --assembly <computed:union-assembly-path> --filter FixtureTests.OB_3 --runtime-resources <computed:golden-cell-path>@100644@<computed:golden-cell-blob> <computed:golden-hidden-flipped-path>@100644@<computed:golden-hidden-flipped-blob> <computed:golden-source-two-path>@100644@<computed:golden-source-two-blob>","exit":1,"status":"RED","criterion":"DW-3 golden mismatch","stdout_hash":"<computed:union-ob3-red-stdout-hash>"}
      ]
    },
    "recipes": [
      {
        "id": "OB-1",
        "construct": {
          "signature": "Fixture.Core.Create(System.Int32,Fixture.Topology)",
          "visibility": "public",
          "owner": "Fixture.Core",
          "args": [
            {
              "name": "size",
              "type": "System.Int32",
              "source": "literal:size-one"
            },
            {
              "name": "topology",
              "type": "Fixture.Topology",
              "source": "fixture:two-room-open-sealed-faces"
            }
          ],
          "returns": "slot:ob1-core"
        },
        "act": {
          "signature": "Fixture.Core.Step(Fixture.Impulse,Fixture.ReactionHandler)",
          "visibility": "public",
          "owner": "operation:Step",
          "receiver": "slot:ob1-core",
          "args": [
            {
              "name": "impulse",
              "type": "Fixture.Impulse",
              "source": "fixture:face-impulse"
            },
            {
              "name": "handler",
              "type": "Fixture.ReactionHandler",
              "source": "fixture:owned-custom-handler"
            }
          ],
          "returns": "slot:ob1-step"
        },
        "observe": {
          "signature": "Fixture.Audit.Read()",
          "visibility": "internal-friend:Fixture.Tests",
          "owner": "Fixture.Audit",
          "receiver": "fixture:audit-reader",
          "args": [],
          "returns": "slot:ob1-audit",
          "assertion_input": "slot:ob1-audit"
        },
        "negative": {
          "signature": "FixtureFault.Select(FixtureFaultKind)",
          "visibility": "internal-friend:Fixture.Tests",
          "owner": "operation:Step",
          "binding": "fixture:fault-selector",
          "args": [
            {
              "name": "kind",
              "type": "FixtureFaultKind",
              "source": "literal:semantic-fault"
            }
          ],
          "controls": [
            "fixture:throw-before",
            "fixture:throw-during",
            "fixture:throw-after"
          ],
          "delegates": "Fixture.Core.Step(Fixture.Impulse,Fixture.ReactionHandler)",
          "returns": "slot:ob1-fault"
        },
        "source": {
          "spec": "openspec/changes/v21-fixture-change/specs/core/spec.md#OB-1",
          "baseline": "<computed:B>:src/PublicApi.fixture#Fixture.Core",
          "topology": "fixture:two-room-open-sealed-faces",
          "golden": "fixture:golden-cell-result",
          "golden_comparator": "fixture:golden-comparator",
          "source_isolation": "fixture:source-isolated-input",
          "handler_owner": "fixture:owned-handler-owner",
          "handler_call_count": "fixture:owned-handler-call-count",
          "loopback": "fixture:loopback-delegates-once"
        },
        "skeleton": [
          "bind:fixture:two-room-open-sealed-faces",
          "invoke:construct->slot:ob1-core",
          "compile-source:fixture:owned-handler-source",
          "bind:fixture:owned-custom-handler",
          "bind:fixture:face-impulse",
          "invoke:fixture:fault-selector->slot:ob1-fault",
          "invoke:act->slot:ob1-step",
          "bind:fixture:audit-reader",
          "invoke:observe->slot:ob1-audit",
          "bind:fixture:golden-cell-result",
          "compile-source:fixture:golden-comparator-source",
          "bind:fixture:golden-comparator",
          "invoke:fixture:golden-compare",
          "bind:fixture:source-isolated-input",
          "compile-source:fixture:loopback-source",
          "bind:fixture:loopback-delegates-once",
          "invoke:fixture:loopback-delegation-count",
          "compile-source:fixture:fault-probe-contract-source",
          "compile-source:fixture:throw-before-source",
          "compile-source:fixture:throw-during-source",
          "compile-source:fixture:throw-after-source",
          "bind:fixture:throw-before",
          "bind:fixture:throw-during",
          "bind:fixture:throw-after",
          "invoke:each expected+observed callable",
          "invoke:fixture:owned-handler-owner",
          "invoke:fixture:owned-handler-call-count",
          "assert:DW-1",
          "assert:golden",
          "assert:source-isolated",
          "assert:owned-handler",
          "assert:loopback-once"
        ],
        "red_realization": {
          "source_path": "<computed:ob1-test-source-path>",
          "source_mode": "100644",
          "source_bytes": "test FixtureTests.OB_1\nlet topology:Fixture.Topology=Fixture.Topology.TwoRoom(Fixture.FaceKind.Open,Fixture.FaceKind.Sealed)\nlet core:Fixture.Core=reflection Fixture.Core::Create(System.Int32,Fixture.Topology)(<computed:k>,topology)\nlet handler:Fixture.Tests.OwnedHandler=new Fixture.Tests.OwnedHandler(core)\nlet impulse:Fixture.Impulse=Fixture.Impulse.AtFace(Fixture.FaceId(0),<computed:k>)\nwith fault:FixtureFault=FixtureFault.Select(FixtureFaultKind.Semantic) owner=operation:Step\nlet step:Fixture.StepResult=core.Step(impulse,handler as Fixture.ReactionHandler)\nlet audit:Fixture.AuditResult=Fixture.Audit.For(core).Read()\nlet golden:Fixture.CellResult=load(<computed:golden-cell-path>,mode=100644,blob=<computed:golden-cell-blob>)\nlet comparator:Fixture.Tests.Golden=new Fixture.Tests.Golden()\nlet source:Fixture.SourceInput=Fixture.SourceInput.Single(Fixture.FaceId(0),<computed:k>,0)\nlet loopback:Fixture.Tests.LoopbackOnce=new Fixture.Tests.LoopbackOnce()\nlet loopstep:Fixture.StepResult=core.Step(impulse,loopback as Fixture.ReactionHandler)\nlet controls:[Fixture.Tests.FaultProbe]=[new Fixture.Tests.ThrowBefore(),new Fixture.Tests.ThrowDuring(),new Fixture.Tests.ThrowAfter()]\nlet phases:[Fixture.Tests.NegativePhase]=[Fixture.Tests.NegativePhase.Before,Fixture.Tests.NegativePhase.During,Fixture.Tests.NegativePhase.After]\nfor i:System.Int32 in [0,1,2] { let control:Fixture.Tests.FaultProbe=controls[i]; let before:Fixture.AuditResult=Fixture.Audit.For(core).Read(); expect throw core.Step(impulse,control as Fixture.ReactionHandler) with fault; assert comparator.AuditEqual(Fixture.Audit.For(core).Read(),before) and control.ExpectedPhase()==phases[i] and control.ObservedPhase()==phases[i]; }\nassert comparator.Compare(audit,golden) and source.neighbor==0 and comparator.ReferenceEqual(handler.Owner(),core) and handler.CallCount()==1 and loopback.DelegationCount()==1\nassert DW-1 absent Create exact result\n",
          "source_blob": "<computed:ob1-test-source-blob>",
          "binding_sources": [
            {"role":"compile-source","node":"fixture:fault-probe-contract-source","path":"<computed:fault-probe-contract-path>","mode":"100644","blob":"<computed:fault-probe-contract-blob>"},
            {
              "role": "compile-source",
              "node": "fixture:owned-handler-source",
              "path": "<computed:owned-handler-path>",
              "mode": "100644",
              "blob": "<computed:owned-handler-blob>"
            },
            {
              "role": "compile-source",
              "node": "fixture:loopback-source",
              "path": "<computed:loopback-handler-path>",
              "mode": "100644",
              "blob": "<computed:loopback-handler-blob>"
            },
            {
              "role": "compile-source",
              "node": "fixture:throw-before-source",
              "path": "<computed:throw-before-path>",
              "mode": "100644",
              "blob": "<computed:throw-before-blob>"
            },
            {
              "role": "compile-source",
              "node": "fixture:throw-during-source",
              "path": "<computed:throw-during-path>",
              "mode": "100644",
              "blob": "<computed:throw-during-blob>"
            },
            {
              "role": "compile-source",
              "node": "fixture:throw-after-source",
              "path": "<computed:throw-after-path>",
              "mode": "100644",
              "blob": "<computed:throw-after-blob>"
            },
            {
              "role": "compile-source",
              "node": "fixture:golden-comparator-source",
              "path": "<computed:golden-comparator-path>",
              "mode": "100644",
              "blob": "<computed:golden-comparator-blob>"
            }
          ],
          "runtime_resources": [
            {"node":"fixture:golden-cell-result","path":"<computed:golden-cell-path>","mode":"100644","blob":"<computed:golden-cell-blob>"}
          ],
          "new_symbol_route": "reflection:Fixture.Core::Create(System.Int32,Fixture.Topology)",
          "production_stub": false,
          "compile": {
            "compiler_identity_ref": "toolchain.runtime_identity.compiler",
            "command": "tools/fixture-compiler.fixture --base <computed:B> --source <computed:ob1-test-source-path> --binding-sources <computed:fault-probe-contract-path> <computed:owned-handler-path> <computed:loopback-handler-path> <computed:throw-before-path> <computed:throw-during-path> <computed:throw-after-path> <computed:golden-comparator-path>",
            "exit": 0,
            "stdout_hash": "<computed:ob1-compile-stdout-hash>",
            "output_path": "<computed:ob1-assembly-path>",
            "output_mode": "100644",
            "output_blob": "<computed:ob1-assembly-blob>"
          },
          "discover": {
            "discover_identity_ref": "toolchain.runtime_identity.discover",
            "command": "tools/fixture-discover.fixture --assembly <computed:ob1-assembly-path> --filter FixtureTests.OB_1",
            "exit": 0,
            "count": 1,
            "ids": [
              "FixtureTests.OB_1"
            ],
            "stdout_hash": "<computed:ob1-discover-stdout-hash>"
          },
          "run": {
            "runner_identity_ref": "toolchain.runtime_identity.runner",
            "command": "tests/FixtureRunner.fixture --assembly <computed:ob1-assembly-path> --filter FixtureTests.OB_1 --runtime-resources <computed:golden-cell-path>@100644@<computed:golden-cell-blob>",
            "exit": 1,
            "status": "RED",
            "criterion": "DW-1 missing member",
            "stdout_hash": "<computed:ob1-red-stdout-hash>"
          }
        }
      },
      {
        "id": "OB-2",
        "construct": {
          "signature": "Fixture.Core.Existing(Fixture.Topology)",
          "visibility": "public",
          "owner": "Fixture.Core",
          "args": [
            {
              "name": "topology",
              "type": "Fixture.Topology",
              "source": "fixture:single-cell-topology"
            }
          ],
          "returns": "slot:ob2-core"
        },
        "act": {
          "signature": "Fixture.Core.Step(Fixture.Impulse,Fixture.ReactionHandler)",
          "visibility": "public",
          "owner": "operation:Step",
          "receiver": "slot:ob2-core",
          "args": [
            {
              "name": "impulse",
              "type": "Fixture.Impulse",
              "source": "fixture:face-impulse"
            },
            {
              "name": "handler",
              "type": "Fixture.ReactionHandler",
              "source": "fixture:loopback-delegates-once"
            }
          ],
          "returns": "slot:ob2-step"
        },
        "observe": {
          "signature": "Fixture.Core.Value()",
          "visibility": "public",
          "owner": "Fixture.Core",
          "receiver": "slot:ob2-core",
          "args": [],
          "returns": "slot:ob2-value",
          "assertion_input": "slot:ob2-value"
        },
        "negative": {
          "signature": "Fixture.Tests.LoopbackOnce.DelegationCount()",
          "visibility": "test-local",
          "owner": "Fixture.Tests.LoopbackOnce",
          "binding": "fixture:loopback-delegation-count",
          "receiver": "fixture:loopback-delegates-once",
          "args": [],
          "controls": [
            "fixture:throw-before",
            "fixture:throw-during",
            "fixture:throw-after"
          ],
          "control_observers": [
            ["fixture:throw-before-expected","fixture:throw-before-observed"],
            ["fixture:throw-during-expected","fixture:throw-during-observed"],
            ["fixture:throw-after-expected","fixture:throw-after-observed"]
          ],
          "delegates": "Fixture.Core.Step(Fixture.Impulse,Fixture.ReactionHandler)",
          "returns": "slot:ob2-delegations"
        },
        "source": {
          "spec": "openspec/changes/v21-fixture-change/specs/core/spec.md#OB-2",
          "baseline": "<computed:B>:src/PublicApi.fixture#Fixture.Core.Step",
          "topology": "fixture:single-cell-topology",
          "loopback": "fixture:loopback-delegates-once"
        },
        "skeleton": [
          "bind:fixture:existing-core",
          "invoke:construct->slot:ob2-core",
          "bind:fixture:face-impulse",
          "invoke:fixture:fault-selector",
          "compile-source:fixture:fault-probe-contract-source",
          "compile-source:fixture:throw-before-source",
          "compile-source:fixture:throw-during-source",
          "compile-source:fixture:throw-after-source",
          "bind:fixture:throw-before",
          "bind:fixture:throw-during",
          "bind:fixture:throw-after",
          "invoke:throw-before expected+observed before DW-2",
          "invoke:throw-during expected+observed before DW-2",
          "invoke:throw-after expected+observed before DW-2",
          "compile-source:fixture:loopback-source",
          "bind:fixture:loopback-delegates-once",
          "invoke:act->slot:ob2-step",
          "invoke:observe->slot:ob2-value",
          "invoke:fixture:loopback-delegation-count->slot:ob2-delegations",
          "invoke:fixture:loopback-call-count",
          "assert:DW-2",
          "assert:atomic-controls",
          "assert:loopback-once"
        ],
        "red_realization": {
          "source_path": "<computed:ob2-test-source-path>",
          "source_mode": "100644",
          "source_bytes": "test FixtureTests.OB_2\nlet topology:Fixture.Topology=Fixture.Topology.SingleCell()\nlet core:Fixture.Core=Fixture.Core.Existing(topology)\nlet impulse:Fixture.Impulse=Fixture.Impulse.AtFace(Fixture.FaceId(0),<computed:k>)\nwith fault:FixtureFault=FixtureFault.Select(FixtureFaultKind.Semantic) owner=operation:Step\nlet controls:[Fixture.Tests.FaultProbe]=[new Fixture.Tests.ThrowBefore(),new Fixture.Tests.ThrowDuring(),new Fixture.Tests.ThrowAfter()]\nlet phases:[Fixture.Tests.NegativePhase]=[Fixture.Tests.NegativePhase.Before,Fixture.Tests.NegativePhase.During,Fixture.Tests.NegativePhase.After]\nfor i:System.Int32 in [0,1,2] { let control:Fixture.Tests.FaultProbe=controls[i]; let before:System.Int32=core.Value(); expect throw core.Step(impulse,control as Fixture.ReactionHandler) with fault; assert core.Value()==before and control.ExpectedPhase()==phases[i] and control.ObservedPhase()==phases[i]; }\nlet loopback:Fixture.Tests.LoopbackOnce=new Fixture.Tests.LoopbackOnce()\nlet step:Fixture.StepResult=core.Step(impulse,loopback as Fixture.ReactionHandler)\nlet value:System.Int32=core.Value()\nassert loopback.DelegationCount()==1 and loopback.CallCount()==2 and value==<computed:k>\nassert DW-2 existing Step loopback once\n",
          "source_blob": "<computed:ob2-test-source-blob>",
          "binding_sources": [
            {"role":"compile-source","node":"fixture:fault-probe-contract-source","path":"<computed:fault-probe-contract-path>","mode":"100644","blob":"<computed:fault-probe-contract-blob>"},
            {
              "role": "compile-source",
              "node": "fixture:loopback-source",
              "path": "<computed:loopback-handler-path>",
              "mode": "100644",
              "blob": "<computed:loopback-handler-blob>"
            },
            {
              "role": "compile-source",
              "node": "fixture:throw-before-source",
              "path": "<computed:throw-before-path>",
              "mode": "100644",
              "blob": "<computed:throw-before-blob>"
            },
            {
              "role": "compile-source",
              "node": "fixture:throw-during-source",
              "path": "<computed:throw-during-path>",
              "mode": "100644",
              "blob": "<computed:throw-during-blob>"
            },
            {
              "role": "compile-source",
              "node": "fixture:throw-after-source",
              "path": "<computed:throw-after-path>",
              "mode": "100644",
              "blob": "<computed:throw-after-blob>"
            }
          ],
          "runtime_resources": [],
          "new_symbol_route": "existing-direct",
          "production_stub": false,
          "compile": {
            "compiler_identity_ref": "toolchain.runtime_identity.compiler",
            "command": "tools/fixture-compiler.fixture --base <computed:B> --source <computed:ob2-test-source-path> --binding-sources <computed:fault-probe-contract-path> <computed:loopback-handler-path> <computed:throw-before-path> <computed:throw-during-path> <computed:throw-after-path>",
            "exit": 0,
            "stdout_hash": "<computed:ob2-compile-stdout-hash>",
            "output_path": "<computed:ob2-assembly-path>",
            "output_mode": "100644",
            "output_blob": "<computed:ob2-assembly-blob>"
          },
          "discover": {
            "discover_identity_ref": "toolchain.runtime_identity.discover",
            "command": "tools/fixture-discover.fixture --assembly <computed:ob2-assembly-path> --filter FixtureTests.OB_2",
            "exit": 0,
            "count": 1,
            "ids": [
              "FixtureTests.OB_2"
            ],
            "stdout_hash": "<computed:ob2-discover-stdout-hash>"
          },
          "run": {
            "runner_identity_ref": "toolchain.runtime_identity.runner",
            "command": "tests/FixtureRunner.fixture --assembly <computed:ob2-assembly-path> --filter FixtureTests.OB_2 --runtime-resources none",
            "exit": 1,
            "status": "RED",
            "criterion": "DW-2 loopback count",
            "stdout_hash": "<computed:ob2-red-stdout-hash>"
          }
        }
      },
      {
        "id": "OB-3",
        "construct": {
          "signature": "Fixture.Core.Existing(Fixture.Topology)",
          "visibility": "public",
          "owner": "Fixture.Core",
          "args": [
            {
              "name": "topology",
              "type": "Fixture.Topology",
              "source": "fixture:single-cell-topology"
            }
          ],
          "invocations": [
            {"id":"zero","returns":"slot:ob3-core-zero"},
            {"id":"neighbor","returns":"slot:ob3-core-neighbor"},
            {"id":"source-two","returns":"slot:ob3-core-source-two"}
          ]
        },
        "act": {
          "signature": "Fixture.Core.StepSource(Fixture.SourceInput)",
          "visibility": "public",
          "owner": "operation:StepSource",
          "invocations": [
            {"receiver":"slot:ob3-core-zero","args":[{"name":"input","type":"Fixture.SourceInput","source":"fixture:source-isolated-input"}],"returns":"slot:ob3-step-zero"},
            {"receiver":"slot:ob3-core-neighbor","args":[{"name":"input","type":"Fixture.SourceInput","source":"fixture:source-same-neighbor-seven"}],"returns":"slot:ob3-step-neighbor"},
            {"receiver":"slot:ob3-core-source-two","args":[{"name":"input","type":"Fixture.SourceInput","source":"fixture:source-two-neighbor-zero"}],"returns":"slot:ob3-step-source-two"}
          ]
        },
        "observe": {
          "signature": "Fixture.Audit.Read(Fixture.Core)",
          "visibility": "internal-friend:Fixture.Tests",
          "owner": "Fixture.Audit",
          "routes": [
            {"binding":"fixture:audit-reader-ob3-zero","args":[{"name":"core","type":"Fixture.Core","source":"slot:ob3-core-zero"}],"returns":"slot:ob3-audit-zero"},
            {"binding":"fixture:audit-reader-ob3-neighbor","args":[{"name":"core","type":"Fixture.Core","source":"slot:ob3-core-neighbor"}],"returns":"slot:ob3-audit-neighbor"},
            {"binding":"fixture:audit-reader-ob3-source-two","args":[{"name":"core","type":"Fixture.Core","source":"slot:ob3-core-source-two"}],"returns":"slot:ob3-audit-source-two"}
          ],
          "assertion_inputs": ["slot:ob3-audit-zero","slot:ob3-audit-neighbor","slot:ob3-audit-source-two"]
        },
        "negative": {
          "signature": "Fixture.Tests.Golden.Compare(Fixture.AuditResult,Fixture.CellResult)",
          "visibility": "test-local",
          "owner": "Fixture.Tests",
          "binding": "fixture:golden-compare",
          "args_matrix": [
            ["slot:ob3-audit-zero","fixture:golden-cell-result"],
            ["slot:ob3-audit-neighbor","fixture:golden-cell-result"],
            ["slot:ob3-audit-source-two","fixture:golden-source-two"],
            ["slot:ob3-audit-zero","fixture:golden-hidden-flipped"]
          ],
          "audit_equality_binding": "fixture:golden-audit-equal",
          "controls": [
            "fixture:golden-hidden-flipped"
          ],
          "delegates": "Fixture.Core.StepSource(Fixture.SourceInput)",
          "returns": "slot:ob3-comparison"
        },
        "source": {
          "spec": "openspec/changes/v21-fixture-change/specs/core/spec.md#OB-3",
          "baseline": "<computed:B>:src/PublicApi.fixture#Fixture.Core.StepSource",
          "topology": "fixture:single-cell-topology",
          "golden": "fixture:golden-cell-result",
          "source_two_golden": "fixture:golden-source-two",
          "negative_golden": "fixture:golden-hidden-flipped",
          "golden_comparator": "fixture:golden-comparator",
          "audit_readers": ["fixture:audit-reader-ob3-zero","fixture:audit-reader-ob3-neighbor","fixture:audit-reader-ob3-source-two"],
          "source_zero": "fixture:source-isolated-input",
          "same_source_neighbor_nonzero": "fixture:source-same-neighbor-seven",
          "different_source_neighbor_zero": "fixture:source-two-neighbor-zero"
        },
        "skeleton": [
          "bind:fixture:existing-core",
          "invoke:construct-zero->slot:ob3-core-zero",
          "invoke:construct-neighbor->slot:ob3-core-neighbor",
          "invoke:construct-source-two->slot:ob3-core-source-two",
          "bind:fixture:source-isolated-input",
          "bind:fixture:source-same-neighbor-seven",
          "bind:fixture:source-two-neighbor-zero",
          "invoke:act-zero->slot:ob3-step-zero",
          "invoke:act-neighbor->slot:ob3-step-neighbor",
          "invoke:act-source-two->slot:ob3-step-source-two",
          "invoke:fixture:audit-reader-ob3-zero->slot:ob3-audit-zero",
          "invoke:fixture:audit-reader-ob3-neighbor->slot:ob3-audit-neighbor",
          "invoke:fixture:audit-reader-ob3-source-two->slot:ob3-audit-source-two",
          "bind:fixture:golden-cell-result",
          "bind:fixture:golden-source-two",
          "bind:fixture:golden-hidden-flipped",
          "compile-source:fixture:golden-comparator-source",
          "bind:fixture:golden-comparator",
          "invoke:fixture:golden-compare four exact routes->slot:ob3-comparison",
          "invoke:fixture:golden-audit-equal zero,neighbor",
          "invoke:fixture:golden-audit-equal zero,source-two",
          "assert:DW-3",
          "assert:same-source-neighbor-invariant",
          "assert:different-source-dependent",
          "assert:golden-positive-and-negative",
          "assert:hidden-audit"
        ],
        "red_realization": {
          "source_path": "<computed:ob3-test-source-path>",
          "source_mode": "100644",
          "source_bytes": "test FixtureTests.OB_3\nlet topology:Fixture.Topology=Fixture.Topology.SingleCell()\nlet core0:Fixture.Core=Fixture.Core.Existing(topology)\nlet coreN:Fixture.Core=Fixture.Core.Existing(topology)\nlet core2:Fixture.Core=Fixture.Core.Existing(topology)\nlet input0:Fixture.SourceInput=Fixture.SourceInput.Single(Fixture.FaceId(0),<computed:k>,0)\nlet inputN:Fixture.SourceInput=Fixture.SourceInput.Single(Fixture.FaceId(0),<computed:k>,<computed:n>)\nlet input2:Fixture.SourceInput=Fixture.SourceInput.Single(Fixture.FaceId(0),<computed:k2>,0)\nlet step0:Fixture.StepResult=core0.StepSource(input0)\nlet stepN:Fixture.StepResult=coreN.StepSource(inputN)\nlet step2:Fixture.StepResult=core2.StepSource(input2)\nlet audit0:Fixture.AuditResult=Fixture.Audit.Read(core0)\nlet auditN:Fixture.AuditResult=Fixture.Audit.Read(coreN)\nlet audit2:Fixture.AuditResult=Fixture.Audit.Read(core2)\nlet golden1:Fixture.CellResult=load(<computed:golden-cell-path>,mode=100644,blob=<computed:golden-cell-blob>)\nlet golden2:Fixture.CellResult=load(<computed:golden-source-two-path>,mode=100644,blob=<computed:golden-source-two-blob>)\nlet negativeGolden:Fixture.CellResult=load(<computed:golden-hidden-flipped-path>,mode=100644,blob=<computed:golden-hidden-flipped-blob>)\nlet comparator:Fixture.Tests.Golden=new Fixture.Tests.Golden()\nassert comparator.Compare(audit0,golden1) and comparator.Compare(auditN,golden1) and comparator.AuditEqual(audit0,auditN)\nassert comparator.Compare(audit2,golden2) and !comparator.AuditEqual(audit2,audit0)\nassert !comparator.Compare(audit0,negativeGolden)\nassert DW-3 source-isolated golden audit\n",
          "source_blob": "<computed:ob3-test-source-blob>",
          "binding_sources": [
            {
              "role": "compile-source",
              "node": "fixture:golden-comparator-source",
              "path": "<computed:golden-comparator-path>",
              "mode": "100644",
              "blob": "<computed:golden-comparator-blob>"
            }
          ],
          "runtime_resources": [
            {"node":"fixture:golden-cell-result","path":"<computed:golden-cell-path>","mode":"100644","blob":"<computed:golden-cell-blob>"},
            {"node":"fixture:golden-hidden-flipped","path":"<computed:golden-hidden-flipped-path>","mode":"100644","blob":"<computed:golden-hidden-flipped-blob>"},
            {"node":"fixture:golden-source-two","path":"<computed:golden-source-two-path>","mode":"100644","blob":"<computed:golden-source-two-blob>"}
          ],
          "new_symbol_route": "existing-direct",
          "production_stub": false,
          "compile": {
            "compiler_identity_ref": "toolchain.runtime_identity.compiler",
            "command": "tools/fixture-compiler.fixture --base <computed:B> --source <computed:ob3-test-source-path> --binding-sources <computed:golden-comparator-path>",
            "exit": 0,
            "stdout_hash": "<computed:ob3-compile-stdout-hash>",
            "output_path": "<computed:ob3-assembly-path>",
            "output_mode": "100644",
            "output_blob": "<computed:ob3-assembly-blob>"
          },
          "discover": {
            "discover_identity_ref": "toolchain.runtime_identity.discover",
            "command": "tools/fixture-discover.fixture --assembly <computed:ob3-assembly-path> --filter FixtureTests.OB_3",
            "exit": 0,
            "count": 1,
            "ids": [
              "FixtureTests.OB_3"
            ],
            "stdout_hash": "<computed:ob3-discover-stdout-hash>"
          },
          "run": {
            "runner_identity_ref": "toolchain.runtime_identity.runner",
            "command": "tests/FixtureRunner.fixture --assembly <computed:ob3-assembly-path> --filter FixtureTests.OB_3 --runtime-resources <computed:golden-cell-path>@100644@<computed:golden-cell-blob> <computed:golden-hidden-flipped-path>@100644@<computed:golden-hidden-flipped-blob> <computed:golden-source-two-path>@100644@<computed:golden-source-two-blob>",
            "exit": 1,
            "status": "RED",
            "criterion": "DW-3 golden mismatch",
            "stdout_hash": "<computed:ob3-red-stdout-hash>"
          }
        }
      }
    ]
  },
  "light": {
    "mode": "coordinated-light",
    "trigger_glob": "openspec/changes/*/specs/*/spec.md",
    "scan_command": "git -c core.quotepath=false ls-files -- openspec/changes/*/specs/*/spec.md",
    "scan_exit": 0,
    "matched_paths": [],
    "stdout_bytes": "",
    "observation_hash": "<computed:light-scan-observation-hash>",
    "validation_conformance_event": "history/<computed:bootstrap-conformance-result-path>@<computed:C-bootstrap-conformance>",
    "validation_conformance_receipt": "<computed:bootstrap-receipt>",
    "forbidden_fields": [
      "testability",
      "testability-mode",
      "testability-blob",
      "input-manifest-hash",
      "binding-registry-hash"
    ],
    "retained_fields": [
      "base-authority",
      "acceptance-source",
      "acceptance-hash",
      "toolchain-manifest-hash",
      "run-id",
      "product-result-path"
    ]
  },
  "setup": {
    "manifest": [
      {
        "op": "create",
        "path": "validation.config",
        "class": "validation-toolchain",
        "source_mode": "100644",
        "source_blob": "<computed:config-blob>"
      },
      {
        "op": "overlay",
        "path": "AGENTS.md",
        "class": "contract",
        "pre_mode": "100644",
        "pre_blob": "<computed:setup-agents-pre-blob>",
        "post_mode": "100644",
        "post_blob": "<computed:setup-agents-post-blob>",
        "patch_hash": "<computed:setup-agents-patch-hash>"
      },
      {
        "op": "create",
        "path": "tools/plan-handoff-check.fixture",
        "class": "validation-toolchain",
        "source_mode": "100644",
        "source_blob": "<computed:checker-blob>"
      },
      {
        "op": "create",
        "path": "tools/plan-handoff-schema.fixture",
        "class": "validation-toolchain",
        "source_mode": "100644",
        "source_blob": "<computed:schema-blob>"
      },
      {
        "op": "create",
        "path": "tools/fixture-compiler.fixture",
        "class": "validation-toolchain",
        "source_mode": "100755",
        "source_blob": "<computed:fixture-compiler-blob>"
      },
      {
        "op": "create",
        "path": "tools/fixture-discover.fixture",
        "class": "validation-toolchain",
        "source_mode": "100755",
        "source_blob": "<computed:fixture-discover-blob>"
      },
      {
        "op": "create",
        "path": "tests/FixtureRunner.fixture",
        "class": "validation-toolchain",
        "source_mode": "100755",
        "source_blob": "<computed:test-runner-blob>"
      },
      {
        "op": "create",
        "path": "docs/adr/ADR-0001-stack.fixture",
        "class": "interview-decision",
        "source_mode": "100644",
        "source_blob": "<computed:stack-adr-blob>"
      }
    ],
    "protected": [
      {
        "path": "notes/owner.txt",
        "mode": "100644",
        "blob": "<computed:owner-note-blob>"
      }
    ],
    "inventory_count": 1,
    "inventory_hash": "<computed:setup-inventory-hash>"
  },
  "setup_variants": {
    "absent": {
      "entry_state": "absent",
      "entry_tree": "<computed:S-absent>",
      "post_tree": "<computed:SB-absent>",
      "protected": [],
      "inventory_count": 0,
      "inventory_hash": "<computed:empty-inventory-hash>",
      "manifest": [
        {
          "op": "create",
          "path": "AGENTS.md",
          "class": "contract",
          "source_mode": "100644",
          "source_blob": "<computed:setup-agents-new-blob>"
        },
        {
          "op": "create",
          "path": "validation.config",
          "class": "validation-toolchain",
          "source_mode": "100644",
          "source_blob": "<computed:config-blob>"
        },
        {
          "op": "create",
          "path": "tools/plan-handoff-check.fixture",
          "class": "validation-toolchain",
          "source_mode": "100644",
          "source_blob": "<computed:checker-blob>"
        },
        {
          "op": "create",
          "path": "tools/plan-handoff-schema.fixture",
          "class": "validation-toolchain",
          "source_mode": "100644",
          "source_blob": "<computed:schema-blob>"
        },
        {
          "op": "create",
          "path": "tools/fixture-compiler.fixture",
          "class": "validation-toolchain",
          "source_mode": "100755",
          "source_blob": "<computed:fixture-compiler-blob>"
        },
        {
          "op": "create",
          "path": "tools/fixture-discover.fixture",
          "class": "validation-toolchain",
          "source_mode": "100755",
          "source_blob": "<computed:fixture-discover-blob>"
        },
        {
          "op": "create",
          "path": "tests/FixtureRunner.fixture",
          "class": "validation-toolchain",
          "source_mode": "100755",
          "source_blob": "<computed:test-runner-blob>"
        },
        {
          "op": "create",
          "path": "docs/adr/ADR-0001-stack.fixture",
          "class": "interview-decision",
          "source_mode": "100644",
          "source_blob": "<computed:stack-adr-blob>"
        }
      ]
    },
    "empty": {
      "inherits": "setup_variants.absent",
      "set": {
        "entry_state": "empty",
        "entry_tree": "<computed:S-empty>",
        "post_tree": "<computed:SB-empty>"
      }
    },
    "nonempty": {
      "entry_state": "nonempty",
      "entry_tree": "<computed:S0>",
      "post_tree": "<computed:SB>",
      "manifest_ref": "setup.manifest",
      "protected_ref": "setup.protected",
      "inventory_count": 1,
      "inventory_hash": "<computed:setup-inventory-hash>"
    }
  },
  "resync": {
    "identity": {
      "repo": "fixture/product",
      "worktree": "<computed:random-root>",
      "branch": "codex/v21-resync",
      "base_authority": "sha:<computed:RB>",
      "base": "<computed:RB>"
    },
    "manifest": [
      {
        "op": "overlay",
        "path": "validation.config",
        "class": "validation-toolchain",
        "pre_mode": "100644",
        "pre_blob": "<computed:v20-config-blob>",
        "post_mode": "100644",
        "post_blob": "<computed:config-blob>",
        "patch_hash": "<computed:v20-v21-config-patch-hash>"
      },
      {
        "op": "overlay",
        "path": "AGENTS.md",
        "class": "contract",
        "pre_mode": "100644",
        "pre_blob": "<computed:v20-agents-blob>",
        "post_mode": "100644",
        "post_blob": "<computed:v21-agents-blob>",
        "patch_hash": "<computed:v20-v21-agents-patch-hash>"
      },
      {
        "op": "create",
        "path": "tools/plan-handoff-check.fixture",
        "class": "validation-toolchain",
        "source_mode": "100644",
        "source_blob": "<computed:checker-blob>"
      },
      {
        "op": "create",
        "path": "tools/plan-handoff-schema.fixture",
        "class": "validation-toolchain",
        "source_mode": "100644",
        "source_blob": "<computed:schema-blob>"
      },
      {
        "op": "create",
        "path": "tools/fixture-compiler.fixture",
        "class": "validation-toolchain",
        "source_mode": "100755",
        "source_blob": "<computed:fixture-compiler-blob>"
      },
      {
        "op": "create",
        "path": "tools/fixture-discover.fixture",
        "class": "validation-toolchain",
        "source_mode": "100755",
        "source_blob": "<computed:fixture-discover-blob>"
      },
      {
        "op": "create",
        "path": "tests/FixtureRunner.fixture",
        "class": "validation-toolchain",
        "source_mode": "100755",
        "source_blob": "<computed:test-runner-blob>"
      }
    ]
  },
  "call_defaults": {
    "to": "executor",
    "direction": "fixture",
    "play": "work",
    "node": "g-fixture",
    "task": "t-fixture",
    "kind": "engineering",
    "repo": "fixture/product",
    "worktree": "<computed:random-root>",
    "budget": "one session"
  },
  "call_intents": {
    "setup_interview": {
      "inherits": "call_defaults",
      "set": {
        "id": "c-setup-interview",
        "goal": "capture exact stack and target inventory without product writes",
        "context": "profile authority plus target path",
        "boundaries": "read-only product; no adapter; no install",
        "done_when": "full inventory and accepted stack profile returned in a complete RESULT",
        "return": "complete RESULT with inventory/profile evidence",
        "packet_stage": "intent",
        "phase": "SETUP",
        "setup_stage": "interview",
        "profile_blob": "<external:stack-profile-blob>",
        "requested_inventory": "path|mode|blob|reparse|git-state"
      }
    },
    "adapter_author_child": {
      "inherits": "call_defaults",
      "set": {
        "id": "c-adapter-author",
        "goal": "author one exact stack adapter artifact",
        "context": "interview event path and payload hash plus pinned corpus/profile",
        "boundaries": "no product write; author cannot review or install",
        "done_when": "declared adapter path/mode/blob and exact output manifest returned",
        "return": "complete RESULT plus one Direction work artifact",
        "packet_stage": "intent",
        "phase": "SETUP",
        "setup_stage": "adapter-author",
        "interview_event_path": "history/setup-interview-result.md",
        "interview_event_payload_hash": "<computed:setup-interview-payload-hash>",
        "profile_path": "os/engineering/profiles/fixture.md",
        "profile_mode": "100644",
        "profile_blob": "<external:stack-profile-blob>",
        "profile_sha256": "<external:stack-profile-sha256>",
        "adapter_source": "work/validation-adapters/<computed:stack-id>-v21.fixture",
        "adapter_mode": "100644",
        "required_output_manifest": "adapter_output_manifest.rows+bytes+hash",
        "corpus_blob": "<external:this-file-git-blob>",
        "specimen_hash": "<external:this-json-sha256>"
      }
    },
    "adapter_review_child": {
      "inherits": "call_defaults",
      "set": {
        "id": "c-adapter-review",
        "goal": "independently refute the exact authored adapter",
        "context": "interview and adapter-author event paths/payload hashes plus pinned corpus/profile",
        "boundaries": "read-only product; reviewer distinct from author and installer",
        "done_when": "canonical materialization refuted or exact path/mode/blob/output manifest accepted",
        "return": "complete RESULT with independent verdict",
        "packet_stage": "intent",
        "phase": "SETUP",
        "setup_stage": "adapter-review",
        "interview_event_path": "history/setup-interview-result.md",
        "interview_event_payload_hash": "<computed:setup-interview-payload-hash>",
        "author_event_path": "history/adapter-author-result.md",
        "author_event_payload_hash": "<computed:adapter-author-payload-hash>",
        "profile_path": "os/engineering/profiles/fixture.md",
        "profile_mode": "100644",
        "profile_blob": "<external:stack-profile-blob>",
        "profile_sha256": "<external:stack-profile-sha256>",
        "adapter_source": "work/validation-adapters/<computed:stack-id>-v21.fixture",
        "adapter_mode": "100644",
        "adapter_blob": "<computed:accepted-adapter-blob>",
        "adapter_output_manifest_path": "work/validation-adapters/<computed:stack-id>-v21.manifest",
        "adapter_output_manifest_mode": "100644",
        "adapter_output_manifest_blob": "<computed:adapter-output-manifest-blob>",
        "adapter_output_manifest_hash": "<computed:adapter-output-manifest-hash>",
        "corpus_blob": "<external:this-file-git-blob>",
        "specimen_hash": "<external:this-json-sha256>"
      }
    },
    "setup_install": {
      "inherits": "call_defaults",
      "set": {
        "id": "c-setup-install",
        "goal": "install exactly the accepted v21 feedback loop",
        "context": "ancestral interview, author and review evidence plus exact create/overlay manifest",
        "boundaries": "only declared manifest delta; preserve all other bytes",
        "done_when": "post-tree clean and full conformance returns GREEN",
        "return": "complete RESULT with installed tree and conformance evidence",
        "packet_stage": "intent",
        "phase": "SETUP",
        "setup_stage": "install",
        "interview_event": "history/setup-interview-result.md@<computed:I-setup-interview>",
        "author_event": "history/adapter-author-result.md@<computed:I-adapter-author-result>",
        "adapter_review_event_path": "history/adapter-review-result.md",
        "adapter_review_event_payload_hash": "<computed:adapter-review-payload-hash>",
        "profile_path": "os/engineering/profiles/fixture.md",
        "profile_mode": "100644",
        "profile_blob": "<external:stack-profile-blob>",
        "profile_sha256": "<external:stack-profile-sha256>",
        "adapter_mode": "100644",
        "adapter_blob": "<computed:accepted-adapter-blob>",
        "adapter_output_manifest_path": "work/validation-adapters/<computed:stack-id>-v21.manifest",
        "adapter_output_manifest_mode": "100644",
        "adapter_output_manifest_blob": "<computed:adapter-output-manifest-blob>",
        "adapter_output_manifest_hash": "<computed:adapter-output-manifest-hash>",
        "manifest_ref": "setup.manifest",
        "toolchain_ref": "toolchain",
        "corpus_blob": "<external:this-file-git-blob>",
        "specimen_hash": "<external:this-json-sha256>"
      }
    },
    "setup_install_absent": {
      "inherits": "call_intents.setup_install",
      "set": {
        "manifest_ref": "setup_variants.absent.manifest"
      }
    },
    "setup_install_empty": {
      "inherits": "call_intents.setup_install",
      "set": {
        "manifest_ref": "setup_variants.empty.manifest"
      }
    },
    "setup_install_nonempty": {
      "inherits": "call_intents.setup_install",
      "set": {}
    },
    "resync": {
      "inherits": "call_defaults",
      "set": {
        "id": "c-resync",
        "goal": "re-sync only the v21 contract and toolchain",
        "context": "initialized exact base plus ancestral interview/author/review evidence",
        "boundaries": "no feature/source/test/acceptance delta",
        "done_when": "clean exact overlay/create post-tree and conformance GREEN",
        "return": "complete RESULT with protected-byte proof",
        "packet_stage": "intent",
        "phase": "RE-SYNC",
        "branch": "codex/v21-resync",
        "base_authority": "sha:<computed:RB>",
        "base": "<computed:RB>",
        "interview_event": "history/setup-interview-result.md@<computed:I-setup-interview>",
        "author_event": "history/adapter-author-result.md@<computed:I-adapter-author-result>",
        "adapter_review_event_path": "history/adapter-review-resync-result.md",
        "adapter_review_event_payload_hash": "<computed:adapter-review-resync-payload-hash>",
        "profile_path": "os/engineering/profiles/fixture.md",
        "profile_mode": "100644",
        "profile_blob": "<external:stack-profile-blob>",
        "profile_sha256": "<external:stack-profile-sha256>",
        "adapter_mode": "100644",
        "adapter_blob": "<computed:accepted-adapter-blob>",
        "adapter_output_manifest_path": "work/validation-adapters/<computed:stack-id>-v21.manifest",
        "adapter_output_manifest_mode": "100644",
        "adapter_output_manifest_blob": "<computed:adapter-output-manifest-blob>",
        "adapter_output_manifest_hash": "<computed:adapter-output-manifest-hash>",
        "manifest_ref": "resync.manifest",
        "toolchain_ref": "toolchain_resync",
        "corpus_blob": "<external:this-file-git-blob>",
        "specimen_hash": "<external:this-json-sha256>"
      }
    },
    "plan_author": {
      "inherits": "call_defaults",
      "set": {
        "id": "c-plan-author",
        "goal": "produce a complete executable handoff candidate",
        "context": "exact base, acceptance, toolchain, conformance and TESTABILITY authority",
        "boundaries": "plan only; no owner verdict; no product implementation or RED authoring",
        "done_when": "candidate is clean and every obligation compiles, uniquely discovers and runs exact RED at base",
        "return": "complete PLAN-GATED RESULT with receipt and no verdict",
        "packet_stage": "intent",
        "phase": "PLAN",
        "plan_stage": "author",
        "branch": "codex/v21-fixture",
        "base_authority": "sha:<computed:B>",
        "base": "<computed:B>",
        "acceptance_source": "call:v21-fixture#done_when",
        "acceptance_hash": "<computed:acceptance-hash>",
        "change_id": "v21-fixture-change",
        "product_result_path": "docs/results/v21-fixture-change.md",
        "validation_conformance_event_path": "history/conformance-result.md",
        "validation_conformance_event_payload_hash": "<computed:conformance-payload-hash>",
        "validation_conformance_receipt": "<computed:validation-conformance-receipt>",
        "toolchain_ref": "toolchain",
        "testability_ref": "testability_pin+testability"
      }
    },
    "plan_author_bootstrap": {
      "inherits": "call_intents.plan_author",
      "set": {
        "validation_conformance_event_path": "history/bootstrap-conformance-result.md",
        "validation_conformance_event_payload_hash": "<computed:bootstrap-conformance-payload-hash>",
        "validation_conformance_receipt": "<computed:bootstrap-receipt>"
      }
    },
    "plan_verdict_child": {
      "inherits": "call_intents.plan_author",
      "delete": [
        "/validation_conformance_event_path",
        "/validation_conformance_event_payload_hash"
      ],
      "set": {
        "id": "c-plan-verdict",
        "goal": "obtain the owner's verdict on the exact gated candidate",
        "context": "exact candidate, PLAN receipt and event payload",
        "boundaries": "no plan edit; no product work; verdict belongs to owner",
        "done_when": "owner words cite exact candidate and receipt or reject it",
        "return": "complete RESULT citing the owner's actual words",
        "plan_stage": "verdict",
        "plan_candidate_head": "<computed:P>",
        "plan_receipt": "<computed:plan-receipt>",
        "validation_conformance_event": "history/conformance-result.md@<computed:C-final-conformance>",
        "plan_event_path": "history/plan-gated-result.md",
        "plan_event_payload_hash": "<computed:plan-gated-payload-hash>"
      }
    },
    "execute_child": {
      "inherits": "call_intents.plan_verdict_child",
      "delete": [
        "/plan_stage",
        "/plan_event_path",
        "/plan_event_payload_hash"
      ],
      "set": {
        "id": "c-execute",
        "goal": "start a fresh isolated execution from the accepted candidate",
        "context": "immutable PLAN/TESTABILITY plus owner and PLAN event payloads",
        "boundaries": "fresh RED author first; builder cannot edit frozen packet/tests",
        "done_when": "fresh run identity and exact independent RED boundary are established",
        "return": "complete execution checkpoint RESULT",
        "phase": "EXECUTE",
        "execution_mode": "fresh",
        "plan_receipt_event": "history/plan-gated-result.md@<computed:W-plan-receipt>",
        "owner_verdict_event_path": "history/owner-verdict-result.md",
        "owner_verdict_event_payload_hash": "<computed:owner-verdict-payload-hash>"
      }
    },
    "execute_light": {
      "inherits": "call_defaults",
      "set": {
        "id": "c-execute-light",
        "goal": "start one coordinated-light execution with no G0 path",
        "context": "exact base, acceptance, conformance, toolchain and light scan",
        "boundaries": "no frozen change path; preserve all transaction identity",
        "done_when": "fresh light run/pre-execution receipts are finalized",
        "return": "complete light execution checkpoint RESULT",
        "packet_stage": "intent",
        "phase": "EXECUTE",
        "execution_mode": "fresh",
        "branch": "codex/v21-light",
        "base_authority": "sha:<computed:B>",
        "base": "<computed:B>",
        "acceptance_source": "call:v21-light#done_when",
        "acceptance_hash": "<computed:light-acceptance-hash>",
        "change_id": "v21-light",
        "product_result_path": "docs/results/v21-light.md",
        "validation_conformance_event_path": "history/conformance-light-result.md",
        "validation_conformance_event_payload_hash": "<computed:conformance-light-payload-hash>",
        "validation_conformance_receipt": "<computed:validation-conformance-receipt>",
        "toolchain_ref": "toolchain",
        "testability_mode": "coordinated-light",
        "light_ref": "light"
      }
    },
    "build_resume_child": {
      "inherits": "call_intents.execute_child",
      "delete": [
        "/owner_verdict_event_path",
        "/owner_verdict_event_payload_hash"
      ],
      "set": {
        "id": "c-build-progress",
        "goal": "resume only the exact accepted execution progress",
        "context": "same immutable PLAN/run plus RED and progress event payloads",
        "boundaries": "resume only; no frozen packet or independent-test edits",
        "done_when": "current progress is verified under the same run and acceptance",
        "return": "complete BUILD checkpoint or terminal product RESULT",
        "phase": "BUILD",
        "execution_mode": "resume",
        "run_id": "<computed:run-id>",
        "pre_red_head": "<computed:P>",
        "pre_execution_receipt": "<computed:preexec-receipt>",
        "owner_verdict_event": "history/owner-verdict-result.md@<computed:W-verdict-result>",
        "red_event": "history/red-result.md@<computed:E-red-accept>",
        "red_checkpoint": "<computed:R>",
        "red_manifest_hash": "<computed:oracle-manifest-hash>",
        "progress_event_path": "history/progress-result.md",
        "progress_event_payload_hash": "<computed:progress-payload-hash>",
        "progress_commit": "<computed:Q>",
        "progress_ledger_path": "history/progress-result.md",
        "progress_ledger_mode": "100644",
        "progress_ledger_blob": "<computed:q-accepted-ledger-blob>"
      }
    },
    "build_resume_red": {
      "inherits": "call_intents.build_resume_child",
      "set": {
        "id": "c-build-red",
        "progress_event_path": "history/red-result.md",
        "progress_event_payload_hash": "<computed:red-payload-hash>",
        "progress_commit": "<computed:R>",
        "progress_ledger_path": "history/red-result.md",
        "progress_ledger_blob": "<computed:red-accepted-ledger-blob>"
      }
    },
    "build_resume_progress": {
      "inherits": "call_intents.build_resume_child",
      "set": {}
    },
    "build_resume_chain": {
      "inherits": "call_intents.execute_child",
      "delete": [
        "/owner_verdict_event_path",
        "/owner_verdict_event_payload_hash"
      ],
      "set": {
        "id": "c-build-chain",
        "goal": "resume only the accepted two-commit independent RED chain",
        "context": "same immutable PLAN/run plus accepted R1->R2 event payload",
        "boundaries": "resume only; every chain commit remains test-author-only",
        "done_when": "R2 and its per-commit allowlist are verified under the same run",
        "return": "complete BUILD checkpoint or terminal product RESULT",
        "phase": "BUILD",
        "execution_mode": "resume",
        "run_id": "<computed:run-id>",
        "pre_red_head": "<computed:P>",
        "pre_execution_receipt": "<computed:preexec-receipt>",
        "owner_verdict_event": "history/owner-verdict-result.md@<computed:W-verdict-result>",
        "red_event": "history/red-chain-result.md@<computed:E-red-chain-accept>",
        "red_checkpoint": "<computed:R2>",
        "red_manifest_hash": "<computed:oracle-manifest-hash>",
        "progress_event_path": "history/red-chain-result.md",
        "progress_event_payload_hash": "<computed:red-chain-payload-hash>",
        "progress_commit": "<computed:R2>",
        "progress_ledger_path": "history/red-chain-result.md",
        "progress_ledger_mode": "100644",
        "progress_ledger_blob": "<computed:red-chain-ledger-blob>"
      }
    },
    "build_resume_chain_progress": {
      "inherits": "call_intents.build_resume_chain",
      "set": {
        "id": "c-build-chain-progress",
        "progress_event_path": "history/chain-progress-result.md",
        "progress_event_payload_hash": "<computed:chain-progress-payload-hash>",
        "progress_commit": "<computed:Q2>",
        "progress_ledger_path": "history/chain-progress-result.md",
        "progress_ledger_blob": "<computed:chain-progress-ledger-blob>"
      }
    },
    "build_resume_revision": {
      "inherits": "call_intents.build_resume_child",
      "set": {
        "id": "c-build-revision",
        "original_red_event": "history/red-result.md@<computed:E-red-accept>",
        "original_red_manifest_hash": "<computed:oracle-manifest-hash>",
        "revision_red_event": "history/revision-result.md@<computed:E-revision-accept>",
        "red_event": "history/revision-result.md@<computed:E-revision-accept>",
        "red_checkpoint": "<computed:T>",
        "red_manifest_hash": "<computed:oracle-revision-manifest-hash>",
        "progress_event_path": "history/revision-result.md",
        "progress_event_payload_hash": "<computed:revision-payload-hash>",
        "progress_commit": "<computed:T>",
        "progress_ledger_path": "history/revision-result.md",
        "progress_ledger_blob": "<computed:t-accepted-ledger-blob>"
      }
    },
    "build_resume_post_revision": {
      "inherits": "call_intents.build_resume_revision",
      "set": {
        "id": "c-build-post-revision",
        "progress_event_path": "history/post-revision-result.md",
        "progress_event_payload_hash": "<computed:post-revision-payload-hash>",
        "progress_commit": "<computed:U>",
        "progress_ledger_path": "history/post-revision-result.md",
        "progress_ledger_blob": "<computed:u-accepted-ledger-blob>"
      }
    },
    "build_resume_light": {
      "inherits": "call_intents.execute_light",
      "delete": [
        "/validation_conformance_event_path",
        "/validation_conformance_event_payload_hash"
      ],
      "set": {
        "id": "c-build-light",
        "goal": "resume only accepted coordinated-light progress",
        "context": "same light run and accepted progress payload",
        "done_when": "light result and gates are complete under the same identity",
        "return": "complete light BUILD checkpoint or terminal product RESULT",
        "phase": "BUILD",
        "execution_mode": "resume",
        "run_id": "<computed:light-run-id>",
        "pre_red_head": "<computed:B>",
        "pre_execution_receipt": "<computed:light-preexec-receipt>",
        "validation_conformance_event": "history/conformance-light-result.md@<computed:C-final-conformance-light>",
        "progress_event_path": "history/light-progress-result.md",
        "progress_event_payload_hash": "<computed:light-progress-payload-hash>",
        "progress_commit": "<computed:LQ>",
        "progress_ledger_path": "history/light-progress-result.md",
        "progress_ledger_mode": "100644",
        "progress_ledger_blob": "<computed:light-progress-ledger-blob>"
      }
    }
  },
  "writer_finalizations": {
    "setup_interview": {
      "intent_ref": "call_intents.setup_interview",
      "command": "writer-interview-guard",
      "writer_set": {
        "packet_stage": "finalized",
        "intent_hash": "<computed:setup-interview-intent-hash>",
        "finalization_receipt": "<computed:setup-interview-finalization-receipt>",
        "writer_observation_hash": "<computed:setup-interview-observation-hash>"
      }
    },
    "adapter_author": {
      "intent_ref": "call_intents.adapter_author_child",
      "command": "writer-event-guard adapter-author",
      "writer_set": {
        "packet_stage": "finalized",
        "interview_event": "history/setup-interview-result.md@<computed:I-setup-interview>",
        "intent_hash": "<computed:adapter-author-intent-hash>",
        "finalization_receipt": "<computed:adapter-author-finalization-receipt>",
        "writer_observation_hash": "<computed:adapter-author-observation-hash>"
      }
    },
    "adapter_review": {
      "intent_ref": "call_intents.adapter_review_child",
      "command": "writer-event-guard adapter-review",
      "writer_set": {
        "packet_stage": "finalized",
        "interview_event": "history/setup-interview-result.md@<computed:I-setup-interview>",
        "author_event": "history/adapter-author-result.md@<computed:I-adapter-author-result>",
        "intent_hash": "<computed:adapter-review-intent-hash>",
        "finalization_receipt": "<computed:adapter-review-finalization-receipt>",
        "writer_observation_hash": "<computed:adapter-review-observation-hash>"
      }
    },
    "setup_install_absent": {
      "intent_ref": "call_intents.setup_install_absent",
      "command": "tools/plan-handoff-check.fixture install",
      "writer_set": {
        "packet_stage": "finalized",
        "adapter_review_event": "history/adapter-review-result.md@<computed:I-adapter-accept>",
        "entry_state": "absent",
        "entry_git": "none",
        "protected_inventory_count": 0,
        "protected_inventory_hash": "<computed:empty-inventory-hash>",
        "conformance_bootstrap_challenge": "<computed:bootstrap-challenge>",
        "intent_hash": "<computed:setup-install-absent-intent-hash>",
        "finalization_receipt": "<computed:setup-install-absent-finalization-receipt>",
        "writer_observation_hash": "<computed:setup-install-absent-observation-hash>"
      }
    },
    "setup_install_empty": {
      "intent_ref": "call_intents.setup_install_empty",
      "command": "tools/plan-handoff-check.fixture install",
      "writer_set": {
        "packet_stage": "finalized",
        "adapter_review_event": "history/adapter-review-result.md@<computed:I-adapter-accept>",
        "entry_state": "empty",
        "entry_git": "none",
        "protected_inventory_count": 0,
        "protected_inventory_hash": "<computed:empty-inventory-hash>",
        "conformance_bootstrap_challenge": "<computed:bootstrap-challenge>",
        "intent_hash": "<computed:setup-install-empty-intent-hash>",
        "finalization_receipt": "<computed:setup-install-empty-finalization-receipt>",
        "writer_observation_hash": "<computed:setup-install-empty-observation-hash>"
      }
    },
    "setup_install_nonempty": {
      "intent_ref": "call_intents.setup_install_nonempty",
      "command": "tools/plan-handoff-check.fixture install",
      "writer_set": {
        "packet_stage": "finalized",
        "adapter_review_event": "history/adapter-review-result.md@<computed:I-adapter-accept>",
        "entry_state": "nonempty",
        "entry_git": "none",
        "protected_inventory_count": 1,
        "protected_inventory_hash": "<computed:setup-inventory-hash>",
        "conformance_bootstrap_challenge": "<computed:bootstrap-challenge>",
        "intent_hash": "<computed:setup-install-nonempty-intent-hash>",
        "finalization_receipt": "<computed:setup-install-nonempty-finalization-receipt>",
        "writer_observation_hash": "<computed:setup-install-nonempty-observation-hash>"
      }
    },
    "resync": {
      "intent_ref": "call_intents.resync",
      "command": "tools/plan-handoff-check.fixture install",
      "writer_set": {
        "packet_stage": "finalized",
        "head": "<computed:RB>",
        "adapter_review_event": "history/adapter-review-resync-result.md@<computed:I-resync-adapter-accept>",
        "protected_inventory_count": 3,
        "protected_inventory_hash": "<computed:resync-interview-inventory-hash>",
        "conformance_bootstrap_challenge": "<computed:bootstrap-challenge>",
        "intent_hash": "<computed:resync-intent-hash>",
        "finalization_receipt": "<computed:resync-finalization-receipt>",
        "writer_observation_hash": "<computed:resync-observation-hash>"
      }
    },
    "plan_author_bootstrap": {
      "intent_ref": "call_intents.plan_author_bootstrap",
      "command": "tools/plan-handoff-check.fixture plan-entry",
      "writer_set": {
        "packet_stage": "finalized",
        "head": "<computed:B>",
        "validation_conformance_event": "history/bootstrap-conformance-result.md@<computed:C-bootstrap-conformance>",
        "intent_hash": "<computed:plan-bootstrap-intent-hash>",
        "finalization_receipt": "<computed:plan-entry-bootstrap-finalization-receipt>",
        "writer_observation_hash": "<computed:plan-entry-observation-hash>"
      }
    },
    "plan_author": {
      "intent_ref": "call_intents.plan_author",
      "command": "tools/plan-handoff-check.fixture plan-entry",
      "writer_set": {
        "packet_stage": "finalized",
        "head": "<computed:B>",
        "validation_conformance_event": "history/conformance-result.md@<computed:C-final-conformance>",
        "intent_hash": "<computed:plan-intent-hash>",
        "finalization_receipt": "<computed:plan-entry-finalization-receipt>",
        "writer_observation_hash": "<computed:plan-entry-final-observation-hash>"
      }
    },
    "plan_verdict": {
      "intent_ref": "call_intents.plan_verdict_child",
      "command": "writer-event-guard plan-verdict",
      "writer_set": {
        "packet_stage": "finalized",
        "head": "<computed:P>",
        "plan_receipt_event": "history/plan-gated-result.md@<computed:W-plan-receipt>",
        "intent_hash": "<computed:verdict-intent-hash>",
        "finalization_receipt": "<computed:verdict-finalization-receipt>",
        "writer_observation_hash": "<computed:verdict-entry-observation-hash>"
      }
    },
    "execute": {
      "intent_ref": "call_intents.execute_child",
      "command": "tools/plan-handoff-check.fixture pre-execution",
      "writer_set": {
        "packet_stage": "finalized",
        "head": "<computed:P>",
        "owner_verdict_event": "history/owner-verdict-result.md@<computed:W-verdict-result>",
        "run_id": "<computed:run-id>",
        "pre_red_head": "<computed:P>",
        "pre_execution_receipt": "<computed:preexec-receipt>",
        "intent_hash": "<computed:execute-intent-hash>",
        "finalization_receipt": "<computed:preexec-finalization-receipt>",
        "writer_observation_hash": "<computed:preexec-observation-hash>"
      }
    },
    "execute_light": {
      "intent_ref": "call_intents.execute_light",
      "command": "tools/plan-handoff-check.fixture pre-execution",
      "writer_set": {
        "packet_stage": "finalized",
        "head": "<computed:B>",
        "validation_conformance_event": "history/conformance-light-result.md@<computed:C-final-conformance-light>",
        "run_id": "<computed:light-run-id>",
        "pre_red_head": "<computed:B>",
        "pre_execution_receipt": "<computed:light-preexec-receipt>",
        "intent_hash": "<computed:light-execute-intent-hash>",
        "finalization_receipt": "<computed:light-preexec-finalization-receipt>",
        "writer_observation_hash": "<computed:light-preexec-observation-hash>"
      }
    },
    "build_resume_red": {
      "intent_ref": "call_intents.build_resume_red",
      "command": "tools/plan-handoff-check.fixture resume",
      "writer_set": {
        "packet_stage": "finalized",
        "head": "<computed:R>",
        "progress_event": "history/red-result.md@<computed:E-red-accept>",
        "intent_hash": "<computed:resume-red-intent-hash>",
        "finalization_receipt": "<computed:resume-red-finalization-receipt>",
        "writer_observation_hash": "<computed:resume-red-observation-hash>"
      }
    },
    "build_resume_progress": {
      "intent_ref": "call_intents.build_resume_progress",
      "command": "tools/plan-handoff-check.fixture resume",
      "writer_set": {
        "packet_stage": "finalized",
        "head": "<computed:Q>",
        "progress_event": "history/progress-result.md@<computed:E-progress-accept>",
        "intent_hash": "<computed:resume-progress-intent-hash>",
        "finalization_receipt": "<computed:resume-progress-finalization-receipt>",
        "writer_observation_hash": "<computed:resume-progress-observation-hash>"
      }
    },
    "build_resume_chain": {
      "intent_ref": "call_intents.build_resume_chain",
      "command": "tools/plan-handoff-check.fixture resume",
      "writer_set": {
        "packet_stage": "finalized",
        "head": "<computed:R2>",
        "progress_event": "history/red-chain-result.md@<computed:E-red-chain-accept>",
        "intent_hash": "<computed:resume-red-chain-intent-hash>",
        "finalization_receipt": "<computed:resume-red-chain-finalization-receipt>",
        "writer_observation_hash": "<computed:resume-red-chain-observation-hash>"
      }
    },
    "build_resume_chain_progress": {
      "intent_ref": "call_intents.build_resume_chain_progress",
      "command": "tools/plan-handoff-check.fixture resume",
      "writer_set": {
        "packet_stage": "finalized",
        "head": "<computed:Q2>",
        "progress_event": "history/chain-progress-result.md@<computed:E-chain-progress-accept>",
        "intent_hash": "<computed:resume-progress-chain-intent-hash>",
        "finalization_receipt": "<computed:resume-progress-chain-finalization-receipt>",
        "writer_observation_hash": "<computed:resume-progress-chain-observation-hash>"
      }
    },
    "build_resume_revision": {
      "intent_ref": "call_intents.build_resume_revision",
      "command": "tools/plan-handoff-check.fixture resume",
      "writer_set": {
        "packet_stage": "finalized",
        "head": "<computed:T>",
        "progress_event": "history/revision-result.md@<computed:E-revision-accept>",
        "intent_hash": "<computed:resume-revision-intent-hash>",
        "finalization_receipt": "<computed:resume-revision-finalization-receipt>",
        "writer_observation_hash": "<computed:resume-revision-observation-hash>"
      }
    },
    "build_resume_post_revision": {
      "intent_ref": "call_intents.build_resume_post_revision",
      "command": "tools/plan-handoff-check.fixture resume",
      "writer_set": {
        "packet_stage": "finalized",
        "head": "<computed:U>",
        "progress_event": "history/post-revision-result.md@<computed:E-post-revision-accept>",
        "intent_hash": "<computed:resume-post-revision-intent-hash>",
        "finalization_receipt": "<computed:resume-post-revision-finalization-receipt>",
        "writer_observation_hash": "<computed:resume-post-revision-observation-hash>"
      }
    },
    "build_resume_light": {
      "intent_ref": "call_intents.build_resume_light",
      "command": "tools/plan-handoff-check.fixture resume",
      "writer_set": {
        "packet_stage": "finalized",
        "head": "<computed:LQ>",
        "progress_event": "history/light-progress-result.md@<computed:E-light-progress-accept>",
        "intent_hash": "<computed:resume-light-intent-hash>",
        "finalization_receipt": "<computed:resume-light-finalization-receipt>",
        "writer_observation_hash": "<computed:resume-light-observation-hash>"
      }
    }
  },
  "abi_contract": {
    "packet_wrapper_order": [
      "schema",
      "snapshot",
      "gate_mode",
      "transaction_stage",
      "finalized_call_bytes",
      "product_observation",
      "handback",
      "result_presence",
      "result_history_bytes"
    ],
    "entry_snapshots": [
      "plan_entry",
      "verdict_call",
      "execute",
      "execute_light",
      "resume_red",
      "resume_progress",
      "resume_red_chain",
      "resume_progress_chain",
      "resume_revision",
      "resume_post_revision",
      "resume_light"
    ],
    "gate_snapshots": [
      "setup_absent",
      "setup_empty",
      "setup",
      "resync",
      "deliver",
      "deliver_revision",
      "deliver_chain",
      "deliver_light"
    ],
    "return_snapshots": [
      "setup_interview",
      "adapter_author_call",
      "adapter_review_call",
      "adapter_review_resync_call",
      "plan_gated",
      "red_boundary",
      "red_chain",
      "red_revision",
      "close",
      "close_revision",
      "close_chain",
      "close_light"
    ],
    "return_result_ref": {
      "setup_interview": "SETUP_INTERVIEW_RESULT_BYTES",
      "adapter_author_call": "ADAPTER_AUTHOR_RESULT_BYTES",
      "adapter_review_call": "ADAPTER_REVIEW_RESULT_BYTES",
      "adapter_review_resync_call": "ADAPTER_REVIEW_RESYNC_RESULT_BYTES",
      "plan_gated": "PLAN_GATED_RESULT_BYTES",
      "red_boundary": "RED_RESULT_BYTES",
      "red_chain": "RED_CHAIN_RESULT_BYTES",
      "red_revision": "T_RESULT_BYTES",
      "close": "CLOSE_RESULT_HISTORY_BYTES",
      "close_revision": "CLOSE_REVISION_RESULT_HISTORY_BYTES",
      "close_chain": "CLOSE_CHAIN_RESULT_HISTORY_BYTES",
      "close_light": "CLOSE_LIGHT_RESULT_HISTORY_BYTES"
    },
    "conformance_gate_result_ref": {
      "setup_absent": "CONFORMANCE_RESULT_BYTES",
      "setup_empty": "CONFORMANCE_RESULT_BYTES",
      "setup": "CONFORMANCE_RESULT_BYTES",
      "resync": "CONFORMANCE_RESYNC_RESULT_BYTES"
    },
    "direction_only_snapshots": [
      "verdict_finalize_pending",
      "plan_after_owner"
    ],
    "handback_projection": {
      "setup_interview": [
        "result_evidence"
      ],
      "adapter_author_call": [
        "result_evidence"
      ],
      "adapter_review_call": [
        "result_evidence"
      ],
      "adapter_review_resync_call": [
        "result_evidence"
      ],
      "setup_absent": [],
      "setup_empty": [],
      "setup": [],
      "resync": [],
      "plan_entry": [
        "writer_authority"
      ],
      "plan_gated": [
        "plan_observation",
        "result_evidence",
        "plan_evidence"
      ],
      "verdict_call": [
        "writer_event",
        "open_call_commit"
      ],
      "execute": [],
      "execute_light": [],
      "red_boundary": [
        "red_evidence"
      ],
      "red_chain": [
        "red_evidence"
      ],
      "resume_red": [
        "writer_authority"
      ],
      "resume_progress": [
        "writer_authority"
      ],
      "resume_red_chain": [
        "writer_authority"
      ],
      "resume_progress_chain": [
        "writer_authority"
      ],
      "red_revision": [
        "writer_authority",
        "red_evidence"
      ],
      "resume_revision": [
        "writer_authority"
      ],
      "resume_post_revision": [
        "writer_authority"
      ],
      "deliver": [
        "writer_authority",
        "actual_acceptance",
        "deliver_evidence"
      ],
      "close": [
        "writer_authority",
        "actual_acceptance",
        "deliver_evidence",
        "close_evidence"
      ],
      "deliver_revision": [
        "writer_authority",
        "actual_acceptance",
        "deliver_evidence"
      ],
      "close_revision": [
        "writer_authority",
        "actual_acceptance",
        "deliver_evidence",
        "close_evidence"
      ],
      "deliver_chain": [
        "writer_authority",
        "actual_acceptance",
        "deliver_evidence"
      ],
      "close_chain": [
        "writer_authority",
        "actual_acceptance",
        "deliver_evidence",
        "close_evidence"
      ],
      "resume_light": [
        "writer_authority"
      ],
      "deliver_light": [
        "writer_authority",
        "actual_acceptance",
        "deliver_evidence"
      ],
      "close_light": [
        "writer_authority",
        "actual_acceptance",
        "deliver_evidence",
        "close_evidence"
      ]
    },
    "authority_slot_order": [
      "interview",
      "adapter-author",
      "adapter-review",
      "conformance",
      "plan",
      "owner-verdict",
      "red",
      "progress"
    ],
    "authority_required": {
      "setup_interview": [],
      "adapter_author_call": [
        "interview"
      ],
      "adapter_review_call": [
        "interview",
        "adapter-author"
      ],
      "adapter_review_resync_call": [
        "interview",
        "adapter-author"
      ],
      "setup_absent": [
        "interview",
        "adapter-author",
        "adapter-review"
      ],
      "setup_empty": [
        "interview",
        "adapter-author",
        "adapter-review"
      ],
      "setup": [
        "interview",
        "adapter-author",
        "adapter-review"
      ],
      "resync": [
        "interview",
        "adapter-author",
        "adapter-review"
      ],
      "plan_entry": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance"
      ],
      "plan_gated": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance"
      ],
      "verdict_call": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "plan"
      ],
      "execute": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "plan",
        "owner-verdict"
      ],
      "execute_light": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance"
      ],
      "red_boundary": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "plan",
        "owner-verdict"
      ],
      "red_chain": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "plan",
        "owner-verdict"
      ],
      "resume_red": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "plan",
        "owner-verdict",
        "red",
        "progress"
      ],
      "resume_progress": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "plan",
        "owner-verdict",
        "red",
        "progress"
      ],
      "resume_red_chain": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "plan",
        "owner-verdict",
        "red",
        "progress"
      ],
      "resume_progress_chain": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "plan",
        "owner-verdict",
        "red",
        "progress"
      ],
      "red_revision": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "plan",
        "owner-verdict",
        "red",
        "progress"
      ],
      "resume_revision": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "plan",
        "owner-verdict",
        "red",
        "progress"
      ],
      "resume_post_revision": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "plan",
        "owner-verdict",
        "red",
        "progress"
      ],
      "deliver": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "plan",
        "owner-verdict",
        "red",
        "progress"
      ],
      "close": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "plan",
        "owner-verdict",
        "red",
        "progress"
      ],
      "deliver_revision": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "plan",
        "owner-verdict",
        "red",
        "progress"
      ],
      "close_revision": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "plan",
        "owner-verdict",
        "red",
        "progress"
      ],
      "deliver_chain": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "plan",
        "owner-verdict",
        "red",
        "progress"
      ],
      "close_chain": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "plan",
        "owner-verdict",
        "red",
        "progress"
      ],
      "resume_light": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "progress"
      ],
      "deliver_light": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "progress"
      ],
      "close_light": [
        "interview",
        "adapter-author",
        "adapter-review",
        "conformance",
        "progress"
      ]
    }
  },
  "direction_transactions": {
    "base_files": {
      "NOW.md": "open_calls: {}\nnext: none\nEND_OF_FILE: live/fixture/NOW.md\n",
      "LOG.md": "# Log\n\nEND_OF_FILE: live/fixture/LOG.md\n"
    },
    "engineering_call_fields": [
      "CALL id",
      "to=executor",
      "direction=fixture",
      "play=work",
      "node=g-fixture",
      "task=t-fixture",
      "goal",
      "context",
      "boundaries",
      "done_when",
      "return",
      "budget",
      "repo=fixture/product",
      "kind=engineering",
      "packet-stage",
      "phase",
      "stage-or-mode",
      "worktree",
      "all stable engineering leaves in printed intent order",
      "writer block when finalized"
    ],
    "finalization_call_fields": [
      "CALL id",
      "to=executor",
      "direction=fixture",
      "play=work",
      "node=g-fixture",
      "task=t-fixture",
      "goal=materialize exactly one event-dependent child",
      "context.event_path",
      "context.event_session_id",
      "context.event_payload_hash",
      "context.child_intent_ref",
      "context.child_intent_hash",
      "boundaries=no owner dialogue|no product command|no other live delta",
      "done_when=fresh RESULT resolves persisted event mode/blob/commit and declares exact child replacement",
      "return=complete RESULT with bounded state_changes",
      "budget=one session",
      "repo=workflow/direction-os",
      "kind=mechanical"
    ],
    "full_result_fields": [
      "RESULT session-id (call: call-id)",
      "direction=fixture",
      "play=work",
      "node/task=g-fixture/t-fixture",
      "outcome",
      "evidence",
      "state_changes",
      "captures",
      "decisions_needed",
      "play_check=all five work steps",
      "log",
      "next=full CALL or awaiting_decision",
      "END_OF_FILE exact history path when persisted"
    ],
    "finalization_result_fields": [
      "all full_result_fields",
      "outcome=child finalized",
      "evidence=event path|mode|history-blob|strict-ancestor commit|semantic-payload-hash plus zero phase guard",
      "state_changes=append this full RESULT history|append one LOG line|remove this finalization call|add exact finalized child|set next child|regenerate declared panel",
      "next=exact full child CALL"
    ],
    "instances": [
      {
        "event_node": "I-setup-authorized",
        "child_node": "I-setup-interview-call",
        "event_kind": "setup-authorized",
        "event_path": "history/setup-authorized-result.md",
        "event_blob": "<computed:setup-authorized-result-blob>",
        "event_payload_hash": "<computed:setup-authorized-payload-hash>",
        "child_intent_ref": "call_intents.setup_interview",
        "child_id": "c-setup-interview"
      },
      {
        "event_node": "I-setup-interview",
        "child_node": "I-adapter-author-call",
        "event_kind": "setup-interview",
        "event_path": "history/setup-interview-result.md",
        "event_blob": "<computed:setup-interview-result-blob>",
        "event_payload_hash": "<computed:setup-interview-payload-hash>",
        "child_intent_ref": "call_intents.adapter_author_child",
        "child_id": "c-adapter-author"
      },
      {
        "event_node": "I-adapter-author-result",
        "child_node": "I-adapter-review-call",
        "event_kind": "adapter-authored",
        "event_path": "history/adapter-author-result.md",
        "event_blob": "<computed:adapter-author-result-blob>",
        "event_payload_hash": "<computed:adapter-author-payload-hash>",
        "event_adds": [
          {
            "path": "work/validation-adapters/<computed:stack-id>-v21.fixture",
            "mode": "100644",
            "blob": "<computed:accepted-adapter-blob>"
          },
          {
            "path": "work/validation-adapters/<computed:stack-id>-v21.manifest",
            "mode": "100644",
            "blob": "<computed:adapter-output-manifest-blob>"
          }
        ],
        "child_intent_ref": "call_intents.adapter_review_child",
        "child_id": "c-adapter-review"
      },
      {
        "event_node": "I-adapter-accept",
        "child_node": "I-install-call",
        "event_kind": "adapter-accepted",
        "event_path": "history/adapter-review-result.md",
        "event_blob": "<computed:adapter-review-result-blob>",
        "event_payload_hash": "<computed:adapter-review-payload-hash>",
        "child_intent_ref": "call_intents.setup_install_nonempty",
        "child_id": "c-setup-install"
      },
      {
        "event_node": "I-resync-adapter-accept",
        "child_node": "I-resync-call",
        "event_kind": "adapter-accepted-resync",
        "event_path": "history/adapter-review-resync-result.md",
        "event_blob": "<computed:adapter-review-resync-result-blob>",
        "event_payload_hash": "<computed:adapter-review-resync-payload-hash>",
        "child_intent_ref": "call_intents.resync",
        "child_id": "c-resync"
      },
      {
        "event_node": "C-final-conformance",
        "child_node": "C-plan-call",
        "event_kind": "final-conformance",
        "event_path": "history/conformance-result.md",
        "event_blob": "<computed:conformance-result-blob>",
        "event_payload_hash": "<computed:conformance-payload-hash>",
        "event_result_ref_by_parent": {
          "I-install-call": "CONFORMANCE_RESULT_BYTES",
          "I-resync-call": "CONFORMANCE_RESYNC_RESULT_BYTES"
        },
        "child_intent_ref": "call_intents.plan_author",
        "child_id": "c-plan-author"
      },
      {
        "event_node": "C-final-conformance-light",
        "child_node": "C-execute-light-call",
        "event_kind": "final-conformance-light",
        "event_path": "history/conformance-light-result.md",
        "event_blob": "<computed:conformance-light-result-blob>",
        "event_payload_hash": "<computed:conformance-light-payload-hash>",
        "child_intent_ref": "call_intents.execute_light",
        "child_id": "c-execute-light"
      },
      {
        "event_node": "W-plan-receipt",
        "child_node": "W-verdict-call",
        "event_kind": "plan-receipt",
        "event_path": "history/plan-gated-result.md",
        "event_blob": "<computed:plan-gated-result-blob>",
        "event_payload_hash": "<computed:plan-gated-payload-hash>",
        "child_intent_ref": "call_intents.plan_verdict_child",
        "child_id": "c-plan-verdict"
      },
      {
        "event_node": "W-verdict-result",
        "child_node": "W-execute-call",
        "event_kind": "owner-verdict",
        "event_path": "history/owner-verdict-result.md",
        "event_blob": "<computed:owner-verdict-result-blob>",
        "event_payload_hash": "<computed:owner-verdict-payload-hash>",
        "child_intent_ref": "call_intents.execute_child",
        "child_id": "c-execute"
      },
      {
        "event_node": "E-red-accept",
        "child_node": "E-build-red-call",
        "event_kind": "red-accepted",
        "event_path": "history/red-result.md",
        "event_blob": "<computed:red-result-blob>",
        "event_payload_blob": "<computed:red-accepted-ledger-blob>",
        "event_payload_hash": "<computed:red-payload-hash>",
        "child_intent_ref": "call_intents.build_resume_red",
        "child_id": "c-build-red"
      },
      {
        "event_node": "E-progress-accept",
        "child_node": "E-build-progress-call",
        "event_kind": "progress-accepted",
        "event_path": "history/progress-result.md",
        "event_blob": "<computed:progress-result-blob>",
        "event_payload_blob": "<computed:q-accepted-ledger-blob>",
        "event_payload_hash": "<computed:progress-payload-hash>",
        "child_intent_ref": "call_intents.build_resume_progress",
        "child_id": "c-build-progress"
      },
      {
        "event_node": "E-red-chain-accept",
        "child_node": "E-build-chain-call",
        "event_kind": "red-chain-accepted",
        "event_path": "history/red-chain-result.md",
        "event_blob": "<computed:red-chain-result-blob>",
        "event_payload_blob": "<computed:red-chain-ledger-blob>",
        "event_payload_hash": "<computed:red-chain-payload-hash>",
        "child_intent_ref": "call_intents.build_resume_chain",
        "child_id": "c-build-chain"
      },
      {
        "event_node": "E-chain-progress-accept",
        "child_node": "E-build-chain-progress-call",
        "event_kind": "chain-progress-accepted",
        "event_path": "history/chain-progress-result.md",
        "event_blob": "<computed:chain-progress-result-blob>",
        "event_payload_blob": "<computed:chain-progress-ledger-blob>",
        "event_payload_hash": "<computed:chain-progress-payload-hash>",
        "child_intent_ref": "call_intents.build_resume_chain_progress",
        "child_id": "c-build-chain-progress"
      },
      {
        "event_node": "E-revision-accept",
        "child_node": "E-build-revision-call",
        "event_kind": "revision-accepted",
        "event_path": "history/revision-result.md",
        "event_blob": "<computed:revision-result-blob>",
        "event_payload_blob": "<computed:t-accepted-ledger-blob>",
        "event_payload_hash": "<computed:revision-payload-hash>",
        "child_intent_ref": "call_intents.build_resume_revision",
        "child_id": "c-build-revision"
      },
      {
        "event_node": "E-post-revision-accept",
        "child_node": "E-build-post-revision-call",
        "event_kind": "post-revision-progress",
        "event_path": "history/post-revision-result.md",
        "event_blob": "<computed:post-revision-result-blob>",
        "event_payload_blob": "<computed:u-accepted-ledger-blob>",
        "event_payload_hash": "<computed:post-revision-payload-hash>",
        "child_intent_ref": "call_intents.build_resume_post_revision",
        "child_id": "c-build-post-revision"
      },
      {
        "event_node": "E-light-progress-accept",
        "child_node": "E-build-light-call",
        "event_kind": "light-progress",
        "event_path": "history/light-progress-result.md",
        "event_blob": "<computed:light-progress-result-blob>",
        "event_payload_blob": "<computed:light-progress-ledger-blob>",
        "event_payload_hash": "<computed:light-progress-payload-hash>",
        "child_intent_ref": "call_intents.build_resume_light",
        "child_id": "c-build-light"
      }
    ],
    "event_commit_tree": "parent tree plus exact full RESULT history file with trailer, one LOG line before trailer, NOW containing only the exact full mechanical finalization CALL and next=that id, and only the ordered instance-declared event_adds path/mode/blob when present; the finalizer CALL carries event path/session/payload hash but never the not-yet-known history blob or commit; all state trailers and declared panel exact",
    "child_commit_tree": "event tree plus exact finalizer RESULT history file, one LOG line before trailer, NOW with finalizer removed and only exact finalized child plus next=child id; no other path or field changes",
    "commit_metadata": {
      "event_message": "direction event <event_kind>",
      "child_message": "direction finalize <event_kind>",
      "author": "Direction OS <direction-os@invalid>",
      "time_rule": "2001-01-03T00:00:00Z plus instance ordinal*2 seconds"
    }
  },
  "snapshots": {
    "setup_interview": {
      "call_intent_ref": "call_intents.setup_interview",
      "writer_finalization_ref": "writer_finalizations.setup_interview",
      "gate_mode": "writer-interview",
      "direction_head": "<computed:I-setup-interview-call>",
      "result_evidence": {
        "target_inventory_count": 1,
        "target_inventory_hash": "<computed:interview-inventory-hash>",
        "product_writes": []
      }
    },
    "adapter_author_call": {
      "call_intent_ref": "call_intents.adapter_author_child",
      "writer_finalization_ref": "writer_finalizations.adapter_author",
      "gate_mode": "writer-adapter-author",
      "direction_head": "<computed:I-adapter-author-call>",
      "result_evidence": {
        "author_session": "<computed:adapter-author-session>",
        "profile_path": "os/engineering/profiles/fixture.md",
        "profile_mode": "100644",
        "profile_blob": "<external:stack-profile-blob>",
        "profile_sha256": "<external:stack-profile-sha256>",
        "adapter_source": "work/validation-adapters/<computed:stack-id>-v21.fixture",
        "adapter_mode": "100644",
        "adapter_blob": "<computed:accepted-adapter-blob>",
        "adapter_output_manifest_path": "work/validation-adapters/<computed:stack-id>-v21.manifest",
        "adapter_output_manifest_mode": "100644",
        "adapter_output_manifest_blob": "<computed:adapter-output-manifest-blob>",
        "adapter_output_manifest_hash": "<computed:adapter-output-manifest-hash>",
        "product_writes": []
      }
    },
    "adapter_review_call": {
      "call_intent_ref": "call_intents.adapter_review_child",
      "writer_finalization_ref": "writer_finalizations.adapter_review",
      "gate_mode": "writer-adapter-review",
      "direction_head": "<computed:I-adapter-review-call>",
      "result_evidence": {
        "reviewer_session": "<computed:adapter-review-session>",
        "author_session": "<computed:adapter-author-session>",
        "profile_path": "os/engineering/profiles/fixture.md",
        "profile_mode": "100644",
        "profile_blob": "<external:stack-profile-blob>",
        "profile_sha256": "<external:stack-profile-sha256>",
        "reviewed_source": "work/validation-adapters/<computed:stack-id>-v21.fixture",
        "reviewed_mode": "100644",
        "reviewed_blob": "<computed:accepted-adapter-blob>",
        "reviewed_output_manifest_path": "work/validation-adapters/<computed:stack-id>-v21.manifest",
        "reviewed_output_manifest_mode": "100644",
        "reviewed_output_manifest_blob": "<computed:adapter-output-manifest-blob>",
        "reviewed_output_manifest_hash": "<computed:adapter-output-manifest-hash>",
        "verdict": "GREEN",
        "product_writes": []
      }
    },
    "adapter_review_resync_call": {
      "inherits": "adapter_review_call",
      "gate_mode": "writer-adapter-review-resync",
      "direction_head": "<computed:I-adapter-review-call>"
    },
    "setup_absent": {
      "call_intent_ref": "call_intents.setup_install_absent",
      "writer_finalization_ref": "writer_finalizations.setup_install_absent",
      "entry_tree": "<computed:S-absent>",
      "tree": "<computed:SB-absent>",
      "gate_mode": "install",
      "direction_head": "<computed:I-install-call>",
      "variant_ref": "setup_variants.absent"
    },
    "setup_empty": {
      "inherits": "setup_absent",
      "call_intent_ref": "call_intents.setup_install_empty",
      "writer_finalization_ref": "writer_finalizations.setup_install_empty",
      "set": {
        "/entry_tree": "<computed:S-empty>",
        "/tree": "<computed:SB-empty>",
        "/variant_ref": "setup_variants.empty"
      }
    },
    "setup": {
      "call_intent_ref": "call_intents.setup_install_nonempty",
      "writer_finalization_ref": "writer_finalizations.setup_install_nonempty",
      "entry_tree": "<computed:S0>",
      "tree": "<computed:SB>",
      "gate_mode": "install",
      "direction_head": "<computed:I-install-call>"
    },
    "resync": {
      "call_intent_ref": "call_intents.resync",
      "writer_finalization_ref": "writer_finalizations.resync",
      "entry_tree": "<computed:RB>",
      "tree": "<computed:RS>",
      "gate_mode": "install",
      "direction_head": "<computed:I-resync-call>"
    },
    "plan_entry": {
      "call_intent_ref": "call_intents.plan_author_bootstrap",
      "writer_finalization_ref": "writer_finalizations.plan_author_bootstrap",
      "tree": "<computed:B>",
      "gate_mode": "plan-entry",
      "writer_authority": {
        "conformance_receipt": "<computed:bootstrap-receipt>",
        "source": "bootstrap-stage-A-observed-rows"
      }
    },
    "plan_gated": {
      "inherits": "plan_entry",
      "call_intent_ref": "call_intents.plan_author",
      "writer_finalization_ref": "writer_finalizations.plan_author",
      "tree": "<computed:P>",
      "gate_mode": "plan",
      "plan_observation": {
        "command": "tools/plan-handoff-check.fixture plan",
        "exit": 0,
        "status_before": "clean:<computed:P>",
        "status_after": "clean:<computed:P>",
        "hash": "<computed:plan-observation-hash>"
      },
      "result_evidence": {
        "checkpoint": "PLAN-GATED",
        "owner_verdict": "<absent>"
      },
      "plan_evidence": {
        "observed_head": "<computed:P>",
        "plan_candidate_head": "<computed:P>",
        "plan_observation_hash": "<computed:plan-observation-hash>",
        "plan_receipt": "<computed:plan-receipt>",
        "testability_ref": "testability_pin+testability"
      }
    },
    "verdict_finalize_pending": {
      "gate_mode": "writer-finalization",
      "direction_head": "<computed:W-plan-receipt>",
      "event": {
        "path": "history/<computed:plan-gated-result-path>",
        "mode": "100644",
        "blob": "<computed:plan-gated-result-blob>"
      },
      "finalization_call": {
        "id": "c-finalize-plan-verdict",
        "kind": "mechanical",
        "child_intent_ref": "call_intents.plan_verdict_child",
        "event_path": "history/<computed:plan-gated-result-path>",
        "event_session_id": "plan-author",
        "event_payload_hash": "<computed:plan-gated-payload-hash>",
        "allowed_state_delta": "history+LOG+replace-this-call-only"
      }
    },
    "verdict_call": {
      "inherits": "plan_gated",
      "call_intent_ref": "call_intents.plan_verdict_child",
      "writer_finalization_ref": "writer_finalizations.plan_verdict",
      "gate_mode": "writer-verdict-entry",
      "direction_head": "<computed:W-verdict-call>",
      "writer_event": {
        "path": "history/<computed:plan-gated-result-path>",
        "mode": "100644",
        "blob": "<computed:plan-gated-result-blob>",
        "commit": "<computed:W-plan-receipt>"
      },
      "open_call_commit": "<computed:W-verdict-call>"
    },
    "plan_after_owner": {
      "inherits": "verdict_call",
      "gate_mode": "writer-verdict-return",
      "direction_head": "<computed:W-verdict-result>",
      "result_evidence": {
        "owner_words": "ACCEPT exact candidate <computed:P> receipt <computed:plan-receipt>",
        "plan_receipt_event": "history/<computed:plan-gated-result-path>@<computed:W-plan-receipt>"
      },
      "execute_finalization_call": {
        "id": "c-finalize-execute",
        "kind": "mechanical",
        "child_intent_ref": "call_intents.execute_child",
        "event_path": "history/<computed:owner-verdict-result-path>",
        "event_session_id": "plan-verdict",
        "event_payload_hash": "<computed:owner-verdict-payload-hash>"
      }
    },
    "execute": {
      "inherits": "plan_after_owner",
      "call_intent_ref": "call_intents.execute_child",
      "writer_finalization_ref": "writer_finalizations.execute",
      "direction_head": "<computed:W-execute-call>",
      "gate_mode": "pre-execution"
    },
    "execute_light": {
      "call_intent_ref": "call_intents.execute_light",
      "writer_finalization_ref": "writer_finalizations.execute_light",
      "tree": "<computed:B>",
      "gate_mode": "pre-execution"
    },
    "resume_light": {
      "inherits": "execute_light",
      "call_intent_ref": "call_intents.build_resume_light",
      "writer_finalization_ref": "writer_finalizations.build_resume_light",
      "tree": "<computed:LQ>",
      "gate_mode": "resume",
      "writer_authority": {
        "event": "history/<computed:light-progress-result-path>@<computed:E-light-progress-accept>",
        "payload_hash": "<computed:light-progress-ledger-blob>"
      }
    },
    "deliver_light": {
      "inherits": "resume_light",
      "tree": "<computed:LD>",
      "gate_mode": "deliver",
      "actual_acceptance": {
        "scan_exit": 0,
        "matched_paths": [],
        "run_exit": 0,
        "stdout_hash": "<computed:light-deliver-stdout-hash>"
      },
      "deliver_evidence": {
        "observed_head": "<computed:LD>",
        "prearchive_commit": "<computed:LD>",
        "product_result_path": "docs/results/v21-light.md",
        "result_blob": "<computed:light-result-blob>"
      }
    },
    "close_light": {
      "inherits": "deliver_light",
      "tree": "<computed:LD>",
      "gate_mode": "close",
      "close_evidence": {
        "observed_head": "<computed:LD>",
        "archive": {
          "deliver": "<computed:LD>",
          "archive": "<computed:LD>",
          "archive_parent": "<absent>",
          "archive_parent_count": 0,
          "source": "n/a-light",
          "target": "n/a-light"
        }
      }
    },
    "red_boundary": {
      "inherits": "execute",
      "call_intent_ref": "call_intents.execute_child",
      "writer_finalization_ref": "writer_finalizations.execute",
      "tree": "<computed:R>",
      "gate_mode": "red-boundary",
      "red_evidence": {
          "observed_head": "<computed:R>",
          "author_role": "independent-test-author",
          "author_session": "fixture-red-1",
          "parent_head": "<computed:P>",
          "checkpoint": "<computed:R>",
          "chain": [
            "<computed:R>"
          ],
          "allowed_delta": [
            "tests/FixtureTests.fixture",
            "docs/validation/oracle-v21-fixture.json"
          ],
          "manifest_hash": "<computed:oracle-manifest-hash>",
          "compile_exit": 0,
          "compile_stdout_hash": "<computed:red-compile-stdout-hash>",
          "unique_ids": [
            "FixtureTests.OB_1",
            "FixtureTests.OB_2",
            "FixtureTests.OB_3"
          ],
          "registration": "Fixture.Tests",
          "filter": "FixtureTests.OB_*",
          "discovery_count": 3,
          "discovery_stdout_hash": "<computed:red-discover-stdout-hash>",
          "expected": [
            "DW-1 missing member",
            "DW-2 loopback count",
            "DW-3 golden mismatch"
          ],
          "run_exit": 1,
          "run_stdout_hash": "<computed:red-run-stdout-hash>",
          "status": "RED",
          "revisions": []
      }
    },
    "red_chain": {
      "inherits": "red_boundary",
      "call_intent_ref": "call_intents.execute_child",
      "writer_finalization_ref": "writer_finalizations.execute",
      "tree": "<computed:R2>",
      "gate_mode": "red-boundary",
      "red_evidence": {
        "inherits": "red_boundary.red_evidence",
        "set": {
          "/observed_head": "<computed:R2>",
          "/checkpoint": "<computed:R2>",
          "/chain": ["<computed:R1>", "<computed:R2>"],
          "/per_commit_allowed_delta": [
          {
            "commit": "<computed:R1>",
            "paths": [
              "tests/FixtureTests.fixture"
            ]
          },
          {
            "commit": "<computed:R2>",
            "paths": [
              "docs/validation/oracle-v21-fixture.json"
            ]
          }
          ]
        }
      }
    },
    "resume_red": {
      "inherits": "red_boundary",
      "call_intent_ref": "call_intents.build_resume_red",
      "writer_finalization_ref": "writer_finalizations.build_resume_red",
      "tree": "<computed:R>",
      "gate_mode": "resume",
      "writer_authority": {
        "event": "history/<computed:red-result-path>@<computed:E-red-accept>",
        "payload_hash": "<computed:red-accepted-ledger-blob>"
      }
    },
    "resume_progress": {
      "inherits": "resume_red",
      "call_intent_ref": "call_intents.build_resume_progress",
      "writer_finalization_ref": "writer_finalizations.build_resume_progress",
      "tree": "<computed:Q>",
      "writer_authority": {
        "event": "history/<computed:progress-result-path>@<computed:E-progress-accept>",
        "payload_hash": "<computed:q-accepted-ledger-blob>"
      }
    },
    "resume_red_chain": {
      "inherits": "red_chain",
      "call_intent_ref": "call_intents.build_resume_chain",
      "writer_finalization_ref": "writer_finalizations.build_resume_chain",
      "tree": "<computed:R2>",
      "gate_mode": "resume",
      "writer_authority": {
        "event": "history/red-chain-result.md@<computed:E-red-chain-accept>",
        "payload_hash": "<computed:red-chain-ledger-blob>"
      }
    },
    "resume_progress_chain": {
      "inherits": "resume_red_chain",
      "call_intent_ref": "call_intents.build_resume_chain_progress",
      "writer_finalization_ref": "writer_finalizations.build_resume_chain_progress",
      "tree": "<computed:Q2>",
      "writer_authority": {
        "event": "history/chain-progress-result.md@<computed:E-chain-progress-accept>",
        "payload_hash": "<computed:chain-progress-ledger-blob>"
      }
    },
    "red_revision": {
      "inherits": "resume_progress",
      "call_intent_ref": "call_intents.build_resume_progress",
      "writer_finalization_ref": "writer_finalizations.build_resume_progress",
      "tree": "<computed:T>",
      "gate_mode": "red-boundary",
      "red_evidence": {
        "observed_head": "<computed:T>",
        "revision":
          {
            "author_role": "independent-test-author",
            "author_session": "fixture-red-2",
            "parent_head": "<computed:Q>",
            "checkpoint": "<computed:T>",
            "chain": [
              "<computed:T>"
            ],
            "allowed_delta": [
              "tests/FixtureTestsV2.fixture",
              "docs/validation/oracle-v21-fixture-v2.json"
            ],
            "original_event": "history/<computed:red-result-path>@<computed:E-red-accept>",
            "original_manifest_hash": "<computed:oracle-manifest-hash>",
            "variant_manifest_hash": "<computed:oracle-revision-manifest-hash>",
            "compile_exit": 0,
            "compile_stdout_hash": "<computed:revision-compile-stdout-hash>",
            "unique_ids": [
              "FixtureTests.OB_1",
              "FixtureTests.OB_2",
              "FixtureTests.OB_3",
              "FixtureTests.OB_1_V2",
              "FixtureTests.OB_2_V2",
              "FixtureTests.OB_3_V2"
            ],
            "registration": "Fixture.Tests",
            "filter": "FixtureTests.OB_*",
            "discovery_count": 6,
            "discovery_stdout_hash": "<computed:revision-discover-stdout-hash>",
            "original_status": "PASS",
            "expected_variant_red": [
              "DW-1 exact result variant mismatch",
              "DW-2 nested loopback count",
              "DW-3 hidden audit mismatch"
            ],
            "run_exit": 1,
            "run_stdout_hash": "<computed:revision-run-stdout-hash>",
            "status": "RED"
          }
      }
    },
    "resume_revision": {
      "inherits": "red_revision",
      "call_intent_ref": "call_intents.build_resume_revision",
      "writer_finalization_ref": "writer_finalizations.build_resume_revision",
      "tree": "<computed:T>",
      "gate_mode": "resume",
      "writer_authority": {
        "event": "history/<computed:revision-result-path>@<computed:E-revision-accept>",
        "payload_hash": "<computed:t-accepted-ledger-blob>"
      }
    },
    "resume_post_revision": {
      "inherits": "resume_revision",
      "call_intent_ref": "call_intents.build_resume_post_revision",
      "writer_finalization_ref": "writer_finalizations.build_resume_post_revision",
      "tree": "<computed:U>",
      "writer_authority": {
        "event": "history/<computed:post-revision-result-path>@<computed:E-post-revision-accept>",
        "payload_hash": "<computed:u-accepted-ledger-blob>"
      }
    },
    "deliver": {
      "inherits": "resume_progress",
      "tree": "<computed:D>",
      "gate_mode": "deliver",
      "actual_acceptance": {
        "compile_exit": 0,
        "compile_stdout_hash": "<computed:deliver-compile-stdout-hash>",
        "discovery_exit": 0,
        "discovery_count": 3,
        "ids": [
          "FixtureTests.OB_1",
          "FixtureTests.OB_2",
          "FixtureTests.OB_3"
        ],
        "discovery_stdout_hash": "<computed:deliver-discover-stdout-hash>",
        "run_exit": 0,
        "status": "PASS",
        "criteria": [
          "DW-1 absent Create exact result",
          "DW-2 existing Step loopback once",
          "DW-3 source-isolated golden audit"
        ],
        "run_stdout_hash": "<computed:deliver-run-stdout-hash>"
      },
      "deliver_evidence": {
        "observed_head": "<computed:D>",
        "prearchive_commit": "<computed:D>",
        "product_result_path": "docs/results/v21-fixture-change.md",
        "result_blob": "<computed:result-blob>"
      }
    },
    "close": {
      "inherits": "deliver",
      "tree": "<computed:A>",
      "gate_mode": "close",
      "close_evidence": {
        "observed_head": "<computed:A>",
        "archive": {
          "deliver": "<computed:D>",
          "archive": "<computed:A>",
          "archive_parent": "<computed:D>",
          "archive_parent_count": 1,
          "source": "openspec/changes/v21-fixture-change",
          "target": "openspec/changes/archive/v21-fixture-change"
        }
      }
    },
    "deliver_revision": {
      "inherits": "resume_post_revision",
      "tree": "<computed:D2>",
      "gate_mode": "deliver",
      "actual_acceptance": {
        "compile_exit": 0,
        "compile_stdout_hash": "<computed:deliver-revision-compile-stdout-hash>",
        "discovery_exit": 0,
        "discovery_count": 6,
        "ids": [
          "FixtureTests.OB_1",
          "FixtureTests.OB_2",
          "FixtureTests.OB_3",
          "FixtureTests.OB_1_V2",
          "FixtureTests.OB_2_V2",
          "FixtureTests.OB_3_V2"
        ],
        "discovery_stdout_hash": "<computed:deliver-revision-discover-stdout-hash>",
        "run_exit": 0,
        "status": "PASS",
        "criteria": [
          "DW-1 absent Create exact result",
          "DW-2 existing Step loopback once",
          "DW-3 source-isolated golden audit",
          "DW-1 exact result variant mismatch",
          "DW-2 nested loopback count",
          "DW-3 hidden audit mismatch"
        ],
        "run_stdout_hash": "<computed:deliver-revision-run-stdout-hash>"
      },
      "deliver_evidence": {
        "observed_head": "<computed:D2>",
        "prearchive_commit": "<computed:D2>",
        "product_result_path": "docs/results/v21-fixture-change.md",
        "result_blob": "<computed:result-revision-blob>"
      }
    },
    "close_revision": {
      "inherits": "deliver_revision",
      "tree": "<computed:A2>",
      "gate_mode": "close",
      "close_evidence": {
        "observed_head": "<computed:A2>",
        "archive": {
          "deliver": "<computed:D2>",
          "archive": "<computed:A2>",
          "archive_parent": "<computed:D2>",
          "archive_parent_count": 1,
          "source": "openspec/changes/v21-fixture-change",
          "target": "openspec/changes/archive/v21-fixture-change"
        }
      }
    },
    "deliver_chain": {
      "inherits": "resume_progress_chain",
      "tree": "<computed:D3>",
      "gate_mode": "deliver",
      "actual_acceptance": {
        "compile_exit": 0,
        "compile_stdout_hash": "<computed:deliver-chain-compile-stdout-hash>",
        "discovery_exit": 0,
        "discovery_count": 3,
        "ids": [
          "FixtureTests.OB_1",
          "FixtureTests.OB_2",
          "FixtureTests.OB_3"
        ],
        "discovery_stdout_hash": "<computed:deliver-chain-discover-stdout-hash>",
        "run_exit": 0,
        "status": "PASS",
        "criteria": [
          "DW-1 absent Create exact result",
          "DW-2 existing Step loopback once",
          "DW-3 source-isolated golden audit"
        ],
        "run_stdout_hash": "<computed:deliver-chain-run-stdout-hash>"
      },
      "deliver_evidence": {
        "observed_head": "<computed:D3>",
        "prearchive_commit": "<computed:D3>",
        "product_result_path": "docs/results/v21-fixture-change.md",
        "result_blob": "<computed:result-chain-blob>"
      }
    },
    "close_chain": {
      "inherits": "deliver_chain",
      "tree": "<computed:A3>",
      "gate_mode": "close",
      "close_evidence": {
        "observed_head": "<computed:A3>",
        "archive": {
          "deliver": "<computed:D3>",
          "archive": "<computed:A3>",
          "archive_parent": "<computed:D3>",
          "archive_parent_count": 1,
          "source": "openspec/changes/v21-fixture-change",
          "target": "openspec/changes/archive/v21-fixture-change"
        }
      }
    }
  }
}
```

## Exact Direction event-to-child graph

The JSON `direction_transactions` is rendered with these exact LF byte functions. Every placeholder is supplied by one listed instance; no timestamp or field is optional.

```text
CANONICAL_LF_JSON(x)=UTF-8 JSON with object insertion order, array order preserved, two-space indent, lowercase `true|false|null`, decimal integers, JSON escaping, no trailing spaces and exactly one final LF. `block(k,v)=k+": |\n"+indent(v,2)`, where `v` already has exactly one final LF. A scalar row is `hyphenated-key+": "+JSON-scalar-without-final-LF+"\n"`; an object/array row is `block(hyphenated-key,CANONICAL_LF_JSON(value))`. Duplicate key, unsupported number, invalid UTF-8 or non-final LF fails.
ENGINEERING_INTENT_CALL_BYTES=exact Markdown: "CALL <id>\n" + "to: executor\ndirection: fixture\nplay: work\nnode: g-fixture  task: t-fixture\n" + block("goal",goal+"\n") + block("context",context+"\n") + block("boundaries",boundaries+"\n") + block("done_when",done_when+"\n") + block("return",return+"\n") + "budget: one session\nrepo: fixture/product\nkind: engineering\n" + every remaining fully expanded `call_intents` member as the scalar/object row above in its resolved insertion order. It contains `packet-stage: intent`, every stable intent leaf and no `writer` key.
FINALIZE_OBJECT(intent,finalization)=require `finalization.intent_ref` is that exact intent; deep-copy the fully expanded intent; require `packet_stage=="intent"`; set only it to `"finalized"`; then add every other exact `writer_set` key/value in printed order; reject overlap, omission, extra leaf or unresolved token. `FINALIZED_ENGINEERING_CALL_BYTES` renders that complete object with the same header/stable rows and then `block("writer",CANONICAL_LF_JSON(writer_set minus packet_stage))`. `PROJECT_STABLE(FINALIZED_ENGINEERING_CALL_BYTES)` removes exactly that writer block and restores only the stage token; it must equal `ENGINEERING_INTENT_CALL_BYTES` byte-for-byte.
FINALIZER_CALL_BYTES=exact Markdown: "CALL <finalizer-id>\nto: executor\ndirection: fixture\nplay: work\nnode: g-fixture  task: t-fixture\n" + the exact goal/context/boundaries/done_when/return/budget values in `direction_transactions.finalization_call_fields` rendered by the same block rule + "repo: workflow/direction-os\nkind: mechanical\n". Context carries event path, event session id, semantic payload hash, child intent ref and hash; it cannot contain the event history blob or commit before persistence.
FULL_RESULT_PACKET_BYTES=exact Markdown: "RESULT <session-id> (call: <call-id>)\ndirection: fixture   play: work   node/task: g-fixture/t-fixture\n" + block("outcome",outcome+"\n") + block("evidence",evidence+"\n") + block("state_changes",complete-stable-target-delta+"\n") + "captures: []\ndecisions_needed: []\nplay_check:\n  - 1 Recite: done\n  - 2 Owner inputs: skipped - mechanical or engineering evidence is not owner-content\n  - 3 Do the work: done\n  - 4 Self-check: done - exact done_when evidence compared\n  - 5 Close: done\nlog: <exact-one-line-log>\n" + block("next",(exact complete CALL bytes or "awaiting_decision\n")). Every argument in angle brackets is supplied by the selected `direction_transactions.instances` row before hashing; none remains in emitted bytes. Owner-verdict RESULT replaces only step 2 with `done - owner words: <exact words>`.
FULL_RESULT_HISTORY_BYTES=FULL_RESULT_PACKET_BYTES + "END_OF_FILE: live/fixture/history/<exact-event-result-file>\n". The history blob is computed only after these complete acyclic bytes exist; a ledger payload is evidence and never substitutes for this file.
FINALIZER_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES for the finalizer session, with evidence equal exact event path|mode|history-blob|strict-ancestor commit|semantic-payload-hash plus zero phase guard; state_changes append this RESULT history and one LOG line, remove only the finalizer CALL, add exact FINALIZED_ENGINEERING_CALL_BYTES, set next to that child and regenerate only a declared panel; next contains the exact complete child CALL.
FINALIZED_CHILD_BYTES=FINALIZED_ENGINEERING_CALL_BYTES for the exact expanded child intent and matching writer finalization
EVENT_NOW_BYTES="open_calls:\n  <finalizer-id>: |\n" + indent(FINALIZER_CALL_BYTES,4) + "next: <finalizer-id>\nEND_OF_FILE: live/fixture/NOW.md\n"
CHILD_NOW_BYTES="open_calls:\n  <child-id>: |\n" + indent(FINALIZED_CHILD_BYTES,4) + "next: <child-id>\nEND_OF_FILE: live/fixture/NOW.md\n"
EVENT_LOG_BYTES=prior LOG bytes before trailer + "event <event-kind> | history/<event-result>.md | finalizer <finalizer-id>\nEND_OF_FILE: live/fixture/LOG.md\n"
CHILD_LOG_BYTES=EVENT_LOG_BYTES before trailer + "finalized <event-kind> | history/<finalizer-result>.md | child <child-id>\nEND_OF_FILE: live/fixture/LOG.md\n"
EVENT_TREE=parent tree with NOW=EVENT_NOW_BYTES, LOG=EVENT_LOG_BYTES, the selected instance event_path=FULL_RESULT_HISTORY_BYTES whose blob equals event_blob, plus every ordered path/mode/blob only when that instance prints `event_adds`; no other delta
CHILD_TREE=EVENT_TREE with NOW=CHILD_NOW_BYTES, LOG=CHILD_LOG_BYTES, history/<finalizer-result>.md=FINALIZER_RESULT_BYTES; no other delta
```

The fixture has no owner panel; a direction declaring one adds exactly its deterministic rendered postimage to both allowed trees. `I-direction-base` is a root commit containing exactly `direction_transactions.base_files`, with constant identity/time, message `direction fixture base\n` and no open CALL. The normal first transaction is the printed `I-setup-authorized -> I-setup-interview-call` event/child pair produced from `call_intents.setup_interview`; there is no magic writer-created CALL. Adapter author RESULT and fresh review CALL are separate event/child commits; setup-install and re-sync adapter-review acceptance rows are alternative branches from the same accepted author/review contour, never siblings in one NOW. The printed setup-install instance is the nonempty canonical; `EACH_SETUP_CREATE` substitutes its matching `setup_install_absent|setup_install_empty` child intent and matching interview inventory before computing event/child commits. The post-install conformance checker invocation is an internal packet gate with no RESULT field; the subsequent Direction event persists a complete result selected exactly by `abi_contract.conformance_gate_result_ref`: every SETUP install uses `CONFORMANCE_RESULT_BYTES` with call `c-setup-install`, while RE-SYNC uses `CONFORMANCE_RESYNC_RESULT_BYTES` with call `c-resync`. Both alternative branches may use the canonical history path `history/conformance-result.md`, but their complete bytes, blobs, payloads and finalizer ids are distinct and cannot be substituted. `C-bootstrap-conformance` is a nonce-local disposable Direction authority commit containing `BOOTSTRAP_CONFORMANCE_RESULT_BYTES`; it exists only while exercising stage-A non-install rows, is not written to live state and cannot be cited by a real CALL. `FINAL_VIEW` replaces it with the branch-selected persisted `C-final-conformance` and final receipt. Every later arrow is a strict parent/ancestor relation. Exact commit chains and messages are:

```text
I-direction-base -> I-setup-authorized -> I-setup-interview-call -> I-setup-interview -> I-adapter-author-call -> I-adapter-author-result -> I-adapter-review-call -> I-adapter-accept -> I-install-call -> C-final-conformance -> C-plan-call -> W-plan-receipt -> W-verdict-call -> W-verdict-result -> W-execute-call -> E-red-accept -> E-build-red-call -> E-progress-accept -> E-build-progress-call -> E-revision-accept -> E-build-revision-call -> E-post-revision-accept -> E-build-post-revision-call
I-direction-base -> I-setup-authorized -> I-setup-interview-call -> I-setup-interview -> I-adapter-author-call -> I-adapter-author-result -> I-adapter-review-call -> I-resync-adapter-accept -> I-resync-call -> C-final-conformance -> C-plan-call
W-execute-call -> E-red-chain-accept -> E-build-chain-call -> E-chain-progress-accept -> E-build-chain-progress-call
C-final-conformance-light -> C-execute-light-call -> E-light-progress-accept -> E-build-light-call
event nodes use EVENT_TREE and message "direction event <event-kind>\n"
immediate child nodes use CHILD_TREE, parent=their event node, message "direction finalize <event-kind>\n"
all later event nodes have the preceding finalized child as ancestor and contain their own exact event payload
```

`RED_LEDGER_BYTES`, `Q_LEDGER_BYTES`, `RED_CHAIN_LEDGER_BYTES`, `CHAIN_PROGRESS_LEDGER_BYTES`, `T_LEDGER_BYTES`, `U_LEDGER_BYTES` and `LIGHT_LEDGER_BYTES` below are semantic evidence payloads only. Their corresponding `*_RESULT_BYTES` are complete persisted RESULT histories with every envelope/play-check/next/trailer field. The setup interview, adapter acceptance, final conformance, PLAN-GATED and owner-verdict event bytes use the same full RESULT schema with the exact receipt/inventory/adapter/candidate/owner fields below. A commit containing both an event and its `@self` finalized child is impossible and corpus-invalid.

## Exact product-tree graph

The adapter maps these exact abstract bytes to stack-native files; its pinned output manifest is checked before use. `REPLACE_EXACT(bytes,old,new)` requires exactly one byte occurrence and replaces it without normalization, otherwise materialization fails. The plan probe is not a schema-only walk: for every recipe it writes the exact `red_realization.source_bytes`, writes every listed compile-only `binding_sources` object and every separately listed `runtime_resources` object to its pinned nonce path, verifies both lists equal their typed reachable registry closures, passes only the test source plus every compile-source path explicitly to the pinned real compiler against the pinned baseline project/friend assembly, invokes the pinned discovery tool against that exact compiled output, then passes every runtime resource as exact `path@mode@blob` only to the pinned runner for the uniquely discovered filtered test against exact base. Compiler and discovery never receive runtime-resource paths; runner never loads an unlisted path. Compile/discovery/run commands, identities, exits, ids, status, criterion and stdout are captured from those processes, not copied from JSON; each recipe must return its declared runtime RED criterion. It also compiles the concatenated three-source set with the exact de-duplicated union compile-source order, supplies the exact union runtime-resource order only to each filtered run, and requires exactly the union of the three ids; a missing/extra helper or resource, per-recipe success with union compile/discovery failure, command/list disagreement, substituted runtime, PASS or wrong RED criterion is nonzero. The later RED and DELIVER probes repeat compilation/discovery/runtime against the protected tree, including the newest accepted test revision.

```text
CONFIG_V21="synced_contract_version: 21\nplan_handoff_check: tools/plan-handoff-check.fixture\nplan_handoff_modes: install,plan-entry,plan,pre-execution,red-boundary,resume,deliver,close\nplan_handoff_trust_roots: validation.config@100644,tools/plan-handoff-check.fixture@100644,tools/plan-handoff-schema.fixture@100644,tools/fixture-compiler.fixture@100755,tools/fixture-discover.fixture@100755,tests/FixtureRunner.fixture@100755\nproduct_result_template: docs/results/{change-id}.md\nproduct_result_required_fields: change-id,base-authority,acceptance-hash,run-id,location,archive-source,archive-target,outcome,evidence,assumptions,cuts,cost,manual-acceptance,next\n"
CONFIG_V20="synced_contract_version: 20\nproduct_result_template: docs/results/{change-id}.md\n"
CHECKER_BYTES="fixture-checker v21\ninput: exact packet+authority ABI\nmodes: install,plan-entry,plan,pre-execution,red-boundary,resume,deliver,close\n"
SCHEMA_BYTES="fixture-schema v21\npacket: full-call+handback+result-history\nauthority-slots: interview,adapter-author,adapter-review,conformance,plan,owner-verdict,red,progress\n"
COMPILER_BYTES="fixture-compiler v1\ninput: base+one test source+ordered compile sources\noutput: exact assembly blob\n"
DISCOVER_BYTES="fixture-discover v1\ninput: exact assembly+filter\noutput: ordered unique ids\n"
RUNNER_BYTES="fixture-runner v1\ninput: exact assembly+filter+ordered runtime resources path@mode@blob\noutput: exact status+criterion\n"
`config-blob=GIT_BLOB(CONFIG_V21)`, `checker-blob=GIT_BLOB(CHECKER_BYTES)`, `schema-blob=GIT_BLOB(SCHEMA_BYTES)`, `fixture-compiler-blob=GIT_BLOB(COMPILER_BYTES)`, `fixture-discover-blob=GIT_BLOB(DISCOVER_BYTES)`, and `test-runner-blob=GIT_BLOB(RUNNER_BYTES)`; the adapter output rows, toolchain roots, runtime identities, installed files and every command path must resolve to those same six objects.
DEPENDENCY_ROWS(config)=[]; DEPENDENCY_ROWS(schema)=[]; DEPENDENCY_ROWS(compiler)=[tools/plan-handoff-schema.fixture|100644|schema-blob]; DEPENDENCY_ROWS(discover)=[]; DEPENDENCY_ROWS(runner)=[]; DEPENDENCY_ROWS(checker)=[tools/plan-handoff-schema.fixture|100644|schema-blob,tools/fixture-compiler.fixture|100755|fixture-compiler-blob,tools/fixture-discover.fixture|100755|fixture-discover-blob,tests/FixtureRunner.fixture|100755|test-runner-blob] in exactly that order.
DEPENDENCY_MANIFEST_BYTES(name)=F("dependency-manifest", exact executable path, mode, blob, runtime, version, each exact ordered `DEPENDENCY_ROWS(name)` path|mode|blob); every `*-dependency-manifest-hash=H(DEPENDENCY_MANIFEST_BYTES(name))` and no unlisted dependency may load.
ADAPTER_OUTPUT_MANIFEST_BYTES=for each ordered `adapter_output_manifest.rows` row exactly `path<TAB>mode<TAB>blob<TAB>runtime<TAB>version<TAB>dependency-manifest-hash<LF>` with one final LF already supplied by the last row; `adapter_output_manifest.blob` is the git blob of those exact bytes and `adapter_output_manifest.hash=H(ADAPTER_OUTPUT_MANIFEST_BYTES)`. The six rows equal `toolchain.roots` and `toolchain.runtime_identity` by path/mode/blob and, for executable rows, runtime/version/dependency hash; the config row is literal `data|1|config-dependency-manifest-hash`.
BOOTSTRAP_CONFORMANCE_RESULT_BYTES=FULL_RESULT_PACKET_BYTES("bootstrap-conformance-fixture","c-bootstrap-conformance","disposable stage-A authority","bootstrap-receipt=<computed:bootstrap-receipt>; live-persisted=no","none","bootstrap conformance fixture only",awaiting_decision)
SETUP_AUTHORIZED_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES("setup-authorized","c-authorize-setup","setup authorized","target=fixture/product; product-writes=none","append this event and exact finalizer c-finalize-setup-authorized","setup authorized",FINALIZER_CALL_BYTES(setup-authorized),"setup-authorized-result.md")
SETUP_INTERVIEW_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES("setup-interview","c-setup-interview","read-only inventory captured","profile-path=os/engineering/profiles/fixture.md; profile-mode=100644; profile-blob=<external:stack-profile-blob>; profile-sha256=<external:stack-profile-sha256>; entry-state=<setup-entry-state>; inventory-count=<setup-inventory-count>; inventory=<setup-interview-inventory-hash>; product-writes=none","append this event and exact finalizer c-finalize-setup-interview","setup interview captured",FINALIZER_CALL_BYTES(setup-interview),"setup-interview-result.md")
ADAPTER_AUTHOR_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES("adapter-author","c-adapter-author","adapter candidate authored","interview=history/setup-interview-result.md@<computed:I-setup-interview>; author=<computed:adapter-author-session>; profile=os/engineering/profiles/fixture.md|100644|<external:stack-profile-blob>|<external:stack-profile-sha256>; adapter=work/validation-adapters/<computed:stack-id>-v21.fixture|100644|<computed:accepted-adapter-blob>; manifest=work/validation-adapters/<computed:stack-id>-v21.manifest|100644|<computed:adapter-output-manifest-blob>|<computed:adapter-output-manifest-hash>; product-writes=none","add exactly adapter+manifest work artifacts; append this event and exact finalizer c-finalize-adapter-authored","adapter authored",FINALIZER_CALL_BYTES(adapter-authored),"adapter-author-result.md")
ADAPTER_REVIEW_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES("adapter-review","c-adapter-review","independently reviewed adapter accepted","interview=history/setup-interview-result.md@<computed:I-setup-interview>; author-event=history/adapter-author-result.md@<computed:I-adapter-author-result>; author=<computed:adapter-author-session>; reviewer=<computed:adapter-review-session>; profile path/mode/blob/sha exact; adapter path/mode/blob exact; manifest path/mode/blob/hash exact; verdict=GREEN; product-writes=none","append this event and exact finalizer c-finalize-adapter-accepted","adapter independently accepted",FINALIZER_CALL_BYTES(adapter-accepted),"adapter-review-result.md")
ADAPTER_REVIEW_RESYNC_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES("adapter-review-resync","c-adapter-review","independently reviewed adapter accepted for re-sync","same exact interview/author/profile/adapter/manifest authority; author=<computed:adapter-author-session>; reviewer=<computed:adapter-review-session>; verdict=GREEN; product-writes=none","append this event and exact finalizer c-finalize-adapter-accepted-resync","adapter independently accepted for resync",FINALIZER_CALL_BYTES(adapter-accepted-resync),"adapter-review-resync-result.md")
RESULT_BYTES="change-id: v21-fixture-change\nbase-authority: sha:<computed:B>\nacceptance-hash: <computed:acceptance-hash>\nrun-id: <computed:run-id>\nlocation: docs/results/v21-fixture-change.md\narchive-source: openspec/changes/v21-fixture-change\narchive-target: openspec/changes/archive/v21-fixture-change\noutcome: exact result\nevidence: fixture evidence\nassumptions: none\ncuts: none\ncost: fixture\nmanual-acceptance: none\nnext: return-to-direction\n"
CONFORMANCE_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES("conformance-install","c-setup-install","final conformance accepted","receipt=<computed:validation-conformance-receipt>; corpus=<external:this-file-git-blob>; profile exact; author event exact; review event exact; adapter+manifest exact","append this event and exact finalizer c-finalize-conformance","conformance accepted",FINALIZER_CALL_BYTES(final-conformance),"conformance-result.md")
CONFORMANCE_RESYNC_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES("conformance-resync","c-resync","final re-sync conformance accepted","receipt=<computed:validation-conformance-receipt>; corpus=<external:this-file-git-blob>; profile exact; author event exact; resync review event exact; adapter+manifest exact","append this event and exact finalizer c-finalize-conformance","re-sync conformance accepted",FINALIZER_CALL_BYTES(final-conformance),"conformance-result.md")
CONFORMANCE_LIGHT_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES("conformance-light","c-setup-install","final conformance accepted for coordinated light","same exact conformance/profile/adapter authority; light-scan required","append this event and exact finalizer c-finalize-conformance-light","light conformance accepted",FINALIZER_CALL_BYTES(final-conformance-light),"conformance-light-result.md")
PLAN_GATED_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES("plan-author","c-plan-author","PLAN-GATED","candidate=<computed:P>; receipt=<computed:plan-receipt>; observation=<computed:plan-observation-hash>; all three actual RED criteria exact; owner-verdict=absent","append this event and exact finalizer c-finalize-plan-verdict","plan candidate gated",FINALIZER_CALL_BYTES(plan-receipt),"plan-gated-result.md")
OWNER_VERDICT_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES_OWNER("plan-verdict","c-plan-verdict","accepted exact candidate <computed:P>","owner-words=ACCEPT exact candidate <computed:P> receipt <computed:plan-receipt>; plan-event=history/plan-gated-result.md@<computed:W-plan-receipt>","append this event and exact finalizer c-finalize-execute","owner accepted exact candidate",FINALIZER_CALL_BYTES(owner-verdict),"owner-verdict-result.md","ACCEPT exact candidate <computed:P> receipt <computed:plan-receipt>")
RESULT_REVISION_BYTES="change-id: v21-fixture-change\nbase-authority: sha:<computed:B>\nacceptance-hash: <computed:acceptance-hash>\nrun-id: <computed:run-id>\nlocation: docs/results/v21-fixture-change.md\narchive-source: openspec/changes/v21-fixture-change\narchive-target: openspec/changes/archive/v21-fixture-change\noutcome: exact revised result\nevidence: latest accepted revision T and progress U\nassumptions: none\ncuts: none\ncost: fixture\nmanual-acceptance: none\nnext: return-to-direction\n"
RED_LEDGER_BYTES="kind: red-accepted\nrun-id: <computed:run-id>\nproduct-commit: <computed:R>\nred-event: first\nmanifest: <computed:oracle-manifest-hash>\n"
Q_LEDGER_BYTES="kind: progress-accepted\nrun-id: <computed:run-id>\nproduct-commit: <computed:Q>\nred-event: history/red-result.md@<computed:E-red-accept>\nmanifest: <computed:oracle-manifest-hash>\n"
RED_CHAIN_LEDGER_BYTES="kind: red-chain-accepted\nrun-id: <computed:run-id>\nproduct-commit: <computed:R2>\nchain: <computed:R1>,<computed:R2>\nmanifest: <computed:oracle-manifest-hash>\n"
CHAIN_PROGRESS_LEDGER_BYTES="kind: chain-progress-accepted\nrun-id: <computed:run-id>\nproduct-commit: <computed:Q2>\nred-event: history/red-chain-result.md@<computed:E-red-chain-accept>\nmanifest: <computed:oracle-manifest-hash>\n"
T_LEDGER_BYTES="kind: revision-accepted\nrun-id: <computed:run-id>\nproduct-commit: <computed:T>\nparent-progress: <computed:Q>\noriginal-event: history/red-result.md@<computed:E-red-accept>\noriginal-manifest: <computed:oracle-manifest-hash>\nvariant-manifest: <computed:oracle-revision-manifest-hash>\n"
U_LEDGER_BYTES="kind: post-revision-progress-accepted\nrun-id: <computed:run-id>\nproduct-commit: <computed:U>\noriginal-event: history/red-result.md@<computed:E-red-accept>\nrevision-event: history/revision-result.md@<computed:E-revision-accept>\noriginal-manifest: <computed:oracle-manifest-hash>\nvariant-manifest: <computed:oracle-revision-manifest-hash>\n"
LIGHT_LEDGER_BYTES="kind: light-progress-accepted\nrun-id: <computed:light-run-id>\nproduct-commit: <computed:LQ>\ng0-scan: <computed:light-scan-observation-hash>\n"
RED_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES("red-accepted","c-execute","independent RED accepted","payload="+RED_LEDGER_BYTES+"; history-blob is not payload-blob","append this event and exact finalizer c-finalize-red-accepted","red accepted",FINALIZER_CALL_BYTES(red-accepted),"red-result.md")
Q_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES("progress-accepted","c-build-red","build progress accepted","payload="+Q_LEDGER_BYTES,"append this event and exact finalizer c-finalize-progress-accepted","progress accepted",FINALIZER_CALL_BYTES(progress-accepted),"progress-result.md")
RED_CHAIN_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES("red-chain-accepted","c-execute","two-commit independent RED accepted","payload="+RED_CHAIN_LEDGER_BYTES,"append this event and exact finalizer c-finalize-red-chain-accepted","red chain accepted",FINALIZER_CALL_BYTES(red-chain-accepted),"red-chain-result.md")
CHAIN_PROGRESS_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES("chain-progress-accepted","c-build-chain","chain build progress accepted","payload="+CHAIN_PROGRESS_LEDGER_BYTES,"append this event and exact finalizer c-finalize-chain-progress-accepted","chain progress accepted",FINALIZER_CALL_BYTES(chain-progress-accepted),"chain-progress-result.md")
T_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES("revision-accepted","c-build-progress","independent revision accepted","payload="+T_LEDGER_BYTES+"; original and variant manifests both pinned","append this event and exact finalizer c-finalize-revision-accepted","revision accepted",FINALIZER_CALL_BYTES(revision-accepted),"revision-result.md")
U_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES("post-revision-progress","c-build-revision","post-revision progress accepted","payload="+U_LEDGER_BYTES,"append this event and exact finalizer c-finalize-post-revision-progress","post revision progress accepted",FINALIZER_CALL_BYTES(post-revision-progress),"post-revision-result.md")
LIGHT_PROGRESS_RESULT_BYTES=FULL_RESULT_HISTORY_BYTES("light-progress","c-execute-light","coordinated-light progress accepted","payload="+LIGHT_LEDGER_BYTES,"append this event and exact finalizer c-finalize-light-progress","light progress accepted",FINALIZER_CALL_BYTES(light-progress),"light-progress-result.md")
CLOSE_RESULT_HISTORY_BYTES=FULL_RESULT_HISTORY_BYTES("build-main","c-build-progress","full BUILD contour closed","deliver=D|docs/results/v21-fixture-change.md|<computed:result-blob>; close=A|parent=D|archive exact; acceptance=3/3 PASS; immutable-call=<computed:resume-progress-finalization-receipt>","record product evidence only; no invented product or Direction outcome","build contour closed",awaiting_decision,"close-result.md")
CLOSE_REVISION_RESULT_HISTORY_BYTES=FULL_RESULT_HISTORY_BYTES("build-revision","c-build-post-revision","full revision BUILD contour closed","deliver=D2|docs/results/v21-fixture-change.md|<computed:result-revision-blob>; close=A2|parent=D2|archive exact; acceptance=6/6 PASS; original+variant manifests retained; immutable-call=<computed:resume-post-revision-finalization-receipt>","record product evidence only; no invented product or Direction outcome","revision build contour closed",awaiting_decision,"close-revision-result.md")
CLOSE_CHAIN_RESULT_HISTORY_BYTES=FULL_RESULT_HISTORY_BYTES("build-chain","c-build-chain-progress","full chained-RED BUILD contour closed","deliver=D3|docs/results/v21-fixture-change.md|<computed:result-chain-blob>; close=A3|parent=D3|archive exact; acceptance=3/3 PASS; R1/R2 per-commit evidence retained; immutable-call=<computed:resume-progress-chain-finalization-receipt>","record product evidence only; no invented product or Direction outcome","chain build contour closed",awaiting_decision,"close-chain-result.md")
CLOSE_LIGHT_RESULT_HISTORY_BYTES=FULL_RESULT_HISTORY_BYTES("build-light","c-build-light","full coordinated-light BUILD contour closed","deliver=LD|docs/results/v21-light.md|<computed:light-result-blob>; close=LD|parent=n/a|archive=n/a-light; light scan exact; immutable-call=<computed:resume-light-finalization-receipt>","record product evidence only; no invented product or Direction outcome","light build contour closed",awaiting_decision,"close-light-result.md")
LIGHT_RESULT_BYTES="change-id: v21-light\nbase-authority: sha:<computed:B>\nacceptance-hash: <computed:light-acceptance-hash>\nrun-id: <computed:light-run-id>\nlocation: docs/results/v21-light.md\narchive-source: n/a-light\narchive-target: n/a-light\noutcome: exact light result\nevidence: no frozen spec path\nassumptions: none\ncuts: none\ncost: fixture\nmanual-acceptance: none\nnext: return-to-direction\n"
ORACLE_BYTES="FixtureTests.OB_1|DW-1 missing member|RED\nFixtureTests.OB_2|DW-2 loopback count|RED\nFixtureTests.OB_3|DW-3 golden mismatch|RED\n"
OB1_VARIANT_BYTES=REPLACE_EXACT(REPLACE_EXACT(testability.recipes[0].red_realization.source_bytes,"test FixtureTests.OB_1\n","test FixtureTests.OB_1_V2\n"),"assert DW-1 absent Create exact result\n","let variantHandler:Fixture.Tests.OwnedHandler=new Fixture.Tests.OwnedHandler(core)\nlet variantStep:Fixture.StepResult=core.Step(impulse,variantHandler as Fixture.ReactionHandler)\nassert variantHandler.CallCount()==1 and comparator.ReferenceEqual(variantHandler.Owner(),core) and comparator.Compare(Fixture.Audit.For(core).Read(),golden) // criterion DW-1 exact result variant mismatch\nassert DW-1 absent Create exact result\n")
OB2_VARIANT_BYTES=REPLACE_EXACT(REPLACE_EXACT(testability.recipes[1].red_realization.source_bytes,"test FixtureTests.OB_2\n","test FixtureTests.OB_2_V2\n"),"assert DW-2 existing Step loopback once\n","let nested:Fixture.StepResult=core.Step(impulse,loopback as Fixture.ReactionHandler)\nassert loopback.DelegationCount()==2 and loopback.CallCount()==3 // criterion DW-2 nested loopback count\nassert DW-2 existing Step loopback once\n")
OB3_VARIANT_BYTES=REPLACE_EXACT(REPLACE_EXACT(testability.recipes[2].red_realization.source_bytes,"test FixtureTests.OB_3\n","test FixtureTests.OB_3_V2\n"),"assert DW-3 source-isolated golden audit\n","let core2N:Fixture.Core=Fixture.Core.Existing(topology)\nlet input2N:Fixture.SourceInput=Fixture.SourceInput.Single(Fixture.FaceId(0),<computed:k2>,<computed:n>)\nlet step2N:Fixture.StepResult=core2N.StepSource(input2N)\nlet audit2N:Fixture.AuditResult=Fixture.Audit.Read(core2N)\nassert comparator.Compare(audit2N,golden2) and comparator.AuditEqual(audit2N,audit2) // criterion DW-3 hidden audit mismatch\nassert DW-3 source-isolated golden audit\n")
VARIANT_TEST_BYTES=OB1_VARIANT_BYTES + OB2_VARIANT_BYTES + OB3_VARIANT_BYTES. Each `REPLACE_EXACT` old string occurs exactly once or materialization fails; no operation reads or writes `tests/FixtureTests.fixture`, so its three original source byte strings remain byte-identical.
VARIANT_ORACLE_BYTES="FixtureTests.OB_1_V2|DW-1 exact result variant mismatch|RED\nFixtureTests.OB_2_V2|DW-2 nested loopback count|RED\nFixtureTests.OB_3_V2|DW-3 hidden audit mismatch|RED\n"
ORACLE_REVISION_BYTES=ORACLE_BYTES + VARIANT_ORACLE_BYTES
S0: AGENTS.md="owner preface\n"; notes/owner.txt="owner data\n"
S-absent: target directory does not exist. S-empty: target directory exists with zero entries. SB-absent/SB-empty: create every row in `setup_variants.absent.manifest`, then initialize one clean root commit; no protected entries exist.
SB-S0: CREATE validation.config and all five pinned tool files (checker, schema, compiler, discoverer, runner); OVERLAY AGENTS.md="owner preface\n\nv21 run contract\n"; notes/owner.txt unchanged; initialize and commit clean installed SB only after exact postimage verification
RB: validation.config=CONFIG_V20; AGENTS.md="owner preface\nv20 run contract\n"; src/Existing.fixture="existing product\n"; branch=codex/v21-resync; clean initialized commit
RS-RB: OVERLAY validation.config=CONFIG_V21; OVERLAY AGENTS.md="owner preface\nv21 run contract\n"; CREATE all five pinned tool files; src/Existing.fixture unchanged; no feature/source/test/acceptance delta
B: validation.config=CONFIG_V21 plus the five exact executable/tool roots from `toolchain.roots`; src/PublicApi.fixture="Fixture.Topology.TwoRoom/SingleCell; Fixture.Impulse.AtFace; Fixture.SourceInput.Single; Fixture.Core.Existing/Step/StepSource/Value; internal Fixture.Audit.For/Read and operation-local FixtureFault.Select friend Fixture.Tests; Fixture.Core.Create(System.Int32,Fixture.Topology) absent\n"; tests/Fixture.Tests.project="references src/PublicApi.fixture; friend tests/FixtureFriendAssembly.fixture; runner tests/FixtureRunner.fixture\n"; tests/FixtureFriendAssembly.fixture="friend Fixture.Tests\n"; tests/FixtureRunner.fixture equals the pinned runner blob from `toolchain.runtime_identity.runner`; AGENTS.md="v21 run contract\n"
P-B: ADD proposal.md="proposal v21\n"; PLAN.md="plan v21\n"; tasks.md="tasks v21\n"; specs/core/spec.md="OB-1 absent Create exact result\nOB-2 existing Step loopback once\nOB-3 source-isolated golden audit\n" under openspec/changes/v21-fixture-change/; ADD docs/adr/ADR-v21-fixture.md="ADR-v21-fixture\n"; ADD TESTABILITY.md as exact canonical rendering of `testability`; no source/test/toolchain/result change
R-P: ADD tests/FixtureTests.fixture as the concatenation of the three exact `red_realization.source_bytes` in recipe order; ADD docs/validation/oracle-v21-fixture.json=ORACLE_BYTES; actual compiler exits 0, discovery returns exactly all three ids, filtered runtime returns each named RED criterion
R1-P: ADD only tests/FixtureTests.fixture with the same exact bytes; R2-R1: ADD only docs/validation/oracle-v21-fixture.json with the same exact bytes. Both commits are the same declared independent test-author session and R2 is the valid two-commit-chain checkpoint.
Q-R: REPLACE src/PublicApi.fixture="type Fixture.Core; Create(System.Int32,Fixture.Topology), Step and Value implemented\n"; ADD PROGRESS.md="accepted build progress\n"
T-Q: independent test-author only ADD tests/FixtureTestsV2.fixture=VARIANT_TEST_BYTES and docs/validation/oracle-v21-fixture-v2.json=VARIANT_ORACLE_BYTES; `tests/FixtureTests.fixture` and `docs/validation/oracle-v21-fixture.json` remain byte-identical to R. Discovery is exactly six ids; the original three PASS at Q and the three V2 ids return their exact variant RED criteria. Both original and variant manifests/events remain pinned; no source/frozen/toolchain/result/unmanifested delta.
D-Q: ADD docs/results/v21-fixture-change.md=RESULT_BYTES after actual acceptance suite returns PASS; no self hash/commit
U-T: REPLACE src/PublicApi.fixture="type Fixture.Core; revised implementation makes all original and V2 tests PASS\n"; ADD PROGRESS-REVISION.md="accepted post-revision progress\n"
D2-U: ADD docs/results/v21-fixture-change.md=RESULT_REVISION_BYTES after all six original-plus-V2 tests return PASS
A2-D2: MOVE the exact packet tree to archive preserving suffix/mode/blob; no other delta
A-D: MOVE openspec/changes/v21-fixture-change/** to openspec/changes/archive/v21-fixture-change/** preserving suffix/mode/blob; no other delta
Q2-R2: same production postimage and accepted progress meaning as Q, but parent is exactly R2. D3-Q2: ADD docs/results/v21-fixture-change.md=RESULT_BYTES after the original three tests PASS. A3-D3: MOVE the exact packet tree to archive preserving suffix/mode/blob; no other delta.
LQ-B: on branch codex/v21-light ADD src/Light.fixture="light change\n" and no openspec change path; LD-LQ: ADD docs/results/v21-light.md=LIGHT_RESULT_BYTES. Light close retains HEAD=LD, records source/target=`n/a-light` and parent absent/count zero; no fake empty archive commit exists. Before LQ work, execute_light is finalized; after LQ is accepted, E-light-progress-accept and E-build-light-call are two separate Direction commits and `resume_light` carries its own fresh finalization evidence.
```

Main feature contour is B -> P -> R -> Q -> D -> A. The alternate valid chained-RED contour is the complete P -> R1 -> R2 -> Q2 -> D3 -> A3 path, including its own Direction red/progress acceptance events. The later-revision contour is Q -> T -> U -> D2 -> A2; T adds separately named variants and never edits or discards the original R files/events/manifests. RE-SYNC is RB -> RS; SETUP begins at absent/empty/nonempty non-git variants and ends at a clean initial commit. Direction event-dependent children follow the separate event/finalizer graph and are rendered only after cited commit ids exist.

The canonical non-install snapshots are stage-A receipt fixtures. Only `bootstrap:noninstall-opaque-receipt` and `bootstrap:plan-clean-stage-A-entry` use them directly; the final-binding smoke explicitly transforms them. Every real downstream valid case and its ordinary mutation first applies `FINAL_VIEW` with persisted `C-final-conformance`; hashes/receipts are recomputed before the stated operation. Thus no real PLAN/EXECUTE/BUILD CALL cites `C-bootstrap-conformance`; deliver and close are not CALL phases.

## Exact valid cases

```text
setup:read-only-interview	snapshot=setup_interview; product_writes=[]; event I-setup-interview precedes adapter author/review	0
adapter:separate-author-review-writer-event	I-setup-interview<I-adapter-author-call<I-adapter-author-result<I-adapter-review-call<I-adapter-accept<I-install-call; author/reviewer/installer sessions distinct; reviewed path/mode/blob/output manifest exact; no product writes	0
adapter:separate-resync-review-return	snapshot=adapter_review_resync_call; same immutable reviewed adapter CALL may return only ADAPTER_REVIEW_RESYNC_RESULT_BYTES on the I-resync-adapter-accept branch; author/reviewer/installer distinct; no product writes	0
writer:all-intent-finalizations	EACH_WRITER_FINALIZATION; exact intent preimage, writer-only additions and observation; no session-owned writer field	0
setup:absent-root	snapshot=setup_absent; interview payload entry=absent inventory=empty; entry=S-absent; expected=SB-absent	0
setup:empty-root	snapshot=setup_empty; interview payload entry=empty inventory=empty; entry=S-empty; expected=SB-empty	0
setup:nonempty-create-overlay-protected	snapshot=setup; interview payload entry=nonempty inventory=<computed:interview-inventory-hash>; entry=S0; expected=SB	0
resync:exact-contract-only	snapshot=resync; interview payload entry=initialized count=3 inventory=<computed:resync-interview-inventory-hash>; entry=RB; expected=RS	0
bootstrap:install-challenge	EACH_INSTALL; challenge present; conformance authority absent	0
bootstrap:noninstall-opaque-receipt	EACH_NONINSTALL; packet receipt equals independent authority; challenge absent	0
bootstrap:final-receipt-binding-smoke	EACH_NONINSTALL FINAL_VIEW(<snapshot>,<computed:validation-conformance-receipt>,history/<computed:conformance-result-path>@<computed:C-final-conformance>,<computed:validation-conformance-receipt>); excluded from conformance preimage	0
direction:event-dependent-finalization	EACH_FINALIZER; event commit contains only finalizer CALL; fresh RESULT child is strict descendant and changes exact allowed paths	0
direction:conformance-event-before-plan	C-final-conformance < C-plan-call; real plan packet carries event@C and final receipt	0
direction:setup-conformance-result-identity	EACH_SETUP_CREATE; internal install gate has result-presence=n/a; subsequent C-final-conformance history equals CONFORMANCE_RESULT_BYTES with call c-setup-install and finalizer c-finalize-conformance	0
direction:resync-conformance-result-identity	snapshot=resync; internal install gate has result-presence=n/a; subsequent C-final-conformance history equals CONFORMANCE_RESYNC_RESULT_BYTES with call c-resync and finalizer c-finalize-conformance	0
bootstrap:plan-clean-stage-A-entry	snapshot=plan_entry; disposable bootstrap authority only	0
plan:gated-author-checkpoint-no-verdict	snapshot=plan_gated; all three obligations actually compile, uniquely discover and run their exact RED criteria	0
plan:writer-event-finalizer-verdict	W-plan-receipt < W-verdict-call; snapshot=verdict_finalize_pending then verdict_call	0
plan:owner-verdict-finalizer-execute	W-verdict-call < W-verdict-result < W-execute-call; snapshot=plan_after_owner then execute	0
identity:stable-ref-full-contour	EACH_REAL_ID replace identity with identity_stable_ref; origin/main remains B through check	0
authority:phase-matrix	EACH_PHASE_SNAPSHOT; packet phase/stage/substage equals snapshot and every cited event equals independent authority path/mode/blob/payload/strict ancestor; deliver/close retain BUILD phase and identical CALL bytes	0
light:full-contour	snapshots=execute_light,resume_light,deliver_light,close_light; zero G0 paths; E-light-progress-accept<E-build-light-call; all identity/run/result/finalization fields retained	0
testability:three-obligation-union	coverage ordinals 0,1,2 map one-to-one OB-1,OB-2,OB-3; every binding DAG node resolves; three expanded sources compile, discover once and return exact filtered RED; union compile/discovery is exact	0
execute:fresh-packet-only	snapshot=execute; head=P; fresh finalization receipt at W-execute-call	0
red:exact-parent-direct	snapshot=red_boundary; head=R; actual compile=0 discovery=3 runtime exact RED	0
red:declared-two-commit-chain	snapshot=red_chain; P<R1<R2; per-commit deltas are exactly test then oracle; E-red-chain-accept<E-build-chain-call	0
resume:accepted-red	snapshot=resume_red; E-red-accept<E-build-red-call; distinct resume finalization	0
resume:accepted-progress	snapshot=resume_progress; E-progress-accept<E-build-progress-call; distinct Q receipt	0
resume:accepted-two-commit-chain	snapshots=resume_red_chain,resume_progress_chain; E-red-chain-accept<E-build-chain-call<E-chain-progress-accept<E-build-chain-progress-call; R2<Q2	0
red:revision-exact-accepted-parent	snapshot=red_revision; Q<T; original files byte-identical; three original PASS plus three V2 exact RED	0
resume:accepted-red-revision	snapshot=resume_revision; E-revision-accept<E-build-revision-call; distinct T receipt	0
resume:accepted-post-revision-progress	snapshot=resume_post_revision; T<U; distinct U receipt	0
deliver:result-at-D	snapshot=deliver; latest protected tests actually PASS; deliver_evidence.observed_head=D while immutable BUILD CALL entry head remains Q	0
close:archive-at-A	snapshot=close; A has exactly one parent D	0
deliver:revision-result-at-D2	snapshot=deliver_revision; all six original-plus-V2 tests PASS; original and variant manifests retained; deliver evidence head=D2 and CALL entry head=U	0
close:revision-archive-at-A2	snapshot=close_revision; A2 has exactly one parent D2	0
deliver:chain-result-at-D3	snapshot=deliver_chain; Q2<D3; original three tests PASS and CALL entry remains Q2	0
close:chain-archive-at-A3	snapshot=close_chain; A3 has exactly one parent D3	0
recover:lost-routing-at-deliver	EACH_RECOVERY_DELIVER snapshot=<snapshot>; rerun returns exact <routing-bytes> and <routing-hash>	0
recover:lost-routing-at-close	EACH_RECOVERY_CLOSE snapshot=<snapshot>; derive <deliver-node>=archive^ and return exact <routing-bytes> and <routing-hash>	0
baseline:current-copy-changed	snapshot=resume_progress; every baseline row resolves at B while current source differs	0
```

## Mutation DSL and exhaustive invalid cases

Typed object operations are exact: `J(snapshot,pointer,old,new)`, `JD(snapshot,pointer,old)`, `JA(snapshot,pointer,absent,new)` mutate an expanded packet/handback; `JA_INTENT` mutates the pre-finalization intent rather than the packet; `C[@mode](pointer,old,new)`, `CD[@mode](pointer,old)`, `CA[@mode](pointer,absent,new)` mutate canonical input before rendering; `CDV(array-pointer,exact-value)` deletes the one exactly equal array value and fails materialization on zero/multiple matches; `/binding_registry[id=<exact-id>]` is a unique-id selector and likewise fails on zero/multiple matches; `AR(snapshot,row,old,new)`, `ARD(snapshot,row,old)`, `ARA(snapshot,row,absent,new)` mutate only the independently rendered authority row. `C_ROUTE(pointer,old-route,old-source,new-route,new-source)` is one atomic semantic route mutation whose source/blob fields are mechanically coupled; `C_SWAP_BODY` swaps only the exact two declared function bodies while preserving source ids, type names and signatures. Both packet families recompute every mechanically dependent intent/packet/blob/manifest/finalization/observation receipt and clean head while preserving the intentionally wrong semantic value and expected outcome. Authority operations recompute only authority bytes/blob and ABI pins. `RAWJ` alone changes a receipt/hash without recomputation and is used only by named tamper cases. Thus authority/meaning cases cannot pass merely by noticing stale receipts.

File/history operations are exact: `TA(tree,path,mode,bytes,parent-or-none)` adds; `TD(tree,path,old-bytes)` deletes a 100644 row; `TR(tree,path,old-bytes,new-bytes)` replaces bytes; `TM(tree,path,old-mode,new-mode,new-payload)` changes index mode using exact new blob, link-target bytes for 120000, or disposable commit for 160000; `RENAME(tree,old,new)` verifies and preserves mode/blob; `TEXT_DELETE_EXACT(tree,path,exact-LF-record)`; `TDIR(tree,prefix)` removes exact sorted rows. `parent=none` is dirty; otherwise the child uses the same constant product specimen metadata as canonical nodes. `ALT(parent,new-node,operation)` creates a clean alternative directly from the same semantic parent and recomputes head/receipts; `CLEAN_SETUP_ALT(entry,new-node,operation-on-canonical-post)` materializes a fresh clean initialized setup alternative, applies that operation and recomputes all receipts; `CLEAN_SETUP_HISTORY` does the same across two clean commits and exposes per-commit preservation; `MERGE_ALT(first-parent,second-parent,new-node,tree)` creates the stated two-parent commit. `HC(parent,h1|h2,operation)` creates exact history descendants; `RESTORE` requires h1 and old mode/blob. `DIR(instance,exact-state-mutation)` applies one coherent mutation to all affected event/child Direction trees, histories, authorities and hashes, then recomputes the alternative commits. `FINAL_VIEW(snapshot,receipt,event,authority-receipt)` is the excluded post-bootstrap view: it replaces the stage-A packet receipt/event and independent authority row, then recomputes dependent packet/authority/finalization bytes; no other field changes. `ACTUAL(snapshot,compile|discover|run|history,exact-output)` changes the real expanded source, captured tool output or traversed per-commit history while leaving self-reported semantic claims as specified. `ADAPTER_RENDER(snapshot,full-markdown|json-fragment|missing-result|extra-wrapper-field)` changes the independently rendered ABI bytes and recomputes its file blob only. `UNACCEPTED_PROGRESS(parent,new-node,source-bytes)` creates one clean same-run product commit and a packet/ledger claim recomputed for it while deliberately leaving the independent authority file without a matching Direction event. `ROUTE_OUTPUT(snapshot,old-bytes,new-bytes)` changes only actual recovery stdout and recomputes its observation hash. `REF_DRIFT`, `REF_MISSING`, `REF_WRONG_OBSERVED`, `REPARSE`, `LOAD`, `RUN_BEFORE_PIN`, `SIDE_EFFECT`, `ENV_ADD/ENV_DELETE/ENV_REPLACE` have explicit old/new values. Every preimage must match or materialization fails.

Expansion sets are closed and ordinal. `EACH_INSTALL[setup_absent,setup_empty,setup,resync]`. `EACH_SETUP_CREATE[setup_absent|S-absent|SB-absent|absent|0|empty-inventory-hash,setup_empty|S-empty|SB-empty|empty|0|empty-inventory-hash]`. `EACH_PHASE_SNAPSHOT[setup_interview,adapter_author_call,adapter_review_call,adapter_review_resync_call,setup_absent,setup_empty,setup,resync,plan_entry,plan_gated,verdict_call,execute,red_boundary,red_chain,resume_red,resume_progress,resume_red_chain,resume_progress_chain,red_revision,resume_revision,resume_post_revision,deliver,close,deliver_revision,close_revision,deliver_chain,close_chain,execute_light,resume_light,deliver_light,close_light]`. `EACH_INSTALLED_MODE[setup_absent,setup_empty,setup,resync,plan_entry,plan_gated,verdict_call,execute,red_boundary,red_chain,resume_red,resume_progress,resume_red_chain,resume_progress_chain,red_revision,resume_revision,resume_post_revision,deliver,close,deliver_revision,close_revision,deliver_chain,close_chain,execute_light,resume_light,deliver_light,close_light]`; it intentionally excludes interview/adapter-author/both adapter-review returns because no product trust roots exist there. `EACH_NONINSTALL` is `EACH_INSTALLED_MODE` minus the four install snapshots. `EACH_REF_SNAPSHOT[resync,plan_entry,plan_gated,verdict_call,execute,red_boundary,red_chain,resume_red,resume_progress,resume_red_chain,resume_progress_chain,red_revision,resume_revision,resume_post_revision,deliver,close,deliver_revision,close_revision,deliver_chain,close_chain,execute_light,resume_light,deliver_light,close_light]`. `EACH_REQUIRED_PACKET_LEAF` expands every present leaf of the fully rendered full Markdown CALL, wrapper and handback; `EACH_IDENTITY_LEAF` expands every present repo/worktree/branch/base-authority/base/acceptance-source/acceptance-hash/change-id/product-result-path/toolchain/TESTABILITY/run/RED/progress/event leaf and supplies both a deletion and a coherent wrong value from another canonical contour; `EACH_AUTHORITY_ROW` expands all eight fixed rows. `EACH_SUBSTAGE` covers all SETUP stages, PLAN author/verdict, EXECUTE fresh and every BUILD resume snapshot including chain/revision/light. `EACH_OBLIGATION[0,1,2]`; `EACH_COVERAGE[0,1,2]`; `EACH_MANIFEST_KIND[packet,authority,baseline]`; `EACH_PACKET_MEMBER[proposal,PLAN,tasks,spec,TESTABILITY]`; `EACH_AUTHORITY_MEMBER[ADR]`; `EACH_TESTABILITY_OBJECT[path,mode,blob,reparse,type]`; `EACH_RESULT_IDENTITY[change-id,base-authority,acceptance-hash,run-id,location,archive-source,archive-target,next]`; `EACH_RESULT_REQUIRED[outcome,evidence,assumptions,cuts,cost,manual-acceptance]`; `EACH_RESULT_FIELD` is their ordered union. `EACH_RED_MEMBER[tests/FixtureTests.fixture,docs/validation/oracle-v21-fixture.json]`; `EACH_VARIANT_MEMBER[tests/FixtureTestsV2.fixture,docs/validation/oracle-v21-fixture-v2.json]`. In close snapshots packet paths resolve to their archive suffix; before close they resolve to active paths. Prefix routing remains setup/adapter/bootstrap->install, plan/recipe/manifest/red-realization->plan, red->red-boundary/resume, result->deliver, archive/close->close; otherwise `@mode` is mandatory.

`EACH_ADAPTER_REVIEW_RETURN[adapter_review_call,adapter_review_resync_call]`. `EACH_CALL_ENVELOPE_FIELD[id,to,direction,play,node,task,goal,context,boundaries,done_when,return,budget,repo,kind,packet-stage,phase]` expands only fields present in that snapshot and includes stage/mode separately through `EACH_SUBSTAGE`. `EACH_STABLE_CALL_LEAF` is every expanded intent leaf except `packet-stage`; `EACH_ENTRY_SNAPSHOT`, `EACH_GATE_SNAPSHOT` and `EACH_RETURN_SNAPSHOT` are exactly the three same-named `abi_contract` arrays, and `EACH_NO_RESULT_SNAPSHOT` is entry followed by gate. `EACH_REQUIRED_AUTHORITY_SLOT` derives every snapshot/slot pair listed in `authority_required`; `EACH_NA_AUTHORITY_SLOT` derives its ordered complement against `authority_slot_order`. `EACH_RESULT_ENVELOPE_FIELD[session-id,call-id,direction,play,node-task,outcome,evidence,state_changes,captures,decisions_needed,play-check-1,play-check-2,play-check-3,play-check-4,play-check-5,log,next,history-trailer]`.

`EACH_FINALIZER[setup-authorized,setup-interview,adapter-authored,adapter-accepted,adapter-accepted-resync,conformance,conformance-light,plan-receipt,owner-verdict,red-accepted,progress-accepted,red-chain-accepted,chain-progress-accepted,revision-accepted,post-revision-progress,light-progress]` expands exact `direction_transactions.instances` order. `EACH_CONFORMANCE_GATE[setup_absent|I-install-call|C-final-conformance|CONFORMANCE_RESULT_BYTES|CONFORMANCE_RESYNC_RESULT_BYTES,setup_empty|I-install-call|C-final-conformance|CONFORMANCE_RESULT_BYTES|CONFORMANCE_RESYNC_RESULT_BYTES,setup|I-install-call|C-final-conformance|CONFORMANCE_RESULT_BYTES|CONFORMANCE_RESYNC_RESULT_BYTES,resync|I-resync-call|C-final-conformance|CONFORMANCE_RESYNC_RESULT_BYTES|CONFORMANCE_RESULT_BYTES]`. `EACH_WRITER_FINALIZATION[setup_interview|setup_interview,adapter_author|adapter_author_call,adapter_review|adapter_review_call,setup_install_absent|setup_absent,setup_install_empty|setup_empty,setup_install_nonempty|setup,resync|resync,plan_author_bootstrap|plan_entry,plan_author|plan_gated,plan_verdict|verdict_call,execute|execute,execute_light|execute_light,build_resume_red|resume_red,build_resume_progress|resume_progress,build_resume_chain|resume_red_chain,build_resume_chain_progress|resume_progress_chain,build_resume_revision|resume_revision,build_resume_post_revision|resume_post_revision,build_resume_light|resume_light]`. `EACH_REAL_ID[plan_gated,verdict_call,execute,red_boundary,red_chain,resume_red,resume_progress,resume_red_chain,resume_progress_chain,red_revision,resume_revision,resume_post_revision,deliver,close,deliver_revision,close_revision,deliver_chain,close_chain]`. `EACH_DESCENDANT[execute,red_boundary,red_chain,resume_red,resume_progress,resume_red_chain,resume_progress_chain,red_revision,resume_revision,resume_post_revision,deliver,close,deliver_revision,close_revision,deliver_chain,close_chain]`. `EACH_RESUME[resume_red,resume_progress,resume_red_chain,resume_progress_chain,resume_revision,resume_post_revision,resume_light]`. `EACH_RECORD[construct,act,observe,negative,source,skeleton,red_realization]`. `EACH_NEGATIVE_SHAPE[throw-before|fixture:throw-before-source|fixture:throw-before|fixture:throw-before-expected|fixture:throw-before-observed,throw-during|fixture:throw-during-source|fixture:throw-during|fixture:throw-during-expected|fixture:throw-during-observed,throw-after|fixture:throw-after-source|fixture:throw-after|fixture:throw-after-expected|fixture:throw-after-observed]`. `EACH_DELIVER_BRANCH[deliver|<computed:D>|docs/results/v21-fixture-change.md|<computed:result-blob>,deliver_revision|<computed:D2>|docs/results/v21-fixture-change.md|<computed:result-revision-blob>,deliver_chain|<computed:D3>|docs/results/v21-fixture-change.md|<computed:result-chain-blob>,deliver_light|<computed:LD>|docs/results/v21-light.md|<computed:light-result-blob>]`. `EACH_CLOSE_BRANCH[close|<computed:D>|<computed:A>|<computed:D>|docs/results/v21-fixture-change.md|<computed:result-blob>|openspec/changes/v21-fixture-change|openspec/changes/archive/v21-fixture-change|1,close_revision|<computed:D2>|<computed:A2>|<computed:D2>|docs/results/v21-fixture-change.md|<computed:result-revision-blob>|openspec/changes/v21-fixture-change|openspec/changes/archive/v21-fixture-change|1,close_chain|<computed:D3>|<computed:A3>|<computed:D3>|docs/results/v21-fixture-change.md|<computed:result-chain-blob>|openspec/changes/v21-fixture-change|openspec/changes/archive/v21-fixture-change|1,close_light|<computed:LD>|<computed:LD>|<absent>|docs/results/v21-light.md|<computed:light-result-blob>|n/a-light|n/a-light|0]`. `EACH_RESULT_BRANCH[Q|D|RESULT_BYTES|docs/results/v21-fixture-change.md,U|D2|RESULT_REVISION_BYTES|docs/results/v21-fixture-change.md,Q2|D3|RESULT_BYTES|docs/results/v21-fixture-change.md,LQ|LD|LIGHT_RESULT_BYTES|docs/results/v21-light.md]`. `EACH_ARCHIVE_BRANCH[close|D|A|Q|RESULT_BYTES|ORACLE_BYTES|docs/results/v21-fixture-change.md,close_revision|D2|A2|U|RESULT_REVISION_BYTES|ORACLE_REVISION_BYTES|docs/results/v21-fixture-change.md,close_chain|D3|A3|Q2|RESULT_BYTES|ORACLE_BYTES|docs/results/v21-fixture-change.md]`; light has its own no-archive mutations. `EACH_RECOVERY_DELIVER[deliver|D|docs/results/v21-fixture-change.md|result-blob|routing-output-hash,deliver_revision|D2|docs/results/v21-fixture-change.md|result-revision-blob|routing-revision-output-hash,deliver_chain|D3|docs/results/v21-fixture-change.md|result-chain-blob|routing-chain-output-hash,deliver_light|LD|docs/results/v21-light.md|light-result-blob|routing-light-output-hash]`; `EACH_RECOVERY_CLOSE` has the same tuples with close snapshot names. Every expansion appends its canonical item/ordinal suffix before uniqueness checks. Result/archive rows substitute the exact tuple, never a hard-coded main-branch path.

`EACH_CONFORMANCE_GATE` binds, in tuple order, `<snapshot>|<conformance-parent>|<conformance-event>|<exact-conformance-result-bytes>|<wrong-conformance-result-bytes>`; the exact bytes are selected from `abi_contract.conformance_gate_result_ref`, and the wrong bytes are the other call identity's complete RESULT history.

Macro values are total. `EACH_MODE` is an exact alias of `EACH_PHASE_SNAPSHOT`; trust-root mutations must use `EACH_INSTALLED_MODE`. `<snapshot>`, `<snapshot-tree>` and `<exact-phase>` come from the expanded snapshot and full finalized CALL; `<snapshot-head>` means the writer-owned CALL entry `head`, never current handback D/A. `<different-phase>` is the next value in `SETUP|RE-SYNC|PLAN|EXECUTE|BUILD` with wraparound. `<exact-transaction-stage>` is `entry|gate|return` by ABI membership and `<different-transaction-stage>` is the next value with wraparound; `<exact-gate-mode>` is the snapshot value and `<different-gate-mode>` is the next distinct printed gate mode. `EACH_REQUIRED_PACKET_LEAF`, `EACH_IDENTITY_LEAF`, `EACH_AUTHORITY_ROW`, `EACH_SUBSTAGE` and `EACH_SETUP_CREATE` supply the exact values declared above; a coherent wrong identity value is taken from the next canonical snapshot that has the same typed leaf, with all dependent hashes recomputed. `EACH_WRITER_FINALIZATION` additionally binds `<finalization>`, its exact intent ref, the next different intent ref, the complete expanded finalized CALL and every stable leaf. Event variables come from one exact `direction_transactions.instances` row; array variables use the current exact array and `<end>` is its actual length. Resume variables come from writer authority, matching finalization evidence and immediate product predecessor. Coverage/obligation variables bind the exact printed object. Manifest reorder selects the first adjacent pair within the explicitly selected kind and is undefined when that kind has fewer than two rows, so such an expansion is skipped rather than defaulted. Result/archive variables come from their exact branch tuple. `<exact-testability-bytes>` is canonical `testability`; `<exact-ob1-source>` is recipe 0 source; `<direct-call-ob1-source>` replaces its one reflection-construction line with the exact direct-call line and must match once. `<two-exact-args>` is the args array of registry id `fixture:two-room-open-sealed-faces`; `<one-exact-arg>` is its first object. `<two-exact-paths>` and `<three-exact-criteria>` are already JSON arrays and are never wrapped again. `<exact-R-bytes>` is the three original sources in recipe order; `<exact-R2-tree>`, `<Q-source>`, `<same-run-unaccepted-source>`, `<exact-oracle-bytes>`, `<exact-spec-bytes>` and `<exact-A-tree>` are the exact named graph bytes. `EACH_FILE_BINDING` derives every registry node whose kind is `test-local-source|runtime-resource`, in registry order, and binds node/path/mode/blob; `EACH_RUNTIME_RESOURCE` derives every per-recipe and union runtime resource row and binds its list pointer, object pointer, exact object, blob and a different valid resource object from the same scope. `EACH_NEGATIVE_SHAPE` binds its exact source/instance/Expected/Observed ids; `<exact-negative-source-bytes>` is that source node's exact bytes, `<wrong-expected-marker-source-bytes>` is the one-occurrence replacement of its `ExpectedPhase` returned enum with the next phase, and `<wrong-observed-marker-source-bytes>` is the one-occurrence replacement of its `observed=` assignment with the next phase. Required/N/A authority macros bind the exact full authority row or a well-formed foreign row with the same slot schema. No numeric registry index is a macro preimage. No unbound angle variable may reach materialization.

The remaining mutation placeholders are a closed projection, not free text. Envelope/stable/identity/leaf/result placeholders bind the selected fully expanded CALL, ABI wrapper or `return_result_ref`; setup entry/post/tree values bind `EACH_SETUP_CREATE`; coverage/recipe/record/binding/manifest/resource placeholders bind the selected printed JSON object and its exact parent array; `<copy-OB-3-as-OB-4>`, `<duplicate-OB-2>` and `<copy-binding-with-id=literal:size-one>` are exact deep copies with only that stated id replacement; compiler/run command placeholders are the selected printed command; RED event/ledger/commit/previous-commit values bind the selected resume intent, writer authority and immediate predecessor; result/deliver/archive path/mode/blob/bytes/source/target/parent values bind the selected branch tuple and exact graph tree; rename/other-suffix/case-collision values are deterministic nonce-local paths inside the same declared class. `<exact-full-result-history-bytes>`, `<exact-result-field-value>`, `<exact-call-id>`, `<exact-history-trailer>` and `<semantic-ledger-bytes>` bind the selected `return_result_ref` and its corresponding named ledger. Any zero-match, multi-match, missing typed source, undeclared placeholder name or expansion that leaves an angle variable is a corpus materialization failure before checker execution.

`x` between two `EACH_*` names is their left-major Cartesian product. `EACH_WRITER_FINALIZATION` binds exact intent/receipt/observation values from the selected full finalized CALL. `EACH_OBLIGATION` binds both the compile-source list and separate runtime-resource list. `EACH_NEGATIVE_SHAPE` binds source, instance, ExpectedPhase callable and ObservedPhase callable. Each recovery tuple binds snapshot, deliver node, result path, result blob token and routing hash token; `<routing-bytes>` uses that tuple's path and final LF. SETUP interview under RE-SYNC binds `initialized|3|resync-interview-inventory-hash` and `/resync/manifest`.

```text
call-intent-executed	J(execute,/call/packet_stage,"finalized","intent")	nonzero
call-guessed-finalization	RAWJ(execute,/call/finalization_receipt,<computed:preexec-finalization-receipt>,"guessed")	nonzero
call-tampered-observation	RAWJ(execute,/call/writer_observation_hash,<computed:preexec-observation-hash>,"tampered")	nonzero
call-stale-head	TA(P,foreign.txt,100644,"after finalization\n",P)	nonzero
call-wrong-worktree	J(execute,/call/worktree,<computed:random-root>,"C:/foreign")	nonzero
call-session-owned-writer-field	JA(execute,/call/writer_field_origin,<absent>,"session")	nonzero
call-envelope-field-missing	EACH_PHASE_SNAPSHOT x EACH_CALL_ENVELOPE_FIELD JD(<snapshot>,<envelope-pointer>,<exact-envelope-value>)	nonzero
call-stable-leaf-missing	EACH_WRITER_FINALIZATION x EACH_STABLE_CALL_LEAF JD(<snapshot>,<stable-pointer>,<exact-stable-value>)	nonzero
call-stable-leaf-changed	EACH_WRITER_FINALIZATION x EACH_STABLE_CALL_LEAF J(<snapshot>,<stable-pointer>,<exact-stable-value>,<coherent-wrong-stable-value>)	nonzero
call-identity-leaf-missing	EACH_PHASE_SNAPSHOT x EACH_IDENTITY_LEAF JD(<snapshot>,<identity-pointer>,<exact-identity-value>)	nonzero
call-identity-leaf-wrong	EACH_PHASE_SNAPSHOT x EACH_IDENTITY_LEAF J(<snapshot>,<identity-pointer>,<exact-identity-value>,<coherent-wrong-identity-value>)	nonzero
call-return-mutates-finalized-call	EACH_RETURN_SNAPSHOT x EACH_STABLE_CALL_LEAF J(<snapshot>,<stable-pointer>,<exact-stable-value>,<coherent-wrong-stable-value>)	nonzero
call-writer-field-present-in-intent	EACH_WRITER_FINALIZATION JA_INTENT(<snapshot>,/writer,<absent>,<exact-writer-object>)	nonzero
call-finalization-intent-ref-mismatch	EACH_WRITER_FINALIZATION C(/writer_finalizations/<finalization>/intent_ref,<exact-intent-ref>,<different-intent-ref>)	nonzero
call-literal-snapshot-copy-forbidden	EACH_PHASE_SNAPSHOT CA(/snapshots/<snapshot>/call,<absent>,<exact-finalized-call-object>)	nonzero
call-packet-stage-missing	EACH_MODE JD(<snapshot>,/call/packet_stage,"finalized")	nonzero
call-packet-stage-not-final	EACH_MODE J(<snapshot>,/call/packet_stage,"finalized","intent")	nonzero
call-phase-missing	EACH_MODE JD(<snapshot>,/call/phase,<exact-phase>)	nonzero
call-phase-wrong	EACH_MODE J(<snapshot>,/call/phase,<exact-phase>,<different-phase>)	nonzero
call-packet-stage-missing-writer	EACH_WRITER_FINALIZATION JD(<snapshot>,/call/packet_stage,"finalized")	nonzero
call-packet-stage-not-final-writer	EACH_WRITER_FINALIZATION J(<snapshot>,/call/packet_stage,"finalized","intent")	nonzero
call-phase-missing-writer	EACH_WRITER_FINALIZATION JD(<snapshot>,/call/phase,<exact-phase>)	nonzero
call-phase-wrong-writer	EACH_WRITER_FINALIZATION J(<snapshot>,/call/phase,<exact-phase>,<different-phase>)	nonzero
call-repo-missing-writer	EACH_WRITER_FINALIZATION JD(<snapshot>,/call/repo,"fixture/product")	nonzero
call-worktree-missing-writer	EACH_WRITER_FINALIZATION JD(<snapshot>,/call/worktree,<computed:random-root>)	nonzero
call-intent-hash-missing-writer	EACH_WRITER_FINALIZATION JD(<snapshot>,/call/intent_hash,<exact-intent-hash>)	nonzero
call-intent-hash-wrong-writer	EACH_WRITER_FINALIZATION RAWJ(<snapshot>,/call/intent_hash,<exact-intent-hash>,"wrong")	nonzero
call-observation-hash-missing-writer	EACH_WRITER_FINALIZATION JD(<snapshot>,/call/writer_observation_hash,<exact-observation-hash>)	nonzero
call-substage-wrong	EACH_SUBSTAGE J(<snapshot>,<phase-substage-pointer>,<exact-substage>,<different-substage>)	nonzero
call-writer-finalization-missing	EACH_WRITER_FINALIZATION JD(<snapshot>,/call/finalization_receipt,<exact-receipt>)	nonzero
call-writer-finalization-stale	EACH_WRITER_FINALIZATION RAWJ(<snapshot>,/call/finalization_receipt,<exact-receipt>,"stale")	nonzero
abi-packet-path-missing	EACH_MODE ENV_DELETE(DIRECTION_PACKET_PATH,<computed:packet-path>)	nonzero
abi-packet-mode-wrong	EACH_MODE ENV_REPLACE(DIRECTION_PACKET_MODE,100644,100755)	nonzero
abi-packet-blob-wrong	EACH_MODE ENV_REPLACE(DIRECTION_PACKET_BLOB,<computed:packet-blob>,"wrong")	nonzero
abi-authority-path-missing	EACH_MODE ENV_DELETE(DIRECTION_AUTHORITY_PATH,<computed:authority-path>)	nonzero
abi-authority-mode-wrong	EACH_MODE ENV_REPLACE(DIRECTION_AUTHORITY_MODE,100644,100755)	nonzero
abi-authority-blob-wrong	EACH_MODE ENV_REPLACE(DIRECTION_AUTHORITY_BLOB,<computed:authority-blob>,"wrong")	nonzero
abi-extra-direction-field	EACH_MODE ENV_ADD(DIRECTION_PHASE,<absent>,"PLAN")	nonzero
abi-packet-mutated-by-checker	EACH_MODE SIDE_EFFECT(<computed:packet-path>,"append")	nonzero
abi-authority-mutated-by-checker	EACH_MODE SIDE_EFFECT(<computed:authority-path>,"append")	nonzero
abi-required-packet-leaf-missing	EACH_MODE x EACH_REQUIRED_PACKET_LEAF JD(<snapshot>,<leaf-pointer>,<leaf-value>)	nonzero
abi-authority-row-missing	EACH_MODE x EACH_AUTHORITY_ROW ARD(<snapshot>,<authority-row>,<authority-value>)	nonzero
abi-authority-row-wrong	EACH_MODE x EACH_AUTHORITY_ROW AR(<snapshot>,<authority-row>,<authority-value>,"foreign")	nonzero
abi-required-authority-as-na	EACH_REQUIRED_AUTHORITY_SLOT AR(<snapshot>,<authority-slot>,<exact-authority-row>,"<authority-slot>\tn/a")	nonzero
abi-na-authority-populated	EACH_NA_AUTHORITY_SLOT AR(<snapshot>,<authority-slot>,"<authority-slot>\tn/a",<foreign-well-formed-authority-row>)	nonzero
abi-nonreturn-result-present	EACH_NO_RESULT_SNAPSHOT J(<snapshot>,/wrapper/result_presence,"n/a","required")	nonzero
abi-nonreturn-result-history-present	EACH_NO_RESULT_SNAPSHOT J(<snapshot>,/wrapper/result_history_bytes,"n/a",<exact-full-result-history-bytes>)	nonzero
abi-return-result-absent	EACH_RETURN_SNAPSHOT J(<snapshot>,/wrapper/result_presence,"required","n/a")	nonzero
abi-return-history-absent	EACH_RETURN_SNAPSHOT J(<snapshot>,/wrapper/result_history_bytes,<exact-full-result-history-bytes>,"n/a")	nonzero
abi-return-result-envelope-field-missing	EACH_RETURN_SNAPSHOT x EACH_RESULT_ENVELOPE_FIELD JD(<snapshot>,/wrapper/result/<result-field>,<exact-result-field-value>)	nonzero
abi-return-result-call-id-wrong	EACH_RETURN_SNAPSHOT J(<snapshot>,/wrapper/result/call_id,<exact-call-id>,"foreign")	nonzero
abi-return-result-history-trailer-wrong	EACH_RETURN_SNAPSHOT J(<snapshot>,/wrapper/result/history_trailer,<exact-history-trailer>,"END_OF_FILE: foreign\n")	nonzero
abi-return-result-ledger-substitution	EACH_RETURN_SNAPSHOT J(<snapshot>,/wrapper/result_history_bytes,<exact-full-result-history-bytes>,<semantic-ledger-bytes>)	nonzero
abi-wrapper-transaction-stage-wrong	EACH_PHASE_SNAPSHOT J(<snapshot>,/wrapper/transaction_stage,<exact-transaction-stage>,<different-transaction-stage>)	nonzero
abi-wrapper-gate-mode-wrong	EACH_PHASE_SNAPSHOT J(<snapshot>,/wrapper/gate_mode,<exact-gate-mode>,<different-gate-mode>)	nonzero
abi-adapter-json-fragment-only	EACH_PHASE_SNAPSHOT ADAPTER_RENDER(<snapshot>,json-fragment)	nonzero
abi-adapter-extra-wrapper-field	EACH_PHASE_SNAPSHOT ADAPTER_RENDER(<snapshot>,extra-wrapper-field)	nonzero
bootstrap-install-missing-challenge	EACH_INSTALL ENV_DELETE(DIRECTION_CONFORMANCE_BOOTSTRAP_CHALLENGE,<computed:bootstrap-challenge>)	nonzero
bootstrap-install-authority-present	EACH_INSTALL ENV_ADD(DIRECTION_CONFORMANCE_AUTHORITY_RECEIPT,<absent>,"guessed-final")	nonzero
bootstrap-noninstall-challenge-present	EACH_NONINSTALL ENV_ADD(DIRECTION_CONFORMANCE_BOOTSTRAP_CHALLENGE,<absent>,<computed:bootstrap-challenge>)	nonzero
bootstrap-noninstall-missing-receipt	EACH_NONINSTALL JD(<snapshot>,/call/validation_conformance_receipt,<computed:bootstrap-receipt>)	nonzero
bootstrap-noninstall-wrong-receipt	EACH_NONINSTALL J(<snapshot>,/call/validation_conformance_receipt,<computed:bootstrap-receipt>,"wrong")	nonzero
bootstrap-writer-authority-missing	EACH_NONINSTALL ARD(<snapshot>,validation-conformance-receipt,<computed:bootstrap-receipt>)	nonzero
bootstrap-writer-authority-wrong	EACH_NONINSTALL AR(<snapshot>,validation-conformance-receipt,<computed:bootstrap-receipt>,"wrong-authority")	nonzero
bootstrap-receipt-changed-between-phases	J(resume_progress,/call/validation_conformance_receipt,<computed:bootstrap-receipt>,"other-phase")	nonzero
bootstrap-final-binding-wrong	EACH_NONINSTALL FINAL_VIEW(<snapshot>,"wrong-final",history/<computed:conformance-result-path>@<computed:C-final-conformance>,<computed:validation-conformance-receipt>)	nonzero
bootstrap-final-event-missing	EACH_NONINSTALL FINAL_VIEW(<snapshot>,<computed:validation-conformance-receipt>,<absent>,<computed:validation-conformance-receipt>)	nonzero
bootstrap-final-event-not-ancestral	EACH_NONINSTALL FINAL_VIEW(<snapshot>,<computed:validation-conformance-receipt>,history/foreign@<computed:foreign-writer-commit>,<computed:validation-conformance-receipt>)	nonzero
bootstrap-final-authority-wrong	EACH_NONINSTALL FINAL_VIEW(<snapshot>,<computed:validation-conformance-receipt>,history/<computed:conformance-result-path>@<computed:C-final-conformance>,"wrong-final")	nonzero
direction-conformance-result-crossed	EACH_CONFORMANCE_GATE DIR(<conformance-event>@<conformance-parent>,event-history-replace,<exact-conformance-result-bytes>,<wrong-conformance-result-bytes>)	nonzero
adapter-event-missing	CD@install(/toolchain/adapter_event,"history/<computed:adapter-review-result-path>@<computed:I-adapter-accept>")	nonzero
adapter-event-not-ancestral	C@install(/toolchain/adapter_event,"history/<computed:adapter-review-result-path>@<computed:I-adapter-accept>","history/foreign@<computed:foreign-writer-commit>")	nonzero
adapter-self-reviewed	C@install(/toolchain/adapter_review_session,<computed:adapter-review-session>,<computed:adapter-author-session>)	nonzero
adapter-installer-is-author	C@install(/toolchain/installer_session,<computed:installer-session>,<computed:adapter-author-session>)	nonzero
adapter-independence-coherent-author-review	DIR(adapter-independence,coherently-rewrite-every-author-review-session-field-and-event-payload-to-one-session)	nonzero
adapter-independence-coherent-author-installer	DIR(adapter-independence,coherently-rewrite-every-author-installer-session-field-and-event-payload-to-one-session)	nonzero
adapter-author-required-output-manifest-missing	JD(adapter_author_call,/call/required_output_manifest,"path|mode|blob|runtime|dependency-manifest-hash")	nonzero
adapter-author-product-write	J(adapter_author_call,/result_evidence/product_writes,[],["validation.config"])	nonzero
adapter-review-author-event-missing	EACH_ADAPTER_REVIEW_RETURN JD(<snapshot>,/call/author_event,"history/<computed:adapter-author-result-path>@<computed:I-adapter-author-result>")	nonzero
adapter-review-author-event-not-ancestral	EACH_ADAPTER_REVIEW_RETURN J(<snapshot>,/call/author_event,"history/<computed:adapter-author-result-path>@<computed:I-adapter-author-result>","history/foreign@<computed:foreign-writer-commit>")	nonzero
adapter-review-author-payload-mismatch	EACH_ADAPTER_REVIEW_RETURN AR(<snapshot>,adapter-author-payload,<computed:adapter-author-result-blob>,"wrong")	nonzero
adapter-review-product-write	EACH_ADAPTER_REVIEW_RETURN J(<snapshot>,/result_evidence/product_writes,[],["tools/plan-handoff-check.fixture"])	nonzero
adapter-review-output-manifest-path-mismatch	EACH_ADAPTER_REVIEW_RETURN J(<snapshot>,/result_evidence/reviewed_output_manifest_path,"work/validation-adapters/<computed:stack-id>-v21.manifest","work/validation-adapters/foreign.manifest")	nonzero
adapter-review-output-manifest-mode-mismatch	EACH_ADAPTER_REVIEW_RETURN J(<snapshot>,/result_evidence/reviewed_output_manifest_mode,"100644","100755")	nonzero
adapter-review-output-manifest-blob-mismatch	EACH_ADAPTER_REVIEW_RETURN J(<snapshot>,/result_evidence/reviewed_output_manifest_blob,<computed:adapter-output-manifest-blob>,"foreign")	nonzero
adapter-review-output-manifest-mismatch	EACH_ADAPTER_REVIEW_RETURN J(<snapshot>,/result_evidence/reviewed_output_manifest_hash,<computed:adapter-output-manifest-hash>,"foreign")	nonzero
adapter-author-source-artifact-missing	DIR(adapter-authored,omit-event-adds-row,adapter-source)	nonzero
adapter-author-manifest-artifact-missing	DIR(adapter-authored,omit-event-adds-row,adapter-output-manifest)	nonzero
adapter-author-artifact-path-wrong	DIR(adapter-authored,replace-selected-event-adds-path,adapter-source,"work/validation-adapters/foreign.fixture")	nonzero
adapter-author-artifact-mode-wrong	DIR(adapter-authored,replace-selected-event-adds-mode,adapter-output-manifest,"100755")	nonzero
adapter-author-artifact-blob-wrong	DIR(adapter-authored,replace-selected-event-adds-blob,adapter-output-manifest,"wrong")	nonzero
adapter-blob-changed-after-review	C@install(/toolchain/adapter_blob,<computed:accepted-adapter-blob>,<computed:changed-adapter-blob>)	nonzero
adapter-output-manifest-missing	CD@install(/toolchain/adapter_output_manifest_hash,<computed:adapter-output-manifest-hash>)	nonzero
adapter-output-manifest-wrong	C@install(/toolchain/adapter_output_manifest_hash,<computed:adapter-output-manifest-hash>,"wrong")	nonzero
adapter-output-manifest-path-wrong	C@install(/adapter_output_manifest/path,"work/validation-adapters/<computed:stack-id>-v21.manifest","work/validation-adapters/foreign.manifest")	nonzero
adapter-output-manifest-mode-wrong	C@install(/adapter_output_manifest/mode,"100644","100755")	nonzero
adapter-output-manifest-blob-wrong	C@install(/adapter_output_manifest/blob,<computed:adapter-output-manifest-blob>,"wrong")	nonzero
adapter-output-manifest-bytes-wrong	C@install(/adapter_output_manifest/bytes_ref,"ADAPTER_OUTPUT_MANIFEST_BYTES","foreign bytes")	nonzero
adapter-output-manifest-row-path-wrong	C@install(/adapter_output_manifest/rows/0/path,"validation.config","foreign.config")	nonzero
adapter-output-manifest-row-mode-wrong	C@install(/adapter_output_manifest/rows/3/mode,"100755","100644")	nonzero
adapter-output-manifest-row-blob-wrong	C@install(/adapter_output_manifest/rows/1/blob,<computed:checker-blob>,"wrong")	nonzero
adapter-output-manifest-row-runtime-wrong	C@install(/adapter_output_manifest/rows/5/runtime,"fixture-runner","foreign")	nonzero
adapter-output-manifest-row-dependency-wrong	C@install(/adapter_output_manifest/rows/5/dependency_manifest_hash,<computed:runner-dependency-manifest-hash>,"wrong")	nonzero
adapter-compiler-dependency-wrong	C@install(/toolchain/runtime_identity/compiler/dependency_manifest_hash,<computed:compiler-dependency-manifest-hash>,"wrong")	nonzero
adapter-before-interview	DIR(adapter-accepted,remove-ancestor-I-setup-interview)	nonzero
adapter-review-before-author-result	DIR(adapter-accepted,remove-ancestor-I-adapter-author-result)	nonzero
setup-interview-profile-missing	JD(setup_interview,/call/profile_blob,<computed:stack-profile-blob>)	nonzero
setup-interview-profile-stale	J(setup_interview,/call/profile_blob,<computed:stack-profile-blob>,"stale")	nonzero
setup-interview-inventory-stale	J(setup_interview,/result_evidence/target_inventory_hash,<computed:interview-inventory-hash>,"stale")	nonzero
setup-interview-product-write	J(setup_interview,/result_evidence/product_writes,[],["validation.config"])	nonzero
setup-install-missing-interview-event	EACH_INSTALL JD(<snapshot>,/call/interview_event,"history/<computed:setup-interview-result-path>@<computed:I-setup-interview>")	nonzero
setup-install-interview-event-not-ancestral	EACH_INSTALL J(<snapshot>,/call/interview_event,"history/<computed:setup-interview-result-path>@<computed:I-setup-interview>","history/foreign@<computed:foreign-writer-commit>")	nonzero
setup-install-interview-payload-mismatch	EACH_INSTALL AR(<snapshot>,setup-interview-payload,<computed:setup-interview-result-blob>,"wrong")	nonzero

finalizer-missing-intent	EACH_FINALIZER DIR(<instance>,delete-finalization-call)	nonzero
finalizer-stale-intent	EACH_FINALIZER DIR(<instance>,replace-child-intent-hash,"stale")	nonzero
finalizer-wrong-call-id	EACH_FINALIZER DIR(<instance>,replace-finalizer-id,"foreign")	nonzero
finalizer-event-path-wrong	EACH_FINALIZER DIR(<instance>,replace-event-path,"history/foreign.md")	nonzero
finalizer-event-session-wrong	EACH_FINALIZER DIR(<instance>,replace-event-session-id,"foreign")	nonzero
finalizer-event-payload-wrong	EACH_FINALIZER DIR(<instance>,replace-event-payload-hash,"foreign")	nonzero
finalizer-result-event-mode-wrong	EACH_FINALIZER DIR(<instance>,replace-finalizer-result-resolved-event-mode,"100755")	nonzero
finalizer-result-event-history-blob-wrong	EACH_FINALIZER DIR(<instance>,replace-finalizer-result-resolved-history-blob,"foreign")	nonzero
finalizer-child-parent-wrong	EACH_FINALIZER DIR(<instance>,parent-child-to-event-parent)	nonzero
finalizer-child-merge-parent	EACH_FINALIZER DIR(<instance>,add-second-child-parent)	nonzero
finalizer-next-wrong	EACH_FINALIZER DIR(<instance>,replace-next,"foreign")	nonzero
finalizer-result-bytes-wrong	EACH_FINALIZER DIR(<instance>,replace-finalizer-result-bytes,"wrong\n")	nonzero
finalizer-result-envelope-field-missing	EACH_FINALIZER x EACH_RESULT_ENVELOPE_FIELD DIR(<instance>,delete-result-field,<result-field>)	nonzero
finalizer-result-call-id-wrong	EACH_FINALIZER DIR(<instance>,replace-result-call-id,"foreign")	nonzero
finalizer-result-node-task-wrong	EACH_FINALIZER DIR(<instance>,replace-result-node-task,"foreign/foreign")	nonzero
finalizer-result-play-check-missing	EACH_FINALIZER DIR(<instance>,delete-one-of-five-play-check-rows)	nonzero
finalizer-result-next-bare-id	EACH_FINALIZER DIR(<instance>,replace-result-next-full-call-with-bare-child-id)	nonzero
finalizer-result-ledger-instead-of-history	EACH_FINALIZER DIR(<instance>,replace-full-result-history-with-semantic-ledger-payload)	nonzero
finalizer-stable-goal-edit	EACH_FINALIZER DIR(<instance>,edit-child-goal)	nonzero
finalizer-stable-done-when-edit	EACH_FINALIZER DIR(<instance>,edit-child-done-when)	nonzero
finalizer-extra-live-delta	EACH_FINALIZER DIR(<instance>,add-unrelated-NOW-field)	nonzero
finalizer-missing-history	EACH_FINALIZER DIR(<instance>,omit-finalizer-result-history)	nonzero
finalizer-missing-log	EACH_FINALIZER DIR(<instance>,omit-finalizer-LOG-line)	nonzero
finalizer-bad-trailer	EACH_FINALIZER DIR(<instance>,remove-END_OF_FILE)	nonzero
finalizer-same-commit-self-reference	EACH_FINALIZER DIR(<instance>,event-node-equals-child-node)	nonzero
finalizer-double-apply	EACH_FINALIZER DIR(<instance>,apply-child-result-after-finalizer-absent)	nonzero
finalizer-collect-before-child	EACH_FINALIZER DIR(<instance>,collect-finalization-call-as-product-child)	nonzero
finalizer-owner-dialogue	EACH_FINALIZER DIR(<instance>,record-owner-words-during-finalize)	nonzero
finalizer-product-command	EACH_FINALIZER DIR(<instance>,record-product-command-during-finalize)	nonzero

setup-create-collision	TA(S0,validation.config,100644,"foreign\n",none)	nonzero
setup-overlay-preimage-mismatch	TR(S0,AGENTS.md,"owner preface\n","owner changed\n")	nonzero
setup-overlay-unrelated-line-loss	TR(SB,AGENTS.md,"owner preface\n\nv21 run contract\n","v21 run contract\n")	nonzero
setup-protected-overwrite	CLEAN_SETUP_ALT(S0,SB-protected-overwrite,TR(SB,notes/owner.txt,"owner data\n","changed\n"))	nonzero
setup-protected-delete	CLEAN_SETUP_ALT(S0,SB-protected-delete,TD(SB,notes/owner.txt,"owner data\n"))	nonzero
setup-undeclared-add	CLEAN_SETUP_ALT(S0,SB-undeclared-add,TA(SB,extra.txt,100644,"extra\n",SB))	nonzero
setup-history-edit-restore-laundering	CLEAN_SETUP_HISTORY(S0,H1,H2,edit notes/owner.txt then restore exact bytes before final tree)	nonzero
setup-stale-inventory	J(setup,/call/protected_inventory_hash,<computed:setup-inventory-hash>,"stale")	nonzero
setup-half-initialized	TA(S0,validation.config,100644,"synced_contract_version: 20\n",none)	nonzero
setup-create-overlay-same-path	CA(/setup/manifest,<end>,{"op":"create","path":"AGENTS.md","class":"contract","source_mode":"100644","source_blob":"<computed:v21-agents-blob>"})	nonzero
setup-create-source-blob-wrong	EACH_SETUP_CREATE C@install(<setup-manifest-pointer>/0/source_blob,<computed:setup-agents-new-blob>,"wrong")	nonzero
setup-create-source-mode-wrong	EACH_SETUP_CREATE C@install(<setup-manifest-pointer>/0/source_mode,"100644","100755")	nonzero
setup-create-postimage-wrong	EACH_SETUP_CREATE ALT(<entry-tree>,setup-create-bad,TR(<post-tree>,AGENTS.md,"v21 run contract\n","wrong\n"))	nonzero
setup-overlay-patch-hash-wrong	C@install(/setup/manifest/1/patch_hash,<computed:setup-agents-patch-hash>,"wrong")	nonzero
setup-overlay-post-mode-wrong	C@install(/setup/manifest/1/post_mode,"100644","100755")	nonzero
setup-overlay-post-blob-wrong	C@install(/setup/manifest/1/post_blob,<computed:setup-agents-post-blob>,"wrong")	nonzero

resync-dirty	TA(RB,dirty.txt,100644,"uncommitted\n",none)	nonzero
resync-wrong-branch	J(resync,/call/branch,"codex/v21-resync","foreign")	nonzero
resync-wrong-base	C@install(/resync/identity/base,<computed:RB>,<computed:RS>)	nonzero
resync-source-touch	ALT(RB,RS-source-touch,TA(RS,src/Leak.fixture,100644,"source edit\n",RS))	nonzero
resync-test-touch	ALT(RB,RS-test-touch,TA(RS,tests/Foreign.fixture,100644,"test edit\n",RS))	nonzero
resync-feature-acceptance-touch	ALT(RB,RS-feature-touch,TA(RS,openspec/changes/foreign/spec.md,100644,"feature\n",RS))	nonzero
resync-history-edit-restore-laundering	HC(RB,H1|H2,edit src/Existing.fixture then RESTORE exact original before RS)	nonzero
resync-hidden-history	TA(RB,hidden.txt,100644,"historical\n",<computed:RB-parent>)	nonzero
resync-self-bumped-stamp	TR(RB,validation.config,CONFIG_V20,CONFIG_V21) before install	nonzero
resync-create-collision	TA(RB,tools/plan-handoff-check.fixture,100644,"foreign\n",RB)	nonzero
resync-overlay-unrelated-line-loss	TR(RS,AGENTS.md,"owner preface\nv21 run contract\n","v21 run contract\n")	nonzero
resync-overlay-wrong-postimage	TR(RS,validation.config,CONFIG_V21,"synced_contract_version: 21\n")	nonzero
resync-create-source-blob-wrong	C@install(/resync/manifest/2/source_blob,<computed:checker-blob>,"wrong")	nonzero
resync-create-source-mode-wrong	C@install(/resync/manifest/4/source_mode,"100755","100644")	nonzero
resync-overlay-patch-hash-wrong	C@install(/resync/manifest/0/patch_hash,<computed:v20-v21-config-patch-hash>,"wrong")	nonzero
resync-overlay-post-mode-wrong	C@install(/resync/manifest/1/post_mode,"100644","100755")	nonzero
resync-overlay-post-blob-wrong	C@install(/resync/manifest/1/post_blob,<computed:v21-agents-blob>,"wrong")	nonzero

plan-skipped	JD(plan_after_owner,/call/plan_receipt,<computed:plan-receipt>)	nonzero
plan-nonzero-observation	ACTUAL(plan_gated,run,"exit=1; stdout=plan failed\n")	nonzero
plan-tampered-observation	RAWJ(plan_gated,/plan_evidence/plan_observation_hash,<computed:plan-observation-hash>,"tampered")	nonzero
plan-author-illegal-owner-verdict	JA(plan_gated,/result_evidence/owner_words,<absent>,"ACCEPT")	nonzero
plan-verdict-call-missing-receipt	JD(verdict_call,/call/plan_receipt_event,"history/<computed:plan-gated-result-path>@<computed:W-plan-receipt>")	nonzero
plan-owner-result-late-receipt	J(plan_after_owner,/result_evidence/plan_receipt_event,"history/<computed:plan-gated-result-path>@<computed:W-plan-receipt>","history/late@<computed:W-verdict-result>")	nonzero
plan-event-not-ancestral	J(verdict_call,/writer_event/commit,<computed:W-plan-receipt>,<computed:foreign-writer-commit>)	nonzero
plan-event-call-same-commit	J(verdict_call,/open_call_commit,<computed:W-verdict-call>,<computed:W-plan-receipt>)	nonzero
plan-result-not-after-call	DIR(owner-verdict,event-node-equals-W-verdict-call)	nonzero
plan-owner-cites-other-receipt	J(plan_after_owner,/result_evidence/owner_words,"ACCEPT exact candidate <computed:P> receipt <computed:plan-receipt>","ACCEPT foreign")	nonzero
plan-verdict-candidate-mismatch	J(verdict_call,/call/plan_candidate_head,<computed:P>,<computed:B>)	nonzero
plan-packet-edit-after-receipt	ALT(B,P-edited,TR(P,openspec/changes/v21-fixture-change/specs/core/spec.md,"OB-1 absent Create exact result\nOB-2 existing Step loopback once\nOB-3 source-isolated golden audit\n","OB-1 edited\nOB-2 existing Step loopback once\nOB-3 source-isolated golden audit\n"))	nonzero
plan-stale-receipt	J(plan_after_owner,/call/plan_candidate_head,<computed:P>,<computed:B>)	nonzero
plan-source-edit	TA(P,src/PlanLeak.fixture,100644,"source\n",P)	nonzero
plan-test-edit	TA(P,tests/PlanLeak.fixture,100644,"test\n",P)	nonzero
plan-toolchain-edit	TR(P,validation.config,CONFIG_V21,"changed\n")	nonzero
plan-unmanifested-edit	TA(P,docs/unmanifested.md,100644,"extra\n",P)	nonzero
plan-coverage-row-omitted	EACH_COVERAGE CD(/testability/coverage/<ordinal>,<exact-object>)	nonzero
plan-coverage-row-duplicated	EACH_COVERAGE CA(/testability/coverage/<next-ordinal>,absent,<duplicate-object>)	nonzero
plan-coverage-reordered	C(/testability/coverage,[0,1,2],[0,2,1])	nonzero
plan-coverage-merged	C(/testability/coverage/1/done_when_bytes,"DW-2 existing Step loopback once\n","DW-2 existing Step loopback once\nDW-3 source-isolated golden audit\n")	nonzero
plan-coverage-rewritten	EACH_COVERAGE C(/testability/coverage/<ordinal>/done_when_bytes,<exact-bytes>,"normalized\n")	nonzero
plan-obligation-orphan	CA(/testability/recipes/3,absent,<copy-OB-3-as-OB-4>)	nonzero
plan-obligation-duplicate	CA(/testability/recipes/3,absent,<duplicate-OB-2>)	nonzero
plan-obligation-missing	EACH_OBLIGATION CD(/testability/recipes/<ordinal>,<exact-object>)	nonzero
plan-tip-as-base	C@plan(/identity/base,<computed:B>,<computed:P>)	nonzero
plan-historical-build-as-base	C@plan(/identity/base,<computed:B>,"b94806deaaa3cbb56a8b6cda9baa75ac52f028c3")	nonzero
ref-moved-after-finalization	EACH_REAL_ID REF_DRIFT(<snapshot>,origin/main,<computed:B>,<computed:P>)	nonzero
ref-missing	EACH_REAL_ID REF_MISSING(<snapshot>,origin/main,<computed:B>)	nonzero
ref-wrong-observed-sha	EACH_REAL_ID REF_WRONG_OBSERVED(<snapshot>,origin/main,<computed:P>,<computed:B>)	nonzero
execute-next-done-when-shrink	J(execute,/call/done_when,"DW-1 absent Create exact result\nDW-2 existing Step loopback once\nDW-3 source-isolated golden audit\n","DW-1 absent Create exact result\n")	nonzero
execute-acceptance-source-rewrite	EACH_DESCENDANT J(<snapshot>,/call/acceptance_source,"call:v21-fixture#done_when","call:foreign#done_when")	nonzero
execute-acceptance-hash-rewrite	EACH_DESCENDANT J(<snapshot>,/call/acceptance_hash,<computed:acceptance-hash>,"foreign")	nonzero
testability-path-missing	EACH_REAL_ID JD(<snapshot>,/call/testability,"openspec/changes/v21-fixture-change/TESTABILITY.md")	nonzero
testability-mode-wrong	EACH_REAL_ID J(<snapshot>,/call/testability-mode,"100644","100755")	nonzero
testability-blob-wrong	EACH_REAL_ID J(<snapshot>,/call/testability-blob,<computed:testability-blob>,"foreign")	nonzero
testability-input-manifest-wrong	EACH_REAL_ID J(<snapshot>,/call/input-manifest-hash,<computed:input-manifest-hash>,"foreign")	nonzero
identity-worktree-wrong-late	EACH_REAL_ID J(<snapshot>,/call/worktree,<computed:random-root>,"C:/foreign")	nonzero
identity-branch-wrong-late	EACH_REAL_ID J(<snapshot>,/call/branch,"codex/v21-fixture","foreign")	nonzero
identity-base-wrong-late	EACH_REAL_ID J(<snapshot>,/call/base,<computed:B>,<computed:P>)	nonzero
identity-base-authority-wrong-late	EACH_REAL_ID J(<snapshot>,/call/base_authority,"sha:<computed:B>","sha:<computed:P>")	nonzero
identity-head-wrong-late	EACH_REAL_ID J(<snapshot>,/call/head,<snapshot-head>,<computed:foreign-Q>)	nonzero
frozen-packet-mutated-late	EACH_DESCENDANT x EACH_PACKET_MEMBER ALT(<semantic-parent>,frozen-bad,TR(<snapshot-tree>,<path>,<old>,"edited\n"))	nonzero
frozen-authority-mutated-late	EACH_DESCENDANT x EACH_AUTHORITY_MEMBER ALT(<semantic-parent>,authority-bad,TR(<snapshot-tree>,<path>,<old>,"edited\n"))	nonzero
testability-object-mutated-late	EACH_DESCENDANT ALT(<semantic-parent>,testability-bad,TR(<snapshot-tree>,<testability-path>,<exact-testability-bytes>,"edited\n"))	nonzero
light-frozen-change-self-declared	J(execute_light,/call/testability_mode,"coordinated-light","frozen")	nonzero
light-nonempty-g0-scan	J(execute_light,/light/matched_paths,[],["openspec/changes/v21-fixture/specs/core/spec.md"])	nonzero
light-scan-command-wrong	J(execute_light,/light/scan_command,"git -c core.quotepath=false ls-files -- openspec/changes/*/specs/*/spec.md","echo none")	nonzero
light-scan-nonzero	J(execute_light,/light/scan_exit,0,1)	nonzero
light-scan-observation-tampered	RAWJ(execute_light,/light/observation_hash,<computed:light-scan-observation-hash>,"tampered")	nonzero
light-testability-field-present	JA(execute_light,/call/testability_blob,absent,"fake")	nonzero
light-close-fake-archive-parent	J(close_light,/close_evidence/archive/archive_parent,<absent>,<computed:LD>)	nonzero
light-close-wrong-na-route	J(close_light,/close_evidence/archive/source,"n/a-light","openspec/changes/v21-light")	nonzero

recipe-record-missing	EACH_OBLIGATION x EACH_RECORD CD(/testability/recipes/<ordinal>/<record>,<exact-value>)	nonzero
recipe-nonempty-unresolved-binding	EACH_OBLIGATION C(/testability/recipes/<ordinal>/construct/args/0/source,<exact-binding-id>,"fixture:nonempty-but-undefined")	nonzero
recipe-skeleton-binding-step-omitted	CDV(/testability/recipes/0/skeleton,"bind:fixture:throw-after")	nonzero
recipe-skeleton-invocation-step-omitted	CDV(/testability/recipes/1/skeleton,"invoke:throw-after expected+observed before DW-2")	nonzero
binding-duplicate-id	CA(/testability/binding_registry/<end>,absent,<copy-binding-with-id=literal:size-one>)	nonzero
binding-registry-hash-tampered	RAWJ(plan_gated,/testability/binding_registry_hash,<computed:binding-registry-hash>,"tampered")	nonzero
expanded-source-set-hash-tampered	RAWJ(plan_gated,/testability/expanded_source_set_hash,<computed:expanded-source-set-hash>,"tampered")	nonzero
binding-file-path-missing	EACH_FILE_BINDING CD(/testability/binding_registry/<ordinal>/path,<binding-path>)	nonzero
binding-file-mode-wrong	EACH_FILE_BINDING C(/testability/binding_registry/<ordinal>/mode,"100644","100755")	nonzero
binding-file-blob-wrong	EACH_FILE_BINDING C(/testability/binding_registry/<ordinal>/blob,<binding-blob>,"wrong")	nonzero
binding-wrong-type	C(/testability/binding_registry[id=fixture:two-room-open-sealed-faces]/type,"Fixture.Topology","Fixture.Impulse")	nonzero
binding-wrong-arity	C(/testability/binding_registry[id=fixture:two-room-open-sealed-faces]/args,<two-exact-args>,<one-exact-arg>)	nonzero
binding-inaccessible	C(/testability/binding_registry[id=fixture:audit-reader]/visibility,"internal-friend:Fixture.Tests","private")	nonzero
binding-cycle	C(/testability/binding_registry[id=slot:ob1-core]/depends_on,["fixture:two-room-open-sealed-faces"],["fixture:owned-custom-handler"])	nonzero
binding-golden-bytes-missing	CD(/testability/binding_registry[id=fixture:golden-cell-result]/bytes,"cell=<computed:k>;counter=1;hidden=0\n")	nonzero
binding-golden-blob-wrong	C(/testability/binding_registry[id=fixture:golden-cell-result]/blob,<computed:golden-cell-blob>,"wrong")	nonzero
binding-source-neighbor-not-zero	C(/testability/binding_registry[id=fixture:source-isolated-input]/args/2/source,"literal:zero","literal:unit-impulse")	nonzero
binding-source-and-neighbor-aliased	C(/testability/binding_registry[id=fixture:source-isolated-input]/signature,"Fixture.SourceInput.Single(Fixture.FaceId,System.Int32,System.Int32)","Fixture.SourceInput.SingleSame(Fixture.FaceId,System.Int32)")	nonzero
binding-golden-hidden-state-wrong	C(/testability/binding_registry[id=fixture:golden-cell-result]/bytes,"cell=<computed:k>;counter=1;hidden=0\n","cell=<computed:k>;counter=1;hidden=1\n")	nonzero
binding-negative-golden-control-missing	CD(/testability/binding_registry[id=fixture:golden-hidden-flipped],<exact-object>)	nonzero
binding-negative-golden-control-equals-positive	C(/testability/binding_registry[id=fixture:golden-hidden-flipped]/bytes,"cell=<computed:k>;counter=1;hidden=1\n","cell=<computed:k>;counter=1;hidden=0\n")	nonzero
binding-topology-unconstructible	C(/testability/binding_registry[id=fixture:two-room-open-sealed-faces]/signature,"Fixture.Topology.TwoRoom(Fixture.FaceKind,Fixture.FaceKind)","Fixture.Topology.Missing(Fixture.FaceKind,Fixture.FaceKind)")	nonzero
binding-impulse-unconstructible	C(/testability/binding_registry[id=fixture:face-impulse]/signature,"Fixture.Impulse.AtFace(Fixture.FaceId,System.Int32)","Fixture.Impulse.Missing(Fixture.FaceId,System.Int32)")	nonzero
binding-handler-source-missing	CD(/testability/binding_registry[id=fixture:owned-handler-source],<exact-object>)	nonzero
binding-handler-instance-unconstructible	C(/testability/binding_registry[id=fixture:owned-custom-handler]/constructor,"Fixture.Tests.OwnedHandler(Fixture.Core)","Fixture.Tests.MissingHandler(Fixture.Core)")	nonzero
binding-handler-owner-callable-missing	CD(/testability/binding_registry[id=fixture:owned-handler-owner],<exact-object>)	nonzero
binding-handler-call-count-callable-missing	CD(/testability/binding_registry[id=fixture:owned-handler-call-count],<exact-object>)	nonzero
binding-audit-unconstructible	C(/testability/binding_registry[id=fixture:audit-reader]/signature,"Fixture.Audit.For(Fixture.Core)","Fixture.Audit.Missing(Fixture.Core)")	nonzero
binding-loopback-source-missing	CD(/testability/binding_registry[id=fixture:loopback-source],<exact-object>)	nonzero
binding-loopback-instance-unconstructible	C(/testability/binding_registry[id=fixture:loopback-delegates-once]/constructor,"Fixture.Tests.LoopbackOnce()","Fixture.Tests.MissingLoopback()")	nonzero
binding-loopback-delegation-callable-missing	CD(/testability/binding_registry[id=fixture:loopback-delegation-count],<exact-object>)	nonzero
binding-loopback-call-count-callable-missing	CD(/testability/binding_registry[id=fixture:loopback-call-count],<exact-object>)	nonzero
binding-negative-source-missing	EACH_NEGATIVE_SHAPE CD(/testability/binding_registry[id=<negative-source-id>],<exact-object>)	nonzero
binding-negative-instance-missing	EACH_NEGATIVE_SHAPE CD(/testability/binding_registry[id=<negative-instance-id>],<exact-object>)	nonzero
binding-negative-expected-callable-missing	EACH_NEGATIVE_SHAPE CD(/testability/binding_registry[id=<negative-expected-id>],<exact-object>)	nonzero
binding-negative-observed-callable-missing	EACH_NEGATIVE_SHAPE CD(/testability/binding_registry[id=<negative-observed-id>],<exact-object>)	nonzero
binding-fault-contract-missing	CD(/testability/binding_registry[id=fixture:fault-probe-contract-source],<exact-object>)	nonzero
binding-fault-selector-owner-wrong	C(/testability/binding_registry[id=fixture:fault-selector]/owner,"operation:Step","global")	nonzero
recipe-wrong-overload	C(/testability/recipes/0/construct/signature,"Fixture.Core.Create(System.Int32,Fixture.Topology)","Fixture.Core.Create()")	nonzero
recipe-omitted-argument	CD(/testability/recipes/0/construct/args/1,<exact-object>)	nonzero
recipe-owner-missing	CD(/testability/recipes/0/negative/owner,"operation:Step")	nonzero
recipe-visibility-wrong	C(/testability/recipes/0/negative/visibility,"internal-friend:Fixture.Tests","private")	nonzero
recipe-observation-vague	C(/testability/recipes/0/observe/signature,"Fixture.Audit.Read()","audit counters")	nonzero
recipe-injection-vague	C(/testability/recipes/0/negative/signature,"FixtureFault.Select(FixtureFaultKind)","fault hook")	nonzero
recipe-topology-missing	CD(/testability/recipes/0/source/topology,"fixture:two-room-open-sealed-faces")	nonzero
recipe-golden-missing	CD(/testability/recipes/0/source/golden,"fixture:golden-cell-result")	nonzero
recipe-golden-comparator-missing	CD(/testability/recipes/2/source/golden_comparator,"fixture:golden-comparator")	nonzero
recipe-source-isolation-missing	CD(/testability/recipes/0/source/source_isolation,"fixture:source-isolated-input")	nonzero
recipe-handler-owner-missing	CD(/testability/recipes/0/source/handler_owner,"fixture:owned-handler-owner")	nonzero
recipe-audit-hidden-observe-wrong	C(/testability/recipes/0/observe/returns,"slot:ob1-audit","slot:ob2-value")	nonzero
recipe-audit-ob3-route-missing	CDV(/testability/recipes/2/observe/routes,{"binding":"fixture:audit-reader-ob3-neighbor","args":[{"name":"core","type":"Fixture.Core","source":"slot:ob3-core-neighbor"}],"returns":"slot:ob3-audit-neighbor"})	nonzero
recipe-loopback-missing	CD(/testability/recipes/0/source/loopback,"fixture:loopback-delegates-once")	nonzero
recipe-delegation-missing	CD(/testability/recipes/0/negative/delegates,"Fixture.Core.Step(Fixture.Impulse,Fixture.ReactionHandler)")	nonzero
red-realization-direct-absent-api-claimed-green	C_ROUTE(/testability/recipes/0/red_realization,"reflection:Fixture.Core::Create(System.Int32,Fixture.Topology)",<exact-ob1-source>,"direct:Fixture.Core.Create(System.Int32,Fixture.Topology)",<direct-call-ob1-source>)	nonzero
red-realization-actual-compile-failure	ACTUAL(plan_gated,compile,"OB-2 expanded source syntax error; claimed exit=0")	nonzero
red-realization-actual-zero-discovery	ACTUAL(plan_gated,discover,"OB-2 ids=[] count=0; claimed count=1")	nonzero
red-realization-actual-duplicate-discovery	ACTUAL(plan_gated,discover,"OB-3 ids=[FixtureTests.OB_3,FixtureTests.OB_3] count=2; claimed count=1")	nonzero
red-realization-union-compile-failure	ACTUAL(plan_gated,compile,"union source set exit=1 although each isolated source claimed exit=0")	nonzero
red-realization-union-zero-discovery	ACTUAL(plan_gated,discover,"union compiled output ids=[] count=0")	nonzero
red-realization-union-extra-discovery	ACTUAL(plan_gated,discover,"union compiled output ids=[FixtureTests.OB_1,FixtureTests.OB_2,FixtureTests.OB_3,FixtureTests.Foreign] count=4")	nonzero
red-realization-actual-pass-claimed-red	ACTUAL(plan_gated,run,"OB-2 exit=0 PASS although metadata status=RED")	nonzero
red-realization-actual-wrong-red-criterion	ACTUAL(plan_gated,run,"OB-3 exit=1 unrelated crash although declared criterion=DW-3 golden mismatch")	nonzero
red-realization-wrong-filter	C(/testability/recipes/1/red_realization/discover/command,"tools/fixture-discover.fixture --assembly <computed:ob2-assembly-path> --filter FixtureTests.OB_2","tools/fixture-discover.fixture --assembly <computed:ob2-assembly-path> --filter NoTests")	nonzero
red-realization-discover-foreign-output	C(/testability/recipes/1/red_realization/discover/command,"tools/fixture-discover.fixture --assembly <computed:ob2-assembly-path> --filter FixtureTests.OB_2","tools/fixture-discover.fixture --assembly foreign --filter FixtureTests.OB_2")	nonzero
red-realization-compile-output-blob-wrong	C(/testability/recipes/1/red_realization/compile/output_blob,<computed:ob2-assembly-blob>,"wrong")	nonzero
red-realization-production-stub	C(/testability/recipes/0/red_realization/production_stub,false,true)	nonzero
red-realization-binding-source-list-missing	EACH_OBLIGATION CD(/testability/recipes/<ordinal>/red_realization/binding_sources,<exact-binding-source-list>)	nonzero
red-realization-binding-source-reachable-omitted	CDV(/testability/recipes/0/red_realization/binding_sources,{"role":"compile-source","node":"fixture:golden-comparator-source","path":"<computed:golden-comparator-path>","mode":"100644","blob":"<computed:golden-comparator-blob>"})	nonzero
red-realization-binding-source-unreachable-extra	CA(/testability/recipes/2/red_realization/binding_sources/<end>,absent,{"role":"compile-source","node":"fixture:throw-before-source","path":"<computed:throw-before-path>","mode":"100644","blob":"<computed:throw-before-blob>"})	nonzero
red-realization-binding-source-command-omits-helper	C(/testability/recipes/0/red_realization/compile/command,"tools/fixture-compiler.fixture --base <computed:B> --source <computed:ob1-test-source-path> --binding-sources <computed:fault-probe-contract-path> <computed:owned-handler-path> <computed:loopback-handler-path> <computed:throw-before-path> <computed:throw-during-path> <computed:throw-after-path> <computed:golden-comparator-path>","tools/fixture-compiler.fixture --base <computed:B> --source <computed:ob1-test-source-path> --binding-sources <computed:fault-probe-contract-path> <computed:owned-handler-path> <computed:loopback-handler-path> <computed:throw-before-path> <computed:throw-during-path> <computed:throw-after-path>")	nonzero
red-realization-union-binding-source-omitted	CDV(/testability/union_red_realization/binding_source_order,"<computed:golden-comparator-path>")	nonzero
red-realization-runtime-resource-list-missing	EACH_OBLIGATION CD(/testability/recipes/<ordinal>/red_realization/runtime_resources,<exact-runtime-resource-list>)	nonzero
red-realization-runtime-resource-omitted	EACH_RUNTIME_RESOURCE CDV(<resource-list-pointer>,<exact-resource-object>)	nonzero
red-realization-runtime-resource-extra	EACH_RUNTIME_RESOURCE CA(<resource-list-pointer>/<end>,absent,<different-valid-resource-object>)	nonzero
red-realization-runtime-resource-extra-empty-ob2	CA(/testability/recipes/1/red_realization/runtime_resources/0,absent,{"role":"runtime-resource","node":"fixture:golden-cell-result","path":"<computed:golden-cell-path>","mode":"100644","blob":"<computed:golden-cell-blob>"})	nonzero
red-realization-runtime-resource-mode-wrong	EACH_RUNTIME_RESOURCE C(<resource-pointer>/mode,"100644","100755")	nonzero
red-realization-runtime-resource-blob-wrong	EACH_RUNTIME_RESOURCE C(<resource-pointer>/blob,<exact-resource-blob>,"wrong")	nonzero
red-realization-runtime-resource-file-missing	EACH_RUNTIME_RESOURCE ACTUAL(plan_gated,run,"declared resource path absent")	nonzero
red-realization-runtime-resource-file-changed	EACH_RUNTIME_RESOURCE ACTUAL(plan_gated,run,"declared resource bytes differ from blob")	nonzero
red-realization-run-command-omits-resource	C(/testability/recipes/2/red_realization/run/command,<exact-ob3-run-command>,"tests/FixtureRunner.fixture --assembly <computed:ob3-assembly-path> --filter FixtureTests.OB_3 --runtime-resources none")	nonzero
red-realization-run-command-adds-resource-ob2	C(/testability/recipes/1/red_realization/run/command,<exact-ob2-run-command>,"tests/FixtureRunner.fixture --assembly <computed:ob2-assembly-path> --filter FixtureTests.OB_2 --runtime-resources <computed:golden-cell-path>@100644@<computed:golden-cell-blob>")	nonzero
red-realization-union-resource-omitted	CDV(/testability/union_red_realization/runtime_resource_order,{"path":"<computed:golden-source-two-path>","mode":"100644","blob":"<computed:golden-source-two-blob>"})	nonzero
red-realization-expanded-hash-excludes-resource	RAWJ(plan_gated,/testability/expanded_source_set_hash,<computed:expanded-source-set-hash>,<computed:expanded-source-set-without-resource-hash>)	nonzero
red-realization-compiler-identity-missing	EACH_OBLIGATION CD(/testability/recipes/<ordinal>/red_realization/compile/compiler_identity_ref,"toolchain.runtime_identity.compiler")	nonzero
red-realization-discover-identity-missing	EACH_OBLIGATION CD(/testability/recipes/<ordinal>/red_realization/discover/discover_identity_ref,"toolchain.runtime_identity.discover")	nonzero
red-realization-runner-identity-missing	EACH_OBLIGATION CD(/testability/recipes/<ordinal>/red_realization/run/runner_identity_ref,"toolchain.runtime_identity.runner")	nonzero
red-realization-compiler-mode-wrong	C(/toolchain/runtime_identity/compiler/mode,"100755","100644")	nonzero
red-realization-compiler-blob-wrong	C(/toolchain/runtime_identity/compiler/blob,<computed:fixture-compiler-blob>,"wrong")	nonzero
red-realization-compiler-runtime-wrong	C(/toolchain/runtime_identity/compiler/runtime,"fixture-compiler","foreign")	nonzero
red-realization-compiler-version-wrong	C(/toolchain/runtime_identity/compiler/version,"1","2")	nonzero
red-realization-compiler-dependency-wrong	C(/toolchain/runtime_identity/compiler/dependency_manifest_hash,<computed:compiler-dependency-manifest-hash>,"wrong")	nonzero
red-realization-discover-mode-wrong	C(/toolchain/runtime_identity/discover/mode,"100755","100644")	nonzero
red-realization-discover-blob-wrong	C(/toolchain/runtime_identity/discover/blob,<computed:fixture-discover-blob>,"wrong")	nonzero
red-realization-discover-runtime-wrong	C(/toolchain/runtime_identity/discover/runtime,"fixture-discover","foreign")	nonzero
red-realization-discover-version-wrong	C(/toolchain/runtime_identity/discover/version,"1","2")	nonzero
red-realization-discover-dependency-wrong	C(/toolchain/runtime_identity/discover/dependency_manifest_hash,<computed:discover-dependency-manifest-hash>,"wrong")	nonzero
red-realization-runner-mode-wrong	C(/toolchain/runtime_identity/runner/mode,"100755","100644")	nonzero
red-realization-runner-blob-wrong	C(/toolchain/runtime_identity/runner/blob,<computed:test-runner-blob>,"wrong")	nonzero
red-realization-runner-runtime-wrong	C(/toolchain/runtime_identity/runner/runtime,"fixture-runner","foreign")	nonzero
red-realization-runner-version-wrong	C(/toolchain/runtime_identity/runner/version,"1","2")	nonzero
red-realization-runner-dependency-wrong	C(/toolchain/runtime_identity/runner/dependency_manifest_hash,<computed:runner-dependency-manifest-hash>,"wrong")	nonzero
red-realization-runner-command-substituted	C(/testability/recipes/1/red_realization/run/command,<exact-ob2-run-command>,"tools/fixture-discover.fixture --assembly <computed:ob2-assembly-path>")	nonzero
red-realization-union-compiler-identity-missing	CD(/testability/union_red_realization/compile/compiler_identity_ref,"toolchain.runtime_identity.compiler")	nonzero
red-realization-union-discover-identity-missing	CD(/testability/union_red_realization/discover/discover_identity_ref,"toolchain.runtime_identity.discover")	nonzero
red-realization-union-runner-identity-missing	CD(/testability/union_red_realization/runs/0/runner_identity_ref,"toolchain.runtime_identity.runner")	nonzero
red-realization-runner-unlisted-load	LOAD(tests/FixtureRunner.fixture,<computed:runtime-path>)	nonzero
fault-phase-enum-collapsed	C(/testability/binding_registry[id=fixture:fault-probe-contract-source]/bytes,<exact-fault-contract-bytes>,"enum Fixture.Tests.NegativePhase { None, One }\ninterface Fixture.Tests.FaultProbe implements Fixture.ReactionHandler { ExpectedPhase():Fixture.Tests.NegativePhase; ObservedPhase():Fixture.Tests.NegativePhase; }\n")	nonzero
fault-phase-expected-marker-changed	EACH_NEGATIVE_SHAPE C(/testability/binding_registry[id=<negative-source-id>]/bytes,<exact-negative-source-bytes>,<wrong-expected-marker-source-bytes>)	nonzero
fault-phase-observed-marker-changed	EACH_NEGATIVE_SHAPE C(/testability/binding_registry[id=<negative-source-id>]/bytes,<exact-negative-source-bytes>,<wrong-observed-marker-source-bytes>)	nonzero
fault-phase-during-after-bodies-swapped	C_SWAP_BODY(fixture:throw-during-source,fixture:throw-after-source,preserve-names-and-signatures)	nonzero
fault-phase-observer-assertions-removed	ACTUAL(plan_gated,run,"OB-2 source omits ExpectedPhase/ObservedPhase assertions but metadata unchanged")	nonzero
source-isolation-neighbor-variant-zero	C(/testability/binding_registry[id=literal:neighbor-seven]/bytes,"<computed:n>","0")	nonzero
source-isolation-source-variant-same	C(/testability/binding_registry[id=literal:source-two]/bytes,"<computed:k2>","<computed:k>")	nonzero
source-isolation-coupled-source-neighbor	C_ROUTE(/testability/recipes/2/source,"fixture:source-same-neighbor-seven","fixture:source-two-neighbor-zero","coupled-source-and-neighbor","fixture:source-two-neighbor-n")	nonzero
source-isolation-golden-two-equals-one	C(/testability/binding_registry[id=fixture:golden-source-two]/bytes,"cell=<computed:k2>;counter=1;hidden=0\n","cell=<computed:k>;counter=1;hidden=0\n")	nonzero
source-isolation-actual-coupled-cases	ACTUAL(plan_gated,run,"OB-3 source replaces three independent core/input chains with one coupled core while claims unchanged")	nonzero

manifest-row-omitted	EACH_MANIFEST_KIND CD(/testability/manifest/<ordinal>,<exact-object>)	nonzero
manifest-row-duplicated	EACH_MANIFEST_KIND CA(/testability/manifest/<next-ordinal>,absent,<duplicate-object>)	nonzero
manifest-row-reordered	C(/testability/manifest,<canonical-order>,<swap-two-same-kind-rows>)	nonzero
manifest-row-noncanonical	EACH_MANIFEST_KIND C(/testability/manifest/<ordinal>/path,<canonical-path>,"./noncanonical/../path")	nonzero
manifest-row-case-collision	EACH_MANIFEST_KIND CA(/testability/manifest/<next-ordinal>,absent,<same-path-different-case>)	nonzero
manifest-wrong-baseline-base	C(/testability/manifest/5/base,<computed:B>,<computed:P>)	nonzero
manifest-object-symlink	EACH_MANIFEST_KIND TM(<object-tree>,<path>,100644,120000,"<computed:outside-link-target-bytes>")	nonzero
manifest-object-gitlink	EACH_MANIFEST_KIND TM(<object-tree>,<path>,100644,160000,<computed:disposable-gitlink-commit>)	nonzero
manifest-object-reparse	EACH_MANIFEST_KIND REPARSE(<object-tree>,<path>,<computed:outside-root>)	nonzero
manifest-object-mode-swap	EACH_MANIFEST_KIND TM(<object-tree>,<path>,100644,100755,<blob>)	nonzero
testability-object-symlink	EACH_REAL_ID TM(<snapshot-tree>,<testability-path>,100644,120000,"<computed:outside-link-target-bytes>")	nonzero
testability-object-gitlink	EACH_REAL_ID TM(<snapshot-tree>,<testability-path>,100644,160000,<computed:disposable-gitlink-commit>)	nonzero
testability-object-reparse	EACH_REAL_ID REPARSE(<snapshot-tree>,<testability-path>,<computed:outside-root>)	nonzero
testability-object-mode-swap	EACH_REAL_ID TM(<snapshot-tree>,<testability-path>,100644,100755,<computed:testability-blob>)	nonzero
testability-object-blob-changed	EACH_REAL_ID ALT(<semantic-parent>,testability-object-bad,TR(<snapshot-tree>,<testability-path>,<exact-testability-bytes>,"changed\n"))	nonzero

red-production-before-R	TA(P,src/Implementation.fixture,100644,"production before RED\n",P)	nonzero
red-mixed-source-test-R	TA(R,src/Implementation.fixture,100644,"mixed\n",R)	nonzero
red-extra-unmanifested-helper	TA(R,tests/HiddenHelper.fixture,100644,"helper\n",R)	nonzero
red-wrong-parent	J(red_boundary,/red_evidence/parent_head,<computed:P>,<computed:B>)	nonzero
red-wrong-author	J(red_boundary,/red_evidence/author_role,"independent-test-author","builder")	nonzero
red-wrong-session	J(red_boundary,/red_evidence/author_session,"fixture-red-1","builder-session")	nonzero
red-wrong-checkpoint	J(red_boundary,/red_evidence/checkpoint,<computed:R>,<computed:R1>)	nonzero
red-chain-skips-parent	J(red_chain,/red_evidence/chain,[<computed:R1>,<computed:R2>],[<computed:R2>])	nonzero
red-chain-foreign-middle	J(red_chain,/red_evidence/chain,[<computed:R1>,<computed:R2>],[<computed:foreign-Q>,<computed:R2>])	nonzero
red-chain-mixed-edit-restore-laundering	HC(P,R1-launder|R2-launder,ADD exact test plus edit src/PublicApi.fixture at R1; RESTORE exact source plus ADD exact oracle at R2; final tree equals canonical R2)	nonzero
red-chain-merge-terminal	MERGE_ALT(<computed:R1>,<computed:foreign-Q>,R2-merge,<exact-R2-tree>)	nonzero
red-chain-wrong-immediate-parent	ALT(P,R2-wrong-parent,ADD exact oracle to canonical R1 tree while omitting R1 parent)	nonzero
red-chain-only-terminal-union	ACTUAL(red_chain,history,"validate only P..R2 union and skip R1/P plus R2/R1 per-commit allowlists")	nonzero
red-allowed-delta-wrong	J(red_boundary,/red_evidence/allowed_delta,<two-exact-paths>,["tests/FixtureTests.fixture"])	nonzero
red-registration-wrong	J(red_boundary,/red_evidence/registration,"Fixture.Tests","Foreign.Tests")	nonzero
red-filter-wrong	J(red_boundary,/red_evidence/filter,"FixtureTests.OB_*","NoTests")	nonzero
red-expected-wrong	J(red_boundary,/red_evidence/expected,<three-exact-criteria>,["other criterion"])	nonzero
red-status-wrong	J(red_boundary,/red_evidence/status,"RED","GREEN")	nonzero
red-actual-compile-error-claimed-red	ACTUAL(red_boundary,compile,"exit=1 syntax error; metadata compile_exit=0 status=RED")	nonzero
red-actual-zero-discovery-claimed-red	ACTUAL(red_boundary,discover,"ids=[] count=0; metadata count=3 status=RED")	nonzero
red-actual-duplicate-discovery-claimed-red	ACTUAL(red_boundary,discover,"duplicate FixtureTests.OB_2; metadata count=3 status=RED")	nonzero
red-actual-pass-claimed-red	ACTUAL(red_boundary,run,"exit=0 PASS; metadata status=RED")	nonzero
red-actual-other-criterion	ACTUAL(red_boundary,run,"exit=1 unrelated crash; metadata expected exact three")	nonzero
red-protected-delete	EACH_RED_MEMBER HC(Q,h1,TD(Q,<path>,<old>)); deliver from h1	nonzero
red-protected-rename	EACH_RED_MEMBER HC(Q,h1,RENAME(Q,<path>,<renamed-path>)); deliver from h1	nonzero
red-protected-edit-restore	EACH_RED_MEMBER HC(Q,h1,TR(Q,<path>,<old>,"edited\n")); HC(h1,h2,RESTORE(h1,<path>,<old>)); deliver from h2 with final bytes equal R	nonzero
red-manifest-rewrite	J(resume_progress,/call/red_manifest_hash,<computed:oracle-manifest-hash>,"rewritten")	nonzero
red-shadow-id	TA(R,tests/Shadow.fixture,100644,"FixtureTests.OB_2\n",R)	nonzero
red-duplicate-id	J(red_boundary,/red_evidence/unique_ids,["FixtureTests.OB_1","FixtureTests.OB_2","FixtureTests.OB_3"],["FixtureTests.OB_1","FixtureTests.OB_2","FixtureTests.OB_2"])	nonzero
red-revision-wrong-parent	J(red_revision,/red_evidence/revision/parent_head,<computed:Q>,<computed:R>)	nonzero
red-revision-mixed-source	TA(T,src/RevisionLeak.fixture,100644,"mixed\n",T)	nonzero
red-revision-extra-helper	TA(T,tests/RevisionHelper.fixture,100644,"unmanifested\n",T)	nonzero
red-revision-registration-wrong	J(red_revision,/red_evidence/revision/registration,"Fixture.Tests","Foreign.Tests")	nonzero
red-revision-filter-wrong	J(red_revision,/red_evidence/revision/filter,"FixtureTests.OB_*","NoTests")	nonzero
red-revision-drops-frozen-obligation-assert	ALT(Q,revision-acceptance-bad,TEXT_DELETE_EXACT(T,tests/FixtureTests.fixture,"assert DW-1 absent Create exact result\n"))	nonzero
red-revision-relabels-frozen-obligation	ALT(Q,revision-oracle-bad,TR(T,docs/validation/oracle-v21-fixture.json,ORACLE_BYTES,"FixtureTests.OB_1|foreign meaning|RED\nFixtureTests.OB_2|DW-2 loopback count|RED\nFixtureTests.OB_3|DW-3 golden mismatch|RED\n"))	nonzero
red-revision-actual-zero-discovery	ACTUAL(red_revision,discover,"ids=[] count=0; metadata count=6")	nonzero
red-revision-actual-pass	ACTUAL(red_revision,run,"exit=0 PASS; metadata status=RED")	nonzero
red-revision-original-member-deleted	EACH_RED_MEMBER ALT(Q,revision-original-delete,TD(T,<path>,<old>))	nonzero
red-revision-original-member-edited	EACH_RED_MEMBER ALT(Q,revision-original-edit,TR(T,<path>,<old>,"edited original\n"))	nonzero
red-revision-variant-member-deleted	EACH_VARIANT_MEMBER ALT(Q,revision-variant-delete,TD(T,<path>,<old>))	nonzero
red-revision-reuses-original-id	ALT(Q,revision-id-reuse,TR(T,tests/FixtureTestsV2.fixture,VARIANT_TEST_BYTES,REPLACE_EXACT(VARIANT_TEST_BYTES,"FixtureTests.OB_1_V2","FixtureTests.OB_1")))	nonzero
red-revision-only-three-discovered	J(red_revision,/red_evidence/revision/discovery_count,6,3)	nonzero
red-revision-only-original-run	ACTUAL(red_revision,run,"only FixtureTests.OB_1..OB_3 executed; variants skipped")	nonzero
red-revision-only-variant-run	ACTUAL(red_revision,run,"only FixtureTests.OB_1_V2..OB_3_V2 executed; originals skipped")	nonzero
resume-revision-original-event-missing	JD(resume_revision,/call/original_red_event,"history/red-result.md@<computed:E-red-accept>")	nonzero
resume-revision-original-manifest-missing	JD(resume_revision,/call/original_red_manifest_hash,<computed:oracle-manifest-hash>)	nonzero
deliver-revision-loses-original-member	EACH_RED_MEMBER ALT(U,D2-original-loss,TD(D2,<path>,<old>))	nonzero
deliver-revision-loses-variant-member	EACH_VARIANT_MEMBER ALT(U,D2-variant-loss,TD(D2,<path>,<old>))	nonzero
archive-revision-loses-original-member	EACH_RED_MEMBER ALT(D2,A2-original-loss,TD(A2,<path>,<old>))	nonzero
archive-revision-loses-variant-member	EACH_VARIANT_MEMBER ALT(D2,A2-variant-loss,TD(A2,<path>,<old>))	nonzero

resume-wrong-run	J(resume_progress,/call/run_id,<computed:run-id>,"foreign")	nonzero
resume-foreign-source	TA(Q,src/Foreign.fixture,100644,"foreign\n",Q)	nonzero
resume-rewritten-R	TR(Q,tests/FixtureTests.fixture,<exact-R-bytes>,"rewritten\n")	nonzero
resume-progress-event-missing	EACH_RESUME JD(<snapshot>,/call/progress_event,<exact-event>)	nonzero
resume-progress-event-not-ancestral	EACH_RESUME J(<snapshot>,/call/progress_event,<exact-event>,"history/foreign@<computed:foreign-writer-commit>")	nonzero
resume-progress-event-payload-mismatch	EACH_RESUME J(<snapshot>,/writer_authority/payload_hash,<exact-ledger-blob>,"foreign")	nonzero
resume-clean-same-run-never-accepted	UNACCEPTED_PROGRESS(R,<computed:Q-unaccepted>,<same-run-unaccepted-source>)	nonzero
resume-unaccepted-progress	J(resume_progress,/call/progress_commit,<computed:Q>,<computed:foreign-Q>)	nonzero
resume-ledger-mismatch	J(resume_progress,/call/progress_ledger_blob,<computed:q-accepted-ledger-blob>,"foreign")	nonzero
resume-historical-checkpoint	J(resume_progress,/call/progress_commit,<computed:Q>,"b94806deaaa3cbb56a8b6cda9baa75ac52f028c3")	nonzero
resume-guessed-finalization	EACH_RESUME RAWJ(<snapshot>,/call/finalization_receipt,<exact-receipt>,"guessed")	nonzero
resume-stale-finalization	EACH_RESUME J(<snapshot>,/call/progress_commit,<exact-commit>,<previous-commit>)	nonzero

deliver-latest-tests-still-red	EACH_DELIVER_BRANCH ACTUAL(<snapshot>,run,"latest accepted tests exit=1 expected RED; result otherwise coherent")	nonzero
deliver-latest-tests-pass-wrong-reason	EACH_DELIVER_BRANCH ACTUAL(<snapshot>,run,"exit=0 but expected criteria not executed")	nonzero
deliver-zero-discovery	EACH_DELIVER_BRANCH ACTUAL(<snapshot>,discover,"ids=[] count=0; result otherwise coherent")	nonzero
deliver-duplicate-discovery	EACH_DELIVER_BRANCH ACTUAL(<snapshot>,discover,"duplicate protected id; result otherwise coherent")	nonzero
deliver-oracle-criterion-mismatch	EACH_DELIVER_BRANCH ACTUAL(<snapshot>,run,"PASS against foreign criterion")	nonzero
deliver-evidence-observed-head-missing	EACH_DELIVER_BRANCH JD(<snapshot>,/deliver_evidence/observed_head,<deliver-node>)	nonzero
deliver-evidence-observed-head-wrong	EACH_DELIVER_BRANCH J(<snapshot>,/deliver_evidence/observed_head,<deliver-node>,<computed:foreign-Q>)	nonzero
deliver-evidence-prearchive-missing	EACH_DELIVER_BRANCH JD(<snapshot>,/deliver_evidence/prearchive_commit,<deliver-node>)	nonzero
deliver-evidence-prearchive-wrong	EACH_DELIVER_BRANCH J(<snapshot>,/deliver_evidence/prearchive_commit,<deliver-node>,<computed:foreign-Q>)	nonzero
deliver-evidence-result-path-missing	EACH_DELIVER_BRANCH JD(<snapshot>,/deliver_evidence/product_result_path,<result-path>)	nonzero
deliver-evidence-result-path-wrong	EACH_DELIVER_BRANCH J(<snapshot>,/deliver_evidence/product_result_path,<result-path>,"RESULT.md")	nonzero
deliver-evidence-result-blob-missing	EACH_DELIVER_BRANCH JD(<snapshot>,/deliver_evidence/result_blob,<result-blob>)	nonzero
deliver-evidence-result-blob-wrong	EACH_DELIVER_BRANCH J(<snapshot>,/deliver_evidence/result_blob,<result-blob>,"wrong")	nonzero
result-self-hash	EACH_RESULT_BRANCH ALT(<semantic-parent>,result-self,TR(<deliver-tree>,<result-path>,<result-bytes>,<result-bytes> plus "self: <computed:result-self>\n"))	nonzero
result-missing-required-field	EACH_RESULT_BRANCH x EACH_RESULT_FIELD ALT(<semantic-parent>,result-missing-<field>,TEXT_DELETE_EXACT(<deliver-tree>,<result-path>,"<field>: <exact-value>\n"))	nonzero
result-identity-value-wrong	EACH_RESULT_BRANCH x EACH_RESULT_IDENTITY ALT(<semantic-parent>,result-wrong-<field>,TR(<deliver-tree>,<result-path>,"<field>: <exact-value>\n","<field>: foreign\n"))	nonzero
result-required-value-empty	EACH_RESULT_BRANCH x EACH_RESULT_REQUIRED ALT(<semantic-parent>,result-empty-<field>,TR(<deliver-tree>,<result-path>,"<field>: <exact-value>\n","<field>: \n"))	nonzero
result-duplicate-key	EACH_RESULT_BRANCH x EACH_RESULT_FIELD ALT(<semantic-parent>,result-duplicate-<field>,TR(<deliver-tree>,<result-path>,<result-bytes>,<result-bytes> plus "<field>: duplicate\n"))	nonzero
result-call-path-substitution	EACH_DELIVER_BRANCH J(<snapshot>,/call/product_result_path,<result-path>,"RESULT.md")	nonzero
result-wrong-path	EACH_RESULT_BRANCH ALT(<semantic-parent>,result-wrong-path,RENAME(<deliver-tree>,<result-path>,RESULT.md))	nonzero
result-unparseable-blob	EACH_RESULT_BRANCH ALT(<semantic-parent>,result-wrong-blob,TR(<deliver-tree>,<result-path>,<result-bytes>,"wrong\n"))	nonzero
archive-nonadjacent	EACH_ARCHIVE_BRANCH J(<snapshot>,/close_evidence/archive/archive_parent,<deliver-tree>,<semantic-parent>)	nonzero
archive-merge-parent	EACH_ARCHIVE_BRANCH MERGE_ALT(<deliver-tree>,<computed:foreign-Q>,archive-merge,<exact-A-tree>)	nonzero
archive-result-edit	EACH_ARCHIVE_BRANCH ALT(<deliver-tree>,archive-result-edit,TR(<archive-tree>,<result-path>,<result-bytes>,"edited\n"))	nonzero
archive-toolchain-edit	EACH_ARCHIVE_BRANCH ALT(<deliver-tree>,archive-toolchain-edit,TR(<archive-tree>,validation.config,CONFIG_V21,"changed\n"))	nonzero
archive-oracle-edit	EACH_ARCHIVE_BRANCH ALT(<deliver-tree>,archive-oracle-edit,TR(<archive-tree>,docs/validation/oracle-v21-fixture.json,<oracle-bytes>,"edited\n"))	nonzero
archive-zero-root	EACH_ARCHIVE_BRANCH ALT(<deliver-tree>,archive-zero-root,TDIR(<archive-tree>,openspec/changes/archive/v21-fixture-change/**))	nonzero
archive-duplicate-root	EACH_ARCHIVE_BRANCH ALT(<deliver-tree>,archive-duplicate-root,TA(<archive-tree>,openspec/changes/archive/v21-fixture-copy/specs/core/spec.md,100644,<exact-spec-bytes>,none))	nonzero
archive-source-left-beside-target	EACH_ARCHIVE_BRANCH x EACH_PACKET_MEMBER ALT(<deliver-tree>,archive-source-left,TA(<archive-tree>,<original-source-path>,<mode>,<blob-bytes>,none))	nonzero
archive-missing-member	EACH_ARCHIVE_BRANCH x EACH_PACKET_MEMBER ALT(<deliver-tree>,archive-missing,TD(<archive-tree>,<archive-path>,<old>))	nonzero
archive-renamed-member	EACH_ARCHIVE_BRANCH x EACH_PACKET_MEMBER ALT(<deliver-tree>,archive-renamed,RENAME(<archive-tree>,<archive-path>,<other-suffix>))	nonzero
archive-edited-member	EACH_ARCHIVE_BRANCH x EACH_PACKET_MEMBER ALT(<deliver-tree>,archive-edited,TR(<archive-tree>,<archive-path>,<old>,"edited\n"))	nonzero
archive-mode-swapped-member	EACH_ARCHIVE_BRANCH x EACH_PACKET_MEMBER ALT(<deliver-tree>,archive-mode,TM(<archive-tree>,<archive-path>,100644,100755,<blob>))	nonzero
archive-extra-member	EACH_ARCHIVE_BRANCH ALT(<deliver-tree>,archive-extra,TA(<archive-tree>,openspec/changes/archive/v21-fixture-change/extra.md,100644,"extra\n",none))	nonzero
archive-undeclared-output	EACH_ARCHIVE_BRANCH ALT(<deliver-tree>,archive-output,TA(<archive-tree>,docs/undeclared-after-D.md,100644,"extra\n",none))	nonzero
archive-authority-edit	EACH_ARCHIVE_BRANCH ALT(<deliver-tree>,archive-authority,TR(<archive-tree>,docs/adr/ADR-v21-fixture.md,"ADR-v21-fixture\n","edited\n"))	nonzero
close-inherited-deliver-head-missing	EACH_CLOSE_BRANCH JD(<snapshot>,/deliver_evidence/observed_head,<deliver-node>)	nonzero
close-inherited-deliver-prearchive-wrong	EACH_CLOSE_BRANCH J(<snapshot>,/deliver_evidence/prearchive_commit,<deliver-node>,<computed:foreign-Q>)	nonzero
close-inherited-deliver-path-wrong	EACH_CLOSE_BRANCH J(<snapshot>,/deliver_evidence/product_result_path,<result-path>,"RESULT.md")	nonzero
close-inherited-deliver-blob-wrong	EACH_CLOSE_BRANCH J(<snapshot>,/deliver_evidence/result_blob,<result-blob>,"wrong")	nonzero
close-observed-head-missing	EACH_CLOSE_BRANCH JD(<snapshot>,/close_evidence/observed_head,<archive-node>)	nonzero
close-observed-head-wrong	EACH_CLOSE_BRANCH J(<snapshot>,/close_evidence/observed_head,<archive-node>,<computed:foreign-Q>)	nonzero
close-archive-deliver-wrong	EACH_CLOSE_BRANCH J(<snapshot>,/close_evidence/archive/deliver,<deliver-node>,<computed:foreign-Q>)	nonzero
close-archive-node-wrong	EACH_CLOSE_BRANCH J(<snapshot>,/close_evidence/archive/archive,<archive-node>,<computed:foreign-Q>)	nonzero
close-archive-parent-wrong	EACH_CLOSE_BRANCH J(<snapshot>,/close_evidence/archive/archive_parent,<archive-parent>,<computed:foreign-Q>)	nonzero
close-archive-parent-count-wrong	EACH_CLOSE_BRANCH J(<snapshot>,/close_evidence/archive/archive_parent_count,<archive-parent-count>,2)	nonzero
close-archive-source-wrong	EACH_CLOSE_BRANCH J(<snapshot>,/close_evidence/archive/source,<archive-source>,"foreign")	nonzero
close-archive-target-wrong	EACH_CLOSE_BRANCH J(<snapshot>,/close_evidence/archive/target,<archive-target>,"foreign")	nonzero
close-wrong-baseline-base	EACH_CLOSE_BRANCH C@close(/testability/manifest/5/base,<computed:B>,<computed:P>)	nonzero
recovery-deliver-empty-output	EACH_RECOVERY_DELIVER ROUTE_OUTPUT(<snapshot>,<routing-bytes>,"")	nonzero
recovery-deliver-wrong-output	EACH_RECOVERY_DELIVER ROUTE_OUTPUT(<snapshot>,<routing-bytes>,"foreign|wrong/path|wrong\n")	nonzero
recovery-close-empty-output	EACH_RECOVERY_CLOSE ROUTE_OUTPUT(<snapshot>,<routing-bytes>,"")	nonzero
recovery-close-wrong-parent-output	EACH_RECOVERY_CLOSE ROUTE_OUTPUT(<snapshot>,<routing-bytes>,"foreign|docs/results/v21-fixture-change.md|wrong\n")	nonzero

trust-root-omitted-each-mode	EACH_INSTALLED_MODE CD(/toolchain/roots/1,<exact-object>)	nonzero
trust-root-substituted-each-mode	EACH_INSTALLED_MODE TR(<snapshot-tree>,tools/plan-handoff-check.fixture,CHECKER_BYTES,"exit 0\n")	nonzero
trust-root-symlink-each-mode	EACH_INSTALLED_MODE TM(<snapshot-tree>,tools/plan-handoff-check.fixture,100644,120000,"<computed:outside-link-target-bytes>")	nonzero
trust-root-gitlink-each-mode	EACH_INSTALLED_MODE TM(<snapshot-tree>,tools/plan-handoff-check.fixture,100644,160000,<computed:disposable-gitlink-commit>)	nonzero
trust-root-reparse-outside-each-mode	EACH_INSTALLED_MODE REPARSE(<snapshot-tree>,tools/plan-handoff-check.fixture,<computed:outside-root>)	nonzero
trust-root-case-collision-each-mode	EACH_INSTALLED_MODE TA(<snapshot-tree>,tools/PLAN-HANDOFF-CHECK.fixture,100644,"collision\n",<snapshot-head>)	nonzero
trust-root-mode-swap-each-mode	EACH_INSTALLED_MODE TM(<snapshot-tree>,tools/plan-handoff-check.fixture,100644,100755,<computed:checker-blob>)	nonzero
trust-root-unlisted-load-each-mode	EACH_INSTALLED_MODE LOAD(<snapshot-tree>,tools/unlisted-helper.fixture)	nonzero
trust-root-dynamic-load-each-mode	EACH_INSTALLED_MODE LOAD(<snapshot-tree>,<computed:runtime-path>)	nonzero
trust-root-checker-before-pin-each-mode	EACH_INSTALLED_MODE RUN_BEFORE_PIN(<snapshot>,tools/plan-handoff-check.fixture)	nonzero
checker-mutates-each-mode	EACH_INSTALLED_MODE SIDE_EFFECT(<snapshot-tree>,checker-mutated.txt,"bad\n")	nonzero
```

## Bootstrap meta-witnesses and external receipt

Writer also substitutes: (1) always-zero; (2) switches on case/order/root; (3) switches on canonical or first-nonce repo/branch/change/path/type/member/test/criterion fingerprint; (4) switches on git commit message/timestamp/current hash learned from the first nonce/order; (5) accepts a fixture nickname without resolving the binding DAG or actual compile/discovery; (6) validates only coverage/recipe index zero; (7) removes each declared defect after declaration; and (8) omits an expanded mutation or changes adapter/specimen. It then executes the closed hybrid matrix `2 nonces x 2 random roots x 2 case permutations x 2 isomorphic product/Direction histories`: each history has identical semantic bytes and topology but fresh product commit ids and fresh Direction event ids. For every cell it substitutes a checker whose accept predicate combines all four forbidden witnesses: the constant product metadata tuple, first-run product commit id, first-run Direction event commit id and first-run canonical/rendered fingerprint, while recomputing ordinary receipts. The checker must reject at least one isomorphic twin and therefore fail bootstrap; accepting all twins by deleting any witness is separately caught by the corresponding single-witness substitution. Every malicious checker must fail bootstrap. The same semantic specimen across all sixteen cells must produce identical verdicts; hashes change, meaning does not.

`mutation-digest=H(F("mutation", exact fully expanded typed operation bytes))`; it contains no label/expected value. Writer persists exactly the `F("case", ...)` row defined in dependency item 7 for every expanded case. Receipt construction follows the explicit bootstrap/final/binding order above. Expected exits, labels, canonical unsalted fingerprints, mutation DSL and git-node purpose never enter checker input.

END_OF_FILE: os/engineering/V21-CONFORMANCE.md
