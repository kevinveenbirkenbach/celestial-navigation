import unittest
from core.corrections import ObservedAltitudeCorrectionDIP, ObservedAltitudeCorrectionMonthly, ObservedAltitudeCorrection, ApparentAltitudeCorrection
from core.index_error import IndexError
from core.altitude import Altitude, AltitudeSextant, AltitudeObserved, AltitudeTrue, AltitudeApperant
from core.degree import Degree

class TestAltitudeObserved(unittest.TestCase):
    def test_observed_altitude(self):
        # Test Observed Altitude, which adds index error to sextant altitude
        altitude_sextant = AltitudeSextant(50)
        index_error = IndexError(1.5)  # Small index error
        observed_altitude = AltitudeObserved(altitude_sextant, index_error)
        self.assertEqual(observed_altitude.decimal, 51.5)
        self.assertEqual(str(observed_altitude), "51°30'00.00\"", "Failed for Observed Altitude.")

    def test_altitude_calculation(self):
        # Convert the string to decimal degrees
        sextant_altitude_decimal = Degree("77°00'").decimal  # Using Degree class to parse the string

        # Pass the decimal value to AltitudeSextant
        sextant_altitude = AltitudeSextant(sextant_altitude_decimal)
        index_error = IndexError(0.0)  # No index error

        observed_altitude = AltitudeObserved(sextant_altitude, index_error)
        self.assertEqual(str(observed_altitude), "77°00'00.00\"", "Failed for observed altitude calculation")

    def test_observed_altitude_with_negativ_index_error_str(self):
        expected_observed_altitude = "77°00'00.00\""
        sextant_altitude = AltitudeSextant("77°00.3'")
        index_error = IndexError("-00°00.3'")
        altitude_observed = AltitudeObserved(sextant_altitude,index_error)
        self.assertEqual(str(altitude_observed),expected_observed_altitude)

def test_observed_altitude_negative_indexerror(self):
        # Test Observed Altitude, which adds index error to sextant altitude
        altitude_sextant = AltitudeSextant(50)
        index_error = IndexError(-1.5)  # Small index error
        observed_altitude = AltitudeObserved(altitude_sextant, index_error)
        self.assertEqual(observed_altitude.decimal, 48.5)

class TestAltitude(unittest.TestCase):

    def test_valid_altitude(self):
        # Test for valid altitude within the range (0° - 90°)
        altitude = Altitude(45)
        self.assertEqual(altitude.decimal, 45)
        self.assertEqual(str(altitude), "45°00'00.00\"", "Failed for valid altitude.")

    def test_invalid_altitude_negative(self):
        # Test for altitude below 0°, which should raise an error
        with self.assertRaises(ValueError):
            Altitude(-5)

    def test_invalid_altitude_above_90(self):
        # Test for altitude above 90°, which should raise an error
        with self.assertRaises(ValueError):
            Altitude(95)

    def test_sextant_altitude(self):
        # Test Sextant Altitude, which is inherited from Altitude
        altitude_sextant = AltitudeSextant(30)
        self.assertEqual(str(altitude_sextant), "30°00'00.00\"", "Failed for Sextant Altitude.")

    def test_true_altitude_given(self):
        # Test True Altitude when given directly
        altitude_true = AltitudeTrue(60)
        self.assertEqual(altitude_true.decimal, 60)
        self.assertEqual(str(altitude_true), "60°00'00.00\"", "Failed for direct True Altitude.")

    def test_true_altitude_invalid_args(self):
        # Test for invalid number of arguments for True Altitude, should raise TypeError
        with self.assertRaises(TypeError):
            AltitudeTrue(1, 2, 3)
class TestAltitudeCalculation(unittest.TestCase):


    def test_altitude_calculation(self):
        # Input values
        sextant_altitude = AltitudeSextant("77°00'")
        index_error = IndexError("00°00'")
        dip_correction = ObservedAltitudeCorrectionDIP("00°12.7'")
        monthly_correction = ObservedAltitudeCorrectionMonthly("00°00.1'")
        apparant_altitude_correction = ApparentAltitudeCorrection("00°16'")

        # Expected values
        expected_observed_altitude = "77°00'00.00\""
        expected_correction_sum = "000°12'48.00\""
        expected_apparant_altitude = "77°12'48.00\""
        expected_true_altitude = "77°28'48.00\""

        # Calculating the observed altitude (OA)
        observed_altitude = AltitudeObserved(sextant_altitude, index_error)
        self.assertEqual(str(observed_altitude), expected_observed_altitude, "Error in calculating observed altitude (Observed Altitude)")

        # Corrections (DIP + Monthly)
        correction_sum = ObservedAltitudeCorrection(monthly_correction, dip_correction)
        self.assertEqual(str(correction_sum), expected_correction_sum, "Error in calculating the total correction (Correction Sum)")

        # Calculating the Apparant Altitute
        apparant_altitude = AltitudeApperant(observed_altitude,correction_sum)
        self.assertEqual(str(apparant_altitude), expected_apparant_altitude, "Error in calculating true altitude (True Altitude)")

        # Calculating the true altitude (TA)
        true_altitude = AltitudeTrue(apparant_altitude, apparant_altitude_correction)
        self.assertEqual(str(true_altitude), expected_true_altitude, "Error in calculating true altitude (True Altitude)")

if __name__ == '__main__':
    unittest.main()
