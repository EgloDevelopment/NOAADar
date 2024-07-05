import wget as request # type: ignore // Its fucking broken in my ide
import time

class images:
    def getOne(station_id):
        current_time = str(time.time()).split(".")[0] # Scuffed af but works
        request_url = f"https://www.ndbc.noaa.gov/buoycam.php?station={station_id}"
        request.download(request_url, f"storage/temp/{current_time}-{station_id}.jpg")

        return f"{current_time}-{station_id}.jpg"

    def getMany(station_ids):
        file_array = []

        for station_id in station_ids:
            current_time = str(time.time()).split(".")[0] # Scuffed af but works
            request_url = f"https://www.ndbc.noaa.gov/buoycam.php?station={station_id}"
            request.download(request_url, f"storage/temp/{current_time}-{station_id}.jpg")
            
            file_array.append(f"{current_time}-{station_id}.jpg")

        return file_array