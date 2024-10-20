import unittest
from core.longitude import Longitude

class TestLongitude(unittest.TestCase):

    def test_longitude_east(self):
        """Test a valid longitude in the eastern hemisphere."""
        lon = Longitude(2.3522)  # Longitude of Paris
        self.assertEqual(str(lon), "002°21'07.92\"E", "Failed for Longitude (East)")

    def test_longitude_west(self):
        """Test a valid longitude in the western hemisphere."""
        lon = Longitude(-74.0060)  # Longitude of New York
        self.assertEqual(str(lon), "074°00'21.60\"W", "Failed for Longitude (West)")

    def test_longitude_zero(self):
        """Test the longitude at the prime meridian (0°)."""
        lon = Longitude(0.0)
        self.assertEqual(str(lon), "000°00'00.00\"E", "Failed for Longitude (Prime Meridian)")

    def test_longitude_negative_zero(self):
        """Test that negative zero longitude also returns as 0°E."""
        lon = Longitude(-0.0)
        self.assertEqual(str(lon), "000°00'00.00\"E", "Failed for Longitude (Negative Zero)")

    def test_longitude_max_positive(self):
        """Test the maximum valid positive longitude (180°E)."""
        lon = Longitude(180.0)
        self.assertEqual(str(lon), "180°00'00.00\"E", "Failed for Longitude (Maximum Positive)")

    def test_longitude_max_negative(self):
        """Test the maximum valid negative longitude (-180°W)."""
        lon = Longitude(-180.0)
        self.assertEqual(str(lon), "180°00'00.00\"W", "Failed for Longitude (Maximum Negative)")

    def test_invalid_longitude_positive(self):
        """Test that an invalid longitude greater than 180° raises a ValueError."""
        with self.assertRaises(ValueError):
            Longitude(181.0)

    def test_invalid_longitude_negative(self):
        """Test that an invalid longitude less than -180° raises a ValueError."""
        with self.assertRaises(ValueError):
            Longitude(-181.0)

    def test_longitude_with_decimal_precision(self):
        """Test a longitude value with high decimal precision."""
        lon = Longitude(123.456789)
        self.assertEqual(str(lon), "123°27'24.44\"E", "Failed for Longitude with decimal precision")

    def test_longitude_edge_case_rounding(self):
        """Test longitude with rounding edge case for seconds."""
        lon = Longitude(120.999999)
        self.assertEqual(str(lon), "121°00'00.00\"E", "Failed for Longitude with rounding edge case")

if __name__ == '__main__':
    unittest.main()
