import unittest
from core.latitude import Latitude
from core.longitude import Longitude
from core.degree import Degree

class TestDegreeConversion(unittest.TestCase):

    def test_latitude_north(self):
        lat = Latitude(51.5074)  # Latitude of London
        self.assertEqual(str(lat), "51°30'26.64\"N", "Failed for Latitude (North)")

    def test_latitude_south(self):
        lat = Latitude(-34.6037)  # Latitude of Buenos Aires
        self.assertEqual(str(lat), "34°36'13.32\"S", "Failed for Latitude (South)")

    def test_longitude_east(self):
        lon = Longitude(2.3522)  # Longitude of Paris
        self.assertEqual(str(lon), "2°21'7.92\"E", "Failed for Longitude (East)")

    def test_longitude_west(self):
        lon = Longitude(-74.0060)  # Longitude of New York
        self.assertEqual(str(lon), "74°0'21.60\"W", "Failed for Longitude (West)")

    def test_degree_no_direction(self):
        degree = Degree(45.1234)  # Generic degree without direction
        self.assertEqual(str(degree), "45°7'24.24\"", "Failed for Degree without direction")

if __name__ == '__main__':
    unittest.main()
