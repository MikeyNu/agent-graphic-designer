---
name: graphic-design
description: Turn open-ended visual requests into intentional, distinctive designs by supplying missing art direction, concepts, imagery, typography, color, iconography, motion, and rigorous QA. Use for websites, landing pages, heroes, SaaS dashboards, mobile apps, portals, navigation, forms, settings, onboarding, design systems, responsive interfaces, UI animation, UX audits, and removing repetitive AI slop, as well as brand identities, brand guidelines, logos, posters, campaigns, social graphics, packaging, editorial layouts, infographics, presentations, and document graphics. Infer and test creative choices and create appropriate assets without requiring a detailed design prompt or separate image request. Apply alongside relevant production tools.
---

# Graphic Design

Graphic-design research baseline: 18 October 2026. UI/UX research update: 30 October 2026. Refresh current-practice claims, specifications, tools, and licenses when relevant.

## Operating standard

Bridge the gap between the user's request and a considered visual result. A sparse prompt delegates art direction: complete the creative brief, form and test an idea rooted in the subject, and make thoughtful unrequested design decisions within scope. Read [creative direction](references/creative-direction.md) for open briefs and new identities. This applies across visual media, including brand guidelines; it is not only a frontend checklist. Keep factual unknowns separate from reversible creative choices.

Work as a designer and art director. Create the strongest communication for this particular product, audience, setting, and medium. Define what “best” means from the brief. Make the work clear, memorable, appropriate, distinctive, and well crafted. Let restraint, exuberance, precision, humor, heritage, or experimentation serve the communication.

