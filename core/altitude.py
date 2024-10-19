from .degree import Degree
from .index_error import IndexError
from .corrections import CorrectionSum
class Altitude(Degree):
    """Represents an Altitude value in degrees."""

class AltitudeSextant(Altitude):
    """Represents an Sextant Altitude value in degrees."""

class AltitudeObserved(Altitude):
    def __init__(self, altitude_sextant: AltitudeSextant, index_error: IndexError):
        super.__init__(altitude_sextant.decimal + index_error.decimal)

class AltitudeTrue(Altitude):
    def __init__(self, altitude_sextant: AltitudeSextant, correction_sum: CorrectionSum):
        super.__init__(altitude_sextant.decimal - correction_sum.decimal)
