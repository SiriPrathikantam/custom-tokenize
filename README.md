# 🔤 Custom Tokenizer with Python

A beginner-friendly project to build your own tokenizer — like how GPT models break down text into tokens.

---

## 📦 What's Inside?

### ✅ Version 1 – Basic Tokenizer
- Tokenizes text (words + punctuation)
- Builds a vocabulary from `harrypotter.txt`
- Converts text to token IDs and back
- Handles unknown tokens with `<UNK>`

### ✅ Version 2 – Advanced Tokenizer
- Tracks unknown tokens with positions
- Shows `<UNK:actual_word>` during decoding
- Saves unknown tokens to a log file
- Auto-creates logs folder with timestamps

---

## 🧱 Folder Structure

LLM/
├── harrypotter.txt # Sample text for vocab
├── tokenizer_v1/ # Version 1 code
├── tokenizer_v2/ # Version 2 code + logs
├── utils/ # Vocabulary generator
├── scratch/ # Rough work / sandbox
└── README.md # This file