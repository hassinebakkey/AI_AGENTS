Develop an AI Agent with Azure AI Agent Service

This project demonstrates how to build an intelligent data analysis agent using Azure AI Agent Service.
The agent uses the built-in Code Interpreter tool to dynamically generate Python code, analyze data, and provide statistical insights or text-based visualizations.

Project Overview

In this project, you will:

Create and configure an Azure AI Foundry project.

Build a Python client application that connects to your Azure AI Agent Service project.

Upload and analyze a data file using the Code Interpreter Tool.

Interact with the agent through a command-line interface.

The project is based on the Azure AI Foundry SDK for Python. Equivalent SDKs exist for .NET, JavaScript, and Java.

Prerequisites

Before running the project, make sure you have:

A valid Azure subscription.

A deployed Azure AI Foundry project and a GPT-4o model.

Python 3.8 or later installed on your machine.

Visual Studio Code or any preferred IDE.

Environment Setup
1. Create a Virtual Environment

Open the integrated terminal in VS Code and run:

python -m venv labenv
2. Activate the Virtual Environment

On Windows PowerShell:

.\labenv\Scripts\Activate.ps1

On Windows CMD:

labenv\Scripts\activate.bat

On Linux / macOS:

source labenv/bin/activate
3. Install Dependencies

Once activated (you should see (labenv) in your terminal), run:

pip install -r requirements.txt azure-ai-projects
Configuration

Open the .env file in VS Code:

code .env

Set your Azure AI Foundry project endpoint and model deployment name:

PROJECT_ENDPOINT="https://your-project-endpoint"
MODEL_DEPLOYMENT_NAME="gpt-4o"

Save and close the file.

Alternatively, you can define the variables directly in agent.py.

Code Overview

The main script is agent.py. It performs the following tasks:

Environment Setup
Loads configuration variables and displays data from data.txt.

Connect to Azure AI Agent
Uses DefaultAzureCredential to authenticate and connects via AgentsClient.

File Upload & Tool Initialization
Uploads the data file and initializes the Code Interpreter tool.

Agent Creation
Creates an agent using GPT-4o with instructions to analyze the uploaded data.

Interactive Conversation
Prompts the user for input and sends it to the agent. Displays the agent’s response and maintains conversation history.

Cleanup
Deletes the agent after the session.

Running the Application

Run the agent with:

python agent.py
Example Prompts:
What's the category with the highest cost?
Create a text-based bar chart showing cost by category.
What's the standard deviation of cost?

To exit the application, type:

quit
Files Included
File	Description
agent.py	Main Python script for the AI agent
data.txt	Example data file for analysis
.env	Configuration file (contains endpoint and model deployment)
requirements.txt	Python dependencies