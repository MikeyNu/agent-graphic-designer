# Agent Graphic Designer

A research-informed graphic design and UI/UX skill for agents that can inspect references, create visual artifacts and interfaces, and iterate on the result. It combines art direction, proactive image and illustration generation, coherent iconography, typography, color, composition, coordinated UI motion, task-centered interaction design, responsive behavior, and rigorous asset, visual, temporal, functional, and production QA.

**Start with [the skill](skills/graphic-design/SKILL.md).** Its supporting guides provide the depth needed for difficult decisions without loading an entire design manual for a small edit.

The goal is beautiful, distinctive work suited to a particular product and audience. Beauty, atmosphere, play, and visual intuition are legitimate design goals alongside clarity and usability. The skill does not promise infallible taste, universal psychological effects, automatic audience validation, or client approval.

Its central purpose is to bridge an incomplete prompt and a considered visual result. A request such as “create a beautiful website for my clothing business” delegates art direction: the agent should develop the missing creative brief, explore a subject-specific identity, and resolve composition, assets, typography, color, iconography, and motion together. The same responsibility applies to brand guidelines, campaigns, documents, and graphics. Thoughtful unrequested touches belong within the design task. The user should not need to prescribe every asset or effect. See [creative direction](skills/graphic-design/references/creative-direction.md).

