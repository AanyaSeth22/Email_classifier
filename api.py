from utils import mask_pii, classify_email_model


def classify_email(email_body):
    masked_email, masked_entities = mask_pii(email_body)
    category = classify_email_model(masked_email)

    return {
        "input_email_body": email_body,
        "list_of_masked_entities": masked_entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }