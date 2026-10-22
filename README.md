# 🔍 Fake Website Finder

A beginner-friendly **Flask web app** that checks a URL with simple rules and tells you whether it looks **FAKE ⚠️** or **REAL ✅**, with clear reasons.

---

## 🎯 Objective
Help users spot potentially fraudulent websites and stay safe online.

## 🚀 Features
- 🔒 Detects missing HTTPS
- 📏 Flags unusually long URLs (over 75 characters)
- 🔢 Identifies IP addresses used instead of domain names
- 🕵️ Scans for suspicious keywords (login, verify, secure, update, bank, account)
- 🟥🟩 Shows a red or green result with the reasons

## 🧰 Tech Stack
- Python 3
- Flask
- HTML and CSS (inline in app.py)

## 🛠 Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/epsonraj050-art/aifakewebdetector.git
cd aifakewebdetector
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate    # macOS / Linux
```

3. Install Flask:

```bash
pip install flask
```

4. Run the app:

```bash
python app.py
```

5. Open **http://127.0.0.1:5000** in your browser.

## 🧪 How It Works
The app applies four rules to the URL you enter:

| Rule | Check | Flagged when |
|------|-------|--------------|
| 1 | HTTPS | URL does not start with https:// |
| 2 | Length | URL is longer than 75 characters |
| 3 | IP address | URL uses an IP instead of a domain |
| 4 | Keywords | URL contains words like login, verify, bank |

If any rule matches, the site is marked **FAKE WEBSITE ⚠️** and every reason is listed. Otherwise it is marked **REAL WEBSITE ✅**.

## 📌 Example
- Input: http://192.168.1.1/verify-account
- Result: FAKE WEBSITE ⚠️ (no HTTPS, IP address used, suspicious keywords)

## ⚠️ Limitations
- Rule-based only, so it can give false positives and false negatives.
- It does not check domain age, SSL certificates, or blacklists.
- Use it for learning, not as your only security check.

## 🔮 Future Improvements
- Machine learning based detection
- Domain age and WHOIS lookup
- Check URLs against phishing blacklists

## 👤 Author
**epsonraj050-art**
