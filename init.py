# init.py
from pymongo import MongoClient
import numpy as np

def init():
    # Create a client to connect to your MongoDB instance
    client = MongoClient("mongodb://localhost:27017/")

    # Access the 'mchat' database and 'embeddings' collection
    db = client['mchat']
    collection = db['embeddings']

    # Initialize an empty dictionary to store the vectors and messageIds
    data = {}

    # Fetch all documents from the collection
    cursor = collection.find({})

    # Load all vectors, messageIds and their corresponding MongoDB _ids into the dictionary
    for doc in cursor:
        vector = np.array(doc['embedding'], dtype=np.float32)
        messageId = doc['messageId']
        data[doc['_id']] = (messageId, vector)

    client.close()

    return data
