import schedule
import os

import data.noaa as noaa
import data.marine as marine
import models.boats as boats

import notifications.telegram as telegram


def main():
    images = noaa.images.getMany(["46011", "46054", "46086"])

    for file_location in images:
        is_detected = boats.identify.simple(file_location)

        if is_detected == True:
            time = file_location.split("-")[0]
            station = file_location.split("-")[1].split(".")[0]

            telegram.message.send(time, station, "image")
        else:
            os.remove(f"storage/temp/{file_location}") 

main()