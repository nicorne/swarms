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


from swarms.models.llama_function_caller import LlamaFunctionCaller

llama_caller = LlamaFunctionCaller()


# Add a custom function
def get_weather(location: str, format: str) -> str:
    # This is a placeholder for the actual implementation
    return f"Weather at {location} in {format} format."


llama_caller.add_func(
    name="get_weather",
    function=get_weather,
    description="Get the weather at a location",
    arguments=[
        {
            "name": "location",
            "type": "string",
            "description": "Location for the weather",
        },
        {
            "name": "format",
            "type": "string",
            "description": "Format of the weather data",
        },
    ],
)

# Call the function
result = llama_caller.call_function(
    "get_weather", location="Paris", format="Celsius"
)
print(result)

# Stream a user prompt
llama_caller("Tell me about the tallest mountain in the world.")
