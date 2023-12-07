if (-not $env:DEVENV) {& "$PSScriptRoot\setup.ps1"}
if ($LASTEXITCODE) {Write-Host "Build failed."; exit 1}


$BUILD = "$env:DEVENV\build"
$RELEASE = "$BUILD\release\gscan"
$CONFIG = "$env:DEVENV\config"
$RESOURCES = "$env:DEVENV\resources"
$SRC = "$env:DEVENV\src"
$TEST_BUILD = "$BUILD\tests"
$TESTS = "$env:DEVENV\tests"


Clear-Host; Write-Host "Build started."

if (Test-Path $BUILD) {Remove-Item $BUILD -Force -Recurse > $null}
New-Item $BUILD -ItemType Directory > $null 

# Release.
New-Item $RELEASE -ItemType Directory > $null

Copy-Item $SRC "$RELEASE/bin" -Recurse > $null
Copy-Item $CONFIG $RELEASE -Recurse > $null
Copy-Item $RESOURCES $RELEASE -Recurse > $null
Write-Host "Release build complete."

# Tests.
New-Item $TEST_BUILD -ItemType Directory > $null
Copy-Item "$TESTS/*" $TEST_BUILD -Recurse > $null

Write-Host "Tests build complete."
Write-Host "Build complete."
