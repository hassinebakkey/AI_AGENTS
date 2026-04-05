# IT Support Agent

## Overview

The IT Support Agent is an AI-powered assistant designed to provide automated IT support services for Contoso Corporation. Built using Microsoft Azure AI Projects, this agent leverages advanced language models and code interpretation capabilities to assist with common IT tasks, data analysis, and policy inquiries.

## Features

- Interactive chat interface for IT support queries
- Data analysis capabilities for system performance metrics
- Chart generation for visual data representation
- File handling and download functionality
- Integration with IT policy documents
- Support for image generation and processing

## Prerequisites

- Python 3.8 or higher
- Azure subscription with access to Azure AI Projects
- Azure CLI installed and configured
- Required Python packages (see requirements.txt)

## Installation

1. Clone or download this repository to your local machine.

2. Navigate to the project directory:
   ```
   cd path/to/it-support-agent
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the project root directory with the following environment variables:
   ```
   PROJECT_ENDPOINT=your_azure_ai_project_endpoint
   AGENT_NAME=it-support-agent
   ```

2. Ensure you have authenticated with Azure using the Azure CLI:
   ```
   az login
   ```

3. Verify that your Azure account has access to the specified AI project and agent.

## Usage

1. Run the agent:
   ```
   python agent_with_functions.py
   ```

2. The agent will connect to your Azure AI project and load the configured agent.

3. Interact with the agent through the command-line interface:
   - Ask IT support questions
   - Request data analysis on system performance
   - Inquire about IT policies
   - Type 'exit' to quit the session

4. Generated charts and files will be saved in the `agent_outputs/` directory.

## Project Structure

- `agent_with_functions.py`: Main application script
- `IT_Policy.txt`: IT support policy document
- `requirements.txt`: Python dependencies
- `system_performance.csv`: Sample system performance data
- `agent_outputs/`: Directory for generated outputs (charts, files)

