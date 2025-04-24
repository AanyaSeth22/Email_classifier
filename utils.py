import re
import spacy

nlp = spacy.load("en_core_web_trf")

PII_PATTERNS = {
    "full_name": r"\b([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)\b",
    "email": r"[\w\.-]+@[\w\.-]+\.\w+",
    "phone_number": r"\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,4}",  # Improved phone number regex
    "dob": r"\b(?:\d{2}[/-]\d{2}[/-]\d{4})\b",  # Keep DOB regex as is
    "aadhar_num": r"\b\d{4}\s\d{4}\s\d{4}\b",
    "credit_debit_no": r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b",
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])/(?:\d{2})\b"
}


def mask_pii(text):
    entities = []
    masked_text = text
    for label, pattern in PII_PATTERNS.items():
        for match in re.finditer(pattern, text):
            start, end = match.span()
            entity_val = match.group()
            if entity_val not in masked_text:
                continue
            masked_text = masked_text.replace(entity_val, f"[{label}]", 1)
            entities.append({
                "position": [start, end],
                "classification": label,
                "entity": entity_val
            })
    return masked_text, entities
