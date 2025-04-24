from flask import Flask, request, render_template
from process_emails import classify_email

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/classify", methods=["POST"])
def classify_form():
    email = request.form["email"]
    result = classify_email(email)
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
