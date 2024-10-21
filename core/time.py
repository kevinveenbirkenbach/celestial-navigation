from datetime import timedelta, datetime, timezone
from .helper import Helper
from .longitude import Longitude
from .degree import Degree

from datetime import datetime, timezone

from datetime import datetime, timezone

class UTCDatetime(datetime):
    def __new__(cls, input_datetime):
        # Check if the input is already a datetime object
        if isinstance(input_datetime, datetime):
            # If the datetime object has a timezone, convert to UTC using astimezone()
            if input_datetime.tzinfo is not None:
                datetime_utc = input_datetime.astimezone(timezone.utc)
            else:
                # If no timezone info, assume it's a naive datetime and set it to UTC
                datetime_utc = input_datetime.replace(tzinfo=timezone.utc)
        # Check if the input is a string
        elif isinstance(input_datetime, str):
            try:
                # Parse the string using the format YYYY-MM-DDTHH:MM:SS
                datetime_parsed = datetime.strptime(input_datetime, "%Y-%m-%dT%H:%M:%S")
                # Set the timezone to UTC
                datetime_utc = datetime_parsed.replace(tzinfo=timezone.utc)
            except ValueError:
                raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DDTHH:MM:SS' but got {input_datetime}")
        else:
            raise TypeError(f"The value '{input_datetime}' is of the wrong type: {type(input_datetime).__name__}.")

        # Return the new UTC datetime instance
        return datetime_utc

    def __str__(self):
        # Return the datetime in ISO 8601 format (in UTC)
        return self.isoformat()

class ArcToTime(timedelta):
    def __new__(cls, longitude: Longitude):
        # Calculate the total minutes corresponding to the longitude
        minutes = abs(longitude.decimal) * 4
        
        # Handle West longitude (subtract time)
        if "W" in longitude.string:
            minutes = -minutes
        
        # Create the new timedelta object
        return super().__new__(cls, minutes=minutes)
    
    @staticmethod
    def get_arc_to_time_string(arc_to_time_delta: timedelta):
        """Return arc to time as a string in hh:mm:ss format."""
        total_seconds = int(arc_to_time_delta.total_seconds())
        hours, remainder = divmod(abs(total_seconds), 3600)
        minutes, seconds = divmod(remainder, 60)

        # Handle negative hours
        sign = "-" if total_seconds < 0 else ""

        # Return arc to time in hh:mm:ss format with leading zeros
        return f"{sign}{hours:02}:{minutes:02}:{seconds:02}"
    
    def __str__(self):
        return ArcToTime.get_arc_to_time_string(self)

class TransitTime(UTCDatetime):
    def __new__(cls, arc_to_time: timedelta, transit_time_greenwich: UTCDatetime):
        # Add the time offset for East longitudes (positive arc_to_time)
        # Subtract the time offset for West longitudes (negative arc_to_time)
        transit_time_at_longitude = transit_time_greenwich + arc_to_time
        
        # Create a new UTCDatetime instance with the calculated time
        return super().__new__(cls, transit_time_at_longitude)

