from flask import Flask, render_template
import feedparser

app = Flask(__name__)

FEEDS = {
    'FBI': 'https://www.fbi.gov/investigate/cyber/news/rss.xml',
    'KrebsOnSecurity': 'https://krebsonsecurity.com/feed/',
    'DarkReading': 'https://www.darkreading.com/rss.xml',
    'SANS ISC': 'https://isc.sans.edu/rssfeed.xml',
    'DC3': 'http://www.dc3.mil/index#news',  # Placeholder, may need scraping
    'US-CERT': 'https://www.cisa.gov/uscert/ncas/all.xml',
    'Threat Brief': 'https://threatbrief.com/feed/'
    # 'Owasp Top10': 'https://owasp.org/www-project-top-ten/all.xml',
    # 'Genai Owasp': 'https://genai.owasp.org/all.xml'
}

@app.route('/')
def index():
    all_entries = []
    for name, url in FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            summary = entry.get('summary', entry.get('description', ''))
            # Extract the first line after the title
            summary_lines = summary.splitlines()
            # Remove empty lines and lines that duplicate the title
            filtered_lines = [line.strip() for line in summary_lines if line.strip() and line.strip() != entry.get('title', '').strip()]
            first_line = filtered_lines[0] if filtered_lines else ''
            all_entries.append({
                'source': name,
                'title': entry.get('title'),
                'link': entry.get('link'),
                'published': entry.get('published', ''),
                'summary': first_line
            })
    from dateutil import parser as dateparser
    from datetime import datetime, timezone
    def parse_date(entry):
        try:
            return dateparser.parse(entry['published'])
        except Exception:
            return datetime(1970, 1, 1, tzinfo=timezone.utc)
    all_entries.sort(key=parse_date, reverse=True)
    return render_template('index.html', entries=all_entries)

if __name__ == '__main__':
    app.run(debug=True)
