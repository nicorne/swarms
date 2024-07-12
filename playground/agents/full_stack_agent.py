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


from swarms import Agent, Anthropic, tool


# Tool
@tool  # Wrap the function with the tool decorator
def search_api(query: str, max_results: int = 10):
    """
    Search the web for the query and return the top `max_results` results.
    """
    return f"Search API: {query} -> {max_results} results"


## Initialize the workflow
agent = Agent(
    agent_name="Youtube Transcript Generator",
    agent_description=(
        "Generate a transcript for a youtube video on what swarms" " are!"
    ),
    llm=Anthropic(),
    max_loops="auto",
    autosave=True,
    dashboard=False,
    streaming_on=True,
    verbose=True,
    stopping_token="<DONE>",
    tools=[search_api],
)

# Run the workflow on a task
agent(
    "Generate a transcript for a youtube video on what swarms are!"
    " Output a <DONE> token when done."
)
