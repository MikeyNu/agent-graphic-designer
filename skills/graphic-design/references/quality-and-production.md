# Quality and production

Use this guide before claiming a graphic is finished, client-presentable, accessible, or prepared for a production workflow. The critique method is a practical synthesis, not a scientific measure of beauty. Technical standards apply only within their stated scope.

## Contents

- Define acceptance
- Critique the design
- Verify content and assets
- Inspect real viewing conditions
- Preflight each medium
- Record evidence and release status

## Define acceptance

Before polishing, record the required message, audience, delivery format, dimensions, mandatory content, intended tone, source needs, and difficult conditions. Separate objective gates from judgment. Wrong event details are a defect regardless of the layout's quality; selecting a more playful typeface is a judgment that depends on the brief.

Use four result states consistently:

| State | Meaning |
| --- | --- |
| PASS | The named check was actually performed on the identified artifact under stated conditions and met its criterion. |
| FAIL | The check was performed and found a relevant defect. |
| NOT RUN | The check is needed or useful but was not performed. State why and the consequence. |
| N/A | The check does not apply to this artifact or requested delivery. Explain non-obvious exclusions. |

Do not convert NOT RUN into PASS because the file is likely correct. Do not mark a needed check N/A merely because a tool is missing. Distinguish an optional diagnostic from a required release gate.

## Critique the design

Inspect the actual render and compare it with the brief. Give concrete observations under these five dimensions:

| Dimension | Strong evidence | Weak evidence |
| --- | --- | --- |
| Fit | The visual idea expresses a specific audience need, product property, place, or story. | A rationale could describe any product; styling leads the communication. |
| Communication | Required information is clearly grouped and readable at intended size. | Essential text competes with ornaments, gets cropped, or requires explanation outside the artwork. |
| Distinctiveness | A coherent idea is recognizable beyond fashionable ingredients. | A new name could replace the existing name without changing the image or composition. |
| Craft | Optical spacing, typography, color, crop, image details, and alignment are intentional. | Nearly aligned edges, accidental tangencies, weak rags, blurry assets, or inconsistent strokes remain. |
| Coherence | Elements and variants reinforce a clear direction while adapting to different formats. | Every section or format seems to belong to a different visual system. |

Rate each as strong, adequate, or weak only to organize judgment. Supply visible evidence and a practical correction. Do not present a self-awarded 9.7/10 as validation. A high aesthetic score cannot offset a content or production failure.

Use a relevant professional benchmark, not an intentionally poor comparison. Compare composition, typography, asset quality, and real application. Awards, brand prestige, or an attractive mockup do not prove that a particular work suits this brief.

For a large or difficult task, use a fresh reviewer with the brief and actual artifacts. Do not prime the reviewer with praise or desired scores. Ask for the most consequential visible defects and what would resolve them. Treat another AI's critique as inspection support, not representative audience research.

### Order revisions by consequence

1. Correct false, missing, misleading, or unusable content.
2. Fix the concept or hierarchy if the communication is wrong.
3. Resolve major layout, type, image, crop, or accessibility defects.
4. Refine spacing, optical alignment, texture, and finish.
5. Re-export and reinspect the affected outputs.

Do not polish a weak concept into a more expensive weak concept. Conversely, do not reopen a successful identity because a reviewer prefers another style. Connect every proposed change to the brief or an observed defect.

## Verify content and assets

Compare final text with the approved copy, including names, dates, times, addresses, phone numbers, links, prices, units, symbols, and claims. Check missing words, duplicated words, accidental placeholders, altered punctuation, and significant line breaks. Extraction or OCR can help, but neither proves good typesetting.

For factual graphics, verify values, labels, totals, axes, legends, scales, units, sources, and distinctions between measured data and projections. A visually smooth curve must not imply observations that were never supplied.

For QR codes or barcodes, decode the exported version and verify the content. Check quiet zones, contrast, deformation, size, and intended use. A generated image resembling a code does not establish function. If a destination is unknown, do not invent it to finish the layout.

For photographs or illustrations, check the factual and visual integrity required by the brief. Inspect product proportions, labels, context, anatomy, contact, reflections, shadows, perspective, joins, and unintended duplication. Distinguish deliberately impossible imagery from accidental errors. Preserve the identity of supplied people, products, and brands according to the requested edit.

For typography, verify actual fonts, styles, glyph coverage, shaping, variable-font instances, clipping, and altered breaks after export. Test the source and delivery files independently. A correct font declaration does not prove the renderer loaded the font.

## Inspect real viewing conditions

Use at least the relevant views below. Record the actual size and renderer rather than writing “looks good on all devices.”

| View | What it can reveal | What it cannot prove |
| --- | --- | --- |
| Full composition | Hierarchy, balance, grouping, visual direction. | Small-print readability at actual use size. |
| Actual delivery size | Reading comfort, essential details, apparent type size. | Every user's visual experience. |
| Smallest important application | Recognition, crop survival, complexity limits. | Quality of larger print detail. |
| Detail crop | Letterforms, edges, masks, retouch defects, fine alignment. | Overall communication. |
| Flat export | What the viewer receives without staging. | Physical material and print finish. |
| Context mockup | Scale and placement in a plausible setting. | Production correctness or audience response. |
| Grayscale or color-vision simulation | Lost distinctions and some hierarchy problems. | Complete accessibility. |
| Print proof | Reproduction on a named setup and substrate. | Every future press run or viewing condition. |

