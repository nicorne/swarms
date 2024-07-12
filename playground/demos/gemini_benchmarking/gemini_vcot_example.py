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

from swarms.models import Gemini
from swarms.prompts.visual_cot import VISUAL_CHAIN_OF_THOUGHT

# Load the environment variables
load_dotenv()

# Get the API key from the environment
api_key = os.environ.get("GEMINI_API_KEY")

# Initialize the language model
llm = Gemini(
    gemini_api_key=api_key,
    temperature=0.5,
    max_tokens=1000,
    system_prompt=VISUAL_CHAIN_OF_THOUGHT,
)

# Initialize the task
task = "This is an eye test. What do you see?"
img = "playground/demos/multi_modal_chain_of_thought/eyetest.jpg"

# Run the workflow on a task
out = llm.run(task=task, img=img)
print(out)
