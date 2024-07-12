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


from swarms import TogetherLLM

# Initialize the model with your parameters
model = TogetherLLM(
    model_name="mistralai/Mixtral-8x7B-Instruct-v0.1",
    max_tokens=1000,
)

# Run the model
model.run("Generate a blog post about the best way to make money online.")
