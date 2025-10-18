# Connect AI Agents to Tools Using Model Context Protocol (MCP)

This project demonstrates how to create an AI agent that connects to an MCP server and dynamically discovers callable functions. The goal is to build a simple inventory assessment agent for a cosmetics retailer.

## Overview

The agent will retrieve inventory information from the MCP server and make restock or clearance suggestions based on inventory levels and weekly sales. The solution uses Python SDKs for Azure AI Foundry and MCP.

## Prerequisites

* Python 3.6 or higher
* Azure AI Foundry account and project
* Basic familiarity with Python and async programming

---

## Step 1: Create an Azure AI Foundry Project

1. Open [Azure AI Foundry portal](https://ai.azure.com) and sign in.
2. Select **Create an agent**.
3. Enter a valid project name and expand **Advanced options**.
4. Configure project settings:

   * Azure AI Foundry resource
   * Subscription
   * Resource group
   * Region (AI Foundry recommended)
5. Click **Create** and wait for the project to be ready.
6. Deploy a GPT-4o model if prompted.
7. Copy the project endpoint for later use in the client application.

---

## Step 2: Configure Application Settings

### On Linux/macOS

1. Open Cloud Shell and run:

```bash
python -m venv labenv
source labenv/bin/activate
pip install -r requirements.txt azure-ai-projects mcp
```

2. Edit the `.env` file:

```bash
code .env
```

### On Windows (PowerShell)

1. Open PowerShell and run:

```powershell
python -m venv labenv
.\labenv\Scripts\Activate.ps1
pip install -r requirements.txt azure-ai-projects mcp
```

2. Edit the `.env` file:

```powershell
code .env
```

Replace `your_project_endpoint` with the endpoint from Azure AI Foundry and set `MODEL_DEPLOYMENT_NAME` to your model deployment name (e.g., `gpt-4o`).

---

## Step 3: Implement an MCP Server

1. Open `server.py` for editing:

```bash
code server.py
```

2. Add inventory and weekly sales tools:

```python
# Add an inventory check tool
@mcp.tool()
def get_inventory_levels() -> dict:
    return {
        "Moisturizer": 6,
        "Shampoo": 8,
        "Body Spray": 28,
        "Hair Gel": 5,
        "Lip Balm": 12,
        "Skin Serum": 9,
        "Cleanser": 30,
        "Conditioner": 3,
        "Setting Powder": 17,
        "Dry Shampoo": 45
    }

# Add a weekly sales tool
@mcp.tool()
def get_weekly_sales() -> dict:
    return {
        "Moisturizer": 22,
        "Shampoo": 18,
        "Body Spray": 3,
        "Hair Gel": 2,
        "Lip Balm": 14,
        "Skin Serum": 19,
        "Cleanser": 4,
        "Conditioner": 1,
        "Setting Powder": 13,
        "Dry Shampoo": 17
    }
```

3. Save the file.

---

## Step 4: Implement an MCP Client

1. Open `client.py` for editing:

```bash
code client.py
```

2. Add references:

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import FunctionTool, MessageRole, ListSortOrder
from azure.identity import DefaultAzureCredential
```

3. Start the MCP server and create a client session:

```python
stdio_transport = await exit_stack.enter_async_context(stdio_client(server_params))
stdio, write = stdio_transport
session = await exit_stack.enter_async_context(ClientSession(stdio, write))
await session.initialize()
```

4. List available tools:

```python
response = await session.list_tools()
tools = response.tools
print([tool.name for tool in tools])
```

---

## Step 5: Connect MCP Tools to Your Agent

1. Connect to the Azure AI project:

```python
agents_client = AgentsClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential(
        exclude_environment_credential=True,
        exclude_managed_identity_credential=True
    )
)
```

2. Build functions for each tool:

```python
functions_dict = {tool.name: make_tool_func(tool.name) for tool in tools}
mcp_function_tool = FunctionTool(functions=list(functions_dict.values()))
```

3. Create the agent:

```python
agent = agents_client.create_agent(
    model=model_deployment,
    name="inventory-agent",
    instructions="""
    You are an inventory assistant. Here are some guidelines:
    - Recommend restock if item inventory < 10 and weekly sales > 15
    - Recommend clearance if item inventory > 20 and weekly sales < 5
    """,
    tools=mcp_function_tool.definitions
)
agents_client.enable_auto_function_calls(tools=mcp_function_tool)
```

4. Start a chat session and invoke the agent:

```python
thread = agents_client.threads.create()
message = agents_client.messages.create(thread_id=thread.id, role=MessageRole.USER, content=user_input)
run = agents_client.runs.create(thread_id=thread.id, agent_id=agent.id)
```

5. Retrieve tool calls and submit outputs:

```python
function_name = tool_call.function.name
args_json = tool_call.function.arguments
kwargs = json.loads(args_json)
required_function = functions_dict.get(function_name)
output = await required_function(**kwargs)
tool_outputs.append({"tool_call_id": tool_call.id, "output": output.content[0].text})
agents_client.runs.submit_tool_outputs(thread_id=thread.id, run_id=run.id, tool_outputs=tool_outputs)
```

6. Display responses:

```python
messages = agents_client.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)
for message in messages:
    if message.text_messages:
        print(message.text_messages[-1].text.value)
```

---

## Step 6: Sign Into Azure and Run the App

1. Sign in using Azure CLI:

```bash
az login
```

2. Run the client application:

```bash
python client.py
```

3. Enter queries such as:

* `What are the current inventory levels?`
* `Are there any products that should be restocked?`
* `Which products would you recommend for clearance?`
* `What are the best sellers this week?`


