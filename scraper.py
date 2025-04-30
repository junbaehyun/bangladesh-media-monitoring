import feedparser
import pandas as pd
import gspread
import requests

from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
from dateutil import parser

# 📌 Category rules
category_keywords = {
    "Politics": ["election", "minister", "government", "president", "law", "parliament", "prime minister"],
    "Business": ["economy", "trade", "market", "business", "investment", "company", "exports"],
    "Health": ["hospital", "health", "virus", "medical", "covid", "disease"],
    "Technology": ["tech", "AI", "satellite", "startup", "internet", "digital"],
    "Sports": ["cricket", "match", "tournament", "T20", "goal", "series"],
    "Education": ["university", "student", "school", "education", "exam"],
}

def detect_category(title):
    title_lower = title.lower()
    for category, keywords in category_keywords.items():
        if any(keyword in title_lower for keyword in keywords):
            return category
    return "General"

# 🌍 Load RSS feed
feed_url = "https://news.google.com/rss/search?q=Bangladesh&hl=en"
feed = feedparser.parse(feed_url)

filtered = []

for entry in feed.entries:
    title = entry.title
    link = entry.link
    published_raw = entry.published if hasattr(entry, "published") else date.today().isoformat()
    published = parser.parse(published_raw).strftime("%Y-%m-%d %H:%M:%S")
    source = entry.source["title"] if "source" in entry else "Unknown"
    category = detect_category(title)

    # ⬇️ Category moved to column B, Title to column E
    filtered.append([
        published,     # A: Date
        category,      # B: Category
        source,        # C: Source
        link,          # D: Link
        title,         # E: Title
        "", "", ""     # F–H: Summary, Tags, Notes
    ])

# 📤 Google Sheets connection
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Bangladesh Media Monitoring").sheet1

# ✅ Step 1: Check for duplicates by link
existing_links = sheet.col_values(4)  # Column D = Link

# ✅ Step 2: Filter only new articles
new_rows = []
for row in filtered:
    if row[3] not in existing_links:
        new_rows.append(row)

# ✅ Step 3: Add header (with Category in column B)
if len(existing_links) == 0:
    sheet.append_row(["Date", "Category", "Source", "Link", "Title", "Summary", "Tags", "Notes"])

# ✅ Step 4: Append new rows
if new_rows:
    sheet.append_rows(new_rows, value_input_option="RAW")
    print(f"✅ {len(new_rows)} new articles saved to your sheet.")
else:
    print("⚠ No new articles to add.")
