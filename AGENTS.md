# Repository instructions

This repository is a reusable graphic-design skill package, not a graphic-design application.

## Before editing

Read `README.md`, `skills/graphic-design/SKILL.md`, and the reference affected by the change. Preserve the existing MIT license. Keep the skill portable: no local machine paths, invented tool names, or hidden runtime dependencies in its operating instructions.

## Writing and research

Use plain instructions and no em dashes. Separate empirical evidence, specifications, practitioner accounts, and original design synthesis. Cite specific factual claims and record limitations in the sourcebook. Never convert current trends into a permanent blacklist or a universal default aesthetic.

Keep the main skill focused and below 500 lines. Put depth in directly linked reference files. Avoid duplicating entire guides in the core. Update the relevant sourcebook entry when factual guidance changes.

## Tools and checks

Use the standard library where practical. Keep optional dependencies explicit. Do not add network calls or automatic package installation to artwork-checking scripts. Do not silently modify supplied assets. Keep unsafe SVG content inert when building review surfaces.

Automated checks may report measurable facts only. Never change NOT RUN into PASS to make a report look complete. Technical checks cannot certify taste, audience response, rights, accessibility as a whole, or client approval.

Run `python3 -m unittest discover -s tests -v` after changing the package or tools. Use `python3 scripts/build_portable_skill.py --output /tmp/GRAPHIC_DESIGN_SKILL.md` to verify portable generation. Do not commit generated bundles, caches, machine paths, or raw temporary review artifacts.

## Evaluation

Use fresh context for design forward tests. Give the agent the brief, required input artifacts, and the skill, without the desired aesthetic or your diagnosis. Inspect the actual outputs. Distinguish an evaluation definition from an evaluation run. Add concise evidence to a dated evaluation record when substantive behavior changes.
