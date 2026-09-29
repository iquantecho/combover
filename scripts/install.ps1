param(
  [ValidateSet("all", "agents", "claude", "cursor", "gemini", "opencode")]
  [string]$Target = "all"
)

$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Source = Join-Path $Root "skills/combover"

function Install-Skill([string]$Destination) {
  $Parent = Split-Path -Parent $Destination
  New-Item -ItemType Directory -Force -Path $Parent | Out-Null
  if (Test-Path $Destination) { Remove-Item -Recurse -Force $Destination }
  Copy-Item -Recurse -Force $Source $Destination
  Write-Host "installed: $Destination"
}

$Targets = @{
  agents   = Join-Path $HOME ".agents/skills/combover"
  claude   = Join-Path $HOME ".claude/skills/combover"
  cursor   = Join-Path $HOME ".cursor/skills/combover"
  gemini   = Join-Path $HOME ".gemini/skills/combover"
  opencode = Join-Path $HOME ".config/opencode/skills/combover"
}

if ($Target -eq "all") {
  foreach ($Name in @("agents", "claude", "cursor", "gemini", "opencode")) {
    Install-Skill $Targets[$Name]
  }
} else {
  Install-Skill $Targets[$Target]
}
