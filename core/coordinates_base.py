from .degree import Degree
from .helper import Helper

# North/South coordinate base class
class NorthSouthCoordinate(Degree):
    def __init__(self, value):
        super().__init__(value)
        if not (Degree(-90) <= self <= Degree(90)):
            raise ValueError(f"North-South Coordinate must be between -90° and 90°, but got {value}")
        self.string = Helper.ensure_two_digit_degrees(self.decimal_to_ddmmss())
    
    def ddmmss_to_decimal(self, input_str):
        # Handles N/S directions and converts to decimal degrees
        direction = input_str[-1]  # Last character should be N/S
        if direction not in ['N', 'S']:
            raise ValueError("Invalid direction for NorthSouthCoordinate. Must be 'N' or 'S'.")
        input_str = input_str[:-1]  # Remove the direction
        decimal = super().ddmmss_to_decimal(input_str)
        return decimal if direction == 'N' else -decimal
    
    def decimal_to_ddmmss(self) -> str:
        """Convert a decimal degree to a D°M'S" format with N/S direction."""
        direction = 'N' if self.decimal >= 0 else 'S'
        ddmmss_format = super().decimal_to_ddmmss()
        return f"{ddmmss_format}{direction}"

# East/West coordinate base class
class EastWestCoordinate(Degree):
    pass