if (-not $env:DEVENV) {& "$PSScriptRoot\setup.ps1"}
if ($LASTEXITCODE) {Write-Host "Test environment setup failed."; exit 1}

$TESTS = "$env:DEVENV\build\tests"
$PYTHON_VENV = "$env:DEVENV\tools\python.ps1"


Clear-Host; Write-Host "Starting tests."

Push-Location $TESTS
& $PYTHON_VENV -activate

python test_runner.py

& $PYTHON_VENV -deactivate
Pop-Location
