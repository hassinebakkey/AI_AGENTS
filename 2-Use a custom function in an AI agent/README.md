# Use a Custom Function in an AI Agent

## Objective
This lab demonstrates how to create a simple **technical support AI agent** that can use a **custom Python function** as a tool to perform a specific task ,in this case, generating a support ticket from user input.

You will build an agent that collects details about a technical problem (email address and description) and automatically creates a support ticket file.

The solution uses the **Azure AI Foundry SDK for Python**.

---

## Technologies and Tools
- **Language:** Python 3.10+
- **Platform:** [Azure AI Foundry](https://ai.azure.com)
- **SDKs and Libraries:**
  - `azure-ai-agents`
  - `azure-identity`
  - `dotenv`
  - `uuid`
  - `pathlib`
  - `json`

---

## Steps

### 1. Create an Azure AI Foundry Project
1. Go to [Azure AI Foundry](https://ai.azure.com).
2. Create a new project and agent.
3. Deploy a `gpt-4o` model.
4. Copy your **project endpoint** and **model deployment name** (usually `gpt-4o`).

---

### 2. Create and Activate a Virtual Environment
```bash
python -m venv labenv
./labenv/bin/Activate.ps1  # for PowerShell
# or
source labenv/bin/activate  # for Linux/Mac
Install Dependencies
pip install -r requirements.txt azure-ai-projects
Run the application:
python agent.py
