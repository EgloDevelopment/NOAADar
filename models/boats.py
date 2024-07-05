from ultralytics import YOLO
import os
import time

class identify:
    def simple(file_location, confidence_threshold):
        model = YOLO("boats.pt")

        results = model(f"storage/temp/{file_location}")

        for result in results[0].boxes:
            if result.conf > confidence_threshold and result.cls == 8:
                return True
            return False