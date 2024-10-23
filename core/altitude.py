from .degree import Degree
from .index_error import IndexError
from .corrections import ObservedAltitudeCorrection, ApparentAltitudeCorrection
from .helper import Helper

class Altitude(Degree):
    """
    Represents an Altitude value in degrees.
    
    More information:
    -  https://rhetos.de/html/lex/altitude_(astronomie).htm
    """
    def __init__(self, value):
        super().__init__(value)
        if not (0 <= self.raw_decimal <= 90):
            raise ValueError(f"Altitude must be between 0° and 90°, but got {value}")
        self.string = Helper.ensure_two_digit_degrees(self.string)

class AltitudeSextant(Altitude):
    pass
        
class AltitudeObserved(Altitude):
    def __init__(self, altitude_sextant: AltitudeSextant, index_error: IndexError):
        super().__init__(altitude_sextant + index_error)

class AltitudeApperant(Altitude):
    def __init__(self, *args):
        super().__init__(Helper.delta(AltitudeObserved,ObservedAltitudeCorrection, True, *args))

class AltitudeTrue(Altitude):
    def __init__(self, *args):
        super().__init__(Helper.delta(AltitudeApperant,ApparentAltitudeCorrection, True, *args))
