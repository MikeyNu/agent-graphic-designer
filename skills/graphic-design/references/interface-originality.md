# Interface originality and repetitive AI layout checks

Use when creating or reviewing interfaces, especially when asked for modern, distinctive work or to remove AI slop. Read alongside [UI and UX design](ui-ux-design.md). This guide diagnoses the work; it cannot identify its author or guarantee originality.

## Contents

- [1. Honor the composition constraint](#1-honor-the-composition-constraint)
- [2. Diagnose the visible problem](#2-diagnose-the-visible-problem)
- [3. Derive alternatives from the product](#3-derive-alternatives-from-the-product)
- [4. Review the whole page and system](#4-review-the-whole-page-and-system)
- [5. Repair without aesthetic overcorrection](#5-repair-without-aesthetic-overcorrection)

## 1. Honor the composition constraint

For new interface compositions, apply the repository owner's explicit preference:

1. Do not put a pill, badge, or rounded announcement above the hero title.
2. Do not use the stock hero with a left column containing headline, paragraph, and CTA stack and a right column containing a detached graphic or mockup.

These are author-selected design constraints, not research findings that the shapes or alignment are inherently unusable. Treat them as disallowed defaults, not optional suggestions that a generic rationale can waive. Use them only if the user explicitly requests that composition or requires faithful preservation of an approved reference. Record that exception briefly. For a narrow maintenance edit, preserve the approved layout rather than expanding scope into an unrequested redesign.

Do not evade the second constraint by mirroring the columns, making the same split 55/45, adding a background gradient, or moving only the badge. Change the organizing relationship. Do not replace every hero with a centered headline and a screenshot beneath it either.

Keep legitimate status labels, filter chips, category controls, and necessary announcements where they help the task. Put important announcements in a distinct, appropriately placed region rather than attaching them to the hero heading. Keep readable left-aligned body copy, tables, forms, conventional navigation, familiar icons, and recognizable controls. The constraint targets a repeated hero composition, not alignment throughout the interface.

A product-detail view pairing product imagery with variant selection, specifications, and purchase controls is not automatically the rejected promotional hero. Judge its task and content relationship. This distinction does not permit relabeling a generic marketing split as a product detail to evade the constraint.

## 2. Diagnose the visible problem

Use concrete observations and consequences. A smell triggers review; it is not a probabilistic AI detector. Several co-occurring smells warrant reopening the concept, but no arbitrary count certifies quality.

| Signal | What to inspect | Correction when unjustified |
| --- | --- | --- |
| Hero assembled from stock blocks | Badge, vague claim, two CTAs, detached right-side mockup | Rebuild around the actual proposition, proof, product, or visitor task. |
| Identity can be swapped with one word | Does the same page fit a bank, dentist, developer tool, and clothing label? | Use truthful domain content and a visual mechanism connected to it. |
| Repeated section recipe | Every section is eyebrow, title, paragraph, three equal cards | Organize each section around its question: comparison, evidence, sequence, work sample, or action. |
| Card carpet | Similar boxes for unrelated content; nested panels; no clear priority | Use shared surfaces, lists, tables, or editorial structure where they express relationships. |
| Decoration carries the brand | Default glows, purple gradients, mesh, glass, sparkles, blobs, floating spheres | Run a subtraction comparison; retain only a purposeful part of the visual idea. |
| Dashboard theater | Fictional charts, duplicated metric labels, unexplained totals, decorative data glyphs, unreadable miniature UI | Reconcile definitions and scope, use meaningful encodings, and support an operational decision. Keep prototype fixtures explicit. |
| Type is loud but unspecific | Oversized vague promise, arbitrary italic word, tiny gray support copy | Establish a voice through actual wording and role-based typography; inspect delivered size. |
| Excessive whitespace or density | Empty screens require scrolling to reach the task, or all content competes | Set density for the information and user context; preserve grouping and priority. |
| Motion masks weak structure | Every object enters late, continuous float, scroll lock, cursor replacement | Keep essential content immediately available; animate meaningful change or explanation. |
| Fake credibility | Unverified reviews, counts, partner logos, scarcity, synthetic people used as customers | Remove unsupported claims and use honest evidence or no proof block. |
| Decorative functionality | Button-shaped elements do nothing; all CTAs open one generic dialog | Define distinct destinations and complete the requested behavior. |
| Cosmetic responsiveness | The same desktop scene shrinks; labels clip; hover-only actions disappear | Recompose around mobile tasks, usable targets, and content order. |
| Copy is interchangeable | Inflated promises, repeated vague verbs, redundant labels | State the actual benefit, mechanism, constraint, and next action. |
| Anti-AI costume | Random serif, acid accent, distress, giant type, or forced asymmetry | Retain only choices that belong to this product and improve the execution. |

Do not ban a library, font family, gradient, border, card, pill-shaped control, or visual period just because it is common. A real product can use familiar components well. Conversely, bespoke code can still deliver generic and unusable output.

Distinguish interchangeable branding and repetitive marketing sections from useful consistency inside a product. Reuse established navigation, form patterns, and page structures for equivalent tasks. Do not randomize each screen to demonstrate originality; predictable behavior reduces relearning.

## 3. Derive alternatives from the product

Before opening a reference feed, write the product's concrete value and a few relevant facts, materials, actions, or data relationships. Use references to expand that starting point rather than letting one admired screenshot set the entire brief.

For substantial new work, render at least three comparable roughs with the same approved content. Change the content architecture, focal point, relationship between text and image, or interaction model, not only the theme. Consider these mechanisms as prompts, never a menu to rotate through automatically:

| Mechanism | Useful when | Principal risk to test |
| --- | --- | --- |
| Start with the useful task | Search, booking, calculation, browsing, or creation is the value | Enough context and trust before asking for input; no forced account wall. |
| Let the product or work organize the page | A collection, portfolio, or physical object provides evidence | Discoverability, labels, accessible alternatives, and performance. |
| Use editorial hierarchy | The proposition depends on a story, argument, or point of view | Strong reading order and a discoverable next step. |
| Integrate type with relevant imagery | Words and imagery express one specific relationship | Legibility, actual text, cropping, and independent mobile composition. |
| Demonstrate a real transformation | A workflow or before/after explains value | Truthful states; understandable without animation or fabricated results. |
| Use a spatial or full-bleed scene | Place, material, or experience is central to the product | Readability, bandwidth, reduced motion, and a direct path to information. |
| Begin with an operational workspace | Returning users need to act | Clear priorities, state recovery, and information density. A hero may be unnecessary. |

For each rough, name the product-specific reason, the main visual relationship, the task it supports, and the likely failure. Compare mobile and desktop silhouettes at low fidelity before spending effort on polish. Choose one coherent direction, not an average of three unrelated aesthetics.

A useful identity may live in typography, content structure, image-making, rhythm, motion, data presentation, or a combination. Do not add a special flourish just to pass a distinction checklist. Small utilitarian interfaces can be excellent through precise task fit and craft.

## 4. Review the whole page and system

Use rendered output, with the known brief beside it:

1. **Silhouette check:** Reduce to content blocks or inspect at thumbnail size. Do independent concepts still have the same outline? If yes, reopen the composition.
2. **Brand-swap check:** Mentally replace the name. Identify what remains meaningfully tied to this offering. Do not require ornamental branding in every utility view.
3. **Subtraction check:** Hide an effect. Restore it only if it contributes to comprehension, hierarchy, identity, or appropriate enjoyment.
4. **Content check:** Replace short idealized copy with realistic labels, an unusually long item, missing imagery, and a meaningful empty state. Inspect what breaks.
5. **Sequence check:** Read the entire page. Each section should answer a different useful question; delete or combine repetition. Keep navigation and recurrent components consistent.
6. **Task check:** Follow the main action and its recovery route. A distinctive entrance must lead into a usable experience.
7. **Reference-distance check:** Compare against the sources. Remove recognizable borrowed identity assets or distinctive compositions that have not become an independent design.

Record important findings as: location, observed pattern, consequence, replacement, and recheck evidence. Prefer this to a numerical slop score. Classify a failure as a brief violation, usability defect, factual problem, accessibility issue, or design judgment so the remedy is clear.

## 5. Repair without aesthetic overcorrection

Correct task and content problems first, then structure, hierarchy, type, imagery, and finish. Preserve successful parts of the existing product. A fresh layout that breaks comparison or hides navigation is a regression.

If the original work is the banned split hero, build a rough that expresses a different relationship with the same content, inspect it at the target sizes, and then implement. Recoloring or swapping sides is not a repair. If the problem is a hero pill alone, remove it or relocate genuine information appropriately and rebalance spacing; do not redesign the entire site automatically.

Stop when the brief is met, the composition has a defensible purpose, critical defects are resolved, and the inspected result is strong. Novelty is not an unlimited mandate. Follow the [reference method and access limits](interface-reference-study.md); support research claims through [U1 and U2](sourcebook.md#ui-and-ux-evidence), not through claims that all AI tools always produce one layout.
