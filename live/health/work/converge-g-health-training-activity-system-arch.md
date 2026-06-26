# Converge-arch — g-health-training-activity-system
# Declare + Decompose + Architect; assembly surface, removable; not a state file

> Produced by converge-arch play, session s-health-training-activity-converge-arch-001
> (2026-06-26). Authority is the owner-signed WHAT in
> work/converge-g-health-training-activity-system.md plus this RESULT history, never
> this file alone. Architecture picks ride later PLAN as context-only input evidence
> and must not be copied into done_when.

## §SCOPE & IMPORTS

Signed WHAT imported unchanged:
- G-TA-1..G-TA-9.
- W1-W20.
- Define signoff: "ок согласен".
- Resolve signoff: "Да, согласен с пакетом B" plus transient-screenshot amendment.

Kernel/core imports:
- g-health-core data layer CA1-CA9.
- g-health-core kernel KC1-KC14 and WA-K1-K12.
- health-ai @8246cec current-head WA-K10 GREEN.
- D-kernel-1 already housed in registry grammar as control-plane decide-and-inform.
- nutrition is an ACTIVE thin sibling with DAY_LOOP continuity.

Owner gate posture:
- owner_gate_batch = [].
- No genuine new owner fork remains. Each pick below is forced by the already
  signed WHAT/kernel rows or by the owner's screenshot/setup amendments.
- If converge-verify refutes this, route to repair/converge-arch correction before
  shape.

## §DECOMPOSE (Step 2)

### Sub-systems

1. Domain attach and bootstrap over the kernel.
2. Training/activity authority: program, progression/regression rules, safety bounds,
   activity options, and session prescriptions.
3. Session brief / "training today" projection.
4. Guided run / live operational route.
5. Specialist import/extraction route.
6. Normalized session LOG family.
7. Safety brake + reduced/bad-week mode.
8. Training review decision.
9. Training mutation path.
10. Routine nutrition demand carrier.
11. Review-level training<->nutrition handoff.
12. Direction OS strategic boundary.
13. WA-K8 second-domain proof surface.

### Internal seams (WHAT side; HOW → PLAN)

- **S1 core attach ↔ training authority.** Training authority exists only as a
  thin-domain instance over the kernel; no router/lifecycle/gate/job model is
  copied into training.
- **S2 authority ↔ session brief.** The brief is a readable projection of ACTIVE
  authority and current core state, never a silent program rewrite.
- **S3 brief/guided/import ↔ normalized LOG.** Three input routes converge on the
  same review-ready LOG meaning, with missing data recorded as confidence gaps.
- **S4 guided checkpoint ↔ job handoff.** A recoverable checkpoint is a job boundary
  in the same LOG family; unconfirmed in-chat micro-progress is not durable state.
- **S5 LOG ↔ review.** Review consumes normalized results, core metrics, feedback,
  safety/recovery signals, and friction; it emits one bounded decision class.
- **S6 review ↔ mutation.** Mutation changes or preserves one named training artifact
  through the kernel gate layer; review is not a free-form summary.
- **S7 safety/reduced mode cross-cut.** Safety brake and bad-week mode constrain
  brief, guided run, import acceptance, review, and mutation.
- **S8 specialist raw ↔ extraction confirmation.** Native records stay native;
  only owner-confirmed structured extraction enters normalized LOG.
- **S9 training demand ↔ nutrition.** Daily coarse demand and review-level handoff
  pass through core-owned surfaces; no direct module-file dependency.
- **S10 Direction OS ↔ Health AI visibility.** Direction OS reads when needed but
  does not persist raw logs/media; Health AI has no Direction OS dependency.
- **S11 WA-K8 verifier ↔ topology.** Training removal and procedure disablement are
  verifier-visible topology properties, not domain business behavior.

### Sub-node decision

**No sub-node is required before verify/shape.**

Rationale:
- Splitting strength, activity, guided run, import, review, or nutrition handoff
  into separate TREE nodes would create false separate authority surfaces. They
  are one training/activity domain over the same core program/review/log loop.
- The heavy seams are internal contracts and later PLAN agenda, not separate life
  outcomes.
- Shape may still cut a small executable bet, and may preserve a later body-execution
  CALL, but that is bet/task slicing, not a required TREE sub-node.
- If converge-verify finds that WA-K8, guided durability, or nutrition handoff cannot
  be refuted inside one node, then repair can return a named split/blocker before
  shape.