The agent should identify and create appropriate assets without a separate image request. It chooses transparent foreground art or opaque scenes according to the composition, uses a coherent existing icon family for controls, and inspects actual pixels and integrated screens. Rich illustration can be generated 2D art; custom SVG is no longer the implied default. The generation and production-quality workflows are integrated from [Visual Asset Pipeline](https://github.com/MikeyNu/visual-asset-pipeline-plugin) and [Agent AI Detector](https://github.com/MikeyNu/agent-ai-detector), with [pinned source attribution and notices](skills/graphic-design/references/integrated-source-notices.md). No separate installation of those packages is required.

## Use it

### With an agent that can read this repository

Give the agent the repository URL and this instruction:

> Use the graphic-design skill in this repository. Read skills/graphic-design/SKILL.md and the guides relevant to the task. Create the actual design, inspect rendered results, compare meaningful alternatives where appropriate, correct defects, and report the checks you really performed. My brief is: [your brief].

Provide the audience, message, required copy, size or placement, brand assets, constraints, and delivery format when known. Missing reversible preferences should not trigger a long questionnaire. Dates, prices, contact details, or other facts must not be invented.

A repository URL does not by itself mean the files have been read or that graphics tools are available. The agent should inspect the files and use the capabilities available in its environment.

### With a directory-based skill installer

Install the complete [skills/graphic-design](skills/graphic-design) directory using your agent's supported skill-installation process. Keep its `references`, `scripts`, `assets`, and `agents` subdirectories together. Where named skill invocation is supported, use `$graphic-design`.

### As one Markdown attachment

Build a portable document containing the core instructions, reference guides, and templates:

```bash
python3 scripts/build_portable_skill.py --output /tmp/GRAPHIC_DESIGN_SKILL.md
```

Attach the generated document with your brief. The document links back to executable tools in this repository; attaching Markdown does not install Python packages or supply tool access. Use the modular package when possible so only relevant material needs to be loaded.

## What is included

| Component | Purpose |
| --- | --- |
| [Core skill](skills/graphic-design/SKILL.md) | Brief, research, concepts, construction, critique, verification, and delivery. |
| [Creative direction](skills/graphic-design/references/creative-direction.md) | Complete open briefs, develop subject-specific ideas, make useful unrequested decisions, and carry an identity into brand guidelines. |
| [Execution and evidence](skills/graphic-design/references/execution-and-evidence.md) | Task scope, approved-direction preservation, honest verification, missing capabilities, recovery, and completion. |
| [UI and UX design](skills/graphic-design/references/ui-ux-design.md) | User tasks, information architecture, pattern selection, visual systems, responsive behavior, and content. |
| [SaaS product design](skills/graphic-design/references/saas-product-design.md) | Trustworthy dashboards, dense collections, bulk actions, permissions, collaboration, and return context. |
| [Mobile app design](skills/graphic-design/references/mobile-app-design.md) | Focused tasks, navigation, device input, interruption, offline states, and actual-device verification. |
| [Interaction and validation](skills/graphic-design/references/interaction-and-validation.md) | Complete flows, states, recovery, accessibility, motion, performance, and actual verification. |
| [Interface originality](skills/graphic-design/references/interface-originality.md) | Explicit hero constraints, repetitive-layout diagnosis, meaningful alternatives, and whole-page critique. |
| [UUPM demo comparison](skills/graphic-design/references/template-convergence-study.md) | All 39 gallery previews and twelve full-page compositions, recurring formulas, useful exceptions, evidence limits, and concrete repairs. |
| [Owner's design taste](skills/graphic-design/references/owner-design-taste.md) | A flexible preference profile covering integrated imagery, shaped surfaces, typography, color, rhythm, and appropriate task conventions. |
| [20-reference close study](skills/graphic-design/references/owner-reference-study.md) | Individual observations from owner-selected commerce, dashboard, mobile, creative-tool, and account-screen examples, including enlarged detail inspection. |
| [Workspace and settings study](skills/graphic-design/references/owner-workspace-study.md) | Twenty further uploads, nineteen distinct images: analytics, learning, assistants, boards, maps, settings, profiles, and notification matrices. |
| [UI and motion co-design](skills/graphic-design/references/interface-motion.md) | Joint composition and animation, shared contracts, choreography, scroll relationships, reference-video study, and temporal QA. |
| [Interface reference study](skills/graphic-design/references/interface-reference-study.md) | How to study Dribbble, Mobbin, Page Flows, and Recent; dated observations with honest access limits. |
| [SaaS and mobile study](skills/graphic-design/references/saas-mobile-reference-study.md) | Seven focused project observations, including desktop/mobile approval views, diagnostics, CRM, tickets, and content use. |
| [Composition and layout](skills/graphic-design/references/composition-and-layout.md) | Hierarchy, grouping, grids, balance, scale, rhythm, visual tension, and annotated review. |
| [Typography and perception](skills/graphic-design/references/typography-and-perception.md) | Font anatomy, situated emotional associations, specimen testing, multilingual text, and microtypography. |
| [Color and accessibility](skills/graphic-design/references/color-and-accessibility.md) | Contextual palette development, color psychology limits, contrast, and color management. |
| [Originality and trends](skills/graphic-design/references/originality-and-trends.md) | Current-practice research, historical reinterpretation, concept experiments, and avoiding generic AI output. |
| [Asset creation](skills/graphic-design/references/asset-creation.md) | Proactive visual opportunities, native image generation, alpha/scene decisions, actual files, responsive integration, and repair. |
| [Iconography](skills/graphic-design/references/iconography.md) | Existing icon families, semantic mapping, optical consistency, accessible controls, and selective custom construction. |
| [Asset quality](skills/graphic-design/references/asset-quality.md) | Whole/native/context inspection, synthetic defects, transparent edges, family consistency, and targeted remediation. |
| [Image prompting](skills/graphic-design/references/image-prompting.md) | Concrete construction and composition, reference roles, model-aware exclusions, controlled repairs, and prompt pitfalls. |
| [Quality and production](skills/graphic-design/references/quality-and-production.md) | Visual review, content accuracy, raster/vector/print checks, evidence, and release status. |
| [Sourcebook](skills/graphic-design/references/sourcebook.md) | Research and primary-source references with dates, precise support, and limitations. |
| [QA tools](skills/graphic-design/references/tools.md) | Contrast calculation, metadata/hash/alpha preflight, cutout pixel checks, and self-contained visual review boards. |
| [Templates](skills/graphic-design/assets) | Brief, concept comparison, honest QA record, and handoff. |
| [Evaluation briefs](evals/briefs.json) | Twelve realistic task definitions with expected behavior and failure signals. |
| [UI/UX evaluation briefs](evals/ui-ux-briefs.json) | Twenty interface tasks covering composition, workflow, accessibility, preservation, SaaS operations, mobile interruptions, aesthetic judgment, owner-taste transfer, joint motion design, template convergence, and research honesty. |
| [Executed examples](evals/examples/README.md) | Original poster, annotated flyer correction, visible concept studies, and actual QA evidence. |
| [QA exercise definitions](evals/qa-briefs.json) | Five scoped creation, repair, prototype, and handoff cases, with evaluator-only expectations. |
| [Asset exercise definitions](evals/asset-briefs.json) | Eleven proactive generation, icon repair, alpha, construction, prompting, capability, family, and layout cases. Definitions are separate from executed evidence. |
| [31 October QA and retained cases](evals/validation-2026-10-31-qa.md) | Fresh-context artifact exercises, actual defects and corrections, automated regressions, and explicit browser limits. |
| [31 October asset integration QA](evals/validation-2026-10-31-assets.md) | Three fresh-context tasks with proactive transparent art, opaque scenes, and icon repair, tested in the local desktop browser. |
| [Retained asset examples](evals/examples/asset-integration-2026-10-31/README.md) | Working source, actual generated assets, selected screenshots, source notices, and bounded check results. |
| [Creative-direction validation](evals/validation-2026-10-31-creative-direction.md) | Open-brief research and two fresh-context written handoffs, with planning outcomes kept separate from visual execution. |
| [Illustration QA and prompting validation](evals/validation-2026-10-31-illustration-quality.md) | Mera reinspection, known 2D defect/control, new native artwork, local-edit regressions, and transparent-viewer false positives. |

## How the design method works

1. **Define the specific brief.** Translate “best,” “modern,” or “creative” into audience, message, aesthetic intent, context, and appropriate success criteria.
2. **Study real work.** Inspect sources and actual images, distinguish original project dates from repost dates, and avoid treating one design feed as the entire audience.
3. **Explore different concepts.** For substantial work, make visible roughs of different visual ideas using comparable copy and fidelity. Palette swaps do not count as different concepts.
4. **Build with the right tools.** Combine original imagery, vector construction, real typography, diagrams, layout tools, or annotations as the idea requires.
5. **Inspect and revise.** Compare the rendered artifact with the brief at actual delivery size and detail. Correct consequential defects before refining decoration.
6. **Deliver with an honest status.** Record what passed, failed, was not run, or does not apply. Separate internal critique from audience testing, client approval, and physical print proofing.

### What “avoid AI slop” means here

It includes attractive, polished work that remains interchangeable because its choices repeat a familiar formula. Evaluate specificity separately from execution quality. Inspect automatic decoration, empty concepts, repetitive composition, inaccurate copy, and synthetic defects as related risks. This does not mean banning gradients, serif fonts, vintage references, rounded shapes, minimalism, expressive illustration, or maximalism.

For generated imagery, the skill also addresses visual anomalies hidden beneath a convincing finish. Its construction pass traces 2D/3D contours, joins, crossings, repeated surface marks, and cutout boundaries. Composition, construction/detail, alpha/export, and placement receive separate conclusions. Prompting defines the important relationships before generation; local repairs are compared against preserved details afterward. This improves the review procedure without pretending to prove authorship or guarantee perfect detection.

The agent should judge the actual visual result and use taste as well as analysis. A crop, color relationship, ornament, or unusual proportion can belong because it is beautiful or evocative; every detail does not need a functional metaphor or measurable business benefit. Historical vocabulary can work well today through its execution and context.

For new interfaces, the owner's explicit defaults exclude pills, badges, and rounded announcements above hero titles and the stock left-copy/right-graphic hero. Mirroring the split does not solve it. Explicit user direction and faithful preservation of approved work take priority, including narrowly scoped maintenance edits. These are design preferences, not claims that left alignment, rounded controls, or familiar interaction patterns are inherently bad.

The owner's [20 selected references](skills/graphic-design/references/owner-reference-study.md) clarify the desired range, from quiet cream dashboards and cinematic product imagery to playful multicolor interfaces and forceful typography. The [taste profile](skills/graphic-design/references/owner-design-taste.md) teaches relationships rather than a new template. Forms beside expressive images, checkout/product pairings, useful rounded controls, and carefully composed cards are within that range. They are not automatically the rejected marketing hero. Current project direction and approved identity take priority over the default profile.

The interface workflow starts with a user task, compares genuinely different compositions, designs the necessary states, and checks the actual result across content and screen conditions. It distinguishes an attractive mockup from a tested flow. It also avoids replacing the rejected formula with compulsory centered heroes, bento cards, large serif type, or another repeated aesthetic.

The [UUPM comparison](skills/graphic-design/references/template-convergence-study.md) turns a supplied negative reference into specific guidance. It distinguishes surface variety from structural variety, maps sections to actual visitor questions before choosing components, checks whether imagery and proof support the proposition, and reviews repeated choreography. It records useful exceptions and limited interaction checks; it does not claim every demo is identical or that familiar components reveal AI authorship. See the [update's validation record](evals/validation-2026-10-30-uupm.md) for package checks and bounded forward exercises.

The [visual-judgment guidance](skills/graphic-design/references/composition-and-layout.md#develop-visual-judgment) protects expressive choices from overcorrection. It encourages intuitive experiments, gives aesthetic quality explicit weight, separates taste from demonstrated defects, and repairs specific problems while preserving the design's character. Subtraction is a comparison, not a mandate to simplify. Accessibility, truthful content, and working controls remain requirements within their applicable scope.

The [30 October UI/UX evidence](skills/graphic-design/references/sourcebook.md#ui-and-ux-evidence) separates standards, research, practitioner evaluation, and design synthesis. The [reference study](skills/graphic-design/references/interface-reference-study.md) records what was visible and what was inaccessible, rather than claiming a complete audit of paid libraries.

### UI and motion designed together

The [second reference set](skills/graphic-design/references/owner-workspace-study.md) expands the visual vocabulary to dense workspaces and settings. The core workflow now develops motion while arranging the interface, prototypes a principal sequence early for interactive implementation, and revises the composition and choreography together. Hover, focus, transitions, scroll scenes, and save feedback are designed states, not a final layer of identical entrance effects. Beauty and enjoyment are valid motion goals.

Use the [shared UI and motion brief](skills/graphic-design/assets/interface-motion-brief.md) with [Web Motion Director](https://github.com/MikeyNu/Web-Motion-Director) when available. The graphic-design skill handles visual relationships and art direction; the companion deepens temporal implementation and verification. Both use the same plan and prototype. This does not install another skill, grant tools, or require multiple agents. The local guide remains usable without the companion.

The [nine-clip motion study](skills/graphic-design/references/owner-motion-study.md) adds timestamped analysis of masks, typography, drawn accents, synchronized progression, surface choreography, and shared-image transitions. It separates interface movement from presentation-camera work and records the sampled-frame limits. [Motion-principles research](skills/graphic-design/references/sourcebook.md#motion-principles-research) supports the expanded guidance. Proposed implementation, exact source easing, and untested behavior remain explicitly distinguished.

### Psychology without a false dictionary

Font voice and color associations are treated as hypotheses grounded in form, culture, content, and context. Research findings retain their limits. A serif is not automatically trustworthy; a sans serif is not automatically modern or more readable; a color does not guarantee a response. See the [sourcebook](skills/graphic-design/references/sourcebook.md).

## Run the tools and tests

The contrast calculator, SVG metadata checks, review-board construction, repository checks, and portable builder use Python's standard library. Raster preflight requires Pillow; PDF metadata checks require pypdf. The pinned versions used for the optional QA environment are in [requirements-qa.txt](requirements-qa.txt).

```bash
python3 -m pip install -r requirements-qa.txt
python3 -m unittest discover -s tests -v
```

Read [the tool guide](skills/graphic-design/references/tools.md) before running the artwork checks. The tools report narrow technical facts and unperformed checks. They do not score beauty, inspect anatomy, validate copyright, perform user research, or certify production readiness.

The repository's CI runs software and package checks. It does not count as visual QA of a future design. See [evaluation guidance](evals/README.md), [the original validation](evals/validation-2026-10-18.md), and [the UI/UX update validation](evals/validation-2026-10-30.md) for the distinction between automated tests and exercises actually performed.

## Maintain it

Refresh time-sensitive source claims, platform specifications, font availability, and licenses when relevant. Keep durable principles separate from current examples. Preserve uncertainty and source scope. Test changes against contrasting briefs and inspect the actual outputs, especially after altering the core workflow.

Do not add permanent trend blacklists, a universal “premium” aesthetic, magic personality prompts, or numerical beauty scores presented as science. Add scripts only for repeated tasks that benefit from reliable execution, and test them with failure cases.

## License and reference material

The repository retains its original [MIT license](LICENSE). Linked studies, brand examples, fonts, and third-party artwork remain subject to their own rights. Links and concise analysis do not grant permission to redistribute or incorporate those assets into client work.
