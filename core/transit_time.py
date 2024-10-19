from datetime import timedelta
from .helper import Helper
from .longitude import Longitude

class TransitTime:
    def __init__(self, longitude: Longitude, transit_greenwich_str):
        self.estimated_longitude = longitude.decimal
        self.transit_greenwich = TransitTime.parse_time_input(transit_greenwich_str)
        self.arc_to_time_decimal =  self.calculate_arc_to_time()
        self.arc_to_time_string =   self.get_arc_to_time_string()
        self.transit_time_at_ep =   self.calculate_transit_time_at_ep()

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

    def calculate_arc_to_time(self):
        """Calculate arc to time from longitude."""
        return self.estimated_longitude * 4  # Longitude in degrees to time in minutes (4 min per degree)

    def calculate_transit_time_at_ep(self):
        """Calculate the transit time at estimated position (EP)."""
        arc_to_time = self.calculate_arc_to_time()
        arc_to_time_delta = timedelta(minutes=arc_to_time)

        if self.estimated_longitude < 0:  # West longitude, subtract arc to time
            transit_ep = self.transit_greenwich - arc_to_time_delta
        else:  # East longitude, add arc to time
            transit_ep = self.transit_greenwich + arc_to_time_delta

        return transit_ep

    def get_arc_to_time_string(self):
        """Calculate arc to time from longitude."""
        arc_to_time_delta = timedelta(minutes=self.calculate_arc_to_time())
        
        # Converting timedelta to hours, minutes, and seconds
        total_seconds = int(arc_to_time_delta.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Return arc to time in hh:mm:ss format
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def __str__(self):
        return f"ARC to time: {self.arc_to_time_string} \nTransit Time at EP: {self.transit_time_at_ep}"
