# Color and accessibility

Use this guide for palette development, emotional intent, contrast, or screen/print reproduction. The workflow and examples are design synthesis. Source links distinguish supporting studies and technical requirements from judgment.

## Contents

- Build color through relationships
- Test emotional intent
- Make information perceivable
- Manage output color
- Run useful experiments
- Avoid false certainty

## Build color through relationships

Start with the visual problem. Identify whether color must attract attention, separate categories, establish identity, reproduce a product accurately, signal an action, create atmosphere, or support prolonged reading. A single color may serve several roles, but conflicting roles need resolution.

Control hue, lightness, saturation or chroma, relative area, adjacency, edge contrast, surrounding imagery, and material. Perceptual lightness and relative luminance are related but different quantities; use the correct quantity for the task. A palette tool is a way to generate hypotheses, not an aesthetic authority.

Use color models deliberately:

| Model or medium | Useful purpose | Avoid |
| --- | --- | --- |
| sRGB | Broadly compatible screen artwork and input to the standard WCAG contrast calculation. | Assuming an RGB triplet is meaningful without a color-space context. |
| Display P3 or another wide gamut | A specifically supported delivery pipeline with richer available colors. | Losing saturation or altering appearance on unsupported destinations without checking fallback. |
| HSL/HSV | Convenient adjustment and communication of a color direction. | Treating equal numeric changes as equal perceptual changes. |
| Lab, LCH, OKLab, or OKLCH | Perceptual organization and controlled palette exploration where supported. | Ignoring gamut mapping or sending unsupported values to the output format. |
| CMYK or spot inks | A named production process and its separations. | Treating arbitrary CMYK percentages as universal brand-color equivalents. |

Choose color relationships such as analogous, complementary, triadic, split-complementary, or monochromatic only when they help. A deliberately dissonant accent can be useful. Begin with a limited set when that clarifies the problem, but do not mandate a fixed number of colors or a 60/30/10 area formula.

Assign roles in the actual composition: dominant field, supporting area, primary text, secondary information, focal accent, and functional states. Judge the amount and placement of each color. A small saturated patch can carry more visual weight than a large muted field.

