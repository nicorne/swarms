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

from swarms.models.gemini import Gemini
from swarms.prompts.react import react_prompt

load_dotenv()

api_key = os.environ["GEMINI_API_KEY"]

# Establish the prompt and image
task = "What is your name"
img = "images/github-banner-swarms.png"

# Initialize the model
model = Gemini(
    gemini_api_key=api_key,
    model_name="gemini-pro",
    max_tokens=1000,
    system_prompt=react_prompt(task=task),
    temperature=0.5,
)


# Run the model
out = model.run(
    "Create the code for a react component that displays a name"
)
print(out)
