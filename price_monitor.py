import json
import os
import urllib.parse
import urllib.request


# -----------------------------
# LOAD PRODUCTS
# -----------------------------

with open("products.json", "r", encoding="utf-8") as file:
    products = json.load(file)


# -----------------------------
# CHECK EACH PRODUCT
# -----------------------------

for product in products:

    product_name = product["name"]
    target_price = product["target_price"]

    # Temporary test price
    current_price = 9000

    print(f"Checking: {product_name}")
    print(f"Target price: ₹{target_price:,.0f}")
    print(f"Current price: ₹{current_price:,.0f}")


    # -----------------------------
    # PRICE DROP CHECK
    # -----------------------------

    if current_price <= target_price:

        message = f"""🔥 PRICE DROP DETECTED!

{product_name}

Current price: ₹{current_price:,.0f}
Target price: ₹{target_price:,.0f}

🛒 Product:
{product["url"]}
"""

        print(message)


        # -----------------------------
        # TELEGRAM
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
            print(response.read().decode())

    else:
        print("No price drop detected.")
