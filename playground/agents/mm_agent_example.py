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


from swarms.agents import MultiModalAgent

load_dict = {"ImageCaptioning": "cuda"}

node = MultiModalAgent(load_dict)

text = node.run_text("What is your name? Generate a picture of yourself")

img = node.run_img("/image1", "What is this image about?")

chat = node.chat(
    (
        "What is your name? Generate a picture of yourself. What is"
        " this image about?"
    ),
    streaming=True,
)
