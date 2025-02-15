[CmdletBinding()]
param([switch] $src, [switch] $exe)

if (-not $env:DEVENV) {& "$PSScriptRoot\setup.ps1"}

if ($src -and $exe) {
    Write-Host "Must select only one option of -src or -exe."
    exit 1
}

if (-not $src -and -not $exe) {$src = $true}

if ($src) {
    Write-Host "Running application from source code."

    $env:PYTHONPATH = "$env:DEVENV\src"
    $pythonVenv = "$env:DEVENV\tools\python_venv.ps1"
    & $pythonVenv -activate
    
    $env:GSCAN_ROOT = $env:DEVENV
    python.exe "$env:DEVENV\src\controllers\app.py"

    $env:GSCAN_ROOT = $NULL
    & $pythonVenv -deactivate
}

elseif ($exe) {
    $exeBinary = "$env:DEVENV\dist\gscan\gscan.exe"
    
    if (-not (Test-Path $exeBinary)) {
        Write-Host "Cannot run exe file $exeBinary as it does not exist."

        exit 1
    }

    & $exeBinary
}