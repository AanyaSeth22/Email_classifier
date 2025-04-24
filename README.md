# Email Classifier - Support Team

## Overview
This project is an email classification system designed to categorize support team emails into categories like "Incident", "Request", and "Problem". It also masks personally identifiable information (PII) such as names, email addresses, and phone numbers.

## Features
- Classify emails into predefined categories.
- Mask PII entities like full names, emails, phone numbers, and dates of birth in the email content.
- Expose an API for email classification (via POST requests).
- Flask web app for easy testing with a front-end interface.

## Setup Instructions

To run this project locally, follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/email-classifier.git
   cd email-classifier
Install the required dependencies: Make sure you have Python installed. Install the required libraries by running:

bash
Copy code
pip install -r requirements.txt
Train the model (optional, if the model is not pre-trained): You can train the model using the following command:

bash
Copy code
python model_training.py
Run the Flask web app: Start the app with:

bash
Copy code
python app.py
Open the web app: Once the Flask app is running, you can view the application in your browser at:

url
Copy code
http://127.0.0.1:5000/
Usage Instructions
On the homepage, enter the content of an email.

Click on "Classify Email" to classify the email and view the detected PII entities.

The result will include the email's classification and a masked version of the email with PII entities replaced by placeholders.

API Usage
Endpoint: /api/classify

Method: POST

Request Body:

json
Copy code
{
  "email": "Your email content here"
}
Response:

json
Copy code
{
  "category": "Incident",
  "masked_email": "Your masked email content",
  "detected_entities": [
    {
      "classification": "full_name",
      "entity": "John Doe",
      "position": [0, 8]
    }
  ]
}

