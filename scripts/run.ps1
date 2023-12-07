if (-not $env:DEVENV) {& "$PSScriptRoot\setup.ps1"}
if ($LASTEXITCODE) {Write-Host "Run failed."; exit 1}

$TARGET = "$env:DEVENV"

