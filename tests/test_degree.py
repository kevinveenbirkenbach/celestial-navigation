import unittest
from core.degree import Degree

class TestDegree(unittest.TestCase):

    def test_normalize_angle_below_360(self):
        # Test when the angle is already less than 360
        degree = Degree(270)
        self.assertEqual(degree.decimal, 270, "Failed to handle angle below 360")

    def test_normalize_angle_above_360(self):
        # Test when the angle is more than 360
        degree = Degree(450)  # 450 should normalize to 90
        self.assertEqual(degree.decimal, 90, "Failed to normalize angle above 360")

    def test_normalize_angle_above_multiple_of_360(self):
        # Test when the angle is a multiple of 360
        degree = Degree(720)  # 720 should normalize to 0
        self.assertEqual(degree.decimal, 0, "Failed to normalize angle that is a multiple of 360")

    def test_normalize_angle_negative(self):
        # Test when the angle is negative
        degree = Degree(-90)  # -90 is still -90 after normalization (depending on requirements)
        self.assertEqual(degree.decimal, -90, "Failed to handle negative angle correctly")

    def test_string_to_decimal_conversion(self):
        # Test string to decimal conversion (D°M'S" format)
        degree = Degree("120°30'30\"")
        self.assertAlmostEqual(degree.decimal, 120.5083, places=4, msg="Failed to convert string to decimal")

    def test_decimal_to_ddmmss(self):
        # Test decimal to D°M'S" format
        degree = Degree(45.7625)
        self.assertEqual(str(degree), "045°45'45.00\"", "Failed to convert decimal to D°M'S\" format")

    def test_invalid_string_format(self):
        # Test invalid string format
        with self.assertRaises(ValueError):
            Degree("invalid string")

    def test_type_error_for_invalid_type(self):
        # Test for invalid type passed to constructor
        with self.assertRaises(TypeError):
            Degree(["invalid", "type"])  # List should raise a TypeError

    def test_normalize_angle_multiple_rounding(self):
        # Test if normalization works with multiple rounds of subtraction
        degree = Degree(1080)  # 1080 should normalize to 0
        self.assertEqual(degree.decimal, 0, "Failed to normalize large angle with multiple 360 subtractions")
    
    def test_degree_no_direction(self):
        degree = Degree(45.1234)  # Generic degree without direction
        self.assertEqual(str(degree), "045°07'24.24\"", "Failed for Degree without direction")
if __name__ == '__main__':
    unittest.main()
