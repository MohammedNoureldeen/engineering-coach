# Validation record

Initial release checks performed on **2026-10-20**, using Windows, Python 3.13, Codex CLI `0.163.0-alpha.10.2`, and the user's configured `gpt-6-astra` model. Claude Code was not installed. These results describe this environment and these sampled outputs, not a guarantee for every host or future model response.

## Package and executable examples

| Check | Result |
| --- | --- |
| Skill creator's `quick_validate.py` | Passed: naming, YAML frontmatter, and scaffold validation |
| `python scripts/check_package.py` | Passed: required files, six modes, UTF-8 Markdown, local links, self-contained installed references, and evaluation cases |
| Codex display metadata | Parsed successfully; short description and default invocation checked |
| `python evals/check_examples.py` | Seven tests passed |
| English / Arabic README review | Equivalent installation, modes, examples, updates, removal, and access limitations |

The seven executable tests cover expiry before/at/after the boundary; order preservation with duplicate and missing users and reversed batch results; empty order lists; gate state sequences and empty frames; exact thresholds and prior state; multi-sample RMS and input preservation; and invalid threshold configurations. They validate the synthetic Python fixtures, not an external application's behavior.

## Installation and discovery

- The documented PowerShell copy procedure was exercised in scratch `.agents/skills/engineering-coach` and `.claude/skills/engineering-coach` directories. Both contained the expected eight files.
- The documented POSIX copy block was executed under Git Bash and produced eight byte-identical files. Native macOS and Linux installation were not tested.
- A fresh Codex CLI session discovered the skill from a scratch project `.agents/skills` directory and explicitly invoked it. Its attempted reads of the mode guide and example were rejected with `blocked by policy` under the read-only execution policy. Automatic discovery and invocation were observed; the complete file-reading workflow was **not verified** in that environment.
- Claude Code's installation location and slash invocation were checked against its [official skills documentation](https://code.claude.com/docs/en/skills). Copying into the expected directory is **not** a Claude Code runtime test.
- Tests used scratch directories and did not install into the user's global skills directories or alter the existing `engineering-mentor` skill.

## Behavioral evaluation

The [17 cases](../evals/cases.json) were run in fresh, ephemeral Codex sessions. Because file reads were blocked, each request included the relevant mode guide and synthetic example as pasted content, with a request to use that material directly without tools. The main skill remained discoverable through the installed scratch package. The criteria were kept out of the model request and the resulting answers were reviewed manually.

| Cases | Observed result |
| --- | --- |
| `changes-boundary`, `default-change` | Explained the exact expiry boundary, defaulted to changes, and separated expected behavior from executed tests |
| `decisions-batching`, `unsupported-speedup` | Explained database call counts, complexity, alternatives, and constraints; rejected the unsupported measured speedup |
| `terms-audio`, `arabic-terms` | Defined RMS and hysteresis accurately, distinguished gating from general denoising, and preserved identifiers in natural Arabic |
| `flow-state` | Correctly traced zero/pass/pass/zero with prior state and explained empty-frame handling |
| `quiz-first-turn`, `quiz-hint`, `quiz-feedback` | Waited after one question, gave a non-revealing hint, and corrected the inclusive-expiry misconception after an attempt |
| `practice-first-turn`, `practice-explicit-solution` | Assigned one bounded transfer exercise with criteria; provided a correct chunked solution only when explicitly requested |
| `missing-chat`, `ambiguous-target`, `empty-menu` | Requested missing material or a concrete selection instead of fabricating a target |
| `direct-answer` | Gave the requested two-sentence answer without a question |
| `current-only` | Stated that the old behavior was unknown and requested the earlier version or diff |

One initial current-only response stated the history limitation but ended with a quiz. The changes guide was refined to request the missing comparison instead; the targeted rerun passed. All 17 final scenarios met their criteria. Scratch skill and example files were hashed before and after every session; no changes were observed.

This fallback verifies sampled teaching behavior with supplied materials. It does not independently prove automatic guide loading, file-reading integration, or permission enforcement by the skill. Follow-up scenarios supplied prior dialogue in the prompt rather than testing a persistent multi-turn session. The read-only sandbox and no-tool request also constrained possible side effects.

## Reproduce and extend

```sh
python scripts/check_package.py
python evals/check_examples.py
```

For behavioral checks, install the skill, open a fresh session with access to this repository, and use the prompts and criteria in `evals/cases.json`. If file-reading tools are unavailable, paste the corresponding guide and example and record that fallback. For Claude Code, replace the `$engineering-coach` prefix with `/engineering-coach`. Save logs outside the tracked project and compare fixture contents before and after.

The skill creator's validator is provided by Codex rather than bundled here; it requires PyYAML when run separately. Runtime testing in Claude Code, native macOS/Linux testing, unrestricted file-reading integration, repeated-sample reliability testing, and learner studies measuring delayed recall or transfer remain unverified. The [research rationale](learning-design.md) distinguishes instructional design from proven learning outcomes.
