"""Behavioral tests for the optional, offline design QA tools."""

from __future__ import annotations

import base64
from contextlib import redirect_stdout
import hashlib
from html.parser import HTMLParser
import importlib.util
import io
import json
import math
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "skills" / "graphic-design" / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))
import contrast_check
import preflight
import review_board

HAS_PILLOW = importlib.util.find_spec("PIL") is not None
HAS_PYPDF = importlib.util.find_spec("pypdf") is not None
PIXEL_PNG = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+a2ioAAAAASUVORK5CYII=")


def checks_by_name(report: dict) -> dict:
    return {check["name"]: check for check in report["checks"]}


class ContrastTests(unittest.TestCase):
    def test_black_white_and_equal_colors(self):
        self.assertEqual(contrast_check.check_contrast("#000", "#fff")["ratio"], 21.0)
        self.assertEqual(contrast_check.check_contrast("#aBcDeF", "#abcdef")["ratio"], 1.0)

    def test_actual_near_boundary_is_not_rounded_into_a_pass(self):
        result = contrast_check.check_contrast("#6e7978", "#ffffff")
        self.assertAlmostEqual(result["ratio"], 4.4975956603938485)
        self.assertEqual(result["ratio_display"], "4.50:1")
        self.assertEqual(result["status"], "FAIL")
        self.assertTrue(contrast_check.meets_threshold(4.5, 4.5))
        self.assertFalse(contrast_check.meets_threshold(math.nextafter(4.5, 0.0), 4.5))

    def test_known_gray_pairs(self):
        self.assertEqual(contrast_check.check_contrast("#777", "#fff")["status"], "FAIL")
        self.assertEqual(contrast_check.check_contrast("#767676", "#fff")["status"], "PASS")
        self.assertEqual(contrast_check.check_contrast("#777", "#fff", target="large-text-aa")["status"], "PASS")

    def test_strict_hex_validation(self):
        for value in ("fff", "#12", "#12345", "#1234567", "#123456789", "#ggg", " #fff", "#fff\n", "#１２３", None, 123):
            with self.subTest(value=value), self.assertRaises(ValueError):
                contrast_check.parse_hex(value)

    def test_alpha_requires_explicit_opaque_canvas(self):
        for foreground, background in (("#0008", "#fff"), ("#000", "#fff8"), ("#000f", "#fff")):
            with self.subTest(foreground=foreground, background=background), self.assertRaises(ValueError):
                contrast_check.check_contrast(foreground, background)
        with self.assertRaises(ValueError):
            contrast_check.check_contrast("#0008", "#fff", "#fff8")

    def test_alpha_compositing_order(self):
        result = contrast_check.check_contrast("#00000080", "#00000080", "#ffffff")
        colors = result["effective_srgb_0_to_1"]
        self.assertAlmostEqual(colors["background"][0], 127 / 255)
        self.assertAlmostEqual(colors["foreground"][0], (127 / 255) ** 2)
        self.assertEqual(contrast_check.check_contrast("#0000", "#fff", "#000")["ratio"], 1.0)

    def test_cli_errors_are_json_and_failure_exit_is_meaningful(self):
        output = io.StringIO()
        with redirect_stdout(output):
            code = contrast_check.main(["#badinput", "#fff"])
        self.assertEqual(code, 2)
        self.assertEqual(json.loads(output.getvalue())["status"], "FAIL")
        with redirect_stdout(io.StringIO()):
            self.assertEqual(contrast_check.main(["#777", "#fff"]), 1)
            self.assertEqual(contrast_check.main(["#000", "#fff"]), 0)


