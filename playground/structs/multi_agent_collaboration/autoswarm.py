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


from swarms import BaseSwarm, AutoSwarmRouter


class FinancialReportSummarization(BaseSwarm):
    def __init__(self, name: str = None, *args, **kwargs):
        super().__init__()

    def run(self, task, *args, **kwargs):
        return task


# Add swarm to router
router = AutoSwarmRouter(swarms=[FinancialReportSummarization])

# Create AutoSwarm Instance
autoswarm = AutoSwarmRouter(
    name="kyegomez/FinancialReportSummarization",
    description="A swarm for financial document summarizing and generation",
    verbose=True,
    router=router,
)

# Run the AutoSwarm
autoswarm.run("Analyze these documents and give me a summary:")
