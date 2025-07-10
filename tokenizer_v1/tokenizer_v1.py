import re

class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.vocab = vocab
        self.id_to_token = {idx: token for token, idx in vocab.items()}

    def encode(self, text):
        tokens = re.findall(r'\w+|\S', text)
        UNK_ID = self.vocab.get('<UNK>', len(self.vocab))
        return [self.vocab.get(token, UNK_ID) for token in tokens]

    def decode(self, ids):
        result = ''
        for id_ in ids:
            if id_ in self.id_to_token:
                token = self.id_to_token[id_]
                if token in {'.', ',', '!', '?'}:
                    result = result.rstrip() + token + ' '
                else:
                    result += token + ' '
        return result.strip()

    def show_vocab_sample(self, n=10):
        print(f"✅ Vocab size: {len(self.vocab)}")
        for token, idx in list(self.vocab.items())[:n]:
            print(f"Token: '{token}' → ID: {idx}")


