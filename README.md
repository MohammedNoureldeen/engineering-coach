# Engineering Coach

[العربية](README.ar.md)

Understand, debug, and independently extend the features you ship with AI. Engineering Coach turns a real diff, feature, or conversation into a focused engineering lesson.

One skill, six modes, for **Codex and Claude Code**. The skill is Markdown and has no runtime dependencies of its own. Your coding assistant provides the model and tools; normal account access and usage limits apply.

## Quick start

Install the skill using the instructions below, then give it a real change:

```text
Codex:       $engineering-coach changes <PR, commit, diff, file, or chat reference>
Claude Code: /engineering-coach changes <PR, commit, diff, or file>
```

For example: "Explain the bug, follow one failing input through the old and new code, and show me how to recognize this problem next time."

## Six learning modes

| Mode | What you learn | Example after the skill name |
| --- | --- | --- |
| `changes` | What changed and how the fix or feature works | `changes explain this PR before and after` |
| `decisions` | Choices, alternatives, tradeoffs, and limits | `decisions why batch these database reads?` |
| `terms` | Relevant terms explained through your code | `terms explain RMS, threshold, and hysteresis here` |
| `flow` | A request or event through data and state | `flow trace one audio frame through this filter` |
| `quiz` | Understanding through prediction and debugging | `quiz me on this boundary fix, one question at a time` |
| `practice` | A small related exercise with acceptance criteria | `practice give me a variation of this batching problem` |

The words after the skill name select a mode; they are not separate slash commands. Natural language also works. A supplied change without a mode defaults to `changes`. With no clear task or target, the skill offers a compact menu.

Explanation modes answer first, then offer one short understanding check. Quiz and practice wait for your attempt, offer hints, and explain after you answer. You can always say **"show me the answer"**, **"no questions"**, **"go deeper"**, or **"explain in Arabic."**

## Install

Clone this public repository into a location of your choice:

```sh
git clone https://github.com/MohammedNoureldeen/engineering-coach.git
cd engineering-coach
```

Copy the **whole** `skills/engineering-coach` directory, including `references` and `agents`. Choose one user directory per tool so you do not create duplicate installations.

| Tool | User destination | Invocation |
| --- | --- | --- |
| Codex | `~/.agents/skills/engineering-coach` | `$engineering-coach changes ...` |
| Claude Code | `~/.claude/skills/engineering-coach` | `/engineering-coach changes ...` |

### Windows PowerShell

Run from the cloned repository. This example installs for Codex:

```powershell
$coachSource = (Resolve-Path '.\skills\engineering-coach').Path
$coachDestination = Join-Path $HOME '.agents\skills\engineering-coach'
if (Test-Path -LiteralPath $coachDestination) { throw 'Skill already exists; see Updating.' }
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $coachDestination) | Out-Null
Copy-Item -LiteralPath $coachSource -Destination $coachDestination -Recurse
```

For Claude Code, use `'.claude\skills\engineering-coach'` in the destination line instead. To install for both, run the block once for each destination.

### macOS / Linux

Run from the cloned repository. This example installs for Codex:

```sh
coach_destination="$HOME/.agents/skills/engineering-coach"
if [ -e "$coach_destination" ]; then
  echo "Skill already exists; see Updating."
else
  mkdir -p "$(dirname "$coach_destination")" &&
    cp -R skills/engineering-coach "$coach_destination"
fi
```

For Claude Code, set `coach_destination="$HOME/.claude/skills/engineering-coach"` instead. To install for both, run the block once per destination.

Start a fresh assistant session after installation. Codex should discover `engineering-coach`; Claude Code should offer `/engineering-coach`. If it is missing, check that `SKILL.md` is directly inside the destination folder and that you installed in the same environment where the tool runs. Windows and WSL can have different home directories.

Codex installations using the existing `$CODEX_HOME/skills` convention can use that directory instead of `.agents/skills`. Do not install the same skill into both locations. See the current [Codex documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code documentation](https://code.claude.com/docs/en/skills) for host-specific discovery behavior. Codex UI metadata lives in `agents/openai.yaml`; the teaching instructions are shared.

### Updating

In your clone, run `git pull --ff-only`. Rename your installed `engineering-coach` folder to a backup **outside the tool's skills directory**, then repeat the copy instructions. Keeping the backup outside prevents duplicate discovery; copying into an empty destination also removes obsolete files from the active installation. Preserve any personal edits in the backup and reapply them deliberately.

### Removing

Delete only the installed `engineering-coach` directory from the destination you chose, then start a fresh session. If installed for both tools, remove both copies. Your repository clone is separate and can be kept for later use. No global settings or other skills need to change.

## Learn from another chat

In a host that supports chat mentions or links and provides a read capability, reference the feature conversation and ask:

```text
$engineering-coach changes
Explain the feature from the referenced chat. Check the actual diff if available.
```

A title or mention does not automatically grant access. The skill uses available reading tools; when the host cannot retrieve the chat, paste the relevant transcript, supply a diff, or point it to accessible code. Claude Code does not gain access to your Codex or ChatGPT chats by installing this skill.

A current file can explain present behavior. A before-and-after claim needs an actual comparison. Claims from an earlier chat are checked against code when code is available, and missing evidence is stated plainly.

## Try the synthetic examples

These examples are invented for learning and contain no private project material:

- [Expiry boundary bug](examples/bug-fix.md): compare exact-boundary behavior and test the fix.
- [N+1 database reads](examples/n-plus-one.md): reason about round trips, missing records, and batch limits.
- [Audio noise gate](examples/noise-gate.md): trace state, understand terminology, and see the limits of threshold filtering.

From this repository, try `$engineering-coach decisions examples/n-plus-one.md` or `/engineering-coach terms examples/noise-gate.md`. Both tools need filesystem access to the example. For Arabic: `$engineering-coach changes examples/bug-fix.md اشرح بالعربية`.

## How it teaches

The learning loop combines concrete explanations, brief recall, and application to a new case. It adapts to your questions and demonstrated understanding. It cites inspected evidence and labels inferred rationale; it does not invent benchmarks or claim tests were run when they were only proposed.

Coaching is read-only by default. Exercises appear in chat, and implementation or execution requires a separate user request. Learning stays in the conversation unless you ask to save it. There is no learner tracking service or reminder system.

The main [SKILL.md](skills/engineering-coach/SKILL.md) routes to one guide per mode. English instructions are the canonical behavior; responses follow the user's language, with English technical terms alongside Arabic where helpful. Supporting guides load as needed.

Read the [research rationale](docs/learning-design.md), [validation results and limitations](docs/validation.md), and [contribution guide](CONTRIBUTING.md). Claude Code compatibility is documented, but runtime testing is reported separately from documentation checks. The package is released under the [MIT License](LICENSE).
