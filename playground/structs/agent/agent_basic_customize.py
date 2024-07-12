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


from swarms.models import OpenAIChat
from swarms.structs import Agent

api_key = ""

# Initialize the language model, this model can be swapped out with Anthropic, ETC, Huggingface Models like Mistral, ETC
llm = OpenAIChat(
    # model_name="gpt-4"
    openai_api_key=api_key,
    temperature=0.5,
    # max_tokens=100,
)

## Initialize the workflow
agent = Agent(
    llm=llm,
    max_loops=2,
    dashboard=True,
    # stopping_condition=None,  # You can define a stopping condition as needed.
    # loop_interval=1,
    # retry_attempts=3,
    # retry_interval=1,
    # interactive=False,  # Set to 'True' for interactive mode.
    # dynamic_temperature=False,  # Set to 'True' for dynamic temperature handling.
)

# Run the workflow on a task
out = agent.run("Generate a 10,000 word blog on health and wellness.")
print(out)
