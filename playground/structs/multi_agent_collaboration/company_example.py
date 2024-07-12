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

from swarms import Agent, OpenAIChat
from swarms.structs.company import Company

load_dotenv()

llm = OpenAIChat(
    openai_api_key=os.getenv("OPENAI_API_KEY"), max_tokens=4000
)

ceo = Agent(llm=llm, ai_name="CEO")
dev = Agent(llm=llm, ai_name="Developer")
va = Agent(llm=llm, ai_name="VA")

# Create a company
company = Company(
    org_chart=[[dev, va]],
    shared_instructions="Do your best",
    ceo=ceo,
)

# Add agents to the company
hr = Agent(llm=llm, name="HR")
company.add(hr)

# Get an agent from the company
hr = company.get("CEO")

# Remove an agent from the company
company.remove(hr)

# Run the company
company.run()
