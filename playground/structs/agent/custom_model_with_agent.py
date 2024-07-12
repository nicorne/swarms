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


from swarms import Agent
from swarms.models.base_llm import BaseLLM


# Define a custom LLM class
class ExampleLLM(BaseLLM):
    def __init__(self):
        pass

    def run(self, task: str, *args, **kwargs):
        # Your LLM logic here
        pass


# Initialize the workflow
agent = Agent(
    llm=ExampleLLM(),  # Instantiate the ExampleLLM class
    max_loops="auto",  # Set the maximum number of loops to "auto"
    autosave=True,  # Enable autosave feature
    dashboard=False,  # Disable the dashboard
    streaming_on=True,  # Enable streaming
    verbose=True,  # Enable verbose mode
    stopping_token="<DONE>",  # Set the stopping token to "<DONE>"
    interactive=True,  # Enable interactive mode
)

# Run the workflow on a task
agent(
    "Generate a transcript for a youtube video on what swarms are!"  # Specify the task
    " Output a <DONE> token when done."  # Specify the stopping condition
)
