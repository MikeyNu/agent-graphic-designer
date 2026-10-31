# Proactive assets, iconography, and visual QA integration

31 October 2026. This update responds to the owner's direct QA finding: agents were underusing image generation, creating weak custom SVG artwork, and waiting for explicit asset requests.

## What changed

Asset assessment is now part of composition and the core operating standard. Agents must identify appropriate imagery themselves, use available native image generation, select alpha foreground art versus opaque scenes deliberately, obtain real files, integrate them, inspect the result, and repair the responsible layer. A dedicated icon guide separates operational symbols from expressive illustration. Rich 2D artwork can be generated raster art; precise vectors and existing icon families retain their appropriate uses.

The production workflow adapts Visual Asset Pipeline at `baf5a97be4e93c8b0d7ebbb2ef112e18c19725bd`. The optical-quality workflow adapts Agent AI Detector at `6f7cba7650409f153888daed9612a545b863fafa`. Their notices are included, and the integrated workflow is self-contained. It preserves provenance while assessing visual quality; it does not claim to prove human/camera origin. Revisions follow progress and the authorized budget instead of inheriting an automatic two-revision ceiling.

## Fresh-context exercises

Three independent agents received the revised skill and task-local briefs, without the expected answers, evaluation rubric, earlier diagnoses, or original user complaint. The two creation prompts did not instruct the agents to generate images. They were asked to complete real static local interfaces. The icon prompt was a focused repair of the existing approved queue. All browser execution used the authorized local Windows desktop and headed Edge 156.0.4314.50 through Desktop Commander. GitHub CI was not used.

| Case | Observed behavior | Executed evidence |
| --- | --- | --- |
| Fieldnote nature journal | Proactively generated a naturalist bird-and-branch illustration on true alpha. Made three visible roughs, selected a fieldbook composition, integrated the WebP, and retained the image in mobile/form layouts. | Native generation, decoded alpha, source/destination hashes, light/dark matte review, rendered desktop/phone views, local form/draft/save/failure and native-dialog checks. |
| Tidemark coastal chapter | Proactively generated opaque portrait and wide coastal environments. Used responsive image selection and editable text, with a real local chapter transition. | Native generation, decoded assets, source/destination hashes, desktop/phone/tablet/short-window inspection, navigation/focus/history/refresh, image failure, and reduced-motion checks. |
| Lantern icon repair | Used verified Lucide source geometry consistently for search, navigation, selects, status, retry, and loading. Preserved approved layout, identity, copy, and state model. Added no unrelated illustration. | Fourteen browser checks and six focused final checks, actual-size screenshots, ready/error/pending/success states, narrow layouts, and forced-colors checks. |

See the [retained implementations and evidence summary](examples/asset-integration-2026-10-31/README.md). These are local prototypes, not production services. All observed assets were actual files consumed by the pages. Separate image requests were unnecessary in both creation cases.

## Findings, repairs, and interpretation

The initial asset choices succeeded, but initial implementations were not flawless. Fieldnote needed mobile word-spacing, image/text spacing, and input-boundary contrast repairs. Tidemark needed a short-window composition repair and stronger local contrast after the image crop changed. Its up-right action arrow also implied the wrong direction; an independent source review prompted a check under the iconography guide, and the agent chose the clearer label without an icon. The icon guide now explicitly covers functional glyphs typed into spans.

Native Edge dialog Tab behavior exposed a recurring harness mistake. Browser chrome can hold focus while the active DOM element is BODY and `document.hasFocus()` is false. The icon agent compared before and after and preserved native behavior. Fieldnote initially added a custom trap, which independent review caught. It removed that trap, recorded the native sequence, and corrected the DOM-only assertion. The interaction and execution guides now state this distinction explicitly. Tidemark also corrected an overflow assertion that mistook scrollbar width for overflow. These were documented test corrections, not hidden product passes.

Final visual inspection included the original portrait and wide coast images, the bird at full/native detail and contact-region crop, a light/dark bird board, integrated desktop and phone covers, the narrow entry form, and desktop/narrow icon states. The bird retains visible drawn detail without a rectangular matte; the scenes provide a coherent setting and distinct mobile/wide framing. These are bounded design judgments about inspected outputs, not universal aesthetic scores or origin certification.

## Software and evidence checks

The offline preflight now reports source SHA-256, measured alpha coverage/range, and oriented nonzero bounds. Its optional cutout check rejects wholly opaque and wholly transparent single-frame rasters. It leaves visual inspection unperformed and does not claim to detect every painted checkerboard or bad edge.

**50 package tests passed** in the executor, including new failures for opaque checkerboards, empty alpha, uniform partial alpha, palette transparency, oriented bounds, animation coverage, unavailable decoding, CLI failure status, and source preservation. Portable generation and link/metadata checks passed. The desktop Python command resolved to an uninstalled Windows Store alias, so these Python checks were not represented as desktop execution. Browser checks ran on the actual desktop as stated above.

The [eight asset evaluation definitions](asset-briefs.json) cover a broader future matrix. They are not eight completed agent runs. Three fresh agent tasks ran; numerical cutout counterexamples ran as software tests. The extended illustration-family and unavailable-tool scenarios were not separately forward-executed in this update.

## Limits

No physical phone, screen-reader, representative-user, cross-browser-engine, field-performance, or complete accessibility-conformance claim is made. Temporal samples and stills do not establish continuously watched motion quality. The imagery is generated for fictional examples. The checks improve observed behavior and expose failure modes; they cannot guarantee every future design or generation will be excellent on its first attempt.
