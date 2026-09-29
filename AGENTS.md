# Combover repository guidance

This repository packages the `combover` Agent Skill. The canonical behavior lives in `skills/combover/SKILL.md`; companion methods live in `skills/combover/references/`.

When a user explicitly invokes Combover or asks for knowledge-work simplification, load the canonical skill and only the companion reference relevant to that task. Do not duplicate the full skill into new adapter files. Keep vendor manifests thin and point them at the canonical `skills/` tree.

Combover is for knowledge work. Do not apply it as a coding style guide merely because an agent is editing this repository.
