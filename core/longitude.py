from .degree import Degree

class Longitude(Degree):
    """Represents a Longitude value in degrees."""

    def decimal_to_ddmmss(self, decimal_degrees: float) -> str:
        """Convert a decimal degree to a D°M'S" format with E/W direction."""
        direction = 'E' if decimal_degrees >= 0 else 'W'
        ddmmss_format = super().decimal_to_ddmmss(decimal_degrees)
        return f"{ddmmss_format}{direction}"
