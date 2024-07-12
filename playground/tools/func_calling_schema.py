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


import json
from swarms.tools.py_func_to_openai_func_str import (
    get_openai_function_schema_from_func,
)
from swarms.tools.prebuilt.bing_api import fetch_web_articles_bing_api

out = get_openai_function_schema_from_func(
    fetch_web_articles_bing_api,
    name="fetch_web_articles_bing_api",
    description="Fetches four articles from Bing Web Search API based on the given query.",
)
out = json.dumps(out, indent=2)
print(out)
