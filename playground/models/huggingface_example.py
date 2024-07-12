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

model_id = "NousResearch/Yarn-Mistral-7b-128k"
inference = HuggingfaceLLM(model_id=model_id)

task = "Once upon a time"
generated_text = inference(task)
print(generated_text)
