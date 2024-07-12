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
from swarms import OpenAIChat, Task, ConcurrentWorkflow, Agent

# Load environment variables from .env file
load_dotenv()

# Load environment variables
llm = OpenAIChat(openai_api_key=os.getenv("OPENAI_API_KEY"))
agent = Agent(llm=llm, max_loops=1)

# Create a workflow
workflow = ConcurrentWorkflow(max_workers=5)

# Create tasks
task1 = Task(agent, "What's the weather in miami")
task2 = Task(agent, "What's the weather in new york")
task3 = Task(agent, "What's the weather in london")

# Add tasks to the workflow
workflow.add(tasks=[task1, task2, task3])

# Run the workflow
workflow.run()
