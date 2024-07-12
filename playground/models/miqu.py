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


from swarms import Mistral

# Initialize the model
model = Mistral(
    model_name="miqudev/miqu-1-70b",
    max_length=500,
    use_flash_attention=True,
    load_in_4bit=True,
)

# Run the model
result = model.run("What is the meaning of life?")
