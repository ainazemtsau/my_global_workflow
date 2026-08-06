# Life-reset — Implementation Research v1 (HOW to build the strict self-improving manager)

Date: 2026-06-21
Session: s-life-reset-research-build-manager-001 (play: research)
CALL: c-life-reset-research-build-manager-001 (node g-life-reset-root)
Status: durable research PRODUCT — evidence + 2-3 options + a recommendation for each of
the 10 deferred mechanisms. NOT decisions (owner decides at shape). NOT a tree change.
The 6-node outcome tree (run/protect/integrate/learn/trust/grow) is the WHAT and is
untouched; this is the HOW that equips the following shape leg.

Method: one research pass, multi-agent per the parallel-verify discipline (workflow
wf_41aaf9c5-c4c, 23 agents). 10 evidence+options generators (one per mechanism,
web-grounded), each recommendation then adversarially REFUTED in a separate pass against
the charter guardrails, then 3 cross-cutting critics (whole-set guardrail audit,
coherence/thin-slice, completeness). Every one of the 10 recommendations returned
`holds_with_fix` — none was refuted, none survived clean. The adversarial pass caught
ONE real guardrail violation (Q7, a G3 recovery breach) and 9 anti-paper / scoping /
wording fixes. That is an honest result: the refuters did real work.

Constraints held throughout (an option breaking one was discarded): G1 sealed core +
inviolable override; G2 no false precision (heuristic + named reasons, never a computed
optimum); G3 recovery/rest protected first-class + owner-paced; G4 source boundaries
(summaries, never raw neighbor data); the ONE-REAL-RUN gate (no calendar week, no N
cycles; "architecture exists" never counts); STAYS LIGHT (single mentor voice, cost less
attention than it saves); works through chat, one entity per chat; do NOT re-open the tree.

---

## 0. Headline

- The 10 named mechanisms each have a defensible recommendation, and they COMPOSE into
  ONE coherent tiny v1 slice (coherence critic: `composes: true`). The whole v1 is a
  single composed pulse on real data — NOT a board, a DAG, an engine, or a questionnaire.
- The spine repeatedly chosen: inherit the existing Direction OS substrate (durable
  markdown, CALL/RESULT, owner-approved gates, git history/, the {hold|mutate|kill|route|
  research|simplify} review, ≤1 experiment, one-change-at-a-time) rather than build new
  infrastructure. Almost every heavier rival was DEFERRED as an evidence-earned upgrade.
- One real guardrail violation was found and patched (Q7 — the hollow-week veto would
  condemn a genuine recovery week = the burnout loop G3 forbids → a recovery carve-out is
  now a MUST-FIX before shipping).
- The completeness critic surfaced a real coverage gap the CALL's 10 topics did not
  include — most importantly **g-lr-integrate** (the summary-contract + conflict-routing)
  and the **recovery-vs-slide** distinction (the line between protected recovery and
  rationalized zone-out), which several recommendations silently depend on. Surfaced, not
  silently expanded (§4). This is the main thing for the owner to weigh before shape.

---

## 1. Per-mechanism findings (Q1–Q10)

Format: strongest evidence · the 2-3 options · the recommendation · the required-fix the
refuter extracted. Full evidence/sources live in the workflow transcript; key sources §7.

### Q1 — Week-graph node/edge form + day-derivation  (g-lr-run)
- Evidence: order-of-placement IS the mechanism (Covey "big rocks first" — wishes only
  fill the gaps floors leave); time-blocking/timeboxing beats an unstructured list but the
  "~30%/2×" figures are vendor-amplified heuristics (so derive the day by a named rule, not
  a claimed optimum); Kanban WIP-limit grounds "≤1 experiment", explicit-policy grounds
  "cuts must be written, not silently dropped"; MIT (Most-Important-Task) is the verified
  "pull the day down from the week, don't re-plan" pattern; GTD/PARA's documented limit
  ("tells you what EXISTS, not what MATTERS") is the wish-list failure the strict order
  prevents; the prior life-reset dry-run already prototyped a week template.
