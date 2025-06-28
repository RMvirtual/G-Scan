[CmdletBinding()]
param ([string[]] $specific)

# Pre-setup checks.
if (-Not $env:DEVENV) {
    & "$PSScriptRoot\setup.ps1"

    if (-Not $env:DEVENV) {
        exit 1
    }
}


# Run tests.
Write-Host "Running tests."
Push-Location "$env:DEVENV\tests"
$venv = "$env:DEVENV\scripts\python_venv.ps1"
& $venv -activate

try {
    if (-Not $specific) {$specific = @()}
    python test_runner.py $specific
}

finally {
    & $venv -deactivate
    Pop-Location
}
