from .degree import Degree
class Correction(Degree):
    pass
class ObservedAltitudeCorrection(Correction):
    """Represents the sum of all corrections in degrees."""
    def __init__(self, *args):
        if len(args) == 2:
            correction_monthly = args[0]
            correction_dip = args[1]
            if not (isinstance(correction_monthly, ObservedAltitudeCorrectionMonthly) and isinstance(correction_dip, ObservedAltitudeCorrectionDIP) ):
                raise TypeError(f"Wrong parameters passed. Expected {opperant_one_instance} and {opperant_two_instance}. Got {args}.")
            correction = correction_monthly + correction_dip
        elif len(args) == 1:
            correction = args[0]
        else:
            raise TypeError(f"Expected 1 or 2 arguments, but got {len(args)}.")
        super().__init__(correction)
        if not (-0.5 <= self.raw_decimal <= 2):
            raise ValueError(f"Correction value must be between -0.5° and 2°, but got {correction}")        
    def __str__(self):
        return f"{self.string}"
class ObservedAltitudeCorrectionMonthly(ObservedAltitudeCorrection):
    """Represents a monthly correction in degrees."""
    def __init__(self, value):
        super().__init__(value)
        if not (-0.5 <= self.raw_decimal <= 0.5):
            raise ValueError(f"Monthly correction must be between -0.5° and 0.5°, but got {value}")

class ObservedAltitudeCorrectionDIP(ObservedAltitudeCorrection):
    """Represents a monthly correction in degrees."""
    def __init__(self, value):
        super().__init__(value)
        if not (0 <= self.raw_decimal <= 1.0):
            raise ValueError(f"DIP correction must be between 0° and 1°, but got {value}")

class ApparentAltitudeCorrection(Correction):
    pass