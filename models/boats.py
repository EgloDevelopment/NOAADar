from ultralytics import YOLO
import os
import time

class identify:
    def simple(file_name, confidence_threshold):
        model = YOLO("boats.pt")

        station_time = file_name.split("-")[0]
        station_id = file_name.split("-")[1]

        results = model(f"storage/temp/{file_name}")

        for result in results:
            if result.boxes.cls == 8:
                result.save(filename = f"storage/saved/{station_id}-{station_time}.jpg")

        return any(box.conf > confidence_threshold and box.cls == 8 for box in results[0].boxes)
