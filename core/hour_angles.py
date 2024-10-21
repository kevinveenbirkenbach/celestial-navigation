from .degree import Degree
from .longitude import Longitude
from .time import UTCDatetime

class Increment(Degree):
    pass

class HourAngle(Degree):
    """
    Represents an Hour Angel in degrees.
    https://en.wikipedia.org/wiki/Hour_angle
    """
    #def __init__(self, value):
    #    super().__init__(value)
    #    if not (-180 <= self.raw_decimal <= 180):
    #        raise ValueError(f"Hour Angel must be between -180° and 180°, but got {value}")
    #    self.string = Longitude.decimal_to_ddmmss(self.decimal)

class GreenwhichHourAngle(HourAngle):
    """
    https://www.navathome.com/ocean2/osection8/aries/aries.aspx
    """
    def __init__(self, value, time: UTCDatetime):
        super().__init__(value)
        self.time = time
    
    @staticmethod
    def new_interpolated_gha(gha_1,gha_2, star_sight_time: UTCDatetime):
        delta_degree = abs(gha_1.decimal - gha_2.decimal)
        delta_time_seconds = abs((gha_1.time - gha_2.time).total_seconds())
        change_degree_per_seconds = delta_degree / delta_time_seconds
        if gha_1.time >= star_sight_time:
            degree_decimal = gha_1.decimal - ((gha_1.time - star_sight_time).total_seconds()*change_degree_per_seconds)
        else:
            degree_decimal = gha_1.decimal + ((star_sight_time - gha_1.time).total_seconds()*change_degree_per_seconds)
        return GreenwhichHourAngle(degree_decimal,star_sight_time)



#class GreenwhichHourAngleAries:

class LocaleHourAngle(HourAngle):
    def __init__(self, greenwhich_hour_angle: GreenwhichHourAngle, longitude: Longitude):
        locale_hour_angel = greenwhich_hour_angle.decimal + longitude.decimal
        super().__init__(locale_hour_angel)

class SiderealhourAngle:
    pass