# Integrate an AI Agent with Foundry IQ

This lab guides you through using **Azure AI Agent Service** to create an AI agent that uses **Foundry IQ** to search and retrieve information from knowledge bases. You will create a search resource, configure a knowledge base, build an agent in the portal, and connect to it programmatically using Python.

---

## Prerequisites

* An **Azure account** with access to Azure AI services.
* Basic knowledge of Python.
* Visual Studio Code installed (or Azure Cloud Shell with editor enabled).

---


## 1. Create a Foundry Project

1. Open the Foundry portal at [https://ai.azure.com](https://ai.azure.com) and sign in.
2. Ensure **New Foundry** toggle is **On**.
3. Select **Create a new project** and provide a valid name (e.g., `agent-iq-lab`).
4. Configure:

   * **Hub:** Create new or select existing.
   * **Subscription:** Your Azure subscription.
   * **Resource group:** Create or select existing.
   * **Location:** Any available region.
5. Click **Create** and wait for the project to initialize.

---

## 2. Create an Agent

1. On the project home page, select **Create an agent**.
2. Provide a name, e.g., `product-expert-agent`.
3. Select **Create**. The default model (like GPT-4.1) is deployed automatically.

---

## 3. Configure Data and Foundry IQ

1. Add the following instructions for the agent:

```
You are a helpful AI assistant for Contoso, specializing in outdoor camping and hiking products.
You must ALWAYS search the knowledge base to answer questions about products.
Provide detailed, accurate information and cite sources.
If no information is found, state so clearly.
```

2. Connect to **Foundry IQ**:

   * In **Knowledge**, click **Add → Connect to Foundry IQ**.
   * Select **Create new resource** and configure:

     * Subscription: Your Azure subscription
     * Resource group: Same as project
     * Service name: Globally unique
     * Location: Same as project
     * Pricing tier: Free or Basic
3. Upload sample product documents:

   * Download: [Contoso product PDFs]
   * Create a **Storage Account** in Azure and upload the 3 PDFs to a container named `contosoproducts`.
4. Create a knowledge base:

   * Name: `ks-contosoproducts`
   * Source: Azure Blob Storage
   * Storage account: Your storage account
   * Container: `contosoproducts`
   * Content extraction: minimal
   * Authentication: API Key
   * Embedding model: `text-embedding-3-small`
   * Chat completions model: `gpt-4.1`
5. Connect the knowledge base to your agent.

---

## 4. Test the Agent in Portal

Try the following queries in the agent playground:

* `What types of tents does Contoso offer?`
* `Tell me about which backpacks are available in XL.`
* `What camping accessories are available?`

Check for:

* Accuracy of information
* Citations to source documents
* Context awareness

---


## 5. Test the Python Client

Run the application:

```bash
python agent_client.py
```

Sample queries:

1. `What types of outdoor products does Contoso offer?`
2. `Tell me about the weatherproof features of your tents.`
3. `What's the difference between daypacks and expedition backpacks?`
4. `What camping accessories would you recommend for a weekend hiking trip?`
5. `How much do those items typically cost?`

Type `history` to view conversation history or `quit` to exit.

---

