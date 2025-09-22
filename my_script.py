# buff-script.py

import logging
import os
import requests
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# === CONFIG ===
BUFF_API_TOKEN = os.environ["BUFF_API_TOKEN"]
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# Buff API endpoint
URL = (
    "https://app.buff.game/api/marketplace/items"
    "?limit=100&device=pc&page=1&sort=POPULARITY_DESC"
    "&type[]=REGULAR&type[]=PREMIUM"
)
HEADERS = {
    "Authorization": f"Bearer {BUFF_API_TOKEN}",
    "User-Agent": "Mozilla/5.0",
}

logging.basicConfig(level=logging.INFO)


def send_telegram_message(text: str):
    """Send a message to your Telegram chat."""
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    try:
        r = requests.post(telegram_url, data=payload, verify=False)
        logging.info(f"Telegram sent: {r.status_code}")
    except Exception as e:
        logging.error(f"Telegram error: {e}")


def main():
    """Fetch Buff API data and send to Telegram."""
    try:
        logging.info("Fetching Buff API data...")
        response = requests.get(URL, headers=HEADERS, verify=False)
        logging.info(f"Buff API status: {response.status_code}")

        data = response.json()
        items = data.get("data")

        if not items:
            logging.warning("No items found or API error.")
            send_telegram_message("No items found or API error.")
        else:
            for item in items:
                simplified = {
                    "name": item.get("name"),
                    "price": item.get("price"),
                    "inStock": not item.get("isOutOfStock", False),
                }
                msg = (
                    f"Name: {simplified['name']}\n"
                    f"Price: {simplified['price']}\n"
                    f"In Stock: {simplified['inStock']}"
                )
                logging.info(f"Sending to Telegram: {simplified['name']}")
                send_telegram_message(msg)


if __name__ == "__main__":
    main()
