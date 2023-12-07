if (-not $env:DEVENV) {& "$PSScriptRoot\setup.ps1"}

if ($LASTEXITCODE) {
    Write-Host "Preliminary setup configuration failed."

    exit 1
}

$BUILD = "$env:DEVENV\build"
$RELEASE = "$BUILD\release"
$TESTS = "$BUILD\tests"


if (Test-Path $BUILD) {Remove-Item $BUILD -Force -Recurse > $null}

New-Item $BUILD -ItemType Directory 
New-Item $RELEASE -ItemType Directory
New-Item $TESTS -ItemType Directory

Write-Host "Build complete."
