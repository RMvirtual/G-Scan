& "$PSScriptRoot\working_directory.ps1"

$PYTHON_VENV = "$env:DEVENV\tools\python_venv.ps1"
$TARGET = "$env:DEVENV\.venv"


Write-Host "Installing development environment." `
    "Please ensure VS code is closed so as not to lock up the virtual " `
    "environment interpreter from being removed."

if (Test-Path $TARGET) {Remove-Item $TARGET -Recurse -Force > $null}
New-Item $TARGET -ItemType Directory > $null

& $PYTHON_VENV -install
