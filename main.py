import json; env = json.load(open("config.json"))

import data.noaa as noaa
import models.boats as boats

import notifications.telegram as telegram

for station in env["STATIONS"]:

    if env["MODE"] == "TESTING":
        image = noaa.images.getTest()
    else:
        image = noaa.images.getOne(station)

    if boats.identify.simple(image) == True:
        telegram.message.send(station, image)