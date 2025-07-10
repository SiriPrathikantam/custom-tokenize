import re

def generate_vocab_from_file(file_path):
    """
    Reads a text file, preprocesses it into tokens, and returns a vocabulary dictionary.
    
    Args:
        file_path (str): Path to the input text file.

    Returns:
        dict: A vocabulary mapping tokens to unique integer IDs.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        raw_text = file.read()

    # Tokenization using regex (words + symbols)
    preprocessed_text = re.findall(r'\w+|\S', raw_text)

    # Create vocabulary dictionary
    vocab = {token: idx for idx, token in enumerate(sorted(set(preprocessed_text)))}
    
    # Add <UNK> token at the end for unknown words
    vocab['<UNK>'] = len(vocab)

    return vocab
