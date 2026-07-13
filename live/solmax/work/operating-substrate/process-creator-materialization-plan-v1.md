# Process Creator materialization plan v1

status: owner-approved
approved_at: 2026-07-13
owner_words: "Approve plan v1"
direction: solmax
node/task: g-operating-substrate-first-process-creator/t-2
product_repo: github.com/ainazemtsau/solmax-operating-substrate
product_base: 34f76d340fb879b5ed2e1ae82bedda258024a623

## Outcome

Materialize one complete Process Creator candidate as the first concrete
process pack. It accepts ordinary owner intent, discovers the concrete process
structure without a universal template, produces a complete candidate pack,
and defines validation, admission, activation, first-live-proof, correction,
readmission and fresh-resume behavior.

The normal owner-facing surface returns exactly one useful result, bounded
question/decision with its blocking reason, clear block with owner/recovery
route, or portable continuation. Internal procedure names, responsibility
classes, lifecycle machinery and state planes stay inspectable but hidden by
default.

`Evidence-to-Decision` from the t-1 walkthrough is a full structural fixture
inside Process Creator verification. It is not a second installed pack and is
not admitted, activated or live-proven by this change.

## Approved bootstrap layout

The chosen layout is local implementation HOW, not a universal pack manifest,
schema, field catalogue or service-block list. No YAML manifest is introduced.

```text
packs/process-creator/
├── README.md
├── contract.md
├── policy.md
├── routing.md
├── procedures/
│   ├── 01-intake-and-frame.md
│   ├── 02-discover-and-classify.md
│   ├── 03-compose-candidate.md
│   ├── 04-validate-and-admit.md
│   ├── 05-activate-via-validated-apply.md
│   ├── 06-run-first-live-proof.md
│   ├── 07-correct-and-readmit.md
│   └── 08-resume-from-continuation.md
└── verification/
    ├── scope-coverage.md
    ├── scenarios.md
    └── evidence-to-decision-fixture.md
```

- `README.md`: candidate identity/status, entry point, governing sources,
  file map and explicit carrier/layout/repository/adapters-as-HOW boundary.
- `contract.md`: objective, applicability, boundaries, local vocabulary,
  owner-facing interaction contract and success/stop/failure/result meanings.
- `policy.md`: state/context/source/memory/history/evidence/artifact/result/
  continuation distinctions; ownership; authority/effect/safety; writer;
  capabilities, degraded routes and compatibility.
- `routing.md`: process-owned procedure catalogue and local dispositions for
  applicable work, clarification, missing input, conflict, no-route, missing
  capability, process gap, effect request and compatibility conflict.
- `procedures/*.md`: actual first-class procedure definitions. Each establishes
  scope, accepted basis, owners, authority/effects, capabilities, behavior,
  legitimate closure and continuation.
- `verification/scope-coverage.md`: default-FAIL mapping of every t-2 and
  scope-contract promise to procedure, validation or proof behavior.
- `verification/scenarios.md`: positive, adverse, apply-uncertainty,
  correction, fresh-resume, anti-bureaucracy and live-proof scenarios.
- `verification/evidence-to-decision-fixture.md`: the complete t-1 semantic
  outline, explicitly candidate-only and structural-only evidence.

Every pack Markdown file ends with its own `END_OF_FILE` trailer.

## Creator procedure flow

1. Intake and frame ordinary owner intent; establish objective,
   applicability, boundaries and one integration owner.
2. Discover the concrete structure and split/classify material atomic claims
   among kernel, reusable-service, process-pack, owner-profile and adapter
   concerns, with one primary normative owner per claim.
3. Compose the candidate's local vocabulary, procedures, routing,
   information, authority, writer, capability, result and continuation rules.
4. Validate Q1-Q7 conformance, capability sufficiency, ownership, authority,
   effects and active-work compatibility; issue admission and impact
   dispositions without treating validation as authorization or activation.
5. Re-read the accepted basis and activate only the admitted, bounded and
   authorized candidate through validated apply. Only the authoritative apply
   result establishes the effective definition.
6. Run one owner-originated obligation through the activated pack and return
   an owner-facing closure without exposing lifecycle bureaucracy.
7. Preserve defect lineage, create a corrected candidate and rerun validation,
   admission and apply; no hidden hot-fix or silent overwrite.
8. Resume from portable continuation in a fresh run after checking definition,
   ownership, authority, effect certainty, references and compatibility.

## Mandatory scope coverage

| # | Mandatory function | Materialization and check |
|---|---|---|
| 1 | Owner-facing intake | `contract.md` + procedure 01; ordinary-language scenario, no manifest questions. |
| 2 | Bounded clarification and material-decision routing | `routing.md` + procedure 01; one question says why it matters and what it blocks. |
| 3 | Objective, applicability and boundaries | `contract.md` + procedure 01; positive and not-applicable cases. |
| 4 | Structure discovery without universal template | procedure 02; fixed-block-list refutation and fixture derivation from intent. |
| 5 | Atomic five-way classification | `policy.md` + procedure 02; mixed claims split, one primary normative owner each. |
| 6 | Process-owned procedure catalogue and routing | `routing.md` + all procedure files; each route has disposition, owner and closure. |
| 7 | State/context/source/memory/history/evidence/artifact/result distinctions | `policy.md`; non-collapse cases, artifact existence is not result/state. |
| 8 | Authority/effect/escalation/safety | `policy.md` + `routing.md`; capability is not authority, effect and insufficient-authority adverse cases. |
| 9 | Writer procedure or policy | `policy.md` + procedure 05; propose/validate/authorize/apply stay distinct and accepted basis is fresh. |
| 10 | Mandatory and optional capabilities | `policy.md`; each has owner, failure meaning and applicability. |
| 11 | Explicit legitimate degraded routes | `policy.md` + scenarios; optional loss uses declared route, mandatory loss blocks. |
| 12 | Candidate conformance validation | procedure 04 + coverage ledger; Q1-Q7 and `REVIEW.md` 1-10 with file/section evidence. |
| 13 | Admission and impact disposition | procedure 04; affected scope/work/owners/authority/effects are explicit. |
| 14 | Authoritative activation | procedure 05; invalid never activates; applied/failed/partial/unknown remain distinct. |
| 15 | First owner-facing live execution | procedure 06 defines the proof contract; real evidence remains t-4/t-6. |
| 16 | Relevant adverse path | `routing.md` + scenarios: missing criterion, no route, missing capability, kernel override and unknown apply. |
| 17 | Portable continuation and fresh resume | `policy.md` + procedure 08; fresh run resumes or names the exact block/owner. |
| 18 | Bounded correction and readmission | procedure 07; lineage preserved, full revalidation/readmission, no silent overwrite. |
| 19 | Structural/usefulness/reuse separation | verification files carry separate structural, useful-live and reuse verdicts; reuse stays `NOT_YET_PROVEN`. |

Every bullet of `t-2.done_when` also has its own coverage row. Missing mapping or
evidence leaves the ledger FAIL.

## Evidence-to-Decision fixture obligations

The fixture preserves the complete accepted t-1 outline: objective,
applicability, boundaries, vocabulary, P1-P8 procedures, routes A-I,
criterion/source/evidence policy, information distinctions, comparison and
recommendation, read-only authority, writer policy, capabilities/degraded
routes, success/failure/recovery, continuation/compatibility, the missing
data-residency-criterion adverse path, proof scenarios and K/RS/PP/OP/AI atomic
ownership decomposition.

The fixture proves only structural expressiveness of the Creator candidate.

## Supporting engineering artifacts

The fresh BUILD session also creates the minimum repo-native declarations:

- `openspec/changes/process-creator-v1/`: approved proposal, tasks and
  acceptance/coverage specification;
- `docs/adr/ADR-0002-process-creator-materialization.md`: change class,
  owner-facing behavior, layout-as-HOW and no-manifest decision;
- `docs/results/process-creator-v1-self-check.md`: author self-conformance;
- root `RESULT.md`: candidate build handback, explicitly not admitted,
  activated or live-proven;
- `tools/check.py`: declaration-list-only addition of the exact pack paths and
  EOF paths to the existing wiring smoke. No new parser, regex, semantic scan
  or behavior oracle. Existing `tools/selfcheck.py` covers required-file misses.

BUILD does not author `docs/reviews/review-process-creator-v1.md`; the binding
fresh t-3/G5 review session owns that artifact.

## Verification and handoff

The BUILD author records file/section evidence for every coverage row and runs
the semantic scenarios. Mechanical validation is local only:

```text
python tools/check.py
python tools/selfcheck.py
python tools/check.py --deliver
```

There is no CI. The candidate change set returns with exact commit/diff/check
evidence and stops before admission, activation or live-use claims. A fresh t-3
session attempts to refute it against Q1-Q7, all scope rows, `REVIEW.md` and the
anti-bureaucracy property.

## Cuts and non-cuts

No mandatory bounded function is cut.

Outside this BUILD: a second installed process pack; actual t-4/t-6/t-7 live
evidence; kernel/services/adapters content; universal manifest/schema/entity
model/lifecycle enum/service-block list; application/dashboard/scheduler/queue/
agent mesh/automatic transport; CI; semantic Python/compiler/regex/parser;
mutation/negative-control/property-layer/code gates; provider semantics;
Q8-Q12 freeze; irreversible high-risk effect; and any claim that structural
completeness equals useful live behavior.

END_OF_FILE: live/solmax/work/operating-substrate/process-creator-materialization-plan-v1.md
