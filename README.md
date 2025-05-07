

it can generate media monitoring automatically 

<img width="1689" alt="image" src="https://github.com/user-attachments/assets/6f486214-5647-4255-8536-8fe62bd678a5" />


# 🇧🇩 Bangladesh Media Monitoring

A Python-based scraper that automatically collects and filters recent news articles about **Bangladesh** from **Google News**, and sends them to a connected **Google Sheet** for easy monitoring and reporting.

---

## 🔍 What It Does

- ✅ Scrapes news articles from Google News RSS feed for the keyword: `Bangladesh`
- ✅ Extracts article title, publish date, source, and link
- ✅ Filters only relevant results
- ✅ Automatically saves results to a structured Google Sheet

---

## 📁 Example Output in Google Sheet

| Date       | Title                             | Source     | Link        |
|------------|------------------------------------|------------|-------------|
| 2025-04-29 | Bangladesh inflation hits 8%       | Reuters    | [link](https://...) |
| 2025-04-29 | Dhaka hosts regional trade summit  | The Diplomat | [link](https://...) |

---

## 🚀 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/junbaehyun/bangladesh-media-monitoring.git
cd bangladesh-media-monitoring
```


### 2. Set up a virtual environment (optional but recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Create your Google service account key
1. Download the service_account.json file from your Google Cloud project
2. Place it in this project directory (do not upload to GitHub!)


### 4. Run the scraper
```bash
python scraper.py
```

### 🔐 Important
Make sure .gitignore includes your service_account.json and .venv/

Do not upload secrets to GitHub

### 📦 Dependencies
feedparser
gspread
oauth2client
pandas

Install them with:

```bash
pip install -r requirements.txt
```



## 🇰🇿 Kazakhstan News Monitoring (Auto Scheduler with Google Cloud)

This project automatically collects Kazakhstan-related news articles via RSS, classifies them by category, and saves them to a Google Spreadsheet. It runs daily using **Google Cloud Functions** and **Cloud Scheduler**.

---

### ✅ Features

* Google News RSS feed parsing (`feedparser`)
* Auto-categorization by keywords (Politics, Business, etc.)
* Google Sheets integration via `gspread`
* Daily automation using Cloud Functions + Scheduler

---

### 🛍️ How It Works

```
Cloud Scheduler (9:00 AM Daily)
        ↓ triggers
Cloud Functions (HTTP Endpoint with Python script)
        ↓ runs
RSS feed → filter + categorize → store in Google Sheet
```

---

### 💠 Setup Process

#### 1. **Prepare Your Code**

* `main.py`
  Contains the core logic and HTTP trigger function:

```python
import functions_framework

@functions_framework.http
def kazakhstan_monitor(request):
    return main_logic()
```

* `requirements.txt`
  Must include these:

```
feedparser
pandas
gspread
oauth2client
functions-framework
```

* `service_account.json`
  Google Cloud service account with access to Google Sheets.
  This will be set as an environment variable `GOOGLE_CREDENTIALS`.

---

#### 2. **Deploy to Google Cloud Functions**

```bash
gcloud functions deploy kazakhstan_monitor \
  --runtime python311 \
  --trigger-http \
  --entry-point kazakhstan_monitor \
  --allow-unauthenticated \
  --source=.
```

---

#### 3. **Set Environment Variable**

In **Google Cloud Console > Cloud Functions > Configuration**,
add:

```
GOOGLE_CREDENTIALS = (paste entire content of your service_account.json as one line)
```

---

#### 4. **Create a Cloud Scheduler Job**

```bash
gcloud scheduler jobs create http kazakhstan-monitor-job \
  --schedule="0 9 * * *" \
  --http-method=GET \
  --uri=https://REGION-PROJECT.cloudfunctions.net/kazakhstan_monitor \
  --time-zone="Asia/Seoul"
```

> Replace `REGION-PROJECT` with your actual Cloud Function endpoint.

---

### ⚙️ Automation Logic (Behind the Scenes)

* `Cloud Scheduler` sends a **GET request** to your Cloud Function every day at 9 AM.
* The Cloud Function:

  * Fetches RSS feed
  * Classifies news
  * Connects to your Google Sheet via the service account
  * Appends new data
* The system avoids duplicates using the article link as unique ID.

---

### ✅ Success Confirmation

* You can **test manually** via:

```bash
gcloud functions call kazakhstan_monitor
```

* Or check:

  * Cloud Logs (Cloud Functions > Logs)
  * Your Google Sheet updates
  * Scheduler run history

---

### 🔐 Security Note

Your `service_account.json` must be set **as an environment variable** securely — never expose it in code or public repositories.

---

### 📌 Future Ideas

* Translate summaries (via Google Translate API)
* Notify via Slack or email
* Store backup in BigQuery


### ✍️ Author
Junbae Hyun

GitHub: @junbaehyun



