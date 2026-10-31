# Design evaluation

The [graphic-design briefs](briefs.json) define twelve realistic tasks and the [UI/UX briefs](ui-ux-briefs.json) add twenty interface cases. The [QA briefs](qa-briefs.json) add five scoped execution and handoff exercises. Definitions are not completed tests. Automated repository checks validate their structure, not the quality of designs an agent might produce.

## Run an execution case

1. Select a brief and supply every required fixture. Several cases explicitly require an image, document, or source file from the evaluator; missing fixtures are not evidence of a skill failure.
2. Start an agent with fresh context. Provide the task, approved facts, constraints, fixtures, and path to the skill. Keep `expected_behaviors` and `failure_signals` for the evaluator.
3. Give the agent access to the actual tools available for the run. Record relevant capability limits. Do not secretly provide an expected aesthetic or the diagnosis of a flawed input.
4. Retain the visible roughs, final artifacts, source files, brief, and actual inspection notes.
5. Review against the brief at composition, actual-size, and detail levels. Verify content and production separately.
6. Record observations, failures, corrections, rechecks, and what remains untested. Another agent's critique is not a human audience study.

## Run a reasoning case

Use a fresh context with the problem statement and constraints. Assess whether the agent distinguishes evidence, inference, and missing information, then proposes concrete next actions. A strong explanation does not prove that the agent can execute the design. Keep reasoning cases separate from artifact-creation cases in reports.

## Scoring discipline

Use strong, adequate, or weak when helpful for aesthetic quality, fit, communication, distinctiveness, craft, and coherence. Require actual viewing for artifact judgments; a concise visual preference is valid without a measured benefit. Record technical checks as PASS, FAIL, NOT RUN, or N/A. Do not let a high aesthetic judgment offset a critical defect or treat a technical pass as proof of beauty.

Do not expect a particular palette, font, period, or layout. Different successful approaches are valid. Test for a meaningful concept, appropriate execution, truthful verification, and adaptation to the specific brief.

For aesthetic-review cases, supply the actual visuals and withhold the evaluator's preferred direction. Either restrained or expressive work may be selected. Examine whether the agent looks at the whole, recognizes what to preserve, distinguishes preference from failure, and proposes proportionate corrections. Do not award a pass simply for repeating that beauty matters, or require a particular winner as hidden ground truth.

## Current evidence

See [validation-2026-10-31-creative-direction.md](validation-2026-10-31-creative-direction.md) for the open-brief refinement and two fresh-context written handoffs. They test creative planning across a storefront and a brand guide, not rendered visual quality or browser behavior. Keep these outputs out of future fresh-agent context unless they are explicit fixtures.

See [validation-2026-10-31-qa.md](validation-2026-10-31-qa.md) for the package audit, five fresh-context exercises, retained original fixtures and outputs, failures, corrections, and unexecuted browser checks. The [curated examples](examples/qa-2026-10-31/README.md) are regression material, not new design defaults or production-ready application claims. Keep them out of fresh-agent context until evaluation is complete.

See [validation-2026-10-18.md](validation-2026-10-18.md) for the initial implementation's recorded automated checks and selected design exercises. Its limits are part of the result, not an invitation to infer universal reliability.

See [validation-2026-10-30.md](validation-2026-10-30.md) for the UI/UX extension's checks and fresh-context exercises. Test composition specificity alongside task completion and preservation: an agent that removes useful controls to look original has not passed. Include the explicit-user exception and narrow-maintenance cases to catch over-application of the hero constraints.

For owner-taste cases, test interpretation and transfer rather than exact visual imitation. The reference-boundary case requires raw images; the cross-dashboard case tests written specification only. Preserve current project identity, keep valid task conventions, and check that the selected reference set has not become a universal palette or silhouette.

For joint-motion cases, supply both skills and the named raw stills without evaluator diagnosis. Evaluate coordinated decisions, reference honesty, and transaction semantics. A reasoning pass does not prove animation execution; temporal QA requires a later running prototype and actual playback/input evidence.

For temporal-reference cases, supply the named original clips and both skills, without analysis notes or evaluator expectations. Check sampled evidence, identity/crop continuity, readability versus settlement, and state truth. These written exercises evaluate transfer and specification only; normal-speed runtime and input checks remain separate.
