# Shared UI and motion brief

Use one brief while composing the interface. The graphic-design and motion skills read and update the same decisions. Use only relevant fields; a small control may inherit an existing component contract. See [the workflow](../references/interface-motion.md).

## Direction and evidence

Product, task, audience, and approved identity:

Visual and temporal character, including desired pleasure or atmosphere:

Source evidence, access level, and timestamps if temporal:

Observed behavior versus newly proposed behavior:

Interface animation versus presentation camera/editing, with access and sampling limits:

Stable anchors, expressive regions, and quiet regions:

Composition/motion alternatives explored and chosen relationship:

Existing stack, animation conventions, and real capability limits:

## Principal sequence

Component or route and persistent object identity:

Trigger, input modes, and responsible state/scroll owner:

Clock: recording evidence, elapsed animation, user progress, or application/data state:

First readable state, input readiness, and visual settlement:

Crop/focal-point continuity, masks, layer order, and text treatment:

| State or beat | Visible composition | Moving properties and origin | Timing/progress, overlap, and easing | Semantic/data state |
| --- | --- | --- | --- | --- |
| Resting | | | | |
| Active or pending | | | | |
| Intermediate | | | | |
| Settled | | | | |
| Canceled or failed, if relevant | | | | |

Treat initial timing values as candidates until inspected. For scroll-linked work, define progress and geometry instead of supplying only milliseconds.

Reversal, rapid repeat input, late async completion, and cleanup:

Navigation, focus, direct entry, Back, and return context:

Narrow/short viewport and touch adaptation:

Reduced-motion composition and preserved information:

Missing media, loading, resize, and enhancement-failure fallback:

## Implementation and verification

Prototype/build and relevant source locations:

Design changes made after observing motion:

| Check | Conditions and method | Status | Evidence or limitation |
| --- | --- | --- | --- |
| Normal-speed sequence, first readability, input readiness, and settlement | | NOT RUN | |
| Mask/type intersections, crop continuity, and loop seam if relevant | | NOT RUN | |
| Reverse, cancel, rapid input, and cleanup | | NOT RUN | |
| Input, semantics, focus, and navigation | | NOT RUN | |
| Scroll entry, progress, reverse, and release, if relevant | | NOT RUN | |
| Responsive, long content, and missing assets | | NOT RUN | |
| Reduced motion and applicable pause controls | | NOT RUN | |
| Performance | | NOT RUN | |

Use PASS, FAIL, NOT RUN, or N/A with reasons. Separate specified, prototyped, implemented, and temporally inspected status. A still image or successful build does not prove animation quality.
