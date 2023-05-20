import tiktoken


def count_tokens(text: str, model_name: str) -> int:
    """Counts the number of tokens in a text string for a specific model."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(text))
    return num_tokens

# Splits a text into chunks that each are at most n tokens long.


def split_into_tokens(text: str, encoding_name: str, n: int):
    """Splits a text string into n tokens according to the specified encoding."""
    encoding = tiktoken.get_encoding(encoding_name)
    token_integers = encoding.encode(text)
    tokens = [encoding.decode_single_token_bytes(
        token).decode('utf-8') for token in token_integers]
    return tokens[:n]
