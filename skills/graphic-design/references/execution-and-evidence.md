# Execute the requested scope and keep evidence traceable

Use when deciding how much work to do, adapting the workflow to available tools, or reviewing whether a result is actually complete. This is a practical execution guide, not another visual style or approval process.

## Start with a compact contract

Record the requested deliverable, approved material to preserve, facts that must be exact, difficult use condition, and checks that can establish completion. A few sentences usually suffice. Ask only when a missing fact materially changes the result and cannot be recovered from available context. Continue independent work while it is unresolved. Do not invent dates, prices, addresses, rights, research, or live product capability.

Follow the user's current scope and explicit direction, then approved project identity and references, then the skill's defaults. An unrelated maintenance fix preserves an approved hero even if that hero would be excluded by the owner's defaults for new work. New concepts are appropriate for a substantial new direction, not a typo correction, a selected design, or a requested faithful reconstruction.

For substantial new work, compare three visible roughs at comparable fidelity before polishing. They must differ in organizing relationship, not only finish. A code file nobody has rendered is not a visible rough. If rendering is unavailable, useful source and concept specifications may still be delivered, but label the missing inspection and do not claim the exploration was visually evaluated.

## Use a small state model before building behavior

For the primary flow, write the states and events that affect truth, navigation, and recovery. Separate the selected object, local draft, pending operation, confirmed result, and visual animation. A local demonstration can simulate outcomes, but label the simulation and never use its timer as evidence of a real service result.

Preserve a stable identifier and current request identity across asynchronous work. Late results must not replace a newly selected object or newer intent. Define whether a navigation leaves an operation running, cancels it, or preserves a draft. Returning must restore meaningful context without replaying the action. Keep semantic state and input readiness independent of animation-completion callbacks.

Include suspension and return when the platform can preserve a page or view. Canceling an effect must also settle transient guards, overlays, and body locks, or leave a deliberate resume path. Test leaving during close and returning, not only rapid toggles while the page stays active. Preserve the intended selection and data; do not replay submissions. A synthetic lifecycle event tests handler logic, not a real browser cache restoration. See the [lifecycle evidence](sourcebook.md#qa-and-lifecycle-evidence).

Use one shared UI/motion contract. A narrow feature can inherit an approved visual system and tested motion tokens; it does not need three new identities, a new framework, or a motion library.

## Choose checks by what they can establish

| Evidence | Can establish | Cannot establish alone |
| --- | --- | --- |
| Source/metadata inspection | Copy, declared dimensions, code paths, dependencies, and some structural errors. | Actual appearance, font fallback, clipping, playback, or task completion. |
| Rendered static artifact | Appearance at the captured size, layout, and visible copy. | Interaction, continuous motion, persistence, or other unobserved variants. |
| Isolated logic tests | Tested state transitions and error handling under named fixtures. | Real browser focus, layout, pointer/keyboard behavior, platform integration, or service success. |
| Executed browser/device flow | Observed behavior under the tested environment, inputs, and conditions. | Untested devices, full accessibility conformance, or representative human usability. |
| Temporal observation | The actual inspected sequence and interruption behavior. | Exact historical easing/library from visual similarity, or performance figures without measurement. |
| Representative human study | Observations from the stated participants and task. | Universal preference, conversion effects, or population-wide conclusions without appropriate evidence. |

For each material check record `artifact/version | condition | method | expected result | observed result | status`. Use PASS, FAIL, NOT RUN, or N/A, with a reason for N/A. Keep implementation stage separate from verification status: a prototype may have tested local behavior while service integration remains outside scope.

Validate the test harness as well as the product. A token pair does not establish the actual background behind a control. A zero-overflow result does not establish readable labels or reachable content inside a fixed panel. Record whether a screenshot shows the visible viewport or a full-page composite. For text-size tests, capture all original computed sizes before applying changes so inherited values are not multiplied repeatedly. When keyboard focus leaves the document for browser controls, distinguish that from focus escaping a modal into the background page. Diagnose unexpected results before changing product behavior or relaxing an assertion.

For a native modal dialog, do not add a custom Tab trap solely to satisfy an assertion that every active element must stay inside the DOM dialog. Record the active element and whether the document has focus, check the next Tab, and verify that background-page controls remain inert. Browser chrome receiving focus is different from a background control receiving focus. Preserve native behavior unless a reproduced product requirement justifies changing it.

## Missing capabilities and failure

Inspect available tools before committing to a format or verification claim. Use an appropriate permitted alternative when it preserves the requested deliverable. Do not silently replace editable vectors with a raster or a working application with prose. If a capability is blocked by host policy, respect the boundary; do not route around it through another browser, tunnel, hidden runtime, or deployment.

Mark the affected check NOT RUN with the concrete reason. Finish useful independent work, preserve editable sources and reproducible instructions, and state the delivery status accurately. A written handoff can be complete as a handoff while runtime checks remain unexecuted. A functioning local simulation is still a prototype. A missing material production check prevents claiming production readiness, not delivery of a clearly labeled review draft.

## Fix and stop

Distinguish a brief violation, factual error, broken task, or applicable accessibility failure from an aesthetic suggestion. Correct the specific defect while preserving the design's strengths. Recheck the changed output and affected shared behavior; do not repeat every unrelated test after a local correction.

Deliver when the requested scope is met and its applicable checks pass, or clearly identify a remaining external blocker and the useful completed result. Do not average blockers into a positive overall score. Do not promise that a skill or checklist guarantees correct results on every future brief.
