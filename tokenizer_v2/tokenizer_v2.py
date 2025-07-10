import re
import os
from datetime import datetime

class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.vocab = vocab
        self.id_to_token = {idx: token for token, idx in vocab.items()}
        self.unknown_tokens = set()
        self.unknown_positions = {}

    def encode(self, text):
        tokens = re.findall(r'\w+|\S', text)
        UNK_ID = self.vocab.get('<UNK>', len(self.vocab))
        encoded_ids = []
        self.unknown_positions = {}

        for i, token in enumerate(tokens):
            token_id = self.vocab.get(token, UNK_ID)
            encoded_ids.append(token_id)

            if token_id == UNK_ID and token != '<UNK>':
                self.unknown_tokens.add(token)
                self.unknown_positions[len(encoded_ids) - 1] = token

        return encoded_ids

    def decode(self, ids):
        result = ''
        for i, id_ in enumerate(ids):
            if id_ in self.id_to_token:
                token = self.id_to_token[id_]
                if token == '<UNK>':
                    unknown_token = self.unknown_positions.get(i, '<UNK>')
                    result += f'<UNK:{unknown_token}> '
                elif token in {'.', ',', '!', '?'}:
                    result = result.rstrip() + token + ' '
                else:
                    result += token + ' '
        return result.strip()

    def print_unknown_tokens(self):
        if self.unknown_tokens:
            print(f"⚠ Unknown tokens found: {self.unknown_tokens}")
        else:
            print("✅ No unknown tokens found!")

    def save_unknown_tokens(self, folder='logs'):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{folder}/unknown_tokens_{timestamp}.txt"

        if folder and not os.path.exists(folder):
            os.makedirs(folder)
            print(f"📁 Created folder: {folder}")

        with open(filename, 'w', encoding='utf-8') as file:
            for token in sorted(self.unknown_tokens):
                file.write(f"{token}\n")
        print(f"✅ Unknown tokens saved to {filename}")


