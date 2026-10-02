<p align="center">
  <img src="combover.png" width="256" alt="Combover mascot">
</p>

<h1 align="center">Combover</h1>

<p align="center"><strong>Less overhead. Same coverage.</strong></p>

<p align="center">
  <img src="https://img.shields.io/badge/Agent%20Skill-portable-111111?style=flat-square" alt="Portable Agent Skill">
  <img src="https://img.shields.io/badge/license-MIT-111111?style=flat-square" alt="MIT license">
  <img src="https://img.shields.io/badge/runtime-none-111111?style=flat-square" alt="No runtime">
</p>

Combover is an Agent Skill for knowledge work. It helps AI agents remove process, artifacts, dependencies, duplicate work, and maintenance without shrinking the outcome you actually asked for.

Think of it as the operator who replaces a steering committee with one checked spreadsheet.

## What it changes

Without Combover, an agent can turn a straightforward business task into a research plan, tracker, reconciliation document, handoff, review loop, and follow-up task.

With Combover, the agent first asks:

1. Does this extra work need to exist?
2. Is the answer already decided or available?
3. Can a native capability do it?
4. Is there a standard method before custom machinery?
5. Can one artifact or action finish it?
6. What is actually still missing?

Then it does the missing work and verifies the result.

## Modes

| Mode | Behavior |
|---|---|
| `lite` | Keep the requested approach, point out one simpler equivalent when useful. |
| `full` | Take the first sufficient route. Default. |
| `ultra` | Challenge optional complexity hardest without dropping requirements. |
| `off` | Stop applying Combover. |

Examples:

```text
Combover
Combover ultra
Combover review: simplify this project task
Combover research: qualify this prospect list
stop combover
```

## Install

### ChatGPT

Once Combover is approved in the public OpenAI Plugins Directory, install it there like any other plugin. Until then, eligible ChatGPT Skills users can download `combover-skill.zip` from GitHub Releases and use **Plugins → Skills → Create → Upload from your computer**.

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

Combover intentionally keeps a single source of truth:

```text
skills/combover/
├── SKILL.md
└── references/
    ├── research.md
    ├── finance.md
    ├── review.md
    └── cleanup.md
```

The core loads a reference only when the task needs that method. There is no mandatory pipeline and no agent swarm hiding behind the skill.

## What Combover is not

- Not a coding minimalism skill. Use [Ponytail](https://github.com/DietrichGebert/ponytail) for that.
- Not a terse-writing formatter. It can produce a complete long artifact when the job requires one.
- Not an MCP server. It uses the tools the host already provides.
- Not an automation daemon. It has no background runtime, credentials, telemetry, or lifecycle-hook dependency.

## Credit: Ponytail came first

Combover is directly inspired by [Ponytail](https://github.com/DietrichGebert/ponytail) by **Dietrich Gebert**, the original project that put a "lazy senior developer" minimalism reflex into AI coding agents.

Ponytail's core idea is the important precedent: understand the work, then stop at the first sufficient solution instead of automatically building more machinery. Combover translates that philosophy from code into knowledge work such as research, finance, CRM, documentation, operations, planning, and business execution.

This is a functional adaptation, not a port of Ponytail's code or wording. Ponytail is not affiliated with Combover.

## Development

Run the zero-dependency validator:

```bash
python tests/validate.py
```

GitHub Actions run the same check on pushes and pull requests. Tags matching `v*` also build `combover-skill.zip` and `combover-plugin.zip` release assets automatically.

## License

MIT
