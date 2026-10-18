#!/usr/bin/env python3
"""Build an offline HTML review surface from local assets, without editing them."""

from __future__ import annotations

import argparse
import base64
import html
import json
import math
from pathlib import Path
from typing import Sequence

import preflight


MAX_ASSETS = 100
MAX_TOTAL_BYTES = 64 * 1024 * 1024
ASSET_KEYS = {"path", "label", "alt", "caption", "annotations"}
ANNOTATION_KEYS = {"number", "x", "y", "text"}


def text_value(value, name: str, default: str = "") -> str:
    if value is None:
        value = default
    if not isinstance(value, str) or len(value) > 20_000:
        raise ValueError(f"{name} must be a string of at most 20,000 characters.")
    return value


def validate_annotations(value) -> list[dict]:
    if not isinstance(value, list) or len(value) > 100:
        raise ValueError("annotations must be a list with at most 100 entries.")
    annotations, numbers = [], set()
    for annotation in value:
        if not isinstance(annotation, dict) or set(annotation) != ANNOTATION_KEYS:
            raise ValueError("Each annotation must contain exactly number, x, y, and text.")
        number = annotation["number"]
        if isinstance(number, bool) or not isinstance(number, int) or not 1 <= number <= 999 or number in numbers:
            raise ValueError("Annotation numbers must be unique integers between 1 and 999 within an asset.")
        numbers.add(number)
        for coordinate in ("x", "y"):
            item = annotation[coordinate]
            if isinstance(item, bool) or not isinstance(item, (int, float)) or not math.isfinite(item) or not 0 <= item <= 100:
                raise ValueError("Annotation x and y coordinates must be finite percentages from 0 to 100.")
        message = text_value(annotation["text"], "Annotation text")
        if not message.strip():
            raise ValueError("Annotation text must not be empty.")
        annotations.append({**annotation, "text": message})
    return sorted(annotations, key=lambda item: item["number"])


def raster_mime(data: bytes) -> str | None:
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "image/png"
    if data.startswith(b"\xff\xd8\xff"):
        return "image/jpeg"
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return "image/gif"
    if data.startswith(b"RIFF") and data[8:12] == b"WEBP":
        return "image/webp"
    return None


def load_asset(item: dict, base_dir: Path) -> dict:
    if not isinstance(item, dict) or "path" not in item or set(item) - ASSET_KEYS:
        raise ValueError("Each asset needs path and may contain only label, alt, caption, and annotations.")
    supplied_path = item["path"]
    if not isinstance(supplied_path, str) or not supplied_path:
        raise ValueError("Asset path must be a nonempty local path string.")
    path = (base_dir / supplied_path).resolve()
    if not path.is_file():
        raise ValueError(f"Asset is not a file: {supplied_path}")
    if path.stat().st_size > preflight.MAX_FILE_BYTES:
        raise ValueError(f"Asset exceeds the 32 MiB limit: {path.name}")
    with path.open("rb") as stream:
        data = stream.read(preflight.MAX_FILE_BYTES + 1)
    if not data or len(data) > preflight.MAX_FILE_BYTES:
        raise ValueError(f"Asset is empty or exceeds the 32 MiB limit: {path.name}")
    report = {"metadata": {}, "checks": []}
    if path.suffix.lower() == ".svg":
        preflight.inspect_svg(data, path, report)
        if not report["metadata"].get("safe_for_static_image_embedding"):
            failures = "; ".join(check["message"] for check in report["checks"] if check["status"] == "FAIL")
            raise ValueError(f"SVG is not suitable for this static review surface ({path.name}): {failures or 'inspection incomplete'}")
        mime = "image/svg+xml"
        dimensions = report["metadata"].get("dimensions", {})
        size = [dimensions.get(key, {}).get("pixels") for key in ("width", "height")]
        intrinsic = size if all(isinstance(value, (int, float)) and value > 0 for value in size) else None
        size_note = "Declared SVG viewport converted to CSS pixels at 96 px per inch."
    else:
        mime = raster_mime(data)
        if mime is None:
            raise ValueError(f"Review assets must be PNG, JPEG, GIF, WebP, or a supported standalone SVG: {path.name}")
        preflight.inspect_raster(data, report, None, 300.0)
        failures = [check["message"] for check in report["checks"] if check["status"] == "FAIL"]
        if failures:
            raise ValueError(f"Raster could not be decoded ({path.name}): {'; '.join(failures)}")
        intrinsic = report["metadata"].get("display_pixel_dimensions")
        size_note = "One CSS pixel per source pixel, with the declared EXIF orientation applied by the browser."
    label = text_value(item.get("label"), "Asset label", path.name)
    alt = text_value(item.get("alt"), "Asset alt", f"Artwork: {path.name}")
    caption = text_value(item.get("caption"), "Asset caption")
    return {
        "path": path,
        "bytes": len(data),
        "uri": f"data:{mime};base64," + base64.b64encode(data).decode("ascii"),
        "label": label,
        "alt": alt,
        "caption": caption,
        "annotations": validate_annotations(item.get("annotations", [])),
        "intrinsic": intrinsic,
        "size_note": size_note,
        "checks": report["checks"],
        "frames": report["metadata"].get("frames", 1),
    }


