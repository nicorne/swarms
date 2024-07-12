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


from swarms import tool


# Create the wrapper to wrap the function
@tool(
    name="Geo Coordinates Locator",
    description=("Locates geo coordinates with a city and or zip code"),
    return_string=False,
    return_dict=False,
)
def send_api_request_to_get_geo_coordinates(
    city: str = None, zip: int = None
):
    return "Test"


# Run the function to get the schema
out = send_api_request_to_get_geo_coordinates()
print(out)
