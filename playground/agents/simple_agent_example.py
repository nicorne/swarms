"""
? TO TEST

What this script does:


Requirements:
1. Add the folowing API key(s) in your .env file:
   - OPENAI_API_KEY
   - AGENTOPS_API_KEY
2. 

Note: 
If you are running playground examples in the project files directly (without swarms installed via PIP),
make sure to add the project root to your PYTHONPATH by running the following command in the project's root directory:
  'export PYTHONPATH=$(pwd):$PYTHONPATH'
"""


import os

from dotenv import load_dotenv

from swarms import (
    Conversation,
    OpenAIChat,
)

conv = Conversation(
    autosave=False,
    time_enabled=True,
)

# Load the environment variables
load_dotenv()

# Get the API key from the environment
api_key = os.environ.get("OPENAI_API_KEY")

# Initialize the language model
llm = OpenAIChat(openai_api_key=api_key)


# Run the language model in a loop
def interactive_conversation(llm, iters: int = 10):
    conv = Conversation()
    for i in range(iters):
        user_input = input("User: ")
        conv.add("user", user_input)

        if user_input.lower() == "quit":
            break

        task = (
            conv.return_history_as_string()
        )  # Get the conversation history

        # Run the language model
        out = llm(task)
        conv.add("assistant", out)
        print(
            f"Assistant: {out}",
        )

        conv.display_conversation()
        # conv.export_conversation("conversation.txt")


# Replace with your LLM instance
interactive_conversation(llm)