- Options: **A** flat ordered four-layer list (order enforced by file POSITION; lightest);
  **B** typed commitment DAG (real depends-on / displaces / derived-from edges; heaviest,
  bureaucracy risk); **C** Kanban lane-board + a separate week-start compose-gate.
- Recommendation: **A** as the v1 spine + ONE borrowed element from B — a single explicit
  `displaces:` line whenever a wish forces a cut, so displacement is always loud. B/C are
  evidence-gated upgrades the weekly review can mutate toward only if a real week proves
  the flat list cannot hold dependencies.
- Required fix: keep the four layers DISTINCT (## Musts | ## Floors | ## Wishes | ## Cuts —
  don't blend non-negotiable floors into negotiable musts); make the displacement test
  non-vacuous (either require one real cut that IS a displacement, or label the
  `displaces:` line a deferred/untested element this probe doesn't yet validate).

### Q2 — Technique-selection method R32  (g-lr-grow)
- Evidence: techniques fail by person-task FIT not by being "wrong" → "tasks/goals first,
  then technique"; the behaviour-change field selects by DIAGNOSE→mechanism-of-action→
  shortlist (BCT Taxonomy v1, 93 techniques; the Theory & Technique Tool is a ready
  lookup), never by personality quiz; if-then implementation intentions are a near-
  universal cheap win (d≈0.65) to apply before bespoke ones; N-of-1 single-case designs
  test one technique against a baseline with only a handful of data points; personal-
  science minimal-intake principle ("collect only data that changes a decision") bounds the
  intake; it can ride the existing one-change-at-a-time + ≤1-experiment + weekly-review
  machinery.
- Options: **A** diagnose-the-blocker → best-bet lookup (a tiny curated blocker→technique
  table, not the raw 93); **B** run-it-and-measure (default to if-then, let the N-of-1
  swap-loop do the selecting); **C** owner-menu pick + manager runs the stop-rule.
- Recommendation: **A spine + B's evaluate-and-swap loop + C's owner-veto** — they answer
  different questions (how to choose / how to evaluate-and-swap / who holds choice
  authority), share ONE mechanism, add almost no ceremony.
- Required fix: drop the "one-week swap" framing (v1 is met when SELECTION fires once);
  keep the signal owner-reported and an explicitly heuristic best-bet (not a score);
  PAUSE rather than fail a technique on a recovery week (G3).

### Q3 — Balance minimum / routine / wishes / rest R29  (g-lr-run)
- Evidence: four independent reference classes CONVERGE on the same rule — Covey (order),
  training-load science (recovery is a performance INPUT; deny it → overtraining/burnout),
  acute:chronic workload ratio (a SURGE relative to your conditioned baseline is the
  danger — a near-exact analog of the fixation crash loop), WIP/Little's Law (cap the
  surge), energy-management (recovery is a scheduled ritual with its own slot). Willpower
  is depletable → floors+recovery must be STRUCTURAL, not defended in the moment.
- Options: **A** lexicographic jar-fill (strict tier order, no numbers; works cold);
  **B** reserved-partition (carve floors+recovery off the top first); **C** baseline-
  relative surge governor (ACWR-analog; needs history, G2-fragile, cold-start-useless).
- Recommendation: **A as v1 spine + B's one move folded in** (floors AND recovery placed
  together in tier-1, untouchable by the filter), with **C deferred** as the explicit named
  seam for g-lr-protect's "throttle the surge" once a baseline exists. Pure precedence
  heuristic, no formula (G2-clean).
- Required fix: widen tier-1 from "FLOORS + RECOVERY" to **FLOORS + ROUTINE REST +
  RECOVERY** — ordinary rest/slack must be a floor too, or a high-energy jar-fill cuts all
  slack (the over-investment that drives the crash). This gives v1 a real surge-throttle
  (cap the good day, not only floor the bad one — the Graham-Greene-quota logic) BEFORE C.

