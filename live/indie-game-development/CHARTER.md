# CHARTER — indie-game-development

## Mission

Build, ship, and commercialize a Steam indie game as a solo developer: a technically strong co-op game around gas + grid + expedition systems that the owner is proud to have made, and a real commercial product that generates external revenue.

The direction exists to create a reusable indie-development business seed: technical capability, product judgment, audience workflow, release discipline, and revenue—not only one isolated prototype.

## Success criteria

1. **Six-month money gate**
   - By 2026-12-11, the game has produced external paid validation tied to this project: donations, crowdfunding pledges, paid prototype access, publisher advance, grant, revenue share, Steam revenue, or another concrete cash commitment.
   - Recommended threshold for “real signal”: at least $1,000 gross external money or signed funding commitment.
   - Minimum owner-stated threshold: more than $0 external money.
   - If the result is $0 and no credible funding path exists, the commercial approach or concept must be reframed.

2. **Steam product outcome**
   - The game reaches Steam as a real product, not only a private prototype or tech demo.
   - Acceptable release paths: paid Early Access followed by 1.0, or direct 1.0 release.
   - The released product must have a public Steam page, trailer/gameplay footage, playable demo or equivalent public slice before launch, and a build that customers can actually play.

3. **Pride / craft bar**
   - The core game is not a gas simulation tech demo.
   - It demonstrates gameplay depth from the interaction of grid, destruction, gas types, gas reactions/transformations, expedition pressure, and player tools.
   - External co-op playtests can verify that gas behavior changes player tactics, creates readable emergent situations, and makes cooperation matter.

4. **Commercial success target**
   - Target commercial success: at least $100,000 gross lifetime revenue or funding attributable to the game and its direct commercial activity.
   - Minimum commercial floor before continuing into a larger multi-year push: the project recovers the initial cash budget and shows an active audience/funding path.
   - This target is calibrated against Steam’s visible success band where thousands of games exceed $100k annually, but most releases still disappear commercially.

## Constraints

- **Time:** the owner can dedicate roughly 80–90 hours/week because this is the primary work direction, not a side hobby.
- **Money:** new cash budget is capped at approximately $3,000 before explicit reconsideration; many plugins/tools are already purchased.
- **Health/rhythm:** high workload is accepted by the owner, but burnout remains a project risk. The OS should treat destroyed health, motivation, or execution reliability as failure pressure, not as “commitment.”
- **Audience gap:** the owner has little existing audience and low interest in manual social media. Audience development must be systematized through workflow, templates, checklists, automation where reasonable, and concrete recurring outputs.
- **Concept status:** `gas+grid / expedition` is the default concept foundation. It is not casually reopened. It can be challenged only by a dedicated audit with clear market/design evidence and a better alternative.
- **Archive status:** `archive/directions/indie-game-development/**` is evidence-only. Old material may be imported selectively only with an explicit reason and pointer. No blind migration.
- **Planning scope:** this frame creates the charter and root only. Goal map and archive analysis are separate map-session work.

## Lenses

1. **Commercial / traction lens**
   - Every major bet must say how it can create wishlists, followers, funding, publisher interest, paid validation, or sales.
   - Work that only improves internals without increasing player-facing proof must be justified.

2. **Core gameplay depth lens**
   - Gas/grid/destruction must produce decisions, risks, tools, and replayable situations.
   - A feature is not valuable merely because it is technically interesting.

3. **Co-op-first lens**
   - Multiplayer is not an add-on.
   - Design should create asymmetric responsibilities, communication, rescue/failure moments, shared planning, and expedition pressure.

4. **Technical feasibility lens**
   - Global gas simulation, destruction, networking, performance, determinism/sync, save/load, and tooling must be treated as first-class risks.
   - Technical ambition is allowed, but only behind playable evidence.

5. **Scope / production lens**
   - The product must stay solo-shippable.
   - Art, content, animation, UI, onboarding, and networking support cannot be assumed free.
   - Cuts are normal; uncontrolled feature expansion is failure.

6. **Audience workflow lens**
   - Because the owner lacks an existing audience, the project needs a repeatable external-output machine: gifs, clips, devlog fragments, playtest calls, Steam updates, mailing/community capture, and publisher/crowdfunding materials.
   - Social/manual posting should be minimized, batched, templated, or assisted.

## Owner edges

1. **Engineering depth**
   - Proving fact: 10 years of professional software development experience, mostly Java/full-stack, gives a strong base for architecture, systems thinking, tooling, debugging, and long technical execution.

2. **Availability and priority**
   - Proving fact: the owner is not currently splitting attention with a normal job and can devote roughly 80–90 hours/week to this direction.

