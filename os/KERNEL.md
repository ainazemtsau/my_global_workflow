# KERNEL — Direction OS

Authority order: live owner instruction > this kernel > the active play > direction state files > everything else (history, prior chats, model memory). On conflict the higher source wins; log the conflict as friction (§7).

## 1. What this is

The OS runs the owner's long-term directions through short AI legs over durable Git state.

- A **direction** lives in `live/<id>/` as the fixed state files (§3).
- A **leg** is one job under one play. Normally one physical chat = one leg. An owner-started `day` chat may hold read-only discussion and sequential saved day legs for one owner day; every saved leg rereads fresh Git, has one RESULT/apply/commit, and the next day starts a new chat. Context is RAM: unwritten memory is not state.
- A **play** is a procedure in `os/plays/`; only plays change state.
- The **owner** decides. Agents do everything else. The owner never composes packets by hand.

## 2. Session contract

1. **OPEN** — input is a CALL or a plain owner message. Assemble the working set with `python osctl.py context --for <target>`: it reads by card links, not by folder, and names what it left out — reading `cards/` whole is 6× the set. Add the play and named evidence. Whatever it lists as waiting for the owner goes to him in plain words BEFORE the first play step; he may defer, and a deferred item stays. Resolve plain input from state:
   - `начинаем день`, a daily status request, or continued discussion in today's day chat → `day`;
   - mission/success change → `frame`; roadmap/future-goal change → `map`; active-objective close, replacement or kill → `review`; a parked `outcome_kind: specification` → owner-authority `work` → fresh `converge-verify` → narrow `review`; ordinary activation → readiness router: passing `converge-verify` RESULT → `shape`; recorded `triage: <type> — converge OFF — because <reason>` copied into shape `play_check` → `shape`; a second-FAIL ceiling decision in his words → its chosen branch, `shape` on what is answered included; otherwise → `converge`;
   - task, lane, launch/loss receipt or recurring work → its `work` CALL; contradiction → `repair`;
   - `продолжаем` → the sole actionable call/decision; several → grouped choice with a recommendation and no mutation; none → waits, blocks, issues and the planning route;
   - question → read-only; no-state ambition → `frame`; otherwise interpret and confirm.
   An ordinary leg opens with the orientation header, numbered play steps/current marked, and a ≤5-line restate. A day chat opens with its plain day header and derived brief; steps stay internal. Then run the play and stop at the first owner step. Play outranks CALL.
2. **WORK** — follow the play. Cross-cutting moves available in any leg:
   - `call:research` — bounded child question;
   - `call:executor` — delegated execution;
   - `capture` — one-line emergent idea for later triage, never acted on in the same leg;
   - `decision` — owner question with 2–3 options and a recommendation;
   - `knowledge` — record one settled durable fact where every load-bearing line cites his exact words or a resolvable artifact and `read_by` names a real consumer. What the leg reasoned out stays a capture. The converge family only proposes; review/pulse merge, retire and mark stale.
3. **CLOSE** — emit RESULT (§4) as the leg's final message only: readable summary, then one fenced RESULT. It ends the leg; the writer applies/commits `state_changes`. A checkpoint issues a continuation CALL. A day chat may accept a later owner turn only after the saved transaction completes; `закрываем день` ends it. Read-only day turns emit no RESULT.

**Orientation header.** Ordinary reply:
`📍 <direction>[/<lane>]/<node>/<task> — <play>: <step> | нужно от тебя: <ничего | вопрос>`.
Day reply:
`📍 День: <простая текущая цель> | от тебя: <ничего | короткий выбор>`.

**Language.** Talk to the owner in Russian. State keys stay English; values may use any language.

**Owner-facing vs machine.** Packets and state are machine artifacts. Owner prose omits ids, enum labels, packet terms and empty fields unless a paste-ready task is requested.

**Legs do not write.** Repo access is not write permission. Changes travel only in RESULT.state_changes; an agent-CLI leg becomes its own writer only after emitting its RESULT.

**Day save boundary.** Discussion, analysis, corrections and the chat dashboard are read-only. Only the owner's explicit words to save/record/launch the exact agreed delta permit a day RESULT. A structural change is handed to its owning play; `day` never edits CHARTER/nodes or silently creates strategy.

**Two strikes.** After two failed correction rounds on the same point, checkpoint and continue in a fresh chat.

## 3. Direction state — five file types, never more

