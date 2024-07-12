"""
! FIXME: Error generating response: expected string or bytes-like object

What this script does:
Swarm of agents finding the best deal on Tesla's Cybertruck using Multion

Requirements:
1. Create an account with multion.ai and run 'pip install multion'
2. Add the folowing API keys in your .env file:
   - MULTION_API_KEY
   - OPENAI_API_KEY

Note: 
If you are running playground examples in the project files directly (without swarms installed via PIP),
make sure to add the project root to your PYTHONPATH by running the following command in the project's root directory:
  'export PYTHONPATH=$(pwd):$PYTHONPATH'
"""

from swarms import Agent, AgentRearrange, OpenAIChat
from swarms.agents.multion_wrapper import MultiOnAgent

model = MultiOnAgent(
    url="https://tesla.com",
)


llm = OpenAIChat()


def browser_automation(task: str):
    """
    Run a task on the browser automation agent.

    Args:
        task (str): The task to be executed on the browser automation agent.
    """
    out = model.run(task)
    return out


# Purpose = To detect email spam using three different agents
agent1 = Agent(
    agent_name="CyberTruckBuyer1",
    system_prompt="Find the best deal on a Cyber Truck and provide your reasoning",
    llm=llm,
    max_loops=1,
    # output_type=str,
    metadata="json",
    function_calling_format_type="OpenAI",
    function_calling_type="json",
    streaming_on=True,
    tools=[browser_automation],
)

agent2 = Agent(
    agent_name="CyberTruckBuyer2",
    system_prompt="Find the best deal on a Cyber Truck and provide your reasoning",
    llm=llm,
    max_loops=1,
    # output_type=str,
    metadata="json",
    function_calling_format_type="OpenAI",
    function_calling_type="json",
    streaming_on=True,
    tools=[browser_automation],
)

agent3 = Agent(
    agent_name="CyberTruckBuyer3",
    system_prompt="Find the best deal on a Cyber Truck and provide your reasoning",
    llm=llm,
    max_loops=1,
    # output_type=str,
    metadata="json",
    function_calling_format_type="OpenAI",
    function_calling_type="json",
    streaming_on=True,
    tools=[browser_automation],
)

swarm = AgentRearrange(
    flow="CyberTruckBuyer1 -> CyberTruckBuyer2 -> CyberTruckBuyer3",
    agents=[agent1, agent2, agent3],
    logging_enabled=True,
    max_loops=1,
)

# Run all the agents
swarm.run("Let's buy a cyber truck")
