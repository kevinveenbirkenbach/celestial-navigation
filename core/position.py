from .longitude import Longitude
from .latitude import Latitude
class Position:
    """ https://de.wikipedia.org/wiki/Geographische_Koordinaten """
    def __init__(self, longitude: Longitude, latitude: Latitude):
        self.latitude = latitude
        self.longitude = longitude
    def __str__(self):
        return f"Lat. {self.latitude.string} φ,  Lon. {self.longitude.string} λ"
    
