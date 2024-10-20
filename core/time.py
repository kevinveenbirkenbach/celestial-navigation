from datetime import timedelta, datetime, timezone
from .helper import Helper
from .longitude import Longitude
from .degree import Degree

class UTCDatetime:
    def __init__(self, input_datetime):
        # Check if the input is already a datetime object
        if isinstance(input_datetime, datetime):
            # If the datetime object has a timezone, convert to UTC using astimezone()
            if input_datetime.tzinfo is not None:
                self.datetime = input_datetime.astimezone(timezone.utc)
            else:
                # If no timezone info, assume it's a naive datetime and set it to UTC
                self.datetime = input_datetime.replace(tzinfo=timezone.utc)
        # Check if the input is a string
        elif isinstance(input_datetime, str):
            try:
                # Parse the string using the format YYYY-MM-DDTHH:MM:SS
                datetime_parsed = datetime.strptime(input_datetime, "%Y-%m-%dT%H:%M:%S")
                # Set the timezone to UTC
                self.datetime = datetime_parsed.replace(tzinfo=timezone.utc)
            except ValueError:
                raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DDTHH:MM:SS' but got {input_datetime}")
        else:
            raise TypeError(f"The value '{input_datetime}' is of the wrong type: {type(input_datetime).__name__}.")

    def __str__(self):
        # Return the datetime in ISO 8601 format (in UTC)
        return self.datetime.isoformat()

class ArcToTime(timedelta):
    def __new__(cls, longitude: Longitude):
        # Calculate the total minutes corresponding to the longitude
        minutes = longitude.decimal * 4
        
        # Create the new timedelta object (using the super call for timedelta)
        return super().__new__(cls, minutes=minutes)
    
    @staticmethod
    def get_arc_to_time_string(arc_to_time_delta: timedelta):
        """Return arc to time as a string in hh:mm:ss format."""
        # Converting timedelta to hours, minutes, and seconds
        total_seconds = int(arc_to_time_delta.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        # Return arc to time in hh:mm:ss format
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    
    def __str__(self):
        # Use the custom string representation for timedelta
        return ArcToTime.get_arc_to_time_string(self)

class TransitTime(UTCDatetime):
    def __init__(self, arc_to_time: ArcToTime, transit_time_greenwich: UTCDatetime):
        transit_time_at_longitude = transit_time_greenwich.datetime - arc_to_time
        return super().__init__(transit_time_at_longitude)
