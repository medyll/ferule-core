# Uninstall watchdog from Windows Task Scheduler

$taskName = "openclaw-watchdog"

if (Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
    Write-Host "Watchdog task '$taskName' removed."
} else {
    Write-Host "Watchdog task '$taskName' not found."
}
