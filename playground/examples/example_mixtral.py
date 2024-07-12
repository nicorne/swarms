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


from swarms.models import Mixtral

# Initialize the Mixtral model with 4 bit and flash attention!
mixtral = Mixtral(load_in_4bit=True, use_flash_attention_2=True)

# Generate text for a simple task
generated_text = mixtral.run("Generate a creative story.")

# Print the generated text
print(generated_text)
