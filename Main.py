from telegram import Bot
import random
import time
from datetime import datetime, timedelta

BOT_TOKEN = "7536402446:AAEF7g4iE4yvYTk1fjxysKVhULeLYJwp5OQ"
CHAT_ID = "@lifechangerbot09"

bot = Bot(token=BOT_TOKEN)

pairs = ["EUR/USD", "USD/JPY", "GBP/USD", "USD/PKR", "USD/TRY", "EUR/JPY", "GOLD", "SILVER"]

def generate_signal():
    pair = random.choice(pairs)
    direction = random.choice(["BUY 🔼", "SELL 🔽"])
    accuracy = round(random.uniform(80.0, 99.9), 2)
    utc_time = datetime.utcnow() + timedelta(hours=5)
    entry_time = utc_time.strftime("%H:%M")
    return f"""📊 LIFE_CHANGER_BOT

PAIR: {pair}
DIRECTION: {direction}
TIMEFRAME: 5 Min
ACCURACY: {accuracy}%
ENTRY TIME: 2 min later
UTC TIME: {entry_time}

📲 Register Quotex Now  
https://broker-qx.pro/sign-up/?lid=1458419
"""

while True:
    try:
        bot.send_message(chat_id=CHAT_ID, text=generate_signal())
        print("✅ Signal Sent at", datetime.now().strftime("%H:%M:%S"))
    except Exception as e:
        print("❌ Error:", e)
    time.sleep(600)
