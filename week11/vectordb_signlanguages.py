import chromadb
from chromadb.utils import embedding_functions
import os

# Create a new database client
# We want the data to be persisted
client = chromadb.PersistentClient(path="signlanguagesdb_backup")

collection = client.create_collection(
    'signlanguages',
    embedding_function=embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.environ['OPENAI_API_KEY'],
        model_name="text-embedding-ada-002"
    ))

filepath = '../signlanguages'

# Load the signlanguages files to the database we just initiated
for f in os.listdir(filepath):
    path = os.path.join(filepath, f)
    with open(path, 'r', encoding="utf8", errors='ignore') as f:
        text = f.read()

    text = text.replace('\n', ' ')

    collection.add(documents=[text], ids=[path])

