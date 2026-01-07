import os
import logging
import threading
import time
import requests
from flask import Flask
from flask_restful import Resource, Api

from pyrogram import Client, idle
from pyromod import listen
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

# -------------------- Logging Setup -------------------- #
logging.basicConfig(
    level=logging.INFO,
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - \033[32m%(pathname)s: \033[31m\033[1m%(message)s \033[0m"
)

# -------------------- Pyrogram Bot Setup -------------------- #
Japanese = Client(
    "JapaneseXStringSession",
    api_id=os.environ.get("API_ID"),
    api_hash=os.environ.get("API_HASH"),
    bot_token=os.environ.get("BOT_TOKEN"),
    in_memory=True,
    plugins={'root': 'Japanese'},  # Keep your plugin folder as is
)

# -------------------- Flask + Keep-Alive Setup -------------------- #
app = Flask(__name__)
api = Api(app)

class Greeting(Resource):
    def get(self):
        return {"message": "Japanese X String Session is Up & Running!"}

api.add_resource(Greeting, '/')

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    url = os.environ.get("PING_URL", "https://your-render-url.onrender.com").strip()
    while True:
        try:
            print(f"[KeepAlive] Pinging {url}")
            requests.get(url, timeout=10)
        except Exception as e:
            print(f"[KeepAlive] Failed to ping: {e}")
        time.sleep(600)  # Ping every 10 minutes

# Start Flask server in a daemon thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

# Start keep-alive thread
threading.Thread(target=keep_alive, daemon=True).start()

# -------------------- Main Execution -------------------- #
if __name__ == "__main__":
    logging.info("Starting JapaneseXStringSession bot")
    try:
        Japanese.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")

    uname = Japanese.me.username
    logging.info(f"@{uname} is now running!")
    idle()
    Japanese.stop()
    logging.info("JapaneseXStringSession stopped!")
