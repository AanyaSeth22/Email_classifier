from models import load_model
from utils import mask_pii

def classify_email(email_text):
    masked_text, entities = mask_pii(email_text)
    model, vectorizer = load_model()

    features = vectorizer.transform([masked_text])
    prediction = model.predict(features)[0]

    return {
        "category": prediction,
        "masked_email": masked_text,
        "detected_entities": entities
    }
