# 🤖 Azure AI MCP Agent — Complete Project

This project demonstrates how to create and run an **Azure AI agent** capable of using a **MCP (Microsoft Content Platform) Tool** to interact with Microsoft’s official documentation.
The agent can receive user prompts, perform searches via the MCP tool, and display the complete conversation.

---

## 🧠 Main Features

* 🔗 Secure connection to an Azure AI project via `AgentsClient`.
* 🧩 Create and manage an intelligent agent (e.g., `gpt-4o`).
* 🧰 Integrate an **MCP tool** to query Microsoft documentation.
* 💬 Manage a conversation thread between the user and the agent.
* 🚀 Automatically execute a *run* with step and tool call display.
* 🧹 Automatically delete the agent after execution to prevent clutter.



## ⚙️ Prerequisites

Before starting, make sure you have:

* Python **3.9+** installed.
* An **Azure AI endpoint** and deployed model (`gpt-4o` or other).
* Valid Azure authentication via CLI, Visual Studio, or Managed Identity.
* Internet access so the agent can call the MCP server.

### 2️⃣ Create a virtual environment

#### Windows:

```bash
python -m venv labenv
labenv\Scripts\activate
```

#### Linux / macOS:

```bash
python -m venv labenv
source labenv/bin/activate
```

### 3️⃣ Install dependencies

If you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install packages directly:

```bash
pip install azure-ai-agents azure-identity python-dotenv
```

---

## 🔐 Configuration

Create a `.env` file in the project root with the following:

```env
PROJECT_ENDPOINT=https://<your-azure-endpoint>
MODEL_DEPLOYMENT_NAME=gpt-4o
```

> ⚠️ Never share your `.env` file publicly; it contains sensitive information.

---

## ▶️ Running the Script

Run the main script:

```bash
python main.py
```


## 📝 Detailed Explanation

### 1) Purpose

This script creates and runs an **Azure AI agent** that can call an **MCP tool**, send a user message to the agent thread, execute a **run**, display the steps, messages, and then delete the agent.

### 2) Import & Environment Variables

```python
import os
from dotenv import load_dotenv
```

* `os`: Access environment variables and system functions.
* `load_dotenv`: Loads variables from a `.env` file.

### 3) Merge Option (Optional)

```python
os.environ["PROJECT_ENDPOINT"] = ""
os.environ["MODEL_DEPLOYMENT_NAME"] = "gpt-4o"
```

* Option to set environment variables directly in the script.
* ⚠️ Never hard-code secrets for production.

### 4) Azure SDK Imports

```python
from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import McpTool, ToolSet, ListSortOrder
```

* `DefaultAzureCredential`: Azure authentication.
* `AgentsClient`: Client for creating/managing agents.
* `McpTool`, `ToolSet`, `ListSortOrder`: Configure MCP tools.

### 5) Load .env and Read Variables

```python
load_dotenv()
project_endpoint = os.getenv("PROJECT_ENDPOINT")
model_deployment = os.getenv("MODEL_DEPLOYMENT_NAME")
```

* Reads endpoint and model name from `.env` or system variables.

### 6) Connect to Agents Client

```python
agents_client = AgentsClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential(
        exclude_environment_credential=True,
        exclude_managed_identity_credential=True
    )
)
```

* Instantiates the client with endpoint and authentication.
* Excludes some default credentials.

### 7) MCP Configuration

```python
mcp_server_url = "https://learn.microsoft.com/api/mcp"
mcp_server_label = "mslearn"
```

* Defines the MCP server URL and label (Microsoft docs).

### 8) Initialize MCP Tool and ToolSet

```python
mcp_tool = McpTool(server_label=mcp_server_label, server_url=mcp_server_url)
mcp_tool.set_approval_mode("never")

toolset = ToolSet()
toolset.add(mcp_tool)
```

* Creates an MCP tool and adds it to the `ToolSet`.
* "never" mode allows automatic use by the agent.

### 9) Create and Run Agent

```python
with agents_client:
    agent = agents_client.create_agent(
        model=model_deployment,
        name="my-mcp-agent",
        instructions="Use MCP tool to search Microsoft docs."
    )
```

* Creates the agent with instructions.
* Displays agent ID and MCP tool details.

### 10) Create Thread and Send Message

```python
thread = agents_client.threads.create()
prompt = input("\nHow can I help?: ")
message = agents_client.messages.create(thread_id=thread.id, role="user", content=prompt)
```

* Creates a conversation thread.
* Sends user message.

### 11) Create and Process Run

```python
run = agents_client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id, toolset=toolset)
```

* Agent reads the message, calls MCP tool if needed, generates a response.
* Displays run status (`succeeded`, `failed`, etc.).

### 12) Inspect Steps and Tool Calls

```python
run_steps = agents_client.run_steps.list(thread_id=thread.id, run_id=run.id)
for step in run_steps:
    # Display step info and tool calls
```

* Shows each step of the run and any MCP tool calls.

### 13) Display Full Conversation

```python
messages = agents_client.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)
for msg in messages:
    if msg.text_messages:
        last_text = msg.text_messages[-1]
        print(f"{msg.role.upper()}: {last_text.text.value}")
```

* Lists all messages in the thread.

### 14) Cleanup

```python
agents_client.delete_agent(agent.id)
```

* Deletes the agent after execution.

---

## 💡 Best Practices & Tips

* Replace `input()` with a fixed prompt for automated tests:

```python
prompt = "Search for Azure AI Agents usage"
```

* Ensure environment variables match your endpoint and model.
* Add multiple MCP tools to the `ToolSet` as needed.
* Adjust tool approval mode depending on your workflow.

---

## 📊 Example Output

```
Created agent, ID: 1234abcd
MCP Server: mslearn at https://learn.microsoft.com/api/mcp
Created thread, ID: 5678efgh

How can I help?: What is Azure AI Foundry?

Created run, ID: 9876ijkl
Run completed with status: succeeded

Conversation:
--------------------------------------------------
USER: What is Azure AI Foundry?
--------------------------------------------------
AGENT: Azure AI Foundry is a unified environment for developing, testing, and deploying AI solutions on Azure.
--------------------------------------------------
Deleted agent
```

---

## 📝 Troubleshooting

* **Authentication error**: Check `DefaultAzureCredential` and Azure CLI login (`az login`).
* **Run failed**: Check `run.last_error` and `run_steps`.
* **MCP tool inaccessible**: Verify MCP server URL.


