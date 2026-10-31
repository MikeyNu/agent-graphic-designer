# QA and execution review, 31 October 2026

**Follow-up:** the user authorized the local desktop browser and confirmed that GitHub CI is unavailable due to billing. The [desktop browser record](validation-2026-10-31-desktop.md) supersedes the runtime NOT RUN and unconfirmed CI-cause statements below for its explicitly tested conditions. The earlier record remains intact as evidence of what was known then.

This review improves execution reliability without claiming that an agent will produce correct results on every future task. It covers Graphic Design and coordinated Web Motion Director. Source review, rendered artwork, isolated logic, browser behavior, and human response are separate kinds of evidence.

## Audit scope and changes

Reviewed the core workflow, all reference guides, owner studies, templates, tools, evaluation definitions, portable builder, package documentation, and automated checks. Historical source observations retain their original dates and access limits; the review did not repeat the original image/video research or re-open every external citation. A targeted primary-documentation refresh covers page lifecycle, browser-tool limits, and selected motion sources.

| Issue | Change | Verification |
| --- | --- | --- |
| A general workflow could over-expand a maintenance edit or written handoff. | Added explicit routes for repairs, reconstruction, substantial new work, and specification; current scope and approved identity take priority. | Exact artwork repair, scoped mobile handoff, and motion repair exercises. |
| Multiple linked guides could duplicate discovery or be read recursively regardless of need. | One shared brief and exploration; directly relevant guides loaded at decision points. | Core/reference consistency review. The route is guidance, not a measured context-efficiency claim. |
| “Tested” could obscure which artifact and behavior were observed. | Added an evidence matrix and artifact/condition/method/result record; stage is separate from PASS/FAIL/NOT RUN/N/A. | Exercise reports explicitly distinguish static, isolated, and runtime evidence. |
| CSS keyframes/declarations were not counted as active SVG content for static review-board embedding. | Preflight conservatively detects CSS animation; static review surfaces reject it without modifying the input. | Regression tests cover normal/prefixed/longhand declarations, review-board rejection, and inert comments. This is bounded detection, not a comprehensive SVG security or animation parser. |
| A canceled closing effect could leave a retained view unusable. | Added leave/return, transient-guard, overlay, and body-lock settlement guidance. | Queue source defect corrected; seven isolated lifecycle checks. Actual browser cache restoration NOT RUN. |
| Documentation drift. | Corrected the UI/UX definition count and the workspace study's obsolete reference to a future clip study. | Local links, package checks, and portable build. |

The companion's [QA record](https://github.com/MikeyNu/Web-Motion-Director/blob/main/VALIDATION-2026-10-31-QA.md) covers the hardened motion scanner, tag/plan validation, browser sampler, package checks, and v1.2.2 release.

## Fresh-context exercise method

Five agents received realistic briefs, required original fixtures, applicable skills, and available-capability constraints without evaluator expectations or the parent's diagnosis. They were instructed not to read evaluation definitions, prior outputs, or validation records. The retained [brief definitions](qa-briefs.json) are reproducible task summaries and evaluator criteria, not full transcripts. The parent inspected actual artifacts or source, read the handoffs, and reran included logic checks. This is internal AI-assisted evaluation, not independent human research.

The first four exercises overlapped the audit and instruction revisions; they are diagnostic evidence, not five clean after-change trials. The motion-repair exercise began after the new core routing and evidence rules. Later documentation refinements consolidate the observed lessons. No repeated-run success rate or controlled before/after comparison was measured.

