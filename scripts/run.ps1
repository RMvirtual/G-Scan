if (-not $env:DEVENV) {& "$PSScriptRoot\setup.ps1"}


$PYTHON_VENV = "$env:DEVENV\tools\python_venv.ps1"


Clear-Host; Write-Host "Running."

& $PYTHON_VENV -activate
python.exe "$env:DEVENV\src\main.py"
& $PYTHON_VENV -deactivate
