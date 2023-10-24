import spacy

# Load the English NER model
nlp = spacy.load('en_core_web_sm')

# Sample text
text = "Apple Inc. was founded in April 1976 by Steve Jobs and Steve Wozniak. The company is headquartered in Cupertino, California."

# Process the text with spaCy
doc = nlp(text)

# Extract and print named entities
for ent in doc.ents:
    print(f"Entity: {ent.text}, Type: {ent.label_}")
