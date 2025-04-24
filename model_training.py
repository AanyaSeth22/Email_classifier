import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

def train_model():
    df = pd.read_csv("masked_pii_data.csv")
    df = df.rename(columns={'email': 'email_text', 'type': 'category'})

    X = df['email_text']
    y = df['category']

    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)

    model = MultinomialNB()
    model.fit(X_vec, y)

    os.makedirs("saved_models", exist_ok=True)
    with open("saved_models/email_classifier_model.pkl", "wb") as f:
        pickle.dump(model, f)
    with open("saved_models/tfidf_vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

if __name__ == '__main__':
    train_model()
