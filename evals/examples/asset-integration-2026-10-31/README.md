# Proactive asset and iconography examples

Three fresh-context tasks exercised the revised skill. The two creation briefs asked for interfaces without requesting image generation. Both agents identified a visual opportunity, generated actual imagery, and integrated it. The focused icon repair used an existing family and preserved the approved interface.

| Case | Implementation | Selected views | Asset record |
| --- | --- | --- | --- |
| Fieldnote, family nature journal | [HTML](fieldnote/index.html), CSS, and JavaScript with local drafts, saving, and a sample dialog | [Desktop](fieldnote/desktop.png), [phone](fieldnote/phone.png), [cutout inspection](fieldnote/evidence/asset-inspection.png) | [Transparent illustration and prompt](fieldnote/ASSET-RECORD.md) |
| Tidemark, fictional coastal journal | [HTML](tidemark/index.html), CSS, and JavaScript with responsive scenes and a chapter transition | [Desktop](tidemark/desktop.png), [phone](tidemark/phone.png) | [Opaque scene prompts](tidemark/ASSET-PROMPTS.md) |
| Lantern, reservation queue icon repair | [Self-contained HTML](icons/index.html) preserving the prior queue's layout and state model | [Desktop](icons/desktop.png), [narrow retry state](icons/phone-retry.png) | [Pinned Lucide sources](icons/vendor/lucide/source.json), [license](icons/vendor/lucide/LICENSE) |

These are fictional local prototypes. There is no backend, account system, real reservation service, or real travel destination. The journal imagery was generated for these examples. Operational icon geometry comes from Lucide at the pinned revision, with the upstream ISC and Feather MIT notices retained.

## Inspect locally

Keep each case's files together. Serve this directory with an available local static server, then open `fieldnote/`, `tidemark/`, or `icons/` in a desktop browser. For example, where Python is installed:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Direct file opening was also exercised, including a Fieldnote save/reload check in the tested Edge version. File-origin storage behavior can differ across browsers; use a local server for a stable origin. GitHub's HTML source viewer is not an interactive preview.

## Executed QA

Browser checks ran in headed Microsoft Edge 156.0.4314.50 on the authorized local Windows desktop. Fieldnote passed 24 main checks plus focused captures and direct-file saving. Tidemark passed 29 main checks and three checks after its final punctuation correction. Lantern passed 14 main checks and six final focused checks. Source and destination hashes were compared before accepting the desktop copies.

The [evidence summary](evidence-summary.json) retains check names, statuses, report hashes, runtime asset measurements, and hashes of the curated files. Full reports and additional views remain in the corresponding `Skill-Asset-QA-Fieldnote`, `Skill-Asset-QA-Tidemark`, and `Skill-Asset-QA-Icons` desktop folders. The summary is an extract of executed evidence, not a runnable browser harness.

The [validation record](../../validation-2026-10-31-assets.md) explains initial defects, repairs, harness corrections, and limits. These outcomes do not establish universal aesthetic quality, full accessibility conformance, or performance on physical phones. The Tidemark zoom check used CSS zoom, not native browser zoom. GitHub CI was not used.

Original generated PNG masters remain with the complete task evidence. This compact repository copy includes the actual WebP files used by each page. Cutout alpha statistics establish transparent pixels, not correct segmentation by themselves; the retained matte board and integrated views show the separate visual inspection.
