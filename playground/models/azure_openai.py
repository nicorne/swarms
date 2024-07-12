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


from swarms.models import AzureOpenAI

# Initialize Azure OpenAI
model = AzureOpenAI()

# Run the model
model(
    "Create a youtube script for a video on how to use the swarms"
    " framework"
)
