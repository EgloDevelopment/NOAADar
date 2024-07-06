import json; env = json.load(open("config.json"))

from ultralytics import YOLO

class identify:
    def simple(image):
        model = YOLO("models/storage/boats-quick.pt")

        results = model(image)

        #for result in results:
            #result.save(filename = "test.jpg")

        for result in results[0].boxes:
            if result.conf > float(env["MINIMUM_CONFIDENCE_LEVEL"]) and result.cls == 8:
                return True
            else:
                return False