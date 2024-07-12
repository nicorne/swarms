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


from langchain.document_loaders import CSVLoader

from swarms.memory import qdrant

loader = CSVLoader(
    file_path="../document_parsing/aipg/aipg.csv",
    encoding="utf-8-sig",
)
docs = loader.load()


# Initialize the Qdrant instance
# See qdrant documentation on how to run locally
qdrant_client = qdrant.Qdrant(
    host="https://697ea26c-2881-4e17-8af4-817fcb5862e8.europe-west3-0.gcp.cloud.qdrant.io",
    collection_name="qdrant",
)
qdrant_client.add_vectors(docs)

# Perform a search
search_query = "Who is jojo"
search_results = qdrant_client.search_vectors(search_query)
print("Search Results:")
for result in search_results:
    print(result)
