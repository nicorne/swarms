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


import requests
from bs4 import BeautifulSoup


def arxiv_search(query):
    """
    Performs a semantic search on arxiv.org for the given query.

    Args:
      query: The query to search for.

    Returns:
      A list of search results.
    """

    # Make a request to arxiv.org
    response = requests.get(
        "http://export.arxiv.org/api/query",
        params={"search_query": query, "start": 0, "max_results": 10},
    )

    # Parse the response
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the search results
    results = []
    for result in soup.find_all("entry"):
        results.append(
            {
                "title": result.find("title").text,
                "author": result.find("author").text,
                "abstract": result.find("summary").text,
                "link": result.find("link")["href"],
            }
        )

    return results


search = arxiv_search("quantum computing")
print(search)
