# Execution Flow & Tool Calling

This document explains the runtime execution loop of **GouthamAgent** and describes how tools are requested, executed, and fed back into the agent context.

---

## Agent Execution Loop

The execution follows a multi-step agentic sequence. Below is a diagram illustrating the flow from user input to final validation.

```mermaid
sequenceDiagram
    autonumber
    actor User as Developer / CLI
    participant Runner as run_agent.py
    participant Agent as GouthamAgent
    participant LLM as LLM (OpenRouter)
    participant Tools as Tool Handlers
    participant Sandbox as Docker Python Sandbox
    
    User->>Runner: Execute command with --agent GouthamAgent
    Runner->>Agent: Instantiate GouthamAgent
    Agent->>Agent: Load user query and DB config
    Agent->>Agent: Construct System Prompt & User Message
    
    rect rgb(240, 248, 255)
        note right of Agent: Loop until return_answer called or max iterations reached
        Agent->>LLM: Send conversation history
        LLM-->>Agent: Return tool call requests (e.g. query_db, execute_python)
        
        alt Tool is query_db or list_db
            Agent->>Tools: Dispatch to Database Tool
            Tools->>Tools: Execute query on SQLite/DuckDB
            Tools-->>Agent: Return data or save to JSON if too large
        else Tool is execute_python
            Agent->>Agent: Sanitize tool call ID (dashes to underscores)
            Agent->>Tools: Dispatch code & variables to ExecTool
            Tools->>Sandbox: Execute code with SmartVariable wrappers
            Sandbox-->>Tools: Print result in strict format
            Tools-->>Agent: Return JSON string
        end
        Agent->>Agent: Append results to message history
    end
    
    Agent->>LLM: Send history with final analysis data
    LLM-->>Agent: Call return_answer(answer)
    Agent->>Runner: Terminate and return final answer
    Runner->>Runner: Write final_agent.json and validation logs
    Runner-->>User: Output final result
```

---

## Tool Calling Flow

When the LLM issues a tool call, GouthamAgent parses and routes the request. Large database queries and Python script variables require special handling to fit within context limits.

```mermaid
graph TD
    Start([LLM requests Tool Call]) --> CheckName{Tool Name?}
    
    CheckName -->|list_db| ListDB[Get DB schema tables] --> ReturnResult[Format result & return to agent]
    CheckName -->|query_db| QueryDB[Run SQL/Mongo query] --> CheckSize{Result size > 2000 chars?}
    
    CheckSize -->|Yes| SaveFile[Save to file_storage/*.json] --> ReturnPreview[Return preview & file path key]
    CheckSize -->|No| ReturnDirect[Return JSON representation directly]
    
    CheckName -->|execute_python| ExecPython[Inject env variables]
    ExecPython --> SanitizeKeys[Replace dashes in tool IDs with underscores]
    SanitizeKeys --> BuildContext[Generate python setup code with SmartVariable wrappers]
    BuildContext --> RunDocker[Run python in isolated Docker container]
    RunDocker --> ParseOutput[Parse print output for __RESULT__ marker]
    ParseOutput --> ReturnResult
    
    CheckName -->|return_answer| ReturnAns[Set final_result & trigger termination] --> ReturnResult
```

### Detailed Tool Specifications

1. **`list_db`**:
   - Lists all table or collection names in a target database.
   - Used during early iterations to learn the database schema structure before crafting SQL/Mongo queries.

2. **`query_db`**:
   - Executes queries on the database (SQLite or DuckDB).
   - If the serialized query output exceeds `PREVIEW_LENGTH` (2,000 characters), it writes the full payload as a JSON file in `file_storage/` and sends a preview alongside the file path back to the agent.

3. **`execute_python`**:
   - Executes custom Python code to transform and merge tables.
   - Code runs inside the isolated Docker sandbox environment.
   - Variables referencing large file paths are wrapped in `SmartVariableList`/`SmartVariableDict` objects, preventing memory overflow.

4. **`return_answer`**:
   - Terminates the agent loop by supplying the final plain-text response back to the user.
