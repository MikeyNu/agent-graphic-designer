#!/usr/bin/env python3
"""Inspect local graphic-file metadata. Never certifies appearance or readiness."""

from __future__ import annotations

import argparse
import base64
import io
import json
import math
from pathlib import Path
import re
from typing import Sequence
from urllib.parse import unquote, urlsplit
import warnings
import xml.etree.ElementTree as ET


MAX_FILE_BYTES = 32 * 1024 * 1024
MAX_RASTER_PIXELS = 50_000_000
SVG_NAMESPACE = "http://www.w3.org/2000/svg"
RASTER_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".tif", ".tiff", ".bmp"}
ACTIVE_SVG_ELEMENTS = {"script", "foreignobject", "iframe", "object", "embed", "audio", "video", "animate", "animatemotion", "animatetransform", "set"}
LENGTH_RE = re.compile(r"([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)\s*(px|pt|pc|mm|cm|in|q|%)?\Z", re.I)
UNIT_TO_PX = {"": 1.0, "px": 1.0, "pt": 96 / 72, "pc": 16.0, "mm": 96 / 25.4, "cm": 96 / 2.54, "in": 96.0, "q": 96 / 101.6}
URL_RE = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.I | re.S)
SCOPE = "Local metadata and structural checks only. No visual review, font-license verification, accessibility audit, PDF/X validation, or client-readiness certification."


def add_check(result: dict, name: str, status: str, message: str) -> None:
    result["checks"].append({"name": name, "status": status, "message": message})


def finish(result: dict) -> dict:
    add_check(result, "visual_review", "NOT RUN", "Render and inspect the final artifact at delivery size and in its intended context.")
    statuses = {item["status"] for item in result["checks"]}
    result["status"] = "FAIL" if "FAIL" in statuses else "NOT RUN" if "NOT RUN" in statuses else "PASS"
    return result


def local_name(name: str) -> str:
    return name.rsplit("}", 1)[-1]


def svg_length(value: str | None) -> dict:
    if value is None:
        return {"raw": None, "status": "NOT RUN", "pixels": None, "reason": "No declared absolute length."}
    match = LENGTH_RE.fullmatch(value.strip())
    if not match:
        return {"raw": value, "status": "NOT RUN", "pixels": None, "reason": "Length needs a rendering context or uses unsupported syntax."}
    number, unit = float(match.group(1)), (match.group(2) or "").lower()
    if not math.isfinite(number) or number <= 0:
        return {"raw": value, "status": "FAIL", "pixels": None, "reason": "Length must be finite and positive."}
    if unit == "%":
        return {"raw": value, "status": "NOT RUN", "pixels": None, "reason": "Percentage length needs a containing viewport."}
    pixels = number * UNIT_TO_PX[unit]
    if not math.isfinite(pixels):
        return {"raw": value, "status": "FAIL", "pixels": None, "reason": "Converted length is not finite."}
    return {"raw": value, "status": "PASS", "pixels": pixels, "unit": unit or "px"}


def _resource(reference: str, asset_path: Path, ids: set[str]) -> dict:
    record = {"reference": reference}
    if reference.startswith("#"):
        exists = unquote(reference[1:]) in ids
        return {**record, "kind": "fragment", "status": "PASS" if exists else "FAIL", "message": "Fragment target exists." if exists else "Missing fragment target."}
    if reference.lower().startswith("data:"):
        match = re.fullmatch(r"data:image/(png|jpeg|gif|webp);base64,([A-Za-z0-9+/=\s]+)", reference, re.I)
        if match:
            try:
                decoded = base64.b64decode(re.sub(r"\s", "", match.group(2)), validate=True)
                if decoded:
                    return {"reference": "[embedded raster data]", "kind": "embedded", "status": "PASS", "message": "Raster data URI has valid base64; its visual content was not inspected."}
            except ValueError:
                pass
        return {"reference": "[unsupported or invalid data URI]", "kind": "data", "status": "FAIL", "message": "Only valid base64 PNG, JPEG, GIF, or WebP data URIs are supported."}
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc or reference.startswith(("/", "\\")):
        return {**record, "kind": "external", "status": "NOT RUN", "message": "External or absolute reference was not fetched or opened."}
    if not parsed.path:
        return {**record, "kind": "local", "status": "FAIL", "message": "Empty resource reference."}
    candidate = (asset_path.parent / unquote(parsed.path)).resolve()
    try:
        candidate.relative_to(asset_path.parent.resolve())
    except ValueError:
        return {**record, "kind": "external", "status": "NOT RUN", "message": "Reference leaves the asset folder and was not inspected."}
    exists = candidate.is_file()
    return {**record, "kind": "local", "status": "PASS" if exists else "FAIL", "message": "Local file exists; its contents were not inspected." if exists else "Local dependency is missing."}


