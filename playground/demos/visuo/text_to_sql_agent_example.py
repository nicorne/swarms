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

# Import the OpenAIChat model and the Agent struct
from swarms import Agent, HuggingfaceLLM

# Load the environment variables
load_dotenv()

# Get the API key from the environment
api_key = os.environ.get("OPENAI_API_KEY")

# Initialize the language model
llm = HuggingfaceLLM(
    model_id="codellama/CodeLlama-70b-hf",
    max_length=4000,
    quantize=True,
    temperature=0.5,
)

## Initialize the workflow
agent = Agent(
    llm=llm,
    max_loops="auto",
    system_prompt=None,
    autosave=True,
    dashboard=True,
    tools=[None],
)

# Run the workflow on a task
agent.run("Generate a 10,000 word blog on health and wellness.")
