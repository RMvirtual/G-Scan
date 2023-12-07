if (-not $env:DEVENV) {& "$PSScriptRoot\..\tools\setup\working_directory.ps1"}

if ($LASTEXITCODE) {
    Write-Host "Preliminary setup configuration failed."

    exit 1
}

exit 0