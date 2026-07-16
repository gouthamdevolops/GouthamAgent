# Technical Write-up

I implemented GouthamAgent as my custom agent for the GITHUB_REPOS database task in the DataAgentBench benchmark. Below is a write-up of what I did, the challenges I ran into, and how I fixed them.

## What I implemented
* I created GouthamAgent.py as a custom agent based on DataAgent.
* I wrote a custom prompt for GouthamAgent with rules on how to write SQLite queries and format Python code.
* I modified run_agent.py to add a CLI flag (`--agent`) to choose between GouthamAgent and the default agent.
* I added a fix in DataAgent.py to clean up variable names inside the Python sandbox.

## Why I made those changes
* The default agent prompt did not warn the model about SQL syntax quirks or the exact print format needed by the sandbox.
* The CLI parameter lets the runner script switch agents dynamically without hardcoding.
* The variable cleaning was needed to prevent sandbox runtime crashes when loading database query outputs.

## Execution Flow
The runner script starts and creates GouthamAgent. The agent reads the user query and asks the LLM for the next step. If the LLM needs database records or wants to run code, it requests a tool. The framework runs the database query or Python script locally, saves large results to a file, and sends the output back to the agent. This loop repeats until the agent calculates the final answer and calls the tool to return it, after which the benchmark generates the execution logs (`final_agent.json`, `tool_calls.jsonl`, and `llm_calls.jsonl`).

## Challenges I faced
* **Sandbox syntax crashes:** The OpenRouter API returned tool IDs with dashes. The framework used these raw IDs as Python variable names inside the sandbox, which caused a SyntaxError because Python treats dashes as subtraction.
* **API credit limits:** The default token settings were too large, which blocked requests with billing errors (HTTP 402).
* **Validation results:** During validation, I noticed that the expected result from the validation script did not match the result calculated from the downloaded database. I verified the database directly and documented this observation in my validation summary.

## How I solved them
* **Replacing dashes with underscores:** I modified DataAgent.py to replace all dashes in the sandbox variable keys with underscores so they are treated as valid variable names.
* **Switching models and limits:** I ran the agent using the free google/gemma-4-31b-it:free model on OpenRouter and reduced the preview size of query results in prompt_builder.py.
* **Verifying database counts:** I wrote a Python script to query the SQLite and DuckDB files directly. I verified that the database contains 128 README files (17 with copyright, or 19 depending on filtering), making 16.83% the correct calculation for the downloaded databases. I documented this validation observation in the summary.

## What I learned
* I learned that dynamically generated variables must be sanitized before passing them to a Python interpreter.
* I learned how to manage context size and use free API models to avoid credit limits.
* I realized that when test scripts fail, querying the database directly is the best way to verify if my agent's math is correct.
