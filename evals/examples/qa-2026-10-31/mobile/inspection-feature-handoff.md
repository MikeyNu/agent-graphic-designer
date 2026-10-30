# Equipment check: recoverable offline draft

**v1 · Implementation handoff · Interaction and motion specified only.** The brief supplies the approved appearance; app screens, platform, code, storage, and service contracts were not supplied. Reuse the existing blue rounded cards, gradient header, typography, controls, and ordinary tab navigation. Proposed timings below need integration review.

Help an inspector resume the exact equipment check without losing a note or photo, understand other inspectors’ changes, and recognize when the server has accepted their submission.

## Screen and navigation contract

Use the existing full-screen check detail route within its current tab. Keep equipment/check identity visible in the header, server status beside that identity, and **draft status beside the editable note and photo**. These are separate statuses. Keep the gradient and surrounding cards still while feedback changes locally. Use ordinary vertical scrolling and the existing action placement, with space for bottom tabs, safe areas, and the keyboard.

| Moment | Required behavior |
| --- | --- |
| Notification opens | Resolve account/tenant and exact equipment/check IDs; notification text is only an entry hint. Restore the matching local draft without creating a duplicate. Fetch current authority and record state when connected. An expired sign-in preserves the intended route, then revalidates it. |
| Opening offline | Show permitted cached context with “Last checked {time}.” Restore a recoverable draft for the known check. If neither a usable cache nor a recoverable draft establishes the target, explain that the check must be loaded online and offer retry/the existing check list. |
| Leaving | Back, system Back/edge gesture, tab switch, and camera launch preserve the draft. Ordinary navigation after a successful local save needs no discard confirmation. Preserve the originating list’s position/filters and tab state. Cold notification entry gets the normal check-list parent route when there is no prior in-app screen. |
| Returning | Restore the saved note, photo, and editing context before refreshing. Preserve scroll/caret where appropriate; do not automatically open the keyboard. Show “Checking latest version” while revalidating access and version. Refresh must not replace local edits or move focus. |
| Reconnected | Reconnection checks state; it does not submit. When current authority and version are known, offer **Submit check** or **Review changes**. Keep an unsubmitted draft locally if the inspector leaves again. |
| Record unavailable | Removed, closed, reassigned, or unauthorized records get a specific safe explanation and parent route. Prevent invalid submission. Retain the draft under its original account scope for permitted recovery; account switches must not expose it. |

Keep **Submit check** visible with an adjacent explanation when unavailable offline or during revalidation. Enable it only after current access/version and required-input checks; offline work is not queued for automatic submission.

## Persistence and truthful feedback

Autosave note changes and accepted photos to durable, account-scoped device storage. A draft needs the check identity, base server revision, local revision, note, durable photo references, and last successful local save time. Commit a new draft revision atomically; retain the previous valid revision on failure. Copy photo bytes out of temporary camera/picker storage before calling them saved. Persist throughout editing, with a save barrier before controlled departure; an unmount/background callback alone is insufficient.

| Visible state | What must be true |
| --- | --- |
| **Saving on this device…** | New changes are not yet durably acknowledged. Keep the last saved revision recoverable. |
| **Saved on this device · Not submitted** | Note and attached photo data for that revision are durably stored. If offline, add “Reconnect to review and submit.” |
| **Couldn’t save on this device** | Keep current input and any previous saved revision. Offer **Retry save** with a concrete reason when known. A controlled exit with uncommitted changes must explain the risk and offer staying/retrying or explicit discard; never silently lose them. |
| **Submitting…** | An explicit submit is in flight. Upload progress is real transport progress, or plain pending text when no amount is known. |
| **Couldn’t confirm submission · Checking status** | A timeout or disconnect leaves the outcome unknown. Reconcile before offering a safe retry. |
| **Submitted · Confirmed {time}** | The server accepted the exact submitted revision and all required photo references, established by its authoritative response or reconciliation. A completed upload alone is insufficient. |

Keep draft status persistent rather than toast-only. A saved draft is never “synced” or “submitted.” A cached server status is labeled “Last confirmed…” with its time and freshness; newly edited content remains “Not submitted.” On local-storage failure, unsaved memory cannot be promised to survive process termination.

Unsubmitted drafts have no silent expiry or cleanup in this feature. **Discard draft** is a separate, explicit action that names the check and attached photos and allows cancellation. Apply the approved account/security retention policy at integration; surface any recovery limit before it can destroy work. Retain a recoverable copy through confirmed submission and reconcile it with the accepted record before cleanup.

## Camera and photo behavior

Request camera permission only after **Take photo**. Save the note before handing control to the camera. Cancellation returns to the same draft. Denial shows “Camera access is off. You can continue your note,” with **Open settings** when supported and a supported **Choose existing photo** alternative. A restricted device may need an explanation rather than a settings action. Do not repeatedly prompt; recheck capability on return from settings.

An accepted capture appears in a reserved thumbnail area labeled “Saving photo…” until durable copy and draft commit complete, then “Saved on this device.” Failed copy keeps the note and offers retry/retake without a falsely saved thumbnail. A failed upload preserves the local photo. Name photo controls distinctly, such as “Remove photo 1”; use the inspection note as a meaningful description where applicable.

Saving a draft never requires a photo. Whether submission requires one must follow the check’s actual rules: show that requirement before submission and an actionable error if missing. Camera denial must not erase the note or force abandonment.

## Concurrent changes and submission

