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


from swarms.memory import WeaviateDB

weaviate_client = WeaviateDB(
    http_host="YOUR_HTTP_HOST",
    http_port="YOUR_HTTP_PORT",
    http_secure=True,
    grpc_host="YOUR_gRPC_HOST",
    grpc_port="YOUR_gRPC_PORT",
    grpc_secure=True,
    auth_client_secret="YOUR_APIKEY",
    additional_headers={"X-OpenAI-Api-Key": "YOUR_OPENAI_APIKEY"},
    additional_config=None,  # You can pass additional configuration here
)

weaviate_client.create_collection(
    name="my_collection",
    properties=[
        {"name": "property1", "dataType": ["string"]},
        {"name": "property2", "dataType": ["int"]},
    ],
    vectorizer_config=None,  # Optional vectorizer configuration
)

weaviate_client.add(
    collection_name="my_collection",
    properties={"property1": "value1", "property2": 42},
)

results = weaviate_client.query(
    collection_name="people", query="name:John", limit=5
)
