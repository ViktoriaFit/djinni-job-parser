import requests
import sqlite3
from bs4 import BeautifulSoup

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"

conn = sqlite3.connect("djinni.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY,
    title TEXT,
    url TEXT UNIQUE
)
""")
conn.commit()

url = "https://djinni.co/jobs/?primary_keyword=Python&exp_level=no_exp"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="job-item")

new_jobs = []
for job in jobs:
    link = job.find("a", class_="job_item__header-link")
    if link:
        title = link.text.strip().split("\n")[0]
        href = "https://djinni.co" + link["href"]
        try:
            cursor.execute("INSERT INTO jobs (title, url) VALUES (?, ?)", (title, href))
            new_jobs.append(f"{title}\n{href}")
        except sqlite3.IntegrityError:
            pass

conn.commit()

if new_jobs:
    message = "🔍 НОВЫЕ ВАКАНСИИ DJINNI\n\n"
    for i, item in enumerate(new_jobs, 1):
        message += f"{i}. {item}\n\n"
    
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message[:4000]}
    tg_response = requests.post(telegram_url, data=data)
    print(f"Новых вакансий: {len(new_jobs)} — отправлено в Telegram")
else:
    print("Новых вакансий нет")

conn.close()