def inspect_svg(data: bytes, path: Path, result: dict) -> None:
    metadata = result["metadata"]
    metadata["safe_for_static_image_embedding"] = False
    # Removing NUL bytes for this check also recognizes ASCII declarations in
    # UTF-16/UTF-32 XML, while the parser still receives the unmodified bytes.
    if re.search(br"<!\s*(?:DOCTYPE|ENTITY)\b|<\?xml-stylesheet\b", data.replace(b"\x00", b""), re.I):
        add_check(result, "xml_safety", "FAIL", "DOCTYPE, entity declarations, and external stylesheet processing instructions are not supported.")
        return
    try:
        root = ET.fromstring(data)
    except ET.ParseError as error:
        add_check(result, "svg_parse", "FAIL", f"Invalid XML: {error}")
        return
    if root.tag != f"{{{SVG_NAMESPACE}}}svg":
        add_check(result, "svg_root", "FAIL", "A standalone SVG must have an svg root in the SVG namespace.")
        return
    add_check(result, "svg_parse", "PASS", "Parsed a standalone SVG document without executing it.")
    dimensions = {key: svg_length(root.get(key)) for key in ("width", "height")}
    metadata["dimensions"] = dimensions
    for key, value in dimensions.items():
        add_check(result, key, value["status"], value.get("reason", "Declared absolute length converted using 96 CSS px per inch."))
    raw_viewbox = root.get("viewBox")
    viewbox = None
    if raw_viewbox is not None:
        try:
            parts = re.split(r"[\s,]+", raw_viewbox.strip())
            viewbox = [float(part) for part in parts]
            if len(viewbox) != 4 or not all(math.isfinite(value) for value in viewbox) or viewbox[2] <= 0 or viewbox[3] <= 0:
                raise ValueError
            add_check(result, "viewbox", "PASS", "viewBox contains four finite values and positive width and height.")
        except ValueError:
            viewbox = None
            add_check(result, "viewbox", "FAIL", "viewBox must contain four finite numbers with positive width and height.")
    else:
        add_check(result, "viewbox", "N/A", "No viewBox is declared; this is permitted but scaling relies on viewport dimensions.")
    metadata["viewbox"] = viewbox
    aspect = " ".join(root.get("preserveAspectRatio", "xMidYMid meet").split())
    metadata["preserve_aspect_ratio"] = aspect
    if not re.fullmatch(r"(?:none|x(?:Min|Mid|Max)Y(?:Min|Mid|Max))(?: (?:meet|slice))?", aspect):
        add_check(result, "aspect_syntax", "FAIL", "Unsupported preserveAspectRatio syntax.")
    elif viewbox and all(dimensions[key]["pixels"] is not None for key in dimensions):
        viewport_ratio = dimensions["width"]["pixels"] / dimensions["height"]["pixels"]
        box_ratio = viewbox[2] / viewbox[3]
        if math.isclose(viewport_ratio, box_ratio, rel_tol=1e-9):
            add_check(result, "aspect_mapping", "PASS", "Declared viewport and viewBox have matching aspect ratios.")
        else:
            behavior = "non-uniform scaling" if aspect.startswith("none") else "cropping at the viewport" if aspect.endswith("slice") else "unused viewport space"
            metadata["aspect_mapping_behavior"] = behavior
            add_check(result, "aspect_mapping", "NOT RUN", f"Mismatched ratios imply {behavior}; inspect whether that behavior is intentional.")
    else:
        add_check(result, "aspect_mapping", "NOT RUN", "The effective mapping requires a render or a declared absolute viewport and viewBox.")

    ids_list = [element.get("id") for element in root.iter() if element.get("id")]
    ids = set(ids_list)
    add_check(result, "unique_ids", "PASS" if len(ids) == len(ids_list) else "FAIL", "Checked for duplicate id attributes.")
    active, css_issues, references, font_families = [], [], [], set()
    has_text = False
    for element in root.iter():
        name = local_name(element.tag).lower()
        if name in ACTIVE_SVG_ELEMENTS:
            active.append(name)
        has_text = has_text or name in ("text", "tspan", "textpath")
        css_values = []
        if name == "style":
            css_values.append("".join(element.itertext()))
        for attribute, value in element.attrib.items():
            key = local_name(attribute).lower()
            if key.startswith("on"):
                active.append(key)
            if key == "base" and attribute.startswith("{http://www.w3.org/XML/1998/namespace}"):
                active.append("xml:base resource rewriting")
            if key in ("href", "src"):
                references.append(value.strip())
            if key == "font-family":
                font_families.add(value)
            if key == "style" or "url" in value.lower() or "\\" in value:
                css_values.append(value)
        for css in css_values:
            cleaned = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
            if "\\" in cleaned or re.search(r"@import\b|expression\s*\(", cleaned, re.I):
                css_issues.append("CSS escapes, imports, or expressions need independent inspection.")
            references.extend(match.group(2).strip() for match in URL_RE.finditer(cleaned))
            if len(re.findall(r"url\s*\(", cleaned, flags=re.I)) != len(list(URL_RE.finditer(cleaned))):
                css_issues.append("Unsupported CSS URL syntax.")
            font_families.update(match.strip() for match in re.findall(r"font-family\s*:\s*([^;}]+)", cleaned, re.I))
    metadata["active_features"] = sorted(set(active))
    add_check(result, "static_content", "FAIL" if active else "PASS", "Active or animated features detected: " + ", ".join(sorted(set(active))) if active else "No known active or animated features detected by this limited scan.")
    add_check(result, "css_dependencies", "FAIL" if css_issues else "PASS", " ".join(sorted(set(css_issues))) if css_issues else "No unsupported CSS dependency syntax detected.")
    dependencies = [_resource(reference, path, ids) for reference in sorted(set(references))]
    metadata["dependencies"] = dependencies
    for index, dependency in enumerate(dependencies, 1):
        add_check(result, f"dependency_{index}", dependency["status"], dependency["message"])
    portable = all(item["kind"] in ("fragment", "embedded") and item["status"] == "PASS" for item in dependencies)
    add_check(result, "self_contained", "PASS" if portable else "FAIL", "References are internal fragments or embedded raster data." if portable else "The SVG contains unresolved, external, or unembedded file dependencies; no resources were fetched.")
    metadata["font_families"] = sorted(font_families)
    metadata["contains_text_elements"] = has_text
    add_check(result, "fonts", "NOT RUN" if has_text else "N/A", "Font availability, fallback, glyph coverage, shaping, and licensing require separate verification." if has_text else "No SVG text elements detected; outlined lettering cannot be identified as text by this scan.")
    add_check(result, "artwork_bounds", "NOT RUN", "Geometric bounds, clipped content, masks, filters, and visible crop correctness need rendering.")
    metadata["safe_for_static_image_embedding"] = not any(item["status"] == "FAIL" for item in result["checks"])


