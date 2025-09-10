 # Python-based web app to aggregate cybersecurity news feeds from FBI, KrebsOnSecurity, DarkReading, SANS ISC, DC3, US-CERT, and Threat Brief using Flask.

# Cybersecurity News Aggregator

This Flask app aggregates news from top cybersecurity sources:
- FBI
- KrebsOnSecurity
- DarkReading
- SANS ISC
- DC3
- US-CERT
- Threat Brief

## Setup

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the app:
   ```sh
   python newsfeeder/app.py
   ```

Visit http://127.0.0.1:5000/ in your browser.

---

Some feeds may require scraping if no RSS is available. DC3 is a placeholder and may need custom handling.
