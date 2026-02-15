from flask import Flask, render_template, request
import torch
from transformers import pipeline

app = Flask(__name__)

# Load model once at startup
device = 0 if torch.cuda.is_available() else -1
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli",
    device=device
)

TAGS = [
    "Billing Issue",
    "Technical Bug",
    "Account Access",
    "Feature Request",
    "Refund Request",
    "Complaint",
    "Password Reset",
    "Subscription Problem",
    "Delivery Issue"
]

def classify_text(text):
    result = classifier(text, TAGS)
    return list(zip(result["labels"][:3], result["scores"][:3]))

@app.route("/", methods=["GET", "POST"])
def index():
    zero_tags = []
    ticket_text = ""
    loading = False

    if request.method == "POST":
        ticket_text = request.form.get("ticket_text")
        if ticket_text:
            zero_tags = classify_text(ticket_text)

    return render_template(
        "index.html",
        zero_tags=zero_tags,
        ticket_text=ticket_text
    )

if __name__ == "__main__":
    app.run(debug=True)
