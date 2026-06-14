# Play: converge-verify

Purpose: a SEPARATE refutation session that tries to BREAK a converged node's spec before shape consumes it — the half of derivability a self-check cannot give, because an author cannot catch the assumption he did not know he made. Reuses G5 (a claim is verified in a session other than the one that made it, by trying to refute it), lifted from code to spec. No gate touched; closure is this play's Done-when.

Reads: work/converge-<node>.md (closed §GLOSSARY/§WHAT/§CONTRACTS), TREE.md (node done_when), CHARTER.md, knowledge/ (node-class decision-class checklists, sibling canon). It does NOT read the deciding sessions' reasoning — it re-derives independently.
Writes: NOW.md (decisions, open_calls — a finding bounces a row), LOG.md. Never writes knowledge/. Never answers a question; it only refutes or passes.

Precondition: converge done (and converge-arch done if the node is heavy or sibling-bearing). Reached via CALL `to: session, play: converge-verify`.

## Steps

1. **Recite the claim** — restate the two propositions this session attacks: (1) the question set is COMPLETE; (2) no answer leans on an unresolved question. Passing both is the only route to shape.

2. **Attack completeness — with an INDEPENDENT oracle.** Do NOT re-derive from the sources converge used (done_when + the chosen mechanism) — that shares the prover's blind spot. Use a THIRD source: the node-type's decision-class checklist in knowledge/ (e.g. a networked-stateful-stream node must answer representation/quantization, divergence bound, recovery/keyframe, channel reliability, settle predicate) PLUS any compete child's precedent set. If no checklist exists for the node-class (first run), AUTHOR one from first principles BEFORE attacking, name it, propose it as canon — an empty oracle is a BLOCKED close, never auto-PASS. First split every COMPOUND done_when criterion atomically (a clause with "and" / a list / multiple verbs → one sub-criterion each) and check each maps to a §WHAT row. Any decision-class with no row, or an unsplit compound, is a completeness FAIL → name the missing question, bounce to converge.

3. **Attack smuggling.** For each weight-bearing §WHAT line and each acceptance criterion, name every value or fact it leans on and check each traces to a cited resolved row (`→Wn` / `→GLOSSARY`) or a frozen canon id. An untraceable value is a smuggled assumption → bounce that row to `open`. Re-check the FIREWALL: any HOW magnitude/format that drifted into an acceptance line → `→ PLAN`.

4. **Close.** If either attack finds anything: `next` = a CALL back to converge (or converge-arch) carrying the bounced rows; verify re-runs after they re-close. If both pass clean: write `§SIGNOFF: converge-verify passed @ <date>`; emit play_check `verify: complete=PASS smuggling=PASS`; `next` = a CALL for shape on this node, whose context names the §WHAT `acceptance` rows + §CONTRACTS requirements to COPY into the executor done_when (binding by G5) and the `→ PLAN` rows as the PLAN-agenda.

## Done when
Both refutations fail to find a hole (or every hole found is bounced and a later verify passes); `§SIGNOFF: converge-verify passed` exists; shape's CALL carries the acceptance + contract rows to copy and the PLAN-agenda.

## Notes
- The anti-smuggling guarantee in its TRUE shape, stated to the owner: citing an open question is structurally impossible (a resolved row exists only with an answer); an UNCITED smuggled assumption is caught HERE, by a separate session with an independent oracle — rigorous, not a closed proof.
- Decision-class checklists are cross-node canon (knowledge/, read_by converge-verify of that node-class); review/pulse promote them.
- No new owner G7 point — verify routes findings; the owner already signed the answers in converge. Same row bouncing twice → two-strikes (KERNEL §2): close with a handoff note.

END_OF_FILE: os/plays/converge-verify.md
