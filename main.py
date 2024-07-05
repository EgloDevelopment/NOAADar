import data.noaa as noaa
import data.marine as marine
import models.boats as boats

images = noaa.images.getMany(["40019", "40010"])

for image in images:
    boats.identify.simple(image, 0.5)