import unittest
from core.altitude import AltitudeSextant, AltitudeObserved, AltitudeTrue
from core.corrections import CorrectionDIP, CorrectionMonthly, CorrectionSum
from core.index_error import IndexError

class TestAltitudeCalculation(unittest.TestCase):

    def test_altitude_calculation(self):
        # Input values
        sextant_altitude = AltitudeSextant("77°00'")
        index_error = IndexError("00°00'")
        dip_correction = CorrectionDIP("00°12.7'")
        monthly_correction = CorrectionMonthly("00°00.1'")

        # Expected values
        expected_observed_altitude = "Observed Altitude (OA): 77°0'0.00\""
        expected_correction_sum = "Correction Sum: 0°12'48.00\""
        expected_true_altitude = "True Altitude (TA): 77°12'48.00\""

        # Calculating the observed altitude (OA)
        observed_altitude = AltitudeObserved(sextant_altitude, index_error)
        self.assertEqual(str(observed_altitude), expected_observed_altitude, "Error in calculating observed altitude (Observed Altitude)")

        # Corrections (DIP + Monthly)
        correction_sum = CorrectionSum(monthly_correction, dip_correction)
        self.assertEqual(str(correction_sum), expected_correction_sum, "Error in calculating the total correction (Correction Sum)")

        # Calculating the true altitude (TA)
        true_altitude = AltitudeTrue(sextant_altitude, correction_sum)
        self.assertEqual(str(true_altitude), expected_true_altitude, "Error in calculating true altitude (True Altitude)")

if __name__ == '__main__':
    unittest.main()
