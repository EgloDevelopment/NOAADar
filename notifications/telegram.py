import telegram
import asyncio

import json; env = json.load(open('config.json'))

bot = telegram.Bot(token = env["TELEGRAM_TOKEN"])
channel_id = env["TELEGRAM_CHANNEL_ID"]

class message:
    def send(time, station_id, image):
        asyncio.run(bot.send_message(chat_id = channel_id, text = f"Boat detected on {station_id} at {time}"))
        #asyncio.run(bot.send_photo(chat_id = channel_id, photo = open(f"storage/saved/{image}", "rb")))