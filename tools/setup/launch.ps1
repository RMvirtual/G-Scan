& "$PSScriptRoot\working_directory.ps1"
if ($LASTEXITCODE) {Write-Host "Launch failed."; exit 1}

$INSTALL_SCRIPT = "$env:DEVENV\tools\setup\install.ps1"
$TARGET = "$env:DEVENV\devenv"


if (-Not (Test-Path $TARGET)) {& $INSTALL_SCRIPT}
exit 0  
