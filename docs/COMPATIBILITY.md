# Compatibility

Combover is intentionally skills-only. It has no MCP server, credentials, telemetry, background service, or lifecycle hook dependency.

The canonical package is `skills/combover/`, using the open Agent Skills layout: one `SKILL.md` plus on-demand `references/`.

| Harness | Native package in this repo | Recommended install path |
|---|---|---|
| ChatGPT / Codex | `plugin.json`, `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json` | Plugin marketplace or uploaded skill/plugin |
| Claude Code | `.claude-plugin/` | Claude plugin marketplace |
| Cursor | root Agent Plugin + `.cursor-plugin/plugin.json` | Cursor plugin or skill install |
| GitHub Copilot | `.github/plugin/` | Copilot plugin marketplace |
| Gemini CLI / Antigravity | `gemini-extension.json`, Agent Skill | `gemini skills install` or extension install |
| OpenCode | standard Agent Skill | `~/.agents/skills` or `~/.config/opencode/skills` |
| Windsurf | `.windsurf/rules/combover.md` adapter | repo rule plus canonical skill |
| Qoder | `.qoder/rules/combover.md` adapter | repo rule plus canonical skill |
| Generic agents | `AGENTS.md` + Agent Skill | point the harness at `skills/combover/` |

The fallback installers copy the same canonical skill into the common user-level skill directories. They do not modify shell profiles or application settings.