def inspect_raster(data: bytes, result: dict, print_size_mm: tuple[float, float] | None, min_ppi: float) -> None:
    try:
        from PIL import Image
    except ImportError:
        add_check(result, "raster_metadata", "NOT RUN", "Pillow is not installed. No raster decoding or PPI assessment was performed.")
        return
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", Image.DecompressionBombWarning)
            with Image.open(io.BytesIO(data)) as picture:
                width, height = picture.size
                if width * height > MAX_RASTER_PIXELS:
                    add_check(result, "raster_decode", "NOT RUN", f"Image exceeds the {MAX_RASTER_PIXELS:,}-pixel inspection limit.")
                    return
                picture.verify()
            with Image.open(io.BytesIO(data)) as picture:
                picture.load()
                orientation = picture.getexif().get(274, 1)
                display_width, display_height = (height, width) if orientation in (5, 6, 7, 8) else (width, height)
                metadata = result["metadata"]
                metadata.update({
                    "format": picture.format,
                    "pixel_dimensions": [width, height],
                    "display_pixel_dimensions": [display_width, display_height],
                    "mode": picture.mode,
                    "exif_orientation": orientation,
                    "frames": getattr(picture, "n_frames", 1),
                    "has_alpha_channel_or_transparency": "A" in picture.getbands() or "transparency" in picture.info,
                    "embedded_icc_profile": bool(picture.info.get("icc_profile")),
                    "declared_dpi": list(picture.info["dpi"]) if "dpi" in picture.info else None,
                })
                add_check(result, "raster_decode", "PASS", "The first raster frame decoded successfully; appearance was not inspected.")
                add_check(result, "other_frames", "NOT RUN" if metadata["frames"] > 1 else "N/A", "Additional frames were not decoded or visually inspected." if metadata["frames"] > 1 else "Single-frame image.")
                add_check(result, "color_profile", "NOT RUN", "ICC presence is reported; profile correctness and output suitability are not validated.")
                if print_size_mm:
                    print_width, print_height = print_size_mm
                    ppi = [display_width / (print_width / 25.4), display_height / (print_height / 25.4)]
                    metadata["print_size_mm"] = list(print_size_mm)
                    metadata["uncropped_ppi_xy"] = ppi
                    metadata["minimum_ppi_requested"] = min_ppi
                    metadata["ppi_assumption"] = "Uses EXIF-oriented dimensions and the entire image, without cropping or resampling."
                    if math.isclose(display_width / display_height, print_width / print_height, rel_tol=0.001):
                        add_check(result, "effective_ppi", "PASS" if min(ppi) >= min_ppi else "FAIL", f"Unrounded PPI values were compared with the requested minimum of {min_ppi:g}; no detail-quality claim is made.")
                    else:
                        add_check(result, "effective_ppi", "NOT RUN", "Image and print rectangle have different aspect ratios. Reported uncropped PPI is conditional; actual crop or fitting must be specified.")
                else:
                    add_check(result, "effective_ppi", "N/A", "No explicit print size supplied; DPI metadata alone is not a quality test.")
                add_check(result, "crop_and_sharpness", "NOT RUN", "Crop, halos, compression defects, generated-image errors, and useful detail require visual inspection.")
    except Exception as error:
        add_check(result, "raster_decode", "FAIL", f"Raster could not be inspected: {type(error).__name__}: {error}")


