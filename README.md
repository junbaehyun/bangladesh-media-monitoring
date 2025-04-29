# bangladesh-media-monitoring

it can generate media monitoring automatically 

ate:
markdown
Copy
Edit
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
2. Set up a virtual environment (optional but recommended)
bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
3. Create your Google service account key
Download the service_account.json file from your Google Cloud project

Place it in this project directory (do not upload to GitHub!)

4. Run the scraper
bash
Copy
Edit
python scraper.py
🔐 Important
Make sure .gitignore includes your service_account.json and .venv/

Do not upload secrets to GitHub

📦 Dependencies
feedparser

gspread

oauth2client

pandas

Install them with:

bash
Copy
Edit
pip install -r requirements.txt
✍️ Author
Junbae Hyun

GitHub: @junbaehyun

yaml
Copy
Edit

---

Would you like me to generate the matching `requirements.txt` file next? (So others can install dependencies in one line.)

<img width="1887" alt="image" src="https://github.com/user-attachments/assets/f7ff301a-3713-4f31-9c7d-4798a6ce17f0" />
