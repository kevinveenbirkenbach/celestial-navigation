import re
from datetime import timedelta

class Helper:
    @staticmethod
    def parse_dms(input_str):
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
    def parse_time_input(time_str):
        """Parse time input in hh:mm or hh:mm:ss format and return a timedelta object."""
        try:
            # Split the input based on the colon separator
            parts = list(map(int, time_str.split(':')))

            if len(parts) == 2:  # Format: hh:mm
                hh, mm = parts
                ss = 0  # Default to zero seconds if not provided
            elif len(parts) == 3:  # Format: hh:mm:ss
                hh, mm, ss = parts
            else:
                raise ValueError("Invalid time format. Use hh:mm or hh:mm:ss format.")
            
            return timedelta(hours=hh, minutes=mm, seconds=ss)
        except ValueError:
            raise ValueError("Invalid time format. Use hh:mm or hh:mm:ss format.")
    
    @staticmethod
    def get_input(prompt):
        return input(prompt)
