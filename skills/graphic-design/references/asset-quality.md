# Asset quality, synthetic defects, and targeted repair

Use for generated, edited, or supplied imagery before accepting it into a design. This integrates the production-quality lane of Agent AI Detector, with [source attribution](integrated-source-notices.md). It is a visual inspection workflow, not an AI-origin classifier. Our generated assets remain generated even when they look excellent.

## Contents

- Establish the target and evidence
- Inspect at three scales
- Trace construction before judging finish
- Apply the relevant defect checks
- Verify cutouts and families
- Repair the responsible layer
- Accept with bounded claims

## Establish the target and evidence

Record the asset's role, desired medium, intended sizes/surfaces, approved invariants, actual source, file/hash when accessible, and transformations. Preserve the original. Distinguish a production-quality question from an investigation of provenance. Usually the goal here is a coherent, convincing asset that fits the composition, not guessing its origin.

Inspect the actual pixels through an available viewer. Do not infer appearance from a filename, prompt, successful download, alpha statistics, or model self-rating. Never claim you zoomed, viewed a crop, played a clip, or checked metadata unless you did. Record unavailable checks. Do not use generated enlargement as evidence of source detail.

For imagery, “AI slop” can describe unexamined visual inconsistencies hidden under appealing finish: fused parts, discontinuous contours, incoherent patterns, invented detail, or careless cutouts. This is separate from repetitive UI composition. Neither is a reliable authorship test. A generated illustration can be excellent; a human-made drawing can contain the same defects. Review the craft rather than trying to assign an AI probability.

Set a short **style and construction contract** before accepting the output: what is intentionally flat, exaggerated, floating, textured, or surreal; which parts and connections must remain coherent; and what the asset will communicate at its largest real use. Use the brief's intent, not a post-hoc claim that every oddity is artistic license. Do not impose physical realism on an intentionally impossible object, but inspect whether the intended illusion and all unrelated details are controlled.

## Inspect at three scales

1. **Whole image and intended character.** Describe the subject, silhouette, medium, focal hierarchy, viewpoint, light, palette, and relationship to the design. First identify what works. Assess specificity, visual appeal, and useful clear space before searching for flaws.
2. **Native-resolution details.** Inspect high-risk boundaries and suspicious regions at original pixel scale, with context and a normal comparison region. Enlarge only for examination and label enlargement as repeated/interpolated pixels, not recovered detail. Record a reproducible region `[x, y, width, height]` in oriented source coordinates when reporting a defect.
3. **Actual placement.** Inspect the integrated screen/page at real sizes and relevant crops. Check light/dark/brand surfaces, mobile, overlap with type, clipping, layering, focus, and compression. A beautiful standalone image can still fail its placement; a tiny irrelevant source blemish need not trigger endless revisions.

Inspect the exact exported file used by the design as well as its master when available. A contact sheet, a downscaled dark-matte preview, or one attractive center crop does not establish complete edge or structural inspection. For prominent art, choose detail views from its risks: crossings/joins, repeated marks on a curved surface, fine exterior edges, and interior holes. Include a normal region for comparison. Keep enough surrounding image to distinguish a real break from an occlusion. Viewing enlarged pixels helps inspection but adds no evidence beyond the original.

## Trace construction before judging finish

After noting the overall strengths, temporarily ignore the attractive palette, lighting, and UI. Read the image as an assembly of shapes. This is a visual reasoning pass, not a requirement to reconstruct a 3D mesh or write a long report.

1. **Inventory the visible parts.** Describe what the pixels show before checking it against the intended prompt. Identify each important body, strip, handle, limb, attachment, and opening. Do not mentally complete missing parts from the generator's description. State uncertain object counts rather than inventing hidden components. Select a few consequential relationships to verify.
2. **Follow boundaries.** Trace each important contour from an actual end through bends to an end or explained occlusion. For a ribbon, cable, branch, or strap, follow both sides. Look for unexplained branching, thickness changes, fused boundaries, disappearing openings, or a part reappearing as a different object. Perspective can change apparent width; the change needs a coherent visual explanation.
3. **Read crossings and contact.** At each important crossing, identify the front object, the rear object, their separate edges, and any expected contact or gap. Trace the rear object's visible continuation. Do not invent its hidden path. A decorative floating object may be intentional; a handle failing to join its own body is a different question.
4. **Follow the surface, not just the silhouette.** Track selected grid lines, seams, perforations, brush contours, or repeating motifs across the same visible surface. Inspect whether they merge, fork, fade, change material, or slip off the surface without a reason. A regular pattern can compress and curve with perspective; random marks may be intentional. Do not assume decorative dots encode accurate data.
5. **Check medium consistency.** Judge the intended 2D or 3D language using the table below. Material beauty cannot compensate for an unexplained structural break.

