import data.noaa as noaa
import data.marine as marine
import models.boats as boats

images = noaa.images.getMany(["46011", "46054", "46086"])

for image in images:
    if boats.identify.simple(image, 0.5) == True:
        print("Recorded a boat at " + image)