# start.ps1 — Quick start for local testing
# Run from: ferule-core/core-ferule-engine/

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot

Set-Location $Root

if (-not (Test-Path "venv")) {
    Write-Host "Creating venv..."
    python -m venv venv
}

& "venv\Scripts\Activate.ps1"
pip install -r requirements.txt --quiet

Write-Host "Starting Core Ferule Engine on http://localhost:8000"
python -m core.engine
