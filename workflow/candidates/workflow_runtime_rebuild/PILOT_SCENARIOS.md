# Pilot Scenarios

status: candidate_draft

## Purpose

This file defines Stage 4 pilot scenarios for Workflow Runtime Rebuild.

The scenarios check whether the candidate runtime is understandable and coherent in realistic work.

They do not activate runtime.
They do not replace the current Workflow OS.
They do not migrate active Directions.
They do not create accepted state by document existence.

## How to read these scenarios

Each scenario tests one practical workflow boundary.

A scenario passes only when the expected behavior is explicit, the output is usable by a human, and the next step is not guessed.

A scenario fails when the runtime hides state changes, treats candidate output as accepted, spreads into unrelated work, or makes the user assemble the next step manually.

## Scenario 1 — create new direction from ordinary human text

Purpose:
  Check that a user can start from normal text, not YAML.

Starting condition:
  No accepted Direction exists for the new project.

Input:
  "Я хочу сделать долгий проект: свой AI-workflow для разработки игры. Нужно, чтобы он не разваливался между чатами."

Expected runtime behavior:
  ChatGPT normalizes the input into a candidate Direction idea.
  It identifies missing decisions needed for Direction Spine.
  It does not pretend that the Direction is already accepted.
  It produces a clear Next Move for defining Direction Spine.

Expected output:
  A short candidate Direction summary.
  Missing root result / success condition questions.
  A candidate Launch Packet or human decision request for Direction Spine definition.

Pass criteria:
  The user sees what was understood.
  The user sees what is still undecided.
  The output can start Direction Spine work without requiring YAML from the user.

Fail conditions:
  ChatGPT creates a full roadmap.
  ChatGPT treats the direction as accepted without explicit user decision.
  ChatGPT starts implementation.

What must not happen:
  No hidden accepted-state mutation.
  No Project Files treated as truth.
  No launch of Codex.
  No global backlog creation.

## Scenario 2 — define Direction Spine

Purpose:
  Check that Direction Spine becomes a simple axis, not a huge roadmap.

Starting condition:
  A candidate Direction idea exists, but no accepted Direction Spine exists.

Input:
  User confirms:
  "Root Result: рабочий AI-workflow для долгих проектов. Success: можно продолжать между чатами, запускать Codex bounded package и не терять принятые решения."

Expected runtime behavior:
  ChatGPT proposes Direction Spine with Root Result, Success Conditions, Spine Points and Tracks.
  It marks the result as candidate until explicit acceptance.
  It identifies any missing acceptance decision.

Expected output:
  Candidate Direction Spine.
  Clear acceptance question or Next Move for parent review.

Pass criteria:
  Direction Spine is visible.
  It is short.
  It does not include every future task.
  It can support Active Front selection.

Fail conditions:
  Direction Spine becomes a full implementation roadmap.
  Tracks become independent projects without relation to Root Result.
  User examples become accepted constraints without confirmation.

What must not happen:
  No automatic acceptance.
  No migration of active Directions.
  No current Workflow OS replacement.

## Scenario 3 — select Active Front

Purpose:
  Check that runtime can choose a small current focus from Direction Spine.

Starting condition:
  Direction Spine exists as candidate or accepted baseline.

Input:
  "Сейчас хочу проверить, достаточно ли модель целостна перед интеграцией."

Expected runtime behavior:
  ChatGPT selects candidate Active Front related to the Direction Spine.
  It explains why this front is selected.
  It states what is out of scope.
  It does not move all tracks at once.

Expected output:
  Active Front summary.
  In-scope boundary.
  Out-of-scope boundary.
  Next Move to open a local Work Graph.

Pass criteria:
  Active Front is bounded and understandable.
  It shows why this is the current focus.
  It prevents unrelated work from entering.

Fail conditions:
  Active Front becomes the whole project.
  Runtime launches work from every track.
  Off-scope issues are executed instead of parked.

What must not happen:
  No hidden route change.
  No acceptance by explanation.
  No Action Inbox auto-run.

