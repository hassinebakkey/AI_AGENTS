# Multi-Agent Solution with Microsoft Agent Framework

---

lab:
title: 'Develop a multi-agent solution with Microsoft Agent Framework'
description: 'Learn to configure multiple agents to collaborate using the Microsoft Agent Framework SDK'
--------------------------------------------------------------------------------------------------------

# Develop a multi-agent solution

In this exercise, you'll practice using the sequential orchestration pattern in the Microsoft Agent Framework SDK. You'll create a simple pipeline of three agents that work together to process customer feedback and suggest next steps:

* **Summarizer agent**: condenses raw feedback into a short, neutral sentence.
* **Classifier agent**: categorizes feedback as Positive, Negative, or a Feature request.
* **Recommended Action agent**: suggests an appropriate follow-up step.


## Deploy a model in Azure AI Foundry

1. Open [Azure AI Foundry portal](https://ai.azure.com) and sign in.
2. Search for `gpt-4o` in **Explore models and capabilities**.
3. Select **Use this model** and create a project.
4. Confirm resource settings and select **Create**.
5. Access the chat playground automatically opened after creation.



Install required libraries:

```powershell
python -m venv labenv
./labenv/bin/Activate.ps1 ou .\labenv\Scripts\Activate.ps1 (windows)
pip install azure-identity agent-framework
```


### Sign in and run

az login
python agents.py

### Summary

You practiced sequential orchestration with Microsoft Agent Framework SDK, combining multiple agents into a streamlined workflow.

