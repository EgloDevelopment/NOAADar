import requests
from PIL import Image
from io import BytesIO

class images:
    def getOne(station_id):
        request_url = f"https://www.ndbc.noaa.gov/buoycam.php?station={station_id}"
        
        response = requests.get(request_url)

        image = Image.open(BytesIO(response.content))

        return image
    
    def getTest():
        request_url = f"https://whitehousecovemarina.com/wp-content/uploads/2022/11/Screen-Shot-2022-11-29-at-1.06.34-PM-1080x675.png"
        
        response = requests.get(request_url)

        image = Image.open(BytesIO(response.content))

        return image