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


from swarms import AutoSwarm, AutoSwarmRouter, BaseSwarm


# Build your own Swarm
class MySwarm(BaseSwarm):
    def __init__(self, name="kyegomez/myswarm", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def run(self, task: str, *args, **kwargs):
        # Add your multi-agent logic here
        # agent 1
        # agent 2
        # agent 3
        return "output of the swarm"


# Add your custom swarm to the AutoSwarmRouter
router = AutoSwarmRouter(swarms=[MySwarm])


# Create an AutoSwarm instance
autoswarm = AutoSwarm(
    name="kyegomez/myswarm",
    description="A simple API to build and run swarms",
    verbose=True,
    router=router,
)


# Run the AutoSwarm
autoswarm.run("Analyze these financial data and give me a summary")
