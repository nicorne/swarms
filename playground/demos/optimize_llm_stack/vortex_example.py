"""
? TO TEST

What this script does:


Requirements:
1. Add the folowing API key(s) in your .env file:
   - OPENAI_API_KEY
   - ..
2. 

Note: 
If you are running playground examples in the project files directly (without swarms installed via PIP),
make sure to add the project root to your PYTHONPATH by running the following command in the project's root directory:
  'export PYTHONPATH=$(pwd):$PYTHONPATH'
"""


import os

from dotenv import load_dotenv

from swarms.models import OpenAIChat
from swarms.structs import Agent

# import modal

load_dotenv()

# Model
llm = OpenAIChat(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model_name="gpt-4",
    max_tokens=1000,
)

# Modal
# stub = modal.Stub(name="swarms")


# Agent
# @stub.function(gpu="any")
agent = Agent(
    llm=llm,
    max_loops=2,
    autosave=True,
    dashboard=True,
)
out = agent.run(
    "Generate a 5,000 word blog on how swarms of autonomous agents"
    " can be used to solve the world's problems."
)
print(out)
