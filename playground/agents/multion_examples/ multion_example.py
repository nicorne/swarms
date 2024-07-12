"""
! FIXME 
TODO

What this script does:
Running the a request to MultiOn in parallel threads

Requirements:
1. Create an account with multion.ai and run 'pip install multion'
2. Install the Multion Chrome extension
3. Add your multion API key in your .env file under the name "MULTION_API_KEY"

Note: 
If you are running playground examples in the project files directly (without swarms installed via PIP),
make sure to add the project root to your PYTHONPATH by running the following command in the project's root directory:
  'export PYTHONPATH=$(pwd):$PYTHONPATH'
"""

import os
import threading
from swarms.agents.multion_wrapper import MultiOnAgent


def run_model():
    model = MultiOnAgent(
        max_steps=500, url="https://news.ycombinator.com/"
    )
    out = model.run("What's the top post on hackernews?")
    print(out)

run_model()

# Create a list to store the threads
threads = []

# Run 10 instances using multithreading
# for _ in range(10):
#     api_key = os.getenv("MULTION_API_KEY")
#     thread = threading.Thread(target=run_model, args=(api_key,))
#     thread.start()
#     threads.append(thread)

# Wait for all threads to finish
# for thread in threads:
#     thread.join()
