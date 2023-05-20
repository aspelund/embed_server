from flask import Flask, request, jsonify
from create_and_store_embedding_vanilla import create_and_store_embedding
from init import init
from search_embeddings_vanilla import search_embeddings
from get_tokens import count_tokens, split_into_tokens

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


@app.route('/count_tokens', methods=['POST'])
def count_tokens_route():
    data = request.get_json()
    text = data.get('text')

    if text is None:
        return jsonify({'error': 'Text is required'}), 400

    try:
        tokens = count_tokens(text, "gpt-4")
        return jsonify({'tokens': tokens})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/split_tokens', methods=['POST'])
def split_tokens_route():
    data = request.get_json()
    text = data.get('text')
    n = data.get('n')

    if text is None or n is None:
        return jsonify({'error': 'Text and n are required'}), 400

    try:
        tokens = split_into_tokens(text, "cl100k_base", n)
        return jsonify({'tokens': tokens})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run()
