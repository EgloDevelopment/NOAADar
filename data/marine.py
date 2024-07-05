import wget as request # type: ignore // Its fucking broken in my ide
import time

class checks:
    def reportedWithinRadius(coordinates):
        request_url = f"http(s)://ais.marineplan.com/location/2/locations.json?area={coordinates}"
        print(request.get(request_url))
        return True