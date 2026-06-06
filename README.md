"""
# 🔍 Fake Website Finder

## 📖 Project Definition
The Fake Website Finder Project is a Flask-based web application that detects fraudulent websites using rule-based URL analysis. It checks for HTTPS, URL length, IP address usage, and suspicious keywords, then classifies them as **FAKE WEBSITE ⚠️** or **REAL WEBSITE ✅** with clear reasons.

---

## 🎯 Objective
To provide a simple, beginner-friendly tool that helps users identify potentially fake websites and stay safe online.

---

## 🚀 Features
- Detects missing HTTPS
- Flags unusually long URLs
- Identifies IP addresses used instead of domains
- Scans for suspicious keywords (login, verify, bank, account, etc.)
- Provides clear red/green indicators with reasons

---

## 🛠 Installation & Setup
1. Clone the repository:
   git clone https://github.com/your-username/fake-website-finder.git
   cd fake-website-finder

2. Create a virtual environment:
   python -m venv .venv
   .venv\Scripts\activate   # Windows

3. Install dependencies:
   pip install flask

4. Run the app:
   python app.py

5. Open in browser:
   http://127.0.0.1:5000/

---

## 📂 Project Structure
fake-website-finder/
│── app.py        # Main Flask application (single file)

---

## 📸 Usage Example
- Input: http://123.45.67.89/login
- Output: FAKE WEBSITE ⚠️
  - Reasons:
    - IP address used instead of domain
    - Contains suspicious keyword "login"

---

## 📜 License
This project is for educational purposes. Free to use and modify.
"""

from flask import Flask, request
import re

app = Flask(__name__)

# --- Rule-Based Fake Website Detector ---
def check_website(url):
    suspicious = False
    reasons = []

    # Rule 1: No HTTPS
    if not url.startswith("https://"):
        suspicious = True
        reasons.append("No HTTPS (secure connection missing)")

    # Rule 2: Very long URL
    if len(url) > 75:
        suspicious = True
        reasons.append("URL length unusually long")

    # Rule 3: IP address in URL
    if re.match(r"^(http|https)://\d+\.\d+\.\d+\.\d+", url):
        suspicious = True
        reasons.append("IP address used instead of domain")

    # Rule 4: Suspicious keywords
    keywords = ["login", "verify", "secure", "update", "bank", "account"]
    if any(word in url.lower() for word in keywords):
        suspicious = True
        reasons.append("Contains suspicious keyword(s)")

    if suspicious:
        return "FAKE WEBSITE ⚠️", reasons
    else:
        return "REAL WEBSITE ✅", ["No suspicious patterns detected"]

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    reasons = []
    if request.method == "POST":
        url = request.form["url"]
        result, reasons = check_website(url)

    # Inline HTML (no templates folder needed)
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Fake Website Finder</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #00c6ff, #0072ff);
                color: white;
                text-align: center;
                padding: 50px;
            }}
            input[type=text] {{
                padding: 10px;
                width: 300px;
                border-radius: 5px;
                border: none;
            }}
            button {{
                padding: 10px 20px;
                background: #ff9800;
                border: none;
                border-radius: 5px;
                color: white;
                cursor: pointer;
            }}
            .result {{
                margin-top: 20px;
                padding: 20px;
                border-radius: 10px;
            }}
            .fake {{
                background-color: #e74c3c;
            }}
            .real {{
                background-color: #2ecc71;
            }}
        </style>
    </head>
    <body>
        <h1>🔍 Fake Website Finder</h1>
        <form method="POST">
            <input type="text" name="url" placeholder="Enter website URL" required>
            <button type="submit">Check</button>
        </form>

        {f'<div class="result {"fake" if "FAKE" in result else "real"}"><h2>{result}</h2><ul>' + ''.join(f"<li>{r}</li>" for r in reasons) + "</ul></div>" if result else ""}
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
