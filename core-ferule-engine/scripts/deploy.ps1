# deploy.ps1 — Core Ferule Engine NSSM Service Installation
#
# Usage:
#   .\deploy.ps1 -Install    # Install service
#   .\deploy.ps1 -Uninstall  # Remove service
#   .\deploy.ps1 -Status     # Check service status
#
# Parameters:
#   -Config    Path to rules_config.yaml (default: config\rules_config.yaml)
#   -LogDir    Log directory (default: %APPDATA%\CoreFeruleEngine\logs)

param(
    [Parameter(Mandatory=$false)]
    [switch]$Install,
    
    [Parameter(Mandatory=$false)]
    [switch]$Uninstall,
    
    [Parameter(Mandatory=$false)]
    [switch]$Status,
    
    [Parameter(Mandatory=$false)]
    [string]$Config = "config\rules_config.yaml",
    
    [Parameter(Mandatory=$false)]
    [string]$LogDir = "$env:APPDATA\CoreFeruleEngine\logs"
)

$SERVICE_NAME = "CoreFeruleEngine"
$SERVICE_DISPLAY = "Core Ferule Engine"
$SERVICE_DESC = "Autonomous business rule engine for OpenClaw ecosystem"

# Paths
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$ENGINE_DIR = $SCRIPT_DIR
$PYTHON_SCRIPT = Join-Path $ENGINE_DIR "core\engine.py"
$CONFIG_PATH = Join-Path $ENGINE_DIR $Config

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Helper Functions
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

function Test-Admin {
    $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

function Test-NSSM {
    try {
        $null = Get-Command nssm -ErrorAction Stop
        return $true
    } catch {
        return $false
    }
}

function Install-Service {
    if (-not (Test-Admin)) {
        Write-Host "❌ Error: Administrator privileges required" -ForegroundColor Red
        exit 1
    }
    
    if (-not (Test-NSSM)) {
        Write-Host "❌ Error: NSSM not found. Install from https://nssm.cc/" -ForegroundColor Red
        Write-Host "   Or run: choco install nssm" -ForegroundColor Yellow
        exit 1
    }
    
    if (-not (Test-Path $PYTHON_SCRIPT)) {
        Write-Host "❌ Error: engine.py not found at $PYTHON_SCRIPT" -ForegroundColor Red
        exit 1
    }
    
    if (-not (Test-Path $CONFIG_PATH)) {
        Write-Host "❌ Error: Config not found at $CONFIG_PATH" -ForegroundColor Red
        exit 1
    }
    
    # Create log directory
    $null = New-Item -ItemType Directory -Force -Path $LogDir
    
    # Remove existing service if present
    $existing = Get-Service -Name $SERVICE_NAME -ErrorAction SilentlyContinue
    if ($existing) {
        Write-Host "⚠️  Service $SERVICE_NAME exists — removing..." -ForegroundColor Yellow
        nssm stop $SERVICE_NAME 2>$null
        nssm remove $SERVICE_NAME confirm 2>$null
    }
    
    # Install service
    Write-Host "📦 Installing $SERVICE_NAME..." -ForegroundColor Cyan
    $pythonExe = (Get-Command python).Source
    nssm install $SERVICE_NAME $pythonExe $PYTHON_SCRIPT --config $CONFIG_PATH
    
    # Configure service
    nssm set $SERVICE_NAME DisplayName $SERVICE_DISPLAY
    nssm set $SERVICE_NAME Description $SERVICE_DESC
    nssm set $SERVICE_NAME Start SERVICE_AUTO_START
    nssm set $SERVICE_NAME ObjectName LocalSystem
    
    # Set working directory
    nssm set $SERVICE_NAME AppDirectory $ENGINE_DIR
    
    # Set environment variables
    nssm set $SERVICE_NAME AppEnvironmentExtra "PYTHONPATH=$ENGINE_DIR`0LOG_DIR=$LogDir"
    
    # Configure restart on failure
    nssm set $SERVICE_NAME AppRestartDelay 5000
    
    # Start service
    Write-Host "🚀 Starting service..." -ForegroundColor Cyan
    Start-Service -Name $SERVICE_NAME
    
    # Verify
    $service = Get-Service -Name $SERVICE_NAME
    if ($service.Status -eq 'Running') {
        Write-Host "✅ Service installed and running" -ForegroundColor Green
        Write-Host "   Name: $SERVICE_NAME"
        Write-Host "   Config: $CONFIG_PATH"
        Write-Host "   Logs: $LogDir"
    } else {
        Write-Host "⚠️  Service installed but not running — check logs" -ForegroundColor Yellow
        Write-Host "   $LogDir"
    }
}

function Uninstall-Service {
    if (-not (Test-Admin)) {
        Write-Host "❌ Error: Administrator privileges required" -ForegroundColor Red
        exit 1
    }
    
    $existing = Get-Service -Name $SERVICE_NAME -ErrorAction SilentlyContinue
    if (-not $existing) {
        Write-Host "ℹ️  Service $SERVICE_NAME not found" -ForegroundColor Gray
        return
    }
    
    Write-Host "🗑️  Stopping and removing $SERVICE_NAME..." -ForegroundColor Cyan
    nssm stop $SERVICE_NAME 2>$null
    nssm remove $SERVICE_NAME confirm 2>$null
    
    Write-Host "✅ Service removed" -ForegroundColor Green
}

function Get-Status {
    $service = Get-Service -Name $SERVICE_NAME -ErrorAction SilentlyContinue
    if (-not $service) {
        Write-Host "ℹ️  Service $SERVICE_NAME not installed" -ForegroundColor Gray
        return
    }
    
    Write-Host "📊 Service Status:" -ForegroundColor Cyan
    Write-Host "   Name: $($service.Name)"
    Write-Host "   Display: $($service.DisplayName)"
    Write-Host "   Status: $($service.Status)" -ForegroundColor $(if ($service.Status -eq 'Running') { 'Green' } else { 'Yellow' })
    Write-Host "   StartType: $($service.StartType)"
    
    if ($service.Status -eq 'Running') {
        Write-Host "   PID: $((Get-Process -Id $service.ServiceProcessId -ErrorAction SilentlyContinue).Id)"
    }
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Main
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if ($Install) {
    Install-Service
} elseif ($Uninstall) {
    Uninstall-Service
} elseif ($Status) {
    Get-Status
} else {
    Write-Host "Core Ferule Engine Deployment Script"
    Write-Host ""
    Write-Host "Usage:"
    Write-Host "  .\deploy.ps1 -Install    # Install service"
    Write-Host "  .\deploy.ps1 -Uninstall  # Remove service"
    Write-Host "  .\deploy.ps1 -Status     # Check service status"
    Write-Host ""
    Write-Host "Options:"
    Write-Host "  -Config    Config path (default: config\rules_config.yaml)"
    Write-Host "  -LogDir    Log directory (default: %APPDATA%\CoreFeruleEngine\logs)"
}
