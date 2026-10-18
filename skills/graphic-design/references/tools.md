# Offline design QA tools

Use these small Python helpers when their checks are relevant to the deliverable. They measure selected properties and prepare an inspection surface. Design judgment, rendered inspection, and approval remain separate tasks.

The scripts make no network calls, install nothing, and never modify source assets. The review-board script writes only the requested HTML output. Keep the three scripts together because the review-board generator imports the preflight helpers.

Executable sources: [contrast checker](../scripts/contrast_check.py), [metadata preflight](../scripts/preflight.py), and [review-board generator](../scripts/review_board.py). These links point to the repository when this guide is included in the portable Markdown attachment.

## Contents

- [Runtime and optional dependencies](#runtime-and-optional-dependencies)
- [Read the statuses correctly](#read-the-statuses-correctly)
- [Check a solid sRGB color pair](#check-a-solid-srgb-color-pair)
- [Inspect file metadata](#inspect-file-metadata)
- [Build a review board without altering imagery](#build-a-review-board-without-altering-imagery)
- [Targeted tests](#targeted-tests)
- [Format and measurement references](#format-and-measurement-references)

## Runtime and optional dependencies

Use Python 3.10 or newer. The tools were tested with Python 3.12.

| Tool | Required packages | Optional capability |
| --- | --- | --- |
| `scripts/contrast_check.py` | Python standard library | None |
| `scripts/preflight.py` | Python standard library | Pillow for raster decoding; pypdf for PDF metadata |
| `scripts/review_board.py` | Python standard library and the adjacent `preflight.py` | Pillow for raster validation and intrinsic dimensions |

If the user wants raster or PDF metadata checks and the corresponding packages are unavailable, use an existing approved environment or install them explicitly in the project's environment:

```bash
python -m pip install Pillow pypdf
```

The scripts never run this command themselves. Missing optional packages produce `NOT RUN` results, not a successful validation. SVG inspection and contrast calculations need no third-party packages.

Commands below assume the repository root as the working directory. When the skill is installed elsewhere, replace `skills/graphic-design/` with its actual directory.

## Read the statuses correctly

| Status | Meaning |
| --- | --- |
| `PASS` | The specifically named condition passed the implemented check. |
| `FAIL` | The check detected a problem or unsupported condition that prevents its stated result. Read the message and scope. |
| `NOT RUN` | The tool did not establish the result. An input, dependency, rendering context, manual inspection, or more capable tool is needed. |
| `N/A` | The check does not apply to the supplied input. |

Preflight always records visual review as `NOT RUN`. Its overall status therefore remains `NOT RUN` unless a detected failure makes it `FAIL`. A command completing successfully does not establish that an artifact is attractive, accessible, approved, or ready for print or a client.

| Command | Exit 0 | Exit 1 | Exit 2 |
| --- | --- | --- | --- |
| Contrast | Selected threshold passed | Selected threshold failed | Invalid arguments or color input |
| Preflight | Inspection completed without a detected failure, including incomplete checks | A listed check failed | Invalid invocation or configuration |
| Review board | HTML review surface created | Not used | Invalid input or output could not be written |

Normal results and handled errors are JSON. Standard `--help` output is text.

## Check a solid sRGB color pair

```bash
python skills/graphic-design/scripts/contrast_check.py '#222222' '#FFFFFF'
python skills/graphic-design/scripts/contrast_check.py '#777777' '#FFFFFF' --target large-text-aa
python skills/graphic-design/scripts/contrast_check.py '#00000080' '#FFFFFF' --canvas '#FFFFFF'
```

Quote hex values so the shell does not treat `#` as a comment. Accepted forms are exactly `#RGB`, `#RGBA`, `#RRGGBB`, and `#RRGGBBAA`. Whitespace, named colors, CSS functions, malformed hex, and alpha-first notation are not accepted. Every input using an alpha channel, including an opaque `FF` channel, requires an explicit opaque canvas.

The background is composited over the canvas, then the foreground is composited over that effective background. Compositing uses source-over arithmetic in encoded sRGB channels. Relative luminance uses the WCAG sRGB conversion, including the `0.04045` channel threshold. The JSON includes the effective channels, full floating-point ratio, rounded display ratio, and every supported threshold assessment.

| Target | Threshold |
| --- | --- |
| `normal-text-aa` | 4.5:1 |
| `large-text-aa` | 3:1 |
| `normal-text-aaa` | 7:1 |
| `large-text-aaa` | 4.5:1 |
| `non-text-aa` | 3:1 |

The default target is `normal-text-aa`. All decisions use the unrounded ratio. For example, `#6e7978` on white produces approximately `4.4975956604:1`. It displays as `4.50:1` but fails the 4.5 threshold.

The caller must determine whether the criterion applies. WCAG has exceptions, including some logo text, incidental content, and essential graphical presentations. Large text has a specific definition, generally at least 18 pt regular or 14 pt bold, with equivalent provisions for other scripts. Assess the delivered size. The tool does not evaluate a screenshot, an entire palette, gradients, background photographs, blend modes, font rendering, or full accessibility conformance.

## Inspect file metadata

```bash
python skills/graphic-design/scripts/preflight.py assets/mark.svg
python skills/graphic-design/scripts/preflight.py assets/poster.png
python skills/graphic-design/scripts/preflight.py assets/photo.png --print-size-mm 50.8 25.4 --min-ppi 300
python skills/graphic-design/scripts/preflight.py exports/brochure.pdf
```

Inspect each requested final format. To retain evidence, redirect JSON into a separate report path or capture it through the host application's normal file workflow. Never redirect onto a source asset.

### SVG

The standard-library XML inspection checks the standalone SVG namespace, declared dimensions, absolute-unit conversion, viewBox values, aspect-ratio mapping, duplicate IDs, fragment targets, dependencies, and a limited set of active features. It reports text elements and declared font families without pretending to verify installed fonts, glyph coverage, shaping, fallback behavior, or licensing.

Absolute SVG units use 96 CSS pixels per inch. Relative or unsupported lengths remain unresolved. A mismatched viewBox and viewport can imply unused space, cropping, or non-uniform scaling. The tool reports the declared behavior as an inspection item; it cannot decide whether the design intended it. It does not calculate full path, stroke, filter, or mask bounds.

Local linked resources are checked for existence only when they remain within the asset's folder. Network URLs, absolute references, and references leaving that folder are not opened. A locally existing linked file still means the SVG is not self-contained. Embedded data URIs are limited to base64 PNG, JPEG, GIF, and WebP.

For the static review-board workflow, the limited scan rejects scripts, event handlers, foreign objects, animation elements, XML entity or DOCTYPE declarations, external stylesheet instructions, unsupported CSS dependency syntax, and external or missing dependencies. A rejection is a reason to export a supported static copy through a suitable authoring tool. The script never silently rewrites or sanitizes the source.

### Raster

With Pillow installed, supported extensions are PNG, JPEG, GIF, WebP, TIFF, and BMP. The tool verifies the container and decodes the first frame, reporting pixels, EXIF orientation, color mode, transparency, frame count, ICC-profile presence, and declared resolution. Other frames, profile accuracy, visual sharpness, compression defects, generated-image errors, and crop quality remain unverified.

An explicit print size is required to assess effective PPI. The calculation is:

```text
PPI = pixels / (printed millimeters / 25.4)
```

The calculation uses the EXIF-oriented full image without cropping or resampling. If the image and print rectangle have different aspect ratios, the tool reports conditional uncropped PPI values and leaves the assessment `NOT RUN`. Confirm the intended crop or fit in the layout application. The default minimum when a print size is supplied is 300 PPI; this is a configurable working assumption, not a universal print requirement. `--min-ppi` requires `--print-size-mm`.

A 600 by 300 pixel image at 50.8 by 25.4 mm has 300 PPI, regardless of whether its resolution metadata says 72 or 300. That calculation does not prove it contains adequate useful detail.

### PDF

With pypdf installed, the tool reads unencrypted PDFs in strict parser mode. It reports page count, declared page boxes, media dimensions including `/UserUnit`, rotation, bounded font-resource metadata, and output-intent presence. It checks up to 200 page geometries and reports that coverage. Font discovery follows page resources and nested form resources to a limited depth; embedded font-program presence is not proof of integrity, rights, complete coverage, or correct rendering.

Encrypted PDFs remain `NOT RUN`. The tool does not request a password or try decryption. It does not render pages, verify PDF/X or PDF/UA conformance, establish reading order, compare copy, check actual crop correctness, measure overprints or ink coverage, validate output profiles, or calculate embedded-image PPI from placement transforms. Use the appropriate PDF and production tools for those tasks.

### Bounded inputs

Metadata inspection is limited to 32 MiB per file. Raster decoding is limited to 50 million pixels. A limit produces an explicit unperformed check. These limits keep the helper lightweight; they are not judgments of the artifact's quality.

## Build a review board without altering imagery

For a quick comparison:

```bash
python skills/graphic-design/scripts/review_board.py assets/poster.png assets/mark.svg --title 'Launch review' --output review.html
```

For explicit labels, meaningful image descriptions, captions, and supplied annotation callouts, create a local JSON manifest:

```json
{
  "title": "Launch artwork review",
  "assets": [
    {
      "path": "assets/poster.png",
      "label": "Poster, direction A",
      "alt": "Poster showing the product above its launch date and booking details.",
      "caption": "Compare the message hierarchy and the date at the intended viewing size.",
      "annotations": [
        {"number": 1, "x": 50, "y": 18, "text": "Check the headline's separation from the photograph."},
        {"number": 2, "x": 72, "y": 83, "text": "Confirm the booking details remain readable after platform resizing."}
      ]
    }
  ]
}
```

```bash
python skills/graphic-design/scripts/review_board.py --manifest review.json --output review.html
```

Manifest paths are relative to the manifest file. Direct command-line paths are relative to the current directory. A manifest and direct asset arguments cannot be combined. Annotation positions are percentages of the complete encoded image viewport. Numbers must be unique positive integers per asset; text is supplied commentary, not an automated diagnosis. Unknown manifest keys are rejected.

The HTML embeds local PNG, JPEG, GIF, WebP, and supported SVG assets as data images. SVG is placed in an image context, never inline as active document markup. A restrictive content security policy disables scripts, network connections, external images, objects, and frames. Labels, captions, alt text, and annotation text are escaped. No JavaScript or remote resources are needed.

The fitted view shows the complete encoded viewport. When absolute dimensions are known, a separate scrollable view maps source raster pixels or declared SVG dimensions to CSS pixels. This is a screen-size inspection aid, not a calibrated physical print proof. SVGs with only a viewBox, raster metadata without Pillow, and extreme dimensions do not receive invented intrinsic-size claims.

Open the output in a browser and inspect it. The generator explicitly states that visual review has not been performed. Record an actual review outcome separately after looking at the artwork. The page's print stylesheet supports convenient review, but printing the board does not produce a production proof of the source assets.

The board accepts at most 100 assets, 32 MiB per asset, and 64 MiB combined source data. The output directory must already exist. Existing HTML output is protected unless `--overwrite` is supplied. Even with that flag, the tool refuses to replace a source asset or the manifest.

## Targeted tests

From the repository root:

```bash
python -m unittest discover -s tests -p 'test_qa_tools.py' -v
```

The tests include known contrast boundaries, alpha compositing, invalid inputs, SVG unit and dependency behavior, active SVG rejection, optional-dependency outcomes, print-PPI assumptions, PDF metadata, HTML escaping, source preservation, and output overwrite protection. Optional raster or PDF tests are skipped when their packages are unavailable. Test success validates the covered software behavior, not the quality of an artwork.

## Format and measurement references

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): relative luminance, contrast ratios, definitions, scope, and exceptions.
- [SVG 2 coordinate systems](https://www.w3.org/TR/SVG/coords.html): viewBox, absolute units, and preserveAspectRatio behavior.
- [SVG 2 conformance criteria](https://www.w3.org/TR/SVG/conform.html): SVG image processing modes and external-resource restrictions.
- [Adobe, Image size, resolution, and resampling](https://helpx.adobe.com/photoshop/desktop/crop-resize-transform/resize-adjust-resolution/image-size-resolution-and-resampling.html): the relationship between pixels, physical size, and resolution.
- [International Color Consortium FAQ](https://www.color.org/faqs/): profiles, rendering intents, and output-dependent color management.

Source behavior and requirements were checked on 18 October 2026. Recheck current destination requirements when producing new work.
