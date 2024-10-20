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

    @staticmethod
    def ensure_two_digit_degrees(degree_str: str) -> str:
        """
        Ensure the degree part of a string in D°M'S" format is exactly two digits.
        Removes leading zero if degrees are three digits and adds leading zero if necessary.
        """
        # Find the position of the degree symbol
        degree_symbol_pos = degree_str.find("°")
        
        # Extract the degrees part (everything before the degree symbol)
        degrees_part = degree_str[:degree_symbol_pos]

        # If the degrees part is three digits, remove the first character
        if len(degrees_part) == 3:
            degrees_two_digits = degrees_part[1:]
        # If the degrees part is one digit, add a leading zero
        elif len(degrees_part) == 1:
            degrees_two_digits = '0' + degrees_part
        else:
            degrees_two_digits = degrees_part

        # Return the modified string, replacing the degrees part with exactly two digits
        return degrees_two_digits + degree_str[degree_symbol_pos:]