## §ARCHITECT (Step 3)

Architecture-on-paper only. All concrete schema, path, literal field names, vendor
adapters, parser mechanics, confidence tokens, test fixtures, and threshold values
remain →PLAN.

### A1 — guided-session durability versus save-at-job-boundary and one-chat-one-job

Question:
How can owner-confirmed guided-session progress survive interruption without
committing every repetition and without violating the kernel job contract?

Options:
- **A1-O1 provider-memory live chat, one final save.**
  - good: lowest friction while the chat survives.
  - refuted: provider memory/thread continuity is explicitly not durable; W14 says
    provider memory alone cannot satisfy guided-session interruption durability.
- **A1-O2 commit every set/repetition.**
  - good: maximal durability.
  - refuted: violates save-at-job-boundary, creates tracking bureaucracy, and turns
    training into a raw diary; directly fights the owner/raw-data boundary.
- **A1-O3 commit only the completed full workout.**
  - good: clean one-save model.
  - refuted: if the chat dies mid-session, all completed confirmed work before final
    close is lost or must be re-narrated; fails W14's recoverability requirement.
- **A1-O4 checkpoint-as-job-boundary in the same LOG family.**
  - good: owner-confirmed completed effort blocks can be saved as bounded LOG jobs;
    the next card resumes from committed handoff/cursor; no repetition-level saves;
    no program rewrite; no raw diary in Direction OS.
  - bad, because: more operational ceremony than a purely live coach.
  - pick: **A1-O4**.

Pick:
A guided training "session" is implemented as a chainable same-family LOG route:
a bounded effort block may close as a DAY_LOOP/logging job, write a recoverable
normalized partial/complete LOG + handoff, then the next guided card continues.
The job boundary is the checkpoint, not every repetition. A full workout can chain
bounded jobs; unconfirmed current-block work is not treated as durable.

Compatibility proof:
- one-chat-one-job holds because each durable checkpoint is one bounded job;
- save-at-job-boundary holds because persistence happens only at checkpoint/job close;
- DAY_LOOP same-state logging exception holds because repeated guided logging remains
  in one LOG family;
- WA-K11 holds because continuation is file-backed, not provider memory;
- W14 holds because completed confirmed checkpoints are recoverable enough after
  interruption.

owner_gate:
none. This pick is forced by W12/W14 plus the kernel job/handoff/cursor contracts.

### A2 — placement of session brief, guided run, normalized LOG, review, and mutation

Question:
Where do the training operational surfaces fit in the existing kernel job/state/
artifact model without creating a second engine?

Options:
- **A2-O1 custom training engine and custom job enum.**
  - good: domain-tailored.
  - refuted: violates WA-K1/WA-K7/WA-K9 and W1; training may not stand up a second
    router, lifecycle, gate, writer barrier, scheduler, or job model.
- **A2-O2 specialist tool owns program, log, review, and mutation.**
  - good: low Health AI implementation burden.
  - refuted: violates W2/W15; Health AI must own program/safety/review/normalized
    result while tools keep native raw records only.
- **A2-O3 one monolithic training artifact/job.**
  - good: simple to describe.
  - refuted: conflates authority, projection, logging, review, and mutation; violates
    the one-family/non-logging job boundary and makes review unable to mutate one
    bounded artifact.
- **A2-O4 existing kernel mapping with domain-owned artifact families.**
  - good: reuses the kernel: authored authority sits under existing authoring job
    types; session brief/guided/import/logging sit in DAY_LOOP same-family LOG route;
    REVIEW emits one decision; MUTATION applies one bounded change.
  - bad, because: requires precise domain state-machine declarations at PLAN.
  - pick: **A2-O4**.

Pick:
Training uses the closed kernel job model:
- PROGRAM / CYCLE / WEEK_PLAN: owner-approved training authority layers and planning
  segments, as domain data, not new kernel job types.
- DAY_LOOP: session brief projection, guided run, specialist import, and normalized
  session LOG route; the brief itself is derived/readable output, while the LOG is
  the durable result.
- REVIEW: one training review decision.
- MUTATION: one bounded scoped change.
- DEFINITION: training state-machine definition rides the existing kernel gate.

owner_gate:
none. This is forced by W1/W2/W4/W9/W10-W13 plus WA-K7/WA-K9.