### Q4 — Safe self-rewrite gate (sealed core + override-survives-rewrite)  (g-lr-learn)
- Evidence: corrigibility CAN be made to survive self-modification, but only STRUCTURALLY
  (Nayebi arXiv 2507.20964 — separate lexicographically-ordered value heads; merging into
  one learned scalar loses the guarantee). CRITICAL LIMIT: proving "no future rewrite ever
  weakens it" is UNDECIDABLE in general (halting reduction) — so "sealed" must mean "every
  ACTUAL rewrite is gate-checked", never "provably unbreakable forever". Constitutional-AI
  treats its constitution as MUTABLE → sealing needs a separate non-amendable layer + an
  amendment gate. Mainstream practice: immutable policy layer (config-as-data) + append-
  only audit log + post-change invariant validators + rollback. The owner's Direction OS
  IS this substrate already (git history/, owner-approved gates, END_OF_FILE, commits).
- Options: **A** layered immutability (sealed core in a file the rewrite can't touch);
  **B** post-rewrite invariant gate (a frozen check-suite re-runs after every rewrite,
  reverts on fail); **C** lexicographic dominance (seal by ORDERING — research-grade,
  undecidable to enforce on an adversarial self-modifier).
- Recommendation: **A+B together**, with C used only as the WORDING inside the sealed core
  (override > recovery/safety/floors > efficiency). Rides the existing OS substrate; the
  self-rewrite is just another gated RESULT touching only the editable layer, with the
  invariant replay as its done_when.
- Required fix: the single v1 self-rewrite MUST be sourced from a REAL saved weekly-review
  conclusion (presupposes g-lr-run already produced one real week/day/review — consistent
  with the run→…→learn order), not a synthetic rewrite. Soften over-claims: "manual
  git-revert" not "auto-reverts"; "a repeatable 2-assertion hand-run smoke check" not
  "makes sealed CHECKABLE" — claim no automation v1 doesn't have (keeps G2 honest).

### Q5 — Collapse-grip detection (inside the override path, NOT auto-surveillance)  (g-lr-protect)
- Evidence: relapse is preceded by detectable covert antecedents (Marlatt — "apparently
  irrelevant decisions", denial) BUT the person in it cannot see them → detect via PRE-named
  upstream signs, not in-the-moment judgment. Self-report is weakest exactly when needed
  (denial co-occurs with disengagement) → can't rest on the owner accurately reporting
  mid-fixation. Ulysses/pre-commitment + implementation-intentions = the validated "owner
  sets triggers while well" form. AA-sponsor reach-in = accountability OUTSIDE willpower
  ("especially when you don't feel like it"). The surveillance line is AUTHORSHIP, not the
  data (Deci/Ryan): owner-authored monitoring is autonomy-supporting; imposed monitoring
  isn't. For THIS owner the upstream sign is structural ("pillars fall" = floors unfilled,
  reviews skipped, week tunneling into one direction) — readable from the rhythm's OWN trace.
- Options: **A** pre-committed observable tripwires (owner authors 2-4 if-then floors while
  well; manager checks only those); **B** sanctioned reach-in on missed self-attestation
  (fire on SILENCE/absence, AA-model); **C** process-trace proxy detection (manager infers
  grip-onset from its own artifacts — most powerful, highest surveillance risk, needs a
  trace to read).
- Recommendation: **A spine + B's absence-trigger bolted on; defer C**. A is purely
  owner-pre-committed (not surveillance); B's silence-trigger plugs A's absence/unreliable-
  narrator hole; C is the later gated mutation once a real trace exists. The tripwire SET +
  reach-in license live in the sealed core (G1) — any move toward C is itself a gated rewrite.
- Required fix: the binding v1 test is a REAL floor lapse on REAL data (drop "or simulate a
  2-day skip"); author the tripwire at the **first-run intake** (mandatory-once, runs first)
  — word it that way, not "g-lr-grow intake", so grow's gated extension work isn't implied
  to precede protect.

### Q6 — Earned / demotable autonomy  (g-lr-learn)
- Evidence: Sheridan/Parasuraman give DISCRETE automation levels incl. "management by
  exception" (act-unless-vetoed) — and Sheridan warned the levels are a design heuristic,
  not an optimizable number (G2). Dietvorst: people abandon an algorithm after ONE error
  and hold it to a higher bar than a human → demotion must be calibrated, not all-or-
  nothing; and giving people a SLIGHT ability to adjust the algorithm dramatically raises
  willingness to keep using it (the demote rung = "supervised", not "off"). Trust-repair:
  a failure drops trust sharply, repairs but rarely to the original level, and an EXPLAINED
  failure is forgiven where a silent one isn't. Corrigibility: autonomy may govern only the
  wish-filter / self-rewrite surface — override+floors sit OUTSIDE the ladder. 3-4 rungs is
  the right grain for a solo chat system.
- Options: **A** stage-gated rung ladder (autonomy = WHICH stage of action: propose →
  act-unless-vetoed → act-and-report; named promote/demote triggers, not a score);
  **B** track-record ledger ("credit" buys a rung — invites the gamified-number G2 trap);
  **C** per-domain trust accounts (separate ladders per life-area — bookkeeping the solo
  owner won't carry).
- Recommendation: **A spine + C's one move** (recovery/floors/override PINNED at the lowest
  rung, outside the ladder; novel self-rewrite classes default to PROPOSE).
- Required fix: do NOT require the DEMOTION to fire inside v1 (hard-code only the one
  promote path + a stated durable demote rule that fires on a real natural overturn, never
  staged — staging it breaks the anti-paper floor); make the R2 "act-unless-vetoed"
  self-rewrite class owner-gated with a real veto window, and state that an R2 rewrite STILL
  passes through Q4's post-rewrite invariant replay (no "earned" rung bypasses the gate).

### Q7 — Hollow-week / aliveness measure  (g-lr-learn)
- Evidence: "subjective vitality" is a validated construct (Ryan & Frederick) with a
  validated single-item STATE form for daily-life use — BUT a one-item form is only a
  SCREEN (a depression one-item: 46% sensitivity / 94% specificity → a "fine" answer misses
  ~half of real cases, a "bad" answer is trustworthy). Decisive: a HIGH aliveness number
  must NEVER certify a week a success; a LOW number / red-flag reliably condemns. SDT
  supplies the NAMED reasons (autonomy/competence/relatedness/meaning) so it's defensible-
  by-reasons, not a happiness score. The owner is an unreliable narrator on a high-fixation
  week → a self-rating alone can be gamed; a behavioral tripwire (a fallen protected pillar)
  is the second key.
- Options: **A** self-rated aliveness 1-5 + a qualitative veto (low number OR flat
  "what-mattered" line flips done→not-a-success); **B** behavioral-tripwire veto (a fallen
  protected pillar auto-arms the hollow flag, no self-rating); **C** two-key OR-veto (A or
  B can each independently condemn).
- Recommendation: **ship A** as the tiny slice, built as the subjective half of C so B's
  behavioral key can snap on later by evidence. A is near-zero ceremony; full C is the
  end-state but too heavy/over-firing to prove first.
- Required fix (the ONE real guardrail violation in the set): **add a recovery carve-out**.
  The veto must NOT fire "not-a-success" on a week tagged genuine protected recovery — a low
  aliveness / flat meaning-line on a real-recovery week is EXPECTED and CLEARS as protected,
  not condemned (else the manager becomes the burnout loop G3 forbids, acute on the first
  run which most likely lands in a recovery phase). Keep the 46%/94% statistic as internal
  reasoning only — never surface a numeric threshold (G2).

### Q8 — Ceremony / burden budget (stays light)  (g-lr-grow)
- Evidence: Gawande — a good checklist is SHORT (5-9 killer items), not comprehensive.
  Lean/Kanban — eliminate waste + WIP cap; "becoming smaller" is a first-class goal.
  Firewall "spring cleaning" — prune rules by USAGE over a sustained period (rules that
  never fire are dormant; ~40-50% go unused). Agile retros are time-boxed but a too-tight
  box starves the learning loop → soft cap with override, not a guillotine. A literal
  overhead RATIO (admin/doing time) has no clean meter for a chat-only solo and risks
  false-precision theater (G2). The CHARTER already encodes the kill trigger ("владелец
  называет это бюрократией → формат немедленно упрощается").
- Options: **A** overhead-ratio cap (structurally unsound for chat-only solo; G2 risk);
  **B** hard WIP cap on active rules/programs (arbitrary this early; could force out a
  load-bearing safety rule); **C** usage-driven prune + the owner's one-word "too heavy"
  veto (firewall dormancy + Gawande killer-items).
- Recommendation: **C**, with G1/G3 sealed-core rules hard-EXEMPT ("fire-on-demand, never
  auto-flagged") and a soft review time-box as a secondary signal (not a measured ratio).
- Required fix: probe success must MATCH g-lr-grow done_when(d) — ≥1 actual SHED rule /
  owner-confirmed simplification, not merely "kept or pruned". And "did not fire in this
  ONE run" cannot justify a prune (that's the N-cycle dormancy the gate forbids, on one
  data point) — in v1 the prune authority is the OWNER naming a rule redundant; the
  `last_fired` field accumulates evidence for FUTURE (many-run) auto-pruning only.

### Q9 — Non-punitive re-plan + non-punishing re-entry  (g-lr-trust)
- Evidence: the Abstinence Violation Effect (a single lapse → guilt → "I've failed" →
  full relapse) IS the owner's documented crash loop; the fix is cognitive restructuring —
  attribute the lapse to the SITUATION (a high-risk moment + coping gap), reframe it as
  data/learning, not a moral failing. Self-compassion after a failure predicts MORE
  re-engagement (Breines & Chen) — a non-punishing welcome-back is the higher-adherence
  move, not softness. An unrepaired alliance rupture predicts the client QUITS; a repaired
  one predicts retention (rupture-repair is a learnable protocol). The alliance predicts
  adherence more than technique. Duolingo "streak freeze" (a missed day doesn't zero the
  state) cut churn ~21% — the pattern: durable running-state persists across a gap; the gap
  is absorbed, not scored. Re-plan (a) and re-entry (b) are ONE restructuring principle at
  two time-scales.
- Options: **1** resume-from-durable-state + delta-only "what changed?" re-entry, lapse
  logged as one situational line; **2** gap-length tiered ladder (false-precision day-
  thresholds, G2); **3** owner-declared re-entry ritual (depends on the owner initiating in
  his worst state).
- Recommendation: **Option 1 base + Option 3's binding** (the non-punishing return is an
  invariant the manager can't argue away), with Option 2 rejected and its one good idea
  (auto-offer recovery on return) folded in via g-lr-protect.
- Required fix: re-cite the hardening as a **sealed-core / gated-self-rewrite INVARIANT**
  (a protected-class rule a rewrite can't weaken), NOT "bound to the owner's override path"
  — the override path is the OWNER's lever over the manager, not a host for manager
  behavior (a category error). Binding trust(b) proof = resume-state + one "what changed?" +
  one neutral situational line + owner confirms non-punishing & takes the next strict call;
  auto-offer-recovery is a g-lr-protect bonus, decoupled from the trust gate.

### Q10 — Realism bar of the one-real-run gate  (g-lr-run / root done_when)
- Evidence: dogfooding only counts on REAL functional use ("watered-down examples" are
  ruled out); ecological validity — an easy/artificial task doesn't generalize to whether
  the rhythm survives a real week; UAT — realness is real data ON A HARD-ENOUGH CASE (the
  filter must bite a wish the owner actually wanted; a no-stakes run validates nothing);
  demo-vs-live (trading) — realness lives in real STAKES, "in the demo, losses don't hurt";
  Agile Definition-of-Done — defeat "looks done" with a short list of VERIFIABLE/DEMONSTRABLE
  artifacts, not a self-feeling. For THIS owner an "easy day" is exactly the day the system
  is NOT under test (the loop only bites on a high-energy fixation day). Restart-survival
  (a fresh chat continues from durable state) is cheap to check and impossible to fake.
- Options: **A** artifact-existence checklist (DoD-style realness card, owner attests);
  **B** stakes/bite test (a real cut hurt / filter bit the owner's own pull / recovery
  protected against temptation); **C** adversarial "try to prove it was a demo" fresh
  session (= the OS's own G5 refutation machinery; heaviest).
- Recommendation: **A spine + B folded as exactly ONE mandatory bite-slot** (satisfiable
  three ways incl. recovery-protected, so a calm real week still passes — G3); **C reserved**
  as the first later hardening if self-attestation proves too soft.
- Required fix: demote the exact 5-slot list from a frozen gate to an ILLUSTRATIVE shape
  input (the precise slot set is sized at shape, so research doesn't pre-decide the gate);
  the realism BAR proper = the anti-paper artifact-existence rule + the one bite event
  (two of the five slots merely restate existing done_when criteria 2 & 4). Record that the
  gate ultimately rests on owner self-attestation, with the deferred C as the named,
  conditional hardening.

---

## 2. Cross-cutting — guardrail audit (whole set)

All 8 guardrails PASS set-wide — but several PASS only **with the required-fixes applied**
(that is the binding state):
- **G1** (sealed core + override): coherent across Q4/Q5/Q6/Q9 — override+floors always
  outside what the rewrite/ladder can touch; no recommendation lets the manager silently
  weaken override.
- **G2** (no false precision): every weighing rule is ordering/precedence/named-reason; the
  only numeric option (Q3-C governor) is explicitly deferred for being G2-fragile; Q7's
  46%/94% quarantined as internal reasoning.
- **G3** (recovery protected): holds ONLY with Q7's recovery carve-out + Q3's rest-axis fix
  applied — without them Q7 self-flagged a real violation.
- **G4** (summaries not raw): largely out of scope for these 10 (it bites at g-lr-integrate,
  unaddressed); nothing ingests raw neighbor data.
- **One-real-run**: holds only because the fixes scrub residual N-cycle/paper leaks
  (Q2 one-week-swap, Q5 "simulate", Q8 one-run dormancy, Q4 synthetic rewrite, Q10 frozen card).
- **Stays-light / tree-not-reopened / works-via-chat**: pass.

Three cross-question dependencies shape MUST reconcile:
1. **Q1 vs Q3 header schema** — both prescribe the same single week-compose file with
   slightly different headers → merge to ONE layout (below).
2. **Q4 vs Q9 hosting** — Q9 must host its non-punishing-return invariant in the sealed
   core (Q4's machinery), NOT on the override path.
3. **Q4 vs Q6 gating altitude** — an "earned" R2 act-unless-vetoed rewrite still triggers
   Q4's post-rewrite invariant replay; state it so the rung can't appear to bypass the gate.

---

## 3. Cross-cutting — coherence + the recommended v1 thin slice  (`composes: true`)

ONE composed pulse, on REAL owner data, in ONE durable markdown surface a chat can hold:

- **A. Compose the week** — one file, four sections in FIXED file-position order (position
  = the "big rocks first" enforcement): **(1) PROTECTED TIER-1** [Musts + Floors +
  Routine-rest + Recovery — rest+recovery off the top, uncuttable, the G3 class] →
  **(2) Routine** → **(3) Wishes-through-filter** [each admitted-with-reason OR
  rejected-to-backlog-with-reason; mark the ≤1 experiment] → **(4) Cuts** [explicit; a
  `displaces:` line when a cut is a displacement]. Pass: floors+recovery+rest before any
  wish; filter bit ≥1; ≥1 explicit cut. Two streams present from neighbor SUMMARIES (not
  raw), topped up by owner if thin (G4).
- **B. Derive one day** — a short timeboxed top-down pull (named MIT-style heuristic, not an
  optimizer), R11 gate firing once at the head ("yesterday's review done? else fill or
  explicitly refuse"; refusal always available). Pass: ≥1 real day, R11 fired ≥1.
- **C. Author the sealed-core file ONCE** (serves Q4/Q5/Q9, not three files): override path
  (incl. R11 refusal) + recovery/safety/floors protected class + manual rollback +
  "rule-changes only via the gate" + ONE owner-authored collapse-grip tripwire + the
  non-punishing-return invariant.
- **D. Protect fires once for real** — the manager throttles a real surge / names a falling
  pillar before a crash and holds the protected class, OR the pre-authored tripwire fires on
  a REAL lapse on REAL data (no paper simulation); the filter passes genuine recovery if
  needed; recovery reads as a protected STATE.
- **E. One real review → one decision** — a saved review, default visibly {hold}, yielding
  ≥1 decision from {hold|mutate|kill|route|research|simplify}; the hollow-veto runs WITH the
  recovery carve-out; a low aliveness signal raises a flag for the owner to weigh, no number
  surfaced.
- **F. Durable + portable** — week/day/review/decision + sealed-core survive a chat restart;
  a fresh chat/provider resumes the LIVE running state (cycle position, current protections,
  autonomy rung) via delta-only re-entry ("what changed?"), no full re-intake.
- **G. Owner attests** — the run was REAL and actually worked (not "architecture looks
  right"); one slot = the BITE event (a real cut that gave something up OR the filter biting
  the owner's own pull OR recovery protected against a real temptation); invented value
  voids the slot.

No board, no edge-types beyond one `displaces:` line, no automated gate, no per-domain
accounts, no surge-governor, no adversarial self-cert. Run + one protect episode + one learn
decision + portability, integrate present-minimal, grow excluded.

---

## 4. Cross-cutting — completeness: what the 10 Qs do NOT cover (SURFACED, not expanded)

The CALL named 10 mechanisms; all 10 are answered. A coherent v1 also needs pieces no
question owned. These are flagged here for the owner / shape — NOT silently built, NOT a
tree change:

LOAD-BEARING (a v1 likely can't be honest without these):
- **g-lr-integrate is entirely unaddressed.** Its done_when needs a SUMMARY CONTRACT (what
  shape a neighbor "agreed summary" takes, how life-reset requests/refreshes it without
  storing raw — G4) and CONFLICT-SURFACING-AND-ROUTING. The slice scopes integrate
  "present", but "present" still needs a concrete summary-ingest + top-up + route mechanism.
  Largest hole.
- **Recovery-vs-slide distinction.** The line between protected recovery and rationalized
  zone-out is flagged in the charter as "research", and G3 + Q3 + Q5 + Q7's carve-out ALL
  silently depend on it. Without it the protected class is either gameable ("everything is
  recovery") or punitive. This is personal to the owner → best resolved WITH him.

UNDER-BUILT (named, but a stub):
- Day-derivation (Q1 gave it one line; the charter daily_loop names главное / protected
  floors / DRIFT DETECTION / REBUILD + adaptive support intensity — none designed).
- R11 storage + R12 interaction (where "yesterday's review" lives so a fresh day-chat finds
  it and refuses to start without it).
- Durable-state / provider-portability FORMAT (what fields encode cycle-position + current
  protections + autonomy rung; how a new chat re-hydrates them).
- The self-improvement-fires ANALYTIC step (how a review derives a conclusion-about-the-owner
  worth a rewrite — the {hold} vs {research/mutate} fork, the "find the weak link" step).
- The {hold|mutate|kill|route|research|simplify} verdict procedure itself (how day-reviews
  aggregate into the weekly one; how the verdict is chosen).
- Backlog lifecycle (inbox→candidate→selected→done/dropped) and the process-extension
  definition gate (g-lr-grow done_when b/c) — grow is excluded from v1, so deferrable.
- The non-caving WEIGHING POLICY ("что считать достаточным доводом") — the core of the
  manager's strictness; charter-flagged "research", still unspecified.

Top uncertainties only a real run resolves: will a flat four-layer file hold real
integrate-streams + day-derivation + drift, or collapse on week 1? Can the manager
distinguish recovery from slide? Do owner-authored tripwires actually fire on the
unreliable-narrator week? Is "sealed core survives rewrite" real or two hand-checked
assertions? Does the gate resist a cherry-picked day given it rests on owner self-attestation?

---

## 5. Recommended next — shape CALL on g-lr-run (bundle)

Shape on g-lr-run, sizing the v1 thin slice (§3) as ONE coherent compose-pulse deliverable.
The shape CALL should: scope the slice across run + one protect episode + one learn decision
+ trust-portability, integrate present-minimal, grow excluded (intake + ≤1 technique-pick
ride inside g-lr-run's first compose); reconcile the ONE header layout (§3.A); size ONE
shared sealed-core file (§3.C); author the realness card as the acceptance frame with the
5-slot list illustrative (binding bar = anti-paper artifact-existence + one bite-slot);
apply EVERY required-fix from §1 as done_when conditions; preserve all invariants in the
boundaries (one-real-run, G1-G4, stays-light); and explicitly DECIDE with the owner how to
handle the two load-bearing gaps (§4 — recovery-vs-slide distinction; integrate summary-
contract): resolve-inside-shape vs a tiny pre-shape probe. Recommendation only — the owner
picks the slice at shape; the riskiest-assumption task (G6) should test the recovery-vs-slide
line and whether the tripwire fires on a real lapse.

---

## 6. Deferred-upgrade backlog (evidence-earned; for g-lr-grow / later — named, NOT built)

- Q1: full typed-commitment DAG / Kanban lane-board (if the flat list can't hold deps).
- Q2: the explicit N-of-1 evaluate-and-swap loop (layers after selection fires once).
- Q3: the baseline-relative surge governor (ACWR-analog) — the g-lr-protect upgrade once a
  baseline exists.
- Q4: automated post-rewrite invariant gate with auto-revert (v1 = manual revert + 2 hand
  assertions).
- Q5: process-trace proxy detection (the unreliable-narrator detector) — gated rewrite once a
  real trace exists.
- Q6: track-record ledger / per-domain trust accounts.
- Q7: the two-key (subjective OR behavioral) hollow-veto.
- Q8: the dormancy auto-flag as a BINDING prune basis (only across many real runs); hard WIP
  cap on rules.
- Q9: gap-length tiered re-entry.
- Q10: the fresh adversarial "try-to-fake-it" self-cert session (= the OS's binding-G5
  machinery) — pre-named hardening if owner self-attestation proves too soft.

---

## 7. Key sources (by question, strongest-verified first)

- Q1: Covey *First Things First* / big-rocks; HBR/JCR time-blocking studies (figures
  vendor-amplified); Kanban WIP + explicit policy (kanban.university); MIT method (Zen
  Habits/Hubstaff); GTD/PARA documented limits.
- Q2: Michie et al. 2013 BCT Taxonomy v1 (93 techniques); Theory & Technique Tool
  (Connell/Carey 2019); Gollwitzer & Sheeran 2006 implementation intentions; WWC single-case
  standards; Nahum-Shani JITAI; Quantified-Self minimal-intake.
- Q3: FranklinCovey Habit 3; Meeusen 2013 overtraining consensus + supercompensation;
  Gabbett acute:chronic workload ratio (+ its critique); Little's Law/WIP; Loehr & Schwartz
  energy management.
- Q4: Nayebi 2025 "Core Safety Values for Provably Corrigible Agents" (arXiv 2507.20964;
  undecidability limit); Constitutional/Collective Constitutional AI; OPA invariant
  validators; prompt regression / golden-anchor suites; git-native markdown agents.
- Q5: Marlatt & Gordon relapse prevention (PMC6760427); "beyond self-report" addiction
  markers; Gollwitzer implementation intentions / Ulysses contracts; AA sponsor reach-in;
  Deci & Ryan self-monitoring vs surveillance; behavioral activation.
- Q6: Parasuraman/Sheridan/Wickens 2000 LOA; Sheridan's own caveat; Dietvorst 2015/2018
  algorithm aversion; de Visser 2018 trust repair; competence-aware supervised autonomy
  (arXiv 2003.07745).
- Q7: Ryan & Frederick Subjective Vitality Scale; SVS-GM single-item validation (PMC9374102);
  Ryan/Huta/Deci 2008 SDT eudaimonia; KORA one-item screen 46%/94% (PMC3906912).
- Q8: Gawande *Checklist Manifesto*; Lean/Kanban muda + WIP; firewall "spring cleaning"
  dormancy; Agile retro time-boxing.
- Q9: Marlatt AVE (PMC6760427); Breines & Chen 2012 self-compassion; Eubanks/Muran/Safran
  2018 rupture-repair; Fluckiger 2018 alliance-outcome; Duolingo streak-freeze (vendor-
  reported).
- Q10: dogfooding (Wikipedia/Splunk); ECOVAL ecological validity (PMC11276482); UAT best
  practices; demo-vs-live trading psychology; Agile Definition-of-Done.

END_OF_FILE: live/life-reset/work/life-reset-implementation-research-v1.md
