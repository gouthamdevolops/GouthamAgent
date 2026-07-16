# Changelog

All notable changes to the **GouthamAgent** project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.2.0] - 2026-07-16
### Added
- Created complete documentation suite under `docs/` (`Architecture.md`, `ExecutionFlow.md`, `Features.md`, `ProjectStructure.md`, `Setup.md`, `SampleOutputs.md`).
- Added `docs/Contributing.md` specifying developer guidelines.
- Created `tests/` directory with `test_sanitization.py` and `test_prompts.py` using Python's standard `unittest` framework (zero-dependency).
- Added GitHub repository templates (`.github/ISSUE_TEMPLATE/` for bug reports and feature requests, and `.github/PULL_REQUEST_TEMPLATE.md`).
- Added GitHub Actions workflow configuration `.github/workflows/ci.yml` for automated checking.
- Created repository helper configurations: `.gitignore`, `.env.example`, `requirements.txt`, and `pyproject.toml`.
- Added MIT license file.

### Improved
- Completely overhauled [README.md](file:///D:/Goutham_DataAgentBench/README.md) with modern badges, banners, and execution flow charts.
- Added comprehensive type hints and module/method-level docstrings inside [Source_Code/DataAgent.py](file:///D:/Goutham_DataAgentBench/Source_Code/DataAgent.py) and [Source_Code/GouthamAgent.py](file:///D:/Goutham_DataAgentBench/Source_Code/GouthamAgent.py).
- Improved overall code readability and self-documentation comments in the source files.

---

## [1.1.0] - 2026-07-01
### Added
- Implemented [Source_Code/GouthamAgent.py](file:///D:/Goutham_DataAgentBench/Source_Code/GouthamAgent.py) to provide a custom subclass of `DataAgent` with refined rules for SQLite JSON extraction and schema-safeties.
- Added variable name sanitization logic in [Source_Code/DataAgent.py](file:///D:/Goutham_DataAgentBench/Source_Code/DataAgent.py) to replace dashes in LLM-generated tool call IDs with underscores, avoiding sandbox `SyntaxError` crashes.
- Extended `run_agent.py` CLI options by introducing the `--agent` parameter to select the active agent dynamically.
- Configured Gemini warning statements in [Source_Code/prompt_builder.py](file:///D:/Goutham_DataAgentBench/Source_Code/prompt_builder.py) to mitigate namespace prefix errors during tool requests.

### Fixed
- Fixed runtime sandbox crashes caused by OpenRouter tool call ID dashes inside python code execution scopes.
- Fixed context overflow errors by adjusting result preview constraints.

---

## [1.0.0] - 2026-06-15
### Added
- Initial setup and replication files based on the DataAgentBench scaffolding.
- Registered standard tools: `list_db`, `query_db`, `execute_python`, and `return_answer`.
- Established logging structures for conversation histories (`final_agent.json` and jsonl files).