3. **Player literacy**
   - Proving fact: lifelong broad game-playing experience gives taste references and intuitive understanding of what feels deep, shallow, boring, or alive.

4. **Existing concept investment**
   - Proving fact: prior work exists in archive and old code/docs around gas simulation, space/grid simulation, and the expedition concept. This is not imported automatically, but it is a real evidence source.

5. **OS-assisted solo workflow**
   - Proving fact: Direction OS can split work into frame/map/shape/work/review loops, preserve state, force done_when evidence, and compensate for solo blind spots with structured sessions.

## Risk posture

**guarded**

Rationale: the direction combines multiple high-risk dimensions—solo development, multiplayer, systemic simulation, Steam commercialization, no existing audience, and a six-month money gate. Exploration is still required, but the default posture must be guarded: early external validation, hard scope control, explicit kill/reframe gates, and no long private engineering tunnel.

## Canonical repos

- Direction state repo: `github.com/ainazemtsau/my_global_workflow`
- Product game repo: not yet canonized.
  - Candidate paths: continue the nearly empty current game repo, use the old repo with existing code, or start fresh.
  - Decision deferred to map/shape/technical audit; do not lock during frame.
- Website / marketing / Steam materials repo: none yet.

## Outside view

Steam success is possible but discoverability is brutal. 2025 data suggests many releases make almost no money, while thousands still cross $100k gross. Co-op/systemic outliers win through a legible fantasy, replayable social situations, community-facing proof, and a playable funnel—not by hiding for months behind technology. For this direction, sequencing should therefore run technical proof and commercial proof in parallel: prototype the gas+grid co-op core, but expose it early through Steam page/demo/playtests/funding experiments.

Reference cases used during frame:
- Steam release base-rate risk: many Steam releases earn little, while a meaningful minority crosses $100k gross.
- Deep Rock Galactic: co-op fantasy, roles, mission structure, procedural replay, and legible social hook.
- Abiotic Factor: co-op systemic/survival fantasy, early-access cadence, wishlist base, and community-facing development.
- Steam Next Fest / demos / Early Access: public-facing playable proof matters before launch; Early Access should not be used solely as a funding substitute.
- Kickstarter Games stats: crowdfunding can validate, but only with a strong proof-of-interest funnel.

## Pre-mortem

This direction failed three years from now because one or more of the following happened.

### 1. Six-month money gate was missed, but the project kept going as if nothing happened

**Failure mode:** by 2026-12-11 the game produced no external money, no signed funding commitment, and no credible path to near-term revenue, but the owner continued private development on momentum and sunk cost.

**Mitigation:** money validation must be treated as a real gate, not a motivational slogan. The project needs early commercial surfaces: Steam page, wishlist funnel, public clips, playable proof, crowdfunding/publisher/grant tests, and direct asks.

**Kill_by candidate:** by 2026-12-11, if external money is $0 and there is no concrete funding/revenue path with named next counterparty or platform, the commercial strategy or concept must be reframed before more production-scale work continues.

### 2. The project became a private engineering tunnel

**Failure mode:** months were spent improving gas simulation, grid architecture, destruction, networking, or tools, but there was no playable co-op proof that outsiders could understand or want.

**Mitigation:** technical work must frequently terminate in player-facing evidence: playable slices, gifs, videos, test scenarios, playtest builds, or Steam-facing materials. “The system is better internally” is insufficient unless it unlocks a visible gameplay result.

**Kill_by candidate:** if a major technical bet cannot produce a visible player-facing improvement within its appetite, cut or simplify the system rather than extending the bet.

### 3. Global gas simulation + destruction + multiplayer proved too expensive for solo production

**Failure mode:** the technical core became unsolo-shippable due to performance, synchronization, determinism, save/load complexity, debugging burden, or content/tooling overhead.

**Mitigation:** the game should prove the smallest commercially legible version of the fantasy before committing to full generality. Prefer constrained spaces, limited gas counts, authored expedition scenarios, simplified destruction, or local simulation boundaries if needed.

**Kill_by candidate:** if multiplayer gas/destruction cannot run reliably in a small representative scenario with acceptable performance and debuggability, the technical model must be narrowed before content production expands.

### 4. The gas/grid system was deep technically but shallow as gameplay

**Failure mode:** gases had types, reactions, transformations, and propagation, but players experienced them as noise, hazards, or gimmicks rather than meaningful decisions.

**Mitigation:** every core gas type needs a gameplay job: tactical choice, risk/reward, tool interaction, co-op role, route planning, emergency, resource, puzzle, combat pressure, or expedition consequence. Simulation complexity should be judged by decisions created, not variables simulated.

**Kill_by candidate:** if external playtesters cannot describe distinct gas behaviors and how those behaviors changed their decisions, the design must be simplified or redesigned.

