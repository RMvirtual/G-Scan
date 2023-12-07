if (-not $env:DEVENV) {& "$PSScriptRoot\setup.ps1"}
if ($LASTEXITCODE) {Write-Host "Build failed."; exit 1}


$BUILD = "$env:DEVENV\build"
$RELEASE = "$BUILD\release"
$SRC = "$env:DEVENV\src"
$TEST_BUILD = "$BUILD\tests"
$TESTS = "$env:DEVENV\tests"


Clear-Host; Write-Host "Build started."

if (Test-Path $BUILD) {Remove-Item $BUILD -Force -Recurse > $null}

New-Item $BUILD -ItemType Directory > $null 
New-Item $RELEASE -ItemType Directory > $null

Copy-Item $SRC "$RELEASE/gscan/bin" -Recurse > $null

Write-Host "Release build complete."

New-Item $TEST_BUILD -ItemType Directory > $null
Copy-Item "$TESTS/*" $TEST_BUILD -Recurse > $null

Write-Host "Tests build complete."
Write-Host "Build complete."
