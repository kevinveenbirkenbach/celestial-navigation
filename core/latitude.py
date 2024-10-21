from .helper import Helper
from .degree import Degree
from .altitude import AltitudeTrue
from .declination import Declination
from .zenith_distance import ZenithDistance

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
    def __init__(self, altitude_true: AltitudeTrue, declination: Declination, estimated_latitude: Latitude):
        self.declination = declination
        self.zenith_distance = ZenithDistance(altitude_true)
        self.estimated_latitude = estimated_latitude
        super().__init__(self.calculate_latitude())

    def are_declination_and_latitude_in_same_hemisphere(self) -> bool:
        return self.declination.decimal >= 0 and self.estimated_latitude.decimal >= 0 or self.declination.decimal <= 0 and self.estimated_latitude.decimal <= 0
    
    def calculate_latitude(self):
        if self.are_declination_and_latitude_in_same_hemisphere():
            if self.estimated_latitude.decimal > self.declination.decimal:
                return self.zenith_distance.decimal + self.declination.decimal
            else:
                return self.declination.decimal - self.zenith_distance.decimal
        else:
            return self.zenith_distance.decimal + self.declination.decimal
            


