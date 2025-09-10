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
}

@app.route('/')
def index():
    all_entries = []
    for name, url in FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            all_entries.append({
                'source': name,
                'title': entry.get('title'),
                'link': entry.get('link'),
                'published': entry.get('published', '')
            })
    all_entries.sort(key=lambda x: x['published'], reverse=True)
    return render_template('index.html', entries=all_entries)

if __name__ == '__main__':
    app.run(debug=True)
