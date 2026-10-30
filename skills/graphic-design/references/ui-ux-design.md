# UI and UX design: task, structure, and visual system

Use for websites, apps, dashboards, portals, and reusable interface systems. Read [interaction and validation](interaction-and-validation.md) before specifying behavior, and [interface originality](interface-originality.md) before choosing a new visual direction. These are practical design instructions, not a fixed style or proof of usability.

## Contents

- [1. Define the experience](#1-define-the-experience)
- [2. Organize information around decisions](#2-organize-information-around-decisions)
- [3. Choose patterns by their job](#3-choose-patterns-by-their-job)
- [4. Compose an interface with purpose](#4-compose-an-interface-with-purpose)
- [5. Establish a small coherent system](#5-establish-a-small-coherent-system)
- [6. Adapt to real devices and content](#6-adapt-to-real-devices-and-content)
- [7. Use language and evidence honestly](#7-use-language-and-evidence-honestly)
- [8. Decide with evidence](#8-decide-with-evidence)

## 1. Define the experience

Start with the user, their immediate task, their context, and the outcome they can recognize. Separate business goals from user goals. A business may want registrations; a visitor may need to establish whether a service covers their area before creating an account. Give that visitor a useful answer.

Capture only the unknowns that change the design:

| Decision | Useful question |
| --- | --- |
| Primary task | What brought this person here, and what counts as finished? |
| Mental model | What words, objects, sequence, and expectations do they already use? |
| Context | Are they learning, comparing, acting under time pressure, or repeating expert work? |
| Constraints | What data, permissions, device, connectivity, language, and assistance are available? |
| Risk | What can be misunderstood, lost, duplicated, or committed accidentally? |
| Evidence | Which needs are observed, supplied by the user, inferred, or still unknown? |

Write one primary task and a few necessary secondary tasks. Trace entry, orientation, action, feedback, completion, and return. Include at least the most consequential failure or interruption. Inventory existing routes, components, tokens, and behavior before adding another system. Preserve familiar working behavior during a visual redesign.

Use Nielsen's heuristics as a review lens: understandable status, familiar language, consistency, control, recognition, error prevention, recovery, and relevant help. They are broad heuristics, not a substitute for observing users. [U3 in the sourcebook](sourcebook.md#ui-and-ux-evidence).

## 2. Organize information around decisions

Group by relationships people need to understand, not by the available component library. Separate global navigation, local navigation, and actions on the current object. Use stable labels and visible current location. Keep the primary route discoverable; search or a command palette can supplement navigation, not conceal it.

Make task priority visible. A work queue should expose what needs attention and why. A personal dashboard should help someone continue or act, not open with four interchangeable KPI tiles because space is available. A metric needs a meaningful time window, unit, comparison, and a next action where relevant.

Use progressive disclosure for secondary detail or advanced settings. Keep costs, consequences, essential instructions, and critical choices visible before commitment. Do not hide required actions in hover states, mystery icons, or tooltips. An info icon can explain a term; it cannot carry the only explanation of a fee or failure.

Distinguish navigation from selection. Tabs switch related views; filters constrain a collection; segmented controls choose a mode; buttons perform actions. Do not make all four look identical. Preserve filter, sort, pagination, and return position when users inspect an item and come back. Use deep links when a view should be shareable or restorable.

## 3. Choose patterns by their job

| Situation | Starting choice | Check before using it |
| --- | --- | --- |
| Compare many records across attributes | Table or aligned list | Useful columns, sort state, row actions, selection scope, small-screen access. |
| Browse visual items | Image-led collection | Comparable imagery, meaningful metadata, loading behavior, clear item destination. |
| See related summaries with different importance | Grouped panels or bento composition | Size follows importance or content; no arbitrary card packing or nested card borders. |
| Inspect an item while retaining a queue | Master-detail view or side panel | Selected item remains identifiable; Back and focus behavior; full-page route when needed. |
| Short contextual edit or consequential confirmation | Dialog | Narrow scope, clear title, focus lifecycle, escape/cancel, no stack of dialogs. |
| Long, complex, or shareable task | Dedicated page | Enough room, progress where useful, saved state and return route. |
| A small number of known choices | Radio group or appropriate native control | Visible labels, sensible default only when justified; never silently opt into commitments. |
| Many known choices | Searchable selection | Keyboard interaction, no-results state, selected value, and ability to change it. |
| Pick a date or plan time | Suitable date input, calendar, or agenda | Timezone, unavailable dates, keyboard access; offer usable text entry where appropriate. |
| Work across time slots | Calendar plus agenda/detail view | Overlaps, small screens, local date format, selected day, current time, and edit/recovery flow. |

Choose the least elaborate pattern that satisfies the actual task. A bottom sheet, command palette, or multistep wizard is not automatically more modern than a page or form. Avoid rebuilding a mature native control without a concrete need and a plan to implement its semantics.

## 4. Compose an interface with purpose

Establish the most important information, the next decision, and the supporting evidence before choosing a grid. Layout should express their relationship. Separate acquisition pages from working interfaces: many authenticated screens should start directly with the task, not a hero.

On a task-oriented entry, inspect how much scrolling precedes the first useful choice at the shortest supported viewport. Remove redundant introductions, repeated instructions, and duplicate step headings. Keep the context needed for an informed decision; do not force everything above the fold or shrink essential text to make it fit.

Use proximity and common alignment to group. Increase separation between groups more than within them. Combine differences in scale, weight, position, and whitespace deliberately. Keep an appropriate reading width for prose while using available space for comparison or work. Treat line length and spacing as tested choices, not magic ratios.

Create a clear first focus without making every heading oversized. A display headline can be expressive; form labels, navigation, numeric values, and dense operational text need consistent reading rhythm. Inspect the actual longest label, numeral formatting, language glyphs, and line breaks. Do not force center alignment onto long text to avoid the banned hero formula.

Give imagery a job: demonstrate the product, establish a meaningful setting, show work, compare states, or explain a process. A floating dashboard miniature that cannot be read and communicates nothing specific is decoration. Do not invent product capabilities to make a convincing screenshot.

Use cards when containment explains a unit or action. Use plain rows, dividers, spacing, typography, or shared surfaces when these communicate better. Neither borderless bento nor brutalist typography is a universal answer. Maintain a deliberate relationship between page margins, section rhythm, panel padding, and control spacing across related routes.

## 5. Establish a small coherent system

Reuse the current system when it works. For new work, define semantic roles before many tokens:

- Text: display, heading, body, label, supporting text, numeric data.
- Color: canvas, surface, primary text, muted text, border, action, focus, and semantic feedback.
- Spacing: a short repeatable scale, with optical exceptions documented where they matter.
- Shape and elevation: distinguish containment, interactive affordance, overlays, and hierarchy.
- State: hover, focus-visible, pressed, selected, loading, disabled, error, and success.

Use shared components for repeated behavior and variants for real differences. Avoid one-off padding and radius values on every page. Avoid abstracting a one-time composition into an elaborate system before reuse exists. Specify content limits and interaction states with each important component, not just its default appearance.

Keep one icon family or a deliberate compatible set; match optical size, stroke, fill, baseline, and meaning. Label unfamiliar actions. Use accessible names for icon-only controls and adequate hit areas regardless of glyph size. Do not treat decorative icons as a substitute for content or differentiation.

Dark mode needs its own surface hierarchy, image treatment, and contrast review. Do not invert colors mechanically or add a theme toggle solely to make a prototype feel complete. Match the requested scope.

## 6. Adapt to real devices and content

Design content-driven breakpoints. Specify what reorders, wraps, collapses, becomes scrollable, or changes presentation, and why. A desktop composition stacked into a long mobile column is not automatically a good mobile experience.

- Preserve task priority and coherent DOM/reading order across layouts. Avoid visual reordering that makes keyboard navigation confusing.
- Test narrow phones, intermediate widths, large screens, short landscape viewports, zoom, long names, large numbers, and empty or overflowing collections.
- Keep page gutters consistent and avoid fixed heights that clip content. Use the entire useful mobile width with appropriate spacing.
- Reserve space for fixed navigation, cookie notices, safe areas, and the on-screen keyboard. Ensure focused fields and final actions remain reachable.
- Use independent sidebar or panel scrolling only when it preserves a useful persistent workspace. Make scroll ownership obvious and avoid trapped nested scroll regions.
- Retain comparison semantics for data tables. Use column priority, row detail, or a labeled scroll region as appropriate; do not silently remove information or automatically turn every row into a huge card.
- Support touch and keyboard without relying on hover. Let people dismiss, go back, and resume without losing their place.
- Treat localization as layout input: expansion, bidirectional text where relevant, names, decimal conventions, currencies, dates, and timezones. Do not assume every locale shares the same formatting or word length.

For web reflow, WCAG 2.2 SC 1.4.10 uses 320 CSS px for vertically scrolling content, with exceptions for content that needs a two-dimensional layout. This is a test condition, not a universal device breakpoint. [U5 in the sourcebook](sourcebook.md#ui-and-ux-evidence).

## 7. Use language and evidence honestly

Use specific labels for the result of an action: saving a draft, sending an invitation, or requesting a quote are different commitments. Explain consequences before destructive or costly actions. Use language people use for their work, not database names or implementation errors.

Write useful empty states: explain what is absent, distinguish a fresh account from filtered-out results, and provide a relevant next step. An illustration is optional. Avoid celebration on a failure screen and filler greetings that push important work down.

Show real proof where available. Never fabricate ratings, customer logos, testimonials, usage counts, prices, trend arrows, availability, or research findings. Label synthetic fixtures in internal prototypes and keep them out of production claims. Missing proof calls for honest content, not decorative credibility.

Avoid manipulative defaults, hidden fees, fake scarcity, forced consent, obstructed cancellation, and language that shames declining. Treat accessible recovery and honest status as part of design quality.

## 8. Decide with evidence

Connect each consequential choice to a task, content relationship, known constraint, observed reference mechanism, or testable hypothesis. Use a short decision record when needed: choice, reason, tradeoff, and how to check it.

Define an observable success criterion for the primary flow, such as finding the relevant item, completing an edit, understanding the confirmation, or recovering without re-entry. With representative participants available, observe task completion, mistakes, uncertainty, and recovery. Ask neutral questions and report the actual sample and conditions. Do not turn an agent walkthrough into user research or claim conversion improvements without measurement.

Apply the [reference study method](interface-reference-study.md) to discover alternatives and [interaction verification](interaction-and-validation.md#6-verify-the-experience) to inspect the result. A beautiful screenshot and a persuasive rationale do not establish a successful experience.
