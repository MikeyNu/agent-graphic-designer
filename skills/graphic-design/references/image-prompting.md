# Direct and repair generated imagery

Use before generating or materially editing an expressive image. Pair this guide with [asset quality](asset-quality.md). Prompting reduces ambiguity; it cannot certify the result. Use the available image tool, its current schema, and any governing host skill. Do not invent model settings, seeds, masks, negative-prompt fields, or guaranteed pixel preservation.

## Contents

- Write a small visual specification
- Prevent predictable construction errors
- Use references and exclusions correctly
- Make controlled repairs
- Avoid misleading shortcuts
- Apply the examples

## Write a small visual specification

Make the creative decision first. A prompt should express the selected visual idea, not ask the generator to supply a generic premium style. For one asset, a short paragraph or these compact lines usually suffice; omit irrelevant fields. There is no required magic format or word count.

```text
Use: placement, medium, smallest and largest important use.
Subject: the concrete subject and meaningful action or relationship.
Construction: important parts, connections, front/back order, and necessary counts.
Composition: viewpoint, silhouette, crop, balance, and reserved space.
Finish: coherent palette, materials or mark-making, and lighting when applicable.
Delivery: actual transparency or scene, plus essential exclusions.
Preserve/change: for edits, identify the target and the approved invariants.
```

Spend detail on likely failure points. An interwoven ribbon needs a clear crossing relationship more than extra lighting adjectives. A flat mascot needs a readable silhouette and limb/prop connections more than simulated camera settings. A decorative object does not need an exhaustive engineering specification.

Before generation, write a few observable acceptance conditions in the working asset record: for example, a handle attaches at both ends, each visible strip has two traceable boundaries, and a pattern follows its surface. Derive these from the chosen design. Keep them separate from the generator's prompt and preserve them during review. This prevents explaining away an accidental defect after seeing an attractive output. A coherent surreal idea may deliberately break physical rules; specify that choice without licensing unrelated errors.

## Prevent predictable construction errors

**Name objects and their relationships.** Prefer “one ceramic cup with one handle attached at its upper and lower ends” to “beautiful sculptural beverage object.” Specify counts only when they matter. Use stable nouns instead of ambiguous chains of “it,” “behind this,” and “the other one.”

**Describe the visible construction.** For a curved sheet, establish whether it is one continuous strip or several separate sheets. Specify its front, back, thickness, crossings, and free ends only as far as they will be visible. For a 2D drawing, describe layer order and the relationship of outline and fill. Avoid forcing photorealism onto an illustration.

**Resolve conflicting instructions.** A transparent canvas is different from a glass object. A separate soft ground shadow is different from an opaque studio floor. Flat screenprint, mirror-polished 3D, and photographic paper fibers cannot all govern the same surface without a deliberate mixed-media plan. Choose the relevant medium and construction before adding finish.

**Control decorative detail.** Decorative grids, stitching, perforations, keys, spokes, and chains add relationships that must remain coherent. Use a detail level appropriate to the delivered scale. If exact spacing, count, text, or mechanism is essential, use an approved source, controlled typesetting, or a capable native geometry workflow for that part. Do not regenerate an entire illustration just to draw an exact label. Do not reflexively replace expressive art with crude custom SVG.

**Reduce ambiguity before adding words.** If several objects merge, try a clearer viewpoint or separation, a construction reference, or independently usable layers with matched perspective and light. Retain the idea's visual character. Complexity is not inherently bad; unnecessary simultaneous constraints make a failed result harder to diagnose. Research on compositional benchmarks motivates checking each relationship, not imposing a universal object limit.

## Use references and exclusions correctly

- Inspect every reference. Label its role: edit target, geometry reference, style reference, palette reference, or insert. State what to borrow and what to preserve. A mood reference is not automatically an edit target or permission to copy its exact composition.
- A simple construction sketch or approved render can communicate a difficult join better than a paragraph. Use supported image-reference/control features only. Do not claim that the generator obeyed a sketch without comparing the result.
- Put the desired state positively first: “two separate straps with visible gaps” is more informative than “no weird straps.” Add only relevant exclusions such as unwanted lettering, props, backdrop, or extra limbs.
- Follow the selected model's treatment of negatives. An ordinary exclusion in a conversational prompt is not a dedicated negative-conditioning parameter. Midjourney syntax and legacy diffusion negative lists are not portable commands. Official Google documentation contains legacy negative-prompt examples alongside newer model restrictions; verify the active interface rather than copying the example blindly.
- Use exact text only when raster lettering is genuinely required. Quote it, constrain location, and inspect it afterward. Keep interface text, operational labels, logos, and factual data in controllable layers whenever practical.
- Request true alpha through the live tool's transparency control as well as the description. Specify the complete silhouette and permitted shadows. Do not request a checkerboard background as a substitute.

## Make controlled repairs

