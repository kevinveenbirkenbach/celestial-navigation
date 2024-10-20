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
    def __init__(self, altitude_true: AltitudeTrue, declination: Declination):
        self.declination = declination
        self.zenith_distance = ZenithDistance(altitude_true)
        super().__init__(self.calculate_latitude())

    def calculate_latitude(self):
        # Apply the rules based on the Noon Sight form:
        if self.declination.string.endswith('N') and self.zenith_distance.decimal >= self.declination.decimal:
            latitude_value = self.zenith_distance.decimal + self.declination.decimal
            direction = 'N'
        elif self.declination.string.endswith('S') and self.zenith_distance.decimal >= self.declination.decimal:
            latitude_value = self.zenith_distance.decimal + self.declination.decimal
            direction = 'S'
        elif self.declination.string.endswith('N') and self.zenith_distance.decimal < self.declination.decimal:
            latitude_value = self.declination.decimal.decimal - self.zenith_distance.decimal
            direction = 'N'
        elif self.declination.string.endswith('S') and self.zenith_distance.decimal < self.declination.decimal:
            latitude_value = self.declination.decimal - self.zenith_distance.decimal
            direction = 'S'
        else:
            # Opposite hemispheres
            latitude_value = self.zenith_distance.decimal - self.declination.decimal
            direction = 'N' if self.zenith_distance.decimal > self.declination.decimal else 'S'

        # Return the latitude with the correct sign based on the direction
        return latitude_value if direction == 'N' else -latitude_value