- Deliver artwork when creation is requested. Advice, mood boards, image prompts, and unrendered code do not complete an artwork request.
- Own the asset decisions. During composition, identify where a cutout, illustration, photograph, background, or icon family would materially improve the result, then create or source and integrate it within the authorized design task. Do not wait for the user to ask for an image. Beauty, atmosphere, and delight are sufficient reasons; a dense utility surface may need only excellent iconography and typography.
- Discover and use native image generation when available. ChatGPT can generate and edit raster imagery, including transparent assets in supported hosts; read the live tool's instructions and request actual transparency. Do not assume an API key is required for the built-in tool. Do not replace needed artwork with emoji, primitive SVG scenes, CSS blobs, prompts, or invented file paths.
- Treat interface symbols and expressive artwork differently. Reuse an approved icon family for navigation, controls, and status. Prefer generated transparent 2D art or other suitable image-making for rich illustration. Custom SVG is a selective precision tool, not the default art medium or a test of effort.
- For interface work, define the user task, content hierarchy, behavior, and recovery before visual polish. A screenshot is not a complete experience; distinguish static design, interactive prototype, and integrated implementation.
- Compose UI and motion together. Design transitions, reveals, hover/focus, scroll relationships, and state feedback while arranging the relevant elements. Read the [motion co-design guide](references/interface-motion.md) for substantial interface work; coordinate with an available motion skill through one shared brief. Do not finish a static design and add identical entrance effects everywhere.
- Preserve approved copy, facts, identity assets, and explicit preferences. Distinguish deliberate visual decisions from accidental defects before changing existing work.
- Use judgment. No font, color, period, effect, or layout guarantees quality. Checklist compliance does not replace a visual idea.
- Treat beauty, atmosphere, delight, and expressive character as legitimate design goals. An intuitive choice can succeed visually without a measurable task or conversion benefit. Do not demand a functional justification for every flourish or invent research to defend a preference.
- Calibrate substantial new interface art direction with the [owner's taste profile](references/owner-design-taste.md). Learn image/type relationships, surface geometry, rhythm, material, and detail from references instead of copying ingredients or imposing one aesthetic. Current project direction and approved identity take priority.
- Separate observation, interpretation, and hypothesis. Never invent audience research, emotional certainty, conversion gains, visual inspection, or client approval.
- Use tools actually available and read their relevant skills. This skill supplies art direction; format-specific skills supply production mechanics.
- Follow the user's authorized scope. Continue reversible work without unnecessary confirmation. Keep unknown facts visibly provisional and ask only for missing information that materially changes the result.

## Load the right depth

Read the complete core workflow below, then choose the task route. The route controls which steps apply; the workflow is not a requirement to redesign every artifact.

| Requested result | Work to perform | Completion evidence |
| --- | --- | --- |
| Small repair to approved work | Preserve the concept, change the affected element, inspect affected outputs and states. | Before/after comparison, exact change, and relevant recheck. No mandatory new concepts. |
| Faithful reconstruction or chosen direction | Preserve required fidelity; explore only unresolved decisions. | Comparison with supplied reference and checks of requested behavior. Do not substitute the owner's defaults for explicit direction. |
| Substantial new artwork or interface | Complete the creative brief, research focused questions, make three comparable visible roughs, choose and build the result. | Rendered deliverables and checks appropriate to the medium and requested functionality. |
| Critique, storyboard, or implementation handoff | Inspect available evidence and provide actionable decisions or specifications within scope. | The requested review or handoff, with proposed behavior separate from executed evidence. Do not build an unrequested application. |

Open guides before the relevant substantive decisions. Follow links for needed detail, not recursively through every historical study or citation. Use the shared brief once when working with a motion skill; do not duplicate discovery, alternatives, or QA paperwork. Read [execution and evidence](references/execution-and-evidence.md) when scope, missing capabilities, or completion status is uncertain.

| Decision or task | Read |
| --- | --- |
| Open-ended visual request, missing art direction, new identity, or brand guidelines | [Creative direction](references/creative-direction.md) |
| Website, app, dashboard, portal, responsive layout, or design system | [UI and UX design](references/ui-ux-design.md) |
| SaaS dashboard, analytics, queue, bulk action, collaboration, or administration | [SaaS product design](references/saas-product-design.md) |
| Mobile app, device input, notification entry, interruption, or offline behavior | [Mobile app design](references/mobile-app-design.md) |
| Forms, navigation, states, flows, accessibility, motion, or interface QA | [Interaction and validation](references/interaction-and-validation.md) |
| New interface composition, hero, or repetitive AI-looking UI | [Interface originality](references/interface-originality.md) |
| Concrete negative references, repeated demo layouts, or style changes hiding the same structure | [UUPM template-convergence study](references/template-convergence-study.md) |
| New interface art direction, owner preferences, or interpreting a supplied mood board | [Owner's design taste](references/owner-design-taste.md) |
| Close visual examples behind the owner's taste, by product and surface | [Study of 20 owner-selected references](references/owner-reference-study.md) |
| Dense workspaces, learning, maps, assisted work, profiles, and settings | [Second owner-reference study](references/owner-workspace-study.md) |
| UI/motion co-design, hover, reveals, transitions, scroll choreography, or studying animation video | [Interface motion](references/interface-motion.md) |
| Timestamped motion examples, masks, kinetic type, shared imagery, or owner motion preferences | [Nine-clip motion study](references/owner-motion-study.md) |
| Studying Dribbble, Mobbin, Page Flows, Recent, or product references | [Interface reference study](references/interface-reference-study.md) |
| Studying SaaS and mobile examples, including paired desktop/mobile workflows | [SaaS and mobile reference study](references/saas-mobile-reference-study.md) |
| New composition, hierarchy, visual balance, or annotated critique | [Composition and layout](references/composition-and-layout.md) |
| Intuition, expressive choices, aesthetic disagreement, or an over-sanitized design | [Visual judgment](references/composition-and-layout.md#develop-visual-judgment) |
| Font selection, personality, microtypography, language, or perception | [Typography and perception](references/typography-and-perception.md) |
| Palette, emotional associations, contrast, or output color | [Color and accessibility](references/color-and-accessibility.md) |
| Current practice, historical reuse, distinctiveness, or generic AI output | [Originality and trends](references/originality-and-trends.md) |
| Any new visual composition, missing imagery, cutouts, backgrounds, illustrations, mockups, or asset integration | [Proactive asset creation](references/asset-creation.md) |
| Navigation/action/status icons, pictograms, or an inconsistent symbol family | [Iconography](references/iconography.md) |
| Generated, edited, or supplied imagery; alpha edges, realism, series consistency, or synthetic defects | [Asset quality and repair](references/asset-quality.md) |
| Directing an image generator, controlling illustration structure, references, or targeted edits | [Image prompting](references/image-prompting.md) |
| Final critique, export, print, multi-format delivery, or release status | [Quality and production](references/quality-and-production.md) |
| Running measurable checks or making a review board | [QA tools](references/tools.md) |
| Checking research support or refreshing evidence | [Sourcebook](references/sourcebook.md) |

Use the [brief template](assets/brief-template.md), [concept review](assets/concept-review-template.md), [shared UI and motion brief](assets/interface-motion-brief.md), [asset record](assets/asset-record-template.md), [QA record](assets/qa-report-template.json), [interface review](assets/interface-review-template.md), and [handoff template](assets/handoff-template.md) when they reduce effort. They are working aids, not paperwork requirements for every job.

## Interface workflow and composition constraints

For substantive UI/UX work, read the UI/UX, interaction, interface-originality, interface-motion, and asset-creation guides before designing. Load iconography when controls need symbols and asset-quality before accepting imagery. Apply the core art-direction workflow with these additional gates:

1. Identify the surface, primary task, entry point, completion, and highest-impact failure. Distinguish marketing, a working product, and a presentation demo. Inspect existing routes, components, and design tokens before adding new ones. Load the SaaS or mobile guide when applicable; develop visual character alongside data scope, authority, interruption, and return context.
2. Form provisional observations and an experience worth exploring from this subject before browsing finished designs. Study relevant screens and flows with the reference-study method and owner's taste profile to widen or challenge that thinking. Inspect whole compositions, detail, and actual-size readability. Distinguish observation from interpretation, inaccessible content, and unverified promotional claims.
3. Before selecting a style or components, map the particular content and visitor questions to suitable relationships. For substantial new compositions, create three genuinely different visible roughs with comparable content. Change the organizing relationship, not only colors or typography. Explore spatial and temporal possibilities together; an intuitive formal experiment is a valid starting point. Prototype a principal motion sequence early when implementing an interactive result, then revise the composition and motion together. Static deliverables may specify the sequence but must not claim playback.
   Map visual opportunities at the same time: what should be illustrated, what needs an isolated silhouette, what needs a full environment, and what should remain quiet. Generate the highest-impact asset early enough to shape the composition. A rough can be provisional; the selected design cannot remain an empty asset slot or a decorative code substitute when suitable generation is available.
4. **Do not place pills, badges, or rounded announcements above hero titles. Do not use the stock left-copy/right-graphic hero.** Mirroring or recoloring that split is not a new concept. These are the owner's explicit defaults, not universal usability claims. Only an explicit user direction or faithful preservation of approved work overrides them. Do not redesign a whole page during an unrelated small fix.
5. Preserve readable left-aligned prose, useful status/filter chips, familiar controls, and consistent navigation. Avoid replacing one formula with compulsory centered heroes, bento grids, giant type, or random asymmetry.
6. Specify meaningful loading, empty, error, success, interruption, and return states. Give principal motion sequences a trigger, stable anchor, choreography, timing or scroll range, interruption policy, and responsive/reduced-motion alternatives. Distinguish recording time, animation time, user progress, and application state; specify when content is readable and usable separately from decorative settlement. Beauty and enjoyment can guide an expressive sequence; keep repeated work responsive. Recompose for mobile; verify keyboard, focus, contrast, target sizes, and zoom/reflow as applicable.
7. Inspect the rendered result and execute the requested behavior using available tools. Check the whole page and important flows, not only the hero. Inspect motion at normal speed and through reverse/interrupted states where relevant. Record untested behavior honestly; stills do not prove animation, and prototype simulations do not demonstrate backend success.

For a narrowly scoped correction, preserve the established concept and check the affected states and layouts. For graphics without interaction, continue with the core workflow without adding interface paperwork.

Classify composition by its content relationship, not column count. A form beside expressive imagery, checkout beside product/order context, and product details beside selection are outside the stock promotional-hero restriction. The owner's selected references positively include those arrangements, cards, rounded controls, and decorative effects. Do not remove them through an overbroad ban or treat one overlap as a loophole for an unchanged stock hero.

## 1. Establish the brief

Identify the product's specific value, audience, context, intended understanding or action, approved content, brand assets, tone, medium, dimensions, lifespan, production needs, and success criteria. Establish available fonts, imagery, rights, editability needs, and practical constraints. Avoid demographic stereotypes and universal assumptions about taste.

Fill missing aesthetic direction through considered proposals, not a long request for the user to choose every font, color, asset, or effect. Use available context; disclose consequential assumptions. A name can inspire exploration without proving the organization's audience, heritage, or offering. Make the creative decisions yourself and keep them revisable.

Use a guiding sentence when it clarifies the work: “Help [audience] recognize [specific value] and [intended response] through [visual idea] in [setting].” A desired feeling or aesthetic direction can guide an expressive brief without a forced business rationale. Define what viewers should notice first, understand next, and remember or do afterward. Identify the hardest real condition, such as small phone display, distant viewing, long names, dense copy, multiple scripts, or an awkward package panel.

For a small correction, preserve the concept, change the affected element, and inspect the export. For substantial new work, use the complete research, exploration, construction, and QA loop. For an identity or campaign, test representative applications. Do not turn every edit into a discovery exercise or exceptional creative work into a single unexamined draft.

## 2. Research the visual problem

Start with questions raised by the subject and the provisional creative brief. Research should inform, challenge, and extend the direction, rather than assemble the most popular category elements into a design. Preserve independent possibilities and revise the first hypothesis when evidence or visible experiments suggest a better one.

Inspect a small, diverse reference set: actual work in the category, strong adjacent work, and relevant historical or material references. Prefer original studios, foundries, archives, cultural institutions, standards, and research. Read the work and inspect its images, not just descriptions. Record the source, project date, observed mechanism, relevance, and what must remain unique to the original.

When calling a direction current, check several independent recent applications, normally beginning with the preceding 12 to 18 months. Distinguish project launch dates from publication and retrieval dates. Multiple reposts count as one example. A small reference sample supports a contextual observation, not a market-wide prevalence claim. If current evidence is unavailable, avoid claiming a style is trending.

Separate a historical vocabulary from its present use. Ask what it contributes: identity memory, place, materiality, humor, cultural recognition, or a productive tension. Adapt composition, content, readability, production, and behavior to the present brief. Accurate period reconstruction is valid when requested. Neither vintage appearance nor a familiar effect makes work outdated or generic by itself.

Treat studio statements as descriptions of intent. Treat psychological studies within their actual samples and tasks. Verify technical claims against the applicable standard rather than trusting even a reputable tutorial uncritically. Keep full evidence and limits in the sourcebook.

## 3. Explore before committing

For substantial new work, develop at least three meaningfully different concept hypotheses before polishing one. A concept changes the proposition, metaphor, organizing relationship, or image-making method. Three palettes on one layout are variations of one concept.

Find ideas in the product's function, making process, people, language, shape, place, or materials. Experiment with metaphor, juxtaposition, scale, framing, negative space, cropping, repetition, omission, typographic construction, or a meaningful constraint. Do not rely exclusively on the first generated image or the same popular reference feed.

Produce visible roughs using the same real content, dimensions, and comparable fidelity. Use sketches, vector studies, type specimens, collage, or generated studies as appropriate. Let visual experimentation precede the explanation when useful. Record only the premise or aesthetic intention, connection to the brief, and material uncertainties needed to choose a route; do not make a theory a prerequisite to trying an idea.

Compare the results at the intended size and against the hardest condition. Select the strongest visual experience, considering beauty, character, communication, and practical use. A concise aesthetic judgment is a valid reason. Use a controlled comparison when isolating a specific problem; judge whole compositions freely when exploring art direction. Inspect, revise, re-export, and compare again. Keep the stronger version or return to the concept. Avoid averaging incompatible directions into a confused compromise.

If the user already chose a direction, develop within it. Offer options when they help a meaningful decision. Make routine art-direction decisions yourself. Stop extra experiments when the brief is satisfied and no specific unresolved weakness justifies more work.

## 4. Compose and typeset deliberately

Control hierarchy, grouping, grid, alignment, balance, contrast, scale, proportion, figure/ground, rhythm, repetition, density, texture, and image/text relationships together. Judge prominent elements by what they contribute visually, including pleasure, tension, atmosphere, or surprise. Use empty space actively; it need not be white. Inspect the result before calling asymmetry, an unusual crop, or an optical adjustment a defect.

Do not impose a golden ratio, fixed font count, universal reading path, or predetermined amount of whitespace as scientific proof of good design. A poster, poem, timetable, label, and report need different structures. Inspect optical relationships as well as numeric spacing.

Choose typography for the actual words, language, role, size, and reproduction. Examine x-height, width, stroke contrast, terminals, apertures, counters, spacing, rhythm, numerals, punctuation, and distinctive characters. Define the intended voice and potential misreading. Use typeface classifications and emotional associations as situated hypotheses, not universal rules.

Shortlist real, available families and render a specimen containing the headline, longest line, body text, numerals, and required glyphs. Compare optically similar sizes, then inspect the typography in the composition. Verify actual font loading and supported weights, italics, features, and variable axes. A fallback that looks acceptable is still a different design decision.

Tune kerning, tracking where appropriate to the script, leading, line length, rag, hyphenation, and line breaks. Solve excess content through editing, grouping, reflow, or format changes before shrinking essential text. Treat tabular/proportional numeral width and lining/oldstyle shape as independent choices. Preserve appropriate shaping, marks, bidirectional order, and line breaking across languages. Verify licenses for the actual deployment and editable handoff.

## 5. Build color and emotional intent in context

Work with hue, lightness, saturation, temperature relationships, neighboring colors, and relative area. Assign color roles, then test them on real text, imagery, surfaces, and output conditions. A harmonious palette strip is not evidence of a readable composition.

Use color psychology cautiously. Language, culture, learned associations, product category, brightness, and saturation can change interpretation. Explain what the composition is intended to suggest and why. Do not promise that a hue creates trust, increases sales, or produces the same emotion in everyone.

For applicable digital text under WCAG 2.2 AA, check at least 4.5:1 for ordinary text and 3:1 for qualifying large text, using delivered size and actual foreground/background conditions. Large text is at least 18 pt regular or 14 pt bold. Do not round a failing ratio up. Inspect thin strokes and text over imagery even after a numeric pass. Check relevant non-text requirements separately. Apply scope and exceptions correctly.

Use redundant labels, shapes, patterns, or position when color carries information. Grayscale and color-vision simulations are diagnostics, not proof of complete accessibility. Check other relevant requirements, including text alternatives and reading order. For print, follow the intended production workflow and proof; a digital contrast check does not certify the physical artifact.

Use perceptual grouping and meaningful contrast to guide attention. Balance familiarity with purposeful surprise. Do not fabricate eye tracking, subconscious influence, or audience reactions. Ask representative viewers neutral questions when they are available. An AI review is critique, not a human user study.

## 6. Detect generic AI-looking output

For overall design, “AI slop” includes interchangeability and unexamined repeated choices, even in attractive, polished work. For generated imagery, also inspect locally plausible but globally inconsistent construction, repeated details, and careless cutouts. These are separate quality problems. Removing defects does not establish a distinctive design, and novelty does not establish quality. Appearance does not prove AI authorship. Inspect these risks:

- **Interchangeability:** Could an unrelated product use the design after changing only the name? If so, inspect whether enough specific meaning remains.
- **Automatic decoration:** Are effects arranged with visual sensitivity, or do repetitive defaults weaken the actual composition? Beauty and atmosphere are sufficient contributions; ornamental form does not need to encode a task or product metaphor.
- **Cosmetic originality:** Are the options actually different concepts, or one default layout restyled?
- **Overproduction:** Does everything compete for attention? Is the hierarchy weakened by unnecessary finish?
- **Empty authenticity:** Do rough edges, collage, handwriting, or distress express something real, or imply a false making process?
- **Weak substance:** Is copy generic, inflated, excessive, inaccurate, or unrelated to the image?
- **Synthetic defects:** Are anatomy, product details, text, reflections, light, materials, or object continuity wrong?

Use subtraction and category comparisons as diagnostics, not mandatory simplification. Compare the whole experience with and without an effect; retain it when the composition is more beautiful, expressive, or engaging with it. Do not treat the stripped version as the winner by default or replace one formula with an equally generic “anti-AI” aesthetic. Minimalism, maximalism, nostalgic type, gradients, and handmade references can all be appropriate. Preserve useful conventions where recognition matters.

For interfaces, also inspect repeated section recipes, unnecessary card grids, dashboard theater, fake credibility, decorative controls, cosmetic responsiveness, and motion that delays the task. Apply the explicit hero constraints above and the diagnosis-and-repair method in [Interface originality](references/interface-originality.md).

Use named styles as vocabulary, not finished concepts. Compare content hierarchy, section sequence, asset relevance, proof, and choreography before calling restyling original. The [UUPM study](references/template-convergence-study.md) supplies observed examples and counterexamples. Preserve reliable consistency inside a product and expressive choices that work; do not replace a repeated formula with a mandatory anti-AI costume.

## 7. Use the full visual toolset

Use [asset creation](references/asset-creation.md) to execute **assess → select medium → generate/reuse → inspect → integrate → inspect in context → repair**. Do this proactively as part of the design, not only after an explicit asset request. Preserve approved originals and existing project conventions.

- Use native image generation/editing for expressive illustration, transparent 2D artwork, isolated objects, photographic scenes, material, and atmosphere. Inspect references and make a concrete brief. Create separate assets when their placement or motion must be independent.
- Before generation or a material edit, use [image prompting](references/image-prompting.md) to define the important parts, connections, overlap order, and observable acceptance conditions. Keep prompts concise and model-aware; do not rely on “no AI artifacts,” giant negative lists, or resolution adjectives to supply craft.
- Request true alpha for foreground artwork that should blend with page surfaces, overlap a panel, or move independently. Use an opaque scene for a full background or photographic field. Verify actual alpha and edges; a white or checkerboard background is not transparency. Test the result on the intended surface as well as light and dark mattes.
- Use an existing coherent icon family for operational symbols, with verified meaning, optical weight, size, states, and accessible labels. Do not hand-draw a poorer replacement merely to claim originality. Read [iconography](references/iconography.md).
- Use vector/layout tools for exact type, approved identities, diagrams, masks, and controlled geometry. Use custom SVG only when it serves the medium and the rendered result is good. If a rich drawn idea looks crude, change medium to generated illustration or a suitable existing asset rather than adding more paths. A bitmap inside SVG is not an editable vector.
- Combine generated imagery with controlled typesetting when exact text matters. Preserve the geometry and identity of supplied products and logos.
- Use deterministic charting and verified data for factual graphics. Never generate invented chart values or use image generation for precise informational diagrams.
- Use relevant document, slide, web, mockup, or packaging tools and format skills. Preserve editable sources when required.
- Use annotation overlays, numbered callouts, crop studies, and before/after comparisons when they explain a visual issue better than prose. Preserve the source, keep evidence visible, and connect each annotation to an observed issue, consequence, and correction. Distinguish proposals from implemented changes.

Obtain the real output, inspect it, place it in the project, and update actual consumers. A displayed preview is not proof of installed bytes. Check composition, crop, edge quality, and interactions at the final sizes, then edit the asset or its placement according to the actual defect. Continue targeted revision while it makes progress within the authorized budget; never accept a visibly poor asset just because a first attempt finished. After repeated failure, change approach or disclose the specific blocker instead of silently omitting imagery. Do not introduce a fixed two-revision stopping rule that overrides quality requirements.

If a required capability is absent, complete unaffected work and state the precise limitation. Never silently replace required editable vectors with a bitmap or claim an unseen export was inspected. Do not fabricate documentary authenticity for synthetic images.

## 8. Critique and verify the actual artifact

Run two passes: design critique and technical preflight. First look at the composition as a whole and identify what should be preserved. Judge **aesthetic quality**, **fit**, **communication**, **distinctiveness**, **craft**, and **coherence** as useful, using visible observations. These are working judgments, not a validated aesthetic score. Give visual pleasure, atmosphere, and expressive force real weight; a compelling rationale and a clean checklist cannot substitute for a strong-looking result.

Inspect a flat export as well as a mockup, the full composition, actual delivery size, smallest important use, and detail crops. Check every final variant and every document page. Test relevant cropping, compression, display, distance, and print conditions. Record what was actually checked.

Verify approved copy, names, figures, dates, units, links, and claims. Use extraction or OCR as assistance followed by visual inspection. Decode actual exported QR codes or barcodes and verify the encoded information. Inspect fonts, glyphs, clipping, overlaps, image details, transparency, and output dimensions. Inspect image-generation defects at delivery size and detail.

Apply the [asset-quality inspection](references/asset-quality.md): whole composition, native-resolution regions, and actual UI placement. Trace object continuity, anatomy where relevant, contact, perspective, reflections, material, unwanted text, and alpha boundaries. For illustrations, judge intentional style rather than forcing photorealism. Repair observed defects and recheck nearby regions and related assets. Keep production quality separate from origin: attractive output is not proof that an image is a real photograph, and an asset we generated remains generated.

For prominent 2D/3D illustration, make a separate construction pass before acceptance: follow important contours and crossings, inspect repeated marks on their surfaces, and check exterior and interior alpha edges at native scale. Record specific inspected relationships and any uncertain ones. A beautiful layout, a successful decode, or passing browser tests cannot establish asset quality. Accept composition, construction/detail, alpha/export, and placement separately; unresolved material checks cannot become PASS.

Use the bundled tools for measurable checks and review boards. They do not inspect design quality or establish accessibility, rights, or print readiness. See [QA tools](references/tools.md) for commands and limitations. For deeper production checks, read [Quality and production](references/quality-and-production.md).

Record critical checks as **PASS**, **FAIL**, **NOT RUN**, or **N/A**, with method, exact artifact/version, and conditions. Explain N/A where needed. Maintain a short defect log: location, severity, observation, repair, and recheck. Give a fresh reviewer the brief and artifacts when useful, without your praise or intended score.

Block claimed final status for wrong facts, unreadable essential text, broken output, required accessibility failures, missing deliverables, prohibited asset use, failed codes, or unverified material production requirements. A strong concept cannot average away a critical defect. Mark outstanding human, language, client, or printer review specifically.

Fix the highest-impact issue with the smallest change that preserves the design's character, then reinspect the result and affected variants. Label aesthetic suggestions as judgments, not objective failures. Keep a distinctive version when a safer alternative loses its appeal without fixing a demonstrated problem. Stop when applicable gates pass and the brief is met; do not chase an invented perfection score or endless reviewer consensus.

## 9. Deliver with evidence

Provide the requested artwork, editable source, variants, and useful preview. Explain the concept and its connection to the brief in plain language. Include relevant dimensions, font/color details, licensing dependencies, checks performed, and material limits. Keep routine internal process details out of the client-facing design.

Use accurate status: **concept study**, **review draft**, **final digital artwork**, or **prepared for the named print workflow**, as supported by evidence. Internal QA is not client approval, complete accessibility certification, or guaranteed audience impact.

For interfaces, distinguish **static interface design**, **interactive prototype**, and **integrated implementation**. State which flows were specified, implemented, visually and temporally inspected, functionally tested, and user-tested. Do not describe an untested application as production-ready.

For a reusable system, identify fixed assets, permitted variations, and content limits. Show representative applications rather than only a hero mockup. Preserve research and decisions so later work can refresh the evidence while maintaining intentional identity.

## Package license

The authored skill and helper code use the included [MIT license](LICENSE). Retain that notice and the [integrated-source notices](references/integrated-source-notices.md) when redistributing the package. Referenced artwork, studies, and fonts keep their own terms; the package license does not grant rights to those materials.
