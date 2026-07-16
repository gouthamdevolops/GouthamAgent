# Project Structure

This document details the file and folder layout of the **GouthamAgent** repository and explains the purpose of each codebase file.

---

## Directory Layout

The repository is structured as a clean, modular python project. The directories and files inside `D:\Goutham_DataAgentBench` are organized as follows:

```text
D:\Goutham_DataAgentBench
├── .github/                  # CI/CD workflows folder
│   └── workflows/
│       └── ci.yml            # GitHub Actions runner configuration
├── .gitignore                # Version control file exclusions
├── .env.example              # Environment variables template
├── requirements.txt          # Python dependency list
├── pyproject.toml            # Formatter (Ruff) & test framework settings
├── LICENSE                   # Open-source MIT License
├── README.md                 # Project entry point and overview
├── docs/                     # Detailed architectural and usage documentation
│   ├── Architecture.md
│   ├── ExecutionFlow.md
│   ├── ProjectStructure.md
│   ├── Features.md
│   ├── Setup.md
│   └── SampleOutputs.md
├── Source_Code/              # Core codebase files
│   ├── DataAgent.py          # Modified orchestration base agent
│   ├── GouthamAgent.py       # Custom agent prompt and logical subclass
│   ├── prompt_builder.py     # Prompt selector and LLM adaptations
│   └── run_agent.py          # Runner CLI with switch flags
├── tests/                    # Zero-dependency Unit Test Suite
│   ├── __init__.py
│   ├── test_sanitization.py  # Tests sandbox string sanitization logic
│   └── test_prompts.py       # Tests model-specific prompt construction
├── Validation/               # Benchmarking results and summary
│   ├── Validation_Summary.md # Analysis of computed result vs expected result
│   └── final_agent.json      # Complete trace log from a benchmark execution
└── Writeup/                  # Engineering review
    └── Technical_Write_up.md # Key challenges, solutions, and takeaways
```

---

## Component Breakdown

### 1. Source_Code/
Contains the modified files that integrate with the `DataAgentBench` framework:
- **[GouthamAgent.py](file:///D:/Goutham_DataAgentBench/Source_Code/GouthamAgent.py)**: Contains the main system prompt containing critical SQLite rules (SQLite double-quotes quirk, JSON parsing) and Python scripting print guidelines.
- **[DataAgent.py](file:///D:/Goutham_DataAgentBench/Source_Code/DataAgent.py)**: Contains the orchestration code. Features a key modification where dashes in tool call IDs (common in OpenRouter providers) are replaced with underscores to prevent syntax crashes when loaded inside Python environments.
- **[prompt_builder.py](file:///D:/Goutham_DataAgentBench/Source_Code/prompt_builder.py)**: Configures instructions based on model names (Gemini-2.5-flash, GPT, Claude, Kimi). Integrates solutions to bypass model-specific errors.
- **[run_agent.py](file:///D:/Goutham_DataAgentBench/Source_Code/run_agent.py)**: The entry point to run evaluations. Added a `--agent` flag to easily select the custom `GouthamAgent` at runtime.

### 2. Validation/
Houses details of model evaluation:
- **[Validation_Summary.md](file:///D:/Goutham_DataAgentBench/Validation/Validation_Summary.md)**: Summarizes database verification results on the `GITHUB_REPOS` dataset.
- **[final_agent.json](file:///D:/Goutham_DataAgentBench/Validation/final_agent.json)**: The serialized agent state, including conversation history, final answers, token costs, and duration metadata.

### 3. Writeup/
Contains reflective documentation:
- **[Technical_Write_up.md](file:///D:/Goutham_DataAgentBench/Writeup/Technical_Write_up.md)**: A retrospective detailing challenges faced, including syntax crashes in sandboxes, API limits, validation mismatches, and how they were solved.

### 4. tests/
Contains the test suite running standard unit verification checks:
- **[test_sanitization.py](file:///D:/Goutham_DataAgentBench/tests/test_sanitization.py)**: Verifies that tool call IDs are safely converted to Python-compatible variable names.
- **[test_prompts.py](file:///D:/Goutham_DataAgentBench/tests/test_prompts.py)**: Confirms prompt customization rules operate properly across different LLM architectures (Gemini, GPT, Claude).

### 5. Workspace Configuration Files
- **.gitignore**: Standardizes folder exclusions for credentials, caches, run logs, and SQL/DuckDB binaries.
- **.env.example**: Supplies a sample template of local variables without exposing secrets.
- **requirements.txt**: Declares explicit dependency versions to maximize reproducibility.
- **pyproject.toml**: Standardizes configurations for code format checking and pytest run patterns.
- **LICENSE**: Provides an MIT Open Source license configuration.
- **.github/workflows/ci.yml**: Configures GitHub Actions CI to run tests and lints automatically on commits.

---

## Framework Integration

This repository contains the custom source files and validation assets of **GouthamAgent**. To execute these scripts in a benchmark run, these files should override or be referenced by the parent **DataAgentBench** framework repository:
- `Source_Code/GouthamAgent.py` and `Source_Code/DataAgent.py` are mapped into the framework's `common_scaffold/` module.
- `Source_Code/run_agent.py` overrides the root `run_agent.py` in the benchmark.
