if (-not $env:DEVENV) {& "$PSScriptRoot\setup.ps1"}


$PYTHON_VENV = "$env:DEVENV\tools\python_venv.ps1"


Clear-Host; Write-Host "Should run here."
& $PYTHON_VENV -activate
& $PYTHON_VENV -deactivate
