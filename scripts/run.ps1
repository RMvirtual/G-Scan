[CmdletBinding()]
param([switch] $src, [switch] $exe)

# Pre-setup checks.
if (-Not $env:DEVENV) {
    & "$PSScriptRoot\setup.ps1"

    if (-Not $env:DEVENV) {
        exit 1
    }
}


# Run application.
if ($src -and $exe) {
    Write-Host "Must select only one option of -src or -exe."
    
    exit 1
}

if (-not $src -and -not $exe) {
    $src = $true
}

if ($src) {
    Write-Host "Running application from source code."

    $env:PYTHONPATH = "$env:DEVENV\src"
    $venv = "$env:DEVENV\scripts\python_venv.ps1"
    & $venv -activate
    
    $env:GSCAN_ROOT = $env:DEVENV
    python.exe "$env:DEVENV\src\controllers\app.py"

    $env:GSCAN_ROOT = $NULL
    & $venv -deactivate
}

elseif ($exe) {
    $exeBinary = "$env:DEVENV\dist\gscan\gscan.exe"
    
    if (-not (Test-Path $exeBinary)) {
        Write-Host "Cannot run exe file $exeBinary as it does not exist."

        exit 1
    }

    & $exeBinary
}