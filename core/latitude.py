from .helper import Helper
from .degree import Degree
from .altitude import AltitudeTrue
from .declination import Declination

class Latitude(Degree):
    """Represents a Latitude value in degrees."""
    def decimal_to_ddmmss(self, decimal_degrees: float) -> str:
        """Convert a decimal degree to a D°M'S" format with N/S direction."""
        direction = 'N' if decimal_degrees >= 0 else 'S'
        ddmmss_format = super().decimal_to_ddmmss(decimal_degrees)
        return f"{ddmmss_format}{direction}"

class CalculatedLatitude(Latitude):
    """Represents a Latitude value in degrees."""
    def __init__(self, altitude_true: AltitudeTrue, declination: Declination):
        self.declination = declination
        self.altitude_true = altitude_true
        self.zd = self.calculateZD()
        super().__init__(self.calculate_latitude())

    def calculateZD(self):
        return 90 - self.altitude_true.decimal

    def calculate_latitude(self):
        if self.declination > self.altitude_true:
            return ZD + self.declination
        else:
            return self.declination - ZD

    def __str__(self):
        return f"ZD: {self.zd} \n{super().__str__()}"