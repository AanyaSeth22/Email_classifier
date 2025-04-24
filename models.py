import pickle

MODEL_PATH = "saved_models/email_classifier_model.pkl"
VEC_PATH = "saved_models/tfidf_vectorizer.pkl"

def load_model():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(VEC_PATH, "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer
