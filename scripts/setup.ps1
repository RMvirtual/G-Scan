[CmdletBinding()]
param([switch] $reinstall)

$env:DEVENV = $null

$rootDir = Resolve-Path "$PSScriptRoot\.."
$expectedPath = "$rootDir\scripts\setup.ps1"

if (-not (Test-Path $expectedPath)) {
    Write-Host "Could not validate working directory of $rootDir."

    exit 1
}

$env:DEVENV = $rootDir
$venv = "$env:DEVENV\.venv"

if ($reinstall -Or (-Not (Test-Path $venv))) {
    $PYTHON_VENV = "$env:DEVENV\scripts\python_venv.ps1"

    Write-Host "Installing Python virtual environment." `
        "Please ensure VS code is closed so as not to lock up the virtual" `
        "environment interpreter from being removed."

    if (Test-Path $venv) {Remove-Item $venv -Recurse -Force > $null}
    & $PYTHON_VENV -install
}

if (-Not $?) {
    Write-Host "Configuration setup failed."; 
    
    exit 1
}

Write-Host "Development environment established."
Set-Location "$env:DEVENV\scripts"
