# Local Windows browser exercise

The user explicitly authorized the local desktop browser for this follow-up. The scripts use a new headed Edge instance and task-owned profiles, without attaching to the user's everyday browser or signed-in sessions. They serve only the two fictional fixtures on loopback. This is optional integration-test infrastructure, not a dependency of the skill or its Python tools.

Create an isolated QA directory with these entries:

- `graphic`: clone of this repository.
- `motion`: clone of `https://github.com/MikeyNu/Web-Motion-Director.git`.
- `tools/node_modules`: Playwright and axe dependencies.
- `browser-qa.cjs` and `bfcache-qa.cjs`: copies of the two scripts in this folder.

On the tested Windows setup, install dependencies explicitly into that directory using `npm install --prefix tools playwright@1.64.1 @axe-core/playwright@4.14.0 --ignore-scripts --no-audit --no-fund`. Edge must already be installed in its standard Windows location. No browser is automatically installed. Do not use these scripts where host policy prohibits their runtime or targets.

Run `node browser-qa.cjs evidence-new-run` from the QA directory, choosing a fresh output directory for every run. Run `node bfcache-qa.cjs` separately after other browser checks finish. The latter launches standalone Edge without Playwright/CDP, injects disclosed lifecycle logging into a served copy, follows native history, and terminates only its own launched process tree. Its temporary browser profile stays in the QA directory and can be removed after that process exits.

The suite returns a nonzero exit for failed assertions. Browser focus may enter native browser controls; the modal assertion rejects background-page focus while the document has focus. Text scaling snapshots every baseline before mutation. Fixed dialogs use viewport screenshots, while page composition uses full-page images. Inspect both outputs and test assumptions; passing assertions do not establish complete accessibility or aesthetic quality.

[browser-summary.json](browser-summary.json) retains the 39 check results, 30 axe scan summaries, sampled browser motion traces, exact/canonical input hashes, screenshot/report hashes, and the genuine persisted-page event sequence from the final run. Full screenshots, videos, and raw traces remain in the task's local desktop evidence directory. See the [dated interpretation](../validation-2026-10-31-desktop.md) for discoveries, corrections, and limits.
