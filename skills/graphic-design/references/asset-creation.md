# Asset creation and tool direction

Use this guide when the concept requires original imagery, exact vector work, factual diagrams, mockups, document graphics, or annotation. These are workflow prescriptions. Tool behavior must be checked against the capabilities and documentation available in the current session.

## Contents

- Choose a production method
- Direct image generation
- Construct exact graphics
- Make annotations useful
- Preserve editability and rights
- Handle missing capabilities

## Choose a production method

Start with what the image must communicate and what must remain exact. Choose a method that can deliver both. Use more than one tool when that gives useful creative freedom without sacrificing accuracy.

| Visual problem | Effective route | Important limitation |
| --- | --- | --- |
| Human scene, material, atmosphere, or expressive illustration | Available image generation, editing, licensed photography, or supplied imagery. | Inspect identity, anatomy, physical plausibility, crop, and context. |
| Precise wordmark, icon, diagram, pattern, or graphic construction | Native vector tools, designed SVG, or appropriate layout tools. | Syntax validity does not establish good spacing or appearance. |
| Exact headline over original imagery | Create the image, then use controlled typography. | Verify final copy and export, even with deterministic typesetting. |
| Technical schematic or factual chart | Use verified data and deterministic plotting or diagram tools. | Do not substitute a plausible-looking generated diagram for a correct one. |
| Editorial page, report, slide, or brochure | Use the requested editable format and its relevant skill. | Render every final page or slide; source structure alone is insufficient. |
| Product or packaging mockup | Use suitable mockup tools or controlled perspective placement. | A mockup is not a dieline, a manufacturing specification, or proof of final materials. |
| Design critique | Use a duplicate, overlay, or side-by-side comparison with precise callouts. | Never silently alter the evidence being discussed. |

Do not treat tool use as a performance. Use the method that improves the work. Custom SVG is valuable for intentional geometry, but reducing a rich illustrative idea to easy circles and rectangles may weaken it. Conversely, generating a bitmap of a simple technical diagram adds uncertainty without improving communication.

## Direct image generation

Inspect every supplied reference before editing or transforming it. Identify what is fixed: identity, product proportions, silhouette, packaging text, logo, color, camera position, or composition. Record what the user wants changed.

Build an image brief from concrete decisions:

1. **Subject and meaning:** Who or what is shown? What action or relationship expresses the proposition?
2. **Composition:** Focal subject, scale, point of view, foreground/background relationships, crop, and reserved space for text.
3. **Light and material:** Source direction, softness, surface finish, texture, environment, and plausible contact shadows.
4. **Visual language:** Photography, illustration, collage, print process, or another coherent medium. Describe its characteristics rather than accumulating fashionable adjectives.
5. **Constraints:** Exact product details, prohibited changes, required aspect ratio, transparency, consistency with a series, and any meaningful exclusions.

Avoid relying on “award-winning,” “premium,” or “8K” to supply decisions. Resolution language does not establish composition, faithful detail, or actual output dimensions. Ask for exact dimensions only when the tool supports them and verify its actual result.

Explore distinct concepts before refining one result. Once a concept is selected, vary one consequential feature at a time. A large batch of near-duplicates is not evidence of a broad search.

For raster creation and editing, use the available image tools according to their current instructions. Do not substitute improvised bitmap manipulation where a governing tool requires a particular workflow. For exact vector or diagram work, use the appropriate native construction instead of image generation.

### Inspect the generated asset in context

Inspect the full image and delivery-size details:

- Anatomy and body continuity where people or animals appear.
- Hands touching objects, facial consistency, and believable interaction.
- Product geometry, materials, brand marks, packaging, and labels.
- Perspective, joins, edges, occlusion, reflections, light, and shadows.
- Repeated objects or motifs, duplicated features, and texture coherence.
- Correct text, plausible signs, and unwanted signatures or marks.
- Crop safety, empty space, visual focus, and relationship to the headline.

Adapt these checks to the style. An intentional surreal image has different criteria from documentary-looking commercial photography. Neither excuses accidental mistakes that undermine the brief.

