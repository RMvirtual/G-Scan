if (-not $env:DEVENV) {& "$PSScriptRoot\setup.ps1"}

$PYTHON_VENV = "$env:DEVENV\tools\python_venv.ps1"


Write-Host "Running application from source code."

& $PYTHON_VENV -activate
$env:GSCAN_ROOT = $env:DEVENV

python.exe "$env:DEVENV\src\main.py"

$env:GSCAN_ROOT = $NULL
& $PYTHON_VENV -deactivate
