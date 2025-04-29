import feedparser
import pandas as pd
import gspread
import requests

from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
from dateutil import parser

# Load Google News RSS feed
feed_url = "https://news.google.com/rss/search?q=Bangladesh&hl=en"
feed = feedparser.parse(feed_url)

filtered = []

for entry in feed.entries:
    title = entry.title
    link = entry.link
    published_raw = entry.published if hasattr(entry, "published") else date.today().isoformat()
    published = parser.parse(published_raw).strftime("%Y-%m-%d %H:%M:%S")
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

# ✅ Step 1: Check existing links in column D to prevent duplicates
existing_links = sheet.col_values(4)  # Column D = "Link"

# ✅ Step 2: Filter only new articles by link
new_rows = []
for row in filtered:
    if row[3] not in existing_links:  # row[3] = link
        new_rows.append(row)

# ✅ Step 3: Add header if sheet is empty
if len(existing_links) == 0:
    sheet.append_row(["Date", "Title", "Source", "Link", "Category", "Summary", "Tags", "Notes"])

# ✅ Step 4: Append new rows in bulk
if new_rows:
    sheet.append_rows(new_rows, value_input_option="RAW")
    print(f"✅ {len(new_rows)} new articles saved to your sheet.")
else:
    print("⚠ No new articles to add.")
