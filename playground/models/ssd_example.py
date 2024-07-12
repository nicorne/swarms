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


from swarms.models.ssd_1b import SSD1B

model = SSD1B()

task = "A painting of a dog"
neg_prompt = "ugly, blurry, poor quality"

image_url = model(task, neg_prompt)
print(image_url)
