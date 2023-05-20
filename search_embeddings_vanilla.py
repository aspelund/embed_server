# search_embeddings_vanilla.py
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def search_embeddings(data, text, top_k=10):
    print("Starting search_embeddings function")

    # Initialize the sentence transformer model
    print("Encoding text into an embedding")
    embedding = model.encode([text])[0].reshape(1, -1)

    # Prepare data for cosine similarity
    ids = list(data.keys())
    vectors = np.concatenate([data[_id][1].reshape(1, -1) for _id in ids])

    print("Calculating cosine similarities")
    similarities = cosine_similarity(embedding, vectors)

    # Get the indices of the top_k most similar vectors
    top_k_indices = np.argsort(similarities[0])[-top_k:]

    print("Found nearest neighbors, returning their IDs")
    # Return the ids of the top_k most similar vectors
    return [ids[i] for i in top_k_indices]