| File | Holds | Written by |
|---|---|---|
| `CHARTER.md` | mission, measurable success, constraints, lenses, repos | frame |
| `NOW.md` | pointer: bet node id, lane WIP limit | every leg |
| `cards/` | one file per entity — bet/node/task/call/issue/decision/recurring/track/extra — each carrying its journal; `node` cards are the roadmap, future objectives visible; closed → `cards/closed/` | `node`: frame/map/shape/review; rest: every leg |
| `history/` | full RESULT of every leg | append-only |
| `knowledge/` | accepted facts; each names who reads it and when | any leg (`knowledge` move); review/pulse curate |

`work/` holds outputs and evidence, never current state.

**Goal node:** stable `id`, outcome `goal`, verifiable `done_when`, one-line `why`, `status: parked | shaped | active | done | dropped`, `_parent` (root: none) and `_pos`. Exactly one non-root node may be `active`: the current bet. A shaped/active node carries `appetite` and `kill_by`.

A node whose result is the exact owner-approved specification itself carries `outcome_kind: specification`; unmarked nodes are ordinary build outcomes. It stays `parked` while an untracked owner-present authority contour authors the versioned artifact, a separate fresh `converge-verify` session refutes it, and narrow `review` marks it done. It never becomes a bet, enters `shape`, creates tasks/tracks, or delegates owner-content verdicts to an executor.

A **bet** is the one active local objective. Its tasks are each ≤ half a focused day; `shape` sizes the list and G1 caps what runs at once. Optional tracks are execution lanes inside that bet, not parallel strategies or future goals. Only `shape` declares a lane — it offers lanes and their owner-set WIP limit; only the owner's exact words declare them, and only `review` dissolves the lanes of the bet it closes. No other play creates or removes one. Work unrelated to the bet becomes an issue/capture until the correct review/map/maintenance route admits it.

## 4. Packets

**CALL** moves work between legs/agents: `goal` · `context` · `boundaries` · `done_when` · `return` · `budget`.

**RESULT** ends a leg: `outcome` · `evidence` · `state_changes` · `captures` · `decisions_needed` · `play_check` · `log` · `next`. It never selects foreign work. Owner steps cite actual owner words.

In lane mode a continuation may be `ready|running|waiting|blocked|paused`; the call card's `status` decides dispatchability. `running` needs an exact launch receipt and is never reoffered.

An engineering CALL goes to a product repo. Its return comes HOME; only Direction issues successor CALLs. Evidence = commits/PR + checks; product delivery alone is not Direction close.

## 5. Hard gates

- **G1 (WIP).** At most one active bet per direction; the owner sets how many of its tasks/lanes run at once, on `shape`'s proposal. Without a bet there are no non-recurring execution lanes; one untracked specification-authoring planning frontier is legal. ≤1 ordinary root per lane.
- **G2 (rolling wave).** Tasks and non-recurring execution lanes serve only the active bet. Future objectives stay outcome-level node cards; unrelated work stays an issue/capture until admitted.
- **G3 (appetite).** Appetite is set before tasks and never extends. Over-appetite work dies; continuation requires a new shape.
- **G4 (bet validity).** A bet without done_when and kill_by is invalid.
- **G5 (evidence).** `done` requires evidence matching done_when. Verification tries to refute the claim in a separate fresh physical chat from the work and any day chat; a re-derivable done_when closes light (`work`).
- **G6 (shape validity).** Shape requires a real cut list, a verdict per lens, and a task testing the riskiest assumption.
- **G7 (decisions).** Owner decisions carry options and a recommendation; batch them. A leg may decide alone only what it is CERTAIN of; any real doubt goes to him — asking is cheap, an invented answer is not. Product concept and gameplay are ALWAYS his: a leg never invents them however certain it feels, and no CALL may widen one narrow owner statement into a standing ban on asking.
- **G8 (intake).** New directions/top-level goals enter through frame. New ideas default parked.
- **G9 (co-creation).** CHARTER/nodes/approvals change only after explicit owner approval of the exact artifact; RESULT marks `owner_approved`.
- **G10 (protocol).** Ordinary legs expose steps; day keeps them internal. RESULT is final only; legs never write state; a day RESULT additionally cites the owner's explicit save words.

A leg that cannot pass a gate stops; it never improvises around it.

## 6. Plays

`frame · map · shape · converge · converge-arch · converge-verify · day · work · guide · review · research · pulse · repair` live in `os/plays/`. Directions may add local plays in `live/<id>/plays/`; a missing/unknown play routes to repair.

## 7. Changing the OS

The OS changes only through `os/MAINTENANCE.md`: an explicit owner request is sufficient; self-initiated changes need ≥2 matching FRICTION entries. Budgets are absolute: kernel ≤1800 words, each play ≤600, five state file types. Prefer removing failed structure to adding another authority layer.

END_OF_FILE: os/KERNEL.md