1. **Localize.** Describe the visible failure and its region with enough context to identify it. Keep the evidence crop separate from the original. Do not ask only to “make it less AI.”
2. **Choose ownership.** Distinguish drawing/construction, texture/material, alpha/export, and layout. Repair the responsible layer. An alpha edit cannot correct a branching pipe; moving CSS cannot reconnect a handle. When an editable vector or native source already exists, repair that source precisely instead of unnecessarily regenerating it. This differs from forcing a rich new illustration into a crude custom SVG.
3. **Request an observable delta.** State the corrected relationship, the permitted edit region, and the protected silhouette, palette, viewpoint, light, object count, and surrounding details. Mention only invariants that matter. Use an actual mask only if the tool supports it; a text region is guidance, not a pixel lock.
4. **Compare, not just admire.** Inspect original and candidate at matched scale, including the repaired region, adjacent joins, and protected areas. Recheck actual alpha and every affected placement. A repair that removes one fault but changes identity or introduces another is not a pass.
5. **Retain or change approach.** Accept a verified improvement, revert a regression, or revise the method. If the same class of failure persists, simplify the ambiguous relationship, use a better structural reference, split suitable layers, or switch to a more controllable source/medium. Do not endlessly append adjectives or regenerate near-duplicates. Respect actual time, quota, and budget; report unresolved material limitations.

Use the best approved source as the next edit input, not automatically the latest output. Repeated edits can drift or degrade surrounding detail. A request to preserve everything is useful guidance but not a guarantee. If exact preservation is required, use an authorized precise editing/compositing route that can enforce it.

## Avoid misleading shortcuts

| Tempting shortcut | Better practice |
| --- | --- |
| “No AI slop, flawless, anatomically perfect, award-winning, 8K” as the main prompt | Specify the visible construction, medium, composition, and relevant constraints. Verify native dimensions separately. |
| A huge copied negative list or incompatible model syntax | Use a few relevant exclusions supported by the current tool. Inspect whether they worked. |
| More detail and maximum quality for every defect | Determine whether the problem is resolution, ambiguous structure, wrong content, or the chosen method. Higher detail can render the same mistake more crisply. |
| Fake grain, pores, scuffs, or asymmetry to disguise generation | Preserve intentional style and fix the actual defect. Do not misrepresent synthetic content as documentary evidence. |
| Upscaling or generative enhancement as forensic evidence | Inspect source pixels. Enhancement can invent different details and requires its own review. |
| A generator's explanation or self-rating as acceptance | Inspect the image against the prewritten observable conditions. |
| Treating one successful image as proof of a universal prompt trick | Record the exact prompt/input/tool and bounded outcome; compare repeated, representative cases when making broader claims. |

## Apply the examples

These are original working examples, not benchmark-proven recipes or a compulsory aesthetic. Adapt them to the composition.

**Stylized 3D cutout, structure before finish**

> Create a sculptural brand illustration for a data collection service. One broad ivory paper strip makes a shallow wave with two visible free ends; it remains a single unbranched surface of consistent thinness. A cobalt arch stands separately behind it, with a visible gap at their nearest crossing. Three colored markers sit on the paper. Use sparse engraved observation marks that follow the paper surface, a matte paper finish, and soft directional studio light. Preserve a strong diagonal silhouette at small size. Isolate the complete sculpture on a genuinely transparent canvas, without text, an opaque floor, or unrelated objects.

This example deliberately chooses a less ambiguous construction. It is not a demand to remove all complex geometry from future work. Exact data should not be baked into such an illustration.

**Expressive 2D cutout**

> Create a flat editorial illustration of a blue watering can tipping toward one potted seedling. Use warm ochre and ink-blue shapes with restrained hand-drawn texture. The handle is an open loop attached to the body at both ends; the spout visibly connects to the body and ends in one clear outlet. Keep the can, plant, and a few falling drops legible as separate shapes. Use consistent outline treatment and purposeful irregularity. Deliver an isolated transparent composition, without lettering or a rectangular background.

**Targeted alpha repair**

> Edit the supplied image only to clean the cutout boundary. Remove the detached pale flecks around the upper-left paper edge and the residue inside the central opening. Preserve the actual ivory paper, thin edge highlights, blue arch, orange disc, all interior details, colors, framing, and object positions. Keep real transparent exterior and interior gaps. Do not introduce a floor or alter the composition.

**Targeted 2D construction repair**

> Reconnect the separated spout to the watering-can body with one continuous filled shape and a matching outline. Preserve the outlet, handle opening, palette, flat illustration style, plant, droplets, canvas, and transparency. Change the join only; do not turn the drawing into a 3D render.

The official prompting guidance and research scope are recorded in the [sourcebook](sourcebook.md#generated-illustration-quality-and-prompting). The construction-focused templates and repair choices are design synthesis, not an infallible detector.
