# Iconography with a coherent visual language

Use this guide when navigation, actions, status, categories, or supporting pictograms need visual symbols. These are design prescriptions. Verify the installed library's actual exports, license, and API; names and props can change.

## Choose the right class of asset

| Role | Preferred source | What to avoid |
| --- | --- | --- |
| Navigation, search, close, edit, upload, settings, status | Existing approved icon family; otherwise one suitable documented family | Emoji, text characters posing as icons, arbitrary hand-drawn paths, unrelated families mixed together. |
| Large category art, welcoming vignette, reward illustration, mascot | Cohesive generated illustration, approved artwork, or a capable illustration workflow | Shrinking a complex illustration into a tiny control; forcing rich art into simplistic custom SVG. |
| Logo, partner mark, product identity | Approved original | Substituting an approximate library glyph or generated lettering. |
| Technical symbol with precise meaning | Applicable approved symbol/standard or verified exact construction | A plausible but incorrect icon standing in for a safety or technical meaning. |

A familiar interface icon may be SVG without being custom SVG. Reuse is a quality decision. Originality belongs in the overall composition and expressive assets, not in making routine controls harder to recognize.

A text character used to imply an action still counts as iconography. Review arrows, close marks, and status glyphs even when they are typed into a span. Distinguish typographic punctuation or ornament from functional symbols. A directional cue should fit the actual destination or movement, not imply an external jump for an in-page transition. When no symbol improves the control, keep its clear text label alone.

## Build the family before placing individual icons

1. Inspect existing imports/assets and render the icons already used. Extend the current family if it fits. In a greenfield project, choose one family that suits the type, density, and tone; Lucide, Material Symbols, Carbon, or another established set are candidates, not compulsory defaults.
2. Map the action or destination to a specific symbol. Distinguish deletion from removal, navigation from submission, download from export, and information from warning. Keep the same meaning mapped consistently. If no clear symbol exists, use a label or an approved pictogram instead of inventing an ambiguous metaphor.
3. Verify each selected export/file exists. Use the installed version or official source, not a guessed package name or remembered path data. Preserve required attribution and notices when vendoring files. Do not add a second large library for one missing symbol.
4. Establish the family rules: stroke/fill treatment, apparent weight, cap/join character, viewBox, optical size, corner language, and spacing to labels. Use the family's intended size variants where available. Do not force every library onto a 24 px grid or impose one stroke width across unrelated designs.
5. Render a small specimen with actual UI labels, a selected/default state, and light/dark or colored surfaces used by the product. Compare at real delivery size. A 16 px symbol on a large screenshot can look correct while its counter closes at 1:1.

## Optical and interaction checks

- Balance apparent size. A wide arrow, circular ring, and compact filled mark can require different optical treatment while sharing a nominal box.
- Keep stroke weight, fill density, terminal treatment, and icon-to-type proportions consistent. Avoid mixing a thin outline set with heavy filled symbols unintentionally.
- Inspect baselines/centering, clipping, viewBox padding, tiny gaps, and anti-aliasing at intended sizes. Distinguish the drawing's size from its interactive target.
- Verify hover, focus, pressed, selected, disabled, loading, and error appearances when relevant. State changes need a discernible cue beyond color alone.
- Keep interactive semantics on the button or link. An icon-only button needs an accessible name describing the action; a decorative icon beside a label should not be announced twice. A tooltip is not the only accessible label.
- Follow the project's applicable contrast and target-size requirements. Library-specific recommendations are not universal WCAG thresholds. Read [interaction and validation](interaction-and-validation.md) for scope and exceptions.
- Recheck localized/RTL interfaces deliberately. Directional navigation may mirror; logos and many physical symbols should not be mirrored mechanically.

## When custom drawing is justified

Use a custom vector for a distinctive approved symbol, a missing simple member of a family, a geometric mask, or precision the existing library cannot provide. Compare it beside neighboring icons at intended size. Inspect negative space, joins, silhouette, and meaning. If it remains weak, switch to a better existing symbol plus text or a suitable art method. Do not keep adding paths to rescue an unsuccessful drawing merely because the file is editable.

For illustrated pictograms, create a style anchor and a small family using the [asset workflow](asset-creation.md). Transparent 2D artwork is often appropriate for independently placed expressive elements. Keep all outputs separate and consistent in viewpoint, palette, detail, silhouette density, and lighting. Use [asset QA](asset-quality.md) at intended display size. Generated pictograms do not replace semantic labels or exact product facts.

## Acceptance

Inspect the actual family in its screen, not only a library catalogue. Accept when symbols are recognizable in context, visibly coherent, legible at the smallest use, correctly labeled, and do not add unnecessary visual noise. Record uncertain meanings as design concerns. Do not claim human comprehension testing unless people actually participated.
