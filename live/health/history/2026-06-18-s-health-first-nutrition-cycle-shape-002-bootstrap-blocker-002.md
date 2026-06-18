RESULT s-health-first-nutrition-cycle-shape-002-bootstrap-blocker-002 (call: c-health-first-nutrition-cycle-shape-002)
direction: health   play: shape   node/task: g-health-first-nutrition-cycle

outcome: |
  g-health-first-nutrition-cycle was not shaped or approved. The session stopped before appetite approval because
  the owner identified a higher-priority trust/blocker defect in the Health AI provider/client carrier surface.

  The blocker is not only "missing ChatGPT Project instructions". The real defect is that the owner cannot trust
  the Health AI startup path until the repo proves an end-to-end provider/client journey:
  - ChatGPT Project can be created from repo-owned instructions.
  - The project uses ainazemtsau/health-ai as source of truth instead of stale uploaded snapshots.
  - Claude/Codex/Claude Code converge on the same repo-owned contract.
  - A normal owner message such as "Хочу начать питание" routes through the nutrition workflow correctly.
  - The expected owner journey is documented in enough detail to audit whether the rest of Health AI is coherent:
    first startup, first days, day-3 safety/friction check, day-8 review, multiple-week continuation, new recipe
    flow, personalization from feedback, writer handoff, and failure/repair routing.

  Therefore this shape session closes as blocked/redirected. The next action is a health-ai executor repair that
  adds/fixes the durable bootstrap surface and produces an owner-readable end-to-end journey proof, then a fresh
  review/refutation session must verify it before the owner treats the setup as accepted.

evidence: |
  Direction state read:
  - live/health/CHARTER.md
  - live/health/TREE.md
  - live/health/NOW.md
  - live/health/knowledge/health-nutrition-workflow-authority-g5-review.md

  Product evidence inspected:
  - health-ai/SYSTEM.md exists as "SYSTEM - Portable Health AI Prompt" and says Health AI is provider-independent,
    owner speaks normally, and durable state lives in Markdown/YAML files in git.
  - health-ai/AGENTS.md exists as canonical operating contract across ChatGPT, Claude, Claude Code, Codex, and
    other LLM surfaces.
  - health-ai/CLAUDE.md exists only as a Claude pointer to AGENTS.md.
  - health-ai/x_nutrition/index.md lists nutrition load order and active artifacts.
  - health-ai/x_nutrition/state/current-workflow.md sets current_state STARTUP_ROUTER and requires graph/router
    validation before output-heavy nutrition artifacts.
  - Direction OS review evidence accepted WG1-WG14/WGA0-WGA15 workflow authority, but that review did not prove
    a complete owner-facing ChatGPT Project setup/journey from project creation to multi-week nutrition use.

  Owner evidence:
  - Owner rejected ad-hoc chat bootstrap and required the setup to live in GitHub:
    "должно быть в гитхабе ... что мне к тебе ... бегать, спрашивать каждый раз, какой bootstrap должен быть".
  - Owner explicitly required a detailed expected user journey because trust is currently broken:
    "детальнейший пример ... user journey от начала до конца ... сначала несколько дней, потом ... несколько недель,
    как новый рецепт, как персонализация под юзера".

