& "$PSScriptRoot\working_directory.ps1"

$PYTHON_VENV = "$env:DEVENV\tools\python.ps1"
$TARGET = "$env:DEVENV\devenv"


Write-Host "Installing development environment."

if (Test-Path $TARGET) {Remove-Item $TARGET -Recurse -Force > $null}
New-Item $TARGET -ItemType Directory > $null

& $PYTHON_VENV -install
