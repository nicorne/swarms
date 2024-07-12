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


from swarms.models.gpt4_vision_api import GPT4VisionAPI
from swarms.structs import Agent

llm = GPT4VisionAPI()

task = "What is the color of the object?"
img = "images/swarms.jpeg"

## Initialize the workflow
agent = Agent(
    llm=llm,
    max_loops="auto",
    dashboard=True,
)

agent.run(task=task, img=img)
