# Proactive asset creation and integration

Use this guide while composing visual work, before assuming the design needs no imagery. The designer owns identifying, creating, integrating, and improving appropriate assets. The user need not separately say “generate an image.” These are workflow prescriptions adapted from the Visual Asset Pipeline; they are not a guarantee about a future host's tools. See [source notes and licenses](integrated-source-notices.md).

## Contents

- Choose a production method
- Map opportunities and discover capabilities
- Choose transparency and layers
- Direct image generation
- Integrate actual files and close the loop
- Construct exact graphics
- Make annotations useful
- Preserve editability and rights
- Handle missing capabilities

## Choose a production method

Start with what the image must communicate and what must remain exact. Choose a method that can deliver both. Use more than one tool when that gives useful creative freedom without sacrificing accuracy.

| Visual problem | Effective route | Important limitation |
| --- | --- | --- |
| Human scene, material, atmosphere, or expressive illustration | Available image generation, editing, licensed photography, or supplied imagery. | Inspect identity, anatomy, physical plausibility, crop, and context. |
| Navigation, action, or status icon | Approved project icon family; otherwise select one suitable maintained family. | Follow [iconography](iconography.md); do not improvise unrelated SVG glyphs or generate tiny bitmap controls. |
| Expressive pictogram, onboarding vignette, mascot, or rich 2D art | Native image generation, editing, approved illustration, or a capable illustration workflow. | A transparent raster can integrate cleanly with UI; it does not have to be a custom SVG. |
| Exact wordmark, technical diagram, mask, or simple geometric construction | Approved source, vector tools, or appropriate layout tools. | Syntax validity does not establish good appearance. Do not disguise a raster as editable geometry. |
| Exact headline over original imagery | Create the image, then use controlled typography. | Verify final copy and export, even with deterministic typesetting. |
| Technical schematic or factual chart | Use verified data and deterministic plotting or diagram tools. | Do not substitute a plausible-looking generated diagram for a correct one. |
| Editorial page, report, slide, or brochure | Use the requested editable format and its relevant skill. | Render every final page or slide; source structure alone is insufficient. |
| Product or packaging mockup | Use suitable mockup tools or controlled perspective placement. | A mockup is not a dieline, a manufacturing specification, or proof of final materials. |
| Design critique | Use a duplicate, overlay, or side-by-side comparison with precise callouts. | Never silently alter the evidence being discussed. |

Do not treat tool use as a performance. Use the method that improves the work. Custom SVG is valuable for intentional geometry, but reducing a rich illustrative idea to easy circles and rectangles may weaken it. Conversely, generating a bitmap of a simple technical diagram adds uncertainty without improving communication.

## Map opportunities and discover capabilities

1. Inspect the actual brief, project, approved assets, references, components, and installed icon family. Preserve the stack and current direction. For a narrow repair, stay within the affected area.
2. Consider each significant surface: would imagery strengthen subject recognition, emotion, atmosphere, category distinction, onboarding, or visual pleasure? Mark it **needed**, **helpful**, or **unnecessary**. Do not require a functional story for beautiful artwork, and do not decorate every table row.
3. Define the visible opportunity, then choose reuse, edit, generation, licensed source, or deterministic geometry. An empty state may benefit from a small illustration; a repeated toolbar generally benefits from coherent symbols. A rich background and a foreground cutout can coexist when they have different jobs.
4. For each chosen asset, record only what affects production: role/consumer, subject, medium, focal area, ratio, alpha, surrounding palette, crop, smallest display size, and essential invariants. Use the [asset record](../assets/asset-record-template.md) for multi-asset work. Do not turn one image into a planning project.
5. Inspect the live tools before declaring generation unavailable. In ChatGPT, prefer the built-in image tool for appropriate raster work, including supported transparent output. Read its current instructions and schema. Do not request an API key for a native tool that does not need one or assume a paid external API is the only option.
6. Generate the strongest composition's main asset early, inspect it in a provisional layout, then use its approved properties as the family anchor. Create siblings with consistent palette, detail density, edge character, viewpoint, lighting, and scale. Produce individually usable files, not a sheet that must be guessed apart.

