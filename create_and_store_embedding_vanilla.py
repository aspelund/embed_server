# create_and_store_embedding_vanilla.py
from sentence_transformers import SentenceTransformer
from pymongo import MongoClient
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')


def create_and_store_embedding(vectors, messageId, text):
    # Initialize the sentence transformer model

    # Create an embedding from the text
    embedding = model.encode([text])[0]

    # Create a client to connect to your MongoDB instance
    client = MongoClient("mongodb://localhost:27017/")

    # Access the 'mchat' database and 'embeddings' collection
    db = client['mchat']
    collection = db['embeddings']

    # Get the next id for the new embedding
    next_id = collection.count_documents({}) + 1

    # Store the embedding in MongoDB
    doc = {
        "_id": next_id,
        "messageId": messageId,
        "text": text,
        "embedding": embedding.tolist()
    }
    result = collection.insert_one(doc)

    # Store the embedding in the vectors list
    vectors[next_id] = (messageId, embedding)

    client.close()

    return next_id