| Medium or feature | Concrete inspection | Avoid a false positive |
| --- | --- | --- |
| Flat 2D illustration | Check fill against intended contour, attachment of limbs/props/handles, line endings, negative-space holes, layer order, and tangencies that make separate forms appear fused. | Intentional flatness, irregular drawing, offset print registration, decorative floating marks, or a consistent no-outline style. |
| Painterly or textured 2D art | Check whether marks describe the same underlying form, detail stays intelligible near joins, and texture does not quietly become pseudo-objects. | Loose brushwork or deliberate abstraction need not resolve into photographic detail. Do not diagnose downsampled texture as invented objects. |
| Stylized 3D art | Follow front/back surfaces, edges and thickness through bends; inspect penetrations, missing contact, incompatible planes, and transitions between materials. | Soft clay, stylized perspective, exaggerated curves, and designed levitation are valid when coherent. |
| Sheets, ribbons, straps, tubes | Trace paired boundaries, free ends, crossings, and visible thickness. Check that one part does not split into two without a designed junction. | An occluded end is not missing; a folded sheet may reveal its reverse. Unresolvable geometry stays uncertain. |
| Grid, stitching, spokes, keys, or repeated detail | Follow a few neighboring repeats and compare their spacing, alignment, termination, and attachment to the same surface. Verify exact counts only when required. | Perspective foreshortening, intentional irregular rhythm, or non-data decoration. |
| Glossy or transparent objects | Inspect the continuity of the object's own rim and silhouette separately from reflected/refracted shapes; compare light and dark mattes. | A reflection is not automatically an extra edge or an internal object. A baked glass illustration cannot refract arbitrary future UI content dynamically. |

For each concern, ask **what visible relationship is inconsistent**, **where it occurs**, and **what plausible alternative explanation remains**. “It looks AI-generated” is not a finding. Neither is “it is abstract, so everything is allowed.” If the pixels do not establish a fault, state the ambiguity and inspect a broader or native-scale view. Do not manufacture a definite defect to justify another generation.

Vision-language models can miss intersections, counts, and fine boundaries. Splitting inspection into local questions is a practical mitigation, not a guarantee. For a prominent unresolved junction, compare the actual crop again, use an independent reviewer with the raw image and brief when available, or choose a clearer construction. Reviewer agreement is not ground truth. Do not turn a missing or inconclusive structural check into PASS because other checks succeeded.

## Apply the relevant defect checks

| Asset feature | Follow the visible relationships | Do not confuse with a defect |
| --- | --- | --- |
| Human/animal anatomy | Visible joint order, head/neck connection, limb continuity, grip/contact, resolved digits, expression | Occlusion, perspective, disability, natural asymmetry, pose, deliberate stylization. Do not invent hidden anatomy. |
| Face and skin when realism is intended | Local texture variation, believable highlight shape, eyes/lids, hair/ear/glasses boundaries, mouth details at usable resolution | Makeup, soft light, dark or light skin, smooth skin, low resolution, ordinary retouching. Do not impose gritty pores as a universal realism style. |
| Objects and products | Follow rails, cables, straps, seams, handles, pages, stems, and components across occlusion; check count and joins | Intentional abstraction, shallow focus, physically plausible overlap. Verify factual product details from approved sources. |
| Perspective and contact | Common viewpoint, plausible scale, contact planes, shadow attachment, weight and occlusion | Wide-angle or stylized projection when coherent with the chosen medium. |
| Reflections and light | Explain key/fill/bounce, reflections of distinctive parts, contact/cast shadows and material response | Multiple lights, curved glass, tinted surfaces, soft diffuse materials. One unequal highlight is not proof of failure. |
| Texture and repeated structure | Seam continuity, coherent material scale, purposeful repetition, no accidental merged or duplicated features | Pattern design, architectural repetition, intentional print texture or handmade irregularity. |
| Text, marks, labels | Exact required copy, no stray pseudo-lettering or accidental marks, faithful approved logo | Stylized art without readable text. Keep operational text and logos in controlled layers. |
| Illustration and 2D art | Confident shape language, consistent line/edge treatment, purposeful simplification, clear overlaps and balanced detail | Flat color, exaggerated proportions, drawn texture, surrealism. Photorealism is not the standard for a stylized illustration. |
| Generic generated appearance | Interchangeable subjects, unsupported visual claims, incoherent finish, mismatch with type/surfaces, gratuitous embellishment | Beauty, polish, gradients, illustration, or a familiar style by itself. Repair a visible weakness, not a supposed model fingerprint. |

For each important flag, test an alternative explanation: lighting, intended style, occlusion, original material, masking, compression, or crop. A soft edge might be depth of field; a cutout fringe visible on dark surfaces might be matte contamination. Separate observation from mechanism. The quality defect may still matter even when its cause is not AI.

## Verify cutouts and families

For cutouts, inspect the decoded alpha and the asset over a light matte, dark matte, and actual product background. Check exterior and interior gaps, edge halos, clipped extremities, transparent padding, stray islands, semitransparent materials, and whether shadows form an unwanted rectangle. Do not treat RGBA mode as transparency or a painted checkerboard as alpha. The [preflight tool](tools.md) measures alpha coverage and bounds; it cannot certify segmentation or beauty.

