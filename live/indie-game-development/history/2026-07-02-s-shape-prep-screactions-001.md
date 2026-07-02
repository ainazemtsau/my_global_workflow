# RESULT s-shape-prep-screactions-001 — Sc-reactions shape-prep: forks (a)–(f) closed, c-exec-021 body rewritten

Session: 2026-07-02, owner present. Play = shape (PREP scope: closes the next slice's design forks and rewrites its
frozen executor CALL; the active bet is NOT changed — G1 untouched, Sc-kernel stays the active task). Ran PARALLEL to
the Sc-kernel executor leg per the NOW.next license.

## Owner decision record (2026-07-02, in-chat; cleaned of speech fillers, meaning verbatim)

- **(a) overflow:** «я не помню вообще, откуда это требование пять газов сошлись … если мы можем делать, чтобы любое
  количество газов сходилось, то это невалидное требование … если можно сделать любое количество или больше, то это
  не требование, это устаревшее осталось» + «какая-то очередь реакций или что-то ещё … это отлично». Then: «если не
  учитывать это, то твои предложения принимаю, именно что касается пункта А». → Layered mass-conserving policy
  CONFIRMED + REFRAME: any-N ZONE mixing = the requirement; per-cell K = internal config constant, never a design cap.
- **(b) schema:** conditional accept — «Если он всё это будет поддерживать, то я принимаю» (his model: gas spawns
  typeless, takes type from environment at spawn; env conditions [temperature thresholds, pressure, rooms…] can flip
  it; gas×gas mixing → type change, or explosion whose wave re-types gas in a radius; env interaction only when the
  environment has a property/TAG). Plus his addition: DEFAULT reactions for undefined combinations («если жарко —
  сгорает; если холодно — стынет, образно») — «я думаю, это как хорошее решение тоже. Вот если ты можешь меня
  критиковать … мы сейчас именно ищем лучшее решение». → Accepted as the FOUR-tier data schema (explicit-SET > AXIS >
  optional env-conditioned DEFAULT rows > identity); env-tags = named env-vector channels; critique folded: blanket
  everything-reacts default rejected; single-reactant env-response rows = schema-admitted data, firing semantics at
  Sc-typing (no instant-flip side door); support-conditions verified: his whole model is covered by
  schema+typing+waves, with honest timing (temp rows dormant until d-tempfeedback-001; typing mechanism = Sc-typing;
  waves = fork).
- **(c) wave×wind:** «для меня вообще сложно … рассчитываю на твоё решение» → DELEGATED; decided = pin the observable
  property: each gas parcel converts EXACTLY ONCE per wave ((cell,wave-id) idempotence) + the wave×wind RED oracle;
  mechanism = the executor PLAN's call; waves remain a fork.
- **(d) blast wave:** «ладно, я смотрю, что ты вроде как правильно понял» — gameplay-load-bearing confirmed; his
  EXTENSION: «Она может стены ещё сносить … объекты, которые физически корректны … должны взрывной волной тоже
  разлетаться» → recorded as design intent and ROUTED, not promised in this slice: walls → S5 breach seam; bodies/
  loot → Sc-damage (after SPEC §4 шов-7 player-kinematics); this slice = gas push via S1 impulse; reserved DORMANT
  outcome kinds (body-impulse, wall-breach, ignite/freeze).
- **(e) typing:** «пункт Е тоже как-то сложновато … рассчитываю на твоё решение» (placement DELEGATED) +
  «Под-развилка 2 согласен с тобой» (mechanism agreed) → decided: Sc-typing = NAMED slice immediately after
  Sc-reactions (July demo-road shape 07-10..15 = named checkpoint to consciously swap vs Sc-damage);
  accumulate-with-hysteresis over instant flip.
- **(f) registry/legacy:** «С пунктом F я с тобой согласен. Единственное, что если нам какой-то класс не нужен, мы
  legacy не храним, удаляем. То есть не должно быть старого кода, чтобы он не загрязнял контекст. Поэтому если
  что-то не нужно, то удалить надо. Просто так не держать.» → outcome registry on near VoxelField confirmed; the
  dead Layers/ReactionLayer demo tier disposition CHANGED keep→DELETE via an owner-pre-signed live-spec amendment —
  this quote IS the pre-signature, SCOPED to the demo-tier files + their ReactionLayer SHALL lines only; the
  GridEvent bus/enum (Reaction=3) stays locked and untouched; verify-uncomposed first; STOP on live composition or
  wider SHALL.

## RESULT

