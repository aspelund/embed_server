# README.md

## Project Name: Embedding Server

This project involves a Flask server that provides two endpoints for interacting with text embeddings. These embeddings are generated using the SentenceTransformer model from the Hugging Face's Transformers library, and stored in a MongoDB database for easy retrieval.

The purpose of this server is to facilitate efficient similarity searches among large amounts of text data. This is done by representing each text as a dense vector (embedding), and then searching for similar texts is reduced to searching for similar vectors, a problem which can be efficiently solved even for large datasets.

## How it works

The Flask server exposes two POST endpoints:

1. `/store`: This endpoint takes a JSON object with a messageId and a text, generates an embedding for the text using the SentenceTransformer model, stores the embedding and messageId in MongoDB and returns the id of the stored embedding.
2. `/search`: This endpoint takes a JSON object with a text, generates an embedding for the text, and searches the MongoDB database for the top K most similar embeddings. The ids of these embeddings are then returned.

The embeddings are generated using the SentenceTransformer model, specifically the 'all-MiniLM-L6-v2' variant. The embeddings are stored in MongoDB in a collection named 'embeddings' in a database named 'mchat'. Each document in the 'embeddings' collection has the following fields: `_id`, `messageId`, `text`, and `embedding`.

There is a shell script `pop.sh` provided for populating the MongoDB database with sample data. It sends 25 POST requests to the `/store` endpoint with random text and messageIds.

## Requirements

- Python 3.11 or later
- Flask
- pymongo
- sentence-transformers
- numpy
- sklearn

## Setup

To set up this project, you first need to install the required Python packages. You can do this by running `pip install -r requirements.txt` (assuming you have a requirements.txt file).

Next, you need to have a MongoDB instance running on your machine. You can install MongoDB Community Edition from [here](https://www.mongodb.com/try/download/community).

Once you have MongoDB installed and running, you can start the Flask server by running `python main.py`. This will start the server on `0.0.0.0:5000`.

To populate the MongoDB database with sample data, you can run the shell script `pop.sh` by running `bash pop.sh`.

Now the server is ready to receive requests!

## Usage

To store a new text and its embedding, send a POST request to `http://localhost:5000/store` with a JSON body like `{"messageId": "your_message_id", "text": "your text"}`.

To search for similar texts, send a POST request to `http://localhost:5000/search` with a JSON body like `{"text": "your text"}`. This will return the ids of the top 10 most similar texts stored in the database.

## Future Work

The current implementation provides basic functionality for storing and searching text embeddings. Future work could include providing additional functionality such as updating existing embeddings, removing embeddings, and allowing for custom similarity thresholds or different numbers of results for the search endpoint.

## Contributions

Contributions are welcome! Please feel free to submit a pull request.