1. Compare the draft’s base revision with the latest authorized record. A changed version shows a persistent “This check changed since you started. Your draft is safe” message and **Review changes**. Do not interrupt typing with a modal or auto-scroll.
2. Open a full-screen comparison using the existing detail navigation. Keep the check identity anchored. Stack **Your saved draft** and **Latest server version** by changed field; include server-provided author/time when available. For notes offer explicit use-latest, use-mine, or edit-combined choices; identify local and remote photos with explicit include/remove controls for the proposed result. Show the resulting note and photo set before submit. Preserve the original draft and unfinished review choices.
3. Submit the reviewed result conditionally against the latest reviewed revision. If another edit wins during review/submission, retain the composed draft and review the newer changes again. Do not silently apply last-write-wins or text/photo merges. If current record rules prohibit editing, preserve the draft and explain the restriction.
4. Persist an immutable outbound snapshot and operation ID before sending. Suppress duplicate submit while it is unresolved; safe retries refer to the same operation. Back/foreground events never create a submission. Submission can continue beyond this screen. Later edits, if allowed by the existing app, form a new local revision; an older acknowledgement cannot clear or label them submitted.
5. On timeout, query operation/record state. If accepted, show confirmed result; if authoritatively not applied, retry safely against current state using the service’s deduplication contract. A newer record alone is not proof that this attempt succeeded. Definitive rejection preserves the draft and supplies a specific retry, sign-in, validation, or conflict path.

## Motion and accessible behavior

**Motion intent:** stable equipment identity and stable input, with brief local feedback for actual state changes. Reuse the app’s existing navigation/motion primitives; this feature needs no new animation library or scrolling system. The following fallback values are proposals, not observed app behavior.

| Trigger and anchor | Proposed sequence | Interruption and reduced motion |
| --- | --- | --- |
| Open check / review; existing header and tabs | Inherit the app’s route transition. If no standard exists, use direct navigation, with an optional 160 ms ease-out opacity treatment on decorative surface detail. Destination text and controls are available at route commit. | Back/reselect immediately follows the latest route. Reduced motion uses direct navigation. Restore the correct parent and focus even if animation is skipped. |
| Press an action; fixed hit area | Immediate existing pressed state; optional 80 ms color/opacity response. The action starts independently of visual settlement. | Rapid release/cancel returns from the current appearance. Reduced motion keeps direct pressed/selected states. |
| Photo preview becomes available; reserved thumbnail frame | Display the pending preview and its status immediately; optional 120 ms ease-out fade on the image only. No scaling or whole-card movement. | A replaced/removed image cancels the old fade. Reduced motion swaps directly. Missing imagery leaves a stable labeled placeholder. |
| Local save, conflict, pending, failure, confirmed result; status region | Status text changes immediately from application state; optional 100 ms icon fade. No timed success, artificial percentage, shake, or replayed form entrance. | New state supersedes older visual callbacks. Reduced motion uses a direct text/icon swap and static pending text. |

Cancel visual work on route exit, resize, and changed motion preference, leaving the current semantic state usable. Persistence and reconciliation live beyond screen animation lifecycles. Late responses must match the account, check, draft revision, and operation before updating visible state.

- Initial notification entry focuses/announces the check heading and identity. Normal return restores appropriate context. Camera/settings return restores the photo action; comparison navigation focuses its heading. Modal discard confirmation uses the platform’s focus containment and returns focus on cancel.
- Announce meaningful saved/restored, conflict, error, and confirmed states once through platform accessibility APIs. Avoid announcements on every keystroke, percentage, or reconnect retry. Background refresh does not steal focus. Submission validation directs focus to an error summary/first invalid field and keeps valid input.
- Use persistent field labels, textual status plus icons, selected-tab semantics, and keyboard/switch access. Photo actions and conflict decisions have visible buttons; essential behavior never depends on swipe, drag, hover, haptic, or color alone.
- Support large accessibility text, long labels, narrow/short screens, and keyboard-open input. Cards and comparison sections grow and wrap. Ensure focused fields, errors, and actions remain visible above the keyboard/tabs. Verify delivered contrast and platform-appropriate touch targets in their actual units.

## Integration verification required

**Specification reviewed against the supplied scenario. Implementation, rendered motion, persistence, device accessibility, and user testing: NOT RUN.** No app runtime or backend was available. These checks are release conditions for this feature, not claims about the current app.

| Verify with | Acceptance evidence needed |
| --- | --- |
| App owner / existing components | Actual route, tab/back behavior, tokens, transition conventions, photo-required rule, closed/reassigned-record policy, and draft retention/security policy. |
| Local storage / real lifecycle | Offline note + photo survive tab exit, camera handoff, backgrounding, process termination, and relaunch after acknowledged save. Exercise storage-full, interrupted write, missing temporary asset, and account switch; no false saved label or cross-account draft. |
| Backend integration | Version preconditions prevent lost updates; submit/attachment finalization and operation deduplication are authoritative. Test a second inspector editing before return and again during review. Confirm timeout-after-commit recovers once, without a duplicate or premature success. |
| Notification / permissions on supported devices | Cold/warm launch targets the correct check; expired sign-in, stale/missing record, offline cache miss, camera denial/restriction/revocation, picker cancellation, and settings return preserve valid work and safe navigation. |
| Accessibility / layout on supported devices | Screen reader, keyboard/switch, large text, long content, safe areas, keyboard overlap, contrast, and target sizing. Verify reading/focus order and sparse truthful announcements through conflict review and recovery. |
| Rendered temporal review | Normal speed and rapid repeat/back at start, midpoint, and end; leave during upload; late responses; return; orientation change; reduced-motion preference changed mid-transition. Confirm stable targets, immediate readability/input, cleanup, and accurate final state. |

Minimum end-to-end proof: notification → offline note/photo → acknowledged device save → leave/terminate → second inspector changes record → reconnect/restore → review → explicit submit → lost response → reconciliation → one server-confirmed result with the draft still recoverable until reconciliation completes.
