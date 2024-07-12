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


from swarms.models import HuggingfaceLLM
import torch

try:
    inference = HuggingfaceLLM(
        model_id="gpt2",
        quantize=False,
        verbose=True,
    )

    device = "cuda" if torch.cuda.is_available() else "cpu"
    inference.model.to(device)

    prompt_text = (
        "Create a list of known biggest risks of structural collapse"
        " with references"
    )
    inputs = inference.tokenizer(prompt_text, return_tensors="pt").to(
        device
    )

    generated_ids = inference.model.generate(
        **inputs,
        max_new_tokens=1000,  # Adjust the length of the generation
        temperature=0.7,  # Adjust creativity
        top_k=50,  # Limits the vocabulary considered at each step
        pad_token_id=inference.tokenizer.eos_token_id,
        do_sample=True,  # Enable sampling to utilize temperature
    )

    generated_text = inference.tokenizer.decode(
        generated_ids[0], skip_special_tokens=True
    )
    print(generated_text)
except Exception as e:
    print(f"An error occurred: {e}")
