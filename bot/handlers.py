from telegram import Bot
from bot.config import BOT_TOKEN, CHAT_ID

def send_payment_notification(email, amount):
    bot = Bot(token=BOT_TOKEN)
    message = f"New payment received:\nEmail: {email}\nAmount: {amount} EUR"
    bot.send_message(chat_id=CHAT_ID, text=message)
