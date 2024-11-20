from prepro import preprocess_text
# Example for use
text = "SpaCy is an amazing tool for natural language processing!"
tokens, lemmas = preprocess_text(text)

print("Tokens:", tokens)
print("Lemmas:", lemmas)
