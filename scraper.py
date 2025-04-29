import feedparser
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date

# Load Google News RSS feed
feed_url = "https://news.google.com/rss/search?q=Bangladesh&hl=en"
feed = feedparser.parse(feed_url)

filtered = []

for entry in feed.entries:
    title = entry.title
    link = entry.link
    published = entry.published if hasattr(entry, "published") else date.today().isoformat()
    source = entry.source["title"] if "source" in entry else "Unknown"
    
    filtered.append([
        published,
        title,
        source,
        link,
        "Bangladesh",  # Category
        "", "", ""      # Summary, Tags, Notes
    ])

# Send to Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Bangladesh Media Monitoring").sheet1
sheet.clear()
sheet.append_row(["Date", "Title", "Source", "Link", "Category", "Summary", "Tags", "Notes"])

for row in filtered:
    sheet.append_row(row)

print(f"✅ {len(filtered)} articles from Google News saved to your sheet.")
