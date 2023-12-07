[CmdletBinding()]
param(
    [switch] $install, [switch] $activate, [switch] $deactivate
)

$REQUIREMENTS = "$env:DEVENV\lib\pip_requirements.txt"
$TARGET = "$env:DEVENV\devenv\python"


function activateVenv
{
    if (-Not (Test-Path $TARGET)) {createVenv}
    & "$TARGET\Scripts\Activate.ps1"
}


function deactivateVenv {if ($env:VIRTUAL_ENV) {deactivate}}


function createVenv
{
    if (Test-Path $TARGET) {Remove-Item $TARGET -Force -Recurse > $null}
    python -m venv $TARGET

    activateVenv

    pip install -r $REQUIREMENTS --disable-pip-version-check

    $pipInstallFailed = -not $?
    deactivateVenv

    if ($pipInstallFailed) {
        Write-Host "Failed to install PIP packages."

        exit 1
    }

    Write-Host "PIP packages installed as per requirements."
}


if ($install) {createVenv}
elseif ($activate) {activateVenv}
elseif ($deactivate) {deactivateVenv}
