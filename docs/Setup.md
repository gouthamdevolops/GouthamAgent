# Installation & Setup Guide

This document explains the prerequisites, installation steps, and CLI usage instructions to get **GouthamAgent** up and running on your local machine.

---

## Prerequisites

Before setting up GouthamAgent, make sure you have the following installed on your system:

1. **Python 3.12+**
2. **Docker Desktop** (Required for the `execute_python` isolated execution sandbox)
3. **OpenRouter API Key** (or OpenAI API Key)

---

## Installation Steps

### Option A: Automated Setup (Recommended)
To automatically clone the underlying framework and overlay GouthamAgent's custom files, run the setup script for your platform from this repository's root directory:

**On Linux/macOS (Bash):**
```bash
chmod +x setup.sh
./setup.sh
```

**On Windows (PowerShell):**
```powershell
./setup.ps1
```

The script will clone `DataAgentBench/` and overlay GouthamAgent's custom Python files automatically. After it completes, change directory to `DataAgentBench/` to continue.

### Option B: Manual Setup
If you prefer to configure the framework manually, perform the following steps:
1. **Clone the Benchmark**:
   ```bash
   git clone https://github.com/DataAgentBench/DataAgentBench.git
   cd DataAgentBench
   ```
2. **Copy Code Files**:
   Manually copy GouthamAgent's files from the `Source_Code/` directory into the cloned repository:
   - Copy [Source_Code/GouthamAgent.py](file:///D:/Goutham_DataAgentBench/Source_Code/GouthamAgent.py) into `common_scaffold/` (replacing the default).
   - Copy [Source_Code/DataAgent.py](file:///D:/Goutham_DataAgentBench/Source_Code/DataAgent.py) into `common_scaffold/` (replacing the default).
   - Copy [Source_Code/prompt_builder.py](file:///D:/Goutham_DataAgentBench/Source_Code/prompt_builder.py) into `common_scaffold/` (replacing the default).
   - Copy [Source_Code/run_agent.py](file:///D:/Goutham_DataAgentBench/Source_Code/run_agent.py) into the root folder (replacing the default).

### Step 3: Setup Virtual Environment & Dependencies
Create a virtual environment and install the required dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
pip install -r requirements.txt
```

Ensure the Docker environment is running:
```bash
docker pull python-data:3.12
```

### Step 4: Environment Variables
Create a `.env` file in the root of the project and insert your API key:
```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

---

## CLI Usage Instructions

Execute the benchmark queries using the runner script:

```bash
python run_agent.py --dataset <dataset_name> --query_id <query_id> --agent GouthamAgent [options]
```

### CLI Arguments:

| Argument | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `--dataset` | `str` | *Required* | Name of the dataset to run (see list below). |
| `--query_id` | `int` | *Required* | ID number of the specific benchmark query. |
| `--agent` | `str` | `DataAgent` | Choose between `DataAgent` (default) and `GouthamAgent` (custom). |
| `--llm` | `str` | `gpt-4o-mini` | LLM model to call (e.g. `google/gemma-2-9b-it:free`, `gpt-4o`). |
| `--iterations`| `int` | `100` | Maximum number of agent loop iterations allowed. |
| `--use_hints` | `flag`| `False` | Includes DB schema tips and hints in system prompt if set. |
| `--root_name` | `str` | `datetime` | Custom directory name under logs/ for saving execution traces. |

### Valid Datasets:
- `bookreview`
- `crmarenapro`
- `DEPS_DEV_V1`
- `GITHUB_REPOS`
- `googlelocal`
- `PANCANCER_ATLAS`
- `PATENTS`
- `stockindex`
- `stockmarket`
- `yelp`
- `agnews`
- `music_brainz_20k`

### Example Commands:

Run query 1 of the `GITHUB_REPOS` dataset using `GouthamAgent` with a free Gemma model:
```bash
python run_agent.py --dataset GITHUB_REPOS --query_id 1 --agent GouthamAgent --llm google/gemma-4-31b-it:free
```

Run with schema hints enabled:
```bash
python run_agent.py --dataset GITHUB_REPOS --query_id 1 --agent GouthamAgent --use_hints
```
