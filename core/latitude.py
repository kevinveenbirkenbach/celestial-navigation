from .helper import Helper
from .degree import Degree

class Latitude(Degree):
    """Represents a Latitude value in degrees."""
    def __init__(self, true_altitude, declination_str):
        self.true_altitude = true_altitude
        self.declination = Helper.parse_ddmmss(declination_str)  # Deklination in DMS, Umwandlung in Dezimalgrad

    def calculate_latitude(self):
        """Calculate the latitude using declination and true altitude (ZD = 90° - TA)."""
        ZD = 90 - self.true_altitude
        if self.declination > self.true_altitude:
            return ZD + self.declination
        else:
            return self.declination - ZD