state_changes: |
  Apply the following exact Direction OS state changes.

  1) live/health/NOW.md
  - Replace active_bet with:
      status: none
      note: >
        No active bet. The workflow authority gate bet met review/refutation in
        s-health-nutrition-workflow-authority-review-004 on 2026-06-18:
        health-ai graph/current-workflow/router/writer validation passed WG1-WG14
        and WGA0-WGA15 checks with blocker_gaps=0, and no nutrition execution
        content was introduced. First nutrition-cycle shape was stopped before
        approval because the owner identified a higher-priority trust/blocker
        defect: Health AI must expose a durable repo-backed ChatGPT Project /
        Claude / Codex startup surface and an end-to-end owner journey proof
        from repo, not an ad-hoc bootstrap invented in chat. Next is health-ai
        bootstrap + journey repair.

  - Replace tasks with: []

  - Replace open_calls with: []

  - Keep recurring: []

  - Replace decisions with: []

  - Replace next with:
      CALL c-health-ai-project-bootstrap-e2e-repair-001
      to: executor
      direction: health
      repo: ainazemtsau/health-ai
      kind: engineering
      node: g-health-nutrition-system
      goal: |
        Health AI has a durable repo-backed provider/client startup surface and
        end-to-end owner journey proof: ChatGPT Project, Claude, Claude Code, and
        Codex can all start from ainazemtsau/health-ai, use current repo files as
        source of truth, route normal owner messages through the nutrition workflow,
        and demonstrate the expected first-days and multi-week nutrition journey
        without ad-hoc prompt text invented in chat, stale uploaded-file snapshots,
        or manual Direction OS packet formats from the owner.
      context: |
        Problem found during c-health-first-nutrition-cycle-shape-002:
        the owner wanted to create/use a ChatGPT Project for Health AI and start
        with a normal message. The session initially produced ad-hoc Project
        Instructions in chat and then a file-upload fallback. Owner rejected this
        correctly: Health AI is supposed to work through GitHub/repo state, so the
        bootstrap must be durable, repo-owned, provider/client-aware, and not require
        the owner to return to a chat to ask what to paste.

        Trust issue:
        This is not only a missing setup file. The owner no longer trusts that the
        rest of the Health AI nutrition workflow is coherent. The repair must include
        a detailed owner-readable end-to-end journey example showing how the system is
        expected to work across:
        - ChatGPT Project creation/setup from repo-owned instructions.
        - First normal owner message.
        - Startup router/current-workflow behavior.
        - Initial minimal questions.
        - First day of nutrition.
        - Day-2 continuation.
        - Day-3 safety/friction check.
        - Days 4-8 continuation.
        - Day-8 review.
        - Weeks 2-4 continuation/mutation.
        - New recipe request/intake.
        - Personalization from feedback and adherence.
        - Fallback meal usage.
        - Writer handoff when the current surface cannot write to repo.
        - Failure modes and repair routing.

        Current product evidence:
        - SYSTEM.md: portable Health AI prompt.
        - AGENTS.md: canonical operating contract for ChatGPT, Claude, Claude Code,
          Codex, and other LLM surfaces.
        - CLAUDE.md: Claude-specific pointer to AGENTS.md, not a separate fork.
        - x_nutrition/index.md: nutrition setup/continuation load order and active
          artifacts.
        - x_nutrition/workflow/graph.md
        - x_nutrition/state/current-workflow.md
        - x_nutrition/procedures/workflow-router.md
        - x_nutrition/procedures/provider-continuation.md
        - x_nutrition/procedures/writer-handoff.md
        - acceptance/x_nutrition/provider-continuation-matrix.json
        - tools/check_nutrition_continuation.py

        Direction OS accepted fact:
        - live/health/knowledge/health-nutrition-workflow-authority-g5-review.md:
          workflow authority review passed on 2026-06-18 with WG1-WG14 and
          WGA0-WGA15 checks, blocker_gaps=0.

        Required repair intent:
        - Do not create another chat-only bootstrap.
        - Make ChatGPT Project setup a repo-owned artifact.
        - Make the setup point to ainazemtsau/health-ai as source of truth.
        - Preserve provider independence: ChatGPT Project, Claude, Claude Code,
          and Codex must converge on repo files, not hidden provider memory.
        - Prove the owner-facing journey with a detailed synthetic example.
        - The owner must be able to start with a normal message like:
          "Хочу начать питание. Проведи меня с нуля до первого рабочего плана."
      boundaries: |
        Do not start real owner nutrition execution.
        Do not create real owner menus, real owner grocery lists, real owner shopping
        instructions, real owner daily plans, or real owner food logs.
        Synthetic examples/fixtures are allowed only if clearly marked as synthetic,
        non-authoritative journey proof and not to be followed as the owner's actual
        nutrition plan.
        Do not move into training/activity implementation.
        Do not rewrite g-health-core or redefine core-owned concepts.
        Do not add app UI, runtime, DB, server, cron, scheduler, or background worker.
        Do not edit Direction OS repo files from this executor.
        Do not make uploaded stale snapshots the normal ChatGPT Project path when
        GitHub/repo access is available.
        Do not ask the owner to choose expert nutrition variables.
        Do not make medical diagnoses or prescriptions.
      allowed_files_or_surfaces: |
        You may edit or add only the carrier/bootstrap/journey/validation surfaces
        needed for this repair:
        - SYSTEM.md
        - AGENTS.md
        - CLAUDE.md
        - README.md if present
        - new repo-owned ChatGPT Project setup/entrypoint doc, recommended:
          CHATGPT_PROJECT.md
        - new owner journey proof doc, recommended:
          docs/owner-journeys/chatgpt-project-nutrition-e2e.md
          or x_nutrition/handoffs/chatgpt-project-nutrition-e2e.md
        - x_nutrition/index.md only if needed to point to the repo-owned project
          bootstrap/journey/load order without changing nutrition semantics
        - x_nutrition/procedures/provider-continuation.md only if needed to clarify
          ChatGPT Project / GitHub-connected continuation behavior
        - x_nutrition/procedures/writer-handoff.md only if needed to clarify
          non-code chat -> writer packet -> repo commit -> continuation
        - acceptance/x_nutrition/provider-continuation-matrix.json
        - tools/check_nutrition_continuation.py
        - optionally a new focused check such as tools/check_project_bootstrap.py
        - minimal synthetic fixtures/examples required by those checks

        If the executor finds a contradiction outside these surfaces that prevents
        the repair from being truthful, stop and return STUCK with exact files and
        contradiction. Do not silently widen scope and do not paper over it with prose.
      mandatory_investigation: |
        Before editing, inspect the existing provider/client carrier surfaces and
        classify the defect explicitly in the executor RESULT:
        - missing repo-owned ChatGPT Project entrypoint;
        - insufficient SYSTEM/AGENTS/CLAUDE load-order clarity;
        - insufficient validation/acceptance coverage;
        - insufficient owner-facing end-to-end journey proof;
        - broader contradiction in nutrition continuation semantics.

        If the issue is broader than bootstrap/journey, the executor must not claim
        the repair is complete. It must return blocker_gaps with the next repair CALL.
      mandatory_owner_journey_artifact: |
        Add or update a repo-owned owner-readable journey document. It must be detailed
        enough that the owner can judge whether the Health AI nutrition workflow is
        coherent.

        The journey document must include at least these sections:

        1. Setup from zero:
           - ChatGPT Project creation.
           - What exact Project Instructions are used or where they are copied from.
           - How GitHub/repo source of truth is established.
           - What happens if the current chat surface has no repo access.
           - Why uploaded files are not the normal path.

        2. First message:
           - Owner writes a normal message, e.g.
             "Хочу начать питание. Проведи меня с нуля до первого рабочего плана."
           - Expected Health AI behavior.
           - No CALL, RESULT, JSON, fixed form, colon fields, or Direction OS packet
             demanded from owner.

        3. Startup routing:
           - Health AI loads SYSTEM.md, AGENTS.md, core/index.md, x_nutrition/index.md.
           - Nutrition startup routes through workflow graph, current-workflow cursor,
             and workflow-router before output-heavy artifacts.
           - Explain in owner language why active menu/cycle files are seeds until
             the router selects one state/artifact family.

        4. First setup conversation:
           - Minimal questions Health AI may ask.
           - Which facts are irreducible owner facts.
           - Which variables Health AI decides itself.
           - What reduced mode looks like if a fact is missing.

        5. First 3 days:
           - Day 1: how owner receives the first bounded action and logs loosely.
           - Day 2: how messy text/photo input is parsed without forcing a template.
           - Day 3: safety/friction check and possible conservative branch.
           - Include synthetic transcript snippets and expected repo/write outcome.

        6. Days 4-8:
           - How continuation works.
           - How fallback food is used.
           - How hunger, energy, adherence, and practical friction affect adjustment.
           - What Health AI stores in its nutrition LOG vs what must not go to
             Direction OS.

        7. Day-8 review:
           - What gets reviewed.
           - How summary/decision/problem is separated from raw diary.
           - How mutation is proposed.

        8. Weeks 2-4:
           - How the next cycle begins.
           - How personalization accumulates from feedback.
           - How a repeated failure changes the plan.
           - How weight trend / adherence / biofeedback influence changes without
             turning into medical diagnosis.

        9. New recipe flow:
           - Owner asks for a new recipe.
           - Health AI checks constraints, preferences, effort level, protein/satiety,
             existing menu/fallback fit.
           - Health AI proposes or files a recipe change through the correct writer path.
           - Synthetic example must show how the recipe becomes a candidate, accepted
             recipe, fallback, or rejected idea.

        10. Provider/client handoff:
            - ChatGPT Project with repo access.
            - ChatGPT Project without repo write access.
            - Codex or Claude Code as writer.
            - Claude/Claude Code loading via CLAUDE.md -> AGENTS.md.
            - What packet or commit is produced.
            - How a fresh chat resumes from repo state.

        11. Failure modes:
            - Chat cannot read repo.
            - Chat emits output-heavy menu before router.
            - Chat asks owner to choose expert variables.
            - Chat tries to write raw daily diary into Direction OS.
            - Cursor/graph mismatch.
            - Stale uploaded file snapshot used as authority.
            - For each: expected block/repair behavior.
      done_when: |
        A committed health-ai repair exists such that:

        1. The repo contains a durable ChatGPT Project entrypoint, recommended
           `CHATGPT_PROJECT.md`, with exact setup instructions and either:
           - exact copy-paste Project Instructions owned by the repo; or
           - a precise minimal bootstrap that points the Project at
             ainazemtsau/health-ai as source of truth and then loads SYSTEM.md /
             AGENTS.md from repo.
           The artifact must not rely on ad-hoc chat text.

        2. The ChatGPT Project entrypoint clearly distinguishes:
           - normal path: GitHub/repo-connected source of truth;
           - reduced/no-repo path: do not claim durable state changed; route to writer
             packet or Codex/Claude Code;
           - manual uploaded snapshots: allowed only as temporary degraded fallback,
             never the accepted normal workflow.

        3. SYSTEM.md, AGENTS.md, CLAUDE.md, and the ChatGPT Project entrypoint have
           a non-contradictory provider/client load order:
           - ChatGPT Project: project bootstrap -> GitHub repo -> SYSTEM.md ->
             AGENTS.md -> core/index.md -> x_nutrition/index.md for nutrition work.
           - Claude: CLAUDE.md -> AGENTS.md.
           - Codex/Claude Code: repo root -> AGENTS.md.
           - Nutrition startup/continuation: x_nutrition/index.md -> workflow graph
             + current-workflow + workflow-router before output-heavy artifacts.

        4. Owner-facing startup remains normal-language:
           the owner can type "Хочу начать питание" and must not provide CALL,
           RESULT, JSON, colon fields, fixed LOG templates, or Direction OS packet
           formats.

        5. The repo contains the mandatory owner journey artifact described above.
           It must show the expected journey from zero setup through first days,
           day-8 review, weeks 2-4, new recipe flow, personalization, provider/client
           handoff, and failure modes. It must be detailed, owner-readable, and
           explicitly marked synthetic/non-authoritative where it includes example
           food/log content.

        6. Nutrition startup still routes through:
           - x_nutrition/workflow/graph.md
           - x_nutrition/state/current-workflow.md
           - x_nutrition/procedures/workflow-router.md
           before output-heavy nutrition artifacts.

        7. Validation is strengthened so this defect cannot silently return:
           existing checks pass, and at minimum tools/check_nutrition_continuation.py
           or a new focused check fails if:
           - the repo lacks the ChatGPT Project bootstrap/entrypoint;
           - the bootstrap tells the owner to use stale uploaded snapshots as the
             default path when GitHub/repo access is available;
           - the bootstrap omits SYSTEM.md/AGENTS.md/core/index.md/x_nutrition/index.md
             load order;
           - the journey artifact is missing;
           - owner-facing startup requires CALL/RESULT/JSON/fixed templates;
           - startup can emit menu/recipe/grocery/daily_plan/raw_log before router.

        8. The executor runs relevant checks and reports exact commands/output.
           Required minimum:
           - python tools/check_acceptance_matrix.py
           - python tools/check_core_slice.py
           - python tools/check_core_evidence.py
           - python tools/check_nutrition_research_setup.py
           - python tools/check_nutrition_full_module.py
           - python tools/check_nutrition_continuation.py
           - plus any new bootstrap/journey check if added.

        9. The executor RESULT includes:
           - commit SHA;
           - changed files;
           - check commands and outputs;
           - blocker_gaps count;
           - explicit defect classification from mandatory_investigation;
           - path to ChatGPT Project entrypoint;
           - path to owner journey artifact;
           - a readable excerpt/summary of the end-to-end journey for owner review;
           - a ready fresh review CALL to verify the repair by refutation.
      return: |
        RESULT from executor with commit SHA, changed files, check output, blocker_gaps,
        defect classification, ChatGPT Project entrypoint path, owner journey artifact
        path, owner-readable journey summary/excerpt, and a ready review/refutation CALL.

        If the executor finds that the defect is broader than bootstrap/journey and
        cannot be fixed within allowed surfaces, return STUCK with exact blockers,
        exact files, and recommended next repair CALL. Do not produce a fake pass.
      budget: one focused half-day

  2) live/health/TREE.md
  - No change.

  3) live/health/LOG.md
  - Append:
      2026-06-18 — health/g-health-first-nutrition-cycle shape: first nutrition-cycle shape stopped before approval; owner identified health-ai repo bootstrap/carrier trust defect; next executor repair must add repo-backed ChatGPT Project/Claude/Codex startup plus detailed owner end-to-end nutrition journey proof. → history/2026-06-18-s-health-first-nutrition-cycle-shape-002-bootstrap-blocker-002.md

  4) live/health/history/
  - Save this full RESULT as:
      live/health/history/2026-06-18-s-health-first-nutrition-cycle-shape-002-bootstrap-blocker-002.md

