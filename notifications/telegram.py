import json; env = json.load(open("config.json"))

import telegram
import asyncio
from io import BytesIO
import time

bot = telegram.Bot(token = env["TELEGRAM_TOKEN"])
channel_id = env["TELEGRAM_CHANNEL_ID"]

class alert:
    def send():
        current_time = time.strftime("%H:%M:%S")

        loop = asyncio.get_event_loop()

        if loop.is_running(): # Super scuffed and I hate my life but it works
            loop.create_task(bot.send_message(chat_id=channel_id, text=f"Running NOAADar at {current_time}"))
        else:
            loop.create_task(bot.send_message(chat_id=channel_id, text=f"Running NOAADar at {current_time}"))

class message:
    def send(station_id, station_image, station_location):
        current_time = time.strftime("%H:%M:%S")

        station_latitude = station_location.split(",")[0]
        station_longitude = station_location.split(",")[1]

        image = BytesIO()
        station_image.save(image, format="JPEG")
        image.seek(0)

        loop = asyncio.get_event_loop()

        if loop.is_running(): # Super scuffed and I hate my life but it works
            loop.create_task(bot.send_message(chat_id=channel_id, text=f"Boat detected on {station_id} at {current_time}"))
            loop.create_task(bot.send_photo(chat_id=channel_id, photo=image))
            loop.run_until_complete(bot.sendLocation(chat_id=channel_id, longitude=station_longitude, latitude=station_latitude, horizontal_accuracy=20))
        else:
            loop.run_until_complete(bot.send_message(chat_id=channel_id, text=f"Boat detected on {station_id} at {current_time}"))
            loop.run_until_complete(bot.send_photo(chat_id=channel_id, photo=image))
            loop.run_until_complete(bot.sendLocation(chat_id=channel_id, longitude=station_longitude, latitude=station_latitude, horizontal_accuracy=20))
