# TicketSense-AI
AI-powered support ticket classification system using zero-shot NLP to automatically assign top-3 relevant tags with real-time Flask web interface.
Intelligent AI system for automatic support ticket tagging using Zero-Shot NLP with a Flask web interface.

Automates classification of customer support tickets into relevant categories, providing fast and accurate routing for support teams.

Overview

Manual ticket classification is time-consuming and error-prone.

TicketSense-AI leverages Hugging Face’s BART model to predict the top 3 relevant tags for any support ticket text in real-time.

This helps organizations streamline ticket management, improve response times, and enhance customer satisfaction.

Key Features

Real-time Zero-Shot NLP classification

Top-3 predicted tags with confidence scores

Modern Flask web UI with animated progress bars

Easy-to-update categories/tags

Lightweight and fast — runs locally or on cloud

Technology Stack

Python – core programming language

Flask – web application framework

Hugging Face Transformers – NLP model integration

PyTorch – deep learning backend

HTML5 & CSS3 – UI/UX design

Project Structure
TicketSense-AI/
│
├── app.py                # Main Flask application
├── templates/
│   └── index.html        # Web UI template
├── static/
│   └── style.css         # Styling for dashboard
├── requirements.txt      # Python dependencies
└── README.md

Installation & Usage
1️⃣ Clone the repository
git clone https://github.com/MaierAhmed/TicketSense-AI.git
cd TicketSense-AI

2️⃣ Setup virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
# OR
source venv/bin/activate    # Linux/Mac

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
python app.py


Open in your browser:

http://127.0.0.1:5000/

Example Inputs
I need a refund for my last month’s subscription.

My account login isn’t working anymore.

Can you help me upgrade my plan to premium?

Example Categories

Billing Issue

Technical Support

Account Management

Refund Request

Feature Request

(You can modify these inside app.py.)

Model

facebook/bart-large-mnli

Zero-Shot Classification pipeline via Hugging Face

Future Improvements

Few-shot learning for improved accuracy

Analytics dashboard to monitor ticket trends

User authentication & role-based access

Cloud deployment & Docker containerization

Demo Screenshot

(Add screenshot after running the app locally)

screenshots/demo.png

Author

AI/ML enthusiast building real-world NLP applications for customer support automation.
