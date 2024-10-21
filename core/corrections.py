from .degree import Degree

class Correction(Degree):
    """Represents a correction in degrees."""
    def __init__(self, value):
        super().__init__(value)
        if not (-0.5 <= self.raw_decimal <= 2):
            raise ValueError(f"Correction value must be between -0.5° and 2°, but got {value}")

class CorrectionMonthly(Correction):
    """Represents a monthly correction in degrees."""
    def __init__(self, value):
        super().__init__(value)
        if not (-0.5 <= self.raw_decimal <= 0.5):
            raise ValueError(f"Monthly correction must be between -0.5° and 0.5°, but got {value}")

class CorrectionDIP(Correction):
    """Represents a monthly correction in degrees."""
    def __init__(self, value):
        super().__init__(value)
        if not (0 <= self.raw_decimal <= 1.0):
            raise ValueError(f"DIP correction must be between 0° and 1°, but got {value}")

class CorrectionSum(Correction):
    """Represents the sum of all corrections in degrees."""
    def __init__(self, correction_monthly:CorrectionMonthly, correction_dip:CorrectionDIP):
        super().__init__(correction_monthly.decimal + correction_dip.decimal)
    def __str__(self):
        return f"Correction Sum: {self.string}"
