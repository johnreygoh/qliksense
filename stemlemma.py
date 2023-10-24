import pandas as pd
import nltk
import spacy
from nltk.stem import PorterStemmer

# Load NLTK and spaCy models
nltk.download('punkt')
nlp = spacy.load('en_core_web_sm')

# Load the CSV dataset
df = pd.read_csv('storeTransactions.csv')  # Replace with your dataset file path

# Function for stemming using NLTK
def stem_text(text):
    stemmer = PorterStemmer()
    words = nltk.word_tokenize(text)
    stemmed_words = [stemmer.stem(word) for word in words]
    return ' '.join(stemmed_words)

# Function for lemmatization using spaCy
def lemmatize_text(text):
    doc = nlp(text)
    lemmatized_words = [token.lemma_ for token in doc]
    return ' '.join(lemmatized_words)

# Apply stemming and lemmatization to all columns
for column in df.columns:
    if df[column].dtype == 'O':  # Check if the column contains text data
        df[f'{column}_stemmed'] = df[column].apply(stem_text)
        df[f'{column}_lemmatized'] = df[column].apply(lemmatize_text)

# Save the processed dataset to a new CSV file
df.to_csv('sample_superstore_processed.csv', index=False)  # Change the output file path as needed
