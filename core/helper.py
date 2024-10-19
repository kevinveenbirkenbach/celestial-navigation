import re
from datetime import timedelta

class Helper:
    @staticmethod
    def parse_ddmmss(input_str):
        """Parse a string in the format of degrees, minutes, and seconds to decimal degrees."""
        dms_pattern = re.compile(r"(?P<degrees>-?\d+\.?\d*)°(?P<minutes>\d*\.?\d*)'(?P<seconds>\d*\.?\d*)\"?(?P<direction>[EWNS])?")
        match = dms_pattern.match(input_str)
        if not match:
            raise ValueError(f"Invalid format. Use D°M'S\" format instead of {input_str}.")
        
        degrees = float(match.group('degrees'))
        minutes = float(match.group('minutes')) if match.group('minutes') else 0
        seconds = float(match.group('seconds')) if match.group('seconds') else 0
        direction = match.group('direction')
        
        decimal_degrees = degrees + minutes / 60 + seconds / 3600
        
        # Adjust for direction
        if direction in ['W', 'S']:
            decimal_degrees = -abs(decimal_degrees)
        
        return decimal_degrees
    
    @staticmethod
    def get_input(prompt):
        return input(prompt)
