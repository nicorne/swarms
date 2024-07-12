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


from swarms import Agent, OpenAIChat

agent = Agent(
    agent_name="API Requester",
    agent_description="This agent is responsible for making API requests.",
    system_prompt="You're a helpful API Requester agent. ",
    llm=OpenAIChat(),
    autosave=True,
    max_loops="auto",
    dashboard=True,
    interactive=True,
)


# Run the agent
out = agent.run("Create an api request to OpenAI in python.")
print(out)
