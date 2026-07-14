# MAINTENANCE — how the OS itself gets changed

The OS is infrastructure, not a direction: no charter, no tree, no bets. It changes through **maintenance sessions** — fresh Claude Code / Codex sessions on this repo. One problem or request = one session. This file is the procedure those sessions follow.

## Entry

The owner opens a fresh agent session on this repo and pastes:

```
MAINTENANCE REQUEST
what: |
  <проблема или фича: что произошло / чего не хватает, своими словами>
where: |
  <если известно: направление, play, файл, цитата из чата — что угодно>
expected: |
  <как должно быть>
```

A problem chat transcript is an equally valid entry: paste the transcript (whole or fragment) plus one line on what felt wrong — the session derives what/where/expected itself.

No other setup. The session reads this file and runs the procedure below.

## Procedure

1. **Locate.** Read `os/FRICTION.md` and the named files; grep for the responsible rule. Restate the problem in ≤3 lines and classify:
   - (a) rule defect — a rule is wrong/ambiguous/contradictory;
   - (b) gap — a needed capability has no home;
   - (c) customization — owner wants different behavior;
   - (d) one-off accident — rules are fine, an execution slipped → no rule change; log friction, suggest the repair play if state is affected;
   - (e) unclear / single occurrence of a suspected pattern → log friction only, no change yet.

   With a transcript: replay it against its play step by step — behavior vs rule text — and give the verdict BEFORE designing anything: the session broke the rule (→ d), the rule produced the behavior (→ a/b), the platform did (connector cache, project chat history → adapter fix or friction watch), or the expectation itself was wrong (explain to the owner; no change). The owner's proposed mechanism is a hunch, not a spec: extract the underlying problem and judge it independently — "rules are fine, usage was wrong" is a valid resolution.
2. **Trigger check.** An explicit owner request is a sufficient trigger for (a)–(c). Self-initiated improvements (nobody asked) need ≥2 FRICTION entries on the same point. Never both fix the request AND slip in unrelated "improvements".
3. **Design the smallest change** that resolves the case, inside the budgets: kernel ≤1500 words, a play ≤600, six state file types, two packet types. If the fix wants to exceed a budget — simplify the fix or propose removing something else in the same change; growing past budgets is solving the wrong problem.
   **Semantic-review boundary:** when the job is to judge the meaning or completeness of a plan, spec, rule, review, or RESULT, the reviewer is the AI reading the authoritative artifacts. The session must not create or run a new script, parser, schema, regex scanner, conformance harness, or other executable proxy to make that judgment. Existing repo-native commands may establish objective facts only (for example exact SHA/ancestry, file existence, clean state, compilation, or test outcome). Any new process automation requires a separate owner-approved maintenance request that names one objective machine predicate; without that explicit approval, stop at a short proposal and do not build it.
4. **Consistency sweep.** Grep every term/file the change touches and update all cross-references. If `os/adapters/SESSION_PAYLOAD.md` changed, say so explicitly in the reply — the owner must re-paste platform instructions (politely degradable, not urgent).
5. **Verify.** Re-read the changed files end-to-end for contradictions; walk one affected scenario (use the validation trace in `os/docs/DESIGN.md` §4 as the test track). A change that can't survive the walkthrough doesn't ship.
6. **Log & close.** Append the case to `os/FRICTION.md` with `→ fixed <commit>` (or `→ logged, watching` for (d)/(e)). **If the change hardened or added a load-bearing engineering gate** (CONTOUR / VALIDATION / PROJECT_SETUP / ESCAPE-CLASSES / a profile), bump `os/engineering/CONTRACT_VERSION` (`current:` + one log line) and name the product-repo §Re-sync as a follow-up — this is what makes the propagation visible (`collect`/`audit`/`digest` flag any repo left behind) instead of silently lagging. **If the case is a product DEFECT that reached a late stage** (owner-eye / independent review / post-merge), also name the CLASS it violated by its INVARIANT — never its surface site — and append it to `os/engineering/ESCAPE-CLASSES.md` with its witness, so the PLAN spec-silence audit (CONTOUR §b) asks it of every future feature of any direction; **a single past-the-test-author escape is a sufficient trigger** for this append (the one place the ≥2-entry threshold is waived — a class must not be allowed a second escape). Commit with a descriptive message. Reply to the owner with: what changed and where, why this is the smallest fix, anything the owner must do (usually nothing), and a one-line litmus to re-test it in his next chat.

## Boundaries

- A maintenance session never touches `live/**` — direction state is the repair play's territory.
- One problem per session. A second problem surfacing mid-session → one line into FRICTION.md, not a second fix.
- No speculative structure: nothing is added "for the future". The parking lot for OS ideas is FRICTION.md with `→ idea, watching`.

END_OF_FILE: os/MAINTENANCE.md
