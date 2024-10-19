from .helper import Helper

class Altitude:
    def __init__(self, sextant_altitude_str, index_error, monthly_correction):
        self.sextant_altitude = Helper.parse_dms(sextant_altitude_str)  # Eingabe in DMS, Umwandlung in Dezimalgrad
        self.index_error = index_error
        self.monthly_correction = monthly_correction

        # Calculate observed altitude
        self.observed_altitude = self.calculate_observed_altitude()

    def calculate_observed_altitude(self):
        """Calculate the observed altitude."""
        return self.sextant_altitude + self.index_error

    def calculate_total_correction(self):
        """Calculate the total correction."""
        return self.index_error + self.monthly_correction

    def calculate_true_altitude(self):
        """Calculate the true altitude."""
        total_correction = self.calculate_total_correction()
        return self.observed_altitude + total_correction
