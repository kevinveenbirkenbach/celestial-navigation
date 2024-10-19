from .helper import Helper

class CelestialNavigation:
    def __init__(self, sextant_altitude_str, index_error, monthly_correction, declination_str):
        self.sextant_altitude = Helper.parse_dms(sextant_altitude_str)  # Eingabe in DMS, Umwandlung in Dezimalgrad
        self.index_error = index_error
        self.monthly_correction = monthly_correction
        self.declination = Helper.parse_dms(declination_str)  # Deklination in DMS, Umwandlung in Dezimalgrad

        # Calculating observed altitude
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

    def calculate_latitude(self):
        """Calculate the latitude using declination and true altitude (ZD = 90° - TA)."""
        true_altitude = self.calculate_true_altitude()
        ZD = 90 - true_altitude
        if self.declination > true_altitude:
            return ZD + self.declination
        else:
            return self.declination - ZD
