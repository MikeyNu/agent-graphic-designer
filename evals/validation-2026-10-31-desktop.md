# Local desktop browser follow-up, 31 October 2026

The user authorized testing on their local desktop browser and confirmed that GitHub CI is unavailable due to billing. No further hosted-CI investigation was attempted. Earlier NOT RUN records remain historical; the conditions below were subsequently executed locally.

## Environment and evidence

Windows, headed Microsoft Edge 156.0.4314.50, Node 26.9.0, Playwright 1.64.1, and @axe-core/playwright 4.14.0. Task-owned browser contexts loaded the fictional queue and disclosure from an isolated loopback server. No user account, production service, or deployment was involved. Browser processes created by the runners were closed afterward.

The [retained runner and summary](browser-qa/README.md) identify exact artifact versions. The Windows Git checkout used CRLF for the unchanged disclosure; canonical LF hashes match its published source. The repaired queue was transferred as LF and its byte hash matches the retained source. Full local evidence includes screenshots, video recordings, and animation-frame traces. Recordings were created, but continuous normal-speed visual playback was not independently watched through the tool. This review inspected selected browser captures and temporal measurements instead of claiming perceived smoothness from a video file's existence.

## Executed coverage

**39 browser checks pass** on the final queue and unchanged disclosure. Ten conditions combine 1440×1000, 768×1024, 390×844, 320×568, and 844×390 viewports with normal and reduced motion. The suite checks queue rendering, native dialog keyboard behavior and dismissal, disclosure Enter/Tab/Escape, returned focus, and overflow. Desktop mobile-sized viewports are not physical mobile-device tests.

Additional executed flows cover accent-insensitive search, no-results recovery, sorting, filters, scroll restoration, pending duplicate prevention, leaving while an update is pending, opening another record, late completion, failure/retry, collection removing a row from Ready, focus fallback, direct links, browser Back/Forward, invalid routes, interrupted close/reselection, resize, live reduced-motion changes, 31 rapid real pointer activations, combined doubled text and expanded spacing, JavaScript-disabled disclosure fallback, and browser console/runtime errors.

Thirty axe scans across the queue, modal, and disclosure report zero violations for the selected WCAG rule tags. Incomplete checks are retained in the summary and require interpretation; zero detected violations is not complete accessibility conformance. The text test applies doubled computed sizes and spacing, not native browser zoom. Selected normal, narrow, and large-text screenshots were visually inspected. Four real animation-frame sequences record normal/reduced queue and disclosure openings, including intermediate and settled geometry. They do not establish device FPS, GPU cost, audio timing, or subjective smoothness.

## Findings and corrections

| Finding | Diagnosis and correction | Recheck |
| --- | --- | --- |
| Footer action failed rendered contrast. | Earlier token checks covered coral on paper, but the reset action actually sat on the darker canvas. Axe reported 4.3:1. Added a darker coral text role and the missing canvas pair to source checks. | Final rendered scans pass; source/color checks now total 22. |
| Large-text header overflowed and row times collided with names. | Header flex children could not wrap; the mobile pickup column stayed 49 px wide. Enabled header wrapping, flexible status filters, and an intrinsic pickup column. | Doubled-text/spacing stress and visual review pass. |
| Narrow detail content competed with fixed actions, and large select text was cramped. | The mobile dialog inherited a fixed-height body/footer arrangement. It now uses a naturally scrolling detail document; its simulation control wraps when needed. | Native keyboard access, viewport captures, large-text reachability, and all five sizes rechecked. |
| Initial focus assertion failed. | A focused BODY with `document.hasFocus() === false` represented Edge browser controls, not a background-page control. A dedicated probe recorded the native sequence back into the modal. | Harness checks document focus correctly. No custom focus trap was added to override native behavior. |
| Initial text-size harness compounded inherited sizes. | It mutated parents before reading descendants. All baseline sizes are now collected before changes. The remaining genuine overflow was then diagnosed separately. | Corrected stress test executed; the original false result is not presented as a product defect. |
| Full-page dialog screenshots were easy to misread. | A full-page composite includes offscreen document content around a fixed overlay. | Open-dialog captures now use the actual viewport. |

The guidance now explicitly requires checking harness assumptions, actual foreground/background pairings, internal reachability, and screenshot scope. Existing art direction is preserved. The queue remains a labeled local simulation and does not demonstrate backend persistence.

## Actual retained-page restoration

A separate standalone Edge window ran without an automation protocol connection. The served fixture copy included event logging and a controlled leave/return sequence. After starting close, it navigated to an away document; that document called native `history.back()`. The observed sequence included `pagehide.persisted === true` and `pageshow.persisted === true`, rather than synthetic event dispatch.

On restoration, the dialog was closed, body scrolling was unlocked, and focus returned to reservation LN-1043. The panel reopened and closed successfully afterward. The final event retained the expected focus and no body lock. This is **one passed genuine BFCache restoration case in this Edge version**, not cross-browser proof. Original source remains unchanged by the logging instrumentation.

## Remaining scope

Physical phones/tablets, other browser engines, assistive-technology users, representative usability studies, OS-level reduced-motion switching, native browser zoom, sustained performance measurement, and production/backend integration were not tested. No such claims are inferred from local browser success. GitHub CI remains unavailable due to the user-confirmed billing issue.
