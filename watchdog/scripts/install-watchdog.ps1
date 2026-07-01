# Install watchdog as a Windows Task Scheduler task
# Runs every 5 minutes, hidden, with highest privileges

$taskName = "openclaw-watchdog"
$scriptPath = "C:\Users\Mydde\.openclaw\workspace\core-ferule\watchdog\scripts\watchdog.mjs"
$nodePath = (Get-Command node).Source

$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 5)
$action = New-ScheduledTaskAction -Execute $nodePath -Argument $scriptPath
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType S4U -RunLevel Highest

Register-ScheduledTask -TaskName $taskName -Trigger $trigger -Action $action -Settings $settings -Principal $principal -Force

Write-Host "Watchdog task '$taskName' installed. Runs every 5 minutes."
