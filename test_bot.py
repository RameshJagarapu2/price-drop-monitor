import os
import urllib.parse
import urllib.request

bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
chat_id = os.environ["TELEGRAM_CHAT_ID"]

message = """🚀 Hello! PriceDropMonitor is alive.

Our first Telegram test worked!"""

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

data = urllib.parse.urlencode({
    "chat_id": chat_id,
    "text": message
}).encode()

request = urllib.request.Request(url, data=data)

with urllib.request.urlopen(request) as response:
    print(response.read().decode())