### A3 — specialist screenshot/export extraction, confirmation, provenance, confidence, and media disposal

Question:
How should Health AI consume screenshots/exports/native tool results without saving
raw media or silently trusting extraction?

Options:
- **A3-O1 save screenshot/export as durable evidence.**
  - good: auditable raw source.
  - refuted: owner explicitly amended that screenshots should not be saved; raw
    specialist records should stay native, not become Direction OS/Health AI raw
    mirrors.
- **A3-O2 silent extraction to normalized LOG.**
  - good: low friction.
  - refuted: violates W11; no extracted value becomes trusted durable session data
    before the owner has a clear chance to verify or correct it.
- **A3-O3 API/direct-integration only.**
  - good: cleaner structured data when available.
  - refuted: violates W15 fallback; process must remain usable without vendor API
    and without tool-vendor lock-in.
- **A3-O4 transient extraction proposal → owner correction/confirmation → normalized result only.**
  - good: matches owner amendment, preserves raw boundary, stores source/confidence,
    and asks only follow-ups that improve review value.
  - bad, because: needs careful UX to avoid turning import into a questionnaire.
  - pick: **A3-O4**.

Pick:
A specialist import is a confirmation gate around an extraction proposal. Health AI
reads the supplied screenshot/export/text/voice as transient input, displays a
readable extracted candidate result, asks only materially useful follow-ups, accepts
correction/confirmation, then persists only the normalized structured result with
source/provenance/confidence and safety/review flags. Screenshot/media/raw exports
are disposed or left in the native tool; Direction OS stores none.

owner_gate:
none new. The owner already signed the Resolve amendment that screenshots are
transient and extraction must be shown for confirmation/correction.

### A4 — routine training-demand plus review-level training<->nutrition handoff

Question:
How do training and nutrition coordinate calories/protein/recovery without direct
module-file dependency or authority leakage?

Options:
- **A4-O1 training writes nutrition targets/artifacts.**
  - good: immediate response to volume.
  - refuted: violates nutrition authority; training must not edit calorie, protein,
    menu, recipe, or food-plan artifacts.
- **A4-O2 nutrition reads raw training logs/telemetry/training files.**
  - good: richer context.
  - refuted: violates no-direct-module-file dependency and raw-data minimization.
- **A4-O3 no training<->nutrition coupling.**
  - good: maximum isolation.
  - refuted: fails TREE/WHAT body-composition requirement; nutrition must respond
    to training demand and recovery patterns.
- **A4-O4 core-mediated two-layer contract.**
  - good: routine daily coupling stays coarse; review-level escalation is bounded;
    each domain retains authority; no raw/direct file dependency.
  - bad, because: requires precise review-handoff wording and confidence handling
    at PLAN.
  - pick: **A4-O4**.

Pick:
Use two layers:
1. Routine: a coarse dated training-demand carrier through the core-owned shared
   surface. Actual execution supersedes planned execution when present. Nutrition
   consumes the coarse demand when resolving its own targets.
2. Review-level: training review can emit a bounded nutrition-review handoff for
   sustained volume, deload/phase, strength decline, recovery, hunger/energy, or
   adherence concerns; nutrition can return a bounded decision summary through the
   core review surface.

Neither domain reads or writes the other's internals. Nutrition remains sole owner
of calories/protein/menu/recipe/food-plan changes. Training may only consume the
returned bounded decision as review context.

owner_gate:
none. This imports core CA5 and the signed W16/G-TA-9 reading.

### A5 — strongest WA-K8 two-live-domain removal and one-procedure-disable proof

Question:
What proof topology demonstrates anti-fragility at the first true two-domain moment?

Options:
- **A5-O1 structural proof with only one live domain.**
  - good: already partly available from kernel/nutrition.
  - refuted: insufficient for this node; W19 requires the second-domain strongest
    form with nutrition and training both attached.
- **A5-O2 remove training but allow compensating core/nutrition edits.**
  - good: can make the system pass after repair.
  - refuted: violates WA-K8; removal must not require persistent compensating edits.
- **A5-O3 disable a training procedure by editing router/kernel behavior.**
  - good: superficially targeted.
  - refuted: violates WA-K9 and the single-router invariant; procedure disablement
    must be data/procedure-scope, not engine surgery.
