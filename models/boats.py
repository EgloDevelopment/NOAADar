from ultralytics import YOLO

import json; env = json.load(open('config.json'))

class identify:
    def simple(file_location):
        model = YOLO("boats.pt")

        results = model(f"storage/temp/{file_location}")

        #for result in results:
            #result.save(filename = f"storage/saved/{file_location}")

        for result in results[0].boxes:
            if result.conf > float(env["MINIMUM_CONFIDENCE_LEVEL"]) and result.cls == 8:
                return True
            else:
                return False