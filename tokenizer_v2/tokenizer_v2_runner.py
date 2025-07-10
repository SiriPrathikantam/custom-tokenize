import sys
import os
sys.path.append(os.path.abspath(".."))  # allow importing utils

from utils.vocab_utils import generate_vocab_from_file
from tokenizer_v2 import SimpleTokenizerV2

if __name__ == "__main__":
    # Step 1: Load vocab
    vocab = generate_vocab_from_file("../harrypotter.txt")

    # Step 2: Initialize tokenizer
    tokenizer = SimpleTokenizerV2(vocab)

    # Step 3: Encode a test sentence
    # test_sentence = "Hedwig delivered mail to Dobby at 8pm!"
    test_sentence = "I grabbed coffee and scrolled Instagram before my meeting."
    encoded = tokenizer.encode(test_sentence)
    print("🧾 Encoded:", encoded)

    # Step 4: Decode it back
    decoded = tokenizer.decode(encoded)
    print("🔁 Decoded:", decoded)

    # Step 5: Print unknown tokens
    tokenizer.print_unknown_tokens()

    # Step 6: Save unknowns to log
    tokenizer.save_unknown_tokens()
