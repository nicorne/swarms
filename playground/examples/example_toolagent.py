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


# Import necessary libraries
from transformers import AutoModelForCausalLM, AutoTokenizer
from swarms import ToolAgent

# Load the pre-trained model and tokenizer
model = AutoModelForCausalLM.from_pretrained("databricks/dolly-v2-12b")
tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-12b")

# Define a JSON schema for person's information
json_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "is_student": {"type": "boolean"},
        "courses": {"type": "array", "items": {"type": "string"}},
    },
}

# Define the task to generate a person's information
task = "Generate a person's information based on the following schema:"

# Create an instance of the ToolAgent class
agent = ToolAgent(
    model=model, tokenizer=tokenizer, json_schema=json_schema
)

# Run the agent to generate the person's information
generated_data = agent.run(task)

# Print the generated data
print(generated_data)
