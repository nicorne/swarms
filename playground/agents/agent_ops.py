"""
* WORKING
? How do I provide an agent with a document?

What this script does:
Simple agent run to test AgentOps (https://www.agentops.ai/)

Requirements:
1. Create an account on https://www.agentops.ai/ and run pip install agentops
2. Add the folowing API key(s) in your .env file:
   - OPENAI_API_KEY
   - AGENTOPS_API_KEY
3. Go to your agentops dashboard to observe your activity

Note: 
If you are running playground examples in the project files directly (without swarms installed via PIP),
make sure to add the project root to your PYTHONPATH by running the following command in the project's root directory:
  'export PYTHONPATH=$(pwd):$PYTHONPATH'
"""

from swarms import Agent, OpenAIChat

# Initialize the agent
agent = Agent(
    agent_name="Accounting Agent",
    system_prompt="Generate a financial report for the company's quarterly earnings.",
    agent_description=(
        "Generate a financial report for the company's quarterly earnings."
    ),
    llm=OpenAIChat(),
    max_loops=1,
    autosave=True,
    dashboard=False,
    streaming_on=True,
    verbose=True,
    stopping_token="<DONE>",
    interactive=False,
    state_save_file_type="json",
    saved_state_path="accounting_agent.json",
    agent_ops_on=True,
)

# Run the Agent on a task
agent.run(
    "Generate a financial report for the company's quarterly earnings!"
)
