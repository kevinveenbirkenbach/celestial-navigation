from .degree import Degree
from .helper import Helper
class Longitude(Degree):
    """Represents a Longitude value in degrees."""
    def __init__(self, value):
        super().__init__(value)
        if not (-180 <= self.decimal <= 180):
            raise ValueError(f"Longitude must be between -180° and 180°, but got {value}")
        self.string = Longitude.decimal_to_ddmmss(self.decimal)

    @staticmethod
    def decimal_to_ddmmss(decimal_degrees: float) -> str:
        """Convert a decimal degree to a D°M'S" format with E/W direction."""
        direction = 'E' if decimal_degrees >= 0 else 'W'
        ddmmss_format = Degree.decimal_to_ddmmss(decimal_degrees)
        return f"{ddmmss_format}{direction}"