For multi-page work, use a contact sheet to find system inconsistency and inspect each page at useful size. A contact sheet alone cannot verify small text. For social graphics, inspect required crops and realistic downscaling or compression. Do not rely only on a large desktop view of a phone graphic.

For animations, inspect the sequence as motion as well as representative frames. Verify that essential copy has adequate reading opportunity and a usable static or reduced-motion presentation where required. Do not infer temporal quality from one still.

## Preflight each medium

### Raster

Inspect dimensions, aspect ratio, crop, image detail, compression, alpha channel, and color profile. Effective PPI depends on the actual placed image after cropping:

`effective PPI = pixel dimension / printed dimension in inches`

For example, an image spanning 1,800 pixels across a 6-inch printed width has 300 effective PPI in that direction. Changing a metadata value to 300 without adding pixels or changing placement does not add detail. [Adobe's current resolution guidance](https://helpx.adobe.com/photoshop/desktop/crop-resize-transform/resize-adjust-resolution/image-size-resolution-and-resampling.html) distinguishes pixel dimensions, physical dimensions, resolution, and resampling. Follow the provider's requirements rather than treating one PPI value as universal.

Inspect both horizontal and vertical effective resolution if scaling is nonuniform. Upsampling does not establish that missing source detail has been recovered. Check the actual result for halos, sharpening artifacts, moire, broken texture, and unintended transparency.

### Vector

Check dimensions, units, viewBox, clipping, path continuity, small counters, stroke behavior, blend effects, raster dependencies, and fonts. Inspect one-color, reversed, and small versions when the identity requires them. XML validity establishes syntax only. See [SVG 2 coordinates](https://www.w3.org/TR/SVG/coords.html) for viewport and aspect-ratio semantics.

An editable vector source must contain the intended editable construction. A flattened bitmap inside SVG is still a bitmap. If the client needs text editing, preserve the font dependency and permitted access. Keep a source copy before outlining text.

### Print and packaging

Establish the provider's specifications: final trim, bleed, safe area, stock, color space, destination profile, output intent, ink limits, PDF standard, marks, folds, binding, die cuts, and finishes as relevant. Avoid invented universal bleed values or rich-black recipes.

The [Adobe InDesign production guide](https://helpx.adobe.com/indesign/desktop/print/print-production-and-file-creation/produce-print-ready-pdf-files.html) describes resource, font, overset-text, and export checks. Its general recommendations must be reconciled with the actual print provider's workflow.

Inspect overprint and separations where applicable. Check font embedding, missing links, placed-image resolution, panel orientation, fold conflicts, cut lines, varnish or special-ink layers, and whether essential content sits safely inside the usable area. Do not invent regulatory wording or barcode data.

Use the provider's color-management requirements. [ICC guidance](https://www.color.org/faqs/) makes clear that device and pipeline differences matter, including print workflows accepting RGB. Check actual color conversion and proof status. A screenshot cannot guarantee metallic ink, fluorescence, paper whiteness, or spot-color fidelity.

### Digital documents and interfaces

Check rendering and content at the intended sizes, accessible text alternatives, heading structure, reading order, selectable text, links, text reflow or resizing when supported, and relevant interaction states. For websites, contrast is only part of [WCAG 2.2](https://www.w3.org/TR/WCAG22/). Do not certify the whole experience from a palette calculation.

WCAG [text-spacing guidance](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html) concerns tolerance of user-applied spacing in its applicable content. It is not a compulsory authored style and currently does not apply to PDF under that success criterion. Do not apply one format's check indiscriminately to another.

### Rights and editable handoff

Check asset provenance, actual permissions, and permitted dependencies. Distinguish supplied assets, purchased stock, original artwork, generated content, and unlicensed references. Do not imply exclusivity, trademark clearance, or model/property releases without evidence.

[Adobe Fonts licensing](https://helpx.adobe.com/fonts/web/font-licensing/font-licensing.html) distinguishes finished outputs from editable client access and font-file redistribution. Other providers have their own terms. Do not package every installed font by default.

Open the editable source and verify that it corresponds to the final export. Use understandable file names and variant labels. Keep reference material and proposed annotations separate from approved artwork.

## Record evidence and release status

Use the [QA record template](../assets/qa-report-template.json) when useful. Record the artifact version, method, conditions, result, defects, changes, and remaining limits. Technical tools must leave visual inspection NOT RUN until someone actually views the artifact.

Distinguish these delivery states:

| Status | Required evidence |
| --- | --- |
| Concept study | Visible idea suitable for comparison; unresolved facts and constraints labeled. |
| Review draft | Developed artifact inspected internally, with named outstanding decisions or reviews. |
| Final digital artwork | Requested digital outputs checked against the brief; applicable critical gates passed. |
| Prepared for a named print workflow | Known production specification applied and preflighted; proof and approval state explicit. |
| Client-approved | Actual approval by the authorized client, beyond internal critique. |

Do not claim final readiness while a material required check is unperformed. Explain the specific limit and complete unaffected work. Stop additional testing once relevant gates pass and the brief is met; repeat checks only after changes or to resolve a real risk.
