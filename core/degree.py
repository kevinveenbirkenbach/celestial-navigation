import re

class Degree:
    def __init__(self, value):
        if isinstance(value, str):
            angle = Degree.ddmmss_to_decimal(value)
        elif isinstance(value, int) or isinstance(value, float):
            angle = value
        else:
            raise TypeError(f"The value '{value}' is of the wrong type: {type(value).__name__}.")
        self.raw_decimal = angle #contains the non-normalized angle
        self.decimal = Degree.normalize_angle(angle)
        self.string = Degree.decimal_to_ddmmss(self.decimal)

    @staticmethod
    def normalize_angle(angle):
        """
        Normalize an angle to be within the range [0, 360).
        
        Parameters:
        angle (float): The angle to normalize.

        Returns:
        float: The normalized angle.
        """
        while angle >= 360:
            angle -= 360
        while angle <= -360:
            angle += 360
        return angle

    @staticmethod
    def ddmmss_to_decimal(input_str):
        """Parse a string in the format of degrees, minutes, and seconds to decimal degrees."""
        dms_pattern = re.compile(r"(?P<degrees>-?\d+\.?\d*)°(?P<minutes>\d*\.?\d*)'(?P<seconds>\d*\.?\d*)\"?(?P<direction>[EWNS])?")
        match = dms_pattern.match(input_str)
        if not match:
            raise ValueError(f"Invalid format. Use D°M'S\" format instead of {input_str}.")
        
        degrees = float(match.group('degrees'))
        minutes = float(match.group('minutes')) if match.group('minutes') else 0
        seconds = float(match.group('seconds')) if match.group('seconds') else 0
        direction = match.group('direction')
        
        # Calculate the decimal degree
        decimal_degrees = degrees + minutes / 60 + seconds / 3600

        # Adjust the sign based on the direction
        if direction in ['W', 'S']:
            decimal_degrees = -abs(decimal_degrees)  # West and South should be negative
        elif direction in ['E', 'N']:
            decimal_degrees = abs(decimal_degrees)   # East and North should be positive
        
        return decimal_degrees
    
    @staticmethod
    def decimal_to_ddmmss(decimal_degrees: float) -> str:
        """
        Convert a decimal degree value to a D°M'S" string format without the direction.
        Subclasses should override this method to provide direction-specific formatting.
        """

        abs_degrees = abs(decimal_degrees)

        # Extract degrees, minutes, and seconds
        degrees = int(abs_degrees)
        minutes = int((abs_degrees - degrees) * 60)
        seconds = (abs_degrees - degrees - minutes / 60) * 3600

        # Handle rounding errors that cause seconds to be 60.00
        if round(seconds) == 60:
            seconds = 0
            minutes += 1

        # If minutes reach 60, increment degrees and reset minutes
        if round(minutes) == 60:
            minutes = 0
            degrees += 1

        # Format into D°M'S" format (without direction)
        return f"{degrees:03d}°{minutes:02d}'{seconds:05.2f}\""
    
    def __str__(self):
        return self.string