def _pdf_object(value):
    return value.get_object() if hasattr(value, "get_object") else value


def _pdf_fonts(resources, fonts: list[dict], seen: set[int], depth: int = 0) -> None:
    if depth > 6 or len(seen) > 200:
        return
    resources = _pdf_object(resources)
    if not hasattr(resources, "get") or id(resources) in seen:
        return
    seen.add(id(resources))
    font_map = _pdf_object(resources.get("/Font", {}))
    for font in font_map.values():
        font = _pdf_object(font)
        subtype = str(font.get("/Subtype", ""))
        candidates = [_pdf_object(item) for item in font.get("/DescendantFonts", [])] or [font]
        embedded = []
        for candidate in candidates:
            descriptor = _pdf_object(candidate.get("/FontDescriptor", {}))
            embedded.append(any(key in descriptor for key in ("/FontFile", "/FontFile2", "/FontFile3")))
        fonts.append({"name": str(font.get("/BaseFont", "[unnamed]")), "subtype": subtype, "embedded_program_detected": bool(font.get("/CharProcs")) if subtype == "/Type3" else all(embedded)})
    for item in _pdf_object(resources.get("/XObject", {})).values():
        item = _pdf_object(item)
        if item.get("/Subtype") == "/Form":
            _pdf_fonts(item.get("/Resources", {}), fonts, seen, depth + 1)


