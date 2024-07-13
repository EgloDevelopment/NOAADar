import json; env = json.load(open("config.json"))

import data.noaa as noaa
import models.boats as boats

import notifications.telegram as telegram

if env["ALERT_ON_RUN"] == "YES":
    telegram.alert.send()

for station in env["STATIONS"]:
    if env["MODE"] == "TESTING":
        image = noaa.images.getTest()
    else:
        image = noaa.images.getOne(station)

    identified = boats.identify.simple(image)
    print(f"{station}: {identified}")

    if identified == True:
        location = noaa.stations.getLocation(station)
        telegram.message.send(station, location, image)