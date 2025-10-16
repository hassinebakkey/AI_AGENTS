# Develop a Multi-Agent Solution

In this exercise, you'll create a project that orchestrates multiple AI agents using **Azure AI Foundry Agent Service**. You'll design an AI solution that assists with ticket triage. The connected agents will assess the ticket's priority, suggest a team assignment, and determine the level of effort required to complete the ticket.


## 1. Create an Azure AI Foundry Project

1. Open the Azure AI Foundry portal: [https://ai.azure.com](https://ai.azure.com) and sign in with your Azure credentials.
2. Close any tips or quick start panes.
3. Select **Create an agent** on the home page.
4. Enter a valid project name and expand **Advanced options**.
5. Confirm the following settings:

   * **Azure AI Foundry resource:** A valid resource name
   * **Subscription:** Your Azure subscription
   * **Resource group:** Create or select a resource group
   * **Region:** Select any AI Foundry recommended region

> Some Azure AI resources are constrained by regional model quotas. If a quota limit is exceeded, you may need to create another resource in a different region.

6. Select **Create** and wait for your project to be created.
7. If prompted, deploy a `gpt-4o` model using either the Global Standard or Standard deployment option.
8. Once the project is created, the **Agents playground** will open.
   Copy the **project endpoint** values for later use in your client application.

---

## 2. Create an AI Agent Client App


```bash
python -m venv labenv
./labenv/bin/Activate.ps1 ou .\labenv\Scripts\Activate.ps1 (windows)
pip install -r requirements.txt azure-ai-projects
```
`

* Replace `your_project_endpoint` with your project endpoint
* Replace `your_model_deployment` with your GPT-4o model deployment name
* Save the file


## 3. Sign into Azure and Run the App

1. sign in:

```bash
az login
```

2. Run the application:

```bash
python agent_triage.py
```

3. Enter a prompt, for example:

```
Users can't reset their password from the mobile app.
```

Test with other ticket prompts, e.g.:

```
Investigate occasional 502 errors from the search endpoint.
```

---

## Notes

* Ensure all environment variables are correctly set.
* Keep the Azure AI Foundry portal open while testing.
* The agents collaborate to triage support tickets automatically.
