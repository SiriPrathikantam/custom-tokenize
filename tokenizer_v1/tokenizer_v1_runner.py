import sys
import os
sys.path.append(os.path.abspath(".."))  # allow importing utils

from utils.vocab_utils import generate_vocab_from_file
from tokenizer_v1 import SimpleTokenizerV1



if __name__ == "__main__":
    # Step 1: Load vocab from file

    vocab = generate_vocab_from_file("../harrypotter.txt")


    # Step 2: Initialize tokenizer
    tokenizer = SimpleTokenizerV1(vocab)

    # Step 3: Try encoding
    sentence = "Harry went to Hogwarts!siri and sukesh followed him."
    encoded = tokenizer.encode(sentence)
    print("🧾 Encoded:", encoded)

    # Step 4: Decode it back
    decoded = tokenizer.decode(encoded)
    print("🔁 Decoded:", decoded)

    # Step 5: Show sample vocab
    tokenizer.show_vocab_sample(10)