| Case | Actual output and inspection | Result and limit |
| --- | --- | --- |
| Original Night Garden poster | Three original SVG concepts were rendered and compared; editable SVG, outlined SVG, and 1080 by 1350 PNG delivered. The author inspected full size, phone-size diagnostic, detail, grayscale, and outlined render. Parent independently viewed final PNG and concept comparison. | Required copy, dimensions, font/glyph availability, bounds, and solid-background essential-text contrast checked. A subtitle overlap in study B, a leaf/bloom intersection, a detached stem, and small footer text were corrected and re-rendered. No audience study, platform upload, actual-device test, or print proof. |
| Approved workshop time repair | Actual SVG changed from 18:00 to 18:30; PNG rendered and viewed. Parent inspected the PNG and checked that replacing only this string reproduces the output exactly. | Approved badge, split composition, palette, layout, and other copy preserved. Input unchanged. No unnecessary concepts or redesign. |
| Lantern equipment queue | Self-contained HTML with eight labeled sample reservations, search/filter/sort, details, simulated collection outcomes, retry, history, and contextual return. Three static composition studies rendered. Parent reviewed source and reran checks. | 14 state/syntax, seven isolated lifecycle, and 21 source/color checks pass. Parent found a page-suspension defect after initial state checks passed; it was corrected. Browser layout, native interaction, accessibility, history, actual BFCache, and temporal playback remain NOT RUN. |
| Mobile inspection handoff | Written screen/state, local draft, photo permission, conflict, submission, acknowledgement, and motion contracts. Parent read the complete handoff. | Appropriate written specification with approved blue cards/gradient/tabs retained. Reconnection does not submit; draft and confirmed result remain distinct. No application, storage, backend, device, or playback execution claimed. |
| Approved Juniper motion repair | Corrected self-contained HTML preserves approved appearance; actual controller exercised by a fake-DOM/timer/animation harness. Parent inspected controller and reran the script. | 15 source/isolated checks pass, including 1,000 toggles, stale callbacks, preference changes, focus-call conditions, missing finish, and failed animation. Browser appearance, native focus, assistive technology, and playback remain NOT RUN. |

Retained [curated fixtures and outputs](examples/qa-2026-10-31/README.md) include exact-version hashes. They are regression material, not preferred layouts. Raw external reference images and clips are not redistributed.

## The lifecycle defect

In the first queue controller, `pagehide` canceled both the closing animation and fallback timer while leaving `routeClosing` true. A subsequent persisted `pageshow` could restore the page without settling the dialog; the return guard could continue rejecting Back/Escape. Ordinary state-model checks did not cover this DOM lifecycle.

The repair retains the pending close context, settles the dialog and guards on suspension, and defers queue focus/scroll restoration until return. It preserves an open, non-closing detail and does not replay collection. The seven new checks execute the actual helper functions against explicit stubs and cover both normal and interrupted close. The parent supplied the lifecycle scenario only after reviewing the completed initial source. This is a diagnosed failure and correction, not an unaided first-pass success or actual BFCache verification.

## Reproducible checks

Run from repository root:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/build_portable_skill.py --output /tmp/GRAPHIC_DESIGN_SKILL.md
node evals/examples/qa-2026-10-31/queue/check-state.cjs
node evals/examples/qa-2026-10-31/queue/check-lifecycle.cjs
python3 evals/examples/qa-2026-10-31/queue/check-source.py
```

The repository suite passes **45 tests**, including two added SVG-animation regressions. The portable document builds with internal links resolved. The skill-creator package validator passes. The companion passes 27 package/helper tests, making **72 repository tests across both packages**; the exercise checks are reported separately and must not be counted as browser tests. MIT notices are unchanged. Both core files remain below 500 lines. Git diff whitespace checks pass. These are local results; configured CI is not a claim that a hosted run completed.

### Post-publication CI observation

The published trees were verified against the locally tested trees. GitHub's [Graphic Design run](https://github.com/MikeyNu/agent-graphic-designer/actions/runs/41146228634) and [Motion Director run](https://github.com/MikeyNu/Web-Motion-Director/actions/runs/41146233823) both report failure before any test steps, with no assigned runner and no downloadable job log. The connector could not retrieve check annotations, so the cause is unconfirmed. The prior Graphic Design main revision also has a [failed hosted run](https://github.com/MikeyNu/agent-graphic-designer/actions/runs/41140249615). Do not describe hosted CI as passing or invent a billing, permission, or workflow diagnosis. The 72 executed local tests remain the available automated execution evidence; hosted execution needs investigation through GitHub's run details.

## Capability boundary and remaining checks

The permitted browser rejected the local `file://` preview with “protocol not allowed (only http/https are supported)” and expressly prohibited alternate routes. No browser workaround followed. A queue agent's earlier local renderer probe had already failed before loading the page because its browser executable was absent. Static SVG rendering through Inkscape and isolated Node/Python checks remained available.

Accordingly, the new HTML examples are implemented review prototypes with bounded source/logic evidence. Browser layout, native keyboard/focus/dialog behavior, normal-speed motion, interrupted playback, on-device behavior, accessibility conformance, and measured performance are NOT RUN. Perform those checks in an authorized runtime before treating either as production-ready. The package's optional browser sampler was tested against fake objects only in this review. It does not certify temporal quality.

The review strengthens scope interpretation, error reporting, recovery, and evidence discipline. It provides five concrete transfer exercises and reproducible regressions; it does not establish universal taste, every-device compatibility, statistical reliability, or client approval.
