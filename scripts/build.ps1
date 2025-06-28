[CmdletBinding()]
param([switch] $clean)

# Pre-setup checks.
if (-Not $env:DEVENV) {
    & "$PSScriptRoot\setup.ps1"

    if (-Not $env:DEVENV) {
        exit 1
    }
}


# Build application.
Write-Host "Building application."
Push-Location $env:DEVENV
$venv = "$env:DEVENV\scripts\python_venv.ps1"
& $venv -activate

try {
    pyinstaller "$env:DEVENV\src\controllers\app.py" `
        --name "gscan" --onedir --noconfirm `
        --add-data "$env:DEVENV\data\*.json:data" `
        --add-data "$env:DEVENV\data\images:data\images" `
        $(if ($clean) {"--clean"})
}

finally {
    & $venv -deactivate
    Pop-Location
}