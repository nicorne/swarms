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


from swarms import QwenVLMultiModal

# Instantiate the QwenVLMultiModal model
model = QwenVLMultiModal(
    model_name="Qwen/Qwen-VL-Chat",
    device="cuda",
    quantize=True,
)

# Run the model
response = model("Hello, how are you?", "https://example.com/image.jpg")

# Print the response
print(response)
