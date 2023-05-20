# main.py
from flask import Flask, request, jsonify
from create_and_store_embedding_vanilla import create_and_store_embedding
from init import init
from search_embeddings_vanilla import search_embeddings

app = Flask(__name__)

# Initialize the vectors list
vectors = init()

@app.route('/store', methods=['POST'])
def store():
    data = request.get_json()
    id = create_and_store_embedding(vectors, data['messageId'], data['text'])
    return jsonify({'embeddingId': str(id)})

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    ids = search_embeddings(vectors, data['text'])
    return jsonify({'ids': [str(id) for id in ids]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
