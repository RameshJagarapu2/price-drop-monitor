import os
import urllib.parse
import urllib.request


# -----------------------------
# TEST PRODUCT DATA
# -----------------------------

product_name = "Test Product"
old_price = 10000
current_price = 9000


# -----------------------------
# PRICE DROP CALCULATION
# -----------------------------

if current_price < old_price:
    price_drop = old_price - current_price
    drop_percentage = (price_drop / old_price) * 100

    message = f"""🔥 PRICE DROP DETECTED!

{product_name}

Old price: ₹{old_price:,.0f}
New price: ₹{current_price:,.0f}

You save: ₹{price_drop:,.0f}
Drop: {drop_percentage:.1f}%
"""

    print(message)

    # -----------------------------
    # TELEGRAM NOTIFICATION
    # -----------------------------

    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": message
    }).encode()

    request = urllib.request.Request(
        telegram_url,
        data=data
    )

    with urllib.request.urlopen(request) as response:
        print("Telegram response:")
        print(response.read().decode())

else:
    print("No price drop detected.")