## Scenario 4 — open local Work Graph

Purpose:
  Check that Work Graph is local to Active Front, not a global graph of the whole direction.

Starting condition:
  Active Front is selected.

Input:
  "Разложи текущий front на ближайшие рабочие nodes."

Expected runtime behavior:
  ChatGPT opens a local Work Graph for the Active Front only.
  It proposes nearest nodes and dependencies.
  It identifies one next node that can produce one meaningful result.

Expected output:
  Local Work Graph.
  Candidate next node.
  Dependencies and blockers.
  Next Move to create Work Contract or Launch Packet.

Pass criteria:
  Work Graph is small.
  Each node has a meaningful expected result.
  It does not duplicate Direction Spine.

Fail conditions:
  Work Graph becomes a universal backlog.
  Nodes are micro-steps.
  Work starts before selecting a node.

What must not happen:
  No global roadmap.
  No unrelated future tasks.
  No Codex package without Work Contract.

## Scenario 5 — launch Work Chat

Purpose:
  Check that a material Work Chat starts with a Launch Packet.

Starting condition:
  A next Work Graph node is selected.

Input:
  Launch Packet for:
  "Design pilot scenarios for Stage 4 candidate runtime."

Expected runtime behavior:
  Work Chat checks source authority, scope, boundaries, expected result, evidence and return destination.
  If context is sufficient, it performs only that bounded work.
  If context is missing, it returns blocked Result Packet.

Expected output:
  Material draft or blocked Result Packet.
  Source/read limitations.
  Exact Next Move.

Pass criteria:
  Launch Packet includes target, source refs, in scope, out of scope, expected result, evidence and return destination.
  Work Chat does not continue from vague memory.

Fail conditions:
  Chat starts from "continue where we left off."
  Chat changes route or acceptance criteria.
  Chat starts unrelated work.

What must not happen:
  No material work without Launch Packet.
  No hidden acceptance.
  No vague closure.

## Scenario 6 — close Work Chat with Result Packet + exact Next Move

Purpose:
  Check that user does not have to guess the next step.

Starting condition:
  Work Chat has produced a candidate result.

Input:
  "Закрой этот work chat."

Expected runtime behavior:
  ChatGPT summarizes what was done and not done.
  It states evidence, limitations, assumptions, unresolved decisions and risks.
  It marks result as candidate unless accepted separately.
  It gives exact Next Move.

Expected output:
  Result Packet.
  Exact Next Move.
  Candidate status notice.

Pass criteria:
  Result Packet is copy-pasteable into parent/integration review.
  Next Move says exactly what to open, paste, verify, accept or decide.

Fail conditions:
  Chat ends with only explanation.
  Chat says "done" without evidence.
  Chat implies accepted state without acceptance/update path.

What must not happen:
  No "you can decide what to do next."
  No acceptance hidden inside Result Packet.
  No missing limitations.

## Scenario 7 — create Codex Work Package

Purpose:
  Check that Codex is bounded and receives a complete package.

Starting condition:
  Work Chat or parent review has a candidate documentation persistence target.

Input:
  "Подготовь Codex handoff, чтобы сохранить Stage 4 candidate docs."

Expected runtime behavior:
  ChatGPT creates self-contained Codex Work Package.
  It includes repository, base ref, target branch, branch policy, allowed paths, forbidden paths, required changes, validation, stop conditions and return fields.
  It does not ask Codex to decide acceptance or activation.

Expected output:
  Copy-paste-ready Codex Work Package.

Pass criteria:
  Codex can run without asking what repository, branch, files or validation to use.
  Allowed and forbidden paths are explicit.
  Branch policy is explicit.

Fail conditions:
  Package says "fix everything."
  Package omits validation.
  Package allows active runtime or Project setup edits.

What must not happen:
  No merge-to-main instruction.
  No runtime activation.
  No scope expansion by Codex.

## Scenario 8 — verify Codex Result Packet

Purpose:
  Check that Codex output remains candidate evidence until verified.

Starting condition:
  Codex returns a Codex Result Packet.

