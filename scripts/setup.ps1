[CmdletBinding()]
param([switch] $reinstall)


if ($reinstall) {& "$PSScriptRoot\..\tools\setup\install.ps1"}
else {& "$PSScriptRoot\..\tools\setup\launch.ps1"}

if ($LASTEXITCODE) {
    Write-Host "Configuration setup failed."

    exit 1
}

Clear-Host; Write-Host "Development environment established."
Set-Location "$env:DEVENV\scripts"

exit 0
