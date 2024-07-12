"""
* WORKING

What this script does:
Using Ollama to run llama2 on your local computer and use it as LLM

Before running the script:
1. Install Ollama on your local computer (https://ollama.com/)
2. run command `ollama pull llama2` in terminal before running script

Note: 
If you are running playground examples in the project files directly (without swarms installed via PIP),
make sure to add the project root to your PYTHONPATH by running the following command in the project's root directory:
  'export PYTHONPATH=$(pwd):$PYTHONPATH'
"""

from swarms import Agent
from langchain_community.llms import Ollama

# Initialise LLM
llm = Ollama(
    model = "llama2",
    base_url = "http://localhost:11434",
    num_predict = 100,
    verbose=False
    )

# Initialize the agent
agent = Agent(
    agent_name="Funny Agent",
    system_prompt="You're the funniest LLM alive",
    agent_description=(
        "You're bin to a circus school"
    ),
    llm=llm,
    max_loops=1
)

# Run the Agent on a task
agent.run(
    "Write me a joke about drunk Aliens playing football"
)