Use the current host's actual output and continuation rules. If generation must end the turn, save the asset/consumer mapping first and resume when permitted. If the tool can continue, continue through integration and QA. Do not invent a turn-ending limitation, a filename, seed, model, cost, or export route. Native generation and separate paid APIs have different authorization and capability requirements.

## Choose transparency and layers

| Intended use | Background choice | Acceptance condition |
| --- | --- | --- |
| Mascot, product cutout, floating 2D illustration, object crossing a panel, independently animated foreground | True alpha, with complete subject silhouette and useful padding | Visible subject plus real transparent exterior; clean edge against the actual surfaces and light/dark mattes. |
| Landscape, photographic setting, atmospheric full-width section, editorial image rectangle | Opaque full scene | Deliberate focal area, copy-safe region where needed, and acceptable desktop/mobile crop. |
| Foreground over a continuous environment | Separate cutout and scene | Shared perspective/light and independent placement; no unwanted opaque rectangle around the cutout. |
| Material, grain, or motif overlay | Alpha or opaque tile according to compositing intent | Inspect seams, opacity, repeat scale, and readability in context. |
| Operational control or navigation symbol | Approved vector icon | Clear silhouette and accessible control semantics at actual size. |

Set the tool's supported transparency control as well as stating the visual requirement. Request no unwanted floor, frame, opaque matte, generated UI, or lettering for a cutout. Allow deliberate translucent edges and soft shadows when they suit the surface; consider a separate shadow layer when independent adjustment is needed. Do not confuse a transparent background with a transparent object. Simple alpha cannot dynamically refract changing page content like physical glass.

Verify decoded alpha, not the filename or preview. RGBA can be fully opaque; an entirely transparent image has no usable subject. A painted checkerboard remains part of the image. The optional preflight `--require-cutout` check establishes visible pixels and some fully transparent pixels, not correct segmentation. Inspect hair, paper edges, white fabric, fine stems, interior gaps, and shadows on contrasting backgrounds. Never globally erase white to remove a background, since white may belong to the subject. Use the permitted image edit/matting workflow and preserve the original.

Plan occupied bounds, not only canvas size. Excess alpha padding can make the subject too small despite a large CSS width. Trim only as a deliberate supported derivative, then recheck its anchor and crops. Keep the complete subject for an isolated asset unless intentional edge cropping is part of the composition. Alpha does not make text flow around the silhouette or shrink a rectangular interactive hit area automatically.

## Direct image generation

Inspect every supplied reference before editing or transforming it. Identify what is fixed: identity, product proportions, silhouette, packaging text, logo, color, camera position, or composition. Record what the user wants changed.

Build an image brief from concrete decisions:

1. **Subject and meaning:** Who or what is shown? What action or relationship expresses the proposition?
2. **Composition:** Focal subject, scale, point of view, foreground/background relationships, crop, and reserved space for text.
3. **Light and material:** Source direction, softness, surface finish, texture, environment, and plausible contact shadows.
4. **Visual language:** Photography, illustration, collage, print process, or another coherent medium. Describe its characteristics rather than accumulating fashionable adjectives.
5. **Constraints:** Exact product details, prohibited changes, required aspect ratio, transparency, consistency with a series, and any meaningful exclusions.

Avoid relying on “award-winning,” “premium,” or “8K” to supply decisions. Resolution language does not establish composition, faithful detail, or actual output dimensions. Ask for exact dimensions only when the tool supports them and verify its actual result.

Explore distinct concepts before refining one result when the scope calls for new art direction. For a focused uncertainty within the selected concept, vary one consequential feature at a time. A coordinated compositional revision may change several related features. A large batch of near-duplicates is not evidence of a broad search.

For raster creation and editing, use the available image tools according to their current instructions. Do not substitute improvised bitmap manipulation where a governing tool requires a particular workflow. For exact vector or diagram work, use the appropriate native construction instead of image generation. In ChatGPT, use native image generation for rich 2D art even when it is destined for a web interface. A code-centric task does not require code-drawn artwork.

