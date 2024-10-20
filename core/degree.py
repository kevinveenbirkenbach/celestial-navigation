import re

class Degree:
    def __init__(self, value):
        if isinstance(value, str):
            self.string  = value
            self.decimal = self.ddmmss_to_decimal(value)
        elif isinstance(value, int) or isinstance(value, float):
            self.decimal = value
            self.string = self.decimal_to_ddmmss(value)
        else:
            raise TypeError(f"The value '{value}' is of the wrong type: {type(value).__name__}.")

    def ddmmss_to_decimal(self, input_str):
        """Parse a string in the format of degrees, minutes, and seconds to decimal degrees."""
        dms_pattern = re.compile(r"(?P<degrees>-?\d+\.?\d*)°(?P<minutes>\d*\.?\d*)'(?P<seconds>\d*\.?\d*)\"?(?P<direction>[EWNS])?")
        match = dms_pattern.match(input_str)
        if not match:
            raise ValueError(f"Invalid format. Use D°M'S\" format instead of {input_str}.")
        
        degrees = float(match.group('degrees'))
        minutes = float(match.group('minutes')) if match.group('minutes') else 0
        seconds = float(match.group('seconds')) if match.group('seconds') else 0
        
        decimal_degrees = degrees + minutes / 60 + seconds / 3600
        
        return decimal_degrees
    
    def decimal_to_ddmmss(self, decimal_degrees: float) -> str:
        """
        Convert a decimal degree value to a D°M'S" string format without the direction.
        Subclasses should override this method to provide direction-specific formatting.
        """

        abs_degrees = abs(decimal_degrees)

        # Extract degrees, minutes, and seconds
        degrees = int(abs_degrees)
        minutes = int((abs_degrees - degrees) * 60)
        seconds = (abs_degrees - degrees - minutes / 60) * 3600

        # Format into D°M'S" format (without direction)
        return f"{degrees}°{minutes}'{seconds:.2f}\""
    
    def __str__(self):
        return self.string