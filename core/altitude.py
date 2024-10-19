from .degree import Degree
from .index_error import IndexError
from .corrections import CorrectionSum
class Altitude(Degree):
    """Represents an Altitude value in degrees."""

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
    def __init__(self, altitude_sextant: AltitudeSextant, correction_sum: CorrectionSum):
        super().__init__(altitude_sextant.decimal + correction_sum.decimal)
    def __str__(self):
        return f"True Altitude (TA): {self.string}"
