from .helper import Helper
from .degree import Degree
from .altitude import AltitudeTrue
from .declination import Declination

class Latitude(Degree):
    def __init__(self, value):
        super().__init__(value)
        if not (-90 <= self.decimal <= 90):
            raise ValueError(f"Latitude must be between -90° and 90°, but got {value}")
        self.string = Helper.ensure_two_digit_degrees(Latitude.decimal_to_ddmmss(self.decimal))

    """Represents a Latitude value in degrees."""
    @staticmethod
    def decimal_to_ddmmss(decimal_degrees: float) -> str:
        """Convert a decimal degree to a D°M'S" format with N/S direction."""
        direction = 'N' if decimal_degrees >= 0 else 'S'
        ddmmss_format = Degree.decimal_to_ddmmss(decimal_degrees)
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
        if self.declination.decimal > self.altitude_true.decimal:
            return self.zd + self.declination.decimal
        else:
            return self.declination.decimal - self.zd