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


from typing import Annotated
from swarms import create_openai_tool
from openai import OpenAI

# Create an instance of the OpenAI client
client = OpenAI()

# Define the user messages for the chat conversation
messages = [
    {
        "role": "user",
        "content": "What's the weather like in San Francisco, Tokyo, and Paris?",
    }
]


# Define the BMI calculator tool using the create_openai_tool decorator
@create_openai_tool(
    name="BMI Calculator",
    description="Calculate the Body Mass Index (BMI)",
)
def calculate_bmi(
    weight: Annotated[float, "Weight in kilograms"],
    height: Annotated[float, "Height in meters"],
) -> Annotated[float, "Body Mass Index"]:
    """Calculate the Body Mass Index (BMI) given a person's weight and height."""
    return weight / (height**2)


# Create a chat completion request using the OpenAI client
response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=messages,
    tools=calculate_bmi,
    tool_choice="auto",  # auto is default, but we'll be explicit
)

# Print the generated response from the chat completion
print(response.choices[0].message["content"])
