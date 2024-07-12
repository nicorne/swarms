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


from swarms.models import vLLM

# Initialize vLLM with custom model and parameters
custom_vllm = vLLM(
    model_name="custom/model",
    tensor_parallel_size=8,
    trust_remote_code=True,
    revision="abc123",
    temperature=0.7,
    top_p=0.8,
)

# Generate text with custom configuration
generated_text = custom_vllm.run("Create a poem about nature.")
print(generated_text)
