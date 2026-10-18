"""Package portability checks, separate from visual-design evaluation."""

import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "graphic-design"
SPEC = importlib.util.spec_from_file_location("portable_builder", ROOT / "scripts" / "build_portable_skill.py")
BUILDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILDER)


class RepositoryTests(unittest.TestCase):
    def test_installable_skill_preserves_repository_license(self):
        self.assertEqual((ROOT / "LICENSE").read_bytes(), (SKILL / "LICENSE").read_bytes())

    def test_core_frontmatter_and_size(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\nname: graphic-design\ndescription: "))
        frontmatter = text.split("---", 2)[1]
        self.assertEqual(len(frontmatter.strip().splitlines()), 2)
        self.assertNotIn("TODO", text)
        self.assertLess(len(text.splitlines()), 500)

    def test_no_machine_paths_in_skill_instructions(self):
        for path in [SKILL / "SKILL.md", *list((SKILL / "references").glob("*.md"))]:
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("/workspace/scratch/", text, str(path))
            self.assertNotIn("/root/.codex/", text, str(path))

    def test_no_em_dashes_in_authored_text(self):
        for path in ROOT.rglob("*"):
            if path.is_file() and path.suffix in {".md", ".json", ".yml", ".yaml"}:
                self.assertNotIn(chr(0x2014), path.read_text(encoding="utf-8"), str(path))

    def test_all_local_markdown_file_links_resolve(self):
        for path in ROOT.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for target in re.findall(r"\]\(([^\s)]+)", text):
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                    continue
                destination = target.split("#", 1)[0]
                if not destination:
                    continue
                resolved = (path.parent / destination).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT), f"Link outside repository: {path.name}: {target}")
                self.assertTrue(resolved.exists(), f"Missing resource: {path.name}: {target}")

    def test_evaluation_definitions_have_distinct_cases(self):
        data = json.loads((ROOT / "evals" / "briefs.json").read_text(encoding="utf-8"))
        cases = data if isinstance(data, list) else data["briefs"]
        self.assertEqual(len(cases), 12)
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        for case in cases:
            for field in ("task", "supplied_facts", "constraints", "expected_behaviors", "failure_signals"):
                self.assertTrue(case[field], f"{case['id']}: {field}")
            self.assertIn(case["test_kind"], {"execution", "reasoning"})

    def test_qa_template_never_preclaims_pass(self):
        report = json.loads((SKILL / "assets" / "qa-report-template.json").read_text(encoding="utf-8"))
        self.assertTrue(report["checks"])
        for check in report["checks"]:
            self.assertEqual(check["status"], "NOT RUN")
            self.assertEqual(check["evidence"], "")
        self.assertEqual(report["human_approval"]["status"], "NOT RUN")


class PortableBuilderTests(unittest.TestCase):
    def test_builds_real_skill_with_internal_anchors(self):
        result = BUILDER.build(SKILL)
        self.assertTrue(result.startswith("---\nname: graphic-design\n"))
        self.assertIn("#bundled-references-color-and-accessibility", result)
        self.assertIn('id="bundled-references-color-and-accessibility"', result)
        self.assertIn("Executable tools remain", result)
        for script in ("contrast_check.py", "preflight.py", "review_board.py"):
            self.assertIn(BUILDER.REPO_URL + "scripts/" + script, result)
        self.assertIn((ROOT / "LICENSE").read_text(encoding="utf-8").strip(), result)
        anchors = set(re.findall(r'<a id="([^"]+)"', result))
        for fragment in re.findall(r"\]\(#([^\s)]+)", result):
            self.assertIn(fragment, anchors, f"Missing bundled anchor: {fragment}")

    def test_missing_resource_fails_instead_of_building_broken_bundle(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "SKILL.md").write_text("# Skill\n[missing](references/missing.md)\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Missing linked resource"):
                BUILDER.build(root)

    def test_reference_cannot_escape_skill_directory(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "skill"
            root.mkdir()
            (root.parent / "outside.md").write_text("private", encoding="utf-8")
            (root / "SKILL.md").write_text("[outside](../outside.md)", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "escapes skill directory"):
                BUILDER.build(root)

    def test_fenced_examples_are_not_rewritten(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "SKILL.md"
            source.write_text("# Skill\n```md\n[example](missing.md)\n```\n", encoding="utf-8")
            self.assertIn("[example](missing.md)", BUILDER.build(root))


if __name__ == "__main__":
    unittest.main()
