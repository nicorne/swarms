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



"""
Boss selects what agent to use
B -> W1, W2, W3
"""

from typing import List, Optional
from pydantic import BaseModel, Field
from swarms.tools.json_utils import str_to_json


class HierarchicalSwarm(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    agents: Optional[List[str]] = Field(
        None, title="List of agents in the hierarchical swarm"
    )
    task: Optional[str] = Field(
        None, title="Task to be done by the agents"
    )


all_agents = HierarchicalSwarm()

agents_schema = HierarchicalSwarm.model_json_schema()
agents_schema = str_to_json(agents_schema)
print(agents_schema)
