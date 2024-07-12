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

from swarms import OpenAITTS

load_dotenv()

tts = OpenAITTS(
    model_name="tts-1-1106",
    voice="onyx",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
)

out = tts.run_and_save("Dammmmmm those tacos were good")
print(out)