captures:
  - After bootstrap + journey repair, run a fresh review/refutation before treating ChatGPT Project setup as accepted owner path.
  - If repair reveals broader contradiction in SYSTEM.md/AGENTS.md/CLAUDE.md/x_nutrition continuation semantics, escalate to provider-continuation repair instead of starting nutrition execution.
  - Owner trust bar for Health AI is now proof-by-journey, not prose claims that the system is provider-independent.

decisions_needed: []

play_check:
  - 1 Recite: done; node goal/done_when and parent/root relation were restated before the owner redirected.
  - 2 Appetite first: blocked; no appetite was approved because owner redirected from first-cycle shaping to bootstrap/carrier repair.
  - 3 Approaches, then minimal solution: skipped because the owner identified a prerequisite trust/blocker defect; producing approaches for the nutrition cycle would bypass the defect.
  - 4 Scope hammer: skipped for the nutrition-cycle bet because no bet is being shaped; repair scope is carried in the next executor CALL with explicit allowed surfaces and boundaries.
  - 5 Lens sweep: skipped because this session closes as blocked/redirected, not as an approved shape.
  - 6 Riskiest assumption: done as redirect finding; top risk is that Health AI provider/client startup and owner journey are not actually durable and coherent from repo.
  - 7 Tasks: skipped for the nutrition-cycle bet; instead a single bounded executor repair CALL is emitted.
  - 8 Kill criteria: skipped because no nutrition-cycle bet is approved.
  - 9 Close: done as blocked checkpoint; owner rejected ad-hoc bootstrap and required repo-owned setup plus detailed journey proof: "должно быть в гитхабе" and "детальнейший пример ... user journey от начала до конца".