Confirm that the inspection viewer composites alpha correctly. Fully transparent pixels can contain arbitrary RGB colors that should not be visible. If a raw preview shows a fringe, colored flecks, or a black surround, compare an alpha-aware composite at native scale and the actual browser/export before diagnosing contamination. Do not erase legitimate subject edges or regenerate an approved asset to fix a viewer artifact. If the fringe survives correct compositing, it is a real candidate for edge repair.

For a family, compare assets side by side at matching visual scale. Lock medium, palette, viewpoint, light, edge character, detail density, and consistent subject proportions. Repair an outlier rather than regenerating approved siblings. For a designed character, compare intended stable features across views without claiming real-person identity verification. A reference sheet is a consistency aid, not a substitute for inspecting individual files.

For animated assets, view normal-speed playback and inspect adjacent frames around suspected incidents. Check object continuity, occlusion, contact, silhouette, shadows, and transitions. Timecode findings. A contact sheet alone cannot establish natural motion. Use the [motion guide](interface-motion.md) for the UI behavior and interruption contract; do not load an unrelated audio-forensics workflow for a static illustration.

## Repair the responsible layer

Keep a short defect queue: `asset/version | region or placement | observed defect | importance at delivery size | alternative explanation | chosen repair | recheck`. Separate critical factual/structural errors, prominent visual weaknesses, and minor polish. For no-defect findings, retain a few actual inspected relationships rather than filling an empty queue with praise. Do not manufacture a numerical quality score.

| Observed problem | Repair route | Recheck |
| --- | --- | --- |
| Merged hand/handle, disconnected stem, impossible equipment | Edit the affected region with surrounding context and invariants; use an approved source or simpler pose if repeated attempts fail | The repaired part, neighboring boundaries, object contact, whole composition. |
| Branched ribbon, fused 2D shapes, or inconsistent repeated surface marks | Specify the intended construction in a targeted edit; use a clearer structural reference or controllable construction when necessary | Paired contours, front/back order, pattern continuity, and preservation of the intended medium. |
| Unwanted wax-like finish in a realistic portrait | Revise local material/light/retouching while preserving natural variation | Face and adjacent skin at final size and native detail, without fake texture overlays. |
| White/dark edge fringe or false transparency | Supported image edit or matting; preserve legitimate white/dark subject detail | Alpha statistics and all required mattes after export. Never “fix” by lowering whole-image opacity. |
| Incorrect logo or generated text | Replace with approved artwork or exact typesetting in the final composition | Spelling, identity, perspective, readable size. |
| Correct asset blocks heading on mobile | Adjust composition, crop, anchor, or variant | Narrow and wide layouts, text expansion, control access. |
| Image path fails or bytes differ after transfer | Fix installation/URL/transport, not the artwork | Destination decode/hash and actual rendered consumer. |
| Rich illustration remains a crude SVG | Change to suitable generated 2D artwork, an approved illustration, or another capable method | Design strength and integration, not path count or markup validity. |
| Repaired image drifts from the family | Reuse the approved anchor and correct the outlier with explicit invariants | Side-by-side family and its actual screen. |

Use the permitted generation/edit workflow and the [prompting and repair guide](image-prompting.md). Request the smallest effective delta and preserve what already works. Compare before/after at matched scale, including protected areas; cleaner edges do not excuse damaged geometry or altered identity. Inspect the repaired region, adjacent regions, and overall composition after each substantive edit. Keep provenance and original files; do not strip authenticity signals or represent generated people, premises, testimonials, or products as verified real evidence.

## Accept with bounded claims

Accept an asset when it is visually strong for its purpose, free of consequential observed defects, coherent with its family, technically usable, and successfully inspected in the final design. Use **passes visual QA for the stated use**, **needs revision**, or **not assessed**, with the actual conditions. Keep unknowns visible. Automated metadata checks cannot promote an unviewed image to visual PASS.

Keep acceptance compact and separate: **composition/style**, **construction/detail**, **alpha/export when relevant**, and **actual placement**. A pass in one does not imply the others. For a prominent generated illustration, the minimum useful record is its exact version, intended sizes/backgrounds, a few named relationships inspected, reproducible regions for important findings, and a repair/recheck or stated limitation. One short asset-record entry suffices. Do not require a forensic dossier for every small decorative image.

Fail the relevant gate for confirmed consequential breaks or cutout contamination. If a prominent construction remains unresolved after inspection, retain **not assessed** for that relationship and do not call the entire asset verified. A minor blemish outside its stated use may be accepted with that limitation; hiding a meaningful error by shrinking, blurring, covering, or adding texture is not a repair. Accept deliberate stylization when the visual evidence and brief support it.

Do not stop at the first usable output if a clear, fixable visual weakness remains. Continue targeted work within available tools and the authorized budget. When progress stalls, change the source, medium, or composition rather than looping near-identical requests. A missing capability or unresolved reference fidelity may leave a blocked asset, not a pretend final. Conversely, stop once the design works; do not damage a strong image chasing forensic perfection or proof of human authorship.
