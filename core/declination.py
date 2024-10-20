from .degree import Degree

class Declination(Degree):
    """Represents a Declination value in degrees."""
    def __init__(self, value):
        super().__init__(value)
        if not (-90 <= self.decimal <= 90):
            raise ValueError(f"Declenation must be between -90° and 90°, but got {value}")