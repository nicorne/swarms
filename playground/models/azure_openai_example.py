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
from swarms import AzureOpenAI

# Load the environment variables
load_dotenv()

# Create an instance of the AzureOpenAI class
model = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    openai_api_version=os.getenv("OPENAI_API_VERSION"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_ad_token=os.getenv("AZURE_OPENAI_AD_TOKEN"),
)

# Define the prompt
prompt = (
    "Analyze this load document and assess it for any risks and"
    " create a table in markdwon format."
)

# Generate a response
response = model(prompt)
print(response)
