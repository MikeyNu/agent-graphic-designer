# Interaction, accessibility, and interface verification

Use for any interface with navigation, input, async behavior, or user decisions. Design the state changes as carefully as the default screen. Scale the checks to the requested scope. A static mockup can specify behavior but cannot demonstrate that behavior works.

## Contents

- [1. Define the flow contract](#1-define-the-flow-contract)
- [2. Specify meaningful states](#2-specify-meaningful-states)
- [3. Design input and recovery](#3-design-input-and-recovery)
- [4. Build accessible behavior](#4-build-accessible-behavior)
- [5. Design motion and responsiveness together](#5-design-motion-and-responsiveness-together)
- [6. Verify the experience](#6-verify-the-experience)
- [7. Report the actual status](#7-report-the-actual-status)

## 1. Define the flow contract

For each important action, identify its trigger, preconditions, destination or state change, feedback, persistence, failure, recovery, and return path. Keep the contract compact enough to use. Include both the primary path and the most consequential alternative. Do not invent implementation dependencies or backend capability.

Example: choosing an appointment should lead to selecting an available slot, reviewing details, submitting, and seeing a confirmed booking only after the server confirms it. If the slot has been taken, preserve the other details and offer current alternatives. Going back must not create a duplicate booking. This is a hypothetical design example, not clinical or scheduling policy.

Distinguish navigation, local state changes, and durable operations. A prototype can simulate outcomes if labeled clearly, but a success toast is not evidence of a persisted operation. In production work, follow the action through its actual dependency and read back the result where appropriate.

## 2. Specify meaningful states

Use states that apply to this flow, rather than mechanically adding every state to every component:

| State | Design requirement |
| --- | --- |
| Initial/loading | Explain what is pending; keep existing useful context. Skeletons should match the content structure and reserve space. |
| Empty/new | Explain absence and offer the next useful action. Avoid fabricated populated data. |
| No results | Preserve the query and filters; provide a way to broaden or clear them. |
| Ready/populated | Use realistic content, priorities, and action hierarchy. |
| Partial or stale | Identify what is missing or outdated; do not display a misleading complete total. |
| Validation error | Identify the field, reason, and correction; preserve valid input. |
| Submission pending | Show progress or pending status, guard against accidental duplicate actions, and avoid premature success. |
| Success | Confirm the actual result, where it can be found, and the relevant next step. |
| Failure/timeout | Describe the known result and safe next action. If the outcome is uncertain, check status before encouraging a potentially duplicate retry. |
| Offline | Distinguish unavailable actions from work that is truly saved locally or queued. Never imply sync succeeded before it did. |
| Permission/session loss | Explain the relevant restriction without exposing private data; preserve permitted work and support re-entry or access requests. |
| Cancel/back/undo | Preserve expected context and state; make the consequence of abandoning unsaved work clear. |

For reversible, low-risk actions, optimistic feedback can be appropriate with rollback and clear failure handling. For irreversible or consequential actions, use an explicit pending state and confirmed outcome. Do not apply optimism indiscriminately to payments, bookings, invitations, or destructive changes.

## 3. Design input and recovery

Ask only for information needed now. Use persistent labels, appropriate input types, autofill support, clear units, relevant examples, and requirements before submission. Placeholders do not replace labels. Do not mark untouched fields as erroneous simply because they are empty.

Validate at a useful moment for the field and task. Avoid interrupting someone while they are still typing a valid possible value. On submission, show actionable field errors; for page-level forms, provide a linked summary when useful and direct focus appropriately. Retain valid data. Distinguish invalid input from service failure. GOV.UK provides a concrete form-recovery pattern, not a required visual theme for other products. [U9 in the sourcebook](sourcebook.md#ui-and-ux-evidence).

Make optional and required information unambiguous. Do not disable the only submit control without a discoverable explanation of what remains incomplete. Use confirmation at meaningful risk boundaries, not on every ordinary action. For destructive work, identify the affected object and scope; provide undo when genuinely possible.

For multistep work, explain meaningful progress, keep completed answers, support Back, and show a review step when consequences warrant it. Request permissions when their benefit becomes clear. Allow optional onboarding to be skipped or resumed without blocking the core task.

For authentication, coordinate sign-in, registration, email verification, and recovery as related but distinct tasks. Keep naming consistent with the actual operation: a reset link, passwordless sign-in link, and code confirmation are not interchangeable. Define code input, paste/autofill, active versus completed state, expiry, resend, correction, and return where relevant. Follow the actual provider's supported behavior and policy instead of borrowing password rules, provider logos, trial claims, or testimonials from a reference. The owner's [account-screen study](owner-reference-study.md#authentication-and-account-flows) is visual evidence, not an authentication specification.

Let expressive media and shaped surfaces accompany a form while keeping the form operable if media is absent or fails. Recompose that relationship for keyboard-open, narrow, and short layouts. Preserve optional visual character where it fits; removing the image on every small screen is not a design requirement.

For selection and bulk actions, distinguish visible rows from all matching results. Show selection count, scope, and the affected items before consequential operations. For filters, show applied criteria and a clear reset path. For calendars, expose timezone and duration, prevent selection of unavailable slots, and provide a usable agenda or list when the grid is too dense.

## 4. Build accessible behavior

Use the applicable platform standard and semantic elements. For web interfaces, use WCAG 2.2 AA as the baseline unless the brief sets a different requirement; apply each criterion's scope and exceptions. Do not claim whole-product conformance from this shortlist.

| Area | Required design and verification |
| --- | --- |
| Meaning and structure | Real text, meaningful headings, landmarks, labels, appropriate alternative text, and coherent reading order. Prefer native links, buttons, and inputs. |
| Keyboard | Reach and operate every function, follow a logical order, show focus, and avoid traps. Add shortcuts as optional acceleration. |
| Focus and overlays | Set initial focus appropriately, keep background-page controls inert during a modal, support dismissal, and restore focus sensibly. Follow the APG pattern and verify the component. For a native dialog, distinguish focus entering browser chrome from background-page escape; do not add a custom trap just to satisfy a DOM-only assertion. See [harness checks](execution-and-evidence.md#choose-checks-by-what-they-can-establish). |
| Sticky UI | Prevent headers, bottom navigation, banners, and sheets from hiding the focused control. SC 2.4.11 AA requires it not be entirely obscured by author-created content; aim for full visibility. |
| Pointer targets | SC 2.5.8 AA specifies at least 24 by 24 CSS px or an applicable exception, including defined spacing. Favor comfortably larger touch targets where practical; do not call 44 or 48 CSS px the universal AA minimum or equate px, pt, and dp. |
| Color and contrast | Verify actual text and essential non-text contrast, all meaningful states, and non-color information cues. Apply the dedicated color guide, not palette-only checks. |
| Zoom and reflow | Check 200% text resizing and 320 CSS px reflow as applicable, user text-spacing overrides, long strings, and unclipped controls. Respect legitimate two-dimensional content exceptions. |
| Gesture and motion | Offer a single-pointer alternative without dragging when dragging is not essential; keyboard support alone is not that alternative. Make hover content usable by keyboard and pointer; retain critical information without animation. |
| Authentication | Support password managers and paste; provide an accessible path through all required steps. Do not force memory puzzles or manual code transcription without the applicable assistance or alternative. |
| Announcements | Make important results and errors perceivable by assistive technology without unnecessary focus jumps or constant live-region chatter. |

See [U4 through U8 and U11 through U13](sourcebook.md#ui-and-ux-evidence). Automated tools can find some defects, but keyboard, screen-reader, content, and visual checks remain necessary. An untested component library is not proof of accessibility.

## 5. Design motion and responsiveness together

Read [Interface motion](interface-motion.md) while composing substantial UI. Define visual and temporal relationships together, share one brief with an available motion skill, and prototype a principal sequence before the entire layout is fixed. Include trigger, anchor, active/intermediate/settled states, timing or scroll progress, interruption, and alternate conditions. Do not satisfy a request for an animated implementation with prose alone.

Use motion for spatial relationships, continuity, feedback, product behavior, expressive rhythm, or enjoyment. An aesthetic reason can be sufficient; inspect the actual sequence and its cost to the experience. Keep essential content available without waiting through a reveal. Respect reduced-motion preferences with a coherent alternative. Do not merely make the same large movement slightly faster.

Let visual response start promptly while durable work remains pending. Show confirmed success only when the actual operation succeeds. Retarget or reverse an interrupted transition from its current state where appropriate; prevent obsolete callbacks from changing a newer state. Verify normal-speed playback, rapid repeat input, reversal, cleanup, and final composition as applicable. A screenshot proves only its captured state.

Avoid scroll hijacking, mandatory horizontal journeys for routine work, custom cursors that obscure targets, distracting continuous movement, and autoplay carousels that hide essential content. Ornamental animation is not automatically a defect; evaluate distraction, control, accessibility, and performance in the actual context. For cinematic experiences, preserve usable navigation, direct access to the information, a reduced-motion path, and a usable mobile experience. Apply pause/stop/hide requirements to qualifying moving content. [U12 and U13](sourcebook.md#ui-and-ux-evidence).

Reserve image and media space, avoid layout shifts, keep font fallbacks usable, and budget images, video, animation, and scripts for the actual audience's devices and connectivity. Load secondary media only when useful; do not defer the content needed for the main task. Show real progress when available rather than invented percentages.

Google's current good Core Web Vitals thresholds are LCP at most 2.5 seconds, INP at most 200 milliseconds, and CLS at most 0.1, evaluated at the 75th percentile and segmented by mobile and desktop. These are performance measures, not a usability score; a lab run does not establish field performance. [U10](sourcebook.md#ui-and-ux-evidence).

## 6. Verify the experience

For substantial implementation, inspect representative pages and every distinct primary flow, plus affected shared components and their difficult states. Use the actual project tooling, browser capabilities, and available assistive technology. Do not silently install dependencies or require a specific framework merely to follow this guide.

1. Open the actual result, confirm fonts and assets loaded, and inspect desktop, narrow phone, and an intermediate width. Include a short viewport and applicable zoom/reflow conditions.
2. Complete the primary task from its real entry point. Verify the destination, durable result where in scope, confirmation, Back, refresh or revisit, and return position.
3. Exercise the most consequential failure, empty/no-results condition, slow response, repeat submission, and interruption relevant to that flow. Use a safe test environment for mutations.
4. Traverse by keyboard. Inspect focus visibility, overlay lifecycle, labels, and non-hover access. Run available automated accessibility checks and manual checks, recording their different coverage.
5. Inspect long and localized content, dense data, missing media, and important interaction states. A zero-overflow measurement does not establish visual success: inspect selected control values, clipped text, overlaps, and internal scrolling. Check sticky UI against the on-screen keyboard where that capability exists.
6. Compare the whole rendered page against the [originality checks](interface-originality.md#4-review-the-whole-page-and-system), the brief, and the existing system. Check more than the hero.
7. Fix blockers first, rerun the affected flow and shared surfaces, and record evidence. Stop repeating unrelated tests when they already pass and nothing relevant changed.

With actual participants, use neutral task prompts and observe completion, errors, time, recovery, and comprehension in context. Do not give away the control they should choose. Label this separately from an internal cognitive walkthrough or agent review. Avoid invented sample sizes, conversion effects, or a universal completion-time target.

## 7. Report the actual status

Use [the interface review template](../assets/interface-review-template.md) where it helps. Separate **specified**, **implemented**, **visually inspected**, **functionally tested**, and **user-tested**. For each check record PASS, FAIL, NOT RUN, or N/A with artifact/version, conditions, method, evidence, and remaining defects.

A static visual must say that behavior is specified, not verified. A local interactive prototype with simulated data must not be called an integrated production flow. Record real browser limitations rather than inferring the unseen result. Never average a blocking task, truthfulness, or accessibility defect into a passing aesthetic rating.
