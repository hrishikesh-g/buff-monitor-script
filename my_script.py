import logging
import os
import requests
import urllib3
import azure.functions as func

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Read secrets from environment
BUFF_API_TOKEN = os.environ["BUFF_API_TOKEN"]
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# Buff API endpoint
URL = "https://app.buff.game/api/marketplace/items?limit=100&device=pc&page=1&sort=POPULARITY_DESC&type[]=REGULAR&type[]=PREMIUM"
HEADERS = {
    "Authorization": f"Bearer {BUFF_API_TOKEN}",
    "User-Agent": "Mozilla/5.0"
}

def send_telegram_message(text: str):
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    try:
        requests.post(telegram_url, data=payload, verify=False)
    except Exception as e:
        logging.error(f"Telegram error: {e}")

def main(mytimer: func.TimerRequest) -> None:
    """This runs automatically on the schedule in function.json."""
    try:
        response = requests.get(URL, headers=HEADERS, verify=False)
        data = response.json()
        items = data.get("data")
        if not items:
            send_telegram_message("No items found or API error.")
        else:
            for item in items:
                simplified = {
                    "name": item.get("name"),
                    "price": item.get("price"),
                    "inStock": not item.get("isOutOfStock", False)
                }
                msg = f"Name: {simplified['name']}\nPrice: {simplified['price']}\nIn Stock: {simplified['inStock']}"
                send_telegram_message(msg)
    except Exception as e:
        send_telegram_message(f"Script error: {e}")
