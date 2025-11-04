from flask import Flask, request
import os
from telegram import Bot

app = Flask(__name__)

# Bot token Environment Variable’dan olinadi
bot_token = os.getenv("8576487577:AAFgmyymECImZgXduHyZfCyMKcbnSpdS21A")
bot = Bot(token=bot_token)

@app.route("/", methods=["GET"])
def home():
    return "Bot ishga tushdi!"

@app.route("/send/<chat_id>/<message>", methods=["GET"])
def send_message(chat_id, message):
    try:
        bot.send_message(chat_id=chat_id, text=message)
        return f"Xabar yuborildi: {message}"
    except Exception as e:
        return f"Xato: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