class AssetTestCase(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.folder = Path(self.directory.name)

    def tearDown(self):
        self.directory.cleanup()

    def svg(self, body: str = '<rect width="200" height="100" fill="#333"/>', attributes: str = 'width="200" height="100" viewBox="0 0 200 100"', name: str = "art.svg") -> Path:
        path = self.folder / name
        path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" {attributes}>{body}</svg>', encoding="utf-8")
        return path


class PreflightTests(AssetTestCase):
    def test_valid_svg_is_metadata_only(self):
        result = preflight.inspect_file(self.svg())
        checks = checks_by_name(result)
        self.assertEqual(result["status"], "NOT RUN")
        self.assertEqual(checks["svg_parse"]["status"], "PASS")
        self.assertEqual(checks["aspect_mapping"]["status"], "PASS")
        self.assertEqual(checks["visual_review"]["status"], "NOT RUN")
        self.assertTrue(result["metadata"]["safe_for_static_image_embedding"])

    def test_viewbox_and_absolute_units(self):
        result = preflight.inspect_file(self.svg(attributes='width="25.4mm" height="0.5in" viewBox="0 0 200 100"'))
        self.assertAlmostEqual(result["metadata"]["dimensions"]["width"]["pixels"], 96)
        self.assertAlmostEqual(result["metadata"]["dimensions"]["height"]["pixels"], 48)
        for viewbox in ("0 0 0 100", "0 0 -2 100", "0 0 nan 100", "0 0 200", "0 0 1e309 100"):
            with self.subTest(viewbox=viewbox):
                report = preflight.inspect_file(self.svg(attributes=f'width="200" height="100" viewBox="{viewbox}"'))
                self.assertEqual(checks_by_name(report)["viewbox"]["status"], "FAIL")

    def test_relative_lengths_do_not_invent_pixels(self):
        result = preflight.inspect_file(self.svg(attributes='width="100%" height="50%" viewBox="0 0 200 100"'))
        self.assertIsNone(result["metadata"]["dimensions"]["width"]["pixels"])
        self.assertEqual(checks_by_name(result)["width"]["status"], "NOT RUN")

    def test_mismatched_aspect_ratio_reports_behavior_without_design_judgment(self):
        for aspect, phrase in (("xMidYMid meet", "unused viewport space"), ("xMidYMid slice", "cropping"), ("none", "non-uniform scaling")):
            with self.subTest(aspect=aspect):
                result = preflight.inspect_file(self.svg(attributes=f'width="200" height="100" viewBox="0 0 100 100" preserveAspectRatio="{aspect}"'))
                check = checks_by_name(result)["aspect_mapping"]
                self.assertEqual(check["status"], "NOT RUN")
                self.assertIn(phrase, check["message"])

    def test_missing_and_existing_local_dependencies(self):
        path = self.svg('<image href="photo.png" width="100" height="100"/>')
        result = preflight.inspect_file(path)
        self.assertEqual(result["metadata"]["dependencies"][0]["status"], "FAIL")
        (self.folder / "photo.png").write_bytes(PIXEL_PNG)
        result = preflight.inspect_file(path)
        self.assertEqual(result["metadata"]["dependencies"][0]["status"], "PASS")
        self.assertEqual(checks_by_name(result)["self_contained"]["status"], "FAIL")

    def test_external_resources_are_not_fetched_or_portable(self):
        for href in ("https://example.invalid/photo.png", "//example.invalid/photo.png", "../photo.png", "/tmp/photo.png"):
            with self.subTest(href=href):
                result = preflight.inspect_file(self.svg(f'<image href="{href}"/>'))
                self.assertEqual(result["metadata"]["dependencies"][0]["status"], "NOT RUN")
                self.assertFalse(result["metadata"]["safe_for_static_image_embedding"])

    def test_fragments_and_duplicate_ids(self):
        valid = self.svg('<defs><linearGradient id="paint"/></defs><rect fill="url(#paint)"/>')
        self.assertEqual(checks_by_name(preflight.inspect_file(valid))["self_contained"]["status"], "PASS")
        missing = self.svg('<use href="#missing"/>')
        self.assertEqual(preflight.inspect_file(missing)["status"], "FAIL")
        duplicate = self.svg('<g id="x"/><g id="x"/>')
        self.assertEqual(checks_by_name(preflight.inspect_file(duplicate))["unique_ids"]["status"], "FAIL")

    def test_active_svg_and_css_dependency_syntax_are_rejected(self):
        bodies = ('<script>alert(1)</script>', '<foreignObject/>', '<rect onload="alert(1)"/>', '<animate attributeName="x"/>', '<style>@import "https://example.invalid/font.css";</style>', '<rect style="fill:u\\72l(https://example.invalid/x)"/>')
        for body in bodies:
            with self.subTest(body=body):
                result = preflight.inspect_file(self.svg(body))
                self.assertEqual(result["status"], "FAIL")
                self.assertFalse(result["metadata"]["safe_for_static_image_embedding"])

    def test_doctype_is_rejected_in_utf8_and_utf16(self):
        source = '<!DOCTYPE svg [<!ENTITY x "hello">]><svg xmlns="http://www.w3.org/2000/svg"><text>&x;</text></svg>'
        for encoding in ("utf-8", "utf-16"):
            with self.subTest(encoding=encoding):
                path = self.folder / "doctype.svg"
                path.write_bytes(source.encode(encoding))
                self.assertEqual(checks_by_name(preflight.inspect_file(path))["xml_safety"]["status"], "FAIL")

    def test_embedded_svg_data_is_not_treated_as_safe_raster(self):
        result = preflight.inspect_file(self.svg('<image href="data:image/svg+xml;base64,PHN2Zy8+"/>'))
        self.assertEqual(result["status"], "FAIL")

    def test_invalid_empty_missing_and_unsupported_files_are_honest(self):
        bad = self.folder / "bad.svg"
        bad.write_text("<svg", encoding="utf-8")
        self.assertEqual(preflight.inspect_file(bad)["status"], "FAIL")
        empty = self.folder / "empty.png"
        empty.write_bytes(b"")
        self.assertEqual(preflight.inspect_file(empty)["status"], "FAIL")
        self.assertEqual(preflight.inspect_file(self.folder / "absent.svg")["status"], "FAIL")
        other = self.folder / "source.ai"
        other.write_text("not inspected", encoding="utf-8")
        self.assertEqual(preflight.inspect_file(other)["status"], "NOT RUN")

    def test_missing_optional_dependencies_are_not_false_passes(self):
        png = self.folder / "pixel.png"
        png.write_bytes(PIXEL_PNG)
        with patch.dict(sys.modules, {"PIL": None}):
            result = preflight.inspect_file(png)
        self.assertEqual(checks_by_name(result)["raster_metadata"]["status"], "NOT RUN")
        pdf = self.folder / "sample.pdf"
        pdf.write_bytes(b"%PDF-1.7\n")
        with patch.dict(sys.modules, {"pypdf": None}):
            result = preflight.inspect_file(pdf)
        self.assertEqual(checks_by_name(result)["pdf_metadata"]["status"], "NOT RUN")

    def test_invalid_print_parameters(self):
        for size in ((0.0, 10.0), (-1.0, 2.0), (math.nan, 2.0), (math.inf, 3.0)):
            with self.subTest(size=size), self.assertRaises(ValueError):
                preflight.inspect_file(self.svg(), size)

    def test_symlink_loop_is_a_reported_file_failure(self):
        loop = self.folder / "loop.svg"
        try:
            loop.symlink_to(loop.name)
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks are unavailable in this environment")
        result = preflight.inspect_file(loop)
        self.assertEqual(checks_by_name(result)["file_read"]["status"], "FAIL")

    @unittest.skipUnless(HAS_PILLOW, "Pillow is optional")
    def test_raster_ppi_uses_pixels_and_explicit_size(self):
        from PIL import Image
        path = self.folder / "600x300.png"
        Image.new("RGB", (600, 300), "white").save(path, dpi=(72, 72))
        result = preflight.inspect_file(path, (50.8, 25.4))
        self.assertEqual(result["metadata"]["uncropped_ppi_xy"], [300.0, 300.0])
        self.assertEqual(checks_by_name(result)["effective_ppi"]["status"], "PASS")
        self.assertEqual(result["status"], "NOT RUN")
        low = preflight.inspect_file(path, (101.6, 50.8))
        self.assertEqual(checks_by_name(low)["effective_ppi"]["status"], "FAIL")
        mismatch = preflight.inspect_file(path, (50.8, 50.8))
        self.assertEqual(checks_by_name(mismatch)["effective_ppi"]["status"], "NOT RUN")

    @unittest.skipUnless(HAS_PILLOW, "Pillow is optional")
    def test_raster_orientation_and_decode_errors(self):
        from PIL import Image
        image = Image.new("RGB", (600, 300), "white")
        exif = Image.Exif()
        exif[274] = 6
        path = self.folder / "rotated.jpg"
        image.save(path, exif=exif)
        result = preflight.inspect_file(path, (25.4, 50.8))
        self.assertEqual(result["metadata"]["display_pixel_dimensions"], [300, 600])
        self.assertEqual(checks_by_name(result)["effective_ppi"]["status"], "PASS")
        (self.folder / "broken.png").write_bytes(b"not a png")
        self.assertEqual(preflight.inspect_file(self.folder / "broken.png")["status"], "FAIL")

    @unittest.skipUnless(HAS_PYPDF, "pypdf is optional")
    def test_pdf_geometry_and_encryption_scope(self):
        from pypdf import PdfWriter
        writer = PdfWriter()
        writer.add_blank_page(width=72, height=144)
        path = self.folder / "page.pdf"
        with path.open("wb") as stream:
            writer.write(stream)
        result = preflight.inspect_file(path)
        self.assertEqual(result["metadata"]["page_count"], 1)
        self.assertEqual(result["metadata"]["pages"][0]["media_size_mm_before_rotation"], [25.4, 50.8])
        self.assertEqual(result["status"], "NOT RUN")
        writer.encrypt("test-only-password")
        encrypted = self.folder / "encrypted.pdf"
        with encrypted.open("wb") as stream:
            writer.write(stream)
        result = preflight.inspect_file(encrypted)
        self.assertEqual(checks_by_name(result)["pdf_metadata"]["status"], "NOT RUN")
        self.assertNotIn("pages", result["metadata"])


class TagCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


class ReviewBoardTests(AssetTestCase):
    def test_html_escaping_data_embedding_and_source_preservation(self):
        path = self.svg()
        before = hashlib.sha256(path.read_bytes()).hexdigest()
        page, sources = review_board.build_review_board([{
            "path": str(path), "label": '<script>alert("label")</script>',
            "alt": '" onerror="alert(1)', "caption": '</figcaption><iframe src="https://example.invalid">',
            "annotations": [{"number": 1, "x": 10, "y": 25, "text": "<b>Supplied comment</b>"}],
        }], title='<img src=x onerror="alert(1)">')
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), before)
        self.assertEqual(sources, [path])
        self.assertIn("&lt;script&gt;", page)
        self.assertIn("&lt;b&gt;Supplied comment&lt;/b&gt;", page)
        self.assertIn("data:image/svg+xml;base64,", page)
        self.assertIn("Visual review: NOT RUN", page)
        self.assertIn("width:200px;height:100px", page)
        parser = TagCollector()
        parser.feed(page)
        self.assertFalse(any(tag in ("script", "iframe", "object", "embed") for tag, _ in parser.tags))
        self.assertFalse(any(any(key.startswith("on") for key in attrs) for _, attrs in parser.tags))
        self.assertTrue(all(attrs["src"].startswith("data:image/") for _, attrs in parser.tags if "src" in attrs))
        self.assertIn("default-src 'none'", page)

    def test_viewbox_alone_does_not_invent_actual_size(self):
        path = self.svg(attributes='viewBox="0 0 200 100"')
        page, _ = review_board.build_review_board([{"path": str(path)}])
        self.assertIn("Intrinsic-size view: NOT RUN", page)

    def test_review_board_rejects_active_and_external_svg(self):
        for body in ('<script>alert(1)</script>', '<image href="https://example.invalid/x.png"/>', '<style>@import "x.css";</style>'):
            with self.subTest(body=body), self.assertRaises(ValueError):
                review_board.build_review_board([{"path": str(self.svg(body))}])

    def test_invalid_annotations_are_not_silently_coerced(self):
        baseline = {"number": 1, "x": 50, "y": 50, "text": "Comment"}
        for change in ({"number": True}, {"number": 0}, {"x": math.nan}, {"x": "50"}, {"y": 101}, {"text": ""}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                review_board.validate_annotations([{**baseline, **change}])
        with self.assertRaises(ValueError):
            review_board.validate_annotations([baseline, baseline])

    def test_png_without_pillow_has_an_explicit_missing_size_check(self):
        path = self.folder / "pixel.png"
        path.write_bytes(PIXEL_PNG)
        with patch.dict(sys.modules, {"PIL": None}):
            page, _ = review_board.build_review_board([{"path": str(path)}])
        self.assertIn("data:image/png;base64,", page)
        self.assertIn("Intrinsic-size view: NOT RUN", page)

    @unittest.skipUnless(HAS_PILLOW, "Pillow is optional")
    def test_raster_board_reports_intrinsic_dimensions_without_editing(self):
        from PIL import Image
        path = self.folder / "art.png"
        Image.new("RGBA", (320, 160), (40, 80, 120, 128)).save(path)
        before = path.read_bytes()
        page, _ = review_board.build_review_board([{"path": str(path), "alt": "A translucent blue rectangle"}])
        self.assertIn("width:320px;height:160px", page)
        self.assertIn("data:image/png;base64,", page)
        self.assertEqual(before, path.read_bytes())

    def test_manifest_cli_resolves_paths_and_refuses_implicit_overwrite(self):
        self.svg()
        manifest = self.folder / "review.json"
        manifest.write_text(json.dumps({"title": "Test board", "assets": [{"path": "art.svg", "alt": "A gray rectangle"}]}), encoding="utf-8")
        output = self.folder / "review.html"
        arguments = ["--manifest", str(manifest), "--output", str(output)]
        with redirect_stdout(io.StringIO()):
            self.assertEqual(review_board.main(arguments), 0)
            first = output.read_text(encoding="utf-8")
            self.assertEqual(review_board.main(arguments), 2)
            self.assertEqual(output.read_text(encoding="utf-8"), first)
            self.assertEqual(review_board.main([*arguments, "--overwrite"]), 0)

    def test_unknown_manifest_keys_and_invalid_files_fail_cleanly(self):
        with self.assertRaises(ValueError):
            review_board.build_review_board([{"path": str(self.svg()), "script": "alert(1)"}])
        path = self.folder / "bad.png"
        path.write_text("not an image", encoding="utf-8")
        with self.assertRaises(ValueError):
            review_board.build_review_board([{"path": str(path)}])


if __name__ == "__main__":
    unittest.main()
