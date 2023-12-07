& "$PSScriptRoot\working_directory.ps1"

$SETUP_SCRIPT = "$env:DEVENV\tools\setup\install.ps1"
$TARGET = "$env:DEVENV\devenv"


if (-Not (Test-Path $TARGET)) {& $SETUP_SCRIPT}
