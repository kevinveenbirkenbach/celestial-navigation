import unittest
from core.corrections import AltitudeCorrectionMonthly, AltitudeCorrectionDIP, AltitudeCorrection

class TestMonthlyCorrections(unittest.TestCase):
    def test_negative_monthly_correction(self):
        # Test for a valid negative monthly correction
        correction_monthly = AltitudeCorrectionMonthly(-0.2)
        self.assertEqual(correction_monthly.decimal, -0.2, "Failed to set correct negative monthly correction value")
        self.assertEqual(str(correction_monthly), "-000°12'00.00\"", "String representation is incorrect for negative value")

    def test_invalid_monthly_correction_out_of_bounds(self):
        # Test for an invalid monthly correction (out of bounds, too negative)
        with self.assertRaises(ValueError):
            AltitudeCorrectionMonthly(-0.6)  # Should raise ValueError because it's less than -0.5

class TestCorrections(unittest.TestCase):

    def test_valid_correction(self):
        # Test for a valid general correction
        correction = AltitudeCorrection(1.5)
        self.assertEqual(correction.decimal, 1.5, "Failed to set correct correction value")
        self.assertEqual(str(correction), "001°30'00.00\"", "String representation is incorrect")

    def test_invalid_correction(self):
        # Test for an invalid correction (out of bounds)
        with self.assertRaises(ValueError):
            AltitudeCorrection(2.5)  # Should raise ValueError because it's greater than 2

    def test_negative_outof_scope_correction(self):
        # Test for a negative correction (should raise an error)
        with self.assertRaises(ValueError):
            AltitudeCorrection(-1)  # Should raise ValueError because it's less than 0

class TestAltitudeCorrectionDIP(unittest.TestCase):
    def test_valid_dip_correction(self):
        # Test for a valid DIP correction
        correction_dip = AltitudeCorrectionDIP(0.8)
        self.assertEqual(correction_dip.decimal, 0.8, "Failed to set correct DIP correction value")
        self.assertEqual(str(correction_dip), "000°48'00.00\"", "String representation is incorrect")

    def test_invalid_dip_correction(self):
        # Test for an invalid DIP correction (out of bounds)
        with self.assertRaises(ValueError):
            AltitudeCorrectionDIP(1.5)  # Should raise ValueError because it's greater than 1.0

    def test_negative_dip_correction(self):
        # Test for a negative DIP correction (should raise an error)
        with self.assertRaises(ValueError):
            AltitudeCorrectionDIP(-0.2)  # Should raise ValueError because it's less than 0

class TestAltitudeCorrection(unittest.TestCase):

    def test_valid_correction_sum(self):
        # Test for a valid correction sum (monthly + DIP)
        correction_monthly = AltitudeCorrectionMonthly(0.2)
        correction_dip = AltitudeCorrectionDIP(0.5)
        correction_sum = AltitudeCorrection(correction_monthly, correction_dip)
        self.assertEqual(correction_sum.decimal, 0.7, "Failed to calculate correct correction sum")
        self.assertEqual(correction_sum.string, "000°42'00.00\"", "String representation is incorrect")

    def test_negative_correction_sum(self):
        correction_monthly = AltitudeCorrectionMonthly(-0.1)  # Monthly correction is negative
        correction_dip = AltitudeCorrectionDIP(0.3)
        correction_sum = AltitudeCorrection(correction_monthly, correction_dip)
        self.assertAlmostEqual(correction_sum.decimal, 0.2, places=7, msg="Failed to calculate correct correction sum")

if __name__ == '__main__':
    unittest.main()