- **A5-O4 live-nutrition + attached-training topology attack.**
  - good: directly tests the required blast radius: remove training domain
    attachment/namespaced content and verify kernel+nutrition; disable/supersede
    one training procedure and verify sibling training procedures.
  - bad, because: cannot fully execute until training exists.
  - pick: **A5-O4**.

Pick:
Converge-verify attacks the proof shape now; product review later executes it:
- precondition: nutrition remains live in DAY_LOOP and training is attached as the
  second thin domain;
- removal proof: remove the training domain attachment and all training-namespaced
  content; kernel and nutrition must still be green, with no dangling reference and
  no compensating core/nutrition rewrite;
- procedure proof: disable or supersede one non-foundational training procedure,
  preferably the guided-run procedure because it is high-risk and has siblings;
  session brief/import/review/mutation siblings must remain routable/green;
- failure mode: any core/nutrition patch, training semantics embedded outside the
  training namespace, or router break is a WA-K8 failure.

owner_gate:
none. WA-K8 is already signed as binding; this is the strongest topology required
by W19.

### Gap-hunt: which architecture question did we not ask?

Candidates considered:
- **Concurrent guided sessions / duplicate same-cursor writes.**
  Disposition: not a new high-risk architecture fork. The kernel handoff token,
  cursor reload, and git conflict/re-resolve model already own same-cursor
  contention. PLAN should add a one-line guard for "one active guided run per
  training cursor unless explicitly resumed/re-resolved".
- **Medical red-flag escalation architecture.**
  Disposition: not a new architecture fork. W7 and the core safety floor already
  force halt/conservative branch/non-diagnostic medical-check language; concrete
  red-flag wording/thresholds stay →PLAN.
- **Direct wearable recovery metrics.**
  Disposition: out of current architecture risk line. Specialist tools are optional
  producers and confidence-marked sources; objective recovery scope remains a
  future evidence/PLAN question, not a blocker to this converge-arch.

Result:
arch_open = 0.

## §KP / PLAN ROUTING

- Training namespace, artifact-family names, state labels, procedure terms, registry
  entry shape → PLAN.
- Concrete program design, exercise selection, volume, intensity, progression,
  conditioning, deload thresholds → PLAN.
- Session-brief schema and rendering order → PLAN.
- Normalized LOG schema, provenance/confidence tokens, review-ready summaries → PLAN.
- Screenshot/export parsing implementation and temporary-media handling mechanics → PLAN.
- Direct API/import adapters and vendor mapping → PLAN.
- Guided checkpoint granularity, copy/save UX, and concurrency guard → PLAN.
- Review cadence/thresholds/baseline method → PLAN.
- Safety threshold magnitudes and escalation wording → PLAN.
- Training-demand labels and review-handoff payload details → PLAN.
- WA-K8 fixture/check mechanics and exact disabled-procedure fixture → PLAN.
- First setup acceptance script and later real-body execution protocol → PLAN.

## §FIREWALL & COVERAGE

- No architecture pick is copied into done_when.
- No workout/exercise/volume/intensity/tool-vendor magnitude is frozen.
- No screenshot, raw workout, route, pulse, wearable record, or daily session LOG
  is stored in Direction OS.
- D-kernel-1 is imported from current registry grammar; no contradiction found.
- contract_coverage: complete via TA-CA1..TA-CA12.
- arch_open: 0.
- arch_in_context_only: PASS.

## §SIGNOFF — converge-arch (Declare + Architect)

status: CLOSED, no new owner decision.
owner_gate_batch: []

Signoff evidence carried:
- Define: owner approved "ок согласен".
- Resolve: owner approved "Да, согласен с пакетом B".
- Screenshot amendment: screenshots are transient, extraction is shown for
  owner correction/confirmation, material follow-ups allowed, only the structured
  normalized result persists.
- D-kernel-1: owner had already accepted option A, and health-ai @8246cec now houses
  it as control-plane decide-and-inform.

Rationale for no new gate:
- A1 is forced by W12/W14 plus the kernel job/handoff/cursor contracts.
- A2 is forced by W1/W2/W10-W13 plus WA-K7/WA-K9.
- A3 is forced by the signed screenshot amendment W11/W15.
- A4 is forced by W16/G-TA-9 plus imported core CA5.
- A5 is forced by W19/WA-K8.
- No value preference remains for the owner; remaining choices are PLAN/HOW.

## §ROUTE

next → converge-verify, not shape or executor.

END_OF_FILE: live/health/work/converge-g-health-training-activity-system-arch.md
