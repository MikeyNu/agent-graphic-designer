# SaaS dashboards and working interfaces

Use for recurring work in analytics, operations, administration, finance, support, and collaboration products. Read with [UI and UX design](ui-ux-design.md) and [interaction and validation](interaction-and-validation.md). These instructions are practical design synthesis. The [SaaS and mobile study](saas-mobile-reference-study.md) supplies bounded visual examples, not proof of product outcomes.

## Contents

- [1. Start with the work and its scope](#1-start-with-the-work-and-its-scope)
- [2. Make dashboards answer questions](#2-make-dashboards-answer-questions)
- [3. Design collections for comparison and action](#3-design-collections-for-comparison-and-action)
- [4. Preserve context through detail and change](#4-preserve-context-through-detail-and-change)
- [5. Make collaboration and administration legible](#5-make-collaboration-and-administration-legible)
- [6. Craft dense interfaces](#6-craft-dense-interfaces)
- [7. Verify a working sequence](#7-verify-a-working-sequence)

## 1. Start with the work and its scope

Identify the user's role, recurring decision, relevant objects, cadence, and cost of a mistake. Distinguish monitoring, investigation, triage, creation, and administration. A returning operator may need a queue immediately; an analyst may need comparisons; a new workspace may need setup. Do not impose a greeting, hero, four KPI cards, and chart grid on all three.

Make the active organization, workspace, project, and environment distinguishable where they change meaning or authority. Do not assume a profile menu sufficiently identifies which organization will be affected. Keep durable object identifiers available when names are duplicated. Display only the context relevant to the task instead of repeating every hierarchy level everywhere.

Scope navigation and filters explicitly. A date filter may affect a chart while the approval queue shows all outstanding work; explain that difference. On workspace changes, prevent actions, selections, cached details, and unsaved drafts from silently applying to a different tenant. Revalidate access before showing sensitive records or committing changes. Interface visibility is not authorization enforcement.

Define what people can recognize as finished: resolving an exception, locating a changed cost, assigning a job, or approving a request at their stage. A clicked button or transient toast is insufficient if the object has not reached the promised state.

## 2. Make dashboards answer questions

Choose the information architecture from the question:

| User question | Useful structure | Required context |
| --- | --- | --- |
| What needs attention now? | Prioritized queue with reason, owner, deadline, and next action | Explain urgency and exclusions; keep routine work reachable. |
| What changed? | Time series and comparable baseline, then relevant breakdown | Units, interval, timezone, missing data, and comparison period. |
| Why did this happen? | Diagnostic panels sharing scope, annotated events, links to records | Correlation is not causation; disclose aggregation and incomplete evidence. |
| Are we within a limit? | Actual versus budget, threshold, or service objective | Period, threshold source, forecast assumptions, and consequences. |
| What should I do next? | Work list or task-specific recommendation with evidence | Explain the reason, available action, authority, and uncertainty. |

Apply the metric-definition checks in the general UI guide. Distinguish zero, unavailable, not applicable, and still loading. Show freshness close to decisions that depend on it; a global sync label must not imply every widget is equally current. Separate observed values, estimates, and forecasts.

Compare like with like. A partial month against a complete previous month needs an explicit basis, such as matched elapsed days or a clearly labeled forecast; do not silently imply equal exposure. Define whether a percentage change is relative change or percentage points. Do not sum different currencies or incompatible populations into a plausible-looking total.

Choose encodings by the comparison. Aligned positions and bars can support comparisons; a line can reveal change over ordered time. Start quantitative bars at zero unless a clearly explained exception is justified; explain nonzero line-chart axes when material. Do not hide uncertainty in smoothing or invent interpolated observations. Keep hover values accessible by other means and provide useful summaries or data access.

Let a chart lead to the relevant records without losing its scope. Keep units, legends, axis labels, and annotations legible at delivered size. Distinguish quantitative encoding from ornament: decorative radial forms, dimensionality, and gradients can add aesthetic pleasure, but must not distort values or imply data they do not represent. A number presented as a metric needs an interpretable meaning. Never claim a specific chart choice improves business outcomes without evidence.

## 3. Design collections for comparison and action

Start with the attributes needed to choose the next record. Use a table when cross-row comparison matters, a list when sequence dominates, and a board when stage and movement matter. Offer more than one view only when the task warrants the maintenance and learning cost. Do not turn rows into giant cards merely to look modern.

- Put identity, decision-critical status, and the next action where scanning reveals them. Align numeric values consistently and distinguish missing values from zero. Let long names wrap or reveal their full value without making hover the only route.
- Distinguish a row's navigation target, selection checkbox, and contextual actions. Avoid nested interactive targets and accidental actions when selecting text. Preserve usable keyboard order.
- State search scope, applied filters, sort order, result count, and pagination or loading behavior. Separate a new empty account, no matches, loading, service failure, and permission-limited results. Do not report a truncated total as complete.
- Preserve filter, sort, page or cursor, selected record, and scroll position when returning from detail. Saved views should say whose preferences they change; make unsaved changes understandable.
- Define selection across pagination and filtering. “Select 25 on this page” differs from “Select all 312 matching requests.” Show count and scope, provide Clear, and explicitly reconcile selections when filters or workspace change.
- Before consequential bulk work, summarize affected scope and exceptions. Separate completed, failed, skipped, and unknown outcomes by record. Retry only the safe unresolved subset after checking its current state; never rerun an entire financial batch blindly.

Large collections need useful loading and navigation, not just performance tricks. If rows are virtualized, test focus, selection, assistive-technology access, find behavior, and return restoration in the actual implementation. Offer export only when authorized and supported; do not imply it includes unavailable data.

## 4. Preserve context through detail and change

Use an inspector for brief work that benefits from a visible queue; use a dedicated route when the task is long, complex, or shareable. On narrow screens, a focused detail view can replace side-by-side panels. Keep object identity, applied context, Back behavior, and return position consistent. Avoid stacked drawers and dialogs with ambiguous ownership.

Place decision evidence next to the action: current value, proposed change, relevant policy, responsible person, affected scope, and downstream effect. Give actions specific labels when the commitment warrants it. An approval stage, payment scheduling, and payment completion are distinct states. An exception routed to another reviewer is not final approval.

Recheck stale or concurrently changed records before commitment. Show what changed and let the person reconsider. Do not overwrite another person's update silently or lose a valid draft after session renewal. Distinguish optimistic local feedback from server-confirmed state. For a timeout with an unknown outcome, reconcile status before offering retry.

Design rejection, return-for-information, cancellation, escalation, and permission loss where relevant. Preserve the user's reason and legitimate input. A disabled action needs an understandable reason and a useful path where one exists; it should not expose confidential policy or records. Offer undo only when the operation can actually be reversed, with the time limit and consequences clear.

After completion, update the affected queue, counts, detail state, and history consistently. If an item leaves the filtered view, explain where it went and move focus to a sensible place. Keep a durable confirmation or record when the user needs to revisit the result.

## 5. Make collaboration and administration legible

Separate personal preferences from workspace-wide settings. Show the affected account, plan, billing period, currency, seats, and effective date when those facts are supplied and relevant. Preview consequential changes without inventing prices or billing rules. Cancellation, downgrading, and removing access need understandable consequences and recovery where available.

For invitations and roles, distinguish pending invitation from active membership, explain permission scope, and make revocation status visible. Reflect actual backend policy; do not assume a viewer can become an administrator through a UI toggle. Avoid exposing sensitive information in previews, activity feeds, or exports.

Use audit history to answer who changed what, when, and with what result, within the viewer's access. Separate human actions from automation. Resolve timezone ambiguity and retain stable record links. A decorative activity feed is not an audit trail.

For AI-assisted work, distinguish generated proposals, cited source material, user edits, and committed actions. Let people inspect evidence, correct the proposal, and reject or cancel it. Show uncertainty and source limits where they affect a decision; never use an invented confidence percentage as a substitute for evidence. Failure or cancellation must leave the work in an understandable state.

## 6. Craft dense interfaces

Spend space on relationships and readable decisions. Use shared baselines, consistent row rhythm, semantic type roles, restrained dividers, and predictable action placement. Allow sufficient target area without inflating every row into a promotional card. Differentiate selected, focused, hovered, disabled, warning, and error states with more than subtle hue changes.

Reserve strong accents for meaningful emphasis rather than coloring every metric. Keep status and magnitude distinct: a rising cost is not automatically a green success. Use tabular numerals where they improve comparison. Inspect realistic magnitudes, long labels, multi-line rows, and empty cells.

Allow a beautiful or playful visual system around these requirements. Rich color, distinctive typography, material, illustration, and pleasing small interactions can belong in SaaS without proving a productivity gain. Judge their actual effect on the composition and the task. Protect truthful chart encodings, readable values, and operable controls with local adjustments; do not strip the product to a neutral template by default.

Reuse navigation and repeated task patterns across the product. Originality can come from unusually clear task fit, domain language, information hierarchy, and thoughtful detail. It does not require making a familiar table, settings page, or search control look unfamiliar.

## 7. Verify a working sequence

Trace a representative person from the real entry point through finding a record, understanding evidence, taking action, receiving a verified result, and returning to work. Include the highest-risk exception. In addition to the general verification guide, inspect:

| Condition | Evidence to seek |
| --- | --- |
| Workspace and role change | Correct data scope; old selection and pending actions cannot leak into the new context. |
| Partial period, stale widget, missing source | Honest units, comparison basis, freshness, and incomplete totals. |
| Pagination, filters, bulk action | Explicit selection scope, per-record results, safe recovery, stable return context. |
| Concurrent change or session expiry | Revalidation, preserved permitted input, no premature success. |
| Dense or narrow content | Readable values, reachable actions, deliberate scroll ownership, useful detail view. |
| Keyboard and assistive technology | Operable controls, understandable table semantics, focus after removed or updated rows. |

Record specified, simulated, and verified behavior separately. A screenshot can demonstrate hierarchy; it cannot prove permission enforcement, accurate live metrics, concurrency handling, or persistence.
