# Project Name: Embedding Server

This project involves a Flask server that provides four endpoints for interacting with text embeddings and text tokenization. These embeddings are generated using the SentenceTransformer model from Hugging Face's Transformers library, and stored in a MongoDB database for easy retrieval.

The purpose of this server is to facilitate efficient similarity searches among large amounts of text data and to assist in tokenizing text. This is done by representing each text as a dense vector (embedding), and then searching for similar texts is reduced to searching for similar vectors, a problem which can be efficiently solved even for large datasets. The tokenization is carried out by the OpenAI's `tiktoken` library.

## How it works

The Flask server exposes four POST endpoints:

1. `/store`: This endpoint takes a JSON object with a messageId and a text, generates an embedding for the text using the SentenceTransformer model, stores the embedding and messageId in MongoDB and returns the id of the stored embedding.
2. `/search`: This endpoint takes a JSON object with a text, generates an embedding for the text, and searches the MongoDB database for the top K most similar embeddings. The ids of these embeddings are then returned.
3. `/count_tokens`: This endpoint takes a JSON object with a text, and returns the number of tokens in the text.
4. `/split_tokens`: This endpoint takes a JSON object with a text and a number n, and returns the first n tokens of the text.

There is a shell script `test.sh` provided for testing the tokenization endpoints. It sends POST requests to the `/count_tokens` and `/split_tokens` endpoints with predefined text and checks the returned response.

## Requirements

- Python 3.11 or later
- Flask
- pymongo
- sentence-transformers
- numpy
- sklearn
- tiktoken

## Setup

To set up this project, you first need to install the required Python packages. You can do this by running `pip install -r requirements.txt`.

Next, you need to have a MongoDB instance running on your machine. You can install MongoDB Community Edition from [here](https://www.mongodb.com/try/download/community).

Once you have MongoDB installed and running, you can start the Flask server by running `python main.py`. This will start the server on `0.0.0.0:5000`.

To test the tokenization endpoints, you can run the shell script `test.sh` by running `bash test.sh`.

Now the server is ready to receive requests!

## Usage

To store a new text and its embedding, send a POST request to `http://localhost:5000/store` with a JSON body like `{"messageId": "your_message_id", "text": "your text"}`.

To search for similar texts, send a POST request to `http://localhost:5000/search` with a JSON body like `{"text": "your text"}`. This will return the ids of the top 10 most similar texts stored in the database.

To count the number of tokens in a text, send a POST request to `http://localhost:5000/count_tokens` with a JSON body like `{"text": "your text"}`.

To split a text into n tokens, send a POST request to `http://localhost:5000/split_tokens` with a JSON body like `{"text": "your text", "n": 3}`.

## Future Work

The current implementation provides basic functionality for storing and searching text embeddings, and tokenizing text. Future work could include providing additional functionality such as updating existing embeddings, removing embeddings, and allowing for custom similarity
