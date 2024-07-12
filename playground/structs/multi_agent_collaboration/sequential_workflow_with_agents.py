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


from swarms import Agent, OpenAIChat, SequentialWorkflow

# Example usage
llm = OpenAIChat(
    temperature=0.5,
    max_tokens=3000,
)

# Initialize the Agent with the language agent
agent1 = Agent(
    agent_name="John the writer",
    llm=llm,
    max_loops=1,
    dashboard=False,
)


# Create another Agent for a different task
agent2 = Agent("Summarizer", llm=llm, max_loops=1, dashboard=False)


# Create the workflow
workflow = SequentialWorkflow(
    name="Blog Generation Workflow",
    description=(
        "Generate a youtube transcript on how to deploy agents into"
        " production"
    ),
    max_loops=1,
    autosave=True,
    dashboard=False,
    agents=[agent1, agent2],
)

# Run the workflow
workflow.run()
