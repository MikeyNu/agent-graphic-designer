#!/usr/bin/env python3
"""Check solid sRGB color pairs. This is not an accessibility audit."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from typing import Sequence


HEX_COLOR = re.compile(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})\Z")
TARGETS = {
    "normal-text-aa": 4.5,
    "large-text-aa": 3.0,
    "normal-text-aaa": 7.0,
    "large-text-aaa": 4.5,
    "non-text-aa": 3.0,
}
SCOPE = (
    "Solid sRGB colors only. Alpha uses source-over compositing in encoded sRGB "
    "channel space on the stated opaque canvas. Gradients, images, blend modes, "
    "color management, font rendering, and accessibility conformance are not tested. "
    "The caller must determine whether a criterion and its exceptions apply."
)


@dataclass(frozen=True)
class Color:
    rgb: tuple[float, float, float]
    alpha: float
    has_alpha: bool


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        print(json.dumps({"status": "FAIL", "error": message, "scope": SCOPE}))
        raise SystemExit(2)


def parse_hex(value: str) -> Color:
    """Accept only #RGB, #RGBA, #RRGGBB, or #RRGGBBAA, without whitespace."""
    if not isinstance(value, str) or not HEX_COLOR.fullmatch(value):
        raise ValueError("Colors must be #RGB, #RGBA, #RRGGBB, or #RRGGBBAA hex strings.")
    digits = value[1:]
    has_alpha = len(digits) in (4, 8)
    if len(digits) in (3, 4):
        digits = "".join(char * 2 for char in digits)
    rgb = tuple(int(digits[index:index + 2], 16) / 255.0 for index in (0, 2, 4))
    alpha = int(digits[6:8], 16) / 255.0 if has_alpha else 1.0
    return Color(rgb, alpha, has_alpha)


def composite(foreground: Color, opaque_background: Sequence[float]) -> tuple[float, float, float]:
    return tuple(
        foreground.alpha * foreground.rgb[index]
        + (1.0 - foreground.alpha) * opaque_background[index]
        for index in range(3)
    )


def luminance(rgb: Sequence[float]) -> float:
    channels = [value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4 for value in rgb]
    return sum(weight * channel for weight, channel in zip((0.2126, 0.7152, 0.0722), channels))


def meets_threshold(ratio: float, threshold: float) -> bool:
    """Never round a displayed ratio before assessing a threshold."""
    return ratio >= threshold


def check_contrast(
    foreground: str,
    background: str,
    canvas: str | None = None,
    target: str = "normal-text-aa",
) -> dict:
    if target not in TARGETS:
        raise ValueError(f"Unknown target: {target}")
    fg, bg = parse_hex(foreground), parse_hex(background)
    base = parse_hex(canvas) if canvas is not None else None
    if base is not None and base.alpha != 1.0:
        raise ValueError("The canvas must be opaque.")
    if (fg.has_alpha or bg.has_alpha) and base is None:
        raise ValueError("Alpha notation requires an explicit opaque --canvas, including an FF alpha channel.")
    effective_bg = composite(bg, base.rgb) if base is not None else bg.rgb
    effective_fg = composite(fg, effective_bg)
    lightness = sorted((luminance(effective_fg), luminance(effective_bg)))
    ratio = (lightness[1] + 0.05) / (lightness[0] + 0.05)
    assessments = {
        name: {"threshold": threshold, "status": "PASS" if meets_threshold(ratio, threshold) else "FAIL"}
        for name, threshold in TARGETS.items()
    }
    return {
        "status": assessments[target]["status"],
        "target": target,
        "input": {"foreground": foreground, "background": background, "canvas": canvas},
        "effective_srgb_0_to_1": {"foreground": effective_fg, "background": effective_bg},
        "ratio": ratio,
        "ratio_display": f"{ratio:.2f}:1",
        "assessments": assessments,
        "scope": SCOPE,
        "large_text_definition": "At least 18 pt regular or 14 pt bold, with equivalent provisions for other scripts; assess at delivery size.",
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = JsonArgumentParser(description=__doc__)
    parser.add_argument("foreground", help="Quoted hex foreground, e.g. '#222222'.")
    parser.add_argument("background", help="Quoted hex background, e.g. '#FFFFFF'.")
    parser.add_argument("--canvas", help="Explicit opaque hex canvas, required for alpha notation.")
    parser.add_argument("--target", choices=tuple(TARGETS), default="normal-text-aa")
    args = parser.parse_args(argv)
    try:
        result = check_contrast(args.foreground, args.background, args.canvas, args.target)
    except ValueError as error:
        print(json.dumps({"status": "FAIL", "error": str(error), "scope": SCOPE}))
        return 2
    print(json.dumps(result, indent=2, allow_nan=False))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
