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


from swarms.models.gpt4_vision_api import GPT4VisionAPI
from swarms.structs import Agent

llm = GPT4VisionAPI()

task = (
    "Analyze this image of an assembly line and identify any issues"
    " such as misaligned parts, defects, or deviations from the"
    " standard assembly process. IF there is anything unsafe in the"
    " image, explain why it is unsafe and how it could be improved."
)
img = "assembly_line.jpg"

## Initialize the workflow
agent = Agent(
    llm=llm,
    max_loops=1,
    dashboard=True,
)

agent.run(task=task, img=img)
