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
from langchain.llms import OpenAIChat

from swarms import Agent

# Loading environment variables from .env file
load_dotenv()

# Initialize the model
llm = OpenAIChat(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    max_tokens=1000,
)

# Initialize the agent
agent = Agent(
    llm=llm,
    max_loops="auto",
    autosave=True,
    dashboard=False,
    streaming_on=True,
    verbose=True,
)

# Run the workflow on a task
agent.run("Generate a 10,000 word blog on health and wellness.")
