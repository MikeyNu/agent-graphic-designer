# Illustration QA and prompting validation, 31 October 2026

## Scope and research

The owner reported that the Mera sign-in page looked good but its generated illustration did not receive sufficiently discerning artifact review. This update strengthens production craft checks for 2D and stylized 3D art. It does not claim a reliable AI-origin classifier or an ability to catch every anomaly.

Research covers nine source entries: three official prompting/documentation groups and six research entries. See [generated illustration quality and prompting](../skills/graphic-design/references/sourcebook.md#generated-illustration-quality-and-prompting). Official product advice, historical benchmark results, and original production synthesis are kept separate. No model benchmark, detector weights, or user study was reproduced.

Changes: a compact image-prompting guide; concrete contour/crossing/surface inspection; explicit alpha-viewer verification; separate composition, construction, export and placement decisions; exact-input and evidence fields in the existing record; three added evaluation definitions. The main skill remains 217 lines. No new detector, scoring model, dependency, or automatic repair framework was introduced.

## Fresh-context exercises

Reviewers received only the skill, the task-local brief and raw image paths. They were not given expected answers, the author's diagnosis, another reviewer's outcome, or the evaluator definitions. The generated-asset creator received the approved subject/palette and output conditions. The second review of the repair correctly received the requested preservation constraints because those define that task.

| Exercise actually run | Observed result | Scope and limitation |
| --- | --- | --- |
| Mera baseline review with the earlier instructions | Flagged apparent pale/colored edge residue in the raw transparent-image viewer. Found no clear structural break. | This edge finding was a false positive, not evidence of defective shipped alpha. |
| Mera review with revised instructions | Compared original and WebP, traced visible arch/sheet/disc relationships, and checked actual alpha-aware mattes. Accepted the pictured desktop use; hidden sheet connectivity remained uncertain rather than invented. | Decoded alpha was identical. This does not establish that every artistic or geometric weakness was found. The owner's precise suspected anomaly was not localized in the brief, so the review cannot claim to have resolved that exact concern. |
| Known 2D construction pair | Located the detached spout in R; accepted the connected construction in S; preserved intentional floating droplets and uneven marks. Also distinguished baked-background raster captures from cutouts. | Controlled diagnostic fixtures, not a representative art benchmark. Final layout at both target sizes was not claimed by that reviewer. |
| New 2D field-research illustration | Created an actual 1536 x 1024 RGBA notebook, magnifier and specimen. Recorded construction conditions before generation, then inspected native joins and 560px/220px proofs on cream, pale blue, white and dark backgrounds. | One generation, not comparative proof of prompt superiority. Accepted as an isolated decorative asset; actual application placement was not tested. |
| Localized native edit of R | Reconnected the spout, but changed the canvas from 588 x 474 to 1397 x 1126, rounded previously square top corners, and introduced mottling/gradients into flat fills. Rejected as the requested local repair. | Demonstrates why a fixed target defect is insufficient when preservation constraints fail. With the editable source available, the appropriate final repair would use that source. No production image was replaced. |

The root agent personally inspected the original Mera image, the native-region desktop-browser proof, both controlled fixtures, the new 2D asset and its size/background proofs, and the generated repair. Independent review supplements that inspection; agreement is not ground truth.

## Correction discovered during R&D

An exploratory Mera edge-cleanup edit was issued before correct alpha compositing established whether the apparent fringe was real. It should not have been issued. The final workflow now requires that check before regeneration. The edit was not installed or presented as a verified improvement.

The baseline and raw viewer could expose RGB values under zero alpha, producing apparent specks or a dark surround. Correct browser compositing of the shipped WebP showed clean edges in the examined regions. This is recorded as a process correction, not hidden as a successful repair. The live Mera site and its approved artwork were unchanged.

Native regions actually reviewed included the left paper edge, paper joins, interior opening, and adjacent orange rim. Root desktop-browser views used oriented source rectangles beginning at (60,190), (360,270), and (720,480), each 600 x 470 pixels. The independent reviewer additionally traced the blue arch and full orange perimeter region. These checks do not reconstruct hidden geometry.

## Local desktop evidence

Headed Microsoft Edge 156.0.4314.50 on the authorized Windows desktop rendered the [controlled fixture](illustration-structure-cases.html) and the native Mera region board. No cloud browser or GitHub CI was used. Test-owned browser processes closed after capture. Static proof images for the new 2D asset were created as inspection surfaces; they are not claimed as browser application integration.

The fixture is retained as reproducible source. R has an intentionally detached spout; S has connected contours. Both include deliberate floating drops and uneven marks. Raster captures contain baked cream and small gray lower-corner wedges from the rounded parent. The reviewer correctly treated that as a separate export/placement issue. This is a QA fixture, not a proposed client illustration or a reason to substitute crude SVG for expressive artwork.

Generated source hashes establish the specific run; raw private-site artwork and temporary review images are not republished here.

| Artifact | Native pixels | SHA-256 |
| --- | --- | --- |
| Mera original PNG | 1402 x 1122 | `2292de31139d363219913ab4554e972655e96dd2b1cff8f5271e5d19a358dfbb` |
| Mera shipped WebP | 1402 x 1122 | `b8fe0240caaec812a48bc78fc99f7732b62412e7eaf7c0dd7c3451e9e75e3c5e` |
| Unnecessary exploratory Mera edit | 1402 x 1122 | `599c902ad0a41b8485a3d88ee9a015e5b6d9f949becb1f52ce27574e526344a6` |
| R raster capture | 588 x 474 | `14b153a1f71336c49c10e1625da57e654809d3834bb746e0e247b870b6a3b61e` |
| S raster capture | 588 x 474 | `e18d029139d5711a086f001faa428e07ba40d8187d052d24eb6c4b78283a18b1` |
| New 2D illustration | 1536 x 1024 | `9a686ba2d6ffc88c7ebd5c511c232d0c2e3b2b128b06b5c6cc7fe20e7719ec7f` |
| Rejected scoped-repair candidate | 1397 x 1126 | `638e6c4919a557918983381469a27ebe1e2f700de1b96dcc7f0eae0f45e4a1dc` |

## Exact generation inputs

All three calls used native image generation, not a fallback API. No seed, internal model name or quality parameter was exposed or invented. These examples are run records, not guaranteed recipes.

### New 2D image

No reference input; transparency enabled.

```text
Use case: illustration-story.
Create one transparent 2D editorial illustration for an established field-research app's “save a discovery” state. The approved subject is one open field notebook, one magnifying glass, and one small botanical specimen.

Composition: a compact, gently oblique overhead vignette with a broad landscape silhouette and generous clean transparent padding. The open notebook is the main shape. Its two warm ivory page surfaces meet at one continuous central fold, with a thin ink-blue cover visible beneath the outer edges. A small botanical sprig rests on the right page. One magnifying glass sits above part of the sprig; its complete ink-blue circular rim and single handle remain plainly traceable, and the handle extends diagonally beyond the notebook toward the lower right. Keep overlaps simple and separated by clear contours. The sprig has one continuous green stem with a few clearly attached leaves. Preserve its visible continuation through the lens. The lens is visually clear with only a restrained drawn glint.

Finish: flat shapes, confident subtly irregular ink contours, and very light drawn hatching that follows the paper and leaves. Use ink blue around #203D50, warm ivory around #F6EFD9, and restrained muted green around #67836A. Keep detail sparse and shapes strong enough to read at both 560 px and 220 px wide over cream or pale blue surfaces. It should feel observant, calm, and editorial, not toy-like or rendered in 3D.

Delivery: genuine transparent background with intact exterior silhouette and interior gaps. No backdrop, floor, enclosing badge, generated interface, text, labels, signature, logo, extra objects, floating flecks, or dramatic shadow.
```

### Scoped 2D repair

Input: R raster capture; transparency disabled to preserve its opaque background.

```text
Edit only the disconnected spout of this flat illustration. Reconnect the detached blue spout to the right side of the watering-can body using one continuous blue filled shape with the same dark-blue outline. Keep the spout's existing upper-right outlet and angle fixed; extend its lower-left base behind the can body so no cream gap remains. Preserve the can body, handle opening and attachments, three pale decorative marks, pot, plant, three floating droplets, colors, flat style, canvas size, cream background and existing corner clipping. No extra objects, no added shadows, no text, no 3D rendering. This is a localized join repair, not a redesign.
```

### Exploratory edge edit, not accepted

Input: original Mera PNG; transparency enabled. Subsequent alpha-aware inspection invalidated the reason for this edit.

```text
Edit the supplied image only to clean its cutout boundary. Remove detached pale flecks around the upper-left paper edge, small residue inside the central opening, and blue/orange stray pixels beyond the sculpture silhouette. Preserve the actual ivory paper, thin legitimate edge highlights, blue arch, orange disc, all interior grid and embossed details, colors, framing, object positions, soft lighting and overall composition. Retain antialiased edges and the real transparent exterior and interior gaps. Do not introduce a floor, a solid matte, checkerboard pixels, text or an extra object. This is an edge cleanup of the same illustration, not a redesign.
```

## Package validation and limits

All **50 package tests passed** in the executor, including link/portable-anchor resolution, core size/frontmatter, license retention, no machine paths or em dashes, and honest QA defaults. Portable generation completed successfully and `git diff --check` was clean. These are software/packaging checks, not asset-quality evidence. Python package checks were not represented as desktop execution.

The executed set is intentionally small: a real 3D illustration, a known-defect/control pair, one new 2D image, and local-edit preservation checks. It supports the practicality of the workflow and exposes important failure modes. It does not establish sensitivity, specificity, a success percentage, human-level artistic judgment, or reliable performance across future image models. No new verification of live Mera authentication or other application flows was performed or needed for this skill-only update.

