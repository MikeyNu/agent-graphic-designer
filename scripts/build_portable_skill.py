#!/usr/bin/env python3
"""Assemble instructions and references into one Markdown attachment, without network access."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re
import sys
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SKILL = REPO_ROOT / "skills" / "graphic-design"
REPO_URL = "https://github.com/MikeyNu/agent-graphic-designer/blob/main/skills/graphic-design/"
LINK = re.compile(r"(!?\[[^\]\n]*\])\(([^\s)]+)([^)]*)\)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")


def slug(text: str) -> str:
    text = re.sub(r"<[^>]*>", "", text)
    return re.sub(r"[^\w\s-]", "", text.lower()).strip().replace(" ", "-")


def section_id(relative: Path) -> str:
    return "bundled-" + slug(relative.with_suffix("").as_posix().replace("/", "-"))


def checked_path(path: Path, root: Path) -> Path:
    resolved = path.resolve()
    if not resolved.is_relative_to(root):
        raise ValueError(f"Resource escapes skill directory: {path.name}")
    if not resolved.is_file():
        raise ValueError(f"Missing linked resource: {path.name}")
    return resolved


def rewrite_markdown(text: str, source: Path, root: Path, included: set[Path]) -> str:
    prefix = section_id(source.relative_to(root))
    seen: Counter[str] = Counter()
    result: list[str] = []
    fence: str | None = None

    def rewrite_link(match: re.Match[str]) -> str:
        label, target, title = match.groups()
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
            return match.group(0)
        path_text, separator, fragment = target.partition("#")
        if not path_text:
            return f"{label}(#{prefix}-{fragment}{title})"
        target_file = checked_path(source.parent / unquote(path_text), root)
        if target_file in included:
            anchor = section_id(target_file.relative_to(root))
            if separator and fragment:
                anchor += "-" + fragment
            return f"{label}(#{anchor}{title})"
        url = REPO_URL + target_file.relative_to(root).as_posix()
        if separator:
            url += "#" + fragment
        return f"{label}({url}{title})"

    for line in text.splitlines():
        stripped = line.lstrip()
        marker = re.match(r"(`{3,}|~{3,})", stripped)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            result.append(line)
            continue
        if fence is not None:
            result.append(line)
            continue
        header = HEADING.match(line)
        if header:
            base = slug(header.group(2))
            count = seen[base]
            seen[base] += 1
            suffix = f"-{count}" if count else ""
            result.append(f'<a id="{prefix}-{base}{suffix}"></a>')
        result.append(LINK.sub(rewrite_link, line))
    return "\n".join(result).rstrip() + "\n"


def build(skill_dir: Path) -> str:
    root = skill_dir.resolve()
    main = checked_path(root / "SKILL.md", root)
    references = sorted((root / "references").glob("*.md"))
    assets = sorted(p for p in (root / "assets").glob("*") if p.suffix in {".md", ".json"})
    license_file = root / "LICENSE"
    files = [main, *references, *assets, *([license_file] if license_file.is_file() else [])]
    included = {checked_path(path, root) for path in files}
    parts: list[str] = []
    for index, path in enumerate(files):
        path = path.resolve()
        relative = path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        if index:
            parts.append(f'\n---\n\n<a id="{section_id(relative)}"></a>\n\n# Bundled resource: {relative.as_posix()}\n\n')
        if path.suffix == ".md":
            parts.append(rewrite_markdown(text, path, root, included))
        elif path.suffix == ".json":
            parts.append("```json\n" + text.rstrip() + "\n```\n")
        else:
            parts.append("```text\n" + text.rstrip() + "\n```\n")
        if index == 0:
            parts.append(
                "\n## Portable attachment note\n\n"
                "The following guides and templates are included in this attachment. "
                "Executable tools remain in the linked repository. Attaching this file does not "
                "install software, provide missing tools, or authorize publishing. Use the "
                "capabilities actually available and identify checks that cannot be run.\n"
            )
    return "".join(parts)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-dir", type=Path, default=DEFAULT_SKILL)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--force", action="store_true", help="Replace an existing output outside the source skill.")
    args = parser.parse_args(argv)
    try:
        output = args.output.resolve()
        if output.suffix.lower() != ".md":
            raise ValueError("Output must have a .md extension.")
        if output.is_relative_to(args.skill_dir.resolve()):
            raise ValueError("Output must be outside the source skill directory.")
        if output.exists() and not args.force:
            raise ValueError("Output already exists; use --force to replace it.")
        content = build(args.skill_dir)
        output.parent.mkdir(parents=True, exist_ok=True)
        mode = "w" if args.force else "x"
        with output.open(mode, encoding="utf-8") as handle:
            handle.write(content)
        print(f"Wrote {output.name}: {len(content.encode('utf-8'))} bytes")
        return 0
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Cannot build portable skill: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