Input:
  Codex Result:
  "DONE. Branch X. Commit Y. Changed files A/B/C. Validation passed."

Expected runtime behavior:
  ChatGPT verifies branch, commit, changed files, allowed paths, forbidden paths, validation, EOF markers, markdown fences and residual risks.
  It classifies result as verified, repair-needed, blocked, rejected scope violation or rejected validation failed.
  It does not accept result automatically.

Expected output:
  Verification result.
  Missing evidence request if needed.
  Exact Next Move.

Pass criteria:
  Changed files are within allowed paths.
  Forbidden paths unchanged.
  Validation evidence is credible.
  Codex Result is not treated as accepted by itself.

Fail conditions:
  ChatGPT accepts "done" without checking changed files.
  Missing commit SHA is ignored when commit was requested.
  Failed validation is treated as success.

What must not happen:
  No hidden acceptance.
  No "no validation but done."
  No Project refresh confusion.

## Scenario 9 — launch Child Chat and return result to Parent / Integration Chat

Purpose:
  Check parent/child coordination without child chats becoming independent workflows.

Starting condition:
  Parent / Integration Chat has a bounded target too broad for one result.

Input:
  Parent creates Child Launch Packet:
  "Audit whether Action Inbox scenarios cover handler flood and stale items."

Expected runtime behavior:
  Parent defines why child result is needed.
  Child Chat receives bounded scope and return destination.
  Child returns Result Packet to parent.
  Parent classifies child output as candidate evidence and synthesizes it.

Expected output:
  Child Launch Packet.
  Child Result Packet.
  Parent synthesis or missing result recovery.

Pass criteria:
  Child does not decide parent acceptance.
  Child does not mutate state.
  Child result returns to parent.

Fail conditions:
  Child launches future work.
  Child accepts parent result.
  Parent treats missing child as completed.

What must not happen:
  No child-level acceptance of parent target.
  No unrelated child chats for thoroughness.
  No lost return destination.

## Scenario 10 — capture off-scope user question into Action Inbox

Purpose:
  Check that useful off-scope input is preserved without derailing current work.

Starting condition:
  Current Work Chat is designing technical feasibility.

Input:
  User asks:
  "А как мы потом будем продвигать игру?"

Expected runtime behavior:
  ChatGPT identifies off-scope question.
  It creates candidate Action Inbox Item with reason, relation, priority, when_to_run or stale_condition.
  It continues current Work Contract unless user changes scope explicitly.

Expected output:
  Parked Action Inbox candidate.
  Current work continues.
  Next Move remains tied to current Work Contract.

Pass criteria:
  The marketing question is not lost.
  It is not executed now.
  It has relation and revisit condition.

Fail conditions:
  Chat jumps to marketing plan.
  Chat ignores the question completely.
  Action Inbox item has no reason or run condition.

What must not happen:
  No phase jump.
  No trash-bin item like "think later."
  No Action Inbox auto-execution.

## Scenario 11 — run Runtime Console status request

Purpose:
  Check that Runtime Console is read-only.

Starting condition:
  Direction has Direction Spine, Active Front, local Work Graph, open Action Inbox items and recent evidence.

Input:
  "Покажи статус."

Expected runtime behavior:
  Runtime Console summarizes current state, uncertainty, blockers, Action Inbox highlights and exact Next Move.
  It does not perform material work.
  It does not accept results.
  It does not mutate state.

Expected output:
  Read-only status view.
  Source limitations.
  Candidate Next Move or blocker.

Pass criteria:
  Console answers "what is going on?"
  It clearly says no material work started.
  It does not become a Work Chat.

Fail conditions:
  Console starts executing a node.
  Console launches Codex.
  Console accepts evidence.

What must not happen:
  No material work inside Runtime Console.
  No silent state mutation.
  No hidden controller behavior.

## Scenario 12 — failure recovery: GitHub unavailable / stale Project Files

Purpose:
  Check source authority behavior when exact repository state cannot be verified.

Starting condition:
  Material work requires repository files.

