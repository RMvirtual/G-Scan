[CmdletBinding()]
param([switch] $clean)

if (-Not $env:DEVENV) {& "$PSScriptRoot\setup.ps1"}

$PYTHON_VENV = "$env:DEVENV\tools\python_venv.ps1"

Write-Host "Building release."

Push-Location $env:DEVENV
& $PYTHON_VENV -activate

pyinstaller "$env:DEVENV\src\main.py" --name "gscan" --onedir --noconfirm `
    --add-data "$env:DEVENV\data\*.json:data" `
    --add-data "$env:DEVENV\data\images:data\images" `
    $(if ($clean) {"--clean"})

& $PYTHON_VENV -deactivate
Pop-Location