```
RESULT s-shape-prep-screactions-001 (2026-07-02, g-9c41 / Sc-reactions prep, play: shape[prep], owner present)

outcome: |
  Sc-reactions design prep CLOSED: shape forks (a)–(f) decided with the owner in-session; the frozen c-exec-021
  body FULLY REWRITTEN at work/c-exec-021-call.md onto the current base (sparse-dominant, base = post-Sc-kernel
  main) — both banner generations retired into it, the 2026-06-30 hardening preserved as principle, audit
  §Package item-5 pins folded with finding-id traceability; the CALL is marked «PREPPED — awaits Sc-kernel GREEN
  to re-harden + fire». Sc-typing homed as the NAMED slice after Sc-reactions. G1 untouched (Sc-kernel stays the
  active task); no product code touched; no locks opened; nothing fired.
evidence: |
  - Rewritten CALL: work/c-exec-021-call.md (STATUS PREPPED; §Re-sync section; PENDING items named, not invented).
  - Owner decisions recorded above (quotes, this file) — the (f) quote doubles as the amendment pre-signature.
  - Adversarial check of the rewritten body vs STATE: workflow wf_8ab4a0cb-401 — 6 lenses (canon / owner-fidelity /
    audit-coverage / staleness / gate-quality / process-lock), 36 findings raised; 10 machine-verified CONFIRMED
    (0 refuted); 26 verifier agents died on subagent quota → adjudicated FIRST-HAND in-session against the draft +
    sources; ~22 distinct defects folded (key: single-reactant env-row firing scope → Sc-typing; chemistry-first
    obeys the telegraph law, no overflow bypass; GridEvent bus/enum scope guard [Reaction=3 STAYS]; Coarse/
    scan-root reconciliation with c-exec-023; §Re-sync section restored; spec-silence-blindness NB restored;
    G5 cross-family restored; consume-vs-residue + regime-vs-identity routed; budget leg wording de-prejudged;
    «written into next_slices» made true by this RESULT's own state_changes). 0 construction-breaking findings.
  - HONESTY: this pass checked the body against STATE (SPEC/NOW/audit/decisions), NOT against post-Sc-kernel code
    (does not exist yet). The binding code-grounded FULL re-hardening runs at fire time per the CALL's STATUS.
    Evidence here = in-session pre-pass + first-hand adjudication, not a binding fresh G5 (none required: this is
    a design artifact, not a «done» bet claim).
state_changes: |
  1. work/c-exec-021-call.md — REPLACED with the rewritten PREPPED body (END_OF_FILE trailer kept).
  2. NOW.md header: updated-by → s-shape-prep-screactions-001.
  3. NOW.md bet.goal road string → «Sc-types → Sc-weight → Sc-rep → Sc-kernel → Sc-reactions → Sc-typing →
     Sc-damage» (reconciles the pre-Sc-kernel wording).
  4. NOW.md bet.current_truth += the 2026-07-02 shape-prep paragraph.
  5. NOW.md next_slices: Sc-reactions row → PREPPED wording (after Sc-kernel); NEW row «Sc-typing after
     Sc-reactions»; Sc-damage row re-homed «after Sc-typing».
  6. NOW.md open_calls c-exec-021 note → replaced with the PREPPED note (decisions a–f, PENDING list, check record).
  7. NOW.md next: PARALLEL paragraph → prep DONE + fire-time procedure.
  8. NOW.md history_pointers += this session.
  9. LOG.md += one line (below).
  10. history/2026-07-02-s-shape-prep-screactions-001.md = this file.
captures: |
  - fork-b synergy (recorded in the CALL as a future data kind, not built): product = «parent substance re-typed
    by local env».
  - The Sc-damage shape must take the шов-7 player-kinematics decision BEFORE any body/loot blast-impulse outcome
    kind activates (fork-d routing; reinforces audit package item 6).
  - Workflow verify legs died on the subscription session limit mid-run (resets 13:00 Europe/Minsk) — first-hand
    adjudication covered the gap this time; for future heavy verifies consider scheduling after the reset.
decisions_needed: |
  none — all six forks closed in-session; the CALL's PENDING items are fed by the Sc-kernel RESULT, not by owner
  questions.
play_check: |
  shape (PREP scope — no bet change): 1 Recite — done (opening contract restated play/goal/done_when vs NOW).
  2 Appetite — n/a for a new bet (G1 untouched); the CALL §budget updated honestly («fatter», split = default).
  3 Approaches — per-fork options + recommendation delivered as one batched brief (G7). 4 Scope hammer — cuts
  recorded in CALL boundaries: walls→S5, bodies/loot→Sc-damage, typing mechanism + single-reactant env rows →
  Sc-typing, cross-type capacity → ≤Sc-damage, wave build → fork. 5 Lens sweep — n/a (no bet re-shape; the CALL's
  gate battery carries the engineering lenses). 6 Riskiest assumption — unchanged carriers: NEW-TYPE-IS-DATA RED +
  N-type junction RED first-class in done_when. 7 Tasks — n/a (executor CALL is the carrier; no NOW task added).
  8 Kill criteria — unchanged (Sc-kernel kill_by governs the active bet; c-021 fires only post-GREEN).
  9 Close (owner) — owner words per fork recorded above ((a) «твои предложения принимаю…», (b) «Если он всё это
  будет поддерживать, то я принимаю», (c)/(e-where) «рассчитываю на твоё решение», (d) «вроде как правильно понял»,
  (e-how) «Под-развилка 2 согласен с тобой», (f) «С пунктом F я с тобой согласен…»).
log: |
  2026-07-02 — shape-prep (g-9c41/Sc-reactions; s-shape-prep-screactions-001): forks (a)–(f) CLOSED owner-present
  (any-N mixing reframe; 4-tier data schema + DEFAULT rows; exactly-once wave semantics; gameplay blast wave with
  walls→S5/bodies→Sc-damage routing; Sc-typing homed after Sc-reactions w/ hysteresis; ReactionLayer → DELETE via
  pre-signed amendment) → c-exec-021 body FULLY REWRITTEN (banners retired; check wf_8ab4a0cb-401: 36 raised →
  ~22 distinct folded, 0 construction-breaking) = PREPPED, awaits Sc-kernel GREEN. Sc-typing added to next_slices.
  G1 untouched. OS commit LOCAL; push owner-gated.
next: |
  UNCHANGED primary work: a FRESH GasCoopGame_dev executor session opens c-exec-023 (Sc-kernel, owner-present
  PLAN, base main @5442be0). On Sc-kernel GREEN: a fresh session runs the c-exec-021 §Re-sync sweep + the FULL
  code-grounded re-hardening, fills §PENDING from the Sc-kernel RESULT, then fires c-exec-021 in a fresh
  GasCoopGame_dev session (owner-present PLAN). This session issues no new CALL.
```

END_OF_FILE: live/indie-game-development/history/2026-07-02-s-shape-prep-screactions-001.md
