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

# Import the model
from swarms import ZeroscopeTTV

# Initialize the model
zeroscope = ZeroscopeTTV()

# Specify the task
task = "A person is walking on the street."

# Generate the video!
video_path = zeroscope(task)
print(video_path)
