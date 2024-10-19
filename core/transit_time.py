from datetime import timedelta
from .helper import Helper

class TransitTimeCalculator:
    def __init__(self, longitude_str, transit_greenwich_str):
        self.estimated_longitude = Helper.parse_dms(longitude_str)
        self.transit_greenwich = Helper.parse_time_input(transit_greenwich_str)

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