log: health/g-health-first-nutrition-cycle shape: stopped before approval; owner identified health-ai repo bootstrap/carrier trust defect; next executor repair must add repo-backed ChatGPT Project/Claude/Codex startup plus detailed owner end-to-end nutrition journey proof.

next: |
  CALL c-health-ai-project-bootstrap-e2e-repair-001
  to: executor
  direction: health
  repo: ainazemtsau/health-ai
  kind: engineering
  node: g-health-nutrition-system
  goal: |
    Health AI has a durable repo-backed provider/client startup surface and
    end-to-end owner journey proof: ChatGPT Project, Claude, Claude Code, and
    Codex can all start from ainazemtsau/health-ai, use current repo files as
    source of truth, route normal owner messages through the nutrition workflow,
    and demonstrate the expected first-days and multi-week nutrition journey
    without ad-hoc prompt text invented in chat, stale uploaded-file snapshots,
    or manual Direction OS packet formats from the owner.
  context: |
    Problem found during c-health-first-nutrition-cycle-shape-002:
    the owner wanted to create/use a ChatGPT Project for Health AI and start
    with a normal message. The session initially produced ad-hoc Project
    Instructions in chat and then a file-upload fallback. Owner rejected this
    correctly: Health AI is supposed to work through GitHub/repo state, so the
    bootstrap must be durable, repo-owned, provider/client-aware, and not require
    the owner to return to a chat to ask what to paste.

    Trust issue:
    This is not only a missing setup file. The owner no longer trusts that the
    rest of the Health AI nutrition workflow is coherent. The repair must include
    a detailed owner-readable end-to-end journey example showing how the system is
    expected to work across:
    - ChatGPT Project creation/setup from repo-owned instructions.
    - First normal owner message.
    - Startup router/current-workflow behavior.
    - Initial minimal questions.
    - First day of nutrition.
    - Day-2 continuation.
    - Day-3 safety/friction check.
    - Days 4-8 continuation.
    - Day-8 review.
    - Weeks 2-4 continuation/mutation.
    - New recipe request/intake.
    - Personalization from feedback and adherence.
    - Fallback meal usage.
    - Writer handoff when the current surface cannot write to repo.
    - Failure modes and repair routing.

    Current product evidence:
    - SYSTEM.md: portable Health AI prompt.
    - AGENTS.md: canonical operating contract for ChatGPT, Claude, Claude Code,
      Codex, and other LLM surfaces.
    - CLAUDE.md: Claude-specific pointer to AGENTS.md, not a separate fork.
    - x_nutrition/index.md: nutrition setup/continuation load order and active
      artifacts.
    - x_nutrition/workflow/graph.md
    - x_nutrition/state/current-workflow.md
    - x_nutrition/procedures/workflow-router.md
    - x_nutrition/procedures/provider-continuation.md
    - x_nutrition/procedures/writer-handoff.md
    - acceptance/x_nutrition/provider-continuation-matrix.json
    - tools/check_nutrition_continuation.py

    Direction OS accepted fact:
    - live/health/knowledge/health-nutrition-workflow-authority-g5-review.md:
      workflow authority review passed on 2026-06-18 with WG1-WG14 and WGA0-WGA15
      checks, blocker_gaps=0.
  boundaries: |
    Do not start real owner nutrition execution.
    Do not create real owner menus, real owner grocery lists, real owner shopping
    instructions, real owner daily plans, or real owner food logs.
    Synthetic examples/fixtures are allowed only if clearly marked as synthetic,
    non-authoritative journey proof and not to be followed as the owner's actual
    nutrition plan.
    Do not move into training/activity implementation.
    Do not rewrite g-health-core or redefine core-owned concepts.
    Do not add app UI, runtime, DB, server, cron, scheduler, or background worker.
    Do not edit Direction OS repo files from this executor.
    Do not make uploaded stale snapshots the normal ChatGPT Project path when
    GitHub/repo access is available.
    Do not ask the owner to choose expert nutrition variables.
    Do not make medical diagnoses or prescriptions.
  allowed_files_or_surfaces: |
    You may edit or add only the carrier/bootstrap/journey/validation surfaces
    needed for this repair:
    - SYSTEM.md
    - AGENTS.md
    - CLAUDE.md
    - README.md if present
    - new repo-owned ChatGPT Project setup/entrypoint doc, recommended:
      CHATGPT_PROJECT.md
    - new owner journey proof doc, recommended:
      docs/owner-journeys/chatgpt-project-nutrition-e2e.md
      or x_nutrition/handoffs/chatgpt-project-nutrition-e2e.md
    - x_nutrition/index.md only if needed to point to the repo-owned project
      bootstrap/journey/load order without changing nutrition semantics
    - x_nutrition/procedures/provider-continuation.md only if needed to clarify
      ChatGPT Project / GitHub-connected continuation behavior
    - x_nutrition/procedures/writer-handoff.md only if needed to clarify
      non-code chat -> writer packet -> repo commit -> continuation
    - acceptance/x_nutrition/provider-continuation-matrix.json
    - tools/check_nutrition_continuation.py
    - optionally a new focused check such as tools/check_project_bootstrap.py
    - minimal synthetic fixtures/examples required by those checks

    If the executor finds a contradiction outside these surfaces that prevents
    the repair from being truthful, stop and return STUCK with exact files and
    contradiction. Do not silently widen scope and do not paper over it with prose.
  mandatory_investigation: |
    Before editing, inspect the existing provider/client carrier surfaces and
    classify the defect explicitly in the executor RESULT:
    - missing repo-owned ChatGPT Project entrypoint;
    - insufficient SYSTEM/AGENTS/CLAUDE load-order clarity;
    - insufficient validation/acceptance coverage;
    - insufficient owner-facing end-to-end journey proof;
    - broader contradiction in nutrition continuation semantics.

    If the issue is broader than bootstrap/journey, the executor must not claim
    the repair is complete. It must return blocker_gaps with the next repair CALL.
  mandatory_owner_journey_artifact: |
    Add or update a repo-owned owner-readable journey document. It must be detailed
    enough that the owner can judge whether the Health AI nutrition workflow is
    coherent.

    The journey document must include at least these sections:
    1. Setup from zero.
    2. First normal owner message.
    3. Startup routing.
    4. First setup conversation.
    5. First 3 days.
    6. Days 4-8.
    7. Day-8 review.
    8. Weeks 2-4.
    9. New recipe flow.
    10. Provider/client handoff.
    11. Failure modes.
  done_when: |
    A committed health-ai repair exists such that:
    1. The repo contains a durable ChatGPT Project entrypoint, recommended
       `CHATGPT_PROJECT.md`, with exact setup instructions and either exact
       copy-paste Project Instructions owned by the repo or a precise minimal
       bootstrap that points the Project at ainazemtsau/health-ai as source of
       truth and then loads SYSTEM.md / AGENTS.md from repo.
    2. The ChatGPT Project entrypoint clearly distinguishes normal GitHub/repo path,
       reduced/no-repo path, and manual snapshot fallback as degraded only.
    3. SYSTEM.md, AGENTS.md, CLAUDE.md, and the ChatGPT Project entrypoint have a
       non-contradictory provider/client load order.
    4. Owner-facing startup remains normal-language and does not require CALL,
       RESULT, JSON, colon fields, fixed LOG templates, or Direction OS packets.
    5. The repo contains the mandatory owner journey artifact showing setup,
       first days, day-8 review, weeks 2-4, new recipe flow, personalization,
       provider/client handoff, and failure modes.
    6. Nutrition startup still routes through workflow graph, current-workflow,
       and workflow-router before output-heavy nutrition artifacts.
    7. Validation fails if bootstrap/journey/load-order/no-stale-snapshot guarantees
       are missing.
    8. Existing checks and any new bootstrap check pass.
    9. Executor RESULT includes commit SHA, changed files, check output,
       blocker_gaps, defect classification, entrypoint path, journey path,
       owner-readable journey summary/excerpt, and ready fresh review CALL.
  return: |
    RESULT from executor with commit SHA, changed files, check output, blocker_gaps,
    defect classification, ChatGPT Project entrypoint path, owner journey artifact
    path, owner-readable journey summary/excerpt, and a ready review/refutation CALL.

    If the executor finds that the defect is broader than bootstrap/journey and
    cannot be fixed within allowed surfaces, return STUCK with exact blockers,
    exact files, and recommended next repair CALL. Do not produce a fake pass.
  budget: one focused half-day

END_OF_FILE: live/health/history/2026-06-18-s-health-first-nutrition-cycle-shape-002-bootstrap-blocker-002.md