def inspect_pdf(data: bytes, result: dict, print_size_mm: tuple[float, float] | None) -> None:
    try:
        from pypdf import PdfReader
    except ImportError:
        add_check(result, "pdf_metadata", "NOT RUN", "pypdf is not installed. PDF structure and page metadata were not inspected.")
        return
    if not data.startswith(b"%PDF-"):
        add_check(result, "pdf_parse", "FAIL", "The file does not start with a PDF header.")
        return
    try:
        reader = PdfReader(io.BytesIO(data), strict=True)
        if reader.is_encrypted:
            add_check(result, "pdf_metadata", "NOT RUN", "Encrypted PDF. No decryption or password attempt was made.")
            return
        count = len(reader.pages)
        result["metadata"]["page_count"] = count
        if count == 0:
            add_check(result, "pdf_pages", "FAIL", "PDF has no pages.")
            return
        add_check(result, "pdf_parse", "PASS", "PDF parsed in strict mode; this is not a PDF conformance validation.")
        pages, fonts, seen = [], [], set()
        page_limit = min(count, 200)
        for index in range(page_limit):
            page = reader.pages[index]
            boxes = {}
            invalid = []
            for name in ("/MediaBox", "/CropBox", "/TrimBox", "/BleedBox", "/ArtBox"):
                box = page.get(name)
                if box is None:
                    boxes[name[1:]] = None
                    continue
                values = [float(value) for value in _pdf_object(box)]
                boxes[name[1:]] = values
                if len(values) != 4 or not all(math.isfinite(value) for value in values) or values[2] <= values[0] or values[3] <= values[1]:
                    invalid.append(name)
            media = [float(value) for value in page.mediabox]
            user_unit = float(page.get("/UserUnit", 1))
            if not math.isfinite(user_unit) or user_unit <= 0:
                invalid.append("UserUnit")
                user_unit = 1
            raw_rotation = float(page.get("/Rotate", 0))
            if not math.isfinite(raw_rotation) or raw_rotation % 90:
                invalid.append("Rotate")
                rotation = 0
            else:
                rotation = int(raw_rotation)
            dimensions = [(media[2] - media[0]) * user_unit * 25.4 / 72, (media[3] - media[1]) * user_unit * 25.4 / 72]
            pages.append({"page": index + 1, "boxes_user_units": boxes, "user_unit": user_unit, "media_size_mm_before_rotation": dimensions, "rotation": rotation})
            add_check(result, f"page_{index + 1}_geometry", "FAIL" if invalid else "PASS", "Invalid geometry: " + ", ".join(invalid) if invalid else "Declared boxes have finite positive extents; visible cropping was not assessed.")
            _pdf_fonts(page.get("/Resources", {}), fonts, seen)
        result["metadata"]["pages"] = pages
        result["metadata"]["pages_inspected"] = page_limit
        result["metadata"]["fonts"] = fonts
        add_check(result, "page_coverage", "PASS" if count <= 200 else "NOT RUN", "All page geometries were inspected." if count <= 200 else "Only the first 200 page geometries were inspected.")
        font_state = "N/A" if not fonts else "PASS" if all(font["embedded_program_detected"] for font in fonts) else "NOT RUN"
        add_check(result, "font_embedding", font_state, "Reports embedded-program presence in page and bounded nested-form resources, not font integrity, glyph correctness, licensing, or all possible font usages.")
        catalog = _pdf_object(reader.trailer["/Root"])
        intents = []
        for value in catalog.get("/OutputIntents", []):
            intent = _pdf_object(value)
            intents.append({"identifier": str(intent.get("/OutputConditionIdentifier", "")), "profile_present": "/DestOutputProfile" in intent})
        result["metadata"]["output_intents"] = intents
        add_check(result, "print_conformance", "NOT RUN", "PDF/X or PDF/UA, actual output-intent suitability, bleed requirements, overprints, ink coverage, and embedded-image effective PPI require dedicated checks.")
        if print_size_mm:
            add_check(result, "requested_print_size", "NOT RUN", "PDF page sizes are reported separately. Image placement transforms and crop-dependent PPI were not calculated.")
    except Exception as error:
        add_check(result, "pdf_parse", "FAIL", f"PDF could not be inspected: {type(error).__name__}: {error}")


