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


# Import necessary modules and classes
from swarms.models import Anthropic

# Initialize an instance of the Anthropic class
model = Anthropic(anthropic_api_key="")

# Using the run method
# completion_1 = model.run("What is the capital of France?")
# print(completion_1)

# Using the __call__ method
completion_2 = model(
    "How far is the moon from the earth?", stop=["miles", "km"]
)
print(completion_2)
