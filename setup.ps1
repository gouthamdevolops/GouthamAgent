# setup.ps1 - Automates overlay setup of GouthamAgent on top of the DataAgentBench framework on Windows.

$ErrorActionPreference = "Stop"

$FrameworkDir = "DataAgentBench"
$FrameworkRepo = "https://github.com/DataAgentBench/DataAgentBench.git"

Write-Host "=== GouthamAgent Setup Utility ===" -ForegroundColor Green

# 1. Clone the parent framework repository if not already present
if (-not (Test-Path $FrameworkDir)) {
    Write-Host "Cloning DataAgentBench framework..." -ForegroundColor Cyan
    git clone $FrameworkRepo $FrameworkDir
} else {
    Write-Host "DataAgentBench folder already exists, skipping clone." -ForegroundColor Yellow
}

# 2. Overlay GouthamAgent custom files
Write-Host "Overlaying custom GouthamAgent files onto framework..." -ForegroundColor Cyan
Copy-Item "Source_Code/GouthamAgent.py" "$FrameworkDir/common_scaffold/GouthamAgent.py" -Force
Copy-Item "Source_Code/DataAgent.py" "$FrameworkDir/common_scaffold/DataAgent.py" -Force
Copy-Item "Source_Code/prompt_builder.py" "$FrameworkDir/common_scaffold/prompt_builder.py" -Force
Copy-Item "Source_Code/run_agent.py" "$FrameworkDir/run_agent.py" -Force

Write-Host "=== Setup Completed Successfully ===" -ForegroundColor Green
Write-Host "Next steps:"
Write-Host "  1. cd $FrameworkDir"
Write-Host "  2. Set up your Python virtual environment and install dependencies (pip install -r requirements.txt)"
Write-Host "  3. Configure your API key in .env (see .env.example)"
Write-Host "  4. Execute runs using: python run_agent.py --agent GouthamAgent --dataset GITHUB_REPOS --query_id 1"