Input:
  GitHub read fails, or only stale Project Files are available.

Expected runtime behavior:
  ChatGPT states source_read limitation.
  It uses supplied excerpts only as classified context if sufficient.
  If exact state is material and unavailable, it returns blocked Result Packet.
  It may propose Check Job or Codex read-only source check.

Expected output:
  Blocked Result Packet or limited candidate result.
  Exact missing path/ref.
  Next Move to restore GitHub access, provide verified excerpts or run source Check Job.

Pass criteria:
  No repository state is guessed.
  Project Files are classified as cache/context.
  Limitation is visible.

Fail conditions:
  Stale Project Files are treated as truth.
  Chat claims latest repository state without verification.
  Missing source is ignored.

What must not happen:
  No false authority claim.
  No accepted state from uploaded cache.
  No broad context request when exact path/ref is known.

## Scenario 13 — failure recovery: Codex validation failed

Purpose:
  Check that failed validation blocks done claim.

Starting condition:
  Codex returns Result Packet with failed validation.

Input:
  "git diff --check failed" or required EOF marker missing.

Expected runtime behavior:
  ChatGPT classifies result as rejected_validation_failed or needs_codex_repair_same_package.
  It creates repair Next Move only within same allowed paths.
  It does not accept the result.

Expected output:
  Verification failure.
  Same-package repair package or rejection.
  Exact return destination.

Pass criteria:
  No done claim.
  Repair scope remains bounded.
  Failed validation is named.

Fail conditions:
  Chat says "mostly done."
  Repair package expands scope.
  Commit is treated as accepted despite failed checks.

What must not happen:
  No validation bypass.
  No forbidden path repair.
  No acceptance before passing evidence.

## Scenario 14 — failure recovery: missing child result

Purpose:
  Check parent recovery when child result is missing.

Starting condition:
  Parent / Integration Chat launched child chats.

Input:
  One child Result Packet is missing.

Expected runtime behavior:
  Parent does not synthesize as if all evidence returned.
  It produces Parent Recovery Block.
  It lists returned and missing child results.
  It gives Next Move to paste missing result, rerun child or narrow parent target.

Expected output:
  Parent Recovery Block.
  Missing child result list.
  Safe resume instruction.

Pass criteria:
  Missing evidence is explicit.
  Parent target remains bounded.
  User can resume in a new parent chat if needed.

Fail conditions:
  Parent pretends child completed.
  Parent accepts incomplete synthesis.
  Parent loses return destination.

What must not happen:
  No silent completion.
  No parent acceptance from incomplete child evidence.
  No unrelated continuation.

## Scenario 15 — handle handler flood / Action Inbox hygiene

Purpose:
  Check that Signals and Handlers do not flood Action Inbox.

Starting condition:
  Several Signals create duplicate or vague candidate actions.

Input:
  Handler creates ten similar items:
  "Check docs later", "Review maybe", "Think about setup", "Verify something."

Expected runtime behavior:
  Runtime triggers inbox_hygiene_handler.
  It merges duplicates, drops vague items, marks stale items and keeps only useful candidates.
  It does not auto-run items.

Expected output:
  Hygiene result.
  Kept / merged / dropped / superseded item list.
  Candidate Next Move only for selected useful item if needed.

Pass criteria:
  Every remaining item has reason, relation, priority and when_to_run or stale_condition.
  Action Inbox remains small and useful.
  Handler conditions can be tightened.

Fail conditions:
  Action Inbox becomes trash bin.
  Every warning becomes high priority.
  Items run automatically.

What must not happen:
  No automatic execution.
  No state mutation by Handler.
  No Action Inbox replacing Direction Spine or Work Graph.

## Stage 4 pilot verdict rule

These scenarios can support one of three candidate concept verdicts:

pass:
  The model is coherent enough for integration planning.

warn:
  The model is promising, but one or more weak areas need revision before integration planning.

fail:
  The model has blocker gaps and should be rejected or restarted.

A pass verdict does not activate runtime.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/PILOT_SCENARIOS.md
