from .degree import Degree
from .coordinates_base import EastWestCoordinate, NorthSouthCoordinate

class Declination(NorthSouthCoordinate):
    """Represents a Declination value in degrees."""
    def __init__(self, value):
        super().__init__(value)
        if not (-90 <= self.raw_decimal <= 90):
            raise ValueError(f"Declenation must be between -90° and 90°, but got {value}")

# Right Ascension (East/West)
class RightAscension(EastWestCoordinate):
    pass