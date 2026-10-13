# Djinni Job Parser

Python parser that scrapes Python junior vacancies from Djinni.co.ua and sends new ones to Telegram.

## What it does

- Downloads Djinni job listing page
- Parses HTML with BeautifulSoup
- Extracts job title and URL
- Stores jobs in SQLite (prevents duplicates)
- Sends new vacancies to Telegram bot

## Technologies

- **Python 3.12**
- **BeautifulSoup4** — HTML parsing
- **requests** — HTTP requests
- **SQLite** — data storage
- **Telegram Bot API** — notifications

## How it works

1. Script downloads Djinni job page via `requests`
2. BeautifulSoup parses HTML and finds all job cards
3. For each job:
   - Extracts title and URL
   - Tries to insert into SQLite (UNIQUE constraint prevents duplicates)
   - If new — adds to list
4. If new vacancies found — sends formatted message to Telegram
5. If nothing new — prints "No new vacancies"

## Setup

1. Clone the repository:
2. Install dependencies:
3. Open `djinni_parser_public.py` and replace the placeholders:
- `YOUR_BOT_TOKEN_HERE` — with your Telegram bot token
- `YOUR_CHAT_ID_HERE` — with your Telegram chat ID

4. Run the parser:
## Author

Viktoria Zykova — Junior Python / AI Developer
GitHub: https://github.com/ViktoriaFit