Inspect colors together. The [Albers Foundation's account of Interaction of Color](https://www.albersfoundation.org/alberses/teaching/interaction-of-color) emphasizes experimental observation of color in context. Translate that into a practical requirement: evaluate a candidate on its intended background, at its intended area, beside the intended image and type. Do not select isolated swatches and assume the composition will inherit their effect.

[Schloss and Palmer's 2011 experiments](https://pubmed.ncbi.nlm.nih.gov/21264737/) separate overall preference, harmony, and preference for a foreground color against a background. These are different judgments. The experiments do not supply an optimum commercial palette or justify banning contrasting hues. Use them to avoid collapsing several design objectives into “this palette looks nice.”

## Test emotional intent

Write an explicit hypothesis: “The warm field, direct product photograph, and compact type are intended to suggest [quality] to [audience] in [setting].” Identify a plausible misreading and how to check it. Attribute the effect to the composition, not a hue alone.

Relevant research supports caution:

- [Palmer and Schloss, 2010](https://doi.org/10.1073/pnas.0906172107), propose and test an account in which color preference relates to affective associations with objects. This is not a formula predicting how a particular brand should look.
- [Wilms and Oberfeld, published online 2017](https://doi.org/10.1007/s00426-017-0880-8), examine hue, saturation, and brightness together in controlled color viewing. The study supports considering multiple dimensions; it does not establish sales effects.
- [Jonauskaite et al., 2020](https://pubmed.ncbi.nlm.nih.gov/32900287/), find broad shared patterns and differences associated with linguistic and geographic proximity across 30 nations. The task concerned color terms and emotion associations, not actual advertisements or purchase behavior.

Distinguish category convention, brand history, audience evidence, and your inference. Red in a discount sign, a ceremonial garment, a food label, and a scientific warning can function differently. Black and white can feel economical, editorial, solemn, contemporary, or ceremonial depending on type, scale, subject, and material.

Do not use gender stereotypes, national stereotypes, or universal “trust colors.” If the interpretation matters, compare real applications and seek representative feedback. Do not ask leading questions such as “Does this trustworthy blue make you feel confident?” Ask what the artifact appears to communicate before describing the intended effect.

## Make information perceivable

Apply accessibility rules to the relevant medium and content. The normative source is [WCAG 2.2](https://www.w3.org/TR/WCAG22/); its Understanding pages explain scope and methods.

| Check | Applicable requirement or practice | Boundary |
| --- | --- | --- |
| Text contrast | Under WCAG AA, ordinary text needs 4.5:1 and qualifying large text 3:1. | Use delivered size. A big font in a source image can become small when the image is displayed. |
| Large text | At least 18 pt regular or 14 pt bold, with provisions for equivalent size in other scripts. | Do not infer qualification from a large export canvas. |
| Non-text contrast | Essential graphical information and relevant interface components generally need 3:1 against adjacent colors. | Apply stated exceptions. Every decorative color boundary does not need this ratio. |
| Use of color | Add another way to identify meaningful differences. | A green/red distinction without labels is weak even if the colors look distinct to the designer. |
| Text alternatives | Supply equivalent information through supported semantic content or alternatives. | A pleasing image is not necessarily usable by a screen reader. |

For exact scope see [text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), and [use of color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html). Decorative artwork and logotypes have scoped exceptions. Corporate colors do not exempt ordinary essential copy.

Measure using the actual foreground and background under normal presentation. Account for transparency, images, gradients, and states. A calculator given opaque hex colors does not inspect a photo. Use the underlying specified colors where available, and examine variable backgrounds. Do not sample anti-aliased edge pixels as the sole definition of a text color.

Do not round 4.499 to a pass at 4.5. Inspect thin strokes and small counters even after a numeric pass. The bundled contrast tool calculates defined color-pair conditions only; it does not establish complete conformance or perceived legibility.

Use grayscale and color-vision simulations to reveal lost hierarchy or category confusion. Label them as diagnostics. They do not represent every visual condition. Evaluate required information separately from optional texture or decoration.

For dense or older-reader communications, consider larger apparent text, clear grouping, shorter essential messages, and robust contrast without assuming every older person has the same needs. Test at actual viewing size. A small phone graphic full of mandatory content may need multiple cards or another format.

## Manage output color

Keep a properly profiled master. Derive delivery copies for the actual destination. Distinguish assigning a profile, which describes how existing numbers should be interpreted, from conversion, which transforms values for another color space. Verify the result rather than relying on a menu label.

The [International Color Consortium FAQ](https://www.color.org/faqs/) explains device-dependent workflows and why some printers accept RGB and perform their own conversion. Obtain the printer's requested color space, profile, output intent, and PDF requirements. Avoid unnecessary repeated conversions. Do not invent a universal rich-black recipe or CMYK equivalent for a brand color.

Soft-proof using the relevant destination profile, rendering intent, and display conditions. [Adobe's proofing guidance](https://helpx.adobe.com/photoshop/using/proofing-colors.html) describes the importance of the monitor, profiles, lighting, and overprint behavior. A soft proof is an estimate. Fluorescent ink, metallic effects, paper texture, varnish, and physical finishes need appropriate physical review.

For ordinary screen delivery with no more specific supported workflow, sRGB is a practical compatibility choice. For print, follow the provider. State unknown production assumptions and distinguish a digital concept from artwork prepared to a confirmed specification.

## Run useful experiments

Keep the concept, copy, dimensions, and type constant while comparing the specific uncertainty.

| Uncertainty | Experiment | Decision evidence |
| --- | --- | --- |
| Accent overwhelms the message | Compare different accent areas, not only different hues. | Which version directs attention to the intended item at actual size? |
| Palette looks attractive but lacks hierarchy | Compare the same composition in color and grayscale. | Are primary and secondary elements distinguishable? |
| Text fails over a photograph | Try a different crop, text placement, opaque field, or controlled treatment. | Does every required line remain readable across its actual background? |
| Heritage palette feels theatrical | Compare its contemporary application with an authentic reference and a restrained alternative. | Does it support this brand's story without costume-like imitation? |
| Screen color may fail in print | Check the actual output profile and proof conditions. | What is clipped, shifted, or physically unrepresentable? |

Preserve the stronger artifact and document why it won. Make a second experiment only if a remaining uncertainty warrants it. Do not claim that your own preference predicts the audience's preference.

## Avoid false certainty

Reject these shortcuts: “complementary colors always look good,” “blue causes trust,” “black automatically looks premium,” “CMYK means print-ready,” “grayscale proves accessibility,” and “a contrast pass proves the whole graphic is accessible.” Each confuses a useful tool or convention with an outcome that still needs evidence.
