import unittest
from core.latitude import Latitude
from core.helper import Helper
from core.degree import Degree

class TestLatitude(unittest.TestCase):
    def test_latitude_north(self):
        lat = Latitude(51.5074)  # Latitude of London
        self.assertEqual(str(lat), "51°30'26.64\"N", "Failed for Latitude (North)")

    def test_latitude_south(self):
        lat = Latitude(-34.6037)  # Latitude of Buenos Aires
        self.assertEqual(str(lat), "34°36'13.32\"S", "Failed for Latitude (South)")

    def test_valid_latitude_north(self):
        # Test a valid latitude in the northern hemisphere
        latitude = Latitude(45.1234)
        self.assertEqual(latitude.decimal, 45.1234)
        self.assertEqual(str(latitude), "45°07'24.24\"N", "Failed for valid northern latitude.")

    def test_valid_latitude_south(self):
        # Test a valid latitude in the southern hemisphere
        latitude = Latitude(-30.5678)
        self.assertEqual(latitude.decimal, -30.5678)
        self.assertEqual(str(latitude), "30°34'04.08\"S", "Failed for valid southern latitude.")

    def test_latitude_zero(self):
        # Test the equator (latitude 0°)
        latitude = Latitude(0)
        self.assertEqual(latitude.decimal, 0)
        self.assertEqual(str(latitude), "00°00'00.00\"N", "Failed for latitude at equator.")

    def test_invalid_latitude_above_90(self):
        # Test for latitude greater than 90° (invalid)
        with self.assertRaises(ValueError):
            Latitude(95)

    def test_invalid_latitude_below_negative_90(self):
        # Test for latitude less than -90° (invalid)
        with self.assertRaises(ValueError):
            Latitude(-95)

    def test_latitude_conversion_to_string(self):
        # Test conversion of decimal degrees to string format (N/S direction)
        latitude = Latitude(45.9876)
        self.assertEqual(str(latitude), "45°59'15.36\"N", "Failed for conversion of decimal degrees to string.")

    def test_negative_latitude_conversion_to_string(self):
        # Test conversion of negative decimal degrees to string format (S direction)
        latitude = Latitude(-45.9876)
        self.assertEqual(str(latitude), "45°59'15.36\"S", "Failed for conversion of negative decimal degrees to string.")

if __name__ == '__main__':
    unittest.main()
