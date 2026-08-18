Remove-Item -Recurse -Force .\allure-results -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path .\allure-results | Out-Null

$envArgs = @()
if (Test-Path .\.env) {
    Get-Content .\.env | ForEach-Object {
        if ($_ -match '^\s*#' -or $_ -match '^\s*$') { return }
        
        if ($_ -match '^([^=]+)=(.*)') {
            $key = $matches[1].Trim()
            $value = $matches[2].Trim().Trim('"').Trim("'")
            $envArgs += "-e", "$key=$value"
        }
    }
} else {
    Write-Host "[WARNING] .env file not found!" -ForegroundColor Yellow
}

Write-Host "[INFO] Starting tests..." -ForegroundColor Green
docker run --rm @envArgs allure-tests

Write-Host "[OK] Tests completed." -ForegroundColor Green