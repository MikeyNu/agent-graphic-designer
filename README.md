# Agent Graphic Designer

A research-informed graphic design skill for agents that can inspect references, create visual artifacts, and iterate on the result. It combines art direction, typography, color, composition, contemporary and historical design judgment, tool selection, and rigorous visual and production QA.

**Start with [the skill](skills/graphic-design/SKILL.md).** Its supporting guides provide the depth needed for difficult decisions without loading an entire design manual for a small edit.

The goal is purposeful, distinctive work for a particular product and audience. The skill does not promise infallible taste, universal psychological effects, automatic audience validation, or client approval.

## Use it

### With an agent that can read this repository

Give the agent the repository URL and this instruction:

> Use the graphic-design skill in this repository. Read skills/graphic-design/SKILL.md and the guides relevant to the task. Create the actual design, inspect rendered results, compare meaningful alternatives where appropriate, correct defects, and report the checks you really performed. My brief is: [your brief].

Provide the audience, message, required copy, size or placement, brand assets, constraints, and delivery format when known. Missing reversible preferences should not trigger a long questionnaire. Dates, prices, contact details, or other facts must not be invented.

A repository URL does not by itself mean the files have been read or that graphics tools are available. The agent should inspect the files and use the capabilities available in its environment.

### With a directory-based skill installer

Install the complete [skills/graphic-design](skills/graphic-design) directory using your agent's supported skill-installation process. Keep its `references`, `scripts`, `assets`, and `agents` subdirectories together. Where named skill invocation is supported, use `$graphic-design`.

### As one Markdown attachment

Build a portable document containing the core instructions, reference guides, and templates:

```bash
python3 scripts/build_portable_skill.py --output /tmp/GRAPHIC_DESIGN_SKILL.md
```

Attach the generated document with your brief. The document links back to executable tools in this repository; attaching Markdown does not install Python packages or supply tool access. Use the modular package when possible so only relevant material needs to be loaded.

## What is included

| Component | Purpose |
| --- | --- |
| [Core skill](skills/graphic-design/SKILL.md) | Brief, research, concepts, construction, critique, verification, and delivery. |
| [Composition and layout](skills/graphic-design/references/composition-and-layout.md) | Hierarchy, grouping, grids, balance, scale, rhythm, visual tension, and annotated review. |
| [Typography and perception](skills/graphic-design/references/typography-and-perception.md) | Font anatomy, situated emotional associations, specimen testing, multilingual text, and microtypography. |
| [Color and accessibility](skills/graphic-design/references/color-and-accessibility.md) | Contextual palette development, color psychology limits, contrast, and color management. |
| [Originality and trends](skills/graphic-design/references/originality-and-trends.md) | Current-practice research, historical reinterpretation, concept experiments, and avoiding generic AI output. |
| [Asset creation](skills/graphic-design/references/asset-creation.md) | Image generation, custom SVG, exact typesetting, factual graphics, mockups, and annotations. |
| [Quality and production](skills/graphic-design/references/quality-and-production.md) | Visual review, content accuracy, raster/vector/print checks, evidence, and release status. |
| [Sourcebook](skills/graphic-design/references/sourcebook.md) | Research and primary-source references with dates, precise support, and limitations. |
| [QA tools](skills/graphic-design/references/tools.md) | Contrast calculation, metadata preflight, and self-contained visual review boards. |
| [Templates](skills/graphic-design/assets) | Brief, concept comparison, honest QA record, and handoff. |
| [Evaluation briefs](evals/briefs.json) | Twelve realistic task definitions with expected behavior and failure signals. |
| [Executed examples](evals/examples/README.md) | Original poster, annotated flyer correction, visible concept studies, and actual QA evidence. |

## How the design method works

1. **Define the specific communication problem.** Translate “best,” “modern,” or “creative” into audience, message, context, and observable success criteria.
2. **Study real work.** Inspect sources and actual images, distinguish original project dates from repost dates, and avoid treating one design feed as the entire audience.
3. **Explore different concepts.** For substantial work, make visible roughs of different visual ideas using comparable copy and fidelity. Palette swaps do not count as different concepts.
4. **Build with the right tools.** Combine original imagery, vector construction, real typography, diagrams, layout tools, or annotations as the idea requires.
5. **Inspect and revise.** Compare the rendered artifact with the brief at actual delivery size and detail. Correct consequential defects before refining decoration.
6. **Deliver with an honest status.** Record what passed, failed, was not run, or does not apply. Separate internal critique from audience testing, client approval, and physical print proofing.

### What “avoid AI slop” means here

It means detecting interchangeability, automatic decoration, empty concepts, repetitive composition, inaccurate copy, and uninspected synthetic defects. It does not mean banning gradients, serif fonts, vintage references, rounded shapes, minimalism, expressive illustration, or maximalism.

The agent should be able to explain why a visual mechanism belongs to the subject, then judge whether the actual execution succeeds. Historical vocabulary can work well today when the application gives it meaning.

### Psychology without a false dictionary

Font voice and color associations are treated as hypotheses grounded in form, culture, content, and context. Research findings retain their limits. A serif is not automatically trustworthy; a sans serif is not automatically modern or more readable; a color does not guarantee a response. See the [sourcebook](skills/graphic-design/references/sourcebook.md).

## Run the tools and tests

The contrast calculator, SVG metadata checks, review-board construction, repository checks, and portable builder use Python's standard library. Raster preflight requires Pillow; PDF metadata checks require pypdf. The pinned versions used for the optional QA environment are in [requirements-qa.txt](requirements-qa.txt).

```bash
python3 -m pip install -r requirements-qa.txt
python3 -m unittest discover -s tests -v
```

Read [the tool guide](skills/graphic-design/references/tools.md) before running the artwork checks. The tools report narrow technical facts and unperformed checks. They do not score beauty, inspect anatomy, validate copyright, perform user research, or certify production readiness.

The repository's CI runs software and package checks. It does not count as visual QA of a future design. See [evaluation guidance](evals/README.md) and [the recorded validation](evals/validation-2026-10-18.md) for the distinction between automated tests and design exercises actually performed.

## Maintain it

Refresh time-sensitive source claims, platform specifications, font availability, and licenses when relevant. Keep durable principles separate from current examples. Preserve uncertainty and source scope. Test changes against contrasting briefs and inspect the actual outputs, especially after altering the core workflow.

Do not add permanent trend blacklists, a universal “premium” aesthetic, magic personality prompts, or numerical beauty scores presented as science. Add scripts only for repeated tasks that benefit from reliable execution, and test them with failure cases.

## License and reference material

The repository retains its original [MIT license](LICENSE). Linked studies, brand examples, fonts, and third-party artwork remain subject to their own rights. Links and concise analysis do not grant permission to redistribute or incorporate those assets into client work.
