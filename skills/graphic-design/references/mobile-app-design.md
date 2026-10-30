# Mobile apps: task, continuity, and device context

Use for native mobile apps, mobile web, and responsive product experiences. Establish which platform and implementation are actually in scope. These are practical design instructions, not a claim that every platform shares one navigation model. Read with [interaction and validation](interaction-and-validation.md); use the [SaaS and mobile study](saas-mobile-reference-study.md) for observed examples and their limits.

## Contents

- [1. Design for the moment of use](#1-design-for-the-moment-of-use)
- [2. Keep navigation and return paths coherent](#2-keep-navigation-and-return-paths-coherent)
- [3. Adapt information instead of shrinking it](#3-adapt-information-instead-of-shrinking-it)
- [4. Design input and device access](#4-design-input-and-device-access)
- [5. Handle interruption and uncertain outcomes](#5-handle-interruption-and-uncertain-outcomes)
- [6. Make mobile craft measurable](#6-make-mobile-craft-measurable)
- [7. Verify more than phone-shaped screenshots](#7-verify-more-than-phone-shaped-screenshots)

## 1. Design for the moment of use

Define the immediate job, entry point, available attention, environment, and cost of interruption. A user reviewing one approval between meetings needs different content from someone investigating a month's spending. A ticket at a venue entrance needs retrieval and legibility; recipe discovery and following cooking steps are different tasks. Treat these as hypotheses to check with the intended audience, not universal assumptions about mobile use.

Design the shortest understandable route to useful value. Keep context and consequences that a decision requires; remove redundant greetings, ornamental onboarding, and unrelated summaries when they delay the task. Do not make optional account setup, personalization, or notifications prerequisites for features that do not need them.

For a notification or external link, specify the target object, expected account, current authority, and safe fallback if it is missing, expired, or changed. Retrieve current state before offering a consequential action. If authentication intervenes, retain the intended destination only when it remains permitted. Do not treat the notification's old text as authoritative state.

## 2. Keep navigation and return paths coherent

Separate persistent destinations, navigation within a destination, and actions. Keep destination labels and ordering stable. Show the current location, including when entering through a deep link. A prominent create or scan action should not masquerade as a destination with a nonexistent history.

Follow the applicable platform's Back, dismiss, sheet, and navigation conventions. Distinguish returning to a previous screen, closing a temporary layer, and canceling an edit. Define the result of system Back or an edge gesture, not only the visible back arrow. Do not invent a back stack that returns someone to an unrelated home screen after every task.

Preserve appropriate tab state, list position, filters, and drafts. If no in-app history exists, provide a sensible parent route. Restore only data the current account may access. Make unsaved-work consequences clear without adding confirmation to every ordinary navigation action.

Use a sheet for bounded contextual work; prefer a full screen for long input, substantial comparisons, or tasks that need a durable route. Test sheet height, internal scroll, dismissal, focus, keyboard, and large text. A fashionable floating bottom bar is not successful if it covers the last list item or conceals destinations behind unlabeled icons.

## 3. Adapt information instead of shrinking it

Choose what the user must recognize now and what detail remains reachable. Preserve identity, current status, relevant amount or date, and the next decision. Avoid copying every desktop KPI into vertically stacked cards before the main task.

| Desktop relationship | Possible mobile adaptation | Preserve |
| --- | --- | --- |
| Queue and side inspector | List followed by focused detail | Selected object, filters, return position, next-record context. |
| Wide comparison table | Priority columns, expandable detail, or deliberate horizontal comparison | Labels, units, relationships, and access to omitted attributes. |
| Overview and many diagnostics | Question-led summary with scoped drill-down | Time range, freshness, comparison basis, and path back. |
| Event and ticket list | Event detail, then focused ticket presentation | Event identity, date, attendee or ticket type, ticket count and state. |
| Content discovery and execution | Browse/detail, then an optional focused task mode | Saved progress, essential reference content, exit and resume. |

Keep units and definitions when simplifying a metric. A “team activity” ring without a denominator remains ambiguous even if it fits neatly on a phone. Distinguish a selected period from a navigation destination. Avoid horizontal carousels for urgent items unless the hidden content and route to all items are clear.

Use imagery to answer a question. A product angle, recipe photograph, or event poster can aid identification; a large abstract object may contribute only to promotion. Ensure captions, variants, instructions, quantities, and imagery describe the same item. Avoid ingredient pictures without usable names or quantities where the task requires them.

Keep critical information available without waiting for animation. Offer visible alternatives to swipe, drag, and long-press where they carry essential actions. A slider or slide-to-confirm control does not by itself prove accessibility or prevent error.

## 4. Design input and device access

Use persistent labels, appropriate keyboard and autofill behavior, sensible input formatting, and useful error placement. Test the entire entry sequence, including moving between fields, dismissing the keyboard, correcting errors, and submitting. Do not let the keyboard or fixed footer cover the current field, its error, or the final action.

Support paste and password managers. For verification codes, preserve accessible alternatives and avoid forcing manual transcription when assistance is applicable. Distinguish authentication from authorization to act on a specific record.

Request camera, microphone, photo, location, or notification access when its benefit is understandable and the task requires it. Design denial, restricted access, later revocation, and settings recovery. Keep unrelated features usable when possible. Do not show a custom illustration as if it were a real system permission dialog.

For biometrics, specify cancellation, failure, unavailable capability, reauthentication, and an appropriate supported fallback. A face or fingerprint glyph in a mockup does not implement platform authentication. Verify native capabilities against current official platform guidance and the actual stack; do not promise them in a web prototype without support.

Show notifications with a privacy-aware preview policy appropriate to the content and user controls. Financial amounts, attendee identity, and private task text may need reduced lock-screen detail. Opening a notification must not automatically commit the action it describes. Distinguish local reminders from confirmed server events.

## 5. Handle interruption and uncertain outcomes

Specify what survives leaving the app, backgrounding, process termination, account changes, and network loss. Preserve useful permitted progress, but do not retain sensitive drafts indefinitely by accident. State the actual storage and expiry policy when known rather than promising offline access universally.

| Situation | Required distinction |
| --- | --- |
| User enters a draft offline | Unsaved, saved on this device, queued, and synced are different states. |
| Consequential request times out | The outcome may be unknown. Reconcile the current record before retrying. |
| Connection returns | Revalidate access and data; resolve conflicts rather than silently overwriting. |
| Notification opens an old record | Show current status, changed conditions, or a safe unavailable state. |
| App resumes after an interruption | Restore useful context and explain stale content without replaying actions. |
| Ticket or credential is cached | Confirm whether offline presentation is supported and how expiry, revocation, or dynamic refresh works. |
| Recording or generation stops | Distinguish captured, locally saved, uploaded, processed, and reviewed content; expose recovery limits. |

Do not queue payments, approvals, invitations, or destructive changes silently. Any supported queued action needs clear intent, state, cancellation where possible, and safe reconciliation. Avoid duplicate submissions from double taps or resume events. A success animation must follow the result it claims.

For generated transcripts, summaries, or tasks, make source material inspectable where available. Separate suggested content from verified fact and a draft from an authorized action. Let users correct, reject, or return to a timestamp without losing their place. Keep counters and action labels consistent with the actual review state.

## 6. Make mobile craft measurable

Use the platform's applicable target-size guidance in its own units. Do not equate CSS px, points, and density-independent pixels or label one native recommendation the universal web AA rule. The general interaction guide records the narrower WCAG web requirements. Refresh native specifications before citing exact current values.

Reserve layout space for system bars, safe areas, keyboards, banners, and transient feedback. Use scalable text and flexible containers. Inspect large accessibility text sizes, long localized labels, multiline buttons, and short landscape layouts rather than shrinking text until the composition fits. Keep controls distinguishable by labels and state, not color alone.

Provide meaningful accessibility names and reading order, understandable selected states, and status announcements where needed. A tiny icon can have a larger target, but adjacent targets must remain distinct. Test screen-reader navigation on the actual platform when available; a DOM check cannot establish native accessibility.

Make charts readable without hover and gestures discoverable without a tutorial. Respect reduced motion while preserving feedback. Use haptics or sound as supplemental cues, never the sole indication of an outcome. Keep essential loading, progress, and error content perceivable when muted or offline.

## 7. Verify more than phone-shaped screenshots

Trace one primary task from its actual entry, with its most consequential interruption. Check a small supported viewport, large text, keyboard-open input, and the relevant platform navigation. Verify long content, system insets, the last scrollable item, focused controls, and bottom actions. Inspect real artifacts at readable size rather than judging an angled device presentation.

Test notification/deep-link entry, denied permission, stale data, slow or lost connection, repeated submission, background/resume, and return state where applicable. Use safe fixtures and supported test environments. A desktop browser at a phone width can reveal layout defects; it does not establish on-device keyboard, biometrics, push, offline credential support, or app lifecycle behavior.

Record exactly which platform, device or simulated viewport, input method, state, and artifact were examined. Separate a static storyboard, interactive simulation, native implementation, and participant study. Do not claim a whole app is accessible, responsive, or reliable from three polished screens.
