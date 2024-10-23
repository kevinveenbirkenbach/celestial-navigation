import unittest
from core.degree import Degree

class TestDegree(unittest.TestCase):

    def test_invalid_direction(self):
        invalid_inputs = [
            "37°49.3'S",  # South
            "37°49.3'E",  # East
            "37°49.3'W",  # West
            "37°49.3'N"   # North
        ]
        
        for input_str in invalid_inputs:
            with self.assertRaises(ValueError, msg=f"ValueError not raised for {input_str}"):
                Degree(input_str)

    def test_string_float(self):
        degree = Degree("270.123")
        self.assertEqual(degree.decimal, 270.123, "Failed to handle string with float")

    def test_string_negative_float(self):
        degree = Degree("-270.123")
        self.assertEqual(degree.decimal, -270.123, "Failed to handle string with float")

    def test_string_int(self):
        degree = Degree("271")
        self.assertEqual(degree.decimal, 271, "Failed to handle string with float")

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

    def test_degree_initialization(self):
        degree = Degree(45.5)
        self.assertEqual(degree.decimal, 45.5)
        self.assertEqual(str(degree), "045°30'00.00\"")

    def test_degree_addition(self):
        degree1 = Degree(45.5)
        degree2 = Degree(30.25)
        result = degree1 + degree2
        self.assertEqual(result.decimal, 75.75)
        self.assertEqual(str(result), "075°45'00.00\"")

    def test_degree_subtraction(self):
        degree1 = Degree(45.5)
        degree2 = Degree(30.25)
        result = degree1 - degree2
        self.assertEqual(result.decimal, 15.25)
        self.assertEqual(str(result), "015°15'00.00\"")

    def test_positive_degree(self):
        degree = Degree("37°49.3'")
        self.assertAlmostEqual(degree.decimal, 37.82166667, places=6, msg="Positive degree conversion failed")
        self.assertEqual(str(degree), "037°49'18.00\"", "Positive degree string format failed")
    
    def test_negative_degree(self):
        degree = Degree("-37°49.3'")
        self.assertAlmostEqual(degree.decimal, -37.82166667, places=6, msg="Negative degree conversion failed")
        self.assertEqual(str(degree), "-037°49'18.00\"", "Negative degree string format failed")
    
##
    def test_zero_degree(self):
        degree = Degree("00°00.0'")
        self.assertAlmostEqual(degree.decimal, 0.0, places=6, msg="Zero degree conversion failed")
        self.assertEqual(str(degree), "000°00'00.00\"", "Zero degree string format failed")
    
    def test_add_degrees(self):
        degree1 = Degree("37°49.3'")
        degree2 = Degree("2°30.0'")
        result = degree1 + degree2
        self.assertAlmostEqual(result.decimal, 40.32166667, places=6, msg="Addition of degrees failed")
        self.assertEqual(str(result), "040°19'18.00\"", "Addition result string format failed")
    
    def test_subtract_degrees(self):
        degree1 = Degree("37°49.3'")
        degree2 = Degree("2°30.0'")
        result = degree1 - degree2
        self.assertAlmostEqual(result.decimal, 35.32166667, places=6, msg="Subtraction of degrees failed")
        self.assertEqual(str(result), "035°19'18.00\"", "Subtraction result string format failed")
    
    def test_multiply_degree_by_scalar(self):
        degree = Degree("37°49.3'")
        result = degree * 2
        self.assertAlmostEqual(result.decimal, 75.64333333, places=6, msg="Multiplication by scalar failed")
        self.assertEqual(str(result), "075°38'36.00\"", "Multiplication result string format failed")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            Degree("Invalid input")

    def test_zero_division_error(self):
        degree = Degree("37°49.3'")
        with self.assertRaises(ZeroDivisionError):
            result = degree / 0

if __name__ == '__main__':
    unittest.main()
