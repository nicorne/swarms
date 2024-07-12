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


import discord
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Discord Bot Setup
client = discord.Client()

# AI Model Setup
tokenizer = AutoTokenizer.from_pretrained(
    "facebook/blenderbot-400M-distill"
)
model = AutoModelForSeq2SeqLM.from_pretrained(
    "facebook/blenderbot-400M-distill"
)


@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!generate"):
        input = message.content[len("!generate") :]
        inputs = tokenizer(input, return_tensors="pt")
        outputs = model.generate(**inputs)
        generated_text = tokenizer.batch_decode(
            outputs, skip_special_tokens=True
        )
        await message.channel.send(generated_text[0])


client.run("YOUR_BOT_TOKEN")
