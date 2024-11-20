import spacy

# Cargar el modelo de spaCy
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    # Creates the NLP document with the input text
    doc = nlp(text)
    # Tokenization and stop words elimination
    tokens = [token.text.lower() for token in doc if not token.is_stop]

    # We do also lemmatization
    lemmas = [token.lemma_ for token in doc if not token.is_stop]

    return tokens, lemmas