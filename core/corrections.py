from .degree import Degree

class Correction(Degree):
    """Represents a correction in degrees."""

class CorrectionMonthly(Correction):
    """Represents a monthly correction in degrees."""

class CorrectionDIP(Correction):
    """Represents a monthly correction in degrees."""

class CorrectionSum(Correction):
    """Represents the sum of all corrections in degrees."""
    def __init__(self, correction_monthly:CorrectionMonthly, correction_dip:CorrectionDIP):
        super().__init__(correction_monthly.decimal + correction_dip.decimal)
    def __str__(self):
        return f"Correction Sum: {self.string}"