If a defect is local, repair the local asset where supported, then reinspect the whole composition. If the asset repeatedly drifts from essential product facts, use supplied photography, exact geometry, a more controllable illustration, or another suitable route. Do not call a synthetic scene a photograph of a real event.

## Construct exact graphics

For logos, icons, diagrams, and graphic patterns, define the visual relationship before writing paths. Use a coherent grid or geometric logic when useful, then make optical corrections. Check joins, counter shapes, apparent stroke weight, corners, spacing, silhouette, and small-size behavior.

For SVG, verify the viewport, `viewBox`, aspect ratio, clipping, strokes, embedded images, font dependencies, and final rendering. The [SVG coordinate specification](https://www.w3.org/TR/SVG/coords.html) explains scaling behavior; it does not establish that every application renders every feature identically.

Keep external dependencies intentional. Do not execute scripts or load remote resources from untrusted supplied SVG just to inspect it. Use a safe rendering path and verify the result. An SVG wrapper around a raster does not make the underlying logo an editable vector.

Keep exact text in controllable text layers. Preserve an editable master before making outlined variants when the handoff requires them. Inspect outlined exports for changed spacing, missing glyphs, and clipping. Outline conversion does not remove font-license obligations.

For factual graphics, verify the data, units, labels, axes, scales, dates, totals, and source. Choose visual encodings that reflect the values correctly. Do not make area or perspective exaggerate a difference accidentally. Prefer a simple accurate representation when ornament would obscure the comparison. Let the accompanying context distinguish observed data, estimates, forecasts, and illustration.

## Make annotations useful

Use annotations when they make a design decision visible: a misplaced caption, conflicting alignment, weak focal point, poor crop, hidden information, or an incorrect graphic relationship.

Work from an unchanged original and create a separate copy, layer, or review view. Use stable page numbers and identify the artifact version. Do not describe a reconstructed page as the original.

Each callout should connect:

> Location and observed issue → consequence for the viewer → proposed correction → evidence after the change.

Number callouts and use lines, outlines, brackets, or shaded regions consistently. Keep the underlying evidence visible. Place commentary outside the artwork when possible. Use line styles or labels as well as color so the annotation remains interpretable.

Good examples include a crop alternative, shared alignment axis, competing hierarchy zones, corrected word spacing, or a before/after detail at the same scale. Avoid decorative scribbles, vague “make premium” labels, or arrows that merely point at entire pages.

Verify coordinates after every crop, resize, or export. A marker attached to the wrong line destroys the explanation. Inspect at final review size and ensure annotations do not introduce unreadable text. Distinguish **observation**, **proposed change**, and **implemented result**.

The bundled review-board tool presents source graphics without modifying them and can display review notes. A generated board is an inspection surface. It does not prove anyone has inspected the image.

## Preserve editability and rights

Keep a short asset register: source or creator, original URL when relevant, license, permitted use, editing restrictions, attribution, and handoff needs. Mark assets as supplied, licensed, original vector, generated, or provisional. Do not imply exclusivity from a stock license.

Check the actual provider's terms. [Adobe Stock's FAQ](https://helpx.adobe.com/stock/web/common-questions/usage-licensing.html), for example, distinguishes editorial/commercial uses and restricts treating its nonexclusive stock assets as logos. These are provider-specific rules, not a universal statement of copyright law.

Check font permissions separately. [Adobe Fonts' FAQ](https://helpx.adobe.com/fonts/web/font-licensing/font-licensing.html) distinguishes many finished uses from editable access and packaging font files. Another foundry may have different terms. Do not embed or redistribute paid font files merely because they are installed.

Preserve layer names and editable text where practical. Deliver exported variants that correspond to the source. Do not pretend that a raster preview can be edited like the original layout. Avoid including copied reference artwork in client deliverables unless its use is authorized.

## Handle missing capabilities

Use a fallback only when it preserves the requested outcome. If visual inspection is unavailable, deliver a clearly labeled draft with the unperformed check identified. If font access is missing, use a justified available family and make the substitution visible in the handoff. If print specifications are unknown, prepare the concept and ask for the specific production information before claiming print readiness.

Do all unaffected creative work. A missing premium font need not halt composition studies. A missing physical proof does not prevent a useful digital review. State the exact limitation without inventing a capability or approval.
