<p align="center">
  <img src="combover.png" width="256" alt="Combover mascot">
</p>

<h1 align="center">Combover</h1>

<p align="center"><strong>Good work. On time.</strong></p>

<p align="center">
  <img src="https://img.shields.io/badge/Agent%20Skill-portable-111111?style=flat-square" alt="Portable Agent Skill">
  <img src="https://img.shields.io/badge/license-MIT-111111?style=flat-square" alt="MIT license">
  <img src="https://img.shields.io/badge/runtime-none-111111?style=flat-square" alt="No runtime">
</p>

**Combover is the lazy senior knowledge worker in your AI toolbox.** The pitch deck is ready before the meeting. The Excel P&L ties out with time to spare. The research brief answers the question. He knows where care pays off and when the work is good enough to use.

Give that judgment to your AI agent. Combover applies the 80/20 rule to effort: concentrate on what changes the outcome, finish the requested work, check what matters, and deliver.

## What good enough looks like

Good enough means complete for its intended use, materially accurate, readable, and ready for the next action. The audience and deadline set the finish line.

| Work | Worth the effort | Time to stop |
|---|---|---|
| Pitch deck | Clear story, supported claims, consistent numbers, readable slides, a specific ask | The deck works in the meeting; another decorative pass adds little |
| Excel P&L or budget | Traceable inputs, working formulas, reconciled totals, clear assumptions | The model supports the decision; extra tabs and styling add little |
| Research brief | Relevant evidence, the answer, citations, consequential uncertainty | Requested coverage is complete and more searching is unlikely to change the answer |
| Proposal or report | Complete requirements, clear reasoning, useful next steps | The reader can decide or act without a companion explanation |
| Operations, HR, teaching, or planning | Accurate instructions, ownership, usable structure, the necessary context | The intended person can do the job |

## How it works

- Understand the audience, requested result, format, and deadline. Make routine decisions without handing the job back.
- Reuse accepted work, existing templates, and native tools. Build only what is missing.
- Finish the whole change. A revised assumption reaches the spreadsheet, chart, and summary that depend on it.
- Check the errors that could matter: unsupported claims, wrong formulas, missing requirements, unreadable output, or unsuccessful writes.
- Deliver when the result is usable and material checks pass. Further work needs a concrete defect, unmet requirement, usability problem, or requested refinement.

Accuracy, explicit requirements, and necessary safeguards stay intact. A complete long report is still appropriate when that is the job. Extra process and endless polish are optional.

## Modes

| Mode | Behavior |
|---|---|
| `lite` | Keep the requested approach, point out one simpler equivalent when useful. |
| `full` | Deliver the simplest complete result and stop when it is ready. Default. |
| `ultra` | Challenge optional complexity hardest without dropping requirements. |
| `off` | Stop applying Combover. |

Examples:

```text
Combover
Combover: get this pitch deck ready for tomorrow's meeting
Combover finance: update the P&L with these actuals
Combover ultra
Combover review: simplify this project task
Combover research: qualify this prospect list
stop combover
```

## Install

### ChatGPT

The portable skill source is in [skills/combover/](skills/combover/). If your ChatGPT workspace supports skill uploads, zip that folder for manual upload.

### Claude Code

```text
/plugin marketplace add iquantecho/combover
/plugin install combover@combover
```

### Codex

```bash
codex plugin marketplace add iquantecho/combover
codex plugin add combover@combover
```

The same portable plugin is suitable for ChatGPT/Codex marketplace import and public OpenAI plugin submission.

### GitHub Copilot CLI

Shortest path:

```bash
copilot plugin install iquantecho/combover
```

Marketplace install also works:

```bash
copilot plugin marketplace add iquantecho/combover
copilot plugin install combover@combover
```

### Gemini CLI / Antigravity

Install the skill directly:

```bash
gemini skills install https://github.com/iquantecho/combover.git --path skills/combover
```

Or install the repo as a Gemini extension:

```bash
gemini extensions install https://github.com/iquantecho/combover
```

### Cursor

Combover includes both the portable Agent Plugin manifest and a Cursor plugin manifest. Add the GitHub repository from Cursor's Plugins UI, or install it from the Cursor Marketplace once listed.

### OpenCode

OpenCode understands the standard Agent Skills layout. The universal installer below places Combover in both the standard agent directory and OpenCode's native directory.

### Universal fallback

macOS/Linux:

```bash
git clone https://github.com/iquantecho/combover.git ~/.combover
~/.combover/scripts/install.sh all
```

Windows PowerShell:

```powershell
git clone https://github.com/iquantecho/combover.git $HOME/.combover
& $HOME/.combover/scripts/install.ps1 all
```

The fallback installer copies the same canonical skill into the common user-level directories for OpenAI-compatible agents, Claude Code, Cursor, Gemini, and OpenCode. No shell profile changes, services, credentials, or telemetry.

See [compatibility details](docs/COMPATIBILITY.md).

## One canonical skill

The behavior lives in [skills/combover/SKILL.md](skills/combover/SKILL.md). Four optional references support [research](skills/combover/references/research.md), [finance](skills/combover/references/finance.md), [review](skills/combover/references/review.md), and [cleanup](skills/combover/references/cleanup.md). The agent loads only the method the task needs.

Combover uses the host's existing tools and artifact skills. It has no background runtime, credentials, telemetry, or lifecycle-hook dependency. For coding work, use [Ponytail](https://github.com/DietrichGebert/ponytail).

## Credit: Ponytail came first

Combover is directly inspired by [Ponytail](https://github.com/DietrichGebert/ponytail) by **Dietrich Gebert**, the original project that put a "lazy senior developer" minimalism reflex into AI coding agents.

Combover 0.3.0 learns from [Ponytail 5](https://github.com/DietrichGebert/ponytail/releases/tag/v5.0.0), using [v5.3.3](https://github.com/DietrichGebert/ponytail/releases/tag/v5.3.3) as the reference: understand the scope, finish affected dependencies, check meaningful risks, and make review findings concrete. Combover applies those lessons to knowledge work and adds a stopping rule based on the audience, deadline, and intended use.

This is a functional adaptation, not a port of Ponytail's code or wording. Ponytail is not affiliated with Combover.

## Development

Run the zero-dependency validator:

```bash
python tests/validate.py
```

GitHub Actions run the same check on pushes and pull requests. Tags matching `v*` also build `combover-skill.zip` and `combover-plugin.zip` release assets automatically.

## License

MIT