### 5. Multiplayer existed technically but did not create cooperation

**Failure mode:** multiple players could run around together, but the optimal experience was still basically solo-with-friends. There were no strong reasons to communicate, split roles, rescue each other, coordinate tools, or plan expeditions.

**Mitigation:** co-op must be designed as a first-class system: asymmetric pressures, complementary tools, shared failure states, communication moments, role tension, rescue/recovery, and expedition logistics.

**Kill_by candidate:** if co-op playtests do not produce visible communication, dependency, or shared tactical planning, the core loop is not yet valid.

### 6. The concept was too illegible or too niche to sell

**Failure mode:** `gas+grid / expedition` made sense internally but did not produce a clear market-facing hook. Players, press, publishers, or backers saw it as a geeky systems toy rather than a game they wanted.

**Mitigation:** the concept must be packaged around a legible fantasy: dangerous expeditions, unstable environments, co-op survival/problem-solving, spectacular chain reactions, and memorable failure stories. Marketing language should lead with the player fantasy, not the simulation architecture.

**Kill_by candidate:** if store-page tests, trailer/gif feedback, playtest recruitment, or publisher/crowdfunding outreach produce persistent confusion or indifference, run a concept positioning audit before further expansion.

### 7. Audience development never became a workflow

**Failure mode:** because the owner dislikes social media and has no existing audience, marketing was postponed, under-posted, or done inconsistently. The game reached public launch with no wishlist base, no mailing/community capture, and no external momentum.

**Mitigation:** audience work must be turned into a repeatable production workflow: batched clips, templated devlog fragments, Steam updates, playtest calls, mailing list/community capture, short-form posts, press/publisher materials, and recurring review of what converts.

**Kill_by candidate:** if the project cannot produce a steady cadence of external artifacts from normal development, scope and workflow must be redesigned until marketing becomes a byproduct of work, not a separate personality tax.

### 8. Scope exploded across simulation, content, art, UX, networking, and release work

**Failure mode:** every system implied more tools, more content, more edge cases, more onboarding, more UI, more animation, more VFX, more balance, and more QA. The product became too large for one person.

**Mitigation:** the map and shape phases must cut aggressively. Content should reuse systemic depth instead of requiring large handcrafted volume. The product should be defined around a small number of high-leverage verbs, gases, tools, enemies/hazards, and mission structures.

**Kill_by candidate:** any shaped bet without a real cut list is invalid. If a feature cannot fit the current appetite, it must be parked, not silently absorbed.

### 9. The game made some money early, but the wrong signal was overinterpreted

**Failure mode:** a small donation, a few wishlists, a friendly publisher reply, or minor crowdfunding interest was treated as proof of market fit, leading to overcommitment.

**Mitigation:** separate “any money” from “strong signal.” The owner’s minimum is more than $0 by six months, but strategic decisions should look for stronger evidence: repeat strangers, wishlist velocity, playtest retention, conversion intent, publisher terms, crowdfunding prelaunch followers, or meaningful gross revenue.

**Accepted risk:** early money is still useful morale and validation. The risk is accepted only if the OS continues to distinguish weak signal from strong signal.

### 10. The old archive became a sunk-cost trap

**Failure mode:** prior documents, old code, and earlier decisions were imported because they existed, not because they still served the new direction.

**Mitigation:** archive material is evidence-only. Every imported item must name the reason it still matters: saves time, proves a technical path, captures a validated decision, or prevents repeating a known failure.

**Kill_by candidate:** if archive review starts turning into migration rather than selection, stop and run a bounded map/audit session with explicit import criteria.

### 11. The owner lost pride in the project while chasing revenue

**Failure mode:** commercial pressure pushed the game toward trend-chasing, shallow content, or mechanics the owner did not respect. Motivation collapsed because the project no longer felt worth making.

**Mitigation:** commercial work should improve packaging, validation, scope, and audience fit—not force the owner to build a game he considers garbage. The craft bar remains a hard constraint.

**Accepted risk:** some commercially attractive options will be rejected if they destroy owner pride. This is accepted because pride is one of the two equal pillars of the direction.

### 12. High workload damaged execution reliability

**Failure mode:** 80–90 hours/week turned into cognitive fatigue, poor judgment, avoidant loops, or inability to finish. Because crunch was framed as passion, warning signs were ignored.

**Mitigation:** the OS should judge by evidence, not hours. If output quality, decision quality, sleep, mood, or execution reliability degrades, reduce scope or change cadence rather than treating more hours as the answer.

**Accepted risk:** high workload is part of the owner’s current strategy. It is accepted only while it produces stable, verifiable progress and does not destroy the ability to ship.

END_OF_FILE: live/indie-game-development/CHARTER.md
