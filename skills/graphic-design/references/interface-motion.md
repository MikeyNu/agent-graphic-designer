# Design the interface through time

Use during substantial interface creation, redesign, or motion refinement. Read this before fixing the composition, not after finishing every screen. The owner's explicit direction is for interfaces that feel alive through transitions, reveals, hover, scrolling, and response. Beauty, rhythm, surprise, and pleasure are valid motion intentions alongside feedback and continuity. Do not require a measurable productivity gain for an expressive sequence.

This guide supplies joint art direction and a shared contract. The companion [Web Motion Director](https://github.com/MikeyNu/Web-Motion-Director/blob/main/skills/web-motion-director/SKILL.md) supplies deeper implementation, scrolling, lifecycle, responsive, and temporal-verification guidance when available. Read the installed or repository version before using it; a link is not proof that the skill or its tools were loaded. The essential workflow below also works when that companion is unavailable. Use the current project's stack and actual host tools.

## Contents

- [1. Compose appearance and movement together](#1-compose-appearance-and-movement-together)
- [2. Give each important transition a contract](#2-give-each-important-transition-a-contract)
- [3. Direct the rhythm](#3-direct-the-rhythm)
- [4. Design scrolling as an experience](#4-design-scrolling-as-an-experience)
- [5. Transfer the reference relationships](#5-transfer-the-reference-relationships)
- [6. Study motion references honestly](#6-study-motion-references-honestly)
- [7. Implement and inspect the sequence](#7-implement-and-inspect-the-sequence)

## 1. Compose appearance and movement together

1. Inspect the task, current identity, routes, content, state model, animation conventions, input methods, and available references. Preserve approved direction. Distinguish an image-only deliverable from a requested working interface.
2. While arranging the composition, identify **stable anchors**, **objects that change**, and **places for expression**. Ask how a panel opens, a card becomes detail, a selection travels, a field responds, or a visual chapter changes. A pleasing material response or playful illustration can be enough reason to try a motion idea.
3. For a substantial new direction, compare different spatial and temporal ideas together. A stable scene with changing foreground, a sequence of graphic chapters, and an object-led continuity scheme are different possibilities, not compulsory presets. Do not create three unrelated palettes and attach the same fade-up to each.
4. Prototype the most consequential or expressive sequence early. Inspect the start, transition, and settled composition, then adjust the layout and motion together. A reveal may need a better crop; an expanding object may need a new boundary; a sticky scene may need less copy. Do not simply animate an unsuitable finished layout.
5. Carry the chosen relationships into repeated controls and adjacent routes. Centralize reusable motion decisions without making every object behave identically. Scale the work: a small hover repair needs its affected states, not a new three-direction study.

The graphic designer owns visual hierarchy, object relationships, image treatment, typography, and desired experience. The motion director owns temporal construction, input/progress mapping, lifecycle, and feasibility. Both review the same prototype and can revise composition or motion. These are responsibilities, not a requirement to create two agents or two disconnected briefs.

Use one [shared UI and motion brief](../assets/interface-motion-brief.md). Record concrete decisions once and link the relevant component/route implementation when it exists. Do not hand over “make it smooth” or run a separate motion brainstorm after the UI has been declared complete.

## 2. Give each important transition a contract

For each principal flow or signature moment, define the following. Simple controls may share a reusable contract; do not produce paperwork for every icon.

| Field | Decision required |
| --- | --- |
| Identity and intention | Which object/region, and what feeling, feedback, continuity, or narrative does the change create? |
| Evidence | Observed in which timestamped source, inherited from the project, or newly proposed? |
| Trigger and ownership | Pointer, keyboard, touch, state update, route, elapsed time, or scroll progress; which system controls it? |
| States | Resting, active/pending, intermediate, settled, and relevant failure or cancel states. |
| Stable anchor | What stays visually reliable while the other elements change? |
| Moving properties | Position, scale, clipping, opacity, shape, color, or media progress; axis, origin, travel, and stacking order. |
| Choreography | What leads, follows, overlaps, holds, and settles? Identify a focal element instead of staggering everything. |
| Timing and easing | Candidate duration or scroll range, easing behavior, and why it feels appropriate here. Label untested values as proposals. |
| Interruption | What happens on immediate reversal, repeated activation, new data, resize, route exit, or late async completion? |
| Input and navigation | Focus, semantics, touch alternative, direct entry, Back/forward, and return position where relevant. |
| Alternate conditions | Narrow/short viewport, long text, reduced motion, slow/missing assets, unsupported enhancement. |
| Proof | Exact prototype/build, playback and input conditions, tested states, measured claims, and unresolved checks. |

Separate visual feedback from committed application state. A button may compress immediately while saving is pending; a successful checkmark must reflect the actual save. An animated toggle position does not establish server persistence. Design pending and failed states as part of the visual system.

## 3. Direct the rhythm

Think in relationships: a quick response can lead into a longer settling surface; a still heading can anchor a moving illustration; related elements can overlap in time instead of entering in a mechanical queue. Let movement express the apparent material. A soft card, rigid table row, drawn line, and photographic crop need not have the same acceleration or rebound.

Define a small family of feedback, component, and scene timings appropriate to this product. Trial values such as 120 ms for a small press response, 240 ms for a compact panel, or 600 ms for an expressive scene are **starting experiments**, not measured recommendations or universal defaults. Tune at normal playback speed, with realistic content and repeated use. Springs need observed damping and settling behavior, not the adjective “bouncy.”

Use delay and stagger selectively. Stagger a small meaningful group if the sequence improves its appeal or reading; cap the aggregate delay and keep controls immediately usable. Do not delay an entire long table row by row. Decide whether entrances run once, on a specific state change, or on deliberate replay. Re-entering a viewport should not blindly replay an introductory performance.

Hover may add a lift, image crop, contour, light change, reveal, or playful accent. Pair it with a deliberate focus state and touch behavior; they need equivalent access, not necessarily identical movement. Keep hit areas stable, avoid hover oscillation caused by a moving target, and distinguish hover, keyboard focus, pressed, selected, disabled, and pending.

Personality does not require perpetual motion. Give expressive moments enough quiet around them to be noticed. A dense workspace can feel responsive through selection continuity, useful panel transitions, and carefully tuned feedback while an illustrated lesson or portfolio earns a more expansive sequence. Do not automatically strip motion from a serious product or impose cinematic delays on every repeated action.

## 4. Design scrolling as an experience

For scroll-rich pages, storyboard relationships between sections, not a list of entrance effects. A graphic object can change scale and role as a chapter changes; a fixed visual scene can support successive annotations; an image crop can reveal a new subject while the next title takes over. Choose a visual idea tied to the composition or desired atmosphere. Build an actual short prototype when implementation is requested.

Distinguish three different mechanisms:

| Mechanism | Specify |
| --- | --- |
| Scroll-triggered | An entry threshold starts a time-based sequence. Define replay, exit, interrupted loading, and a fully visible fallback. |
| Scroll-linked | Progress directly maps to the sequence. Define start/end geometry, progress keyframes, reverse traversal, and resize recalculation. A duration alone is insufficient. |
| Sticky or pinned chapter | A bounded region holds an anchor while content evolves. Define entry, hold, release, overflow travel, skip/direct access, and behavior on short viewports. |

Maintain one clear owner for each animated property and scroll relationship. Do not let hover transforms, layout transitions, and scroll code overwrite each other. Nested visual layers can separate those responsibilities without changing semantic structure.

Native scrolling can drive rich choreography; a smooth-scroll engine is not a prerequisite. Preserve wheel, touch, keyboard, direct navigation, and predictable escape. Do not leave extra blank distance after a pinned scene, trap a user in a chapter, or require long sideways travel to read routine form labels. An ordinary settings/list scroll may remain direct while its controls and state changes are fully designed.

Recompose for narrow and short screens. A desktop chapter may become smaller discrete scenes, a native rail, or ordinary vertical content with selective animation. Reduced motion is a separate design dimension: preserve every fact and action while replacing spatial travel, parallax, or camera motion with a stable view, direct change, or suitable brief fade. Do not just speed up the same large movement.

## 5. Transfer the reference relationships

These are **proposed adaptations** of the static [workspace study](owner-workspace-study.md), not recovered animation recipes. Do not implement every row as a checklist.

| Static relationship | Motion direction to explore | What the contract must preserve |
| --- | --- | --- |
| R21 ranked person with adjacent expanded analytics | Keep the person's identity anchored while detail opens; coordinate metric focus rather than replaying every chart. | Scope, stable totals, readable labels, cancel/reselect behavior. |
| R22 central work and activity side region | Let a selected task reveal related context while the task list stays still. | Draft messages, selected task, panel scroll ownership. |
| R23 conversation beside a table artifact | Reveal the artifact's frame as a coherent surface; show partial generation inside it. | Cancellation, draft edits, incomplete versus saved data. |
| R24 overlapping account geometry | Shift the selected card face with a controlled edge/scale relationship. | Card identity, accessible selection, pending data, quiet numerals. |
| R25 illustrated lesson covers and connected steps | Give a selected cover a brief illustration response, then carry its title/art into a lesson opening. | Immediate lesson access, resume state, touch/focus alternatives. |
| R26 luminous insight stack | Change depth and emphasis as another insight is selected; make the front card settle into a reading plane. | Complete text, stable targets, no continual forced rotation. |
| R28 selected board object | Preserve the object's visual identity while moving stage or opening detail. | Valid destination, pending/rejected move, alternative controls, return context. |
| R30 driver, map, and activity | Coordinate selected route emphasis and detail; animate a fit-to-route only when intended. | Manual pan, follow mode, stale positions, reduced spatial motion. |
| R31 chart focus and linked records | Carry focused period/category into the resulting filtered table. | Equivalent non-hover access, correct data scope, Back restoration. |
| R33 through R38 settings and preferences | Tune switch, tab indicator, local disclosure, dirty state, and save feedback as one family. | Transaction boundaries, persistent labels, failed saves, no delayed input. |
| R39 and R40 profile editing beside identity/preview | Maintain identity as the image editor opens; update a draft preview coherently. | Original versus draft, cancel restoration, upload failure, privacy scope. |

Preserve visual integrity in intermediate states: clipping, contours, shadows, text contrast, and layer intersections matter while things move. Keep numbers truthful. A count-up that passes invented interim values or a chart drawn from zero on each filter change may misrepresent the data; use a transition that preserves its meaning.

## 6. Study motion references honestly

When the owner supplies video, use the available media tools to inspect it before writing claims. Record file/source identity, dimensions, duration, frame-rate information if available, and access limits. Watch normal-speed playback and inspect timestamped frames around key events. If only sampled frames are accessible, say so: they can support order and positions but cannot establish perceived smoothness or exact timing between samples.

For each useful sequence:

1. Identify the product surface and what is actually visible. Separate in-interface animation from camera pans, mockup rotations, editorial cuts, speed ramps, and presentation transitions.
2. Mark observable onset, key intermediate states, overlap, hold, and settlement with timestamps. Distinguish the recording's time from a proposed implementation duration. Compression, dropped frames, and edited playback limit precision.
3. Identify the input only when shown or otherwise supported. Without a cursor, scroll indicator, or other evidence, keep hover, scroll, and autoplay as hypotheses. A visible input may still leave its internal implementation unknown.
4. Trace object identity, stable anchors, direction, transform origin, clipping, layering, and depth. Note what arrives first and whether motion settles, loops, reverses, or is interrupted in the available recording.
5. Describe the observed acceleration qualitatively unless measurements support more. Do not invent the original easing curve, spring constants, library, shader, or DOM structure. A matching implementation can use different technology.
6. Record what should transfer and what is specific to that creator's assets or composition. Propose a new version for the current product, including narrow, touch, reduced-motion, and failed-load variants.
7. Prototype and compare at normal speed. Judge rhythm, character, continuity, readability, and actual input response together. Separate faithful reconstruction from inspired adaptation.

Use an evidence row: `source + timestamps | observed sequence | supported trigger | uncertainties | transferable relationship | proposed implementation | checks`. Do not mark a planned video analysis as completed. This update contains static-image study and motion proposals only.

## 7. Implement and inspect the sequence

Use the project's existing motion system where suitable. Start with CSS for simple state transitions, an existing animation API for cancelable sequences, and established project tools for complex timelines or spatial scenes. Choose heavier systems from the actual problem; verify current API support and documentation when implementing. Do not promise a particular library is available from the skill text.

Coordinate state, geometry, and lifecycle. Retarget or reverse from the current visual state when appropriate, cancel obsolete work, and prevent an old animation callback from reopening a closed panel or announcing success for a failed operation. After resize, preference changes, route exit, or media failure, leave correct state and usable controls. Keep semantic expansion, focus, and input availability aligned with the real interaction, rather than waiting for a decorative finish.

Prefer transform and opacity for frequent visual changes where they express the desired result; inspect layout, paint, and compositing costs rather than claiming free GPU performance. Use `will-change` selectively, reserve media space, and stop unused work. [U14 in the sourcebook](sourcebook.md#ui-and-ux-evidence) supports this performance guidance, not a frame-rate guarantee.

Respect the scoped pause/stop/hide requirements and the reduced-motion design standard. WCAG 2.2 SC 2.3.3 is AAA; SC 2.2.2 is Level A and has different conditions for movement and automatic updates. [U12 and U13](sourcebook.md#ui-and-ux-evidence). Do not claim complete accessibility from one media query or animation check.

Verify the actual rendered sequence:

- Normal-speed forward playback and settled appearance, not just an attractive midpoint screenshot.
- Immediate reversal, rapid repeat activation, cancellation, late data, and navigation away/back as relevant.
- Keyboard, focus, pointer, touch, direct route entry, history, and return position.
- Narrow and short viewports, long content, resize, reduced motion, and missing/slow media.
- Start/end/reverse of scroll chapters, release, cleanup, and consistent state after re-entry.
- Console issues and observed performance, with measured evidence before numeric claims.

Record **specified**, **prototyped**, **implemented**, and **temporally inspected** separately. A storyboard is not a running animation; a build is not temporal QA; sampled frames do not establish continuous smoothness. If runtime access is absent, deliver the concrete motion contract and identify the remaining check. Do not invent playback or device verification.
