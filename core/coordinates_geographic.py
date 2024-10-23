from .helper import Helper
from .degree import Degree
from .altitude import AltitudeTrue
from .coordinates_celestial import Declination
from .zenith_distance import ZenithDistance
from .coordinates_base import EastWestCoordinate, NorthSouthCoordinate

class GeographicCoordinates(Degree):
    def decimal_to_ddmmss(self) -> str:
        return super().decimal_to_ddmmss().lstrip("-")

class Latitude(GeographicCoordinates, NorthSouthCoordinate):
    pass

#    def ddmmss_to_decimal(self, input_str) -> float:
#        """Convert a D°M'S" string with N/S direction to a decimal degree."""
#        direction = input_str[-1]  # Get the last character for direction (N or S)
#        if direction not in ['N', 'S']:
#            raise ValueError("Invalid direction for Latitude. Use 'N' or 'S'.")
#        ddmmss = input_str[:-1]  # Remove the direction character from the string
#        decimal_degrees = super().ddmmss_to_decimal(ddmmss)
#        
#        # Apply negative sign for 'S' (south)
#        if direction == 'S':
#            decimal_degrees = -abs(decimal_degrees)
#        
#        return decimal_degrees
#
#    """Represents a Latitude value in degrees."""
#    def decimal_to_ddmmss(self) -> str:
#        """Convert a decimal degree to a D°M'S" format with N/S direction."""
#        direction = 'N' if self.decimal >= 0 else 'S'
#        ddmmss_format = super().decimal_to_ddmmss()
#        return f"{ddmmss_format}{direction}"

class CalculatedLatitude(Latitude):
    """Represents a Latitude value in degrees."""
    def __init__(self, altitude_true: AltitudeTrue, declination: Declination, estimated_latitude: Latitude):
        self.declination = declination
        self.zenith_distance = ZenithDistance(altitude_true)
        self.estimated_latitude = estimated_latitude
        super().__init__(self.calculate_latitude())

    def are_declination_and_latitude_in_same_hemisphere(self) -> bool:
        return self.declination >= Degree(0) and self.estimated_latitude >= Degree(0) or self.declination <= Degree(0) and self.estimated_latitude <= Degree(0)
    
    def calculate_latitude(self):
        if self.are_declination_and_latitude_in_same_hemisphere():
            if self.estimated_latitude > self.declination:
                return self.zenith_distance + self.declination
            else:
                return self.declination - self.zenith_distance
        else:
            return self.zenith_distance + self.declination
            
class Longitude(GeographicCoordinates, EastWestCoordinate):
    """
    Represents a Longitude value in degrees.
    @see https://en.wikipedia.org/wiki/Longitude
    """
    def __init__(self, value):
        super().__init__(value)
        if not (Degree(-180) <= self <= Degree(180)):
            raise ValueError(f"Longitude must be between -180° and 180°, but got {value}")
        self.string = self.decimal_to_ddmmss()

    def decimal_to_ddmmss(self) -> str:
        """Convert a decimal degree to a D°M'S" format with E/W direction."""
        direction = 'E' if self.decimal >= 0 else 'W'
        ddmmss_format = super().decimal_to_ddmmss()
        return f"{ddmmss_format}{direction}"

    def ddmmss_to_decimal(self, input_str) -> float:
        """Convert a D°M'S" string with E/W direction to a decimal degree."""
        direction = input_str[-1]  # Get the last character for direction (E or W)
        if direction not in ['E', 'W']:
            raise ValueError("Invalid direction for Longitude. Use 'E' or 'W'.")
        ddmmss = input_str[:-1]  # Remove the direction character from the string
        decimal_degrees = super().ddmmss_to_decimal(ddmmss)
        
        # Apply negative sign for 'W' (west)
        if direction == 'W':
            decimal_degrees = -abs(decimal_degrees)
        
        return decimal_degrees