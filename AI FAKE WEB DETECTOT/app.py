from flask import Flask, request
import re

app = Flask(__name__)

# --- Simple Rule-Based Fake Website Detector ---
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
