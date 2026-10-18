# Typography and perception

Treat typography as the voice and structure of the actual message. Select, render, compare, and inspect it. Do not substitute a memorized font pairing or personality label for that work. Coordinate type with [composition and layout](composition-and-layout.md).

## Contents

- [Ground decisions in evidence](#ground-decisions-in-evidence)
- [Inspect anatomy and behavior](#inspect-anatomy-and-behavior)
- [Use emotional associations as hypotheses](#use-emotional-associations-as-hypotheses)
- [Build useful specimens](#build-useful-specimens)
- [Control font technology](#control-font-technology)
- [Respect language and script](#respect-language-and-script)
- [Check readability and accessibility](#check-readability-and-accessibility)
- [Work through contrasting applications](#work-through-contrasting-applications)
- [Finish with a typographic review](#finish-with-a-typographic-review)

## Ground decisions in evidence

Separate three kinds of statement:

- **Empirical finding:** a reported result for particular participants, stimuli, and conditions.
- **Technical requirement:** behavior specified by a standard or the terms of an actual license.
- **Design hypothesis:** an interpretation or working choice to test in this project.

Research supports perceived typeface personality and interactions with emotional content. It does not provide a universal font-to-emotion dictionary. [Hazlett and colleagues' two studies](https://www.microsoft.com/en-us/research/publication/two-studies-on-how-a-typeface-congruent-with-content-can-enhance-onscreen-communication/) concern specific experimental tasks. An [Arabic study](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.01229/full) found different personality ratings for eleven typefaces among 28 fluent female readers aged 18–28. Do not generalize those samples into claims about every culture or customer.

Reject a universally most readable font. [Wallace and colleagues](https://research.adobe.com/publication/towards-individuated-reading-experiences-different-fonts-increase-reading-speed-for-different-individuals/) found considerable variation across individuals after normalizing font size by human perception. Their fastest-versus-slowest comparison does not promise an equivalent improvement from a new font in this project. Treat preference, emotional fit, reading speed, and comprehension as different evaluation questions.

Before choosing families, establish the audience, language, exact copy, reading duration, viewing distance, medium, required text roles, brand assets, and licensing constraints. Translate vague requests into observable intentions: “welcoming without looking juvenile,” for example. Keep assumptions explicit and proceed with reversible exploration when details are missing.

## Inspect anatomy and behavior

Use this table to direct inspection. The suggested consequences are hypotheses to verify in the rendered work.

| Feature | Inspect | Decision it informs |
| --- | --- | --- |
| Stroke contrast | Relationship between thick and thin strokes | Whether detail survives reduction, printing, or a textured background |
| X-height and capitals | Apparent lowercase size relative to capitals | Body density, mixed-case rhythm, companion-font alignment |
| Counters and apertures | Interior spaces and openings | Whether small characters close up or become ambiguous |
| Width and proportion | Condensed, normal, extended; broad and narrow glyphs | Headline fit, pace, identity, economy of space |
| Terminals and serifs | Shapes at stroke endings | Tone, texture, and coherence with image or illustration |
| Curvature and construction | Geometric, calligraphic, angular, irregular | A formal vocabulary for a concept, without assigning universal emotions |
| Spacing and kerning | Word rhythm and troublesome pairs | Awkward gaps, collisions, misleading word groupings |
| Ascenders and descenders | Extents above and below the main letter body | Line spacing, clipping, diacritic clearance |
| Numerals and symbols | Currency, fractions, punctuation, figure styles | Accurate prices, tables, dates, and technical content |
| Family range | Actual weights, italics, widths, optical sizes | A coherent system that survives different applications |

Inspect actual shapes rather than relying on the serif/sans category. Compare confusing characters such as `I l 1`, `O 0`, and `rn m` when relevant. Do not distort a font horizontally to solve a line-length problem unless that distortion is an intentional display treatment that survives review. Prefer a suitable designed width or a better composition.

## Use emotional associations as hypotheses

Use the following culturally situated associations to develop candidates. They are design heuristics, not guaranteed psychological effects. Weight, spacing, scale, copy, imagery, and audience familiarity can change or reverse them.

| Route | Association to investigate | Risk to inspect |
| --- | --- | --- |
| Old-style or humanist serif | Literary, considered, established, humane | Unwanted historical tone or fragile small detail |
| Transitional serif | Editorial, formal, institutional | Accidental newspaper, school, or legal-document character |
| High-contrast serif / Didone | Fashion editorial, ceremony, precision | Disappearing hairlines or interchangeable luxury branding |
| Humanist sans | Practical, open, conversational | Familiarity without a distinctive concept |
| Grotesque / neo-grotesque | Direct, systematic, understated | Sterility or weak character differentiation |
| Geometric sans | Constructed, orderly, optimistic, technological | An unintended toy-like or impersonal effect |
| Slab serif | Solid, assertive, utilitarian, craft-related | Accidental sports, Western, or industrial costume |
| Monospaced | Technical, archival, procedural | Decorative pseudo-technical signals and inefficient long-copy rhythm |
| Script / calligraphic | Personal, expressive, ceremonial | Generic wedding shorthand or poor small-size recognition |
| Vernacular or specific display | A particular place, era, subculture, or performance | Misreading, parody, cultural misuse, or illegibility |

For each serious candidate, complete: “This treatment should suggest **quality** to **audience**, because of **visible feature or relevant reference**. Its likely misreading is **risk**, which I will check through **comparison or review**.”

Do not equate new fonts with modern design, old fonts with obsolete work, or popular fonts with poor quality. A familiar face can be excellent in a specific composition. Research the present context before making a claim about current overuse. Avoid gender-essentialist font rules and novelty added solely to escape familiarity.

## Build useful specimens

1. **Use the real content.** Set the organization name, longest heading, supporting paragraph, smallest caption, call to action, numbers, punctuation, and language-specific text. Use a pangram only as an additional diagnostic.
2. **Compare relevant alternatives.** For a consequential original direction, render candidates that differ in voice or structural treatment. For a correction within an established identity, preserve the system and investigate the defect.
3. **Control the comparison.** Keep copy and layout conditions consistent when testing type alone. Compare perceived size as well as nominal point size. Then test the strongest candidate in its intended composition.
4. **Test the limiting conditions.** Inspect the smallest delivered size, the longest plausible text, a representative paragraph, the actual background, and realistic export compression or printing where available.
5. **Separate judgments.** Record character recognition, comfortable reading, intended tone, distinctive character, and compatibility with the rest of the design independently.
6. **Tune the setting.** Adjust line length, leading, width, weight, kerning, tracking where appropriate, line breaks, and optical alignment. Preserve the meaning of phrases when breaking headlines.

Create a compact specimen sheet with actual role labels and sizes, not an impressive alphabet poster. Include applicable stress strings such as `Il1 O0 rn m`, `0123456789`, `R1,299.50`, `% & @`, and the project's own names and diacritics. Use the audience's number conventions. Show promising pairings in paragraphs and headings, not just two font names beside one another.

Choose companions by useful relationships: contrasting voice, compatible apparent size, complementary rhythm, or a shared family system. Do not impose a fixed maximum of two families on every artifact. Add another only when it performs a role the existing system cannot perform clearly.

## Control font technology

Verify the installed or available font, its source, version where obtainable, supported glyphs, actual styles, and export behavior. A family name in CSS or a design file does not prove that the requested font rendered. Inspect a rendered specimen and check the active font when the tool exposes that information.

For variable fonts, inspect the axes the file actually supplies. Standard axes include weight `wght`, width `wdth`, slant `slnt`, italic `ital`, and optical size `opsz`; do not assume all are present. Optical sizing varies the design for different text sizes. Verify automatic or explicit settings in the target renderer using the [OpenType optical-size specification](https://learn.microsoft.com/en-us/typography/opentype/spec/dvaraxistag_opsz). Retest line breaks when weight or width changes. Avoid animation of type merely because an axis can move.

Distinguish numeral **width** from numeral **form**. Tabular/proportional and lining/oldstyle are separate choices; tabular oldstyle figures are possible. Use the [OpenType figure-width definitions](https://learn.microsoft.com/en-us/typography/opentype/spec/features_pt) and [lining/oldstyle definitions](https://learn.microsoft.com/en-us/typography/opentype/spec/features_ko). Use tabular numerals where column comparison benefits, and align decimals deliberately. Do not make the entire document monospaced just to align a few values.

Use real small capitals, italics, and other designed features when appropriate. Inspect synthetic bold, simulated italics, and scaled capitals rather than assuming they reproduce designed styles. Preserve necessary shaping features.

Check licensing for the intended output and editable handoff. [Adobe Fonts' licensing FAQ](https://helpx.adobe.com/fonts/web/font-licensing/font-licensing.html) distinguishes finished artwork, client editing, application embedding, and font-file transfer. Those terms do not cover every locally installed font. Retain the relevant license record; distribute font files only when permitted. Do not purchase or accept new obligations without applicable authorization.

## Respect language and script

Test real language, not Latin placeholders. [W3C's international typography guidance](https://www.w3.org/International/articles/typography/justification) explains that spacing and justification depend on writing system, language, and calligraphic style. Use language-aware shaping and line breaking rather than importing Latin conventions everywhere.

Check:

- Required accented letters, combining marks, numerals, currency, and punctuation; distinguish genuine coverage from silent fallback.
- Arabic connections and marks, Indic conjuncts, or other shaping required by the actual script; do not manually separate characters to imitate tracking.
- Right-to-left text mixed with numbers, Latin names, addresses, or punctuation.
- CJK line starts and endings, punctuation spacing, and mixed-script proportions.
- Cropped diacritics, overlapping marks, mismatched baselines, and line-height failures.
- Expansion caused by translation or longer names across every required format.

Obtain a fluent-reader review when available. If unavailable, report that limitation instead of claiming linguistic validation. Preserve logical text order and searchable copy. Do not insert spacing characters into source text to conceal a rendering problem.

## Check readability and accessibility

Distinguish character recognition, sustained reading, and accessibility. [Google Fonts' accessibility guidance](https://fuchsia.googlesource.com/third_party/github.com/google/fonts/%2B/905b0f31b9830271fff1b0ffa84c305e5c17658a/cc-by-sa/knowledge/modules/readability_and_accessibility/lessons/introducing_accessibility_in_typography/content.md) rejects a single universally accessible font and discusses character differentiation, spacing, and semantic access. Evaluate the actual audience and medium instead of enforcing one minimum size across posters, phones, books, and packaging.

For applicable web content, verify [WCAG 2.2](https://www.w3.org/TR/WCAG22/) requirements: ordinary text contrast of at least 4.5:1, qualifying large text at least 3:1, specified exceptions, and relevant resize and images-of-text criteria. Treat contrast as one check. [W3C notes](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) that thin fonts may appear fainter after rendering despite nominally passing contrast.

Apply [text-spacing guidance](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html) accurately. The required tolerance for specified user overrides is not a mandatory authored style: line height 1.5 times font size; paragraph spacing 2 times; letter spacing 0.12 times; word spacing 0.16 times. Respect script exceptions and medium applicability. Do not certify a PDF or print design from an HTML spacing test.

## Work through contrasting applications

**Community event poster:** Explore a clear, welcoming headline with a highly readable details block. Judge date, venue, price, and contact information at expected viewing distance. An expressive title can work if it does not obscure what the event is. Reject a ceremonial script merely chosen because the organization is traditional. Treat audience response as untested until reviewed.

**Experimental music sleeve:** Explore compressed type, unusual scale, or historically informed lettering when connected to the music's concept. Allow deliberate tension in the title while retaining required credits and distribution information. Test the physical sleeve and tiny streaming thumbnail separately. Do not reuse poster readability priorities without considering the artwork's role.

These examples demonstrate different judgments, not fixed style recipes. A conventional font can be the stronger choice in either case.

## Finish with a typographic review

Read all required copy against its approved source. Inspect spelling, meaningful line breaks, spacing pairs, widows, stranded headings, captions, and numerical consistency. Reopen final exports and compare font appearance, glyph coverage, and line breaks with the working master.

For image-generated text, use OCR as an aid and visually inspect every required word; OCR cannot establish sound kerning or letter construction. Prefer controllable typesetting for precise final copy. Preserve a live-text master when practical and provide an accessible alternative where the delivery medium calls for one.

Record: **role; intended effect; selected family/style; relevant settings; source/license; observed defect; correction; recheck; remaining uncertainty**. Never claim audience testing, complete accessibility, or export verification that did not occur.