def inspect_file(path: str | Path, print_size_mm: tuple[float, float] | None = None, min_ppi: float = 300.0) -> dict:
    if print_size_mm is not None and (len(print_size_mm) != 2 or any(not math.isfinite(value) or value <= 0 for value in print_size_mm)):
        raise ValueError("Print width and height must be finite positive millimeters.")
    if not math.isfinite(min_ppi) or min_ppi <= 0:
        raise ValueError("Minimum PPI must be finite and positive.")
    path = Path(path)
    result = {"file": str(path), "kind": "unknown", "metadata": {}, "checks": [], "scope": SCOPE}
    try:
        path = path.resolve()
        result["file"] = str(path)
        if not path.is_file():
            raise ValueError("Path is not a regular file.")
        if path.stat().st_size > MAX_FILE_BYTES:
            add_check(result, "file_size", "NOT RUN", f"File exceeds the {MAX_FILE_BYTES // (1024 * 1024)} MiB inspection limit.")
            return finish(result)
        with path.open("rb") as stream:
            data = stream.read(MAX_FILE_BYTES + 1)
        if len(data) > MAX_FILE_BYTES:
            add_check(result, "file_size", "NOT RUN", "File grew beyond the inspection limit while reading.")
            return finish(result)
        if not data:
            raise ValueError("File is empty.")
        result["metadata"]["file_bytes"] = len(data)
        add_check(result, "file_read", "PASS", "Read the supplied local file without changing it.")
    except (OSError, ValueError, RuntimeError) as error:
        add_check(result, "file_read", "FAIL", str(error))
        return finish(result)
    suffix = path.suffix.lower()
    if suffix == ".svg":
        result["kind"] = "svg"
        try:
            inspect_svg(data, path, result)
        except (OSError, ValueError, RuntimeError) as error:
            add_check(result, "svg_metadata", "FAIL", f"SVG metadata could not be inspected: {error}")
        if print_size_mm:
            add_check(result, "effective_ppi", "NOT RUN", "SVG may contain raster imagery. Raster placement PPI and print fitting were not calculated.")
    elif suffix in RASTER_SUFFIXES:
        result["kind"] = "raster"
        inspect_raster(data, result, print_size_mm, min_ppi)
    elif suffix == ".pdf":
        result["kind"] = "pdf"
        inspect_pdf(data, result, print_size_mm)
    else:
        add_check(result, "format_support", "NOT RUN", "Supported extensions: SVG, PNG, JPEG, GIF, WebP, TIFF, BMP, and PDF.")
    return finish(result)


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        print(json.dumps({"status": "FAIL", "error": message, "scope": SCOPE}))
        raise SystemExit(2)


def main(argv: Sequence[str] | None = None) -> int:
    parser = JsonArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--print-size-mm", type=float, nargs=2, metavar=("WIDTH", "HEIGHT"))
    parser.add_argument("--min-ppi", type=float, help="Required PPI for an explicit print size. Default with a print size: 300.")
    args = parser.parse_args(argv)
    if args.min_ppi is not None and args.print_size_mm is None:
        parser.error("--min-ppi requires --print-size-mm.")
    try:
        result = inspect_file(args.file, tuple(args.print_size_mm) if args.print_size_mm else None, args.min_ppi if args.min_ppi is not None else 300.0)
        print(json.dumps(result, indent=2, allow_nan=False))
    except (ValueError, OSError) as error:
        print(json.dumps({"status": "FAIL", "error": str(error), "scope": SCOPE}))
        return 2
    return 1 if result["status"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
