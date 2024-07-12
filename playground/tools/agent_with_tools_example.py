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
from swarms import tool

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")


llm = OpenAIChat(api_key=api_key)


@tool
def search_api(query: str) -> str:
    """Search API

    Args:
        query (str): _description_

    Returns:
        str: _description_
    """
    print(f"Searching API for {query}")


## Initialize the workflow
agent = Agent(
    llm=llm,
    max_loops=5,
    tools=[search_api],
    dashboard=True,
)

out = agent.run(
    "Use the search api to find the best restaurants in New York" " City."
)
print(out)
