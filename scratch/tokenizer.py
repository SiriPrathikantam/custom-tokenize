# first we open file harrypotter.txt and read it 
# and total number of characters in the file and print 1st 100 characters

with open("harrypotter.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

# print("total number of charaters in the file :", len(raw_text))  # 6284923
# print("first 1000 characters of the file :",raw_text[:1000]) 

# Our goal is to tokenize this 6284923-character short story into individual words 
# and special characters that we can then turn into embeddings for LLM training

# we will use re module to tokenize the text

import re 
import os
from datetime import datetime

# text = "hey siri how are you doing today? I am fine, thank you!"
# result = re.split(r'(\s)',text) here we split the text by whitespace and keep the whitespace as well
# print(result)
# Output ['hey', ' ', 'siri', ' ', 'how', ' ', 'are', ' ', 'you', ' ', 'doing', ' ', 'today?', ' ', 'I', ' ', 'am', ' ', 'fine,', ' ', 'thank', ' ', 'you!']
# if we want to split with punctuation then we can use re.split(r'([,.!?]|\s)', text)

# other issue is still whitespaces are present in the list

# result = [item for item in result if item.strip()]

# If item.strip() produces a non-empty string → condition is True → keep it
# If item.strip() produces "" (empty string) → condition is False → discard it

preproccessed_text = re.findall(r'\w+|\S',raw_text)
# print(preproccessed_text[:1000])  # first 1000 tokens

# print(len(preproccessed_text))  # total number of tokens in the file 1450158

# now we need to assign a unique id to each token first using set to remove duplicates and then sort and then using enumerate to assign unique id

vocab = {token:integer for integer,token in enumerate(sorted(set(preproccessed_text)))}

# for token, integer in list(vocab.items())[:1000]:
#     print(f"Token:{token} -> ID : {integer}")

# print(len(vocab))  # total number of unique tokens in the file 25366

vocab['<UNK>'] = len(vocab)  # Adding a special token for unknown words

# Update your encode method so it:
# Logs unknown tokens in a set or list
# Returns normal IDs, but remembers what was unknown
# Update your decode so it can highlight unknown tokens

class Tokenizer:
    def __init__(self, vocab):
        # using provided vocab we already did the tokenization
        # and created a dictionary of tokens and their unique ids
        # so we can use this vocab to tokenize the text
        # and convert the tokens to their unique ids
        self.vocab = vocab

        # we will also create a reverse vocab to convert ids back to tokens
        self.id_to_token = {integer:token for token, integer in self.vocab.items()}

        self.unknown_tokens = set()  # To keep track of unknown tokens
        self.unknown_positions = {}  # position in encoded list → original unknown token
    
    def encode(self,text):
        # this will take a text and give us a list of tokens 

        tokens = re.findall(r'\w+|\S', text) 
        UNK_ID = self.vocab.get('<UNK>', len(self.vocab))  # Get the ID for <UNK> token, default to next available ID if not found

        # return [self.vocab.get(token,UNK_ID) for token in tokens]

        encoded_ids = []
        self.unknown_positions = {}  # Reset unknown positions for each encode call

        for i,token in enumerate(tokens):
            token_id = self.vocab.get(token,UNK_ID)
            encoded_ids.append(token_id)

            if token_id == UNK_ID and token != '<UNK>':
                self.unknown_tokens.add(token)
                self.unknown_positions[len(encoded_ids)-1] = token
        
        return encoded_ids
    

    
    def decode(self,ids):

        # tokens = [self.id_to_token[id_] for id_ in ids if id_ in self.id_to_token]

        result = ' '
        for i, id_ in enumerate(ids):
            if id_ in self.id_to_token:
                token = self.id_to_token[id_]
                if token == '<UNK>':
                    # Fetch the original unknown token if we logged it
                    unknown_token = self.unknown_positions.get(i,'<UNK>')
                    result += f'<UNK:{unknown_token}> '
                elif token in {'.', ',', '!', '?'}:
                    result = result.rstrip() + token + ' '
                else:
                    result += token + ' '

        return result.strip()
    
    def print_unknown_tokens(self):
        if self.unknown_tokens:
            print(f'⚠ unknown tokens are found : {self.unknown_tokens}')
        else:
            print('✅ No unknown tokens found!')
    
    def save_unknown_tokens(self, folder = 'logs'):

        # Build timestamped filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{folder}/unknown_tokens_{timestamp}.txt"


        # folder = os.path.dirname(filename)

        if folder and not os.path.exists(folder):
            os.makedirs(folder)
            print(f"📁 Created folder: {folder}")

        with open(filename, 'w', encoding='utf-8') as file:
            for token in sorted(self.unknown_tokens):
                file.write(f"{token}\n")
        print(f"✅ Unknown tokens saved to {filename}")


# tokenizer = Tokenizer(vocab)

# sentence = "hey siri apple sukesh how are you doing today? I am fine, thank you!"
# encoded = tokenizer.encode(sentence)
# print(f"Encoded: {encoded}")

# decoded = tokenizer.decode(encoded)
# print(f"Decoded: {decoded}")

#  Output:
# Encoded: [14198, 14432, 7244, 25323, 11265, 23314, 83, 2923, 7018, 12604, 4, 23040, 25323, 0]
# Decoded: hey how are you doing today? I am fine, thank you!
#  here siri got skipped because it is not in the vocab
#  now im updating the vocan with UKN AND Tokend id to next available id

# tokenizer = Tokenizer(vocab)

# sentence = "hey siri apple sukesh how are you doing today?"
# encoded = tokenizer.encode(sentence)
# print(f"Encoded: {encoded}")

# decoded = tokenizer.decode(encoded)
# print(f"Decoded: {decoded}")

# tokenizer.print_unknown_tokens()

# # Save unknown tokens to logs folder
# tokenizer.save_unknown_tokens("logs/unknown_tokens.txt")

tokenizer = Tokenizer(vocab)

sentence = "Artificial intelligence is transforming the world rapidly! Let's embrace the change."
encoded = tokenizer.encode(sentence)
print(f"Encoded: {encoded}")

decoded = tokenizer.decode(encoded)
print(f"Decoded: {decoded}")

tokenizer.print_unknown_tokens()

tokenizer.save_unknown_tokens("logs")




