import json
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Directly set project endpoint and agent name
project_endpoint = ""
agent_name = "product-expert-agent"

print(f"Connecting to project: {project_endpoint}")
print(f"Using agent: {agent_name}\n")

# Connect to project and agent
credential = DefaultAzureCredential(
    exclude_environment_credential=True,
    exclude_managed_identity_credential=True
)
project_client = AIProjectClient(
    credential=credential,
    endpoint=project_endpoint
)

# Get the OpenAI client
openai_client = project_client.get_openai_client()

# Get the agent
agent = project_client.agents.get(agent_name=agent_name)
print(f"Connected to agent: {agent.name} (id: {agent.id})\n")

# Create a new conversation
conversation = openai_client.conversations.create(items=[])
print(f"Created conversation (id: {conversation.id})\n")

# Conversation history for context
conversation_history = []

def send_message_to_agent(user_message):
    try:
        print(f"You: {user_message}\n")
        print("Agent: ", end="", flush=True)

        # Add user message to conversation
        openai_client.conversations.items.create(
            conversation_id=conversation.id,
            items=[{"type": "message", "role": "user", "content": user_message}]
        )

        conversation_history.append({
            "role": "user",
            "content": user_message
        })

        # Create response using agent
        response = openai_client.responses.create(
            conversation=conversation.id,
            extra_body={"agent": {"name": agent.name, "type": "agent_reference"}},
            input=""
        )

        # Check for MCP approval request
        approval_request = None
        if hasattr(response, "output") and response.output:
            for item in response.output:
                if getattr(item, "type", None) == "mcp_approval_request":
                    approval_request = item
                    break

        if approval_request:
            print(f"[Approval required for: {approval_request.name}]\n")
            print(f"Server: {approval_request.server_label}")

            try:
                args = json.loads(approval_request.arguments)
                print(f"Arguments:\n{json.dumps(args, indent=2)}\n")
            except Exception:
                print(f"Arguments: {approval_request.arguments}\n")

            approval_input = input("Approve this action? (yes/no): ").strip().lower()

            approval_response = {
                "type": "mcp_approval_response",
                "approval_request_id": approval_request.id,
                "approve": approval_input in ["yes", "y"]
            }

            openai_client.conversations.items.create(
                conversation_id=conversation.id,
                items=[approval_response]
            )

            response = openai_client.responses.create(
                conversation=conversation.id,
                extra_body={"agent": {"name": agent.name, "type": "agent_reference"}},
                input=""
            )

        if response and response.output_text:
            response_text = response.output_text
            print(f"{response_text}\n")

            if hasattr(response, "citations") and response.citations:
                print("Sources:")
                for citation in response.citations:
                    print(f"  - {getattr(citation, 'content', 'Knowledge Base')}")

            conversation_history.append({
                "role": "assistant",
                "content": response_text
            })
            return response_text

        print("No response received.\n")
        return None

    except Exception as e:
        print(f"\nError: {str(e)}\n")
        return None

def display_conversation_history():
    print("\n" + "="*60)
    print("CONVERSATION HISTORY")
    print("="*60 + "\n")

    for turn in conversation_history:
        print(f"{turn['role'].upper()}: {turn['content']}\n")

    print("="*60 + "\n")

def main():
    print("Contoso Product Expert Agent")
    print("Ask questions about our outdoor and camping products.")
    print("Type 'history' to see conversation history, or 'quit' to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue
            if user_input.lower() == "quit":
                print("\nEnding conversation...")
                break
            if user_input.lower() == "history":
                display_conversation_history()
                continue

            send_message_to_agent(user_input)

        except KeyboardInterrupt:
            print("\nInterrupted by user.")
            break
        except Exception as e:
            print(f"\nUnexpected error: {str(e)}\n")

    print("\nConversation ended.")

if __name__ == "__main__":
    main()
