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


import timeit

from swarms import Agent, ConcurrentWorkflow, Task
from swarms.agents.multion_agent import MultiOnAgent

# model
model = MultiOnAgent(multion_api_key="api-key")


# out = model.run("search for a recipe")
agent = Agent(
    agent_name="MultiOnAgent",
    description="A multi-on agent that performs browsing tasks.",
    llm=model,
    max_loops=1,
    system_prompt=None,
)

# logger.info("[Agent][ID][MultiOnAgent][Initialized][Successfully")

# Task
task = Task(
    agent=agent,
    description="Download https://www.coachcamel.com/",
)

# Swarm
# logger.info(
#     f"Running concurrent workflow with task: {task.description}"
# )

# Measure execution time
start_time = timeit.default_timer()

workflow = ConcurrentWorkflow(
    max_workers=20,
    autosave=True,
    print_results=True,
    return_results=True,
)

# Add task to workflow
workflow.add(task)
workflow.run()

# Calculate execution time
execution_time = timeit.default_timer() - start_time
# logger.info(f"Execution time: {execution_time} seconds")
print(f"Execution time: {execution_time} seconds")
