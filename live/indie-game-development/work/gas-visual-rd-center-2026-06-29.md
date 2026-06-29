# Gas-Visual R&D Center — read-only research loop

Direction: `indie-game-development`
Track: `g-7e15` VISUAL / GASG
Created: 2026-06-29

This center is a read-only Codex-side research lab for the gas visual track: it studies technologies, references, and visual mechanisms that can make gas the game's heart/jewel, while Claude Code continues implementation in the product repo.

It is NOT a second builder and NOT a replacement for the current build leg. The active build path remains `c-visual-002` in GasCoopGame_dev_2, using `GasCoopGame docs/gas-visual-stage-plan.md §S6+`.

## 1. Mission

Find practical ways for the gas to become:

- visually impressive enough to sell the game's fantasy in clips;
- readable enough for gameplay without debug overlays;
- characterful per gas type, not just recolored;
- compatible with the locked read-only visual architecture over the authoritative integer grid;
- small enough for a solo developer and the current Unity/URP pipeline.

Owner target, carried from `s-visual-005`: gas = the game's HEART / JEWEL; it should look especially cool and unique. Low-poly is the world style, not a ceiling on gas quality.

## 2. Hard boundaries

The center may:

- read OS state, visual-track history, product docs, screenshots/videos, code, Unity docs, papers, assets, plugins, and reference media;
- compare technologies and propose small probes;
- produce research notes, decision briefs, and executor-call input;
- challenge a current visual approach if evidence shows a better path.

The center must NOT:

- edit GasCoopGame code, scenes, assets, materials, shaders, packages, or branches;
- ask Claude Code to change direction without a routed CALL / owner decision;
- move the authoritative gas truth out of the sim;
- propose Zibra/Obi/other live fluid solvers as the core gas body unless the owner explicitly reopens architecture;
- let a cosmetic effect create gameplay truth, danger truth, or network-relevant state;
- treat a pretty demo as sufficient if it cannot read our grid or be reduced to a cheap proof.

Any idea that needs implementation returns as a probe brief or capture. It does not become code in this chat.

## 3. Operating loop

One R&D pass = one bounded question.

1. Frame one question.
2. Gather sources and references.
3. Test against our constraints: read-only seam, URP, gas-lab, owner-eye jewel gate, solo-dev cost.
4. Return one technology card or one shortlist.
5. Recommend: `probe now`, `watch`, `drop`, or `needs owner decision`.

The output should be useful to either:

- the owner, for taste/direction decisions;
- Claude Code, as bounded input for a future PLAN;
- the OS track, as captures/decisions for `g-7e15`.

## 4. Technology card template

Use this shape for each technology or visual mechanism:

```markdown
## Card: <name>

Question:
What exact visual problem does this answer?

Jewel payoff:
What would become more impressive, memorable, or clip-worthy?

Fit with our architecture:
- Reads GridView / GasParams / WarningEvents?
- Requires new buffer/layout?
- Cosmetic-only or danger/readability-critical?
- URP-compatible?

Implementation sketch (non-binding):
The smallest plausible way Claude Code could probe it.

Cheapest proof:
What can be shown in 30-90 minutes or one small build leg?

Falsifier:
What result means we drop it?

Risks:
Performance, readability, pipeline, solo-dev complexity, asset dependency, licensing.

Sources / references:
Links, docs, papers, screenshots, games, plugins.

Verdict:
probe now | watch | drop | owner decision
```

## 5. Scoring rubric

Score 0-3, then use judgment. A low total can still win if it solves a critical visual gap.

| Axis | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Jewel payoff | invisible / generic | minor polish | clearly better | clip-worthy / signature |
| Read-only fit | breaks truth | awkward bridge | fits with care | natural GridView/Event read |
| Readability | obscures gameplay | unclear | readable with tuning | improves danger/type/front read |
| Solo-dev cost | large system | medium feature | small feature | tiny probe |
| Performance risk | unknown/high | heavy but tunable | likely manageable | cheap/default-off |
| Uniqueness | stock | common | distinctive combo | strong identity |
| Claude handoff | vague | needs design work | clear probe | near-CALL-ready |

Default recommendation thresholds:

- `probe now`: high jewel payoff, good read-only fit, cheap proof.
- `watch`: promising but too wide, too expensive, or waiting on current build evidence.
- `drop`: breaks architecture, mostly marketplace magic, unreadable, or expensive for generic results.
- `owner decision`: changes aesthetic direction, license/cost, pipeline, or architecture.

## 6. Initial R&D queues

### Queue A — immediate support for c-visual-002

These help the live look-development leg without changing its scope.

1. **Gas-lab composition audit**
   What lighting/camera/background makes open-space gas evaluable instead of box-scene-misleading?

2. **Body shader upgrade pack**
   Which shader levers make the existing raymarch look expensive: blue-noise/jitter, erosion, transmittance, glow, depth-front reconstruction, camera-inside clamp, color grading?

3. **Jewel gate checklist**
   A tiny owner-eye checklist for "moves toward the jewel" so slices do not pass only on legibility.

### Queue B — next likely probes

1. **Front/accent layer over GridView**
   Compare VFX Graph GraphicsBuffer sampling, classic ParticleSystem + force fields, custom instanced quads/tubes, and shader-only front streaks. Goal: tendrils, wisps, jet streaks, suction lines, reaction sparks.

2. **Per-type character grammar**
   Define how gases differ by motion/noise/light/erosion/silhouette, not just hue. Output: 3-5 character archetypes and which fields must live in data.

3. **Event-drama layer**
   Danger/reaction telegraphs: decals, light pulses, screen-space distortion, pooled bursts, audio hooks. Must stay event-driven, not idle noise.

4. **Hero/special gas module**
   One flagship anomalous gas with a bespoke visual behavior: floor creep, reaching tendrils, crystalline fog, living glass-like pulses, or oppressive glow. Cosmetic/read-only unless the sim already emits the event.

### Queue C — watch / only if triggered

1. **Baked VDB / flipbook volumes**
   Useful for rare hero events, not the live gas body.

2. **Marketplace fluid solvers**
   Zibra/Obi/etc. only as cosmetic overlay candidates, never authoritative gas truth.

3. **HDRP volumetric stack**
   Watch only. Pipeline switch is not justified by current evidence.

4. **Fixed-point / velocity-driven visual swirl**
   Only if the engine track pulls the Tier-3 trigger or exposes enough bias/front vectors to fake it cosmetically.

## 7. Handoff format to Claude Code

If a research card becomes implementation input, hand off only a small probe brief:

- Goal: what the owner should see.
- Input data: which existing buffer/event/source it reads.
- Boundaries: render-only, no Core, no architecture change.
- Done_when: green existing visual checks + owner-eye jewel movement.
- Falsifier: what visual/perf result kills it.
- Budget: one small leg or explicit owner-approved larger leg.

No implementation recipe is binding. Claude Code's PLAN owns the actual build.

## 8. First recommended pass

Open with **Body shader upgrade pack** if `c-visual-002` is still actively shaping the gas-lab look.

Open with **Front/accent layer over GridView** if the gas-lab body is already readable but still lacks motion/personality.

Both are compatible with the earlier `s-research-gas-visual-tech-001` verdict: keep the shared URP raymarch body as the readable mass layer, then add controlled spectacle on top.

END_OF_FILE: live/indie-game-development/work/gas-visual-rd-center-2026-06-29.md
