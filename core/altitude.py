from .degree import Degree
from .index_error import IndexError
from .corrections import CorrectionSum
class Altitude(Degree):
    """
    Represents an Altitude value in degrees.
    
    More information:
    -  https://rhetos.de/html/lex/altitude_(astronomie).htm
    """

class AltitudeSextant(Altitude):
    """Represents an Sextant Altitude value in degrees."""
    def __str__(self):
        return f"Sextant Altitude (SA): {self.string}"
        
class AltitudeObserved(Altitude):
    def __init__(self, altitude_sextant: AltitudeSextant, index_error: IndexError):
        super().__init__(altitude_sextant.decimal + index_error.decimal)
    def __str__(self):
        return f"Observed Altitude (OA): {self.string}"

class AltitudeTrue(Altitude):
    def __init__(self, *args):
        if len(args) == 1:
            """TRUE ALTITUDE GIVEN"""
            altitude_true_decimal = args[0]
        elif len(args) == 2:
            """TRUE ALTITUDE CALCULATED"""
            altitude_sextant_decimal = args[0]
            correction_sum_decimal= args[1]
            altitude_true_decimal = altitude_sextant_decimal + correction_sum_decimal
        else:
            raise TypeError(f"Expected 1 or 2 arguments, but got {len(args)}")
        super().__init__(altitude_true_decimal)
    def __str__(self):
        return f"True Altitude (TA): {self.string}"
