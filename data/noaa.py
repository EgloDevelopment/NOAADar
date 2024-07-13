import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup

class images:
    def getOne(station_id):
        request_url = f"https://www.ndbc.noaa.gov/buoycam.php?station={station_id}"
        
        response = requests.get(request_url)

        image = Image.open(BytesIO(response.content))

        return image
    
    def getTest():
        request_url = f"https://whitehousecovemarina.com/wp-content/uploads/2022/11/Screen-Shot-2022-11-29-at-1.06.34-PM-1080x675.png" # Boats in a pier/dock
        #request_url = f"https://file.kelleybluebookimages.com/kbb/base/evox/CP/52722/2024-Honda-Accord-front_52722_032_1810x721_GC_cropped.png" # Honda something
        #request_url = f"https://i0.wp.com/theglorioustable.com/wp-content/uploads/2018/10/see-ocean-beyond-waves.png" # Straight fucking water
        
        response = requests.get(request_url)

        image = Image.open(BytesIO(response.content))

        return image
    
class stations:
    def getLocation(station_id):
        request_url = f"https://www.ndbc.noaa.gov/sar.php?station={station_id}"

        html = requests.get(request_url).text
        soup = BeautifulSoup(html, features="html.parser")

        coordinate_string = str(soup.findAll("b")[1])

        # Please someone just fucking shoot me, I hate it more than you do
        latitude = coordinate_string.split("<br/>")[1].split("N")[0].strip()
        longitude = coordinate_string.split("<br/>")[1].split("N")[1].split("W")[0].strip()

        return f"{latitude},-{longitude}" # Negative here because the longitude is west