For example, a journal onboarding screen might use one isolated 2D field-study vignette with a complete silhouette and an intentionally limited ink-and-wash palette. A travel chapter may instead need one opaque photographic environment with quiet space around live type. These are examples of medium selection, not mandatory styles. Keep navigation and text outside the generated image.

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

Use [asset quality and repair](asset-quality.md) for a systematic whole-image, native-pixel, and in-context audit. Inspect the repaired region plus surrounding regions and sibling assets. Do not make every illustration photographic or add fake imperfections merely to make an image appear less synthetic.

## Integrate actual files and close the loop

**Acquisition.** Use an actual mounted output, documented file reference/export, byte response, or authorized reachable download. Follow the host's image storage rules. A preview or opaque ID alone is not a project file. If a preview is the only result, discover a supported export route; otherwise record the precise blocker. Do not substitute a remote placeholder, guessed path, or blank asset slot and call it complete.

**Persistence.** Preserve the original and obtain the real bytes for the project using its existing asset convention. Decode the file, record dimensions/format/hash, and preserve alpha in delivery formats. Keep useful derivatives within native resolution unless an upscale is intentional and disclosed. Do not rename file extensions as conversion. Keep private generation records out of public runtime directories.

**Transfer.** Treat chat storage, GitHub, and a desktop as distinct filesystems. A chat sandbox link is not a Windows file path. Use a documented binary/file transfer or the project's authorized Git workflow; a supported text transport needs programmatic encoding/decoding and destination hash verification. Never create a remote or publish private files merely to move an image. Include the actual asset and its consumer together in an authorized change.

**Composition.** Implement the real import/URL, intrinsic dimensions, responsive sizing, focal position, and layer order. Keep copy, controls, values, and semantics in HTML/native components. Use alt text according to purpose and empty alt for decorative imagery. Prevent decorative overlays from intercepting pointer/keyboard access. A full scene spanning sections needs one shared positioning context where continuity is intended. A cutout may use contain, a scene may use cover; inspect the actual crop rather than treating either as universal.

**Responsive and motion work.** Judge the asset at its smallest and largest real uses. Recompose, choose a meaningful crop, or generate a purposeful variant when a desktop scene fails on mobile. Do not delete its expressive contribution automatically. Align independent asset layers with the shared motion brief, including settled/reduced-motion states. Keep stable controls usable while artwork moves.

**Recheck.** Run project checks, confirm image decoding and path resolution on actual routes, and visually inspect the integrated result at representative widths. Inspect lazy-loaded sections after scrolling and all relevant backgrounds/masks. Check clipping, light direction, subject scale, edge halos, text contrast, layout shift, and control access. The asset must work inside the design, not only in a flattering standalone preview.

**Repair until fit.** Diagnose whether the defect belongs to the artwork, alpha/export, transport, or layout. Repair that layer. A correct cutout need not be regenerated because CSS positioned it badly; incorrect anatomy cannot be fixed by shrinking it until it is hard to see. After repeated unproductive attempts, change the method, simplify the concept without losing its intent, use an approved alternative, or state the unresolved blocker. Do not impose the source pipeline's default two-revision ceiling over the user's quality expectation. Respect actual quotas, budget, and tool boundaries, and avoid unbounded near-duplicate generations.

Keep completion evidence precise: **planned → generated → prepared → installed → integrated → verified**, or **blocked** with the last successful checkpoint. Reused assets enter after source inspection. “Generated” can mean a tool returned an image; “verified” requires file, placement, visual, and relevant interaction evidence. Never award visual PASS based on a successful build or a generated report.

## Construct exact graphics

For exact identities, diagrams, and graphic patterns, define the visual relationship before writing paths. Use a coherent grid or geometric logic when useful, then make optical corrections. Check joins, counter shapes, apparent stroke weight, corners, spacing, silhouette, and small-size behavior. For interface icons, start with the existing family and use the [iconography route](iconography.md). Do not improvise a complex SVG illustration when generated transparent art would look better.

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
