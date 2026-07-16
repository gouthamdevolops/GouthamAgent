#!/bin/bash
# setup.sh - Automates overlay setup of GouthamAgent on top of the DataAgentBench framework.

set -e

FRAMEWORK_DIR="DataAgentBench"
FRAMEWORK_REPO="https://github.com/DataAgentBench/DataAgentBench.git"

echo "=== GouthamAgent Setup Utility ==="

# 1. Clone the parent framework repository if not already present
if [ ! -d "$FRAMEWORK_DIR" ]; then
    echo "Cloning DataAgentBench framework..."
    git clone "$FRAMEWORK_REPO" "$FRAMEWORK_DIR"
else
    echo "DataAgentBench folder already exists, skipping clone."
fi

# 2. Overlay GouthamAgent custom files
echo "Overlaying custom GouthamAgent files onto framework..."
cp Source_Code/GouthamAgent.py "$FRAMEWORK_DIR/common_scaffold/GouthamAgent.py"
cp Source_Code/DataAgent.py "$FRAMEWORK_DIR/common_scaffold/DataAgent.py"
cp Source_Code/prompt_builder.py "$FRAMEWORK_DIR/common_scaffold/prompt_builder.py"
cp Source_Code/run_agent.py "$FRAMEWORK_DIR/run_agent.py"

echo "=== Setup Completed Successfully ==="
echo "Next steps:"
echo "  1. cd $FRAMEWORK_DIR"
echo "  2. Set up your Python virtual environment and install dependencies (pip install -r requirements.txt)"
echo "  3. Configure your API key in .env (see .env.example)"
echo "  4. Execute runs using: python run_agent.py --agent GouthamAgent --dataset GITHUB_REPOS --query_id 1"
