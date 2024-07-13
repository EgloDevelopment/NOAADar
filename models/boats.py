import json; env = json.load(open("config.json"))

from ultralytics import YOLO
import random
import os

class identify:
    def simple(image):
        model = YOLO("models/storage/boats-quick.pt")

        results = model(image)

        if env["SAVE_IMAGES"] == "YES":
            if not os.path.exists("saved"):
                os.makedirs("saved")

            for result in results:
                random_string = ''.join(random.choice("0123456789abcdefghijklmnopqrstuvwxyz") for i in range(24)) # Long af because of how often the script runs
                result.save(filename = f"saved/{random_string}.jpg")

        try:
            for result in results:
                if result[0].boxes.conf > float(env["MINIMUM_CONFIDENCE_LEVEL"]) and result[0].boxes.cls == 8: # 8 is number for boats
                    return True
        except:
            pass # If there is nothing (which there often is) it will break 
            
        return False