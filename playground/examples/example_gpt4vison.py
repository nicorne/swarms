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


from swarms import GPT4VisionAPI

# Initialize with default API key and custom max_tokens
api = GPT4VisionAPI(max_tokens=1000)

# Define the task and image URL
task = "Describe the scene in the image."
img = (
    "/home/kye/.swarms/swarms/examples/Screenshot from 2024-02-20"
    " 05-55-34.png"
)

# Run the GPT-4 Vision model
response = api.run(task, img)

# Print the model's response
print(response)
