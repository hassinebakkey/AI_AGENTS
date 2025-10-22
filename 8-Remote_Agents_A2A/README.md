# Connect to Remote Agents with A2A Protocol

This lab demonstrates how to use **Azure AI Agent Service** with the **A2A (Agent-to-Agent)** protocol to create simple remote agents that collaborate with each other.

In this exercise, two agents are created:
- A **Title Agent** that generates catchy headlines for developer blog posts.
- An **Outline Agent** that uses the generated title to create a short article outline.

These agents communicate via the A2A protocol using Python and the Azure AI Foundry SDK.


## 🧩 Prerequisites

- An active **Azure subscription**.
- Access to the [Azure AI Foundry portal](https://ai.azure.com).
- Python 3.10+ installed.
- Basic understanding of Python and RESTful APIs.

---

## ⚙️ Setup Instructions
   ```

**Create and activate a virtual environment:**

   ```
   python -m venv labenv
   ./labenv/bin/Activate.ps1 ou .\labenv\Scripts\Activate.ps1 (windows)
   ```

**Install dependencies:**

   ```
   pip install -r requirements.txt azure-ai-projects a2a-sdk
   ```
**Edit the `.env` file** and replace placeholders with your Azure AI Foundry project endpoint and model deployment name (`gpt-4o`).

---

## 🧩 Project Structure

```
python
├── outline_agent/
│   ├── agent.py
│   ├── agent_executor.py
│   └── server.py
├── routing_agent/
│   ├── agent.py
│   └── server.py
├── title_agent/
│   ├── agent.py
│   ├── agent_executor.py
│   └── server.py
├── client.py
└── run_all.py
```

- **title_agent**: Generates titles for blog posts.
- **outline_agent**: Generates outlines based on titles.
- **routing_agent**: Routes user requests to the correct agent.
- **client.py**: Command-line client to interact with the agents.
- **run_all.py**: Starts all agent servers and runs the system.

---

## 🚀 Run the Application

1. **Sign into Azure:**
   ```
   az login
   ```

2. **Run the application:**
   ```
   python run_all.py
   ```

3. When prompted, try a request such as:

   ```
   Create a title and outline for an article about React programming.
   ```

4. To exit the application, type:
   ```
   quit
   ```

