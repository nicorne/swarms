"""
! FIXME
? difference with prev script

What this script does:
Long term memory example using ChromaDB

Requirements:
Add the folowing API key(s) in your .env file:
   - OPENAI_API_KEY (or change the LLM below)

Note: 
If you are running playground examples in the project files directly (without swarms installed via PIP),
make sure to add the project root to your PYTHONPATH by running the following command in the project's root directory:
  'export PYTHONPATH=$(pwd):$PYTHONPATH'
"""

import os

from swarms import Agent, OpenAIChat
from swarms_memory import ChromaDB


# Initialize the language model
llm = OpenAIChat(
    temperature=0.5,
    max_tokens=1000,
)

# Initilaize the chromadb client
chromadb = ChromaDB(
    metric="cosine",
    output_dir="scp",
    docs_folder="artifacts",
)

## Initialize the workflow
agent = Agent(
    llm=llm,
    name="Health and Wellness Blog",
    system_prompt="Generate a 10,000 word blog on health and wellness.",
    max_loops=4,
    autosave=True,
    dashboard=True,
    long_term_memory=[chromadb],
    memory_chunk_size=300,
)

# Run the workflow on a task
agent.run("Generate a 10,000 word blog on health and wellness.")
