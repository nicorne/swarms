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


import asyncio

from swarms.models.distilled_whisperx import DistilWhisperModel

model_wrapper = DistilWhisperModel()

# Download mp3 of voice and place the path here
transcription = model_wrapper("path/to/audio.mp3")

# For async usage
transcription = asyncio.run(
    model_wrapper.async_transcribe("path/to/audio.mp3")
)
