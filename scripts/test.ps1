[CmdletBinding()]
param ([string[]] $specific)

if (-not $env:DEVENV) {& "$PSScriptRoot\setup.ps1"}

$PYTHON_VENV = "$env:DEVENV\tools\python_venv.ps1"

Write-Host "Starting tests."
if (-Not $specific) {$specific = @()}

Push-Location "$env:DEVENV\tests"
& $PYTHON_VENV -activate

python test_runner.py $specific

& $PYTHON_VENV -deactivate
Pop-Location