def render_board(assets: Sequence[dict], title: str) -> str:
    esc = html.escape
    sections = []
    for index, asset in enumerate(assets, 1):
        label, alt, caption = esc(asset["label"]), esc(asset["alt"], quote=True), esc(asset["caption"])
        markers, annotation_items = [], []
        for annotation in asset["annotations"]:
            number = annotation["number"]
            anchor = f"asset-{index}-annotation-{number}"
            message = esc(annotation["text"])
            aria = esc(f"Annotation {number}: {annotation['text']}", quote=True)
            markers.append(f'<a class="pin" href="#{anchor}" style="left:{annotation["x"]:.6g}%;top:{annotation["y"]:.6g}%" aria-label="{aria}">{number}</a>')
            annotation_items.append(f'<li id="{anchor}" value="{number}">{message}</li>')
        size = asset["intrinsic"]
        viewport_style = f' style="max-width:{size[0]:.6g}px"' if size else ""
        full = f'<div class="artwork"{viewport_style}><img class="full" src="{asset["uri"]}" alt="{alt}">{"".join(markers)}</div>'
        if size and max(size) <= 100_000:
            actual = (
                '<details class="actual"><summary>Inspect at intrinsic or declared size</summary>'
                f'<p>{size[0]:g} × {size[1]:g} CSS px. {esc(asset["size_note"])} '
                'This is not a physical print proof. Browser zoom and device density affect physical size.</p>'
                f'<div class="actual-scroll" tabindex="0" aria-label="Scrollable intrinsic-size artwork"><img src="{asset["uri"]}" alt="{alt}" style="width:{size[0]:.6g}px;height:{size[1]:.6g}px"></div></details>'
            )
        else:
            actual = '<p class="notice">Intrinsic-size view: NOT RUN. Absolute dimensions are unavailable or exceed the 100,000 CSS px display limit.</p>'
        annotations = '<ol class="annotations">' + "".join(annotation_items) + "</ol>" if annotation_items else ""
        check_items = "".join(f'<li><strong>{esc(check["status"])}: {esc(check["name"])}</strong>. {esc(check["message"])}</li>' for check in asset["checks"])
        animation = '<p class="notice">This asset has multiple frames. The metadata check decoded only its first frame.</p>' if asset["frames"] > 1 else ""
        sections.append(
            f'<section class="asset" aria-labelledby="asset-{index}"><h2 id="asset-{index}">{index:02d}. {label}</h2>'
            f'{animation}<figure>{full}<figcaption>{caption}</figcaption></figure>{annotations}{actual}'
            f'<details class="checks"><summary>Metadata checks and unverified conditions</summary><ul>{check_items}</ul></details></section>'
        )
    title = esc(text_value(title, "Title"))
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; img-src data:; style-src 'unsafe-inline'; script-src 'none'; connect-src 'none'; object-src 'none'; frame-src 'none'; base-uri 'none'; form-action 'none'">
<meta name="referrer" content="no-referrer">
<title>{title}</title>
<style>
:root{{color-scheme:light;font-family:Arial,Helvetica,sans-serif;color:#171717;background:#ecebe8}}
*{{box-sizing:border-box}} body{{margin:0}} main{{max-width:1400px;margin:auto;padding:36px 24px 72px}}
header{{max-width:900px;margin-bottom:32px}} h1{{font-size:clamp(1.8rem,4vw,3rem);line-height:1.08;margin:0 0 20px}}
h2{{font-size:1.35rem;margin:0 0 24px;overflow-wrap:anywhere}} p,li,figcaption{{line-height:1.55}}
.notice{{background:#fff4cb;border-left:4px solid #785300;padding:12px 16px}}
.asset{{background:#fff;padding:28px;margin:0 0 28px;border:1px solid #c6c5c1}}
figure{{margin:0}} .artwork{{position:relative;margin:auto;background-color:#fff;background-image:linear-gradient(45deg,#ddd 25%,transparent 25%),linear-gradient(-45deg,#ddd 25%,transparent 25%),linear-gradient(45deg,transparent 75%,#ddd 75%),linear-gradient(-45deg,transparent 75%,#ddd 75%);background-size:20px 20px;background-position:0 0,0 10px,10px -10px,-10px 0}}
img{{image-orientation:from-image}} img.full{{display:block;width:100%;height:auto}} figcaption{{margin-top:16px;white-space:pre-wrap;overflow-wrap:anywhere}}
.pin{{position:absolute;display:grid;place-items:center;min-width:28px;height:28px;padding:0 6px;border:2px solid #fff;border-radius:50%;background:#111;color:#fff;font-size:14px;font-weight:700;text-decoration:none;transform:translate(-50%,-50%);box-shadow:0 0 0 1px #111}}
.annotations{{padding-left:28px}} .annotations li{{padding:7px 0;scroll-margin-top:24px;white-space:pre-wrap;overflow-wrap:anywhere}}
details{{margin-top:20px;border-top:1px solid #ccc;padding-top:16px}} summary{{cursor:pointer;font-weight:700;line-height:1.5}}
.actual-scroll{{overflow:auto;max-height:75vh;background:#eee;border:1px solid #777}} .actual-scroll img{{display:block;max-width:none}}
:focus-visible{{outline:3px solid #1256bd;outline-offset:4px}} .checks li{{font-size:.9rem;margin:10px 0;overflow-wrap:anywhere}}
@media(max-width:600px){{main{{padding:24px 12px}}.asset{{padding:18px}}}}
@media print{{body{{background:white}}main{{max-width:none;padding:0}}.asset{{break-inside:avoid;border:0;padding:12px 0}}.actual,.checks{{display:none}}}}
</style>
</head>
<body><main>
<header><h1>{title}</h1><p class="notice"><strong>Visual review: NOT RUN by this generator.</strong> This page is a review surface. Metadata checks and supplied annotations do not establish visual quality, accessibility, print accuracy, approval, or client readiness.</p><p>The fitted artwork shows the complete encoded viewport. Checkerboard areas show transparency. Numbered annotations are supplied commentary in a separate overlay; the source images are unchanged. Inspect the intrinsic-size view and the intended delivery context before recording a review outcome.</p></header>
{"".join(sections)}
</main></body></html>
'''


def build_review_board(items: Sequence[dict], title: str = "Design review", base_dir: Path | None = None) -> tuple[str, list[Path]]:
    if not isinstance(items, (list, tuple)) or not 1 <= len(items) <= MAX_ASSETS:
        raise ValueError(f"Supply between 1 and {MAX_ASSETS} assets.")
    assets, total = [], 0
    for item in items:
        asset = load_asset(item, (base_dir or Path.cwd()).resolve())
        total += asset["bytes"]
        if total > MAX_TOTAL_BYTES:
            raise ValueError("Combined source assets exceed the 64 MiB review-board limit.")
        assets.append(asset)
    return render_board(assets, title), [asset["path"] for asset in assets]


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        print(json.dumps({"status": "FAIL", "error": message, "visual_review": "NOT RUN"}))
        raise SystemExit(2)


def main(argv: Sequence[str] | None = None) -> int:
    parser = JsonArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path, nargs="*")
    parser.add_argument("--manifest", type=Path, help="JSON title and assets with optional supplied annotations.")
    parser.add_argument("--title", help="Review-board title, overriding the manifest title.")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--overwrite", action="store_true", help="Permit replacement of an existing HTML output, never an input asset or manifest.")
    args = parser.parse_args(argv)
    if bool(args.manifest) == bool(args.files):
        parser.error("Supply either local files or --manifest, but not both.")
    try:
        if args.manifest:
            if args.manifest.stat().st_size > 1024 * 1024:
                raise ValueError("Manifest exceeds the 1 MiB limit.")
            manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
            if not isinstance(manifest, dict) or "assets" not in manifest or set(manifest) - {"title", "assets"}:
                raise ValueError("Manifest must contain assets and may contain title.")
            items, base_dir = manifest["assets"], args.manifest.resolve().parent
            title = args.title if args.title is not None else manifest.get("title", "Design review")
        else:
            items = [{"path": str(path)} for path in args.files]
            base_dir, title = Path.cwd(), args.title if args.title is not None else "Design review"
        output = args.output.resolve()
        if output.suffix.lower() != ".html":
            raise ValueError("Output must have a .html extension.")
        page, sources = build_review_board(items, title, base_dir)
        if output in sources or (args.manifest and output == args.manifest.resolve()):
            raise ValueError("Output must not replace a source asset or manifest.")
        with output.open("w" if args.overwrite else "x", encoding="utf-8") as stream:
            stream.write(page)
        print(json.dumps({"status": "PASS", "operation": "review_surface_created", "output": str(output), "assets": len(sources), "visual_review": "NOT RUN", "source_assets_modified": False}, indent=2))
        return 0
    except (OSError, ValueError, TypeError, KeyError, RuntimeError) as error:
        print(json.dumps({"status": "FAIL", "error": str(error), "visual_review": "NOT RUN"}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
