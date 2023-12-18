if (-not $env:DEVENV) {
    & "$PSScriptRoot\setup.ps1"

    if ($LASTEXITCODE) {Write-Host "Run failed."}
}


$PYTHON_VENV = "$env:DEVENV\tools\python.ps1"
$TARGET = "$env:DEVENV\build\release\gscan\bin"


Clear-Host; Write-Host "Running from Build."

Push-Location $TARGET
& $PYTHON_VENV -activate

python gui_launcher.py

& $PYTHON_VENV -deactivate
Pop-Location
