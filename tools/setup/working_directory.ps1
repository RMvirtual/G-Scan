$env:DEVENV = $null

$workingDirectory = Resolve-Path "$PSScriptRoot\..\.."
$expectedPath = "$workingDirectory\tools\setup\working_directory.ps1"

if (-not (Test-Path $expectedPath)) {
    Write-Host "Could not validate working directory of $workingDirectory."

    exit 1
}

$env:DEVENV = $workingDirectory

exit 0