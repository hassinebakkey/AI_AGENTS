# Develop an Azure AI Chat Agent with Microsoft Agent Framework SDK

This project demonstrates how to use the Microsoft Agent Framework SDK and Azure AI Agent Service to create an AI agent that processes expense claims.


## Deploy a Model in Azure AI Foundry

1. Open [Azure AI Foundry portal](https://ai.azure.com) and sign in.
2. Search for the `gpt-4o` model.
3. Click **Use this model** and create a new project with the following settings:

   * Azure AI Foundry resource: *valid name*
   * Subscription: *your subscription*
   * Resource group: *create or select*
   * Region: *any recommended*
4. Wait for the project and deployment to be created.
5. Note the model deployment name, usually `gpt-4o`.


### Configure Application Settings

1. Create a virtual environment and install dependencies:

```powershell
python -m venv labenv
./labenv/bin/Activate.ps1 ou .\labenv\Scripts\Activate.ps1 (windows)
pip install azure-identity agent-framework
```

## Sign into Azure and Run the App

1. Sign in:

```
az login
```

2. Run the application:

```
python agent-framework.py
```

3. Enter `Submit an expense claim` when prompted.

## Summary

You have successfully created an Azure AI chat agent using Microsoft Agent Framework SDK and a custom tool.


